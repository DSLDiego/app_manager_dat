"""Highlighter especializado em arquivos CMG (.dat, .inc)."""

from __future__ import annotations

import re

from PySide6.QtGui import QColor, QFont, QSyntaxHighlighter, QTextCharFormat

CMG_KEYWORDS = {
    "*ABD", "*ALLOCATION", "*AQUIFER", "*BHP", "*BHT", "*CAUSTINCOST", "*CCCOL",
    "*CPOR", "*CPRESS", "*CROCK", "*CT", "*DATES", "*DENSITY", "*DIM", "*DIPO",
    "*DREF", "*DUALPOR", "*DUALPERM", "*ECHO", "*FINAL", "*FLUID", "*FLOWHED",
    "*FRAC", "*FRACTURE", "*GASW", "*GCREG", "*GEOMF", "*GRAVITY", "*GRID",
    "*GRIDCORNER", "*GW", "*HYS", "*INCLUDE", "*INIT", "*KRG", "*KRGCW",
    "*KRGCL", "*KRO", "*KROCW", "*KRTYPE", "*KRW", "*LIFTOPT", "*MAPS",
    "*MAX", "*MD", "*MDIMS", "*MFRAC", "*MODEL", "*MONITOR", "*MULT", "*MULTF",
    "*MULTP", "*NTG", "*NUMERIC", "*OCTREE", "*OPERATE", "*OPTIONS", "*OUT",
    "*OUTPRN", "*OUTSRF", "*PBTYPES", "*PEMB", "*PERM", "*PERMI", "*PERMJ",
    "*PERMK", "*PHASE", "*PRAT", "*PRODUCER", "*PVT", "*PWREF", "*QTAB",
    "*RADIAL", "*REFINE", "*RESULTS", "*ROCK", "*ROCKTYPE", "*RUN", "*SCHEDULE",
    "*SG", "*SOF", "*SO", "*STOP", "*SW", "*TEMP", "*TIME", "*TITLE", "*TOL",
    "*TRANS", "*TUNING", "*UNCONFORMITY", "*VISCOSITY", "*VMAT", "*VSHIFT",
    "*VSON", "*VOIL", "*WCONINJE", "*WCONPROD", "*WELLDIMS", "*WELL",
    "*WELLSTRE", "*WFRACSPEG", "*WFRACSPROD", "*WWREF",
}

TOKEN_RE = re.compile(r"\$(?P<prefix>(?:var|[vV]))?(?P<num>\d+)(?!\d)")
KEYWORD_RE = re.compile(r"^\s*(\*[A-Za-z_][A-Za-z0-9_]*)\b")
COMMENT_RE = re.compile(r"--.*$")
NUMBER_RE = re.compile(r"(?<![\w.])(-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)(?![\w.])")
STRING_RE = re.compile(r"'[^']*'|\"[^\"]*\"")


def token_var_id(match: re.Match) -> int:
    """$1 → 1  |  $var1 / $v1 → 10000+1 (namespaces distintos)."""
    prefix = match.group("prefix")
    return int(match.group("num")) + (10_000 if prefix is not None else 0)


def var_label(var_id: int) -> str:
    """Função `var_label`.
        Parâmetros: `var_id`.
        Retorna o resultado calculado a partir do estado local."""
    if var_id >= 10_000:
        return f"$var{var_id - 10_000}"
    return f"${var_id}"


class DatHighlighter(QSyntaxHighlighter):
    """Realce tematável: recebe o nome do tema (dracula/light)."""

    def __init__(self, document, theme_name: str = "dracula", parent=None):
        """Método `DatHighlighter.__init__`.
            Parâmetros: `self`, `document`, `theme_name`, `parent`."""
        super().__init__(document)
        self.theme_name = theme_name
        self._variables = {}
        self._rebuild_formats(theme_name)

    def _rebuild_formats(self, theme_name: str) -> None:
        """Método `DatHighlighter._rebuild_formats`.
            Parâmetros: `self`, `theme_name`."""
        from app.ui.editor.themes import theme_colors

        colors = theme_colors(theme_name)

        self.f_keyword = QTextCharFormat()
        self.f_keyword.setForeground(QColor(colors["keyword"]))
        self.f_keyword.setFontWeight(QFont.Weight.Bold)

        self.f_keyword_unknown = QTextCharFormat()
        self.f_keyword_unknown.setForeground(QColor(colors["keyword_unknown"]))
        self.f_keyword_unknown.setFontWeight(QFont.Weight.Bold)

        self.f_token = QTextCharFormat()
        self.f_token.setForeground(QColor(colors["token"]))
        self.f_token.setFontWeight(QFont.Weight.Bold)

        self.f_token_prefixed = QTextCharFormat()
        self.f_token_prefixed.setForeground(QColor(colors["string"]))
        self.f_token_prefixed.setFontWeight(QFont.Weight.Bold)
        self.f_token_prefixed.setFontItalic(True)

        self.f_comment = QTextCharFormat()
        self.f_comment.setForeground(QColor(colors["comment"]))
        self.f_comment.setFontItalic(True)

        self.f_number = QTextCharFormat()
        self.f_number.setForeground(QColor(colors["number"]))

        self.f_string = QTextCharFormat()
        self.f_string.setForeground(QColor(colors["string"]))

    def apply_theme(self, theme_name: str) -> None:
        """Método `DatHighlighter.apply_theme`.
            Parâmetros: `self`, `theme_name`."""
        self._rebuild_formats(theme_name)
        self.rehighlight()

    def set_variables(self, variables: dict) -> None:
        """Método `DatHighlighter.set_variables`.
            Parâmetros: `self`, `variables`."""
        self._variables = dict(variables)
        self.rehighlight()

    def highlightBlock(self, text: str) -> None:
        """Método `DatHighlighter.highlightBlock`.
            Parâmetros: `self`, `text`.
            Retorna o resultado calculado a partir do estado local."""
        comment_ranges = [(m.start(), m.end()) for m in COMMENT_RE.finditer(text)]

        def in_comment(pos: int) -> bool:
            """Função `in_comment`.
                Parâmetros: `pos`.
                Retorna o resultado calculado a partir do estado local."""
            return any(start <= pos < end for start, end in comment_ranges)

        for start, end in comment_ranges:
            self.setFormat(start, end - start, self.f_comment)

        for match in KEYWORD_RE.finditer(text):
            if in_comment(match.start()):
                continue
            kw = match.group(1).upper()
            fmt = self.f_keyword if kw in CMG_KEYWORDS else self.f_keyword_unknown
            self.setFormat(match.start(1), len(match.group(1)), fmt)

        for match in STRING_RE.finditer(text):
            if in_comment(match.start()):
                continue
            self.setFormat(match.start(), match.end() - match.start(), self.f_string)

        for match in TOKEN_RE.finditer(text):
            if in_comment(match.start()):
                continue
            color = self.f_token if match.group("prefix") is None else self.f_token_prefixed
            self.setFormat(match.start(), match.end() - match.start(), color)

        for match in NUMBER_RE.finditer(text):
            if in_comment(match.start()):
                continue
            self.setFormat(match.start(), match.end() - match.start(), self.f_number)
