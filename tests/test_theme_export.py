"""Testes: tema Dracula do editor, namespaces $1 vs $var1 e export com pasta clicável."""

import pytest

pytest.importorskip("pytestqt")


def _qapp():
    from PySide6.QtWidgets import QApplication

    return QApplication.instance() or QApplication([])


def test_default_theme_is_dracula(qtbot):
    from app.ui.editor.code_editor import CodeEditor

    editor = CodeEditor()
    qtbot.addWidget(editor)
    assert editor.theme_name == "dracula"
    assert editor._colors["editor_background"] == "#282a36"


def test_apply_theme_dracula_changes_background(qtbot):
    from PySide6.QtGui import QPalette

    from app.ui.editor.code_editor import CodeEditor

    editor = CodeEditor()
    qtbot.addWidget(editor)
    editor.apply_theme("light")
    color = editor.palette().color(QPalette.ColorRole.Base)
    assert color.name() == "#ffffff"
    editor.apply_theme("dracula")
    assert editor.palette().color(QPalette.ColorRole.Base).name() == "#282a36"


def test_highlighter_theme_formats_dracula(qtbot):
    from PySide6.QtGui import QColor

    from app.ui.editor.code_editor import CodeEditor
    from app.ui.editor.highlighter import DatHighlighter

    editor = CodeEditor()
    qtbot.addWidget(editor)
    high = DatHighlighter(editor.document(), "dracula")
    assert high.f_keyword.foreground().color().name() == QColor("#ff79c6").name()
    high.apply_theme("light")
    assert high.f_keyword.foreground().color().name() == QColor("#1e6bb8").name()


def test_editor_widget_theme_signal(qtbot):
    from app.ui.editor.editor_widget import EditorWidget

    tab = EditorWidget()
    qtbot.addWidget(tab)
    received = []
    tab.theme_changed.connect(lambda t: received.append(t))
    tab.set_theme("light")
    tab.set_theme("dracula")
    assert received == ["light", "dracula"]
    assert tab.editor.theme_name == "dracula"
    assert tab.highlighter.theme_name == "dracula"


def test_theme_persist_roundtrip(mocker_or_none=None):
    from app.ui.editor.themes import persist_theme, saved_theme

    persist_theme("light")
    assert saved_theme() == "light"
    persist_theme("dracula")
    assert saved_theme() == "dracula"


def test_dollar_and_var_same_number_distinct():
    from app.core.parsing import find_variables

    assert find_variables("A $1 (local) e $var1 (Rede Nova)") == [1, 10001]


def test_highliqhter_colors_plain_vs_prefixed(qtbot):
    from PySide6.QtGui import QColor

    from app.ui.editor.code_editor import CodeEditor
    from app.ui.editor.highlighter import DatHighlighter

    editor = CodeEditor()
    qtbot.addWidget(editor)
    high = DatHighlighter(editor.document(), "dracula")
    editor.setPlainText("X $1 Y $var1")
    assert high.f_token.foreground().color().name() == QColor("#8be9fd").name()
    assert high.f_token_prefixed.foreground().color().name() == QColor("#50fa7b").name()


# -------------------------------------------------------------------------
# Export: dialog de sucesso com "Abrir no Explorer"
# -------------------------------------------------------------------------
def test_export_done_dialog_opens_folder_in_explorer(qtbot, monkeypatch, tmp_path):
    from PySide6.QtCore import QUrl

    opened = []
    monkeypatch.setattr(
        "app.ui.widgets.export_done_dialog.QDesktopServices.openUrl",
        lambda url: opened.append(url.toString()),
    )

    from app.ui.widgets.export_done_dialog import ExportDoneDialog

    destino = tmp_path / "saída" / "meu_batch" / "v1"
    dialog = ExportDoneDialog(destino, n_files=7, manifest_path=None)
    qtbot.addWidget(dialog)

    assert "Ao exportar" not in dialog.windowTitle()
    btn_open = dialog.findChildren(
        __import__("PySide6.QtWidgets", fromlist=["QPushButton"]).QPushButton
    )[0]
    btn_open.click()
    assert opened == [QUrl.fromLocalFile(str(destino)).toString()]
    assert destino.exists()  # criada antes de abrir


def test_export_done_dialog_manifest(qtbot, monkeypatch, tmp_path):
    opened = []
    monkeypatch.setattr(
        "app.ui.widgets.export_done_dialog.QDesktopServices.openUrl",
        lambda url: opened.append(url.toString()),
    )
    from pathlib import Path as _P
    from PySide6.QtCore import QUrl

    from app.ui.widgets.export_done_dialog import ExportDoneDialog

    destino = tmp_path / "batch" / "v2"
    destino.mkdir(parents=True)
    manifest = destino / "manifest.csv"
    manifest.write_text("external_id,values\n1,{}", encoding="utf-8")

    dialog = ExportDoneDialog(destino, n_files=1, manifest_path=manifest)
    qtbot.addWidget(dialog)
    buttons = dialog.findChildren(
        __import__("PySide6.QtWidgets", fromlist=["QPushButton"]).QPushButton
    )
    labels = [b.text() for b in buttons]
    assert any("manifest.csv" in l for l in labels)

    btn_manifest = buttons[next(i for i, l in enumerate(labels) if "manifest.csv" in l)]
    monkeypatch.setattr(
        "app.ui.widgets.export_done_dialog.QDesktopServices.openUrl",
        lambda url: opened.append(url.toString()),
    )
    btn_manifest.click()
    assert opened == [QUrl.fromLocalFile(str(manifest)).toString()]
