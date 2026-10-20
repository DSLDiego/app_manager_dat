"""Dialog de comparação tripla A/B/C (T5438) e scatter por variável (T5441)."""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import (
    QDialog,
    QLabel,
    QSplitter,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from app.services.comparison_service import ComparisonService
from app.services.comparison_round34 import scatter_points
from app.core.parsing import var_label


class ScatterCanvas(QWidget):
    """Scatter matplotlib-free (QPainter) dos pares A×B de uma variável."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._xs: list[float] = []
        self._ys: list[float] = []
        self.setMinimumSize(260, 220)
        self.setWindowTitle("Scatter A×B")

    def set_points(self, xs, ys, label=""):
        """Guarda os pares e redesenha (múnimo 2 pts fazem o range)."""
        self._xs = [float(v) for v in (xs or [])]
        self._ys = [float(v) for v in (ys or [])]
        self.setToolTip(label)
        self.update()

    def paintEvent(self, event):  # noqa: N802 (Qt)
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.GlobalColor.white)
        if len(self._xs) < 2:
            painter.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter, "sem dados")
            return
        margin = 24
        w = self.width() - 2 * margin
        h = self.height() - 2 * margin
        x0, x1 = min(self._xs), max(self._xs)
        y0, y1 = min(self._ys), max(self._ys)
        rx, ry = (x1 - x0) or 1.0, (y1 - y0) or 1.0
        painter.setPen(Qt.GlobalColor.darkBlue)
        for x, y in zip(self._xs, self._ys):
            px = int(margin + (x - x0) / rx * w)
            py = int(self.height() - margin - ((y - y0) / ry) * h)
            painter.drawRect(px - 2, py - 2, 4, 4)


class TripleCompareDialog(QDialog):
    """Três experimentos: tabela A/B/C + gráfico scatter A×B por variável."""

    def __init__(self, rows: list, service, parent=None):
        """rows: [(label, values), ...] já resolvidos."""
        super().__init__(parent)
        self.setWindowTitle("Comparação A/B/C")
        self.resize(860, 560)
        layout = QVBoxLayout(self)

        var_ids = sorted({int(v) for _, values in rows for v in values})
        self.table = QTableWidget(len(var_ids), len(rows), self)
        labels = [label for label, _ in rows]
        self.table.setHorizontalHeaderLabels(labels)
        self.table.verticalHeader().setVisible(False)
        for r, var_id in enumerate(var_ids):
            self.table.setItem(r, 0, QTableWidgetItem(var_label(var_id)))
            for c, (_, values) in enumerate(rows):
                value = values.get(var_id)
                self.table.setItem(
                    r, c,
                    QTableWidgetItem(f"{value:.10g}" if value is not None else ""),
                )
        if len(var_ids):
            self.table.resizeColumnsToContents()
        layout.addWidget(self.table, 3)

        self.plot = ScatterCanvas(self)
        split = QSplitter(self)
        split.addWidget(self.plot)
        info = QLabel("Selecione os 2 primeiros experimentos para o scatter.")
        split.addWidget(info)
        layout.addWidget(split, 1)

    def set_scatter(self, values_a, values_b, label=""):
        """Preenche o scatter com pares (A, B) da variável atual."""
        xs, ys, _ = scatter_points(values_a, values_b)
        self.plot.set_points(xs, ys, label)
        self.plot.show()
