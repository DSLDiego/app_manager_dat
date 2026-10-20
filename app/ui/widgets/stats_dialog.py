"""Estatísticas descritivas dos experimentos (por variável) — tabela em diálogo.

Puro em stats_summary(); MainWindow/painel só alimenta page_rows.
"""

from __future__ import annotations

import math

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
)

from app.core.parsing import var_label

STAT_COLUMNS = ("n", "mín", "média", "desvio", "máx")


def stats_summary(rows: list, var_ids: list[int]) -> dict[int, dict]:
    """{var_id: {n, min, mean, std, max}} — puro; sem dados ⇒ n=0 e campos None."""
    out: dict[int, dict] = {}
    for var_id in var_ids:
        vals = [
            float(r["values"][var_id])
            for r in rows
            if (r.get("values") or {}).get(var_id) is not None
        ]
        n = len(vals)
        if n == 0:
            out[var_id] = {"n": 0, "min": None, "mean": None, "std": None, "max": None}
            continue
        mean = sum(vals) / n
        var = sum((v - mean) ** 2 for v in vals) / n  # populacional
        out[var_id] = {
            "n": n,
            "min": min(vals),
            "mean": mean,
            "std": math.sqrt(var),
            "max": max(vals),
        }
    return out


def stats_row_text(summary: dict) -> str:
    """Linha compacta p/ tooltip/status — puro; None → '—'."""
    fmt = lambda v: "—" if v is None else f"{v:.4g}"  # noqa: E731
    return (
        f"n={summary['n']} · mín={fmt(summary['min'])} · média={fmt(summary['mean'])}"
        f" · desvio={fmt(summary['std'])} · máx={fmt(summary['max'])}"
    )


class StatsDialog(QDialog):
    """Tabela variáveis × estatísticas da página atual."""

    def __init__(self, rows: list, var_ids: list[int], parent=None):
        """Método `StatsDialog.__init__`.
            Parâmetros: `self`, `rows`, `var_ids`, `parent`."""
        super().__init__(parent)
        self.setWindowTitle("Estatísticas descritivas — página atual")
        self.resize(560, 320)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 6, 8, 6)
        layout.setSpacing(4)

        summary = stats_summary(rows, var_ids)
        self.lbl_info = QLabel(f"{len(var_ids)} variável(is) · {len(rows)} experimento(s) na página.")
        layout.addWidget(self.lbl_info)

        self.table = QTableWidget()
        self.table.setColumnCount(len(STAT_COLUMNS))
        self.table.setHorizontalHeaderLabels(list(STAT_COLUMNS))
        self.table.setRowCount(len(var_ids))
        self.table.setEditTriggers(self.table.editTriggers().__class__.NoEditTriggers)
        for i, var_id in enumerate(var_ids):
            s = summary[var_id]
            self.table.setVerticalHeaderItem(i, QTableWidgetItem(var_label(var_id)))
            values = [s["n"], s["min"], s["mean"], s["std"], s["max"]]
            for j, v in enumerate(values):
                text = "—" if v is None else (str(v) if j == 0 else f"{v:.4g}")
                item = QTableWidgetItem(text)
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.table.setItem(i, j, item)
        layout.addWidget(self.table, 1)

        bar = QHBoxLayout()
        btn_close = QPushButton("Fechar")
        btn_close.clicked.connect(self.accept)
        bar.addStretch()
        bar.addWidget(btn_close)
        layout.addLayout(bar)
