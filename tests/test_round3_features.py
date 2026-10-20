"""Regressões da rodada: triangular, halton, rename, filtro/CSV, API async, temas."""

import csv
import json
import time
import urllib.request

import numpy as np
import pytest

pytest.importorskip("pytestqt")


def _repo(tmp_path):
    from app.infrastructure.experiment_repository import ExperimentRepository

    return ExperimentRepository(str(tmp_path / "exp.db"))


def _populate(repo, batch, n=6):
    repo.create_batch(batch, "sampling", 1, n)
    repo.insert_result(
        batch,
        [1, 10002],
        [[float(i), float(i * 2)] for i in range(1, n + 1)],
    )


# ---------- provider triangular ----------
def test_triangular_registered_and_sampled():
    from app.domain.entities import DistributionSpec, SamplingRequest
    from app.infrastructure.distribution_registry import build_default_registry
    from app.services.sampling_service import SamplingService

    registry = build_default_registry()
    assert "triangular" in registry.provider_names()

    service = SamplingService(registry)
    request = SamplingRequest(
        var_ids=[1, 2],
        specs={
            1: DistributionSpec(
                provider="triangular",
                name="value",
                params={"low": 0, "mode": 2, "high": 4},
            ),
            2: DistributionSpec(provider="fixed", name="value", params={"value": 9}),
        },
        n_experiments=500,
        seed=11,
        strategy="monte_carlo",
    )
    result = service.run(request)
    col = np.asarray(result.matrix)[:, 0]
    assert col.min() >= 0 and col.max() <= 4
    # média teórica (0+2+4)/3 = 2; tolerância de amostra
    assert abs(col.mean() - 2.0) < 0.35


def test_triangular_validation_and_ppf():
    from app.domain.entities import DistributionSpec
    from app.infrastructure.distribution_registry import build_default_registry

    tri = build_default_registry().get_provider("triangular")
    ok = DistributionSpec(provider="triangular", name="value", params={"low": 0, "mode": 1, "high": 2})
    bad = DistributionSpec(provider="triangular", name="value", params={"low": 3, "mode": 1, "high": 2})
    incomplete = DistributionSpec(provider="triangular", name="value", params={"low": 0, "mode": 1})
    assert tri.validate(ok) == []
    assert tri.validate(bad) and "low < mode < high" in tri.validate(bad)[0]
    assert tri.validate(incomplete) and "high" in " ".join(tri.validate(incomplete))

    qs = tri.ppf(ok, np.array([0.0, 0.5, 1.0]))
    assert qs[0] == pytest.approx(0.0)
    assert qs[-1] == pytest.approx(2.0)
    assert qs[1] == pytest.approx(1.0)  # F⁻¹(mode) = média no ponto de quebra


# ---------- estrategia halton ----------
def test_halton_reproducible_and_bounded():
    from app.services.strategies.halton import HaltonStrategy

    strat = HaltonStrategy()
    assert strat.name == "halton"
    rng = np.random.default_rng(21)
    u1 = strat.generate_uniforms(64, 3, rng)
    u2 = strat.generate_uniforms(64, 3, np.random.default_rng(21))
    assert u1.shape == (64, 3)
    assert np.allclose(u1, u2)
    assert (u1 >= 0).all() and (u1 <= 1).all()
    # baixa discrepância: colunas quase uniformes (coef de variação baixo)
    assert u1[:, 0].std() < 0.4


def test_halton_registered_in_service():
    from app.domain.entities import DistributionSpec, SamplingRequest
    from app.infrastructure.distribution_registry import build_default_registry
    from app.services.sampling_service import SamplingService

    service = SamplingService(build_default_registry())
    assert "halton" in service._strategies
    result = service.run(
        SamplingRequest(
            var_ids=[1],
            specs={1: DistributionSpec(provider="fixed", name="value", params={"value": 3})},
            n_experiments=8,
            seed=2,
            strategy="halton",
        )
    )
    assert len(result.matrix) == 8
    assert np.all(np.asarray(result.matrix)[:, 0] == 3.0)


# ---------- política rename ----------
def _export(container, populated_batch, out, **kw):
    return container.batch_export_service.export(
        populated_batch["batch_id"],
        populated_batch["version_id"],
        out,
        **kw,
    )


def test_export_rename_policy(container, populated_batch):
    out = container.base_dir / "out_rename"
    manifest_1 = _export(container, populated_batch, out)
    first = sorted(manifest_1.output_dir.glob("*.dat"))[0]
    original = first.read_text(encoding="utf-8")

    manifest_2 = _export(container, populated_batch, out, overwrite=False, rename_existing=True)
    assert manifest_2.n_files == 12
    files = sorted(manifest_2.output_dir.glob("*.dat"))
    renamed = [f for f in files if f.stem.endswith("-1")]
    assert len(renamed) == 12
    # original intacto; renomeado com MESMO conteúdo (mesma versão)
    assert first.read_text(encoding="utf-8") == original
    assert first.read_text(encoding="utf-8") == renamed[0].read_text(encoding="utf-8")


def test_export_rename_finds_first_free_suffix(tmp_path):
    from app.services.batch_export_service import _next_free_path

    out = tmp_path / "dir"
    out.mkdir()
    base = out / "experimento_000001"
    base.with_suffix(".dat").write_text("x", encoding="utf-8")
    (out / "experimento_000001-1.dat").write_text("y", encoding="utf-8")
    nxt = _next_free_path(out, "experimento_{id:06d}", 1)
    assert nxt.name == "experimento_000001-2.dat"


