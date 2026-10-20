"""Regressão da rodada 21: recentes persistentes, prefs de UI, diff sync/swap."""

import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import pytest
from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QApplication


@pytest.fixture(scope="module")
def qapp():
    app = QApplication.instance() or QApplication([])
    yield app


# ---------- puro: serialização de recentes ----------

def test_recent_join_split_roundtrip():
    from app.ui.editor.editor_tabs import recent_join, recent_split

    items = ["C:\\a\\um.dat", "C:\\b\\dois.dat"]
    assert recent_split(recent_join(items)) == items
    assert recent_split("") == []
    assert recent_split(None) == []
    assert recent_split("\n\n") == []
    assert recent_join([]) == ""


# ---------- recentes persistidos ----------

def test_recent_persisted_across_windows(tmp_path, qapp):
    from app.container import Container
    from app.ui.main_window import MainWindow

    f = tmp_path / "persist.dat"
    f.write_text("$1 = 0.1\n", encoding="utf-8")
    try:
        container = Container(base_dir=str(tmp_path / "c21a"), load_plugins=False)
        window = MainWindow(container)
        window._push_recent(str(f))
        window.close()
        container.shutdown()

        # nova janela (nova sessão) já vem com o recente
        container2 = Container(base_dir=str(tmp_path / "c21b"), load_plugins=False)
        window2 = MainWindow(container2)
        assert str(f) in window2._recent
        assert any(a.text() == "persist.dat" for a in window2.menu_recent.actions())
        window2.close()
    finally:
        # limpa o estado global do QSettings
        QSettings("datstudio", "dtengine").remove("recent/files")
        container.shutdown() if False else None


def test_clear_recent_persists(tmp_path, qapp):
    from app.container import Container
    from app.ui.main_window import MainWindow

    try:
        container = Container(base_dir=str(tmp_path / "c21c"), load_plugins=False)
        window = MainWindow(container)
        f = tmp_path / "x.dat"
        f.write_text("a\n", encoding="utf-8")
        window._push_recent(str(f))
        assert QSettings("datstudio", "dtengine").value("recent/files", "")
        window._clear_recent()
        assert not QSettings("datstudio", "dtengine").value("recent/files", "")
        window.close()
    finally:
        QSettings("datstudio", "dtengine").remove("recent/files")


# ---------- prefs de UI ----------

def test_ui_prefs_roundtrip(qapp):
    from app.ui.ui_prefs import drop_ui_choice, load_ui_choice, save_ui_choice

    key = "test/round21"
    try:
        assert load_ui_choice(key, "padrão") == "padrão"
        save_ui_choice(key, 42)
        assert load_ui_choice(key, 0) == 42
        drop_ui_choice(key)
        assert load_ui_choice(key, "padrão") == "padrão"
    finally:
        drop_ui_choice(key)


def test_main_window_restores_format_choice(tmp_path, qapp):
    from app.container import Container
    from app.ui.main_window import MainWindow
    from app.ui.ui_prefs import load_ui_choice, save_ui_choice, drop_ui_choice

    key_val = None
    try:
        old = load_ui_choice("experiments/format", None)
        key_val = old
        save_ui_choice("experiments/format", 2)  # Lista compacta
        container = Container(base_dir=str(tmp_path / "c21d"), load_plugins=False)
        window = MainWindow(container)
        assert window.experiments_panel.combo_format.currentIndex() == 2
        assert window.experiments_panel.view_stack.currentIndex() == 2
        window.close()
    finally:
        if key_val is None:
            drop_ui_choice("experiments/format")
        else:
            save_ui_choice("experiments/format", key_val)


# ---------- diff: sincronismo e troca ----------

def test_diff_scroll_sync(qapp):
    from app.ui.widgets.diff_dialog import DiffDialog

    dlg = DiffDialog(open_files=[("A", "\n".join(f"linha {i}" for i in range(200)))])
    dlg.compare()
    dlg.txt_b.setPlainText("\n".join(f"L{i}" for i in range(200)))
    dlg.txt_a.verticalScrollBar().setValue(50)
    dlg._follow_a(50)
    assert dlg.txt_b.verticalScrollBar().value() == 50
    # b → a também
    dlg._follow_b(80)
    assert dlg.txt_a.verticalScrollBar().value() == 80
    # desligado não segue
    dlg.chk_sync.setChecked(False)
    dlg._follow_a(10)
    assert dlg.txt_a.verticalScrollBar().value() == 80


def test_diff_swap(qapp):
    from app.ui.widgets.diff_dialog import DiffDialog

    dlg = DiffDialog(open_files=[("A.dat", "1\n2\n3\n"), ("B.dat", "1\n2\n3\n4\n")])
    dlg.compare()
    ia, ib = dlg.combo_a.currentIndex(), dlg.combo_b.currentIndex()
    summary_before = dlg.lbl_summary.text()
    dlg.btn_swap.click()
    assert dlg.combo_a.currentIndex() == ib
    assert dlg.combo_b.currentIndex() == ia
    # direção invertida: a linha extra de B vira remoção (+1/−0 → +0/−1)
    assert "+0" in dlg.lbl_summary.text() and "\u22121" in dlg.lbl_summary.text()


def test_diff_swap_changes_diff(qapp):
    from app.ui.widgets.diff_dialog import DiffDialog

    dlg = DiffDialog(open_files=[("A.dat", "só A\n"), ("B.dat", "só B\n")])
    dlg.compare()
    assert "só A" in dlg.txt_a.toPlainText()
    dlg.btn_swap.click()
    assert "só B" in dlg.txt_a.toPlainText()
    assert "só A" in dlg.txt_b.toPlainText()
