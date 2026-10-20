"""Regressão da rodada 19: curva normal nos histogramas, CSV da matriz, recentes."""

import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import numpy as np
import pytest
from PySide6.QtWidgets import QApplication


@pytest.fixture(scope="module")
def qapp():
    app = QApplication.instance() or QApplication([])
    yield app


# ---------- puro: curva normal ----------

def test_normal_curve_pure():
    from app.ui.widgets.histogram_grid_panel import normal_curve

    assert normal_curve([]) == ([], [])
    assert normal_curve([1.0]) == ([], [])          # < 3 pontos
    assert normal_curve([5.0, 5.0, 5.0]) == ([], [])  # desvio 0
    rng = np.random.default_rng(42)
    vals = rng.normal(10.0, 2.0, 500).tolist()
    xs, ys = normal_curve(vals)
    assert len(xs) == len(ys) == 64
    assert min(xs) < 10.0 - 2.0 and max(xs) > 10.0 + 2.0
    # pico da curva perto da média; ys na escala de fração por bin
    peak = max(ys)
    assert 0.0 < peak < 1.0
    assert xs[ys.index(peak)] == pytest.approx(10.0, abs=0.5)


def test_minihistogram_fit_toggle_and_paint(qapp):
    from app.ui.widgets.histogram_grid_panel import MiniHistogram

    cell = MiniHistogram(1)
    rng = np.random.default_rng(7)
    vals = rng.normal(0.0, 1.0, 200).tolist()
    cell.set_values(vals)
    assert cell.show_fit is False
    cell.set_show_fit(True)
    assert cell.show_fit is True
    cell.grab()  # pinta barras + curva sem quebrar
    cell.set_values([1.0, 2.0])  # poucos dados → curva omitida
    cell.grab()


def test_hist_panel_fit_checkbox(qapp, tmp_path):
    from app.infrastructure.experiment_repository import ExperimentRepository
    from app.ui.widgets.histogram_grid_panel import HistogramGridPanel, MiniHistogram

    repo = ExperimentRepository(str(tmp_path / "m19.db"))
    repo.create_batch("b19", "lhs", 1, 2)
    rng = np.random.default_rng(3)
    repo.insert_result("b19", [1], [[v] for v in rng.normal(5.0, 1.0, 50)])
    panel = HistogramGridPanel()
    panel.load_from_repo(repo)
    assert panel.chk_fit.text() == "Curva normal"
    panel.chk_fit.setChecked(True)
    cell = panel.table.cellWidget(0, 0)
    assert isinstance(cell, MiniHistogram) and cell.show_fit is True
    panel.chk_fit.setChecked(False)
    assert cell.show_fit is False


# ---------- puro: CSV da matriz ----------

def test_matrix_csv_pure():
    from app.ui.widgets.experiment_matrix_view import matrix_csv

    rows = [
        {"external_id": 1, "values": {1: 1.5, 2: 10.0}},
        {"external_id": 2, "values": {1: 2.25}},
    ]
    csv = matrix_csv(rows, [1, 2])
    lines = csv.strip().split("\n")
    assert lines[0] == "experimento;$1;$2"
    assert lines[1] == "1;1.5;10"
    assert lines[2] == "2;2.25;"  # ausente → vazio
    assert csv.endswith("\n")


def test_panel_export_matrix_csv(tmp_path, qapp, monkeypatch):
    from PySide6.QtWidgets import QFileDialog

    from app.infrastructure.experiment_repository import ExperimentRepository
    from app.ui.models.repository_paged_model import RepositoryPagedModel
    from app.ui.widgets.experiments_panel import ExperimentsPanel

    repo = ExperimentRepository(str(tmp_path / "m19x.db"))
    repo.create_batch("b19x", "lhs", 1, 4)
    repo.insert_result("b19x", [1, 2], [[1.0, 5.0]] * 4)
    panel = ExperimentsPanel(RepositoryPagedModel(repo, page_size=4))
    target = tmp_path / "matriz.csv"
    QFileDialog.getSaveFileName = staticmethod(
        lambda *a, **k: (str(target), "CSV (*.csv)")
    )
    panel._export_matrix_csv()
    content = target.read_text(encoding="utf-8")
    assert content.startswith("experimento;$1;$2\n")
    assert content.count("\n") == 5  # header + 4 experimentos


def test_panel_export_matrix_cancelled(qapp, tmp_path, monkeypatch):
    from PySide6.QtWidgets import QFileDialog

    from app.infrastructure.experiment_repository import ExperimentRepository
    from app.ui.models.repository_paged_model import RepositoryPagedModel
    from app.ui.widgets.experiments_panel import ExperimentsPanel

    repo = ExperimentRepository(str(tmp_path / "m19y.db"))
    repo.create_batch("b19y", "lhs", 1, 2)
    repo.insert_result("b19y", [1], [[1.0]] * 2)
    panel = ExperimentsPanel(RepositoryPagedModel(repo, page_size=2))
    QFileDialog.getSaveFileName = staticmethod(lambda *a, **k: ("", ""))
    panel._export_matrix_csv()  # não explode nem cria arquivo


# ---------- recentes ----------

def test_recent_push_pure():
    from app.ui.editor.editor_tabs import recent_push

    assert recent_push([], "a") == ["a"]
    assert recent_push(["a", "b"], "c") == ["c", "a", "b"]
    assert recent_push(["a", "b"], "a") == ["a", "b"]  # move p/ frente
    assert len(recent_push(["x"] * 9 + ["y"], "z", cap=8)) == 8
    assert recent_push(["a"], "", cap=0) == []


def test_recent_menu_flow(tmp_path, qapp, monkeypatch):
    from PySide6.QtCore import QSettings

    from app.container import Container
    from app.ui.main_window import MainWindow

    # r26: recentes persistem entre sessões — limpa antes/depois
    QSettings("datstudio", "dtengine").remove("recent/files")
    container = Container(base_dir=str(tmp_path / "c19"), load_plugins=False)
    try:
        window = MainWindow(container)
        # menu vazio no início
        assert window.menu_recent.actions()[0].isEnabled() is False
        # abre 2 arquivos de verdade
        f1 = tmp_path / "um.dat"
        f2 = tmp_path / "dois.dat"
        f1.write_text("$1 = 0.1\n", encoding="utf-8")
        f2.write_text("$2 = 0.2\n", encoding="utf-8")
        window.editor_tabs.open_file(str(f1))
        window.editor_tabs.open_file(str(f2))
        assert window._recent == [str(f2), str(f1)]
        labels = [a.text() for a in window.menu_recent.actions()]
        assert "dois.dat" in labels and "um.dat" in labels
        # reabrir f1 move p/ frente
        window.editor_tabs.open_file(str(f1))
        assert window._recent[0] == str(f1)
        # cap respeitado
        for i in range(10):
            fx = tmp_path / f"x{i}.dat"
            fx.write_text(f"$1 = {i}\n", encoding="utf-8")
            window.editor_tabs.open_file(str(fx))
        assert len(window._recent) <= 8
        # limpar
        window._clear_recent()
        assert window._recent == []
        assert window.menu_recent.actions()[0].isEnabled() is False
        window.close()
    finally:
        QSettings("datstudio", "dtengine").remove("recent/files")
        container.shutdown()
