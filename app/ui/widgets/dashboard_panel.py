"""Dashboard: KPIs, gráficos matplotlib e tabelas de atividade."""

from __future__ import annotations

from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QTabWidget,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from app.services.metrics_service import MetricsService


class KpiTile(QLabel):
    """Classe `KpiTile` do módulo."""
    def __init__(self, title: str, value: str = "—"):
        """Método `KpiTile.__init__`.
            Parâmetros: `self`, `title`, `value`."""
        super().__init__(f"<b>{title}</b><br>{value}")
        self.setMinimumWidth(140)
        self.setStyleSheet("padding:8px; font-size:15px;")


class DashboardPanel(QWidget):
    """Classe `DashboardPanel` do módulo."""
    def __init__(self, metrics: MetricsService, parent=None):
        """Método `DashboardPanel.__init__`.
            Parâmetros: `self`, `metrics`, `parent`."""
        super().__init__(parent)
        self.metrics = metrics

        layout = QVBoxLayout(self)
        layout.setContentsMargins(6, 3, 6, 3)
        layout.setSpacing(2)
        header = QHBoxLayout()
        self.tile_batches = KpiTile("Batches")
        self.tile_experiments = KpiTile("Experimentos")
        self.tile_templates = KpiTile("Templates")
        self.tile_logs_24h = KpiTile("Logs 24h")
        for t in (self.tile_batches, self.tile_experiments, self.tile_templates, self.tile_logs_24h):
            header.addWidget(t)
        layout.addLayout(header)

        self.tabs = QTabWidget()
        self.tab_actions = self._table_tab()
        self.tab_batches = self._table_tab()
        self.tab_days = self._table_tab()
        self.tabs.addTab(self.tab_actions, "Top ações")
        self.tabs.addTab(self.tab_batches, "Batchês recentes")
        self.tabs.addTab(self.tab_days, "Ações por dia")
        layout.addWidget(self.tabs)

        self.graphs_widget = None
        self.refresh()

    @staticmethod
    def _table_tab() -> QTableWidget:
        """Método `DashboardPanel._table_tab`.
            Retorna o resultado calculado a partir do estado local."""
        table = QTableWidget(0, 2)
        table.setHorizontalHeaderLabels(["Chave", "Valor"])
        table.verticalHeader().setVisible(False)
        return table

    def refresh(self):
        """Método `DashboardPanel.refresh`.
            Parâmetros: `self`."""
        if self.metrics is None:
            return
        s = self.metrics.summary()
        self.tile_batches.setText(f"<b>Batches</b><br>{s.total_batches}")
        self.tile_experiments.setText(f"<b>Experimentos</b><br>{s.total_experiments}")
        self.tile_templates.setText(f"<b>Templates</b><br>{s.total_templates}")
        self.tile_logs_24h.setText(f"<b>Logs 24h</b><br>{s.logs_24h}")

        self._fill(self.tab_actions, [(a, str(n)) for a, n in self.metrics.top_actions(15)])
        self._fill(self.tab_batches, [(b, str(n)) for b, n in self.metrics.experiments_per_batch(15)])
        self._fill(self.tab_days, [(d, str(n)) for d, n in self.metrics.actions_per_day(14)])

    @staticmethod
    def _fill(table: QTableWidget, rows: list):
        """Método `DashboardPanel._fill`.
            Parâmetros: `table`, `rows`."""
        table.setRowCount(len(rows))
        for r, (k, v) in enumerate(rows):
            table.setItem(r, 0, QTableWidgetItem(str(k)))
            table.setItem(r, 1, QTableWidgetItem(str(v)))
