"""Regressão da rodada 20: estatísticas descritivas, minimapa por tema, PNG da página."""

import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import pytest
from PySide6.QtWidgets import QApplication


@pytest.fixture(scope="module")
def qapp():
    app = QApplication.instance() or QApplication([])
    yield app


# ---------- puro: estatísticas ----------

def test_stats_summary_pure():
    from app.ui.widgets.stats_dialog import stats_summary

    rows = [
        {"external_id": 1, "values": {1: 0.0, 2: 10.0}},
        {"external_id": 2, "values": {1: 2.0}},
        {"external_id": 3, "values": {1: 4.0, 2: 20.0}},
    ]
    s = stats_summary(rows, [1, 2])
    assert s[1]["n"] == 3
    assert s[1]["min"] == 0.0 and s[1]["max"] == 4.0
    assert s[1]["mean"] == pytest.approx(2.0)
    assert s[1]["std"] == pytest.approx((8.0 / 3.0) ** 0.5, rel=1e-6)  # populacional
    # var 2 tem 2 valores
    assert s[2]["n"] == 2 and s[2]["mean"] == pytest.approx(15.0)
    # sem dados
    empty = stats_summary(rows, [9])
    assert empty[9] == {"n": 0, "min": None, "mean": None, "std": None, "max": None}


def test_stats_row_text_pure():
    from app.ui.widgets.stats_dialog import stats_row_text

    full = {"n": 3, "min": 0.0, "mean": 2.0, "std": 1.3333, "max": 4.0}
    text = stats_row_text(full)
    assert "n=3" in text and "média=2" in text and "máx=4" in text
    empty = {"n": 0, "min": None, "mean": None, "std": None, "max": None}
    assert stats_row_text(empty).count("\u2014") == 4


def test_stats_dialog_table(qapp):
    from app.ui.widgets.stats_dialog import StatsDialog

    rows = [
        {"external_id": i, "values": {1: float(i), 2: None}} for i in range(1, 5)
    ]
    dlg = StatsDialog(rows, [1, 2])
    assert dlg.table.rowCount() == 2
    assert dlg.table.columnCount() == 5
    assert dlg.table.verticalHeaderItem(0).text() == "$1"
    # var 1: n=4, média=2.5
    assert dlg.table.item(0, 0).text() == "4"
    assert dlg.table.item(0, 2).text().startswith("2.5")
    # var 2: sem dados → travessões
    assert dlg.table.item(1, 0).text() == "0"
    assert dlg.table.item(1, 1).text() == "\u2014"


def test_panel_stats_button(qapp, tmp_path):
    from app.infrastructure.experiment_repository import ExperimentRepository
    from app.ui.models.repository_paged_model import RepositoryPagedModel
    from app.ui.widgets.experiments_panel import ExperimentsPanel

    repo = ExperimentRepository(str(tmp_path / "m20.db"))
    repo.create_batch("b20", "lhs", 1, 3)
    repo.insert_result("b20", [1, 2], [[1.0, 5.0]] * 3)
    panel = ExperimentsPanel(RepositoryPagedModel(repo, page_size=3))
    assert panel.btn_stats.text() == "Estatísticas"
    # show() não modal — só valida rota sem travar
    panel._open_stats()
    panel.btn_stats.click()


# ---------- minimapa por tema ----------

def test_minimap_theme_colors(qapp):
    from app.ui.editor.editor_minimap import EditorMinimap

    m = EditorMinimap()
    assert m._colors["bg"] == "#f4f6f9"
    m.set_theme_colors("#21222c", "#6272a4")
    assert m._colors["bg"] == "#21222c" and m._colors["bar"] == "#6272a4"
    m.set_document("a\nbb\nccc\n")
    m.set_scroll(3, 1, 1)
    m.grab()  # pinta com cores do tema dark
    # rgb sem alfa também aceito
    m.set_theme_colors("#000000", "#ffffff", (255, 255, 255))
    m.grab()


def test_editor_theme_syncs_minimap(qapp):
    from app.ui.editor.editor_widget import EditorWidget

    tab = EditorWidget()
    tab.set_content("x = $1\n")
    for theme in ("dracula", "claro", "nord"):
        try:
            tab.apply_theme(theme)
        except Exception:  # noqa: BLE001 — tema pode não existir
            continue
        assert tab.minimap._colors["bg"] not in ("", None)


# ---------- PNG da página de histogramas ----------

def test_hist_page_png(tmp_path, qapp):
    from PySide6.QtWidgets import QFileDialog

    from app.ui.widgets.histogram_grid_panel import HistogramGridPanel

    panel = HistogramGridPanel()
    panel.set_values_map({1: [1.0, 2.0, 2.5, 3.0]})
    target = tmp_path / "hist.png"
    QFileDialog.getSaveFileName = staticmethod(
        lambda *a, **k: (str(target), "PNG (*.png)")
    )
    panel._save_page_png()
    assert target.exists() and target.stat().st_size > 0
    assert "PNG salvo" in panel.lbl_info.text()


def test_hist_page_png_cancelled(qapp):
    from PySide6.QtWidgets import QFileDialog

    from app.ui.widgets.histogram_grid_panel import HistogramGridPanel

    panel = HistogramGridPanel()
    panel.set_values_map({1: [1.0, 2.0]})
    QFileDialog.getSaveFileName = staticmethod(lambda *a, **k: ("", ""))
    before = panel.lbl_info.text()
    panel._save_page_png()
    assert panel.lbl_info.text() == before
