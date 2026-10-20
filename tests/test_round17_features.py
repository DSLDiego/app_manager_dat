"""Regressão da rodada 17: cap de largura dos docks (≤20% da janela) + matriz exp×var."""

import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import pytest
from PySide6.QtWidgets import QApplication, QWidget


@pytest.fixture(scope="module")
def qapp():
    app = QApplication.instance() or QApplication([])
    yield app


# ---------- puro: cap de largura ----------

def test_dock_width_cap_pure():
    from app.ui.layout_presets import dock_width_cap, DOCK_WIDTH_FRACTION

    assert dock_width_cap(1000) == 200
    assert dock_width_cap(860) == 172
    assert dock_width_cap(400) == 90  # piso
    assert DOCK_WIDTH_FRACTION == 0.20


def test_widgets_over_cap_pure(qapp):
    from app.ui.layout_presets import widgets_over_cap

    narrow = QWidget()
    narrow.setMinimumWidth(120)
    wide = QWidget()
    wide.setMinimumWidth(400)
    over = widgets_over_cap([narrow, wide], 172)
    assert over == [wide]
    # baixa o mínimo até o cap
    wide.setMinimumWidth(172)
    assert widgets_over_cap([wide], 172) == []
    # widget C++ deletado não explode
    gone = QWidget()
    gone.deleteLater()
    assert widgets_over_cap([gone], 172) == []


def test_main_window_enforces_dock_caps(tmp_path, qapp):
    from app.container import Container
    from app.ui.layout_presets import dock_width_cap
    from app.ui.main_window import MainWindow

    container = Container(base_dir=str(tmp_path / "c17"), load_plugins=False)
    try:
        window = MainWindow(container)
        window.resize(1000, 700)
        cap = dock_width_cap(window.width())
        assert cap == 200
        # experiments table tinha mínimo 170 — dentro do cap
        assert window.experiments_panel.table.minimumWidth() <= cap
        # widget artificialmente largo dentro de um dock é reduzido
        fat = QWidget()
        fat.setMinimumWidth(500)
        window._dock_logs.widget().setMinimumWidth(500)
        window._enforce_dock_width_caps()
        # após o enforce, nada explícito acima do cap nos docks
        from app.ui.layout_presets import widgets_over_cap

        all_widgets = []
        for dock in window._dock_names().values():
            if dock is not None and dock.widget() is not None:
                all_widgets.append(dock.widget())
                all_widgets.extend(dock.widget().findChildren(QWidget))
        assert widgets_over_cap(all_widgets, cap) == []
        # resizeEvent dispara o enforce sem erro
        window.resize(800, 600)
        window.close()
    finally:
        container.shutdown()


# ---------- puro: matriz exp×var ----------

def test_matrix_cells_pure():
    from app.ui.widgets.experiment_matrix_view import matrix_cells

    rows = [
        {"external_id": 1, "values": {1: 0.0, 2: 10.0}},
        {"external_id": 2, "values": {1: 5.0}},
        {"external_id": 3, "values": {}},
    ]
    cells, scales = matrix_cells(rows, [1, 2])
    assert cells == [[0.0, 10.0], [5.0, None], [None, None]]
    assert scales[1] == (0.0, 5.0)
    assert scales[2] == (10.0, 10.0)
    # cap de linhas
    big = [{"external_id": i, "values": {1: float(i)}} for i in range(500)]
    cells_big, _ = matrix_cells(big, [1])
    assert len(cells_big) == 200


def test_cell_text_and_color_pure():
    from app.ui.widgets.experiment_matrix_view import cell_text, cell_color

    assert cell_text(None) == "\u2014"
    assert cell_text(3.14159) == "3.142"
    # valor ausente → cinza neutro
    assert cell_color(None, (0.0, 1.0), "azul\u2192amarelo") == "#edf1f5"
    # extremos dão cores distintas
    lo_c = cell_color(0.0, (0.0, 10.0), "azul\u2192amarelo")
    hi_c = cell_color(10.0, (0.0, 10.0), "azul\u2192amarelo")
    assert lo_c != hi_c
    # escala degenerada → meio (sem divisão por zero)
    mid = cell_color(7.0, (3.0, 3.0), "azul\u2192amarelo")
    assert mid == cell_color(3.0, (3.0, 3.0), "azul\u2192amarelo")


def test_matrix_view_widget(qapp):
    from PySide6.QtGui import QColor

    from app.ui.widgets.experiment_matrix_view import ExperimentMatrixView

    view = ExperimentMatrixView()
    rows = [
        {"external_id": 1, "values": {1: 0.0, 2: 10.0}},
        {"external_id": 2, "values": {1: 5.0}},
    ]
    n = view.set_data(rows, [1, 2])
    assert n == 2
    assert view.table.rowCount() == 2
    assert view.table.columnCount() == 2
    it = view.table.item(0, 0)
    assert it.text() == "0"
    assert it.background().color() != QColor("#ffffff")
    # célula ausente → texto travessão e fundo neutro
    miss = view.table.item(1, 1)
    assert miss.text() == "\u2014"
    assert miss.background().color().name() == "#edf1f5"


def test_panel_four_formats(qapp, tmp_path):
    from app.infrastructure.experiment_repository import ExperimentRepository
    from app.ui.models.repository_paged_model import RepositoryPagedModel
    from app.ui.widgets.experiments_panel import ExperimentsPanel

    repo = ExperimentRepository(str(tmp_path / "m17.db"))
    repo.create_batch("b17", "lhs", 1, 6)
    repo.insert_result("b17", [1, 2], [[1.0, 5.0]] * 6)
    panel = ExperimentsPanel(RepositoryPagedModel(repo, page_size=6))
    assert panel.combo_format.count() == 4
    assert panel.view_stack.count() == 4
    panel.combo_format.setCurrentIndex(3)  # Matriz
    assert panel.view_stack.currentIndex() == 3
    assert panel.matrix_view.table.rowCount() == 6
    assert panel.matrix_view.table.columnCount() == 2
    # volta à tabela
    panel.combo_format.setCurrentIndex(0)
    assert panel.view_stack.currentIndex() == 0
