"""Barra de busca/substituição (ancorada em QPlainTextEdit) com suporte a regex."""

from __future__ import annotations

import re

from PySide6.QtCore import Signal
from PySide6.QtGui import QBrush, QColor, QTextCharFormat, QTextCursor, QTextDocument
from PySide6.QtWidgets import (
    QCheckBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QPlainTextEdit,
    QWidget,
)

HIGHLIGHT_HEX = "#8fd18f"  # destaque de todas as ocorrências (verde suave)
MAX_HIGHLIGHTS = 4000


def iter_matches(
    text: str, needle: str, case_sensitive: bool = False, regex: bool = False
):
    """Ocorrências como (start, end); [] se vazio; None se regex inválido."""
    if not needle:
        return []
    if regex:
        try:
            flags = 0 if case_sensitive else re.IGNORECASE
            pat = re.compile(needle, flags)
        except re.error:
            return None
        return [m.span() for m in pat.finditer(text)]
    spans: list[tuple[int, int]] = []
    haystack = text if case_sensitive else text.lower()
    target = needle if case_sensitive else needle.lower()
    step = max(1, len(target))
    pos = haystack.find(target)
    while pos != -1:
        spans.append((pos, pos + len(needle)))
        pos = haystack.find(target, pos + step)
    return spans


def replace_matches(
    text: str, needle: str, new: str, case_sensitive: bool = False, regex: bool = False
):
    """Todas as substituições; retorna (texto, contagem) ou None (regex inválida)."""
    spans = iter_matches(text, needle, case_sensitive, regex)
    if spans is None:
        return None
    if regex:
        flags = 0 if case_sensitive else re.IGNORECASE
        return re.sub(needle, new, text, flags=flags), len(spans)
    parts: list[str] = []
    last = 0
    for start, end in spans:
        parts.append(text[last:start])
        parts.append(new)
        last = end
    parts.append(text[last:])
    return "".join(parts), len(spans)


class FindReplaceBar(QWidget):
    """Sinais: find_next(text, case, regex), replace_one(old, new, case, regex),
    replace_all(old, new, case, regex)."""

    find_next = Signal(str, bool, bool)
    replace_one = Signal(str, str, bool, bool)
    replace_all = Signal(str, str, bool, bool)
    closed = Signal()

    def __init__(self, parent=None):
        """Método `FindReplaceBar.__init__`.
            Parâmetros: `self`, `parent`."""
        super().__init__(parent)
        self.setVisible(False)

        self.input = QLineEdit()
        self.input.setPlaceholderText("Buscar…")
        self.input.setFixedWidth(200)
        self.replace_input = QLineEdit()
        self.replace_input.setPlaceholderText("Substituir por…")
        self.replace_input.setFixedWidth(200)
        self.case_check = QCheckBox("Maiúsc./minúsc.")
        self.regex_check = QCheckBox("Regex")
        self.regex_check.setToolTip(
            "Expressão regular: $var\\d+, \\d{2}… Backreferences \\1 na substituição."
        )
        self.label = QLabel("")

        btn_find = QPushButton("Próximo")
        btn_replace = QPushButton("Substituir")
        btn_all = QPushButton("Todos")
        btn_close = QPushButton("✕")

        row = QHBoxLayout(self)
        row.setContentsMargins(4, 2, 4, 2)
        for w in (
            self.input, btn_find, self.replace_input, btn_replace,
            btn_all, self.regex_check, self.case_check, self.label, btn_close,
        ):
            row.addWidget(w)
        row.addStretch()
        self.setStyleSheet("background: #f0f4f8; border: 1px solid #c8d4e0;")

        btn_find.clicked.connect(self._emit_find)
        btn_replace.clicked.connect(self._emit_replace_one)
        btn_all.clicked.connect(self._emit_replace_all)
        btn_close.clicked.connect(self._close)
        self.input.returnPressed.connect(self._emit_find)

    def _emit_find(self):
        """Método `FindReplaceBar._emit_find`.
            Parâmetros: `self`."""
        text = self.input.text()
        if text:
            self.find_next.emit(text, self.case_check.isChecked(), self.regex_check.isChecked())

    def _emit_replace_one(self):
        """Método `FindReplaceBar._emit_replace_one`.
            Parâmetros: `self`."""
        self.replace_one.emit(
            self.input.text(), self.replace_input.text(),
            self.case_check.isChecked(), self.regex_check.isChecked(),
        )

    def _emit_replace_all(self):
        """Método `FindReplaceBar._emit_replace_all`.
            Parâmetros: `self`."""
        self.replace_all.emit(
            self.input.text(), self.replace_input.text(),
            self.case_check.isChecked(), self.regex_check.isChecked(),
        )

    def _close(self):
        """Método `FindReplaceBar._close`.
            Parâmetros: `self`."""
        self.setVisible(False)
        self.closed.emit()

    def show_bar(self):
        """Método `FindReplaceBar.show_bar`.
            Parâmetros: `self`."""
        self.setVisible(True)
        self.input.setFocus()
        self.input.selectAll()


