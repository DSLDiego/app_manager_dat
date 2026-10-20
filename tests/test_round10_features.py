"""Regressão da rodada 10: find/replace com regex + destaque, ranking de divergência,
renomear estudo, grade uniforme no heatmap e visual dos gráficos."""

import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from pathlib import Path

import pytest
from PySide6.QtWidgets import QApplication


@pytest.fixture(scope="module")
def qapp():
    app = QApplication.instance() or QApplication([])
    yield app


@pytest.fixture()
def tmp_container(tmp_path, qapp):
    from app.container import Container

    container = Container(base_dir=str(tmp_path / "c10"), load_plugins=False)
    yield container
    container.shutdown()


# ---------- iter_matches / replace_matches (puro) ----------

def test_iter_matches_literal_and_case():
    from app.ui.editor.find_replace_bar import iter_matches

    assert iter_matches("DAT dat DaT", "dat") == [(0, 3), (4, 7), (8, 11)]
    assert iter_matches("DAT dat DaT", "dat", case_sensitive=True) == [(4, 7)]
    assert iter_matches("abc", "") == []
    assert iter_matches("aaaa", "aa") == [(0, 2), (2, 4)]  # sem sobreposição


def test_iter_matches_regex_and_invalid():
    from app.ui.editor.find_replace_bar import iter_matches

    spans = iter_matches("T $var1 $var12 X", r"\$var\d+", regex=True)
    assert spans == [(2, 7), (8, 14)]
    assert iter_matches("x", "[", regex=True) is None  # regex inválida


def test_replace_matches_regex_backref():
    from app.ui.editor.find_replace_bar import replace_matches

    text, count = replace_matches("T $1 $var2", r"\$(var)?(\d+)", r"x\2", regex=True)
    assert text == "T x1 x2"
    assert count == 2
    assert replace_matches("a", "(", "y", True, True) is None


def test_replace_matches_case_insensitive_literal():
    from app.ui.editor.find_replace_bar import replace_matches

    text, count = replace_matches("Dat daT", "dat", "N")
    assert text == "N N"
    assert count == 2


# ---------- controller + bar widgets ----------

def test_bar_emits_regex_flag(qapp):
    from app.ui.editor.find_replace_bar import FindReplaceBar

    bar = FindReplaceBar()
    captured = []
    bar.find_next.connect(lambda t, c, r: captured.append((t, c, r)))
    bar.regex_check.setChecked(True)
    bar.input.setText("x")  # _emit_find ignora needle vazio
    bar._emit_find()
    assert captured == [("x", False, True)]


def test_controller_counts_and_highlights(qapp):
    from app.ui.editor.code_editor import CodeEditor
    from app.ui.editor.find_replace_bar import FindReplaceBar, FindReplaceController

    bar = FindReplaceBar()
    editor = CodeEditor()
    controller = FindReplaceController(bar, editor)
    editor.setPlainText("T $a $a $b")
    controller.find("$a", regex=False)
    assert "2 ocorrência(s)" in bar.label.text()
    assert len(editor._search_sels) == 2  # camada de busca separada da current-line
    bar._close()  # fecha a barra → limpa destaques
    assert editor._search_sels == []


def test_controller_regex_invalid_shows_hint(qapp):
    from app.ui.editor.code_editor import CodeEditor
    from app.ui.editor.find_replace_bar import FindReplaceBar, FindReplaceController

    bar = FindReplaceBar()
    controller = FindReplaceController(bar, CodeEditor())
    controller.find("[unclosed", regex=True)
    assert "Regex inválida" in bar.label.text()


def test_controller_regex_replace_everywhere(qapp):
    from app.ui.editor.code_editor import CodeEditor
    from app.ui.editor.find_replace_bar import FindReplaceBar, FindReplaceController

    bar = FindReplaceBar()
    editor = CodeEditor()
    controller = FindReplaceController(bar, editor)
    editor.setPlainText("T $var1 $var12 FIM\nR $var1")
    controller.replace_everywhere(r"\$var(\d+)", r"X\1", regex=True)
    assert editor.toPlainText() == "T X1 X12 FIM\nR X1"
    assert "3 substituições" in bar.label.text()
    # destaque ainda mostra as expressões restantes: nenhuma sobrou → 0
    assert editor._search_sels == []
    editor.setPlainText("T $var1 $var12")
    controller.find(r"\$var\d+", regex=True)
    assert len(editor._search_sels) == 2
    # linha atual composta + destaques (3 no total)
    assert len(editor.extraSelections()) == 3


def test_existing_behavior_literal_still_works(qapp):
    from app.ui.editor.code_editor import CodeEditor
    from app.ui.editor.find_replace_bar import FindReplaceBar, FindReplaceController

    bar = FindReplaceBar()
    editor = CodeEditor()
    controller = FindReplaceController(bar, editor)
    editor.setPlainText("DAT dat DaT")
    controller.replace_everywhere("dat", "X", case_sensitive=False)
    assert editor.toPlainText() == "X X X"


# ---------- ranking de divergência ----------

def _mk_diff(var_id, a, b):
    from app.services.comparison_service import VariableDiff

    abs_d = None if a is None or b is None else b - a
    rel_d = None
    if abs_d is not None and a:
        rel_d = 100.0 * abs_d / abs(a)
    return VariableDiff(var_id, a, b, abs_d, rel_d)


def test_divergence_ranking_order():
    from app.services.comparison_service import ComparisonService

    diffs = [
        _mk_diff(1, 1000.0, 1100.0),   # 10%
        _mk_diff(2, 2.0, 6.0),         # 150% — maior divergência
        _mk_diff(3, 10.0, 10.5),       # 5%
        _mk_diff(4, None, 1.0),        # faltante
    ]
    ranked = ComparisonService.divergence_ranking(diffs)
    assert [d.var_id for d in ranked] == [2, 1, 3, 4]
    top2 = ComparisonService.divergence_ranking(diffs, top=2)
    assert [d.var_id for d in top2] == [2, 1]


