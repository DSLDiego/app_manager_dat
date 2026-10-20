"""Minimapa do editor — visão aérea do arquivo (barras por linha).

Puro em minimap_bars(); o widget espelha o scroll vertical do CodeEditor.
"""

from __future__ import annotations

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QColor, QPainter
from PySide6.QtWidgets import QWidget

MAX_MINIMAP_LINES = 4000
BAR_W_FRAC_MAX = 1.0


def minimap_bars(lines: list[str], max_lines: int = MAX_MINIMAP_LINES) -> list[float]:
    """Fração de largura (0..1) por linha — puro; cap de linhas."""
    if not lines:
        return []
    lines = lines[:max_lines]
    longest = max(1, max(len(line) for line in lines))
    return [min(BAR_W_FRAC_MAX, len(line) / longest) for line in lines]


def scroll_window(n_lines: int, visible: int, first: int) -> tuple[float, float]:
    """(topo, altura) da janela visível em fração — puro, seguro p/ 0 linhas."""
    if n_lines <= 0:
        return 0.0, 1.0
    top = min(1.0, max(0.0, first / n_lines))
    height = min(1.0 - top, max(0.0, visible / n_lines))
    return top, height


class EditorMinimap(QWidget):
    """Coluna fina à direita do editor: barras por linha + janela visível."""

    lineClicked = Signal(int)
    MIN_WIDTH = 48

    def __init__(self, parent=None):
        """Método `EditorMinimap.__init__`.
            Parâmetros: `self`, `parent`."""
        super().__init__(parent)
        self._bars: list[float] = []
        self._win: tuple[float, float] = (0.0, 1.0)
        self._colors = {
            "bg": "#f4f6f9",
            "bar": "#b8c4d0",
            "win": (90, 130, 180, 40),
        }
        self.setMinimumWidth(self.MIN_WIDTH)
        self.setMaximumWidth(72)
        self.setToolTip("Minimapa — clique para navegar até a posição.")

    # ---------- estado ----------
    def set_theme_colors(self, bg_hex: str, bar_hex: str, win_rgb: tuple | None = None):
        """Cores do minimapa acompanham o tema do editor (r20)."""
        self._colors["bg"] = str(bg_hex)
        self._colors["bar"] = str(bar_hex)
        if win_rgb is not None:
            self._colors["win"] = win_rgb
        self.update()
    def set_document(self, text: str):
        """Método `EditorMinimap.set_document`.
            Parâmetros: `self`, `text`."""
        self._bars = minimap_bars(text.splitlines())
        self.update()

    def set_scroll(self, n_lines: int, visible: int, first: int):
        """Método `EditorMinimap.set_scroll`.
            Parâmetros: `self`, `n_lines`, `visible`, `first`."""
        self._win = scroll_window(n_lines, visible, first)
        self.update()

    # ---------- navegação ----------
    def line_at(self, y: float) -> int:
        """Linha clicada — puro-friendly (usa altura atual)."""
        if not self._bars or self.height() <= 0:
            return 0
        return min(len(self._bars) - 1, max(0, int(y / self.height() * len(self._bars))))

    def mousePressEvent(self, event):
        """Método `EditorMinimap.mousePressEvent`.
            Parâmetros: `self`, `event`."""
        self.lineClicked.emit(self.line_at(event.position().y()))
        event.accept()

    # ---------- pintura ----------
    def paintEvent(self, event):
        """Método `EditorMinimap.paintEvent`.
            Parâmetros: `self`, `event`."""
        p = QPainter(self)
        p.fillRect(self.rect(), QColor(self._colors["bg"]))
        if not self._bars:
            return
        bar_h = max(1.0, self.height() / len(self._bars))
        bar_area_w = self.width() - 4
        p.setPen(Qt.PenStyle.NoPen)
        bar_color = QColor(self._colors["bar"])
        for i, frac in enumerate(self._bars):
            w = max(2.0, frac * bar_area_w)
            p.fillRect(2.0, i * bar_h, w, max(1.0, bar_h - 1.0), bar_color)
        # janela visível
        top, height = self._win
        y = top * self.height()
        h = max(8.0, height * self.height())
        win_color = self._colors["win"]
        if len(win_color) == 4:
            p.fillRect(0, y, self.width(), h, QColor(*win_color))
        else:
            p.fillRect(0, y, self.width(), h, QColor(*win_color, 40))
        p.end()
