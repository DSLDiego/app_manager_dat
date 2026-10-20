"""Regressão da rodada 13: cartões (grid n×m), fluxo de uso, ticks/labels nos gráficos."""

import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import pytest
from PySide6.QtWidgets import QApplication, QStackedWidget


@pytest.fixture(scope="module")
def qapp():
    app = QApplication.instance() or QApplication([])
    yield app


# ---------- puro: card_grid / scales / flow ----------

def test_card_grid_pure():
    from app.ui.widgets.experiment_cards_view import card_grid

    assert card_grid(13, cols=4) == (4, 4, 13)
    assert card_grid(0, cols=4) == (1, 4, 0)
    assert card_grid(120, cols=4) == (30, 4, 60)  # clampa em MAX_CARDS=60
    assert card_grid(7, cols=1) == (7, 1, 7)


def test_global_scales():
    from app.ui.widgets.experiment_cards_view import global_scales

    rows = [
        {"external_id": 1, "values": {1: 2.0, 2: 0.5}},
        {"external_id": 2, "values": {1: 4.0}},
    ]
    scales = global_scales(rows, [1, 2])
    assert scales[1] == (2.0, 4.0)
    assert scales[2] == (0.5, 0.5)
    empty = global_scales(rows, [9])
    assert empty[9] == (0.0, 0.0)


def test_flow_model_and_next_pending():
    from app.ui.widgets.usage_flow_panel import flow_model, next_pending

    empty = {}
    pend = next_pending(empty)
    assert pend == "tpl"
    assert next_pending({"template_hash": True}) == "dist"
    assert next_pending({"template_hash": True, "specs": True, "sampling": True}) == "dats"
    full = {
        "template_hash": True, "specs": True, "sampling": True,
        "output_dir": True, "template_version_id": True, "has_studies": True,
    }
    assert next_pending(full) is None
    steps = flow_model(full)
    assert all(done for _, _, done in steps) and [x[0] for x in steps][0] == "tpl"


# ---------- widgets dos painéis ----------

def test_flow_panel_renders_and_clicks(qapp):
    from app.ui.widgets.usage_flow_panel import UsageFlowPanel, next_pending

    panel = UsageFlowPanel()
    assert panel.list.count() == 6
    panel.refresh({})
    assert panel.lbl_head.text().startswith("Próxima etapa:")
    # clique na etapa → actionRequested(sid)
    emitted = []
    panel.actionRequested.connect(lambda sid: emitted.append(sid))
    panel._on_step_clicked(panel.list.item(3))
    assert emitted == ["dats"]
    # estado completo
    panel.refresh({
        "template_hash": True, "specs": True, "sampling": True,
        "output_dir": True, "template_version_id": True, "has_studies": True,
    })
    assert "completo" in panel.lbl_head.text().lower()
    panel.btn_next_step.click()  # emit actionRequested do "tpl" (estado foi resetado? mantém _state)


def test_flow_panel_next_step_emits(qapp):
    from app.ui.widgets.usage_flow_panel import UsageFlowPanel

    panel = UsageFlowPanel()
    emitted = []
    panel.actionRequested.connect(lambda sid: emitted.append(sid))
    panel.btn_next_step.click()
    assert emitted == ["tpl"]
    panel.refresh({"template_hash": True})
    panel.btn_next_step.click()
    assert emitted == ["tpl", "dist"]


def test_model_page_rows(qapp, tmp_path):
    from app.infrastructure.experiment_repository import ExperimentRepository
    from app.ui.models.repository_paged_model import RepositoryPagedModel

    repo = ExperimentRepository(str(tmp_path / "m13.db"))
    repo.create_batch("bm", "lhs", 1, 5)
    repo.insert_result("bm", [1, 2], [[1.0, 5.0]] * 5)
    model = RepositoryPagedModel(repo)
    rows = model.page_rows
    assert len(rows) == 5
    assert rows[0]["external_id"] >= 1 and 1 in rows[0]["values"]


