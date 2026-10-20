"""Dialog de estatísticas: tabela com p10/p50/p90, média, std, min/max."""

from __future__ import annotations

from PySide6.QtWidgets import (
    QDialog,
    QPushButton,
    QSpinBox,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
)

from app.services.statistics_service import StatisticsService


class StatisticsDialog(QDialog):
    """Classe `StatisticsDialog` do módulo."""
    STATS_COLUMNS = ("Métrica", "Valor")

    def __init__(self, stats_service: StatisticsService, values_provider, parent=None):
        """Método `StatisticsDialog.__init__`.
            Parâmetros: `self`, `stats_service`, `values_provider`, `parent`."""
        super().__init__(parent)
        self.setWindowTitle("Estatísticas dos Resultados")
        self.stats_service = stats_service
        self._values_provider = values_provider

        layout = QVBoxLayout(self)
        self.spin_var = QSpinBox()
        self.spin_var.setRange(1, 10**6)
        self.spin_var.setValue(1)
        layout.addWidget(self.spin_var)

        btn = QPushButton("Calcular")
        btn.clicked.connect(self.refresh)
        layout.addWidget(btn)

        self.table = QTableWidget(0, 2)
        self.table.setHorizontalHeaderLabels(list(self.STATS_COLUMNS))
        self.table.verticalHeader().setVisible(False)
        layout.addWidget(self.table)

    def refresh(self):
        """Método `StatisticsDialog.refresh`.
            Parâmetros: `self`."""
        var_id = self.spin_var.value()
        try:
            values = self._values_provider(var_id)
        except Exception as exc:
            values = []
        stats = self.stats_service.compute(var_id, values)

        rows = [
            ("Amostras", str(stats.count)),
            ("Média", f"{stats.mean:.10g}"),
            ("Desvio-Padrão", f"{stats.std:.10g}"),
            ("Mínimo", f"{stats.minimum:.10g}"),
            ("Máximo", f"{stats.maximum:.10g}"),
            ("p10", f"{stats.p10:.10g}"),
            ("p50", f"{stats.p50:.10g}"),
            ("p90", f"{stats.p90:.10g}"),
        ]

        self.table.setRowCount(len(rows))
        for r, (name, value) in enumerate(rows):
            self.table.setItem(r, 0, QTableWidgetItem(name))
            self.table.setItem(r, 1, QTableWidgetItem(value))
