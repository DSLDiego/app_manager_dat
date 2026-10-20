"""Regressão da rodada 16: presets de layout, diff de arquivos, painéis estreitos."""

import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import pytest
from PySide6.QtWidgets import QApplication


@pytest.fixture(scope="module")
def qapp():
    app = QApplication.instance() or QApplication([])
    yield app


# ---------- puro: planos de layout ----------

DOCKS = ["files", "flow", "variables", "experiments", "matrix", "hists", "logs"]


def test_grid_plan_pure():
    from app.ui.layout_presets import grid_plan

    plan = grid_plan(["a", "b", "c", "d"])
    # cols=ceil(sqrt(4))=2 → h-pairs: (a,b),(c,d); v-pairs: (a,c),(b,d)
    assert ("split_h", "a", "b") in plan
    assert ("split_h", "c", "d") in plan
    assert ("split_v", "a", "c") in plan
    assert ("split_v", "b", "d") in plan
    assert len(plan) == 4
    assert grid_plan([]) == []
    plan1 = grid_plan(["só"])
    assert plan1 == []


def test_tabs_and_quadrants_plan_pure():
    from app.ui.layout_presets import tabs_plan, quadrants_plan, layout_plan

    assert tabs_plan(["a", "b", "c"]) == [
        ("tabify", "a", "b"),
        ("tabify", "a", "c"),
    ]
    q = quadrants_plan(["a", "b", "c", "d", "e"])
    assert ("split_v", "a", "b") in q
    assert ("split_h", "a", "c") in q
    assert ("split_v", "c", "d") in q
    assert ("tabify", "d", "e") in q
    # <4 docks → cai para abas
    assert quadrants_plan(["a", "b"]) == tabs_plan(["a", "b"])
    assert layout_plan("4 quadrantes", DOCKS)[0] == ("split_v", "files", "flow")
    with pytest.raises(ValueError):
        layout_plan("layout inexistente", DOCKS)


def test_layout_presets_registry():
    from app.ui.layout_presets import LAYOUT_PRESETS

    assert set(LAYOUT_PRESETS) == {"Grade", "Abas", "Editor | Painéis", "4 quadrantes"}


# ---------- MainWindow aplica presets ----------

def test_main_window_applies_all_presets(tmp_path, qapp):
    from app.container import Container
    from app.ui.layout_presets import LAYOUT_PRESETS
    from app.ui.main_window import MainWindow

    container = Container(base_dir=str(tmp_path / "c16"), load_plugins=False)
    try:
        window = MainWindow(container)
        assert window.combo_layout.count() == 4
        for preset in LAYOUT_PRESETS:
            window._apply_layout_preset(preset)  # não pode lançar
        # Abas: todos os docks visíveis tabificados no primeiro
        window._apply_layout_preset("Abas")
        window.close()
    finally:
        container.shutdown()


# ---------- diff de arquivos ----------

def test_diff_lines_and_count_pure():
    from app.ui.widgets.diff_dialog import diff_lines, count_changes, is_different

    a = "linha1\nlinha2\nlinha3\n"
    b = "linha1\nmudou\nlinha3\nnova\n"
    dl = diff_lines(a, b)
    assert any(l.startswith("-") for l in dl)
    assert any(l.startswith("+") for l in dl)
    added, removed, same = count_changes(a, b)
    assert added == 2 and removed == 1 and same == 2
    assert is_different(a, b) is True
    assert is_different(a, a) is False
    assert diff_lines(a, a) == []
    # cap de segurança
    huge_a = "\n".join(f"x{i}" for i in range(30_000))
    assert len(diff_lines(huge_a, "")) <= 20_000


def test_diff_dialog_texts_and_summary(qapp):
    from app.ui.widgets.diff_dialog import DiffDialog

    dlg = DiffDialog(open_files=[("A.dat", "x\ny\n"), ("B.dat", "x\nz\n")])
    assert dlg.combo_a.count() == 2
    assert dlg.combo_b.currentIndex() == 1  # pré-seleciona o 2º
    summary = dlg.compare()
    assert summary["different"] is True
    assert summary["added"] == 1 and summary["removed"] == 1
    assert "+" in dlg.lbl_summary.text()
    # idênticos
    dlg.combo_b.setCurrentIndex(0)
    s2 = dlg.compare()
    assert s2["different"] is False and s2["added"] == 0
    assert "IDÊNTICOS" in dlg.lbl_summary.text()
    assert "(sem diferenças)" in dlg.txt_diff.toPlainText()


def test_diff_dialog_disk_browse(monkeypatch, qapp, tmp_path):
    from app.ui.widgets.diff_dialog import DiffDialog

    f = tmp_path / "outro.dat"
    f.write_text("1\n2\n3\n", encoding="utf-8")
    dlg = DiffDialog(open_files=[("A.dat", "1\n2\n3\n")])
    monkeypatch.setattr(
        "app.ui.widgets.diff_dialog.QFileDialog.getOpenFileName",
        staticmethod(lambda *a, **k: (str(f), "")),
    )
    dlg.btn_browse_b.click()
    assert dlg.combo_b.currentText().endswith("outro.dat")
    summary = dlg.compare()
    assert summary["different"] is False  # mesmo conteúdo


def test_files_panel_diff_button(qapp):
    from app.ui.widgets.files_list_panel import FilesListPanel
    from app.ui.editor.editor_tabs import EditorTabs

    tabs = EditorTabs()
    tabs.new_tab(title="A")
    panel = FilesListPanel(tabs)
    emitted = []
    panel.diffRequested.connect(lambda: emitted.append(True))
    panel.btn_diff.click()
    assert emitted == [True]


def test_main_window_diff_opens_with_open_tabs(tmp_path, qapp, monkeypatch):
    from app.container import Container
    from app.ui.main_window import MainWindow

    container = Container(base_dir=str(tmp_path / "c16d"), load_plugins=False)
    try:
        window = MainWindow(container)
        window.editor_tabs.new_tab(title="T1")
        window.editor_tabs.new_tab(title="T2")
        opened = []
        monkeypatch.setattr(
            "app.ui.widgets.diff_dialog.DiffDialog.show",
            lambda self: opened.append(True),
        )
        window._open_files_diff()
        assert opened == [True]
        window.close()
    finally:
        container.shutdown()


# ---------- painéis mais estreitos ----------

def test_panels_narrow_minimums(qapp, tmp_path):
    from app.infrastructure.experiment_repository import ExperimentRepository
    from app.ui.models.repository_paged_model import RepositoryPagedModel
    from app.ui.widgets.experiments_panel import ExperimentsPanel
    from app.ui.widgets.histogram_grid_panel import HistogramGridPanel
    from app.ui.widgets.heat_matrix_panel import HeatMatrixPanel

    repo = ExperimentRepository(str(tmp_path / "m16.db"))
    repo.create_batch("b16", "lhs", 1, 3)
    repo.insert_result("b16", [1], [[1.0]] * 3)
    panel = ExperimentsPanel(RepositoryPagedModel(repo, page_size=3))
    assert panel.table.minimumSize().width() <= 180  # r16: cabem em docks estreitos

    hist = HistogramGridPanel()
    assert hist.table.minimumSize().width() <= 160

    heat = HeatMatrixPanel()
    assert heat.table.minimumSize().width() <= 160