def test_experiments_panel_cards_format(qapp, tmp_path):
    from app.infrastructure.experiment_repository import ExperimentRepository
    from app.ui.models.repository_paged_model import RepositoryPagedModel
    from app.ui.widgets.experiments_panel import ExperimentsPanel

    repo = ExperimentRepository(str(tmp_path / "m13c.db"))
    repo.create_batch("bc13", "lhs", 1, 9)
    repo.insert_result("bc13", [1, 2], [[1.0, 5.0]] * 9)
    model = RepositoryPagedModel(repo, page_size=4)
    panel = ExperimentsPanel(model)
    assert panel.view_stack.count() == 4  # r13 tabela/cartões → r17 + lista + matriz
    assert isinstance(panel.view_stack, QStackedWidget)
    # formato tabela por padrão
    assert panel.combo_format.currentIndex() == 0
    assert panel.view_stack.currentIndex() == 0
    # troca para cartões
    panel.combo_format.setCurrentIndex(1)
    assert panel.view_stack.currentIndex() == 1
    shown = panel.cards_view.grid.count()
    assert shown == 4  # página de 4 experimentos → 4 cartões
    # paginação recarrega cartões
    panel._next()
    assert panel.cards_view.grid.count() == 4
    panel.combo_format.setCurrentIndex(0)
    assert panel.view_stack.currentIndex() == 0


def test_experiments_cards_view_sets_and_palette(qapp):
    from app.ui.widgets.experiment_cards_view import ExperimentCardsView, ExperimentCard

    view = ExperimentCardsView(cols=3)
    rows = [{"external_id": i, "values": {1: float(i)}} for i in range(1, 8)]
    shown = view.set_data(rows, [1])
    assert shown == 7
    assert view.grid.count() == 9  # 7 cartões + 2 placeholders (grade 3×3, r14)
    first = view.grid.itemAt(0).widget()
    assert isinstance(first, ExperimentCard)
    assert first.exp_id == 1
    view.set_palette("roxo→verde")
    void = view.set_data([], [1])
    assert void == 0


# ---------- MainWindow: dock do fluxo + estado ----------

def test_flow_dock_in_main_window(tmp_path, qapp):
    from PySide6.QtCore import Qt

    from app.container import Container
    from app.ui.main_window import MainWindow

    container = Container(base_dir=str(tmp_path / "c13"), load_plugins=False)
    try:
        window = MainWindow(container)
        assert window._dock_flow.widget() is window.flow_panel
        assert window.flow_panel.list.count() == 6
        # estado inicial do container novo: só "study" possível → tpl pendente
        state = window._flow_state()
        assert state["has_studies"] is False
        # ação sample → dispara amostragem (só valida rota, sem exceção)
        window.variables_panel.specs = {}
        box = __import__("PySide6.QtWidgets", fromlist=["QMessageBox"]).QMessageBox
        box.warning = staticmethod(lambda *a, **k: box.StandardButton.Ok)
        box.information = staticmethod(lambda *a, **k: box.StandardButton.Ok)
        window._on_flow_action("sample")  # sem specs → aviso modificado, sem travar
        window.close()
    finally:
        container.shutdown()


# ---------- gráficos ----------

def test_plot_x_ticks_and_bar_labels_render(qapp):
    import numpy as np
    from PySide6.QtCore import QRectF

    from app.ui.widgets.distribution_plot_dialog import PlotCanvas, format_tick

    assert format_tick(15_000.0) == "15k"
    canvas = PlotCanvas()
    canvas.mode = "bar"
    xs = np.arange(6, dtype=float)
    ys = np.full(6, 2.0)
    canvas.add_series("PMF", xs, ys, True)
    canvas.grab()  # paintEvent roda: ticks X formatados + labels de valor


def test_plot_renders_long_series_no_labels(qapp):
    import numpy as np

    from app.ui.widgets.distribution_plot_dialog import PlotCanvas

    canvas = PlotCanvas()
    canvas.mode = "bar"
    xs = np.arange(50, dtype=float)
    ys = np.ones(50)
    canvas.add_series("Longas", xs, ys, True)
    canvas.grab()
