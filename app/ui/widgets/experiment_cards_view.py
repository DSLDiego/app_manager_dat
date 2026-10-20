"""Cartões de experimentos — formato grid n×m alternativo à tabela.

Cada cartão: nº externo + barras coloridas por variável (escala global do lote).
Puro em card_grid(); UI leve, ≤ MAX_CARDS por tela + aviso de paginação.
"""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont, QPalette
from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
    QLabel,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from app.core.parsing import var_label
from app.ui.colors import color_with_palette

CARD_COLS_DEFAULT = 4
MAX_CARDS = 60

SHEET_HEX = "#f2f5f8"
CARD_HEX = "#ffffff"


def card_grid(n_items: int, cols: int = CARD_COLS_DEFAULT) -> tuple[int, int, int]:
    """(linhas, colunas, cartões mostrados) — grade n×m pura."""
    cols = max(1, int(cols))
    rows = max(1, -(-max(0, n_items) // cols))
    shown = min(n_items, MAX_CARDS)
    return rows, cols, shown


def global_scales(rows: list, var_ids: list[int]) -> dict[int, tuple[float, float]]:
    """(min, max) por variável sobre a página (fallback 0..1)."""
    scales: dict[int, tuple[float, float]] = {}
    for var_id in var_ids:
        vals = [r["values"].get(var_id) for r in rows if r["values"].get(var_id) is not None]
        if vals:
            scales[var_id] = (min(vals), max(vals))
        else:
            scales[var_id] = (0.0, 0.0)
    return scales


class ExperimentCard(QFrame):
    """Um experimento: id + valor de cada variável colorido pela escala do lote."""

    def __init__(self, exp_id: int, palette_name: str = "azul\u2192amarelo", parent=None):
        """Método `ExperimentCard.__init__`.
            Parâmetros: `self`, `exp_id`, `palette_name`, `parent`."""
        super().__init__(parent)
        self.setStyleSheet(
            f"QFrame {{ background: {CARD_HEX}; border: 1px solid #d3dde8; border-radius: 4px; }}\n"
            "QLabel { border: none; }"
        )
        self.exp_id = exp_id
        self.palette_name = palette_name
        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(6, 4, 6, 4)
        self._layout.setSpacing(1)
        lbl_id = QLabel(f"#{exp_id}")
        f = QFont()
        f.setBold(True)
        lbl_id.setFont(f)
        self._layout.addWidget(lbl_id)
        self._bars: dict[int, QLabel] = {}
        self._scales: dict[int, tuple[float, float]] = {}

    def set_bars(self, values: dict[int, float | None], scales: dict[int, tuple[float, float]]) -> None:
        """Método `ExperimentCard.set_bars`.
            Parâmetros: `self`, `values`, `scales`."""
        self._scales = scales
        for lbl in list(self._bars.values()):
            lbl.setParent(None)
            lbl.deleteLater()
        self._bars.clear()
        for var_id, value in scales.items():
            v = values.get(var_id)
            text = f"{var_label(var_id)}: {'—' if v is None else f'{v:.4g}'}"
            lbl = QLabel(text)
            if v is None:
                lbl.setStyleSheet("color:#8a94a0;")
            else:
                lo, hi = scales[var_id]
                ratio = 0.5 if hi - lo < 1e-12 else (v - lo) / (hi - lo)
                hexc = color_with_palette(ratio, 0.0, 1.0, self.palette_name)
                c = QColor(hexc)
                text_hex = (
                    "#20262e" if c.lightness() > 130 else "#f5f7fa"
                )
                lbl.setStyleSheet(
                    f"background:{hexc}; color:{text_hex}; border-radius:3px; padding:0 3px;"
                )
            self._layout.addWidget(lbl)
            self._bars[var_id] = lbl


class ExperimentCardsView(QWidget):
    """Scroll + grade de cartões; consome rows do modelo paginado."""

    def __init__(self, cols: int = CARD_COLS_DEFAULT, parent=None):
        """Método `ExperimentCardsView.__init__`.
            Parâmetros: `self`, `cols`, `parent`."""
        super().__init__(parent)
        self._cols = cols
        self._palette_name = "azul→amarelo"

        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(2)
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setFrameShape(QFrame.Shape.NoFrame)
        outer.addWidget(self.scroll, 1)

        self.container = QWidget()
        self.grid = QGridLayout(self.container)
        self.grid.setContentsMargins(4, 4, 4, 4)
        self.grid.setSpacing(4)
        self.scroll.setWidget(self.container)

        self.lbl_note = QLabel("")
        outer.addWidget(self.lbl_note)

    # ---------- dados ----------
    def set_palette(self, name: str):
        """Método `ExperimentCardsView.set_palette`.
            Parâmetros: `self`, `name`."""
        self._palette_name = name
        self.update()

    def _make_placeholder(self) -> QFrame:
        """Slot vazio da grade: ocupa arrumado em vez de buraco branco."""
        frame = QFrame()
        frame.setStyleSheet(
            f"QFrame {{ background: {SHEET_HEX}; border: 1px dashed #c9d3df; "
            "border-radius: 4px; } QLabel { border: none; color:#aeb8c4; }"
        )
        lay = QVBoxLayout(frame)
        lay.setContentsMargins(6, 4, 6, 4)
        lbl = QLabel("vazio")
        lay.addWidget(lbl)
        lay.addStretch(1)
        return frame

    def set_data(self, rows: list, var_ids: list[int], scales: dict | None = None) -> int:
        """Método `ExperimentCardsView.set_data`.
            Parâmetros: `self`, `rows`, `var_ids`, `scales`.
            Retorna o resultado calculado a partir do estado local."""
        while self.grid.count():
            item = self.grid.takeAt(0)
            w = item.widget()
            if w is not None:
                w.setParent(None)
                w.deleteLater()
        rows = list(rows)
        if scales is None:
            scales = global_scales(rows, var_ids)
        to_show = rows[:MAX_CARDS]
        if len(rows) > MAX_CARDS:
            self.lbl_note.setText(f"cartões: só os {MAX_CARDS} primeiros (página maior)")
        else:
            self.lbl_note.setText("")
        for i, row in enumerate(to_show):
            r, c = divmod(i, self._cols)
            card = ExperimentCard(int(row["external_id"]), self._palette_name)
            card.set_bars(row.get("values") or {}, scales)
            self.grid.addWidget(card, r, c)
        line_r, cols_n, _ = card_grid(len(to_show), self._cols)
        for c in range(cols_n):
            self.grid.setColumnStretch(c, 1)
        shape = card_grid(len(to_show), self._cols)
        total_cells = shape[0] * cols_n
        for j in range(len(to_show), total_cells):
            r, c = divmod(j, self._cols)
            self.grid.addWidget(self._make_placeholder(), r, c)
        return len(to_show)
