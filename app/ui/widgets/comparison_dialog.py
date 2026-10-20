"""Dialog de comparação de dois experimentos: tabela de diffs + diff do .dat + scatter."""

from __future__ import annotations

from PySide6.QtCore import QRectF, Signal
from PySide6.QtGui import QBrush, QColor, QPainter, QPen
from PySide6.QtWidgets import (
    QDialog,
    QHBoxLayout,
    QLabel,
    QPlainTextEdit,
    QSizePolicy,
    QSpinBox,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from app.core.parsing import var_label
from app.services.comparison_round34 import scatter_points, unified_with_context
from app.services.comparison_service import ComparisonResult, ComparisonService


class ScatterPlotWidget(QWidget):
    """T5441: scatter por variável desenhado com QPainter (pontos + eixos + ticks)."""

    def __init__(self, parent=None):
        """Método `ScatterPlotWidget.__init__`.
            Parâmetros: `self`, `parent`."""
        super().__init__(parent)
        self.values_a: list[float] = []
        self.values_b: list[float] = []
        self.correlation: float = 0.0
        self.setMinimumSize(320, 260)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

    def set_data(self, values_a, values_b) -> int:
        """Carrega os pares (a, b) usando `scatter_points` e repinta. Retorna nº de pontos."""
        xs, ys, corr = scatter_points(values_a, values_b)
        self.values_a = xs
        self.values_b = ys
        self.correlation = corr
        self.update()
        return len(xs)

    def paintEvent(self, event):
        """Desenha eixos, ticks, pontos e o rótulo com a correlação."""
        super().paintEvent(event)
        qp = QPainter(self)
        qp.setRenderHint(QPainter.Antialiasing)
        margin = 36
        w = self.width() - 2 * margin
        h = self.height() - 2 * margin
        if w <= 10 or h <= 10:
            return
        n = min(len(self.values_a), len(self.values_b))
        if n < 1:
            qp.setPen(QColor("#7f8c8d"))
            qp.drawText(margin, self.height() // 2, "sem dados")
            return
        va, vb = self.values_a, self.values_b
        x_min, x_max = min(va), max(va)
        y_min, y_max = min(vb), max(vb)

        def to_x(val: float) -> float:
            if x_max > x_min:
                return margin + (val - x_min) / (x_max - x_min) * w
            return margin + w / 2

        def to_y(val: float) -> float:
            if y_max > y_min:
                return margin + h - (val - y_min) / (y_max - y_min) * h
            return margin + h / 2

        # eixos
        qp.setPen(QPen(QColor("#555555"), 1))
        qp.drawLine(margin, margin, margin, margin + h)        # Y
        qp.drawLine(margin, margin + h, margin + w, margin + h)  # X
        # ticks + rótulos
        for i in range(5):
            x = margin + i * w / 4
            qp.drawLine(int(x), margin + h, int(x), margin + h + 4)
            qp.drawText(int(x) - 14, margin + h + 18, f"{x_min + i * (x_max - x_min) / 4:.4g}")
            y = margin + i * h / 4
            qp.drawLine(margin - 4, int(y), margin, int(y))
            qp.drawText(2, int(y) + 4, f"{y_max - i * (y_max - y_min) / 4:.4g}")
        # pontos
        qp.setPen(QPen(QColor("#2c3e50"), 1))
        qp.setBrush(QBrush(QColor("#2980b9")))
        for i in range(n):
            qp.drawEllipse(QRectF(to_x(va[i]) - 3, to_y(vb[i]) - 3, 6, 6))
        # rótulo
        qp.setPen(QColor("#555555"))
        qp.drawText(6, 14, f"Scatter (r={self.correlation:.3f}, n={n})")


class ComparisonDialog(QDialog):
    """Classe `ComparisonDialog` do módulo."""

    def __init__(self, result: ComparisonResult, parent=None):
        # ordena por divergência (mais divergente primeiro)
        """Método `ComparisonDialog.__init__`.
            Parâmetros: `self`, `result`, `parent`."""
        super().__init__(parent)
        self.setWindowTitle(
            f"Comparar exp {result.exp_a_id} vs exp {result.exp_b_id}"
        )
        self.setMinimumSize(700, 550)

        layout = QVBoxLayout(self)

        self._diffs = ComparisonService.divergence_ranking(result.diffs)
        self.table = QTableWidget(len(self._diffs), 5)
        header_labels = ["Variável", "A", "B", "Δ", "Δ%"]
        self.table.verticalHeader().setVisible(False)
        self.table.setColumnCount(len(header_labels))
        self.table.setHorizontalHeaderLabels(header_labels)
        for r, d in enumerate(self._diffs):
            self.table.setItem(r, 0, QTableWidgetItem(var_label(d.var_id)))
            self.table.setItem(
                r, 1, QTableWidgetItem(f"{d.value_a:.10g}" if d.value_a is not None else "")
            )
            self.table.setItem(
                r, 2, QTableWidgetItem(f"{d.value_b:.10g}" if d.value_b is not None else "")
            )
            self.table.setItem(
                r, 3, QTableWidgetItem(f"{d.abs_diff:.10g}" if d.abs_diff is not None else "")
            )
            self.table.setItem(
                r, 4, QTableWidgetItem(f"{d.rel_diff:.10g}%" if d.rel_diff is not None else "")
            )
        layout.addWidget(self.table)

        # T5439: diff textual com janela de contexto ajustável
        bar = QHBoxLayout()
        bar.addWidget(QLabel("Contexto:"))
        self.spin_context = QSpinBox()
        self.spin_context.setRange(0, 20)
        self.spin_context.setValue(3)
        self.spin_context.setToolTip("Linhas de contexto do diff (0 = só mudanças).")
        bar.addWidget(self.spin_context)
        bar.addStretch()
        layout.addLayout(bar)

        self.diff_view = QPlainTextEdit()
        self.diff_view.setReadOnly(True)
        self._dat_a = result.dat_text_a
        self._dat_b = result.dat_text_b
        self.diff_view.setPlainText(
            unified_with_context(self._dat_a, self._dat_b, 3)
            if (self._dat_a and self._dat_b)
            else (result.dat_diff or "— sem diff de .dat —")
        )
        layout.addWidget(self.diff_view)
        self.spin_context.valueChanged.connect(self._recompute_dat_diff)

        # T5441: scatter por variável
        self.scatter_widget = ScatterPlotWidget()
        layout.addWidget(self.scatter_widget)

    def _recompute_dat_diff(self, context: int):
        """T5439: recalcula o diff do .dat com a janela escolhida."""
        if not self._dat_a or not self._dat_b:
            return
        self.diff_view.setPlainText(
            unified_with_context(self._dat_a, self._dat_b, context)
        )

    def update_scatter(self, values_a, values_b) -> int:
        """T5441: atualiza o scatter plot com os valores de uma variável. Retorna nº de pontos."""
        return self.scatter_widget.set_data(values_a, values_b)
