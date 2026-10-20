"""Regressões de recursos da rodada 6."""

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


# ---------- Panel apply current to all ----------
def test_panel_apply_current_to_all(qapp):
    from PySide6.QtCore import Qt

    from app.infrastructure.distribution_registry import build_default_registry
    from app.ui.widgets.variables_panel import VariablesPanel

    panel = VariablesPanel(build_default_registry())
    panel.update_tokens("T $1 $2 $3")
    spec = DistributionSpec(provider="scipy", name="norm", params={"loc": 5.0, "scale": 1.0})
    panel.specs[2] = spec
    panel.update_tokens("")
    for row in range(panel.list_widget.count()):
        if panel.list_widget.item(row, 0).data(Qt.ItemDataRole.UserRole) == 2:
            panel.list_widget.setCurrentCell(row, 0)
            break
    assert panel.apply_current_to_all()
    assert set(panel.specs) == {1, 2, 3}
    assert all(s.name == "norm" for s in panel.specs.values())


def test_panel_apply_current_to_all_without_spec(qapp, monkeypatch):
    from app.infrastructure.distribution_registry import build_default_registry
    from app.ui import widgets
    from app.ui.widgets import variables_panel
    from app.ui.widgets.variables_panel import VariablesPanel

    calls = []
    monkeypatch.setattr(
        variables_panel.QMessageBox,
        "information",
        staticmethod(lambda *a, **k: calls.append(a[1] if len(a) > 1 else "")),
    )
    panel = VariablesPanel(build_default_registry())
    panel.update_tokens("T $1 $2")
    panel.list_widget.setCurrentCell(0, 0)
    assert panel.apply_current_to_all() is False
    assert calls and "Sem distribuição" in calls[0]


def test_panel_clear_all_specs(qapp):
    from app.infrastructure.distribution_registry import build_default_registry
    from app.ui.widgets.variables_panel import VariablesPanel

    panel = VariablesPanel(build_default_registry())
    panel.update_tokens("T $1")
    panel.specs[1] = DistributionSpec(provider="fixed", name="value", params={"value": 1.0})
    panel.clear_all_specs()
    assert panel.specs == {}
    assert panel.missing_count() == 1


# ---------- EditorTabs ----------
def test_editor_tabs_dirty_marker_after_close(qtbot, qapp):
    from app.ui.editor.editor_tabs import EditorTabs

    tabs = EditorTabs()
    qtbot.addWidget(tabs)
    a = tabs.new_tab(title="A")
    b = tabs.new_tab(title="B")

    a.editor.document().setModified(True)
    assert tabs.tabText(0) == "• A"

    tabs.removeTab(0)  # A sai; B vira índice 0
    assert tabs.widget(0) is b
    b.editor.document().setModified(True)
    # com lambda travada em índice antigo, B ficaria desmarcada
    assert tabs.tabText(0) == "• B"


def test_editor_tabs_save_title_uses_file_name(qtbot, qapp, tmp_path, monkeypatch):
    from app.ui.editor.editor_tabs import EditorTabs

    target = tmp_path / "template_teste.dat"
    tabs = EditorTabs()
    qtbot.addWidget(tabs)
    tab = tabs.new_tab(content="RUNTEST")

    monkeypatch.setattr(
        "app.ui.editor.editor_tabs.QFileDialog.getSaveFileName",
        lambda *a, **k: (str(target), ""),
    )
    tabs.save_current()
    assert tabs.tabText(tabs.indexOf(tab)) == "template_teste.dat"
    assert target.read_text(encoding="utf-8") == "RUNTEST"


# ---------- FindReplace ----------
def test_find_replace_case_insensitive_all(qtbot, qapp):
    from app.ui.editor.code_editor import CodeEditor
    from app.ui.editor.find_replace_bar import FindReplaceBar, FindReplaceController

    bar = FindReplaceBar()
    editor = CodeEditor()
    controller = FindReplaceController(bar, editor)
    qtbot.addWidget(editor)

    editor.setPlainText("DAT dat DaT")
    controller.replace_everywhere("dat", "XYZ", case_sensitive=False)
    assert editor.toPlainText() == "XYZ XYZ XYZ"
    assert "3 substituições" in bar.label.text()

    editor.setPlainText("ABC abc")
    controller.replace_everywhere("ABC", "Z", case_sensitive=True)
    assert editor.toPlainText() == "Z abc"
    assert "1 substituições" in bar.label.text()


def test_find_replace_escaping_replacement(qtbot, qapp):
    from app.ui.editor.code_editor import CodeEditor
    from app.ui.editor.find_replace_bar import FindReplaceBar, FindReplaceController

    bar = FindReplaceBar()
    editor = CodeEditor()
    controller = FindReplaceController(bar, editor)
    qtbot.addWidget(editor)

    editor.setPlainText("a b a")
    controller.replace_everywhere("a", r"\1", case_sensitive=False)
    assert editor.toPlainText() == r"\1 b \1"


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


# ---------- RepositoryPagedModel ----------
def test_paged_model_pages_and_headers(container, populated_batch, qtbot):
    from PySide6.QtCore import Qt

    from app.ui.models.repository_paged_model import RepositoryPagedModel

    model = RepositoryPagedModel(container.exp_repo, page_size=5)
    assert model.total_rows == 12
    assert model.total_pages == 3
    from PySide6.QtCore import QModelIndex

    assert model.columnCount(QModelIndex()) == 3
    assert model.headerData(0, Qt.Orientation.Horizontal) == "Experimento"
    assert model.headerData(1, Qt.Orientation.Horizontal) == "$1"
    assert model.headerData(2, Qt.Orientation.Horizontal) == "$var2"

    model.next_page()
    assert model.current_page == 1
    model.next_page()
    model.next_page()  # no-op: última página
    assert model.current_page == 2
    assert model.data(model.index(0, 0)) == 11
    model.prev_page()
    assert model.current_page == 1
    assert model.data(model.index(0, 0)) == 6


# ---------- models: PagedExperimentsModel ----------
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