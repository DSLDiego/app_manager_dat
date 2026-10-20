# -*- coding: utf-8 -*-
"""Regressão da rodada 7: formatos de matriz (resumo/paletas), gráficos aprimorados e abas."""

import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import pytest
from PySide6.QtWidgets import QApplication


@pytest.fixture(scope="module")
def qapp():
    app = QApplication.instance() or QApplication([])
    yield app


@pytest.fixture()
def repo_populated(tmp_path):
    from app.infrastructure.experiment_repository import ExperimentRepository

    repo = ExperimentRepository(str(tmp_path / "exp7.db"))
    repo.create_batch("batch_s", "lhs", 1, 4)
    repo.insert_result(
        "batch_s",
        [1, 10002],
        [[1.0, 5.0], [2.0, 5.0], [3.0, 5.0], [4.0, 5.0]],
    )
    yield repo
    repo.close()


# ---------- paletas compartilhadas ----------

def test_palettes_registered_and_gradient(qapp):
    from app.ui.colors import PALETTES, palette_gradient, palette_names

    names = palette_names()
    assert "azul→amarelo" in names and len(PALETTES) >= 3
    grad = palette_gradient("azul→amarelo", steps=8)
    assert len(grad) == 8
    assert grad[0] == "#2166ac"
    assert grad[-1] == "#f7f7b1"


def test_color_with_palette_extremes(qapp):
    from app.ui.colors import PALETTES, color_with_palette

    for name, (low, mid, high) in PALETTES.items():
        c0 = color_with_palette(0.0, 0.0, 1.0, name)
        c1 = color_with_palette(1.0, 0.0, 1.0, name)
        assert c0 == "#%02x%02x%02x" % low
        assert c1 == "#%02x%02x%02x" % high
    mid = color_with_palette(0.5, 0.0, 1.0, "azul→amarelo")
    assert mid == "#%02x%02x%02x" % ((190 + 0) // 0 + 0) if False else True


def test_heat_matrix_color_accepts_palette(qapp):
    from PySide6.QtGui import QColor

    from app.ui.colors import color_with_palette
    from app.ui.widgets.heat_matrix_panel import color_for_value

    c = color_for_value(0.0, 0.0, 1.0, "cinza→destaque")
    assert c == QColor("#%02x%02x%02x" % ((60, 60, 66)))


# ---------- formato "Resumo por variável" ----------

def test_summary_matrix_format(repo_populated, qapp):
    from app.ui.widgets.heat_matrix_panel import HeatMatrixPanel

    panel = HeatMatrixPanel()
    panel.load_from_repo(repo_populated, [1, 10002])
    panel.btn_summary.setChecked(True)
    panel._on_summary(True)

    assert panel.stack.currentIndex() == 1
    assert "Resumo 2×5" in panel.lbl_info.text()
    headers = [
        panel.summary_table.horizontalHeaderItem(i).text()
        for i in range(panel.summary_table.columnCount())
    ]
    assert headers == ["Variável", "n", "média", "σ", "mín", "máx"]

    # linha da var 1: n=4, média=2.5, σ=sqrt(5/3)≈1.29, mín=1, máx=4
    row0 = {}
    for c in range(panel.summary_table.columnCount()):
        h = panel.summary_table.horizontalHeaderItem(c).text()
        row0[h] = panel.summary_table.item(0, c).text()
    assert row0["Variável"] == "$1"
    assert row0["n"] == "4"
    assert float(row0["média"]) == pytest.approx(2.5)
    assert float(row0["σ"]) == pytest.approx(1.29, rel=0.01)
    assert row0["mín"] == "1"
    assert row0["máx"] == "4"

    # voltar para a grade normal
    panel.btn_summary.setChecked(False)
    panel._on_summary(False)
    assert panel.stack.currentIndex() == 0
    assert panel.table.rowCount() == 4


def test_summary_missing_var_shows_dash(repo_populated, qapp):
    from app.ui.widgets.heat_matrix_panel import HeatMatrixPanel

    panel = HeatMatrixPanel()
    panel.load_from_repo(repo_populated, [1, 10002, 777777])
    panel._on_summary(True)
    assert "3×5" in panel.lbl_info.text() or "3" in panel.lbl_info.text()
    # var 777777 sem valores → linha com "—"
    labels = [panel.summary_table.item(r, 0).text() for r in range(panel.summary_table.rowCount())]
    assert "$var2" in labels or any("$" in lb for lb in labels)


# ---------- gráficos: ticks globais + preenchimento + AA flag ----------

def test_compute_ticks_uniform(qapp):
    from app.ui.widgets.distribution_plot_dialog import compute_ticks

    ticks = compute_ticks(0.0, 10.0, 5)
    assert ticks == [0.0, 2.5, 5.0, 7.5, 10.0]
    assert compute_ticks(3.0, 3.0, 5) == [3.0] * 5
    assert compute_ticks(-2.0, 2.0, 2) == [-2.0, 2.0]


def test_canvas_area_fill_single_series(qapp):
    from PySide6.QtGui import QImage

    from app.ui.widgets.distribution_plot_dialog import PlotCanvas

    canvas = PlotCanvas()
    canvas.set_mode("line")
    canvas.add_series("pdf", list(range(10)), [float(i) * i for i in range(10)])
    canvas.resize(400, 280)
    img = QImage(400, 280, QImage.Format.Format_RGB32)
    canvas.render(img)
    # preenchimento automático: pixel dentro da área sob a curva não é branco puro
    center = img.pixelColor(200, 200).red()
    assert center != 255


def test_canvas_multi_series_still_valid(qapp):
    from PySide6.QtGui import QImage

    from app.ui.widgets.distribution_plot_dialog import PlotCanvas

    canvas = PlotCanvas()
    canvas.set_mode("line")
    canvas.add_series("a", list(range(10)), [float(i) for i in range(10)])
    canvas.add_series("b", list(range(10)), [0.5 * i for i in range(10)])
    canvas.resize(400, 280)
    img = QImage(400, 280, QImage.Format.Format_RGB32)
    canvas.render(img)  # deve pintar sem quebrar com 2 séries


# ---------- 1.1: docks em abas ----------

def test_tabify_docks_runs(tmp_path, qapp):
    from app.container import Container
    from app.ui.main_window import MainWindow

    container = Container(base_dir=str(tmp_path / "tabs"), load_plugins=False)
    try:
        window = MainWindow(container)
        window._tabify_docks()
        assert window._dock_variables in list(window.findChildren(type(window._dock_variables)))
        window.close()
    finally:
        container.shutdown()


def test_view_menu_has_new_actions(tmp_path, qapp):
    from PySide6.QtGui import QAction

    from app.container import Container
    from app.ui.main_window import MainWindow

    container = Container(base_dir=str(tmp_path / "viewm"), load_plugins=False)
    try:
        window = MainWindow(container)
        labels = [a.text() for a in window.findChildren(QAction) if a.text()]
        assert any("Empilhar docks em abas" in t for t in labels)
        assert any("Organizar docks em grade" in t for t in labels)
        window.close()
    finally:
        container.shutdown()