# ---------- filtro por variável + model ----------
def test_model_var_filter(qtbot, tmp_path):
    from PySide6.QtWidgets import QApplication

    QApplication.instance() or QApplication([])
    from app.ui.models.repository_paged_model import RepositoryPagedModel

    repo = _repo(tmp_path)
    _populate(repo, "b1")
    model = RepositoryPagedModel(repo)

    assert model.columnCount() == 3  # experimento + $1 + $var2
    assert model.total_rows == 6

    model.set_var_filter(10002)
    assert model.columnCount() == 2
    assert model.shown_var_ids == [10002]
    assert model.var_filter == 10002
    headers = [model.headerData(c, __import__(
        "PySide6.QtCore", fromlist=["Qt"]
    ).Qt.Orientation.Horizontal) for c in range(model.columnCount())]
    assert headers == ["Experimento", "$var2"]

    model.set_var_filter(None)
    assert model.columnCount() == 3
    repo.close()


# ---------- export CSV paginado (puro) ----------
def test_export_experiments_csv_all_and_filtered(tmp_path):
    from app.services.experiments_export_service import export_experiments_csv

    repo = _repo(tmp_path / "sub")
    repo.create_batch("b1", "sampling", 1, 6)
    repo.insert_result(
        "b1", [1, 10002],
        [[float(i), float(i * 10)] for i in range(1, 7)],
    )

    path_all = tmp_path / "all.csv"
    n = export_experiments_csv(repo, path_all)
    assert n == 6
    with open(path_all, encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    assert rows[0] == ["experimento", "$1", "$var2"]
    assert rows[1] == ["1", "1.0", "10.0"]
    assert rows[-1] == ["6", "6.0", "60.0"]

    path_one = tmp_path / "one.csv"
    n2 = export_experiments_csv(repo, path_one, var_ids=[10002])
    assert n2 == 6
    with open(path_one, encoding="utf-8", newline="") as f:
        rows2 = list(csv.reader(f))
    assert rows2[0] == ["experimento", "$var2"]
    assert rows2[1] == ["1", "10.0"]
    repo.close()


def test_experiments_panel_combo_and_buttons(qtbot, tmp_path):
    from PySide6.QtWidgets import QApplication

    QApplication.instance() or QApplication([])
    from app.infrastructure.experiment_repository import ExperimentRepository
    from app.ui.models.repository_paged_model import RepositoryPagedModel
    from app.ui.widgets.experiments_panel import ExperimentsPanel

    repo = ExperimentRepository(str(tmp_path / "p.db"))
    _populate(repo, "bx", n=3)
    model = RepositoryPagedModel(repo)
    panel = ExperimentsPanel(model)

    combo = panel.combo_var_filter
    texts = [combo.itemText(i) for i in range(combo.count())]
    assert texts[0] == "Todas as variáveis"
    assert "$var2" in texts
    assert "Comparar selecionados…" in panel._new_button.text()
    assert panel._csv_button.text() == "Exportar CSV"
    assert panel._clear_button.text() == "Limpar tabela"

    idx = combo.findData(10002)
    combo.setCurrentIndex(idx)
    assert model.var_filter == 10002
    assert model.columnCount() == 2

    combo.setCurrentIndex(0)
    assert model.var_filter is None
    repo.close()


# ---------- API assíncrona ----------
def test_api_post_export_async_and_poll(container, populated_batch):
    from app.infrastructure.api.routes import build_api_routes
    from app.infrastructure.api.server import ApiServer

    server = ApiServer(host="127.0.0.1", port=0)
    build_api_routes(server, container.exp_repo, container.template_repo)
    server.start()
    try:
        base = f"http://127.0.0.1:{server.port}/api"
        payload = json.dumps(
            {
                "template_version_id": populated_batch["version_id"],
                "output_root": str(container.base_dir / "out_async"),
            }
        ).encode("utf-8")
        req = urllib.request.Request(
            f"{base}/batches/batch_x/export-async",
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            body = json.loads(resp.read().decode("utf-8"))
        assert body["status"] == "running"
        job_id = body["job_id"]

        deadline = time.time() + 15
        job = None
        while time.time() < deadline:
            with urllib.request.urlopen(f"{base}/jobs/{job_id}", timeout=5) as r:
                job = json.loads(r.read().decode("utf-8"))
            if job["status"] != "running":
                break
            time.sleep(0.1)
        assert job is not None and job["status"] == "done"
        assert job["n_files"] == 12

        # job desconhecido -> 404
        with pytest.raises(urllib.error.HTTPError) as exc:
            urllib.request.urlopen(f"{base}/jobs/nao-existe", timeout=5)
        assert exc.value.code == 404
    finally:
        server.stop()


# ---------- temas ----------
def test_themes_nord_solarized_available():
    from app.ui.editor.themes import THEMES, theme_colors

    assert {"dracula", "light", "nord", "solarized"} <= set(THEMES.keys())
    for name in ("nord", "solarized"):
        palette = theme_colors(name)
        for key in ("editor_background", "keyword", "string", "token"):
            assert key in palette
            assert not palette[key].startswith("#0")  # cores distintas
    # tema desconhecido cai no dracula
    from app.ui.editor.themes import theme_colors as tc

    assert tc("romano") == THEMES["dracula"]
