"""Regressão da rodada 22: specs_diff, comparar estudos, contador de vars."""

import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import pytest
from PySide6.QtWidgets import QApplication


@pytest.fixture(scope="module")
def qapp():
    app = QApplication.instance() or QApplication([])
    yield app


# ---------- puro: specs_diff ----------

def test_specs_diff_identical():
    from app.services.specs_diff import diff_is_empty, specs_diff

    specs = {"1": {"provider": "normal", "name": "±σ", "params": {"mean": 0, "std": 1}}}
    diff = specs_diff(specs, dict(specs))
    assert diff == {"added": [], "removed": [], "changed": []}
    assert diff_is_empty(diff)


def test_specs_diff_add_remove_change():
    from app.services.specs_diff import diff_is_empty, specs_diff

    a = {
        1: {"provider": "normal", "name": "±σ", "params": {"mean": 0, "std": 1}},
        2: {"provider": "normal", "name": "×2", "params": {"factor": 2}},
        10001: {"provider": "triangular", "name": "Δ", "params": {}},
    }
    b = {
        1: {"provider": "normal", "name": "±σ", "params": {"mean": 5, "std": 1}},
        2: {"provider": "uniforme", "name": "×2", "params": {"lo": 1, "hi": 3}},
        3: {"provider": "normal", "name": "novo", "params": {}},
    }
    diff = specs_diff(a, b)
    assert diff["added"] == ["3"]
    assert diff["removed"] == ["10001"]
    fields = {(c["var"], c["field"]) for c in diff["changed"]}
    assert ("1", "params") in fields
    assert ("2", "provider") in fields
    assert not diff_is_empty(diff)
    # chaves sempre str, mesmo com ids int de entrada
    assert all(isinstance(v, str) for v in diff["added"] + diff["removed"])


def test_specs_diff_accepts_plain_dicts_and_objects():
    from types import SimpleNamespace

    from app.services.specs_diff import diff_is_empty, specs_diff

    obj = SimpleNamespace(provider="uniforme", name="U(0,1)", params={"lo": 0, "hi": 1})
    diff = specs_diff({1: obj}, {"1": {"provider": "uniforme", "name": "U(0,1)", "params": {"lo": 0, "hi": 1}}})
    assert diff_is_empty(diff)


def test_diff_line_format():
    from app.services.specs_diff import diff_line

    line = diff_line({"var": "1", "field": "params", "a": {"mean": 0}, "b": {"mean": 5}})
    assert line == "$var1 · params: {'mean': 0} → {'mean': 5}"


# ---------- comparação de estudos via serviço real ----------

def test_compare_studies_dialog_with_service(tmp_path, qapp):
    from app.services.study_service import StudyService
    from app.ui.widgets.studies_compare_dialog import StudiesCompareDialog

    from app.infrastructure.study_repository import StudyRepository

    svc = StudyService(StudyRepository(":memory:"))
    svc.create("Estudo A", {1: {"provider": "normal", "name": "±σ", "params": {"mean": 0, "std": 1}}})
    svc.create("Estudo B", {
        1: {"provider": "normal", "name": "±σ", "params": {"mean": 10, "std": 2}},
        2: {"provider": "uniforme", "name": "U", "params": {"lo": 0, "hi": 1}},
    })
    studies = svc.list_studies()
    studies.sort(key=lambda s: s["id"])  # A primeiro
    dlg = StudiesCompareDialog(svc, studies)
    assert dlg.combo_a.currentText().endswith("Estudo A")
    assert dlg.combo_b.currentText().endswith("Estudo B")
    diff = dlg.compare()
    assert diff["added"] == ["2"]
    assert ("1", "params") in {(c["var"], c["field"]) for c in diff["changed"]}
    assert "+1" in dlg.lbl_summary.text() or "1 adicionada" in dlg.lbl_summary.text()
    assert dlg.table.rowCount() >= 2
    # trocar A ↔ B a partir do estado inicial: added vira removed
    diff2 = dlg._swap()
    assert diff2["removed"] == ["2"]
    assert diff2["added"] == []
    # comparação de estudo com ele mesmo (mesma opção nos dois)
    dlg.combo_b.setCurrentIndex(dlg.combo_a.currentIndex())
    diff3 = dlg.compare()
    assert diff_is_empty_local(diff3)
    dlg.close()


def diff_is_empty_local(diff):
    return not (diff["added"] or diff["removed"] or diff["changed"])


# ---------- contador de variáveis ----------

def test_vars_status_text_pure():
    from app.core.parsing import vars_status_text

    assert vars_status_text("") == "0 vars ($:0 · $var:0)"
    assert vars_status_text("$1 = 0.\n$2.") == "2 vars ($:2 · $var:0)"
    assert vars_status_text("$var3 = $var3 * 2") == "1 vars ($:0 · $var:1)"
    assert vars_status_text("$1 e $var1") == "2 vars ($:1 · $var:1)"
    assert vars_status_text("sem variáveis!") == "0 vars ($:0 · $var:0)"


def test_main_window_vars_status_label(tmp_path, qapp):
    from PySide6.QtCore import QSettings

    from app.container import Container
    from app.ui.main_window import MainWindow

    try:
        QSettings("datstudio", "dtengine").remove("recent/files")
        container = Container(base_dir=str(tmp_path / "c22"), load_plugins=False)
        window = MainWindow(container)
        editor = window.editor_tabs.current_editor()
        assert editor is not None
        editor.set_content("$1\n$var2\n$var2\n")
        window._update_vars_status()
        assert window.lbl_vars_status.text() == "2 vars ($:1 · $var:1)"
        editor.set_content("texto sem vars")
        window._update_vars_status()
        assert window.lbl_vars_status.text() == "0 vars ($:0 · $var:0)"
        # timer configurado
        assert window._vars_timer.isActive()
        assert window._vars_timer.interval() == 700
        window.close()
    finally:
        QSettings("datstudio", "dtengine").remove("recent/files")


# ---------- botão no diálogo de estudos ----------

def test_studies_dialog_has_compare_button(tmp_path, qapp):
    from PySide6.QtWidgets import QMessageBox

    from app.services.study_service import StudyService
    from app.ui.widgets.studies_dialog import StudiesDialog

    original = QMessageBox.information
    QMessageBox.information = staticmethod(lambda *a, **k: 0)
    try:
        svc = StudyService(_reg())
        svc.create("Único", {1: {"provider": "normal", "name": "±σ", "params": {}}})
        dlg = StudiesDialog(svc)
        assert dlg.btn_compare.text() == "Comparar estudos…"
        # só 1 estudo → bloqueia com informação, sem abrir janela
        dlg._compare_studies()
        svc.create("Segundo", {})
        dlg.refresh()
        assert dlg.btn_compare.isEnabled()
    finally:
        QMessageBox.information = original


def _reg():
    from app.infrastructure.study_repository import StudyRepository

    return StudyRepository(":memory:")
