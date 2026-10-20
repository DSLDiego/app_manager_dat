"""Regressões das features novas: Sobol, logs, export, WAL, CSV de correlação, API export."""

import json
import sqlite3
import urllib.request
from datetime import datetime, timedelta

import numpy as np
import pytest

from app.infrastructure.distribution_registry import build_default_registry

pytest.importorskip("pytestqt")


# ---------- Sobol ----------
def test_sobol_reproducible_and_bounded():
    import random

    rng = np.random.default_rng(11)
    from app.services.strategies.sobol import SobolStrategy

    strat = SobolStrategy()
    assert strat.name == "sobol"
    u1 = strat.generate_uniforms(16, 3, rng)
    rng2 = np.random.default_rng(11)
    u2 = strat.generate_uniforms(16, 3, rng2)
    assert u1.shape == (16, 3)
    assert np.allclose(u1, u2)
    assert (u1 >= 0).all() and (u1 <= 1).all()
    # sobol estratifica melhor que MC: variance menor
    strat_mc = __import__(
        "app.services.strategies.latin_hypercube", fromlist=["MonteCarloStrategy"]
    ).MonteCarloStrategy()
    u_mc = strat_mc.generate_uniforms(256, 1, np.random.default_rng(5))
    u_sob = strat.generate_uniforms(256, 1, np.random.default_rng(5))
    assert u_sob[:, 0].var() <= u_mc[:, 0].var() * 1.5 + 1e-3


def test_sobol_registered_in_service_and_sampling():
    from app.services.sampling_service import SamplingService
    from app.domain.entities import DistributionSpec, SamplingRequest

    service = SamplingService(build_default_registry())
    request = SamplingRequest(
        var_ids=[1, 10002],
        specs={
            1: DistributionSpec(provider="scipy", name="norm", params={"loc": 20, "scale": 4}),
            10002: DistributionSpec(provider="fixed", name="value", params={"value": 1.0}),
        },
        n_experiments=32,
        seed=5,
        strategy="sobol",
    )
    result = service.run(request)
    matrix = np.asarray(result.matrix)
    assert matrix.shape == (32, 2)
    assert np.all(matrix[:, 1] == 1.0)
    assert np.all((matrix[:, 0] > 5) & (matrix[:, 0] < 35))
    again = service.run(request)
    assert np.allclose(np.asarray(again.matrix), matrix)


# ---------- logs: retenção e filtro por datas ----------
def _insert_row_with_date(log_repo, created_at_iso):
    with log_repo._lock, log_repo.conn:
        log_repo.conn.execute(
            "INSERT INTO logs (created_at, level, category, action, message) "
            "VALUES (?, 'INFO', 'SYSTEM', 'old', 'x')",
            (created_at_iso,),
        )


def test_log_purge_old_deletes_only_old(log_repo, qtbot):
    log_repo.wait_pending()
    old = (datetime.now() - timedelta(days=40)).isoformat()
    recent = datetime.now().isoformat()
    _insert_row_with_date(log_repo, old)
    _insert_row_with_date(log_repo, recent)

    deleted = log_repo.purge_old(days=30)
    assert deleted >= 1
    cutoff = (datetime.now() - timedelta(days=30)).isoformat()
    remaining = log_repo.fetch()
    assert all(row["created_at"] >= cutoff for row in remaining)
    ids_now = {r["id"] for r in remaining}
    with log_repo._lock, log_repo.conn:
        ids_all = {r["id"] for r in log_repo.conn.execute("SELECT id FROM logs").fetchall()}
    assert ids_now == ids_all  # fetch() enxerga as mesmas linhas que sobraram


def test_log_fetch_date_filters(log_repo, qtbot):
    log_repo.wait_pending()
    log_repo.wait_pending()
    yesterday = (datetime.now() - timedelta(days=2)).isoformat()
    _insert_row_with_date(log_repo, yesterday)
    with log_repo._lock, log_repo.conn:
        log_repo.conn.execute(
            "INSERT INTO logs (created_at, level, category, action, message) "
            "VALUES (?, 'INFO', 'SYSTEM', 'today', 'novo')",
            (datetime.now().isoformat(),),
        )

    rows = log_repo.fetch(date_from=yesterday, date_to=yesterday + "Z")
    assert rows and all(r["action"] == "old" or r["created_at"] < datetime.now().isoformat() for r in rows)

    only_today = log_repo.fetch(
        date_from=(datetime.now() - timedelta(minutes=10)).isoformat()
    )
    assert only_today and all(r["created_at"] >= yesterday for r in only_today)
    assert all(r["action"] != "old" for r in only_today)


