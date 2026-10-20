import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from pathlib import Path

import pytest
from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QApplication

from app.container import Container
from app.ui.main_window import MainWindow
from app.ui.editor.themes import (
    theme_contrast_issues,
    contrast_ratio,
    relative_luminance,
    TEXT_PAIRS,
    MIN_CONTRAST,
)
from app.ui.widgets.scale_preview_dialog import SystemScaleDialog

APP = Path(__file__).resolve().parents[1]


@pytest.fixture()
def qapp():
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    return app


@pytest.fixture()
def window(tmp_path, qapp):
    container = Container(base_dir=str(tmp_path / "c28"), load_plugins=False)
    QSettings("datstudio", "dtengine").remove("recent/files")
    w = MainWindow(container)
    yield w
    w.close()
    QSettings("datstudio", "dtengine").remove("recent/files")


def test_themes_have_zero_contrast_issues():
    for name in ("dracula", "light", "nord", "solarized"):
        assert theme_contrast_issues(name) == [], (name, theme_contrast_issues(name))


def test_contrast_ratio_symmetric():
    assert contrast_ratio("#000000", "#ffffff") == contrast_ratio("#ffffff", "#000000")


def test_relative_luminance_known():
    assert relative_luminance("#000000") == 0.0
    assert relative_luminance("#ffffff") == 1.0


def test_text_pairs_nonempty():
    assert len(TEXT_PAIRS) >= 10


def test_min_contrast_at_least_four():
    assert MIN_CONTRAST >= 4.0


def test_scale_preview_dialog_clamps_and_converts(window):
    dialog = SystemScaleDialog(1.0)
    assert dialog.result_scale() == 1.0
    dialog._slider.setValue(50)
    assert dialog.result_scale() == 0.5
    dialog._slider.setValue(400)
    assert dialog.result_scale() == 4.0
    assert dialog.preview_point_size() >= 6


def test_scale_preview_dialog_preview_text(window):
    dialog = SystemScaleDialog(1.2)
    assert "preview em" in dialog.lbl_preview.text()
    assert dialog.lbl_preview.font().pointSizeF() >= 6


def test_mainwindow_menu_has_scale_preview_action(window):
    labels = []
    for action in window.menuBar().actions():
        menu = action.menu()
        if menu is None:
            continue
        for child in menu.actions():
            if child.text():
                labels.append(child.text())
            sub = child.menu()
            if sub is not None:
                for grand in sub.actions():
                    if grand.text():
                        labels.append(grand.text())
    assert any("escala da fonte do sistema" in label.lower() for label in labels)


def test_mainwindow_dock_shortcuts_created(window):
    assert hasattr(window, "_dock_shortcuts")
    assert len(window._dock_shortcuts) == 9


def test_mainwindow_focus_dock_by_number(window):
    dock = window._focus_dock_by_number(1)
    assert dock is not None
    assert dock.windowTitle() == "Variáveis"
    assert window._focus_dock_by_number(99) is None