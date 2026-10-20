"""Regressões de teste UI quick."""

import pytest

pytest.importorskip("pytestqt")


# ---------- VariablesPanel ----------
def test_variables_panel_tokens(qtbot, qapp, registry):
    from app.ui.widgets.variables_panel import VariablesPanel

    panel = VariablesPanel(registry)
    qtbot.addWidget(panel)
    var_ids = panel.update_tokens("RUNZ $1 -- $var2 *DATES $3")
    assert var_ids == [1, 3, 10002]
    assert panel.list_widget.count() == 3
    labels = [panel.list_widget.item(i, 0).text() for i in range(3)]
    assert labels == ["$1", "$var2", "$DATES"]


def test_variables_panel_item_userrole_both_namespaces(qtbot, registry):
    from app.ui.widgets.variables_panel import VariablesPanel

    panel = VariablesPanel(registry)
    qtbot.addWidget(panel)
    result = panel.update_tokens("A $1 e $var1 e $V2 e $2")
    assert result == [1, 2, 10001, 10002]
    for i in range(panel.list_widget.count()):
        item = panel.list_widget.item(i, 0)  # coluna 0: Variável
        assert item.data(int(
            "PySide6.QtCore", fromlist=["Qt"]
        ).Qt.ItemDataRole.UserRole) == result[i]


# ---------- Highlighter ----------
def test_highlighter_token_has_theme_color(qtbot, qapp):
    from app.ui.editor.editor_widget import EditorWidget
    from app.ui.editor.themes import theme_colors

    widget = EditorWidget()
    qtbot.addWidget(widget)
    widget.editor.setPlainText("RANZ $1 -- FIM")

    spans = []
    layout = widget.editor.document().firstBlock().layout()
    text = widget.editor.toPlainText()
    for fr in layout.formats():
        spans.append((text[fr.start : fr.start + fr.length], fr.format.foreground().color().name()))

    assert any("$" in s and c == theme_colors(widget.theme_name)["token"] for s, c in spans)
    # comentário colorido como comentário, nunca como token
    assert any(
        "--" in s and c == theme_colors(widget.theme_name)["comment"] for s, c in spans
    )


# ---------- CorrelationDialog ----------
def test_correlation_dialog_resize_keeps_ids(qtbot, qapp):
    from app.ui.widgets.correlation_dialog import CorrelationDialog

    dlg = CorrelationDialog(var_ids=[7, 13], corr=[[1.0, 0.5], [0.5, 1.0]])
    qtbot.addWidget(dlg)

    # range do spin é 2..200: extensão preserva ids e apenda novos
    dlg.spin_n.setValue(3)
    dlg._resize()
    assert dlg.var_ids == [7, 13, 3]
    import numpy as np

    m = np.asarray(dlg.corr)
    assert m.shape == (3, 3)
    assert m[0, 1] == pytest.approx(0.5)
    assert np.allclose(np.diag(m), 1.0)

    # reparo via _fill/render: valores casuais ficam válidos
    Item = __import__("PySide6.QtWidgets", fromlist=["QTableWidgetItem"]).QTableWidgetItem
    dlg.table.setItem(0, 0, Item("1.0"))


def test_correlation_dialog_repair_message(qtbot, qapp):
    from app.ui.widgets.correlation_dialog import CorrelationDialog

    dlg = CorrelationDialog(var_ids=[1, 2], corr=[[1.0, 0.9], [0.9, 1.0]])
    qtbot.addWidget(dlg)
    dlg._repair()
    assert dlg.label_status.text() == "Matriz reparada."
    import numpy as np

    m = np.asarray(dlg.corr)
    assert np.allclose(np.diag(m), 1.0)
    assert m.max() <= 1.0 + 1e-9


def test_correlation_dialog_apply_signal(qtbot, qapp):
    from app.ui.widgets.correlation_dialog import CorrelationDialog

    dlg = CorrelationDialog(var_ids=[1, 2], corr=[[1.0, 0.4], [0.4, 1.0]])
    qtbot.addWidget(dlg)
    seen = []
    dlg.accepted_correlation.connect(seen.append)
    dlg._apply()
    assert len(seen) == 1 and seen[0] == [[1.0, 0.4], [0.4, 1.0]]


# ---------- BatchExportDialog ----------
def test_batch_export_dialog_signal(qtbot, qapp):
    from app.ui.widgets.batch_export_dialog import BatchExportDialog

    dlg = BatchExportDialog(["batch_1", "batch_2"], [(5, "template 1 — v1")])
    qtbot.addWidget(dlg)
    dlg.combo_batch.setCurrentText("batch_2")
    dlg.combo_version.setCurrentIndex(0)
    dlg.input_dir.setText("C:/out")
    seen = []
    dlg.exportRequested.connect(lambda *a: seen.append(a))
    dlg._emit()
    assert seen == [("batch_2", 5, "C:/out")]


# ---------- ExportDoneDialog ----------
def test_export_done_dialog_plain_label(qtbot, qapp, tmp_path):
    from PySide6.QtWidgets import QLabel

    from app.ui.widgets.export_done_dialog import ExportDoneDialog

    dlg = ExportDoneDialog(tmp_path, 12)
    qtbot.addWidget(dlg)
    texts = [l.text() for l in dlg.findChildren(QLabel)]
    assert any("12" in t for t in texts)
    assert not any("**" in t for t in texts)


