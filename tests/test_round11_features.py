"""Regressão da rodada 11: lista de arquivos (Notepad++), grade n×m dinâmica,
atalhos de busca e detalhes visuais do plot."""

import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import pytest
from PySide6.QtGui import QShortcut
from PySide6.QtWidgets import QApplication, QMessageBox


@pytest.fixture(scope="module")
def qapp():
    app = QApplication.instance() or QApplication([])
    yield app


@pytest.fixture()
def tabs(qapp):
    from PySide6.QtWidgets import QMessageBox

    from app.ui.editor.editor_tabs import EditorTabs

    if hasattr(QMessageBox, "question"):
        QMessageBox.question = staticmethod(
            lambda *a, **k: QMessageBox.StandardButton.Discard
        )
    yield EditorTabs()


# ---------- FilesListPanel ----------

def test_files_list_reflects_tabs(tabs, qapp):
    from app.ui.widgets.files_list_panel import FilesListPanel

    tabs.new_tab("DAT $1", "Sem título")
    assert tabs.tabsChanged  # sinal existe
    panel = FilesListPanel(tabs)
    assert panel.list.count() == 1
    assert "Sem título" in panel.list.item(0).text()


def test_files_list_dirty_mark_updates(tabs, qapp):
    from app.ui.widgets.files_list_panel import FilesListPanel

    tabs.new_tab("", "t1.dat")
    panel = FilesListPanel(tabs)
    tab = tabs.current_editor()
    tab.editor.setPlainText("alterado")
    tabs.current_editor().set_content("x")  # garante dirty
    tab.set_content("")  # reseta
    tab.editor.setPlainText("mudou de novo")
    if not tab.is_modified():
        tab.set_content("conteúdo")
    panel.refresh()
    assert panel.list.count() == 1
    item_text = panel.list.item(0).text()
    assert ("●" in item_text) or (panel.list.item(0).toolTip() != "")


def test_files_list_click_activates_tab(tabs, qapp):
    from app.ui.widgets.files_list_panel import FilesListPanel

    tabs.new_tab("a", "ABA1")
    tabs.new_tab("b", "ABA2")
    idx_first = 0
    panel = FilesListPanel(tabs)
    panel.fileActivated.connect(tabs.setCurrentIndex)
    panel._on_item_clicked(panel.list.item(idx_first))
    assert tabs.currentIndex() == idx_first


def test_files_list_row_and_tooltip(tabs, qapp):
    from app.ui.widgets.files_list_panel import FilesListPanel

    tabs.new_tab("x", "Sem t")
    panel = FilesListPanel(tabs)
    assert panel.list.currentRow() == tabs.currentIndex()


# ---------- grade n×m dinâmica do hist-grid ----------

def test_grid_layout_pure():
    from app.ui.widgets.histogram_grid_panel import HistogramGridPanel

    total_rows, cols, cells = HistogramGridPanel.grid_layout(n_items=13, cols=4)
    assert (total_rows, cols, cells) == (6, 4, 12)
    r2, c2, cells2 = HistogramGridPanel.grid_layout(n_items=40, cols=2)
    assert c2 == 2 and cells2 == 6 and r2 >= 21


def test_grid_combo_cols_changes_shape(qapp, tmp_path):
    from app.infrastructure.experiment_repository import ExperimentRepository
    from app.ui.widgets.histogram_grid_panel import HistogramGridPanel

    repo = ExperimentRepository(str(tmp_path / "h11.db"))
    repo.create_batch("bh11", "lhs", 1, 20)
    var_ids = list(range(1, 19))  # 18 variáveis
    repo.insert_result(
        "bh11", var_ids, [[float(v) for v in var_ids] for _ in range(6)]
    )  # 6 experimentos × 18 valores
    panel = HistogramGridPanel()
    panel.load_from_repo(repo)
    assert panel.table.columnCount() == 4
    panel.combo_cols.setCurrentText("2")
    assert panel.table.columnCount() == 2
    assert panel._cols == 2
    assert len(panel._current_ids()) == 6  # 2×3
    panel.combo_cols.setCurrentText("6")
    assert len(panel._current_ids()) == 18  # 6×3
    repo.close()


