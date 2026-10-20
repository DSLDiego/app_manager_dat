# -*- coding: utf-8 -*-
"""Regressão da rodada 5: formatos de matrix, plots, batch filter, diffs de estudo e benchmark."""

import os
import time

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import numpy as np
import pytest
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication

from app.container import Container
from app.domain.entities import DistributionSpec


@pytest.fixture(scope="module")
def qapp():
    app = QApplication.instance() or QApplication([])
    yield app


@pytest.fixture()
def repo_with_two_batches(tmp_path):
    from app.infrastructure.experiment_repository import ExperimentRepository

    repo = ExperimentRepository(str(tmp_path / "exp.db"))
    repo.create_batch("batch_a", "lhs", 1, 3)
    repo.create_batch("batch_b", "monte_carlo", 2, 4)
    repo.insert_result(
        "batch_a",
        [1, 10002],
        [[1.0, 5.0], [2.0, 5.0], [3.0, 5.0]],
    )
    repo.insert_result(
        "batch_b",
        [1, 10002],
        [[10.0, 5.0], [20.0, 5.0], [30.0, 5.0], [40.0, 5.0]],
    )
    yield repo
    repo.close()


# ---------- heat matrix: transposta e tamanho de página ----------

def test_heat_matrix_transpose_layout(repo_with_two_batches, qapp):
    from app.ui.widgets.heat_matrix_panel import HeatMatrixPanel
    from app.infrastructure.experiment_repository import ExperimentRepository as R  # noqa: F401

    repo = repo_with_two_batches
    panel = HeatMatrixPanel()
    panel.load_from_repo(repo, [1, 10002])
    assert panel.table.rowCount() == 7  # 3 + 4 experimentos

    panel.chk_transpose.setChecked(True)
    assert panel.table.rowCount() == 2  # uma linha por variável
    assert panel.table.horizontalHeaderItem(0).text() == "Variável"
    assert panel.lbl_info.text().startswith("Matriz 2×7")

    panel.chk_transpose.setChecked(False)
    assert panel.table.rowCount() == 7
    assert panel.table.horizontalHeaderItem(0).text() == "#"


def test_heat_matrix_page_size(repo_with_two_batches, qapp):
    from app.ui.widgets.heat_matrix_panel import HeatMatrixPanel

    repo = repo_with_two_batches
    panel = HeatMatrixPanel()
    panel.load_from_repo(repo, [1, 10002])
    panel.spin_page_size.setValue(3)
    assert panel.table.rowCount() == 3
    assert "1/3" in panel.lbl_info.text()
    panel._next()
    assert "2/3" in panel.lbl_info.text()


# ---------- correlação com headers canônicos ----------

def test_correlation_headers_use_var_label(repo_with_two_batches, qapp):
    from app.ui.widgets.correlation_dialog import CorrelationDialog

    dialog = CorrelationDialog([1, 10002])
    labels = [dialog.table.horizontalHeaderItem(i).text() for i in range(2)]
    assert labels == ["$1", "$var2"]


# ---------- plots: histograma empírico e séries sobrepostas ----------

def test_plot_empirical_histogram(repo_with_two_batches, qapp):
    from app.infrastructure.distribution_registry import build_default_registry
    from app.ui.widgets.distribution_plot_dialog import DistributionPlotDialog

    registry = build_default_registry()
    dialog = DistributionPlotDialog(registry, exp_repo=repo_with_two_batches)
    assert dialog.combo_var.count() == 2
    dialog.combo_kind.setCurrentIndex(3)
    dialog.redraw()
    assert len(dialog.canvas._series) == 1
    label, xs, ys, valid = dialog.canvas._series[0]
    assert valid
    assert dialog.canvas.mode == "bar"
    assert abs(float(ys.sum()) - 1.0) < 1e-9  # histograma normalizado


def test_plot_empirical_empty_repo(qapp):
    from app.infrastructure.distribution_registry import build_default_registry
    from app.ui.widgets.distribution_plot_dialog import DistributionPlotDialog

    class EmptyRepo:
        def count(self):
            return 0

        def var_ids(self):
            return []

    dialog = DistributionPlotDialog(build_default_registry(), exp_repo=EmptyRepo())
    dialog.combo_kind.setCurrentIndex(3)
    dialog.redraw()
    assert dialog.canvas._series[0][0] == "(nenhuma)"


def test_plot_overlay_two_series(qapp):
    from app.infrastructure.distribution_registry import build_default_registry
    from app.ui.widgets.distribution_plot_dialog import DistributionPlotDialog

    dialog = DistributionPlotDialog(build_default_registry())
    dialog.combo_kind.setCurrentIndex(0)  # PDF linha
    dialog.redraw()
    assert len(dialog.canvas._series) == 1
    dialog.line_expr.setText("x**2")
    dialog.combo_kind.setCurrentIndex(2)  # f(x)
    dialog.redraw(keep_existing=True)
    assert len(dialog.canvas._series) == 2
    assert dialog.canvas._series[1][0] == "f(x)"