def test_comparison_dialog_sorted_and_headers(qapp):
    from app.services.comparison_service import ComparisonResult
    from app.ui.widgets.comparison_dialog import ComparisonDialog

    result = ComparisonResult(
        exp_a_id=1, exp_b_id=2,
        diffs=[_mk_diff(1, 1000.0, 1100.0), _mk_diff(2, 2.0, 6.0)],
    )
    dialog = ComparisonDialog(result)
    assert dialog.table.horizontalHeaderItem(3).text() == "Δ"
    assert dialog._diffs[0].var_id == 2  # divergente primeiro


# ---------- renomear estudo ----------

def test_repo_rename_study(tmp_path, qapp):
    from app.infrastructure.study_repository import StudyRepository

    repo = StudyRepository(str(tmp_path / "st.db"))
    s1 = repo.create_study("Original", {1: {"type": "normal", "params": {}}}, meta={"dat_path": "x"})
    assert repo.rename_study(s1, "NovoNome") is True
    assert repo.get_study(s1)["name"] == "NovoNome"
    # duplicidade em outro estudo → False
    s2 = repo.create_study("Outro", {1: {"type": "uniform", "params": {}}})
    assert repo.rename_study(s2, "NovoNome") is False
    assert repo.rename_study(999, "Qualquer") is False
    assert repo.rename_study(s2, "   ") is False
    assert repo.rename_study(s1, "  NovoNome  ") is True  # strip
    repo.close()


def test_studies_dialog_rename(tmp_path, qapp, monkeypatch):
    from PySide6.QtWidgets import QInputDialog, QMessageBox

    from app.container import Container
    from app.ui.widgets.studies_dialog import StudiesDialog

    container = Container(base_dir=str(tmp_path / "c10s"), load_plugins=False)
    try:
        container.ensure_services()
        sid = container.study_service.create("Estudo X", {1: {"type": "normal", "params": {}}}, meta={"dat_path": "x"})
        dialog = StudiesDialog(container.study_service)
        monkeypatch.setattr(
            QInputDialog, "getText",
            staticmethod(lambda *a, **k: ("Estudo X Renomeado", True)),
        )
        warns = []
        monkeypatch.setattr(QMessageBox, "warning", staticmethod(lambda *a, **k: warns.append(a)))
        dialog.list_widget.setCurrentRow(sid - 1)
        dialog.btn_rename.click()
        assert container.study_service.get(sid)["name"] == "Estudo X Renomeado"
        # a lista do dialog reflete o novo nome (refresh automático)
        texts = [dialog.list_widget.item(i).text() for i in range(dialog.list_widget.count())]
        assert any("Estudo X Renomeado" in t for t in texts)
        # nome duplicado → dialog renomeia de volta ao padrão para o teste
        container.study_service.create("Outro", {1: {"type": "uniform", "params": {}}})
        assert container.study_service.rename(sid, "Outro") is False  # duplicado no service
        assert container.study_service.get(sid)["name"] != "Outro"
    finally:
        container.shutdown()


# ---------- heatmap: grade uniforme + margens ----------

def test_heat_stretch_toggle(qapp, tmp_path):
    from app.infrastructure.experiment_repository import ExperimentRepository
    from PySide6.QtWidgets import QHeaderView

    from app.ui.widgets.heat_matrix_panel import HeatMatrixPanel

    repo = ExperimentRepository(str(tmp_path / "h10.db"))
    repo.create_batch("bh10", "lhs", 1, 4)
    repo.insert_result("bh10", [1, 2], [[1.0, 5.0]] * 4)
    panel = HeatMatrixPanel()
    panel.load_from_repo(repo)
    assert panel.table.horizontalHeader().sectionResizeMode(0) == QHeaderView.ResizeMode.ResizeToContents
    panel.chk_stretch.setChecked(True)
    assert panel.table.horizontalHeader().sectionResizeMode(0) == QHeaderView.ResizeMode.Stretch
    panel.chk_stretch.setChecked(False)
    assert panel.table.horizontalHeader().sectionResizeMode(0) == QHeaderView.ResizeMode.ResizeToContents
    repo.close()


def test_panels_compact_margins(qapp, tmp_path):
    from app.container import Container
    from app.ui.main_window import MainWindow

    container = Container(base_dir=str(tmp_path / "m10"), load_plugins=False)
    try:
        window = MainWindow(container)
        assert window.variables_panel.layout().contentsMargins().left() <= 8
        assert window.experiments_panel.layout().spacing() <= 4
        assert window.matrix_panel.layout().contentsMargins().left() <= 8
        window.close()
    finally:
        container.shutdown()


# ---------- gráficos: paleta nas séries ----------

def test_series_colors_from_palette(qapp):
    from app.ui.colors import palette_gradient
    from app.ui.widgets.distribution_plot_dialog import _SERIES_COLORS

    assert len(_SERIES_COLORS) >= 6
    assert tuple(_SERIES_COLORS) == tuple(palette_gradient("roxo→verde", steps=9))


def test_canvas_title_and_data_roundtrip(qapp):
    from app.ui.widgets.distribution_plot_dialog import PlotCanvas

    canvas = PlotCanvas()
    canvas.set_title("Normal(mu=2) (pdf)")
    import numpy as np

    canvas.add_series("Normal(mu)", np.linspace(0, 4, 12), np.ones(12), True)
    assert canvas._title.startswith("Normal")
    assert len(canvas._series) == 1