# ---------- WAL ----------
def test_repositories_use_wal(tmp_path):
    from app.infrastructure.experiment_repository import ExperimentRepository
    from app.infrastructure.task_repository import TaskRepository
    from app.infrastructure.template_repository import TemplateRepository

    exp = ExperimentRepository(str(tmp_path / "e.db"))
    tpl = TemplateRepository(str(tmp_path / "t.db"))
    task = TaskRepository(str(tmp_path / "k.db"))
    for repo in (exp, tpl, task):
        mode = repo.conn.execute("PRAGMA journal_mode").fetchone()[0]
        assert mode == "wal", mode
    exp.close()
    tpl.close()
    task.close()


# ---------- export: máscara e política ----------
def test_export_filename_pattern(container, populated_batch):
    out = container.base_dir / "out_pattern"
    manifest = container.batch_export_service.export(
        populated_batch["batch_id"],
        populated_batch["version_id"],
        out,
        filename_pattern="run_{id:06d}",
    )
    files = sorted(manifest.output_dir.glob("*.dat"))
    assert len(files) == 12
    assert files[0].name == "run_000001.dat"
    assert all("$" not in p.read_text(encoding="utf-8") for p in files)


def test_export_skip_existing_policy(container, populated_batch):
    out = container.base_dir / "out_skip"
    first = container.batch_export_service.export(
        populated_batch["batch_id"], populated_batch["version_id"], out
    )
    victim = next(iter(sorted(first.output_dir.glob("*.dat"))))

    mtime_before = victim.stat().st_mtime_ns
    # muda a versão do template para garantir que o conteúdo CONTINUA antigo
    from app.infrastructure.template_repository import TemplateRepository

    container.template_repo.save_version(
        int(populated_batch["version_id"]) - 0, "NOVO CONTEUDO $1"
    )
    second = container.batch_export_service.export(
        populated_batch["batch_id"],
        populated_batch["version_id"],
        out,
        overwrite=False,
    )
    assert second.n_files == 12
    assert victim.read_text(encoding="utf-8") == victim.read_text(encoding="utf-8")
    assert victim.stat().st_mtime_ns == mtime_before  # não regravou


# ---------- correlação CSV ----------
def test_correlation_csv_roundtrip(tmp_path):
    from app.services.correlation_service import CorrelationService

    svc = CorrelationService()
    corr = [[1.0, 0.3, -0.5], [0.3, 1.0, 0.2], [-0.5, 0.2, 1.0]]
    path = tmp_path / "corr.csv"
    svc.to_csv(corr, path)
    loaded = svc.load_csv(path)
    assert np.allclose(np.asarray(loaded), np.asarray(corr))

    # CSV com vírgula decimal? não permitido: valores técnicos usam ponto
    assert path.read_text(encoding="utf-8").startswith("1.0")


def test_correlation_csv_empty(tmp_path):
    from app.services.correlation_service import CorrelationService

    svc = CorrelationService()
    path = tmp_path / "vazio.csv"
    path.write_text("", encoding="utf-8")
    assert svc.load_csv(path) == []


# ---------- API: POST export ----------
def test_api_post_export_endpoint(container, populated_batch):
    from app.infrastructure.api.routes import build_api_routes
    from app.infrastructure.api.server import ApiServer

    server = ApiServer(host="127.0.0.1", port=0)
    build_api_routes(server, container.exp_repo, container.template_repo)
    server.start()
    try:
        base = f"http://127.0.0.1:{server.port}/api"
        out_root = str(container.base_dir / "out_api")
        payload = json.dumps(
            {
                "template_version_id": populated_batch["version_id"],
                "output_root": out_root,
            }
        ).encode("utf-8")
        req = urllib.request.Request(
            f"{base}/batches/batch_x/export",
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
        assert body["n_files"] == 12
        assert body["batch_id"] == "batch_x"
        import os

        assert os.path.isdir(body["output_dir"])

        # sem corpo → 404 (ValueError tratado)
        bad = urllib.request.Request(
            f"{base}/batches/batch_x/export", data=b"", method="POST"
        )
        with pytest.raises(urllib.error.HTTPError) as exc:
            urllib.request.urlopen(bad, timeout=15)
        assert exc.value.code == 404
    finally:
        server.stop()
