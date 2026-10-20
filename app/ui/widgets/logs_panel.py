"""Painel de logs: filtros, busca, auto-refresh, export CSV."""

from __future__ import annotations

import csv
import json
import re

from PySide6.QtCore import QDate, QTimer, Signal
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDateEdit,
    QFileDialog,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)



class LogsPanel(QWidget):
    """Classe `LogsPanel` do módulo."""
    refreshRequested = Signal()

    COLUMNS = ("id", "created_at", "level", "category", "action", "destino", "message")

    LEVEL_COLORS = {
        "INFO": QColor("#2980b9"),
        "WARNING": QColor("#f39c12"),
        "ERROR": QColor("#c0392b"),
        "DEBUG": QColor("#7f8c8d"),
    }

    def __init__(self, log_repo, parent=None):
        """Método `LogsPanel.__init__`.
            Parâmetros: `self`, `log_repo`, `parent`."""
        super().__init__(parent)
        self.log_repo = log_repo
        self._rows = []

        layout = QVBoxLayout(self)
        layout.setContentsMargins(6, 3, 6, 3)
        layout.setSpacing(2)

        bar = QHBoxLayout()
        self.combo_category = QComboBox()
        self.combo_category.addItems(["Todos", "EDITOR", "SAMPLING", "EXPORT", "USAGE", "AUDIT", "SYSTEM"])
        self.combo_level = QComboBox()
        self.combo_level.addItems(["Todos", "INFO", "WARNING", "ERROR", "DEBUG"])
        self.input_search = QLineEdit()
        self.input_search.setPlaceholderText("Buscar…")
        # v1: filtro por intervalo de datas
        self.date_from = QDateEdit()
        self.date_from.setCalendarPopup(True)
        self.date_from.setDisplayFormat("yyyy-MM-dd")
        self.date_from.setSpecialValueText("inicio")
        self.date_from.setMinimumDate(QDate(2000, 1, 1))
        self.date_to = QDateEdit()
        self.date_to.setCalendarPopup(True)
        self.date_to.setDisplayFormat("yyyy-MM-dd")
        self.date_to.setSpecialValueText("fim")
        self.date_to.setMinimumDate(QDate(2000, 1, 1))
        self.chk_auto = QCheckBox("Auto-refresh (2s)")
        btn_refresh = QPushButton("Atualizar")
        btn_export = QPushButton("Exportar CSV")
        for w in (self.combo_category, self.combo_level, self.input_search, self.date_from, self.date_to, self.chk_auto, btn_refresh, btn_export):
            bar.addWidget(w)
        layout.addLayout(bar)

        self.table = QTableWidget(0, len(self.COLUMNS))
        self.table.setHorizontalHeaderLabels([c.upper() for c in self.COLUMNS])
        self.table.verticalHeader().setVisible(False)
        layout.addWidget(self.table)

        self.combo_category.currentIndexChanged.connect(self.refresh)
        self.combo_level.currentIndexChanged.connect(self.refresh)
        self.input_search.textChanged.connect(self.refresh)
        self.date_from.dateChanged.connect(self.refresh)
        self.date_to.dateChanged.connect(self.refresh)
        btn_refresh.clicked.connect(self.refresh)
        btn_export.clicked.connect(self.export_csv)

        self.timer = QTimer(self)
        self.timer.setInterval(2000)
        self.timer.timeout.connect(self.refresh)
        self.chk_auto.toggled.connect(self._toggle_auto)

    def _toggle_auto(self, checked: bool):
        """Método `LogsPanel._toggle_auto`.
            Parâmetros: `self`, `checked`."""
        if checked:
            self.timer.start()
        else:
            self.timer.stop()

    def refresh(self):
        """Método `LogsPanel.refresh`.
            Parâmetros: `self`."""
        if self.log_repo is None:
            return
        date_from = None
        date_to = None
        if self.date_from.date().isValid() and self.date_from.date() != self.date_from.minimumDate():
            date_from = self.date_from.date().toString("yyyy-MM-dd") + "T00:00:00"
        if self.date_to.date().isValid() and self.date_to.date() != self.date_to.minimumDate():
            date_to = self.date_to.date().toString("yyyy-MM-dd") + "T23:59:59"
        self._rows = self.log_repo.fetch(
            category=self.combo_category.currentText(),
            level=self.combo_level.currentText(),
            search=self.input_search.text() or None,
            date_from=date_from,
            date_to=date_to,
            limit=1000,
        )
        self.table.setRowCount(len(self._rows))
        for r, row in enumerate(self._rows):
            for c, key in enumerate(self.COLUMNS):
                value = self._cell_value(row, key)
                item = QTableWidgetItem(str(value))
                if key == "level" and str(value) in self.LEVEL_COLORS:
                    item.setForeground(self.LEVEL_COLORS[str(value)])
                self.table.setItem(r, c, item)

    @staticmethod
    def _cell_value(row: dict, key: str) -> str:
        """Método `LogsPanel._cell_value`.
            Parâmetros: `row`, `key`.
            Retorna o resultado calculado a partir do estado local."""
        if key == "destino":
            return parse_log_destino(row)
        return str(row.get(key, ""))

    def export_csv(self):
        """Método `LogsPanel.export_csv`.
            Parâmetros: `self`."""
        self.refresh()  # exporta o estado atual da consulta
        path, _ = QFileDialog.getSaveFileName(self, "Exportar logs", "logs.csv", "CSV (*.csv)")
        if not path:
            return
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(self.COLUMNS)
            for row in self._rows:
                writer.writerow([self._cell_value(row, c) for c in self.COLUMNS])


_PATH_RE = re.compile(r"[A-Za-z]:\\[^\r\n\"]+|/[^\r\n\"\s,]+|output[\\/]example_batch.*")


def parse_log_destino(row: dict) -> str:
    """Glitch-free: pasta de saída dos .dats gerados, via payload ou mensagem."""
    raw = row.get("payload_json")
    if raw:
        try:
            payload = json.loads(raw)
            output = payload.get("output_dir") or payload.get("output_root")
            if output:
                return str(output)
        except (json.JSONDecodeError, AttributeError):
            pass

    message = str(row.get("message") or "")
    match = _PATH_RE.search(message)
    if match:
        candidate = match.group(0).rstrip(".,;)")
        return candidate
    return ""