def test_plot_canvas_paints_with_legend(qapp):
    from app.ui.widgets.distribution_plot_dialog import PlotCanvas

    canvas = PlotCanvas()
    canvas.set_mode("line")
    canvas.add_series("a", np.array([0.0, 1.0, 2.0]), np.array([1.0, 2.0, 1.0]))
    canvas.add_series("b", np.array([0.0, 1.0, 2.0]), np.array([1.5, 1.8, 1.5]))
    canvas.render_reason = "test"
    from PySide6.QtGui import QImage

    img = QImage(400, 300, QImage.Format.Format_RGB32)
    canvas.resize(400, 300)
    canvas.repaint()
    # apenas garante que paint não quebra; smoke
    canvas.deleteLater()


# ---------- filtro por lote no modelo paginado ----------

def test_paged_model_batch_filter(repo_with_two_batches, qapp):
    from app.ui.models.repository_paged_model import RepositoryPagedModel

    model = RepositoryPagedModel(repo_with_two_batches)
    assert model.total_rows == 7

    model.set_batch_filter("batch_a")
    assert model.batch_filter == "batch_a"
    assert model.total_rows == 3
    assert all(row["batch_id"] == "batch_a" for row in model._rows)

    model.set_batch_filter("batch_b")
    assert model.total_rows == 4

    model.set_batch_filter(None)
    assert model.total_rows == 7


def test_fetch_page_returns_batch_id(repo_with_two_batches):
    rows = repo_with_two_batches.fetch_page(0, 10)
    assert {"batch_id", "external_id", "db_id", "values"} <= set(rows[0].keys())


def test_get_variable_values_batch_filter(repo_with_two_batches):
    all_values = repo_with_two_batches.get_variable_values(1)
    only_a = repo_with_two_batches.get_variable_values(1, batch_id="batch_a")
    assert sorted(all_values) == [1.0, 2.0, 3.0, 10.0, 20.0, 30.0, 40.0]
    assert sorted(only_a) == [1.0, 2.0, 3.0]


# ---------- estudo carregado filtra a tabela de experimentos ----------

def test_study_load_sets_batch_filter(tmp_path, qapp):
    from app.ui.main_window import MainWindow

    container = Container(base_dir=str(tmp_path / "study_load"), load_plugins=False)
    container.ensure_services()
    try:
        container.exp_repo.create_batch("batch_x", "lhs", 1, 2)
        container.exp_repo.insert_result("batch_x", [1], [[1.0], [2.0]])
        study_id = container.study_service.create(
            "Estudo Filtro",
            {1: DistributionSpec(provider="scipy", name="norm", params={"loc": 0.0, "scale": 1.0})},
            meta={
                "dat_path": "x.dat",
                "template_text": "T $1",
                "batch_id": "batch_x",
                "output_dir": str(tmp_path / "out"),
            },
        )
        window = MainWindow(container)
        window._load_study(study_id)
        assert window.exp_model.batch_filter == "batch_x"
        window._clear_batch_filter()
        assert window.exp_model.batch_filter is None
        window.close()
    finally:
        container.shutdown()


# ---------- diff de versões do estudo ----------

def test_build_diff_specs_and_meta():
    from app.ui.widgets.studies_dialog import StudiesDialog

    va = {
        "specs": {"1": {"provider": "scipy", "name": "norm", "params": {"loc": 0.0}}},
        "meta": {"batch_id": "b1", "output_dir": "/x"},
    }
    vb = {
        "specs": {
            "1": {"provider": "scipy", "name": "norm", "params": {"loc": 5.0}},
            "10002": {"provider": "fixed", "name": "value", "params": {"value": 1.0}},
        },
        "meta": {"batch_id": "b2", "output_dir": "/x"},
    }
    lines = StudiesDialog._build_diff(va, vb)
    assert len(lines) == 3
    assert "'b1' → 'b2'" in lines[2]


def test_build_diff_no_changes():
    from app.ui.widgets.studies_dialog import StudiesDialog

    study = {
        "specs": {"1": {"provider": "fixed", "name": "value", "params": {"value": 1.0}}},
        "meta": {"batch_id": "b1"},
    }
    assert StudiesDialog._build_diff(study, study) == []


# ---------- benchmark: render compilado ≥ 2x mais rápido ----------

def test_compiled_render_clearly_faster_than_regex():
    from app.core.parsing import compile_template, render_template

    var_ids = list(range(1, 101))
    var_ids += [10000 + i for i in range(1, 101)]
    template = " ".join(f"$({v})" for v in var_ids)
    values_row = {v: float(v) for v in var_ids}

    compiled = compile_template(template)

    t0 = time.perf_counter()
    for _ in range(400):
        render_template(template, values_row)
    t_regex = time.perf_counter() - t0

    t0 = time.perf_counter()
    for _ in range(400):
        compiled.render(values_row)
    t_compiled = time.perf_counter() - t0

    assert t_compiled * 2.0 < t_regex, (
        f"compilado ({t_compiled:.4f}s) deveria ser >= 2x mais rápido "
        f"que regex ({t_regex:.4f}s)"
    )
