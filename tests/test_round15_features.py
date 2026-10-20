"""Regressão da rodada 15: zoom/pan nos gráficos, histogramas em fluxo, árvore de estudos."""

import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import numpy as np
import pytest
from PySide6.QtWidgets import QApplication


@pytest.fixture(scope="module")
def qapp():
    app = QApplication.instance() or QApplication([])
    yield app


# ---------- puro: zoom / pan ----------

def test_zoom_span_pure():
    from app.ui.widgets.distribution_plot_dialog import zoom_span

    assert zoom_span(0.0, 10.0, 0.5) == (2.5, 7.5)
    assert zoom_span(0.0, 10.0, 1.0) == (0.0, 10.0)
    lo, hi = zoom_span(4.0, 6.0, 2.0)
    assert (lo, hi) == (3.0, 7.0)


def test_pan_span_pure():
    from app.ui.widgets.distribution_plot_dialog import pan_span

    assert pan_span(0.0, 10.0, 0.1) == (1.0, 11.0)
    assert pan_span(0.0, 10.0, -0.2) == (-2.0, 8.0)
    assert pan_span(3.0, 3.0, 5.0) == (3.0, 3.0)


def test_zoom_at_keeps_anchor_fixed():
    from app.ui.widgets.distribution_plot_dialog import zoom_at

    # âncora no centro: janela simétrica
    assert zoom_at(0.0, 10.0, 0.5, 0.5) == (2.5, 7.5)
    # âncora na borda esquerda: borda fica fixa
    assert zoom_at(0.0, 10.0, 0.0, 0.5) == (0.0, 5.0)
    # âncora na borda direita
    assert zoom_at(0.0, 10.0, 1.0, 0.5) == (5.0, 10.0)


def test_clamp_zoom_limits():
    from app.ui.widgets.distribution_plot_dialog import clamp_zoom

    # dentro dos dados: passa direto
    assert clamp_zoom(2.0, 3.0, 0.0, 10.0) == (2.0, 3.0)
    # maior que os dados: volta à vista cheia
    assert clamp_zoom(-5.0, 15.0, 0.0, 10.0) == (0.0, 10.0)
    # zoom demais: respeita min_frac
    lo, hi = clamp_zoom(4.999, 5.001, 0.0, 10.0, min_frac=0.002)
    assert hi - lo == pytest.approx(0.02)


# ---------- PlotCanvas: estado de zoom ----------

def _canvas_with_series():
    from app.ui.widgets.distribution_plot_dialog import PlotCanvas

    canvas = PlotCanvas()
    canvas.mode = "bar"
    xs = np.arange(11, dtype=float)
    ys = np.linspace(1.0, 5.0, 11)
    canvas.add_series("s", xs, ys, True)
    return canvas


def test_wheel_zoom_and_reset(qapp):
    canvas = _canvas_with_series()
    assert canvas._zoom is None
    assert canvas.wheel_zoom(120, 0.5) is True
    z = canvas._zoom
    assert z is not None and z[1] - z[0] < 10.0  # aproximou
    # zoom-out além da vista cheia → volta aos extremos dos dados
    canvas.wheel_zoom(-120, 0.5)
    canvas.wheel_zoom(-120, 0.5)
    full = canvas.data_extents()
    assert (canvas._zoom[0], canvas._zoom[1]) == (full[0], full[1])
    canvas.reset_view()
    assert canvas._zoom is None


def test_wheel_zoom_without_series_is_noop(qapp):
    from app.ui.widgets.distribution_plot_dialog import PlotCanvas

    canvas = PlotCanvas()
    assert canvas.wheel_zoom(120, 0.5) is False
    assert canvas.drag_offset(10, 500.0) is False


def test_drag_offset_pans_within_bounds(qapp):
    canvas = _canvas_with_series()
    canvas._drag_zoom0 = (2.0, 8.0, 1.0, 5.0)
    ok = canvas.drag_offset(50, 500.0)
    assert ok is True
    z = canvas._zoom
    # arrasto p/ direita → janela desloca p/ esquerda
    assert z[0] == pytest.approx(1.4)
    assert z[1] == pytest.approx(7.4)
    # borda: janela não sai dos dados
    canvas._drag_zoom0 = (2.0, 8.0, 1.0, 5.0)
    canvas.drag_offset(5000, 500.0)
    assert canvas._zoom[0] == pytest.approx(0.0)


def test_canvas_renders_with_zoom(qapp):
    canvas = _canvas_with_series()
    canvas._zoom = (2.0, 8.0, 1.0, 5.0)
    canvas.grab()  # paintEvent com janela ampliada não pode quebrar
    canvas.reset_view()
    canvas.grab()


def test_dialog_zoom_buttons(qapp):
    from app.ui.widgets.distribution_plot_dialog import DistributionPlotDialog

    dlg = DistributionPlotDialog()
    assert dlg.btn_zoom_in.text() == "+"
    assert dlg.btn_zoom_out.text() == "−"
    assert dlg.btn_zoom_reset.text() == "Reset zoom"
    import numpy as _np

    dlg.canvas.add_series("a", _np.arange(10, dtype=float), _np.ones(10), True)
    dlg.btn_zoom_in.click()
    assert dlg.canvas._zoom is not None
    dlg.btn_zoom_reset.click()
    assert dlg.canvas._zoom is None
    dlg.btn_zoom_out.click()
    assert dlg.canvas._zoom is not None


# ---------- histogramas em fluxo ----------

def test_hist_values_pure():
    from app.ui.widgets.hist_flow_view import hist_values

    assert hist_values([]) == ([], [])
    assert hist_values(None) == ([], [])
    vals = [float(i) for i in range(24)]
    centers, counts = hist_values(vals, bins=6)
    assert len(centers) == len(counts) == 6
    assert sum(counts) == 24
    assert centers == sorted(centers)


