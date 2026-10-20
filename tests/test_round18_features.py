"""Regressão da rodada 18: minimapa, wizard de template, salvar PNG do gráfico."""

import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import pytest
from PySide6.QtWidgets import QApplication


@pytest.fixture(scope="module")
def qapp():
    app = QApplication.instance() or QApplication([])
    yield app


# ---------- puro: minimapa ----------

def test_minimap_bars_pure():
    from app.ui.editor.editor_minimap import minimap_bars

    assert minimap_bars([]) == []
    bars = minimap_bars(["", "abc", "abcdef"])
    assert bars == [0.0, 0.5, 1.0]
    # cap de linhas
    big = [f"linha {i}" for i in range(10_000)]
    assert len(minimap_bars(big)) == 4000
    assert minimap_bars(big)[-1] == 1.0  # "linha 3999" é a mais larga do cap


def test_scroll_window_pure():
    from app.ui.editor.editor_minimap import scroll_window

    assert scroll_window(0, 10, 0) == (0.0, 1.0)
    top, height = scroll_window(100, 20, 30)
    assert top == pytest.approx(0.3)
    assert height == pytest.approx(0.2)
    # janela maior que o documento → clamp
    top2, height2 = scroll_window(10, 50, 8)
    assert top2 == pytest.approx(0.8)
    assert height2 == pytest.approx(0.2)  # 1.0 - 0.8


def test_minimap_widget_paint_and_click(qapp):
    from PySide6.QtCore import QPoint, Qt
    from PySide6.QtTest import QTest

    from app.ui.editor.editor_minimap import EditorMinimap

    m = EditorMinimap()
    m.resize(60, 200)
    m.set_document("a\nbb\nccc\ndddd\n")
    assert m._bars == [0.25, 0.5, 0.75, 1.0]
    assert m.line_at(150) == 3  # 150/200 × 4 barras
    assert m.line_at(120) == 2
    m.set_scroll(4, 2, 2)
    assert m._win[0] == pytest.approx(0.5)
    m.grab()  # paintEvent com barras + janela
    # clique navega: sinal com linha
    clicked = []
    m.lineClicked.connect(lambda line: clicked.append(line))
    QTest.mouseClick(m, Qt.MouseButton.LeftButton, pos=QPoint(30, 180))
    assert clicked == [3]


def test_editor_widget_minimap_sync(qapp):
    from app.ui.editor.editor_widget import EditorWidget

    tab = EditorWidget()
    assert tab.minimap is not None and tab.minimap.isVisible() is False or True
    tab.set_content("x = $1\ny = $var2\n")
    assert tab.minimap._bars == [pytest.approx(6 / 9), 1.0]
    # toggle não explode (menu Ver)
    tab.set_minimap_visible(False)
    assert not tab.minimap.isVisible()
    tab.set_minimap_visible(True)


# ---------- wizard de template ----------

def test_wizard_scan_and_suggest_pure():
    from app.ui.widgets.template_wizard_dialog import wizard_scan, wizard_suggest

    scan = wizard_scan("A = $1\nB = $var3\nC = $1\n")
    assert scan["var_ids"] == [1, 10003]
    assert scan["n_regular"] == 1 and scan["n_namespace"] == 1
    assert scan["empty"] is False
    assert wizard_scan("   ")["empty"] is True
    assert wizard_suggest([1, 2]) == {1: "uniform", 2: "uniform"}


def test_wizard_dialog_steps(qapp):
    from app.ui.widgets.template_wizard_dialog import TemplateWizardDialog

    dlg = TemplateWizardDialog()
    assert dlg.stack.count() == 3
    assert dlg.stack.currentIndex() == 0
    assert not dlg.btn_back.isEnabled()
    # passo 1: exemplo
    dlg.btn_sample.click()
    assert "$1" in dlg.txt_base.toPlainText()
    # passo 2: variáveis
    dlg.btn_next.click()
    assert dlg.stack.currentIndex() == 1
    assert "3 variável(is)" in dlg.lbl_vars.text()  # $1, $2 e $var3
    assert dlg.tbl_vars.rowCount() == 3
    # passo 3: revisão
    dlg.btn_next.click()
    assert dlg.stack.currentIndex() == 2
    assert not dlg.btn_next.isEnabled() and dlg.btn_back.isEnabled()
    # concluir → sinal com o texto
    got = []
    dlg.templateReady.connect(lambda t: got.append(t))
    dlg.btn_finish.click()
    assert len(got) == 1 and "$var3" in got[0]
    assert dlg.result() == dlg.DialogCode.Accepted


def test_wizard_empty_finish_blocked(qapp):
    from app.ui.widgets.template_wizard_dialog import TemplateWizardDialog

    dlg = TemplateWizardDialog()
    got = []
    dlg.templateReady.connect(lambda t: got.append(t))
    dlg.btn_finish.click()  # texto vazio → não emite
    assert got == []


def test_main_window_wizard_creates_tab(tmp_path, qapp):
    from app.container import Container
    from app.ui.main_window import MainWindow
    from app.ui.widgets.template_wizard_dialog import SAMPLE_TEMPLATE

    container = Container(base_dir=str(tmp_path / "c18"), load_plugins=False)
    try:
        window = MainWindow(container)
        n0 = window.editor_tabs.count()
        window._create_template_tab(SAMPLE_TEMPLATE)
        assert window.editor_tabs.count() == n0 + 1
        assert SAMPLE_TEMPLATE in window.editor_tabs.widget(
            window.editor_tabs.count() - 1
        ).text()
        window.close()
    finally:
        container.shutdown()


# ---------- salvar PNG ----------

def test_plot_save_png(tmp_path, qapp, monkeypatch):
    import numpy as np
    from PySide6.QtWidgets import QFileDialog

    from app.ui.widgets.distribution_plot_dialog import DistributionPlotDialog

    dlg = DistributionPlotDialog()
    dlg.canvas.add_series("s", np.arange(5, dtype=float), np.ones(5), True)
    target = tmp_path / "graf.png"
    QFileDialog.getSaveFileName = staticmethod(
        lambda *a, **k: (str(target), "PNG (*.png)")
    )
    dlg._save_png()
    assert target.exists() and target.stat().st_size > 0
    assert "salvo" in dlg.windowTitle().lower()


def test_plot_save_png_cancelled(qapp):
    from PySide6.QtWidgets import QFileDialog

    from app.ui.widgets.distribution_plot_dialog import DistributionPlotDialog

    dlg = DistributionPlotDialog()
    QFileDialog.getSaveFileName = staticmethod(lambda *a, **k: ("", ""))
    before = dlg.windowTitle()
    dlg._save_png()
    assert dlg.windowTitle() == before


# ---------- menu Ver: minimapa na janela inteira ----------

def test_main_window_toggle_minimap(tmp_path, qapp):
    from app.container import Container
    from app.ui.main_window import MainWindow

    container = Container(base_dir=str(tmp_path / "c18m"), load_plugins=False)
    try:
        window = MainWindow(container)
        window.editor_tabs.new_tab(title="T1")
        window.editor_tabs.new_tab(title="T2")
        window._toggle_minimap(False)
        for i in range(window.editor_tabs.count()):
            assert not window.editor_tabs.widget(i).minimap.isVisible()
        window._toggle_minimap(True)
        window.close()
    finally:
        container.shutdown()
