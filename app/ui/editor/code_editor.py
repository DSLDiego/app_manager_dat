"""QPlainTextEdit com números de linha, linha atual e auto-indent."""

from __future__ import annotations

from PySide6.QtCore import QRect, QSize, Qt
from PySide6.QtGui import (
    QColor,
    QFont,
    QPainter,
    QPen,
    QTextCharFormat,
    QTextCursor,
)
from PySide6.QtWidgets import QPlainTextEdit, QTextEdit, QWidget


class _LineNumberArea(QWidget):
    """Classe `_LineNumberArea` do módulo."""
    def __init__(self, editor: "CodeEditor"):
        """Método `_LineNumberArea.__init__`.
            Parâmetros: `self`, `editor`."""
        super().__init__(editor)
        self._editor = editor

    def sizeHint(self) -> QSize:
        """Método `_LineNumberArea.sizeHint`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        return QSize(self._editor.line_number_width(), 0)

    def paintEvent(self, event):
        """Método `_LineNumberArea.paintEvent`.
            Parâmetros: `self`, `event`."""
        self._editor.paint_line_numbers(event)


class CodeEditor(QPlainTextEdit):
    """Classe `CodeEditor` do módulo."""
    BASE_FONT_SIZE = 10

    def __init__(self, parent=None):
        """Método `CodeEditor.__init__`.
            Parâmetros: `self`, `parent`."""
        super().__init__(parent)
        from app.ui.editor.themes import DEFAULT_THEME, saved_font_scale, theme_colors

        self.theme_name = DEFAULT_THEME
        self._colors = theme_colors(self.theme_name)
        self._font_scale = saved_font_scale()

        font = QFont("Consolas")
        font.setStyleHint(QFont.StyleHint.Monospace)
        font.setPointSize(self.BASE_FONT_SIZE)
        self.setFont(font)
        self.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)
        self.setTabStopDistance(4 * self.fontMetrics().horizontalAdvance(" "))
        # r15: setDocumentMargin(<4) aqui QUEBRA modificationChanged no PySide6
        # 6.11.1 (quirk bisectado) — não re-adicionar; compacto via viewport only.
        self.setViewportMargins(0, 1, 0, 0)

        self._area = _LineNumberArea(self)
        self.blockCountChanged.connect(self._update_area_width)
        self.updateRequest.connect(self._update_area)
        self.cursorPositionChanged.connect(self._highlight_current)
        self._update_area_width(0)
        self._highlight_current()
        self.apply_theme(self.theme_name)

    # ---------- temas ----------
    def apply_theme(self, theme_name: str) -> None:
        """Método `CodeEditor.apply_theme`.
            Parâmetros: `self`, `theme_name`."""
        from app.ui.editor.themes import theme_colors

        self.theme_name = theme_name
        self._colors = theme_colors(theme_name)
        colors = self._colors

        palette = self.palette()
        from PySide6.QtGui import QPalette

        palette.setColor(QPalette.ColorRole.Window, QColor(colors["editor_background"]))
        palette.setColor(QPalette.ColorRole.Base, QColor(colors["editor_background"]))
        palette.setColor(QPalette.ColorRole.Text, QColor(colors["editor_foreground"]))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(colors["editor_foreground"]))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(colors["selection_background"]))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor(colors["selection_foreground"]))
        self.setPalette(palette)
        self.viewport().setPalette(palette)

        self._area.update()
        self._highlight_current()

    # ---------- zoom de fonte ----------
    def _apply_editor_font(self) -> None:
        """Método `CodeEditor._apply_editor_font`.
            Parâmetros: `self`."""
        from app.ui.editor.themes import persist_font_scale

        size = max(4, round(self.BASE_FONT_SIZE * self._font_scale))
        if self.font().pointSize() == size:
            return
        font = QFont("Consolas")
        font.setStyleHint(QFont.StyleHint.Monospace)
        font.setPointSize(size)
        self.setFont(font)
        self.setTabStopDistance(4 * self.fontMetrics().horizontalAdvance(" "))

    def zoom(self, delta: int) -> None:
        """Método `CodeEditor.zoom`.
            Parâmetros: `self`, `delta`."""
        from app.ui.editor.themes import ZOOM_STEP, persist_font_scale

        if delta > 0:
            self._font_scale = min(4.0, self._font_scale + ZOOM_STEP)
        else:
            self._font_scale = max(0.5, self._font_scale - ZOOM_STEP)
        self._apply_editor_font()
        persist_font_scale(self._font_scale)

    def zoom_reset(self) -> None:
        """Método `CodeEditor.zoom_reset`.
            Parâmetros: `self`."""
        from app.ui.editor.themes import DEFAULT_FONT_SCALE, persist_font_scale

        self._font_scale = DEFAULT_FONT_SCALE
        self._apply_editor_font()
        persist_font_scale(self._font_scale)

    # ---------- números de linha ----------
    def line_number_width(self) -> int:
        """Método `CodeEditor.line_number_width`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        digits = max(2, len(str(self.blockCount())))
        return 12 + self.fontMetrics().horizontalAdvance("9") * digits

    def _update_area_width(self, _):
        """Método `CodeEditor._update_area_width`.
            Parâmetros: `self`, `_`."""
        self.setViewportMargins(self.line_number_width(), 1, 0, 0)

    def _update_area(self, rect, dy):
        """Método `CodeEditor._update_area`.
            Parâmetros: `self`, `rect`, `dy`."""
        if dy:
            self._area.scroll(0, dy)
        else:
            self._area.update(0, rect.y(), self._area.width(), rect.height())
        if rect.contains(self.viewport().rect()):
            self._update_area_width(0)

    def resizeEvent(self, event):
        """Método `CodeEditor.resizeEvent`.
            Parâmetros: `self`, `event`."""
        super().resizeEvent(event)
        cr = self.contentsRect()
        self._area.setGeometry(QRect(cr.left(), cr.top(), self.line_number_width(), cr.height()))

    def paint_line_numbers(self, event):
        """Método `CodeEditor.paint_line_numbers`.
            Parâmetros: `self`, `event`."""
        colors = self._colors
        painter = QPainter(self._area)
        painter.fillRect(event.rect(), QColor(colors["line_number_area"]))

        block = self.firstVisibleBlock()
        block_number = block.blockNumber()
        top = round(self.blockBoundingGeometry(block).translated(self.contentOffset()).top())
        bottom = top + round(self.blockBoundingRect(block).height())
        current = self.textCursor().blockNumber()

        painter.setPen(QColor(colors["line_number"]))
        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                if block_number == current:
                    painter.setPen(QColor(colors["line_number_active"]))
                painter.drawText(
                    0, top, self._area.width() - 6,
                    self.fontMetrics().height(),
                    Qt.AlignmentFlag.AlignRight, str(block_number + 1),
                )
                if block_number == current:
                    painter.setPen(QColor(colors["line_number"]))
            block = block.next()
            top = bottom
            bottom = top + round(self.blockBoundingRect(block).height())
            block_number += 1

    def _highlight_current(self):
        """Linha atual + destaques de busca (duas camadas compostas)."""
        sels = list(getattr(self, "_search_sels", []) or [])
        sel = QTextEdit.ExtraSelection()
        sel.format.setBackground(QColor(self._colors["current_line"]))
        sel.format.setProperty(QTextCharFormat.Property.FullWidthSelection, True)
        sel.cursor = self.textCursor()
        sel.cursor.clearSelection()
        sels.append(sel)
        self.setExtraSelections(sels)

    def set_search_selections(self, selections):
        """Destaques de todas as ocorrências (FindReplaceController)."""
        self._search_sels = list(selections or [])
        self._highlight_current()

    # ---------- atalhos ----------
    def keyPressEvent(self, event):
        """Método `CodeEditor.keyPressEvent`.
            Parâmetros: `self`, `event`."""
        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            self._auto_indent(event)
            return
        if event.key() == Qt.Key.Key_Tab and self.textCursor().hasSelection():
            self._indent_selection(1)
            return
        if event.key() == Qt.Key.Key_Backtab and self.textCursor().hasSelection():
            self._indent_selection(-1)
            return
        ctrl = event.modifiers() & Qt.KeyboardModifier.ControlModifier
        if ctrl and event.key() in (Qt.Key.Key_Plus, Qt.Key.Key_Equal):
            self.zoom(1)
            return
        if ctrl and event.key() == Qt.Key.Key_Minus:
            self.zoom(-1)
            return
        if ctrl and event.key() == Qt.Key.Key_0:
            self.zoom_reset()
            return
        super().keyPressEvent(event)

    def wheelEvent(self, event):
        """Método `CodeEditor.wheelEvent`.
            Parâmetros: `self`, `event`."""
        if event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            self.zoom(1 if event.angleDelta().y() > 0 else -1)
            event.accept()
            return
        super().wheelEvent(event)

    def _auto_indent(self, event):
        """Método `CodeEditor._auto_indent`.
            Parâmetros: `self`, `event`."""
        cursor = self.textCursor()
        line = cursor.block().text()
        indent = " " * (len(line) - len(line.lstrip()))
        extra = "    " if line.rstrip().endswith((":", "{")) else ""
        cursor.insertText("\n" + indent + extra)
        self.setTextCursor(cursor)
        event.accept()

    def _indent_selection(self, direction: int):
        """Método `CodeEditor._indent_selection`.
            Parâmetros: `self`, `direction`."""
        cursor = self.textCursor()
        start, end = cursor.selectionStart(), cursor.selectionEnd()
        cursor.setPosition(start)
        cursor.movePosition(QTextCursor.MoveOperation.StartOfBlock)
        first = cursor.blockNumber()
        cursor.setPosition(end)
        last = cursor.blockNumber()
        cursor.setPosition(start)
        cursor.movePosition(QTextCursor.MoveOperation.StartOfBlock)
        cursor.beginEditBlock()
        for _ in range(last - first + 1):
            if direction > 0:
                cursor.insertText("    ")
            else:
                text = cursor.block().text()
                if text.startswith(" "):
                    cursor.movePosition(QTextCursor.MoveOperation.NextCharacter, QTextCursor.MoveMode.KeepAnchor, 4)
                    cursor.removeSelectedText()
            cursor.movePosition(QTextCursor.MoveOperation.NextBlock)
        cursor.endEditBlock()
