"""Lista compacta de experimentos — formato lista (uma linha por experimento).

Cada linha: `#id  var1=v1  var2=v2 …`. Puro em compact_row(); UI: QListWidget.
"""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QListWidget,
    QListWidgetItem,
    QVBoxLayout,
    QWidget,
)

from app.core.parsing import var_label

MAX_LIST_ROWS = 5000


def compact_row(row: dict, var_ids: list[int]) -> str:
    """Linha compacta — puro, fácil de testar."""
    parts: list[str] = [f"#{row.get('external_id', 0)}"]
    values = row.get("values") or {}
    for var_id in var_ids:
        v = values.get(var_id)
        parts.append(f"{var_label(var_id)}={'—' if v is None else f'{v:.4g}'}")
    return "  ".join(parts)


class ExperimentListView(QWidget):
    """Lista compacta; consome rows do modelo paginado (formato 3 do painel)."""

    def __init__(self, parent=None):
        """Método `ExperimentListView.__init__`.
            Parâmetros: `self`, `parent`."""
        super().__init__(parent)
        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(2)
        self.list = QListWidget()
        self.list.setToolTip("Um experimento por linha — var=valor em compacto.")
        self.list.setAlternatingRowColors(True)
        outer.addWidget(self.list, 1)
        self.lbl_note = QLabel("")
        outer.addWidget(self.lbl_note)

    def set_data(self, rows: list, var_ids: list[int]) -> int:
        """Preenche a lista; retorna nº de linhas mostradas."""
        self.list.clear()
        rows = list(rows)
        to_show = rows[:MAX_LIST_ROWS]
        for row in to_show:
            item = QListWidgetItem(compact_row(row, var_ids))
            item.setData(
                Qt.ItemDataRole.UserRole, int(row.get("external_id", 0))
            )
            self.list.addItem(item)
        if len(rows) > MAX_LIST_ROWS:
            self.lbl_note.setText(
                f"lista: só as {MAX_LIST_ROWS} primeiras (página maior)"
            )
        else:
            self.lbl_note.setText("")
        return len(to_show)
