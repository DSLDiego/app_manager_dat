# -*- coding: utf-8 -*-
"""Regressão da rodada 8: grade de histograms, salvar template, re-ler .dat, format_tick."""

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

    repo = ExperimentRepository(str(tmp_path / "exp8.db"))
    repo.create_batch("batch_h", "lhs", 1, 30)
    rng_values = [
        [float(i % 7), float(i % 3) + 10.0] for i in range(30)
    ]
    repo.insert_result("batch_h", [1, 10002], rng_values)
    yield repo
    repo.close()


# ---------- grade de mini-histogramas ----------

def test_histogram_bins(qapp):
    from app.ui.widgets.histogram_grid_panel import histogram_bins

    bins, n = histogram_bins([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], bins=5)
    assert n == 10
    assert len(bins) == 5
    assert abs(sum(h for _, h in bins) - 1.0) < 1e-9
    empty_bins, empty_n = histogram_bins([float("nan"), float("inf")])
    assert empty_n == 0 and empty_bins == []


def test_grid_layout_4x3(qapp, repo_populated):
    from app.ui.widgets.histogram_grid_panel import HistogramGridPanel

    panel = HistogramGridPanel()
    panel.load_from_repo(repo_populated)
    assert panel.table.rowCount() == 3 and panel.table.columnCount() == 4
    assert panel.lbl_info.text().startswith("Variáveis 2")
    cells = [
        panel.table.cellWidget(r, c)
        for r in range(3) for c in range(4)
        if panel.table.cellWidget(r, c) is not None
    ]
    assert 1 <= len(cells) <= 2
    mini = cells[0]
    assert mini._n == 30
    assert len(mini._bins) == 20


def test_grid_pagination(qapp, repo_populated):
    from app.ui.widgets.histogram_grid_panel import HistogramGridPanel

    more_repo = repo_populated
    panel = HistogramGridPanel()
    # 14 variáveis para testar paginação (12 + 2)
    panel.load_from_repo(more_repo, list(range(200, 214)))
    assert "1/2" in panel.lbl_info.text()
    panel._next()
    assert "2/2" in panel.lbl_info.text()
    panel._next()  # retorna à página 2 (não avança mais)
    assert "2/2" in panel.lbl_info.text()
    panel._prev()
    assert "1/2" in panel.lbl_info.text()


def test_set_values_map_without_repo(qapp):
    from app.ui.widgets.histogram_grid_panel import HistogramGridPanel

    panel = HistogramGridPanel()
    panel.set_values_map({1: [0.0, 0.5, 1.0], 10002: [5.0, 5.0, 5.0]})
    assert sorted(panel._var_ids) == [1, 10002]
    assert panel.lbl_info.text().startswith("Variáveis 2")


# ---------- salvar template / re-ler .dat ----------

def test_save_template_version(tmp_path, qapp, monkeypatch):
    from app.container import Container
    from app.ui import main_window as mw
    from app.ui.main_window import MainWindow

    monkeypatch.setattr(
        mw.QMessageBox, "warning", staticmethod(lambda *a, **k: None)
    )
    container = Container(base_dir=str(tmp_path / "tpl"), load_plugins=False)
    try:
        window = MainWindow(container)
        window.editor_tabs.new_tab("TEMPLATE $var1")
        window._save_template_version()
        assert window._last_template_version_id is not None
        content = container.template_repo.get_version(
            window._last_template_version_id
        )["content"]
        assert "TEMPLATE" in content
        # segunda versão na mesma árvore
        window.editor_tabs.new_tab("TEMPLATE $var1 $2")
        window._save_template_version()
        versions = container.template_repo.list_versions(window._main_template_id)
        assert len(versions) >= 2
        window.close()
    finally:
        container.shutdown()


def test_save_template_empty_warns(tmp_path, qapp, monkeypatch):
    from app.container import Container
    from app.ui import main_window as mw
    from app.ui.main_window import MainWindow

    warns = []
    monkeypatch.setattr(
        mw.QMessageBox, "warning",
        staticmethod(lambda *a, **k: warns.append(a[2])),
    )
    container = Container(base_dir=str(tmp_path / "tplE"), load_plugins=False)
    try:
        window = MainWindow(container)
        window.editor_tabs.new_tab("   ")
        window._save_template_version()
        assert warns and "Nada para salvar" in warns[0]
        window.close()
    finally:
        container.shutdown()


