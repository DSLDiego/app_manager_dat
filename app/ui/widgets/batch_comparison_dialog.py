"""Dialog comparação de batches (LHS vs MC): tabela de deltas + ranking de divergência."""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPen, QBrush
from PySide6.QtWidgets import (
    QDialog,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from app.domain.batch_comparison import BatchComparisonResult
from app.core.parsing import var_label
from app.services.comparison_round34 import batch_divergence_ranking, format_batch_ranking


class BatchComparisonDialog(QDialog):
    """Classe `BatchComparisonDialog` do módulo."""
    def __init__(self, result: BatchComparisonResult, parent=None):
        """Método `BatchComparisonDialog.__init__`.
            Parâmetros: `self`, `result`, `parent`."""
        super().__init__(parent)
        self.setWindowTitle(
            f"Batch {result.batch_a_id} vs {result.batch_b_id}"
        )
        layout = QVBoxLayout(self)

        self.table = QTableWidget(len(result.variables), 9)
        headers = [
            "Variable", "Mean A", "Mean B", "p10 A", "p10 B",
            "p50 A", "p50 B", "p90 A", "p90 B", "Δ Mean", "Δ%",
        ]
        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(headers)
        self.table.verticalHeader().setVisible(False)
        for r, v in enumerate(result.variables):
            cells = [
                var_label(v.var_id),
                f"{v.mean_a:.6g}", f"{v.mean_b:.6g}",
                f"{v.p10_a:.6g}", f"{v.p10_b:.6g}",
                f"{v.p50_a:.6g}", f"{v.p50_b:.6g}",
                f"{v.p90_a:.6g}", f"{v.p90_b:.6g}",
                f"{v.mean_delta:.6g}",
                f"{v.mean_delta_pct:.6g}%" if v.mean_delta_pct is not None else "",
            ]
            for c, text in enumerate(cells):
                self.table.setItem(r, c, QTableWidgetItem(text))
        layout.addWidget(self.table)

        # T5442: ranking de variáveis mais divergentes
        rank_bar = QHBoxLayout()
        self.btn_rank = QPushButton("Ranking de divergência")
        self.btn_rank.setToolTip("Mostrar variáveis mais divergentes entre batches A e B.")
        self.btn_rank.clicked.connect(self._show_ranking)
        rank_bar.addStretch()
        rank_bar.addWidget(self.btn_rank)
        rank_bar.addStretch()
        layout.insertLayout(0, rank_bar)

        header = QLabel(
            f"A: {result.batch_a_id} ({result.n_a} exps) — "
            f"B: {result.batch_b_id} ({result.n_b} exps)"
        )
        layout.insertWidget(1, header)

    def _show_ranking(self):
        """T5442: mostra ranking de variáveis mais divergentes."""
        import re

        # Coletar stats das variáveis da tabela (QTableWidget: usar .item())
        stats = []
        for r in range(self.table.rowCount()):
            var_id_item = self.table.item(r, 0)
            mean_a_item = self.table.item(r, 1)
            mean_b_item = self.table.item(r, 2)
            if not (var_id_item and mean_a_item and mean_b_item):
                continue
            label = var_id_item.text()
            # aceita '$1' (numérico) e '$var10002' (>= 10000)
            m = re.match(r"\$(?:var)?(\d+)", label)
            if not m:
                continue
            try:
                mean_a = float(mean_a_item.text())
                mean_b = float(mean_b_item.text())
            except ValueError:
                continue
            stats.append({
                "var_id": int(m.group(1)),
                "mean_a": mean_a,
                "mean_b": mean_b,
                "std_a": abs(mean_a) * 0.1,  # estimativa
                "std_b": abs(mean_b) * 0.1,  # estimativa
            })
        if not stats:
            QMessageBox.information(self, "Ranking", "Nenhum dado para ranking.")
            return
        ranked = batch_divergence_ranking(stats, top=10)
        lines = format_batch_ranking(ranked, width=60)
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Ranking de divergência")
        dlg.setText("Variáveis mais divergentes:")
        dlg.setIcon(QMessageBox.Information)
        details = "\n".join(lines)
        dlg.setDetailedText(details)
        dlg.exec()
