"""Testes de zoom de fonte do editor e escala da fonte do sistema."""

import os

import pytest
from PySide6.QtCore import QEvent, QPoint, Qt
from PySide6.QtGui import QKeyEvent, QWheelEvent

from app.ui.editor.themes import persist_font_scale, persist_system_scale


@pytest.fixture(autouse=True)
def _reset_scale():
    persist_font_scale(1.0)
    persist_system_scale(1.0)
    yield
    persist_font_scale(1.0)
    persist_system_scale(1.0)


def _wheel(editor):
    return QWheelEvent(
        QPoint(10, 10), QPoint(10, 10), QPoint(0, 0), QPoint(0, 120),
        Qt.MouseButton.NoButton, Qt.KeyboardModifier.ControlModifier,
        Qt.ScrollPhase.NoScrollPhase, False,
    )


def _key(editor, key):
    event = QKeyEvent(QEvent.Type.KeyPress, key, Qt.KeyboardModifier.ControlModifier)
    editor.keyPressEvent(event)


def test_dialog_no_pending_attribute_error(container, qtbot):
    from app.ui.widgets.distribution_dialog import DistributionDialog

    dlg = DistributionDialog(container.registry, var_id=1, current=None)
    qtbot.addWidget(dlg)
    assert dlg.combo_dist.count() > 0
    dlg.combo_provider.setCurrentText("scipy")
    assert dlg.combo_dist.currentText() != ""
    spec = dlg.collect()
    assert spec.provider == "scipy" and spec.params


def test_dialog_restores_existing_spec(container, qtbot):
    from app.domain.entities import DistributionSpec
    from app.ui.widgets.distribution_dialog import DistributionDialog

    current = DistributionSpec(
        provider="scipy", name="alpha", params={"a": 2.0, "loc": 3.0, "scale": 4.0}
    )
    dlg = DistributionDialog(container.registry, var_id=10001, current=current)
    qtbot.addWidget(dlg)
    assert dlg.combo_provider.currentText() == "scipy"
    assert dlg.combo_dist.currentText() == "alpha"
    # r26-27: _widgets guarda metadados no próprio widget (_param_name/_param_type)
    params = {w._param_name: w.value() for w in dlg._widgets}
    assert params == {"a": 2.0, "loc": 3.0, "scale": 4.0}


def test_editor_zoom_methods(main_window_offscreen):
    editor = main_window_offscreen.editor_tabs.current_editor().editor
    base = editor.font().pointSize()

    editor.zoom(1)
    assert editor.font().pointSize() == base + 1
    editor.zoom(-1)
    assert editor.font().pointSize() == base
    editor.zoom(-100)
    assert editor.font().pointSize() >= 4  # piso da escala
    editor.zoom_reset()
    assert editor.font().pointSize() == base


def test_editor_zoom_shortcuts(main_window_offscreen):
    editor = main_window_offscreen.editor_tabs.current_editor().editor
    base = editor.font().pointSize()

    _key(editor, Qt.Key.Key_Plus)
    assert editor.font().pointSize() == base + 1
    _key(editor, Qt.Key.Key_Equal)
    _key(editor, Qt.Key.Key_Minus)
    _key(editor, Qt.Key.Key_Minus)
    assert editor.font().pointSize() == base
    _key(editor, Qt.Key.Key_0)
    assert editor.font().pointSize() == base


def test_editor_zoom_ctrl_wheel(main_window_offscreen):
    editor = main_window_offscreen.editor_tabs.current_editor().editor
    base = editor.font().pointSize()

    editor.wheelEvent(_wheel(editor))
    assert editor.font().pointSize() == base + 1


def test_menu_zoom_applies_to_all_tabs(main_window_offscreen):
    window = main_window_offscreen
    window.editor_tabs.new_tab()
    base = window.editor_tabs.widget(0).editor.font().pointSize()

    window._zoom_editors(1)
    sizes = [
        window.editor_tabs.widget(i).editor.font().pointSize()
        for i in range(window.editor_tabs.count())
    ]
    assert sizes[0] == sizes[1] == base + 1

    window._reset_zoom_editors()
    for i in range(window.editor_tabs.count()):
        tab = window.editor_tabs.widget(i)
        if tab is not None and hasattr(tab, "editor"):
            assert tab.editor.font().pointSize() == base


def test_system_font_scale(main_window_offscreen):
    from PySide6.QtWidgets import QApplication

    window = main_window_offscreen
    assert window._base_app_font.family()

    window._apply_system_font()
    ref = QApplication.instance().font().pointSize()

    window._change_system_font(1)
    assert QApplication.instance().font().pointSize() >= ref
    window._reset_system_font()
    assert QApplication.instance().font().pointSize() == ref