def test_reload_dat_file_requires_file(tmp_path, qapp, monkeypatch):
    from app.container import Container
    from app.ui import main_window as mw
    from app.ui.main_window import MainWindow

    infos = []
    monkeypatch.setattr(
        mw.QMessageBox, "information",
        staticmethod(lambda *a, **k: infos.append(a[2])),
    )
    container = Container(base_dir=str(tmp_path / "rld"), load_plugins=False)
    try:
        window = MainWindow(container)
        window.editor_tabs.new_tab("sem arquivo")  # Sem título — Sem arquivo
        window._reload_dat_file()
        assert infos and "não está ligada" in infos[0]
        window.close()
    finally:
        container.shutdown()


def test_reload_dat_file_updates_tokens(tmp_path, qapp, monkeypatch):
    from pathlib import Path

    from app.container import Container
    from app.ui.main_window import MainWindow

    dat = tmp_path / "meu.dat"
    dat.write_text("INICIAL $var1", encoding="utf-8")
    container = Container(base_dir=str(tmp_path / "rld2"), load_plugins=False)
    try:
        window = MainWindow(container)
        window.editor_tabs.open_file(str(dat))
        editor = window.editor_tabs.current_editor()
        assert editor.file_path == str(dat)
        # altera no DISCO e re-lê:
        dat.write_text("ATUALIZADO $var1 $10002 $3", encoding="utf-8")
        window._reload_dat_file()
        assert "ATUALIZADO" in editor.text()
        # $3→3, $var1→10001, $10002→10002 (namespaces normalizados)
        assert sorted(window.variables_panel.var_map) == [3, 10001, 10002]
        window.close()
    finally:
        container.shutdown()


# ---------- 1.2: gráficos — format_tick e título ----------

def test_format_tick(qapp):
    from app.ui.widgets.distribution_plot_dialog import format_tick

    assert format_tick(0) == "0"
    assert format_tick(1234) == "1.2k"
    assert format_tick(-1234567) == "-1.2M"
    assert format_tick(56.789) == "56.79"
    assert format_tick(0.0012) == "1.2m"
    assert format_tick(0.0001).endswith("e-04")


def test_canvas_title(qapp):
    from PySide6.QtGui import QImage

    from app.ui.widgets.distribution_plot_dialog import PlotCanvas

    canvas = PlotCanvas()
    canvas.set_title("Minha Distribuição")
    canvas.add_series("s", [0.0, 1.0, 2.0], [0.0, 1.0, 0.5])
    canvas.resize(300, 200)
    img = QImage(300, 200, QImage.Format.Format_RGB32)
    canvas.render(img)  # paint com topo cuja não quebra


def test_plot_dialog_sets_title(qapp):
    from app.infrastructure.distribution_registry import build_default_registry
    from app.ui.widgets.distribution_plot_dialog import DistributionPlotDialog

    dialog = DistributionPlotDialog(build_default_registry())
    dialog.combo_kind.setCurrentIndex(0)
    dialog.redraw()
    code = dialog.combo_distcombo.currentText()
    assert dialog.canvas._title == f"{code} (pdf)"
    dialog.line_expr.setText("x**2")
    dialog.combo_kind.setCurrentIndex(2)
    dialog.redraw()
    assert dialog.canvas._title == "f(x) = x**2"


# ---------- toolbar e docks extras ----------

def test_panels_have_action_buttons(tmp_path, qapp):
    from PySide6.QtWidgets import QToolBar

    from app.container import Container
    from app.ui.main_window import MainWindow

    container = Container(base_dir=str(tmp_path / "tb2"), load_plugins=False)
    try:
        window = MainWindow(container)
        # botões migrados da toolbar para os painéis
        assert window.experiments_panel.btn_generate.text() == "Gerar .dats"
        assert window.experiments_panel.btn_save_tpl.text() == "Salvar template"
        assert window.variables_panel.btn_reload_dat.text() == "Re-ler .dat"
        # sem toolbar duplicada
        assert not window.findChildren(QToolBar)
        window.close()
    finally:
        container.shutdown()


def test_hist_dock_exists_and_wires(tmp_path, qapp):
    from app.container import Container
    from app.ui.main_window import MainWindow

    container = Container(base_dir=str(tmp_path / "hd"), load_plugins=False)
    try:
        window = MainWindow(container)
        window.exp_model.refresh()
        assert window.hist_panel._var_ids is not None
        window._arrange_docks_grid()
        window._tabify_docks()
        window.close()
    finally:
        container.shutdown()
