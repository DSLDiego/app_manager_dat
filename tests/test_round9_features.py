"""Regressão da rodada 9: export por lote, fail-fast de variáveis, mínimos de janela, botões nos painéis."""

import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from pathlib import Path

import pytest

from PySide6.QtWidgets import QApplication  # noqa: F401 — QFont precisa de app

from PySide6.QtWidgets import QToolBar


@pytest.fixture(scope="module")
def qapp():
    app = QApplication.instance() or QApplication([])
    yield app


@pytest.fixture()
def tmp_container(tmp_path, qapp):
    from PySide6.QtWidgets import QApplication

    from app.container import Container

    assert QApplication.instance() is not None
    container = Container(base_dir=str(tmp_path / "c9"), load_plugins=False)
    yield container
    container.shutdown()


def _populate_two_batches(exp_repo):
    exp_repo.create_batch("b1", "lhs", 1, 2)
    exp_repo.create_batch("b2", "lhs", 2, 3)
    exp_repo.insert_result("b1", [1], [[10.0], [20.0]])
    exp_repo.insert_result("b2", [1], [[1.0], [2.0], [3.0]])


# ---------- export por lote + fail-fast ----------

def test_export_only_requested_batch(tmp_container):
    from app.services.batch_export_service import BatchExportService

    _populate_two_batches(tmp_container.exp_repo)
    tpl = tmp_container.template_repo.create_template("t")
    vid = tmp_container.template_repo.save_version(tpl, "T $1", comment="v1")
    svc = BatchExportService(
        tmp_container.exp_repo, tmp_container.template_repo, renderer=lambda tid, vals: f"T {vals[1]:.0f}"
    )
    out = Path(tmp_container.base_dir) / "out_root"
    manifest = svc.export("b2", vid, out)
    assert manifest.n_files == 3  # só o lote b2, sem misturar b1
    assert (out / "b2" / "v1" / "experimento_000001.dat").exists()


def test_export_fail_fast_missing_variable(tmp_container):
    from app.services.batch_export_service import BatchExportService

    _populate_two_batches(tmp_container.exp_repo)
    # b1 $1=$1 e $var1 — $var1 já está no lote? convertendo: var 1 e 10001
    exp_repo = tmp_container.exp_repo
    exp_repo.insert_result("b1", [10001], [[5.0], [6.0]])
    tpl = tmp_container.template_repo.create_template("t2")
    vid = tmp_container.template_repo.save_version(tpl, "T $1 $var11", comment="bad")
    svc = BatchExportService(
        tmp_container.exp_repo, tmp_container.template_repo,
        renderer=lambda tid, vals: "T " + " ".join(f"{v:.0f}" for _, v in sorted(vals.items())),
    )
    out = Path(tmp_container.base_dir) / "out_ff"
    with pytest.raises(ValueError) as exc:
        svc.export("b1", vid, out)
    assert "$var11" in str(exc.value)
    # fail-fast: nenhum arquivo gravado antes do erro
    assert not (out / "b1").exists()


def test_export_empty_batch_clear_error(tmp_container):
    from app.services.batch_export_service import BatchExportService

    _populate_two_batches(tmp_container.exp_repo)
    tpl = tmp_container.template_repo.create_template("t3")
    vid = tmp_container.template_repo.save_version(tpl, "T $1", comment="v1")
    svc = BatchExportService(
        tmp_container.exp_repo, tmp_container.template_repo, renderer=lambda tid, vals: "T"
    )
    with pytest.raises(ValueError) as exc:
        svc.export("no_existe", vid, Path(tmp_container.base_dir) / "o")
    assert "no_existe" in str(exc.value)


# ---------- janela: mínimos e botões ----------

def test_window_minimum_size_is_portable(tmp_container):
    from app.ui.main_window import MainWindow

    window = MainWindow(tmp_container)
    assert window.minimumSize().width() <= 900
    assert window.minimumSize().height() <= 560
    assert not window.findChildren(QToolBar)
    window.close()


def test_panel_button_signals(tmp_container, monkeypatch):
    from app.ui.main_window import MainWindow

    calls = []
    window = MainWindow(tmp_container)
    monkeypatch.setattr(window, "_open_batch_export", lambda: calls.append("gen"))
    monkeypatch.setattr(window, "_save_template_version", lambda: calls.append("save"))
    monkeypatch.setattr(window, "_reload_dat_file", lambda: calls.append("reload"))
    window.experiments_panel.btn_generate.click()
    window.experiments_panel.btn_save_tpl.click()
    window.variables_panel.btn_reload_dat.click()
    assert calls == ["gen", "save", "reload"]
    window.close()