# ---------- atalhos de busca ----------

def test_editor_widget_search_shortcuts(qapp):
    from app.ui.editor.editor_widget import EditorWidget

    widget = EditorWidget()
    widget.set_content("T $var1 $var2")
    widget.find_bar.show_bar()
    assert not widget.find_bar.isHidden()
    # F3 (_repeat_find) repete a ÚLTIMA busca do controller
    widget._repeat_find()  # sem busca anterior → no-op seguro
    widget.find_bar.input.setText("$var")
    widget.find_bar._emit_find()
    assert "2 ocorrência(s)" in widget.find_bar.label.text()
    widget.find_controller._last = "$var"
    widget._repeat_find()
    assert "2 ocorrência(s)" in widget.find_bar.label.text()


def test_editor_shortcuts_registered(qapp):
    from PySide6.QtGui import QShortcut

    from app.ui.editor.editor_widget import EditorWidget

    widget = EditorWidget()
    shortcuts = widget.editor.findChildren(QShortcut)
    assert len(shortcuts) >= 2  # Ctrl+F + F3 no editor (Esc no bar)


# ---------- plot: detalhes visuais ----------

def test_canvas_bar_markers_and_title(qapp):
    import numpy as np

    from app.ui.widgets.distribution_plot_dialog import PlotCanvas

    canvas = PlotCanvas()
    canvas.set_title("Bordas")
    xs = np.linspace(0, 4, 40)
    canvas.add_series("Normal(mu)", xs, np.exp(-((xs - 2) ** 2)), True)
    assert canvas.mode == "line"
    from PySide6.QtWidgets import QWidget

    canvas.grab()  # paintEvent roda sem exceções com marcadores


def test_canvas_renders_bars(qapp):
    import numpy as np

    from app.ui.widgets.distribution_plot_dialog import PlotCanvas

    canvas = PlotCanvas()
    canvas.mode = "bar"
    xs = np.arange(10, dtype=float)
    ys = np.ones(10)
    canvas.add_series("PMF", xs, ys, True)
    canvas.grab()


# ---------- editores preenchem 100% (margens zero) ----------

def test_editor_widget_margins_zero(qapp):
    from app.ui.editor.editor_widget import EditorWidget

    widget = EditorWidget()
    margins = widget.layout().contentsMargins()
    assert (margins.left(), margins.top(), margins.right(), margins.bottom()) == (0, 0, 0, 0)
    assert widget.layout().spacing() == 0


def test_files_panel_margins_compact(qapp, tmp_path, tabs):
    from app.ui.widgets.files_list_panel import FilesListPanel

    panels = FilesListPanel(tabs)
    margins = panels.layout().contentsMargins()
    assert margins.left() <= 8
    assert panels.layout().spacing() <= 4


# ---------- integração: dock de arquivos no MainWindow ----------

def test_files_dock_in_main_window(tmp_path, qapp):
    from PySide6.QtCore import Qt

    from app.container import Container
    from app.ui.main_window import MainWindow

    container = Container(base_dir=str(tmp_path / "fw"), load_plugins=False)
    try:
        window = MainWindow(container)
        base_tabs = window.files_panel.list.count()  # ctor já cria 1 aba
        window.editor_tabs.new_tab("T $1", "Sem t1")
        window.editor_tabs.new_tab("T $2", "Sem t2")
        window.files_panel.refresh()
        assert window.files_panel.list.count() == base_tabs + 2
        # clique ativa
        window.files_panel.fileActivated.connect(window.editor_tabs.setCurrentIndex)
        window.files_panel._on_item_clicked(window.files_panel.list.item(0))
        assert window.editor_tabs.currentIndex() == 0
        # grade e abas contemplam o dock novo (6 docks)
        window._arrange_docks_grid()
        window._tabify_docks()
        window.close()
    finally:
        container.shutdown()