class FindReplaceController:
    """Busca (com regex), destaque de todas as ocorrências e substituições."""

    def __init__(self, bar: FindReplaceBar, editor):
        """Método `FindReplaceController.__init__`.
            Parâmetros: `self`, `bar`, `editor`."""
        self.bar = bar
        self.editor = editor
        self._last = ""
        self._last_case = False
        self._last_regex = False

        bar.find_next.connect(self.find)
        bar.replace_one.connect(self.replace_current)
        bar.replace_all.connect(self.replace_everywhere)
        bar.closed.connect(self._clear_highlight)

    def highlight_all(self, needle, case_sensitive=False, regex=False):
        """Pinta HIGHLIGHT_HEX em todas as ocorrências (ExtraSelections)."""
        if not needle:
            self._clear_highlight()
            return
        spans = iter_matches(self.editor.toPlainText(), needle, case_sensitive, regex)
        if spans is None:
            self._clear_highlight()
            return
        fmt = QTextCharFormat()
        fmt.setBackground(QBrush(QColor(HIGHLIGHT_HEX)))
        selections = []
        doc = self.editor.document()
        for start, end in spans[:MAX_HIGHLIGHTS]:
            sel = QTextEdit.ExtraSelection()
            cur = QTextCursor(doc)
            cur.setPosition(start)
            cur.setPosition(end, QTextCursor.MoveMode.KeepAnchor)
            sel.cursor = cur
            sel.format = fmt
            selections.append(sel)
        if hasattr(self.editor, "set_search_selections"):
            self.editor.set_search_selections(selections)
        else:
            self.editor.setExtraSelections(selections)

    def _clear_highlight(self):
        """Método `FindReplaceController._clear_highlight`.
            Parâmetros: `self`."""
        if hasattr(self.editor, "set_search_selections"):
            self.editor.set_search_selections([])
        else:
            self.editor.setExtraSelections([])

    def _regex_flags(self, case_sensitive: bool):
        """Método `FindReplaceController._regex_flags`.
            Parâmetros: `self`, `case_sensitive`.
            Retorna o resultado calculado a partir do estado local."""
        return 0 if case_sensitive else re.IGNORECASE

    def find(self, needle: str, case_sensitive: bool = False, regex: bool = False) -> None:
        """Método `FindReplaceController.find`.
            Parâmetros: `self`, `needle`, `case_sensitive`, `regex`."""
        self._last = needle
        self._last_case = case_sensitive
        self._last_regex = regex
        flags = QTextDocument.FindFlag(0)
        if case_sensitive:
            flags |= QTextDocument.FindFlag.FindCaseSensitively

        if regex:
            try:
                re.compile(needle, self._regex_flags(case_sensitive))
            except re.error:
                self.bar.label.setText("Regex inválida")
                self._clear_highlight()
                return

        text = self.editor.toPlainText()
        spans = iter_matches(text, needle, case_sensitive, regex)
        count = len(spans) if spans is not None else 0
        self.highlight_all(needle, case_sensitive, regex)
        self.bar.label.setText(f"{count} ocorrência(s)" if count else "Não encontrado")

        if regex:
            from PySide6.QtCore import QRegularExpression

            pattern_opts = QRegularExpression.PatternOption(0)
            if not case_sensitive:
                pattern_opts |= QRegularExpression.PatternOption.CaseInsensitiveOption
            qre = QRegularExpression(needle, pattern_opts)
            if not self.editor.find(qre, flags):
                cursor = self.editor.textCursor()
                cursor.movePosition(QTextCursor.MoveOperation.Start)
                self.editor.setTextCursor(cursor)
        else:
            if not self.editor.find(needle, flags):
                cursor = self.editor.textCursor()
                cursor.movePosition(QTextCursor.MoveOperation.Start)
                self.editor.setTextCursor(cursor)

    def replace_current(self, old: str, new: str, case_sensitive: bool = False, regex: bool = False) -> None:  # noqa: E501
        """Método `FindReplaceController.replace_current`.
            Parâmetros: `self`, `old`, `new`, `case_sensitive`, `regex`."""
        cursor = self.editor.textCursor()
        selected = cursor.selectedText()
        reflags = self._regex_flags(case_sensitive)
        if selected:
            try:
                if regex:
                    m = re.fullmatch(old, selected, reflags)
                    if m:
                        cursor.insertText(m.expand(new))
                elif selected == old or (not case_sensitive and selected.lower() == old.lower()):
                    cursor.insertText(new)
            except re.error:
                pass
        self.find(old, case_sensitive, regex)

    def replace_everywhere(self, old: str, new: str, case_sensitive: bool = False, regex: bool = False) -> None:  # noqa: E501
        """Método `FindReplaceController.replace_everywhere`.
            Parâmetros: `self`, `old`, `new`, `case_sensitive`, `regex`."""
        if not old:
            return
        pair = replace_matches(
            self.editor.toPlainText(), old, new, case_sensitive, regex
        )
        if pair is None:
            self.bar.label.setText("Regex inválida")
            return
        text, count = pair
        self.editor.setPlainText(text)
        self.bar.label.setText(f"{count} substituições")
        self.highlight_all(old, case_sensitive, regex)
