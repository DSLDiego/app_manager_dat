"""Rodada 30: exportar heatmap em PNG e editar descrição do estudo."""

import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import pytest
from PySide6.QtWidgets import QApplication, QTableWidgetItem

from app.container import Container
from app.ui.widgets.heat_matrix_panel import HeatMatrixPanel


@pytest.fixture()
def qapp():
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    return app


@pytest.fixture()
def container(tmp_path):
    return Container(base_dir=str(tmp_path / "c30"), load_plugins=False)


# ---------- heatmap PNG ----------

def test_export_png_empty_returns_false(qapp, tmp_path):
    panel = HeatMatrixPanel()
    assert panel.export_png(tmp_path / "vazio.png") is False
    assert not (tmp_path / "vazio.png").exists()


def test_export_png_writes_real_png(qapp, tmp_path):
    panel = HeatMatrixPanel()
    panel.table.setRowCount(2)
    panel.table.setColumnCount(2)
    for r in range(2):
        for c in range(2):
            panel.table.setItem(r, c, QTableWidgetItem(f"{r}-{c}"))
    target = tmp_path / "heat.png"
    assert panel.export_png(target) is True
    assert target.exists()
    assert target.stat().st_size > 100
    with open(target, "rb") as fh:
        assert fh.read(8) == b"\x89PNG\r\n\x1a\n"
    panel.close()


def test_heat_panel_has_export_button(qapp):
    panel = HeatMatrixPanel()
    assert "PNG" in panel.btn_export_png.text()
    assert panel.btn_export_png.isEnabled()
    panel.close()


def test_export_png_summary_mode(qapp, tmp_path):
    panel = HeatMatrixPanel()
    panel.summary_table.setRowCount(1)
    panel.summary_table.setColumnCount(3)
    for c in range(3):
        panel.summary_table.setItem(0, c, QTableWidgetItem(str(c)))
    panel.btn_summary.click()
    assert panel.stack.currentIndex() == 1
    panel.summary_table.setRowCount(1)
    panel.summary_table.setColumnCount(3)
    for c in range(3):
        panel.summary_table.setItem(0, c, QTableWidgetItem(str(c)))
    target = tmp_path / "resumo.png"
    assert panel.export_png(target) is True
    assert target.exists()
    panel.close()


# ---------- descrição do estudo ----------

def test_service_set_description(container):
    sid = container.study_service.create("Estudo A", {})
    container.study_service.set_description(sid, "primeira descrição")
    assert container.study_service.get(sid)["description"] == "primeira descrição"
    container.study_service.set_description(sid, "atualizada")
    assert container.study_service.get(sid)["description"] == "atualizada"


def test_set_description_missing_raises(container):
    from app.services.study_service import StudyOperationError

    with pytest.raises(StudyOperationError):
        container.study_service.set_description(99999, "x")


def test_set_description_keeps_specs(container):
    sid = container.study_service.create("Estudo B", {1: {"dist": "normal"}})
    before = dict(container.study_service.get(sid)["specs"])
    container.study_service.set_description(sid, "nova")
    after = container.study_service.get(sid)
    assert after["specs"] == before
    assert after["description"] == "nova"


def test_studies_dialog_has_description_button(qapp, container):
    from app.ui.widgets.studies_dialog import StudiesDialog

    dialog = StudiesDialog(container.study_service)
    assert "descrição" in dialog.btn_desc.text().lower()
    dialog.close()