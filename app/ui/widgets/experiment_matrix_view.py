"""Matriz experimentos × variáveis — células coloridas pela escala global.

Formato 4 do painel de experimentos: cada linha é um experimento, cada coluna
uma variável; cor = posição do valor na escala global do lote (azul→amarelo).
Puro em matrix_cells(); UI: QTableWidget com setBackground.
"""

from __future__ import annotations

from PySide6.QtGui import QColor
from PySide6.QtWidgets import QAbstractItemView, QTableWidget, QTableWidgetItem, QWidget

from app.core.parsing import var_label
from app.ui.colors import color_with_palette

MAX_MATRIX_ROWS = 200


def matrix_cells(
    rows: list, var_ids: list[int]
) -> tuple[list[list], dict[int, tuple[float, float]]]:
    """(células, escalas) — células[i][j] = valor ou None; puro.

    Linhas capadas em MAX_MATRIX_ROWS (o modelo paginado já limita, mas garantir).
    """
    var_ids = list(var_ids)
    cells: list[list] = []
    for row in rows[:MAX_MATRIX_ROWS]:
        values = row.get("values") or {}
        cells.append([values.get(var_id) for var_id in var_ids])
    scales: dict[int, tuple[float, float]] = {}
    for j, var_id in enumerate(var_ids):
        vals = [c[j] for c in cells if c[j] is not None]
        if vals:
            scales[var_id] = (min(vals), max(vals))
        else:
            scales[var_id] = (0.0, 0.0)
    return cells, scales


def cell_text(value) -> str:
    """Texto da célula — puro ('—' quando ausente)."""
    return "—" if value is None else f"{value:.4g}"


def cell_color(value, scale: tuple[float, float], palette: str) -> str:
    """Cor hex da célula na escala — puro; None → cinza neutro."""
    if value is None:
        return "#edf1f5"
    lo, hi = scale
    ratio = 0.5 if hi - lo < 1e-12 else (value - lo) / (hi - lo)
    return color_with_palette(ratio, 0.0, 1.0, palette)


def matrix_csv(rows: list, var_ids: list[int]) -> str:
    """CSV da matriz exp×var (';' decimal ponto, vazio p/ ausente) — puro."""
    header = "experimento;" + ";".join(var_label(v) for v in var_ids)
    lines = [header]
    for row in rows[:MAX_MATRIX_ROWS]:
        values = row.get("values") or {}
        cells = [
            "" if values.get(v) is None else f"{values.get(v):.6g}" for v in var_ids
        ]
        lines.append(str(row.get("external_id", 0)) + ";" + ";".join(cells))
    return "\n".join(lines) + "\n"


class ExperimentMatrixView(QWidget):
    """QTableWidget colorido: linhas=experimentos, colunas=variáveis."""

    def __init__(self, parent=None):
        """Método `ExperimentMatrixView.__init__`.
            Parâmetros: `self`, `parent`."""
        super().__init__(parent)
        from PySide6.QtWidgets import QVBoxLayout

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)
        self.table = QTableWidget()
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.setAlternatingRowColors(True)
        self.table.verticalHeader().setVisible(True)
        self.table.setToolTip("Matriz experimentos × variáveis — cor = escala global do lote.")
        layout.addWidget(self.table, 1)

    def set_data(self, rows: list, var_ids: list[int], palette: str = "azul\u2192amarelo") -> int:
        """Preenche a matriz; retorna nº de experimentos mostrados."""
        cells, scales = matrix_cells(rows, var_ids)
        self.table.setColumnCount(len(var_ids))
        self.table.setRowCount(len(cells))
        self.table.setHorizontalHeaderLabels([var_label(v) for v in var_ids])
        for i, row_vals in enumerate(cells):
            for j, value in enumerate(row_vals):
                item = QTableWidgetItem(cell_text(value))
                hexc = cell_color(value, scales[var_ids[j]], palette)
                c = QColor(hexc)
                item.setBackground(c)
                if value is not None:
                    item.setForeground(
                        QColor("#20262e") if c.lightness() > 130 else QColor("#f5f7fa")
                    )
                self.table.setItem(i, j, item)
        return len(cells)
