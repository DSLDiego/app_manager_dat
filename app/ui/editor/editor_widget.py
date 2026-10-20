"""Widget composto: CodeEditor + Highlighter + FindReplace (MVO)."""

from __future__ import annotations

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QVBoxLayout, QWidget

from app.ui.editor.code_editor import CodeEditor
from app.ui.editor.find_replace_bar import FindReplaceBar, FindReplaceController
from app.ui.editor.highlighter import DatHighlighter


class EditorWidget(QWidget):
    """Classe `EditorWidget` do módulo."""
    modified_changed = Signal(bool)
    saved = Signal(str)
    theme_changed = Signal(str)

    def __init__(self, file_path: str | None = None, parent=None):
        """Método `EditorWidget.__init__`.
            Parâmetros: `self`, `file_path`, `parent`."""
        super().__init__(parent)
        self.file_path = file_path
        self.readonly = False

        from app.ui.editor.themes import saved_theme

        self.theme_name = saved_theme()
        self.editor = CodeEditor(self)
        self.highlighter = DatHighlighter(self.editor.document(), self.theme_name)
        self.editor.apply_theme(self.theme_name)
        self.find_bar = FindReplaceBar(self)
        self.find_controller = FindReplaceController(self.find_bar, self.editor)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.find_bar)

        # r18: editor + minimapa lado a lado (minimapa pode ser desligado)
        from PySide6.QtWidgets import QHBoxLayout, QWidget as _QWidget

        from app.ui.editor.editor_minimap import EditorMinimap

        self.minimap = EditorMinimap()
        center = _QWidget()
        center_l = QHBoxLayout(center)
        center_l.setContentsMargins(0, 0, 0, 0)
        center_l.setSpacing(2)
        center_l.addWidget(self.editor, 1)
        center_l.addWidget(self.minimap)
        layout.addWidget(center, 1)

        self.minimap.set_document("")
        self.editor.textChanged.connect(
            lambda: self.minimap.set_document(self.editor.toPlainText())
        )
        sb = self.editor.verticalScrollBar()
        sb.valueChanged.connect(
            lambda v: self.minimap.set_scroll(
                self.editor.document().blockCount(),
                max(1, int(self.editor.height() / self.editor.fontMetrics().lineSpacing()) - 1),
                v,
            )
        )
        self.minimap.lineClicked.connect(self._minimap_goto)

        self.editor.textChanged.connect(self._on_text_changed)
        self.editor.document().modificationChanged.connect(self._on_modification)

        # atalhos de busca: Ctrl+F abre, F3 repete, Esc fecha
        from PySide6.QtGui import QKeySequence as _QKS, QShortcut as _Shortcut

        _Shortcut(_QKS("Ctrl+F"), self.editor, activated=self.find_bar.show_bar)
        _Shortcut(_QKS("F3"), self.editor, activated=self._repeat_find)
        _Shortcut(_QKS("Esc"), self.find_bar, activated=self.find_bar._close)

    def _repeat_find(self):
        """Método `EditorWidget._repeat_find`.
            Parâmetros: `self`."""
        last = getattr(self.find_controller, "_last", "")
        if last:
            self.find_controller.find(
                last, self.find_controller._last_case, self.find_controller._last_regex
            )

    # ---------- conteúdo ----------
    def set_content(self, text: str) -> None:
        """Método `EditorWidget.set_content`.
            Parâmetros: `self`, `text`."""
        self.editor.setPlainText(text)
        self.editor.document().setModified(False)

    def text(self) -> str:
        """Método `EditorWidget.text`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        return self.editor.toPlainText()

    def is_modified(self) -> bool:
        """Método `EditorWidget.is_modified`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        return self.editor.document().isModified()

    def set_readonly(self, value: bool) -> None:
        """Método `EditorWidget.set_readonly`.
            Parâmetros: `self`, `value`."""
        self.readonly = value
        self.editor.setReadOnly(value)

    def set_variables(self, variables: dict[int, str]) -> None:
        """Método `EditorWidget.set_variables`.
            Parâmetros: `self`, `variables`."""
        self.highlighter.set_variables(variables)

    def set_theme(self, theme_name: str) -> None:
        """Método `EditorWidget.set_theme`.
            Parâmetros: `self`, `theme_name`."""
        self.theme_name = theme_name
        self.editor.apply_theme(theme_name)
        self.highlighter.apply_theme(theme_name)
        self._sync_minimap_theme(theme_name)
        self.theme_changed.emit(theme_name)

    def _sync_minimap_theme(self, theme_name: str):
        """Minimapa acompanha o tema do editor (r20)."""
        from app.ui.editor.themes import theme_colors

        colors = theme_colors(theme_name)
        bg = colors.get("line_number_area", colors.get("editor_background", "#f4f6f9"))
        bar = colors.get("line_number", "#b8c4d0")
        self.minimap.set_theme_colors(bg, bar)

    # ---------- zoom ----------
    def zoom(self, delta: int) -> None:
        """Método `EditorWidget.zoom`.
            Parâmetros: `self`, `delta`."""
        self.editor.zoom(delta)

    def zoom_reset(self) -> None:
        """Método `EditorWidget.zoom_reset`.
            Parâmetros: `self`."""
        self.editor.zoom_reset()

    # ---------- arquivo ----------
    def save(self) -> None:
        """Método `EditorWidget.save`.
            Parâmetros: `self`."""
        if not self.file_path:
            return
        with open(self.file_path, "w", encoding="utf-8") as f:
            f.write(self.text())
        self.editor.document().setModified(False)
        self.saved.emit(self.file_path)

    def load_file(self, path: str) -> None:
        """Método `EditorWidget.load_file`.
            Parâmetros: `self`, `path`."""
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            self.set_content(f.read())
        self.file_path = path

    # ---------- eventos ----------
    def _minimap_goto(self, line: int):
        """Clique no minimapa → move cursor e rola até a linha."""
        block = self.editor.document().findBlockByNumber(max(0, int(line)))
        if block.isValid():
            cursor = self.editor.textCursor()
            cursor.setPosition(block.position())
            self.editor.setTextCursor(cursor)
            self.editor.centerCursor()

    def set_minimap_visible(self, visible: bool):
        """Liga/desliga o minimapa (menu Ver)."""
        self.minimap.setVisible(bool(visible))

    def _on_text_changed(self):
        """Método `EditorWidget._on_text_changed`.
            Parâmetros: `self`."""
        self.modified_changed.emit(self.is_modified())

    def _on_modification(self, value: bool):
        """Método `EditorWidget._on_modification`.
            Parâmetros: `self`, `value`."""
        self.modified_changed.emit(value)

    def keyPressEvent(self, event: QKeyEvent):
        """Método `EditorWidget.keyPressEvent`.
            Parâmetros: `self`, `event`."""
        if event.key() == Qt.Key.Key_F and event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            self.find_bar.show_bar()
            return
        super().keyPressEvent(event)