def test_flow_order_clamps():
    from app.ui.widgets.hist_flow_view import flow_order, MAX_FLOW_STAGES

    assert flow_order([3, 1, 2]) == [3, 1, 2]
    ids = list(range(50))
    out = flow_order(ids)
    assert len(out) == MAX_FLOW_STAGES
    assert out == ids[:MAX_FLOW_STAGES]


def test_hist_flow_view_stages_and_arrows(qapp):
    from PySide6.QtWidgets import QLabel

    from app.ui.widgets.distribution_plot_dialog import PlotCanvas
    from app.ui.widgets.hist_flow_view import HistFlowView

    view = HistFlowView()
    values_map = {
        1: [1.0, 1.2, 0.9, 1.1],
        2: [5.0, 5.5, 4.8],
        3: [2.0, 2.1, 1.9, 2.3, 2.0],
    }
    n = view.set_values_map(values_map)
    assert n == 3
    widgets = [
        view.strip_layout.itemAt(i).widget() for i in range(view.strip_layout.count())
    ]
    canvases = [w for w in widgets if isinstance(w, PlotCanvas)]
    arrows = [w for w in widgets if isinstance(w, QLabel) and w.text() == "\u2192"]
    assert len(canvases) == 3 and len(arrows) == 2
    assert [sid for sid, _st in view._stages] == [1, 2, 3]
    # sem dados: estágio vazio mas a cadeia existe
    n_empty = view.set_values_map({9: []})
    assert n_empty == 1


# ---------- estudos em lista de listas ----------

def test_study_tree_pure():
    from app.ui.widgets.studies_tree_view import study_tree

    studies = [
        {"id": 1, "name": "A", "meta": {"batch_id": "b1"}},
        {"id": 2, "name": "B", "meta": {}},
    ]
    rows = study_tree(studies, {1: ["v1", "v2"]})
    assert rows[0][0].startswith("#1 — A") and "batch=b1" in rows[0][0]
    assert rows[0][1] == ["v1", "v2"]
    assert rows[1][1] == ["(nenhuma versão)"]


def test_studies_tree_view_widget(qapp):
    from app.ui.widgets.studies_tree_view import StudiesTreeView

    tree = StudiesTreeView()
    studies = [
        {"id": 1, "name": "A", "meta": {"batch_id": "b1"}},
        {"id": 2, "name": "B", "meta": {}},
    ]
    n = tree.populate(studies, {1: ["v1"]})
    assert n == 2
    assert tree.topLevelItemCount() == 2
    assert tree.topLevelItem(0).childCount() == 1
    assert tree.topLevelItem(1).childCount() == 1  # placeholder
    # seleção: topo → 0; filho → pai (0); nada → None
    tree.setCurrentItem(tree.topLevelItem(0))
    assert tree.selected_study_row() == 0
    tree.setCurrentItem(tree.topLevelItem(0).child(0))
    assert tree.selected_study_row() == 0
    tree.setCurrentItem(tree.topLevelItem(1))
    assert tree.selected_study_row() == 1
    tree.setCurrentItem(None)
    assert tree.selected_study_row() is None


def test_studies_dialog_tree_toggle(qapp):
    from app.services.study_service import StudyService
    from app.ui.widgets.studies_dialog import StudiesDialog
    from app.ui.widgets.studies_tree_view import StudiesTreeView

    svc = StudyService(_reg())
    svc.create("Estudo A", {}, meta={"batch_id": "b1"})
    sid = svc.create("Estudo B", {}, meta={})
    dlg = StudiesDialog(svc)
    assert dlg.view_stack.count() == 2
    assert dlg.view_stack.currentIndex() == 0
    # alternar p/ árvore
    dlg.btn_format.click()
    assert dlg.view_stack.currentIndex() == 1
    assert dlg.btn_format.text() == "Formato: Lista"
    assert isinstance(dlg.tree_view, StudiesTreeView)
    assert dlg.tree_view.topLevelItemCount() == 2
    # seleção na árvore → _current_index resolve (list() é updated_at DESC)
    order = [s["id"] for s in svc.list_studies()]
    idx_expected = order.index(sid)
    dlg.tree_view.setCurrentItem(dlg.tree_view.topLevelItem(idx_expected))
    assert dlg._current_index() == idx_expected
    study = dlg._current_study()
    assert study is not None and study["id"] == sid
    # voltar p/ lista
    dlg.btn_format.click()
    assert dlg.view_stack.currentIndex() == 0
    assert dlg._current_index() is None  # lista sem seleção


def _reg():
    from app.infrastructure.study_repository import StudyRepository

    return StudyRepository(":memory:")


# ---------- editor compacto ----------

def test_code_editor_tight_viewport_and_signals(qapp):
    from app.ui.editor.code_editor import CodeEditor

    editor = CodeEditor()
    # r15: viewport comprimido, mas documentMargin NÃO pode mudar
    # (setDocumentMargin(<4) quebra modificationChanged no PySide6 6.11.1)
    assert editor.viewportMargins().top() == 1
    assert editor.document().documentMargin() == 4


def test_code_editor_modification_signal_alive(qapp):
    """Regressão do quirk: dirty marker depende deste sinal."""
    from app.ui.editor.editor_widget import EditorWidget

    tab = EditorWidget()
    fired = []
    tab.modified_changed.connect(lambda v: fired.append(v))
    tab.editor.document().setModified(True)
    assert fired and fired[-1] is True
    tab.editor.document().setModified(False)
    assert fired[-1] is False
