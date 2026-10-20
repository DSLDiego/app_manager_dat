"""Regressão da rodada 25: histórico de lotes e reuso de seed."""

import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import pytest
from PySide6.QtCore import QSettings
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QApplication

from app.container import Container
from app.ui.main_window import MainWindow


@pytest.fixture()
def qapp():
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    return app


@pytest.fixture()
def window(tmp_path, qapp):
    container = Container(base_dir=str(tmp_path / "c25"), load_plugins=False)
    QSettings("datstudio", "dtengine").remove("recent/files")
    w = MainWindow(container)
    yield w
    w.close()
    QSettings("datstudio", "dtengine").remove("recent/files")


# ---------- puro: linha resumida ----------

def test_format_batch_row():
    from app.ui.widgets.batch_history_dialog import format_batch_row

    row = {"id": "batch_20250101_000001", "method": "sampling", "seed": 42, "n_experiments": 100}
    assert format_batch_row(row) == "batch_20250101_000001 · sampling · seed=42 · 100 exps"
    assert format_batch_row({"id": "b2", "method": "manual"}) == "b2 · manual · seed=— · 0 exps"
    seed_none = {"id": "x", "method": "m", "seed": None, "n_experiments": 3}
    assert "seed=—" in format_batch_row(seed_none)


# ---------- diálogo com repositório real ----------

def _repo_with_batches(tmp_path):
    from app.infrastructure.experiment_repository import ExperimentRepository

    repo = ExperimentRepository(str(tmp_path / "exp25.db"))
    repo.create_batch("batch_1", method="sampling", seed=42, n_experiments=10)
    import random

    repo.insert_result("batch_1", [1], [[random.random()] for _ in range(10)])
    repo.create_batch("batch_2", method="sobol", seed=999, n_experiments=5)
    repo.insert_result("batch_2", [1], [[random.random()] for _ in range(5)])
    return repo


def test_batch_history_dialog_lists_batches(tmp_path, qapp):
    from app.ui.widgets.batch_history_dialog import BatchHistoryDialog

    repo = _repo_with_batches(tmp_path)
    dlg = BatchHistoryDialog(repo)
    assert dlg.table.rowCount() == 2
    ids = {dlg.table.item(i, 0).text() for i in range(2)}
    assert ids == {"batch_1", "batch_2"}
    seeds = {dlg.table.item(i, 2).text() for i in range(2)}
    assert seeds == {"42", "999"}
    assert "lotes." in dlg.lbl_summary.text()
    assert dlg.selected_row is not None
    assert dlg.btn_copy.isEnabled()
    assert dlg.btn_use.isEnabled()
    dlg.close()


def test_batch_history_dialog_copy_seed(tmp_path, qapp):
    from app.ui.widgets.batch_history_dialog import BatchHistoryDialog

    repo = _repo_with_batches(tmp_path)
    dlg = BatchHistoryDialog(repo)
    # linha com seed 42 é a mais recente (batch_2 em cima)
    seed = dlg._selected_seed()
    assert seed == 999
    dlg._copy_seed()
    assert QGuiApplication.clipboard().text() == "999"
    # seleciona a outra linha e copia
    dlg.table.selectRow(1)
    assert dlg._selected_seed() == 42
    dlg._copy_seed()
    assert QGuiApplication.clipboard().text() == "42"
    dlg.close()


def test_batch_history_dialog_use_requested_signal(tmp_path, qapp):
    from app.ui.widgets.batch_history_dialog import BatchHistoryDialog

    repo = _repo_with_batches(tmp_path)
    dlg = BatchHistoryDialog(repo)
    received = []
    dlg.useRequested.connect(lambda seed: received.append(seed))
    dlg.table.selectRow(1)
    dlg._use_seed()
    assert received == [42]
    dlg.close()


def test_batch_history_dialog_empty_repo(tmp_path, qapp):
    from app.infrastructure.experiment_repository import ExperimentRepository
    from app.ui.widgets.batch_history_dialog import BatchHistoryDialog

    repo = ExperimentRepository(str(tmp_path / "empty25.db"))
    dlg = BatchHistoryDialog(repo)
    assert dlg.table.rowCount() == 0
    assert dlg.selected_row is None
    assert not dlg.btn_copy.isEnabled()
    assert not dlg.btn_use.isEnabled()
    dlg.close()


# ---------- MainWindow: memorizar seed ----------

def test_main_window_pending_seed_flow(window):
    received_status = window.status_message()
    window._apply_pending_seed(31337)
    assert window._pending_seed == 31337
    assert "31337" in window.status_message()
    assert received_status != window.status_message()


class _SeedHostFake:
    """Suporte mínimo: edit_seed do diálogo."""

    def __init__(self):
        self.edit_seed = plt_stub()


def plt_stub():
    class E:
        def __init__(self):
            self._t = ""

        def setText(self, t):
            self._t = t

        def text(self):
            return self._t

    return E()


def test_prefill_seed_input_fills_dialog(window):
    window._pending_seed = 4242
    fake = _SeedHostFake()
    assert window._prefill_seed_input(fake) is True
    assert fake.edit_seed.text() == "4242"
    # sem pendência → não preenche
    window._pending_seed = None
    fake2 = _SeedHostFake()
    assert window._prefill_seed_input(fake2) is False
    # objeto sem edit_seed → False seguro
    assert window._prefill_seed_input(object()) is False


def test_main_window_menu_batch_history_action(window):
    acts = []
    for menu_action in window.menuBar().actions():
        sub = menu_action.menu()
        if sub is None:
            continue
        acts.extend(a.text() for a in sub.actions())
    assert "Histórico de lotes…" in acts