# ---------- TasksPanel ----------
def test_tasks_panel_rows_and_signal(qtbot, qapp, tmp_path):
    from app.domain.tasks import TaskKind
    from app.infrastructure.task_repository import TaskRepository
    from app.ui.widgets.tasks_panel import TasksPanel

    repo = TaskRepository(str(tmp_path / "tasks.db"))
    task = repo.create(TaskKind.BATCH_EXPORT, {"batch_id": "b1"})
    panel = TasksPanel(repo)
    qtbot.addWidget(panel)
    assert panel.table.rowCount() == 1
    assert panel.table.item(0, 0).text() == str(task.id)
    assert panel.table.columnCount() == 5

    seen = []
    panel.pauseRequested.connect(seen.append)
    panel.table.selectRow(0)
    panel._emit(panel.pauseRequested)()
    assert seen == [task.id]
    repo.close()


# ---------- LogsPanel ----------
def test_logs_panel_refresh_and_filters(qtbot, qapp, log_repo):
    from app.services.log_service import LogService
    from app.ui.widgets.logs_panel import LogsPanel

    svc = LogService(repo=log_repo)
    svc.info("SAMPLING", "start", "iniciado")
    svc.error("EXPORT", "fail", "cabou")
    log_repo.wait_pending()

    panel = LogsPanel(log_repo)
    qtbot.addWidget(panel)
    panel.refresh()
    assert panel.table.rowCount() == 2

    panel.combo_level.setCurrentText("ERROR")
    panel.refresh()
    assert panel.table.rowCount() == 1
    assert panel.table.item(0, 3).text() == "EXPORT"

    panel.combo_level.setCurrentText("Todos")
    panel.combo_category.setCurrentText("SAMPLING")
    panel.refresh()
    assert panel.table.rowCount() == 1
    assert panel.table.item(0, 3).text() == "SAMPLING"


def test_logs_panel_export_csv(qtbot, qapp, log_repo, tmp_path, monkeypatch):
    import csv as _csv

    from PySide6.QtWidgets import QFileDialog

    from app.services.log_service import LogService
    from app.ui.widgets.logs_panel import LogsPanel

    svc = LogService(repo=log_repo)
    svc.warning("SYSTEM", "boot", "oi")
    log_repo.wait_pending()

    path = tmp_path / "logs_export.csv"
    monkeypatch.setattr(
        QFileDialog, "getSaveFileName", staticmethod(lambda *a, **k: (str(path), ""))
    )
    panel = LogsPanel(log_repo)
    qtbot.addWidget(panel)
    panel.export_csv()
    lines = list(_csv.reader(path.open(encoding="utf-8")))
    assert lines[0][:3] == ["id", "created_at", "level"]
    assert len(lines) == 2


# ---------- PagedExperimentsModel ----------
def test_paged_model_basic(qtbot, qapp):
    from PySide6.QtCore import QModelIndex

    from app.ui.models.experiments_table_model import PagedExperimentsModel

    model = PagedExperimentsModel(page_size=4)
    model.set_data([1, 10001], [[float(i), float(i) + 1] for i in range(6)])
    assert model.rowCount(QModelIndex()) == 4
    assert model.total_pages == 2
    model.next_page()
    assert model.rowCount(QModelIndex()) == 2
    assert model.data(model.index(0, 0)) == 5
    assert model.data(model.index(0, 2)) == "5"
    model.prev_page()
    assert model.data(model.index(0, 0)) == 1


def test_statistics_dialog_fills_rows(qtbot, qapp, container, populated_batch):
    from app.services.statistics_service import StatisticsService
    from app.ui.widgets.statistics_dialog import StatisticsDialog

    dlg = StatisticsDialog(
        StatisticsService(),
        lambda var_id: container.exp_repo.get_variable_values(10002),
    )
    qtbot.addWidget(dlg)
    dlg.spin_var.setValue(10002)
    dlg.refresh()

    names = [dlg.table.item(r, 0).text() for r in range(dlg.table.rowCount())]
    assert names[:3] == ["Amostras", "Média", "Desvio-Padrão"]
    assert dlg.table.item(0, 1).text() == "12"
    assert dlg.table.item(1, 1).text() == "5"


def test_comparison_dialog_rows(qtbot, qapp, container, populated_batch):
    container.ensure_services()
    from app.ui.widgets.comparison_dialog import ComparisonDialog

    result = container.comparison_service.compare(1, 2)
    dlg = ComparisonDialog(result)
    qtbot.addWidget(dlg)
    assert dlg.table.rowCount() == 2
    assert dlg.table.item(0, 0).text() == "$1"
    assert dlg.table.item(1, 0).text() == "$var2"


def test_batch_comparison_dialog_columns(qtbot, qapp, container, populated_batch):
    container.ensure_services()
    from app.ui.widgets.batch_comparison_dialog import BatchComparisonDialog

    cmp_result = container.batch_comparison_service.compare("batch_x", "batch_x")
    dlg = BatchComparisonDialog(cmp_result)
    qtbot.addWidget(dlg)
    assert dlg.table.columnCount() == 11
    assert dlg.table.rowCount() == len(cmp_result.variables)
    assert dlg.table.item(1, 0).text() == "$var2"