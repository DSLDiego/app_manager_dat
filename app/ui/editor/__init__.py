"""Editor de texto profissional para .dat / .txt / .inc."""

from app.ui.editor.code_editor import CodeEditor
from app.ui.editor.editor_tabs import EditorTabs
from app.ui.editor.editor_widget import EditorWidget
from app.ui.editor.find_replace_bar import FindReplaceBar
from app.ui.editor.highlighter import DatHighlighter

__all__ = [
    "CodeEditor",
    "DatHighlighter",
    "EditorTabs",
    "EditorWidget",
    "FindReplaceBar",
]
