"""Dialog de matriz de correlação com heatmap e reparo automático."""

from __future__ import annotations

from typing import List

import numpy as np
from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QDialog,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSpinBox,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
)

from app.core.parsing import var_label
from app.services.correlation_service import CorrelationService


def _color_from_value(value: float):
    """Função `_color_from_value`.
        Parâmetros: `value`.
        Retorna o resultado calculado a partir do estado local."""
    from PySide6.QtGui import QColor

    # -1 vermelho -> 0 branco -> +1 azul
    if value >= 0:
        return QColor(235 - int(130 * value), 235, 235)
    return QColor(235, 235, int(235 + 130 * value))


class CorrelationDialog(QDialog):
    """Classe `CorrelationDialog` do módulo."""
    accepted_correlation = Signal(object)  # list[list[float]]

    def __init__(self, var_ids: List[int], corr: List[List[float]] | None = None, parent=None):
        """Método `CorrelationDialog.__init__`.
            Parâmetros: `self`, `var_ids`, `corr`, `parent`."""
        super().__init__(parent)
        self.setWindowTitle("Matriz de Correlação")
        self.service = CorrelationService()
        self.var_ids = var_ids
        if corr is None:
            corr = self.service.identity(len(var_ids))
        self.corr = corr

        self.table = QTableWidget(len(var_ids), len(var_ids))
        labels = [var_label(v) for v in var_ids]
        self.table.setHorizontalHeaderLabels(labels)
        self.table.setVerticalHeaderLabels(labels)
        layout = QVBoxLayout(self)
        layout.addWidget(self.table)

        top = QHBoxLayout()
        self.spin_n = QSpinBox()
        self.spin_n.setRange(2, 200)
        self.spin_n.setValue(len(var_ids))
        btn_resize = QPushButton("Redimensionar")
        btn_resize.clicked.connect(self._resize)
        top.addWidget(QLabel("N:"))
        top.addWidget(self.spin_n)
        top.addWidget(btn_resize)
        top.addStretch()
        layout.addLayout(top)

        bottom = QHBoxLayout()
        btn_validate = QPushButton("Validar")
        btn_repair = QPushButton("Reparar (PSD)")
        btn_ok = QPushButton("Aplicar")
        btn_ok.setDefault(True)
        bottom.addStretch()
        bottom.addWidget(btn_validate)
        bottom.addWidget(btn_repair)
        bottom.addWidget(btn_ok)
        layout.addLayout(bottom)

        btn_validate.clicked.connect(self._validate)
        btn_repair.clicked.connect(self._repair)
        btn_ok.clicked.connect(self._apply)

        self.label_status = QLabel("")
        layout.addWidget(self.label_status)
        self._fill()

    def _fill(self):
        """Método `CorrelationDialog._fill`.
            Parâmetros: `self`."""
        self.table.setRowCount(len(self.corr))
        for r, row in enumerate(self.corr):
            self.table.setRowHeight(r, 26)
            for c, value in enumerate(row[: self.table.columnCount()]):
                item = QTableWidgetItem(f"{value:.2f}")
                item.setBackground(_color_from_value(float(value)))
                self.table.setItem(r, c, item)

    def _read_matrix(self) -> List[List[float]]:
        """Método `CorrelationDialog._read_matrix`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        n = len(self.var_ids)
        matrix = []
        current = self.corr
        for r in range(n):
            row = []
            for c in range(n):
                text = self.table.item(r, c).text() if self.table.item(r, c) else "0"
                try:
                    row.append(float(text))
                except ValueError:
                    row.append(0.0)
            matrix.append(row)
        self.corr = matrix
        return matrix

    def _validate(self):
        """Método `CorrelationDialog._validate`.
            Parâmetros: `self`."""
        ok, msg = self.service.is_valid(self._read_matrix())
        self.label_status.setText(("✓ " if ok else "✗ ") + msg)

    def _repair(self):
        """Método `CorrelationDialog._repair`.
            Parâmetros: `self`."""
        repaired = self.service.repair(self._read_matrix())
        self.corr = repaired
        self._fill()
        self.label_status.setText("Matriz reparada.")

    def _resize(self):
        """Método `CorrelationDialog._resize`.
            Parâmetros: `self`."""
        n = self.spin_n.value()
        old = np.asarray(self.corr, dtype=float)
        identity = np.eye(n)
        portion = old[:n, :n]
        k = min(portion.shape)
        identity[:k, :k] = portion
        np.fill_diagonal(identity, 1.0)
        old_ids = list(self.var_ids)
        if n <= len(old_ids):
            self.var_ids = old_ids[:n]
        else:
            self.var_ids = old_ids + list(range(len(old_ids) + 1, n + 1))
        self.corr = identity.tolist()
        self.table.setRowCount(n)
        self.table.setColumnCount(n)
        labels = [var_label(v) for v in self.var_ids]
        self.table.setHorizontalHeaderLabels(labels)
        self.table.setVerticalHeaderLabels(labels)
        self._fill()

    def _apply(self):
        """Método `CorrelationDialog._apply`.
            Parâmetros: `self`."""
        matrix = self._read_matrix()
        ok, _ = self.service.is_valid(matrix)
        if not ok:
            self._validate()
            return
        self.accepted_correlation.emit(matrix)
        self.accept()
