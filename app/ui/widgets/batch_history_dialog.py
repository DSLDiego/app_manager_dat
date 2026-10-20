"""Histórico de lotes — tabela com seed/método/n e reuso da seed.

Pure helpers facilitam regressão sem widget.
"""

from __future__ import annotations

from typing import Any

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import (
    QDialog,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
)


def format_batch_row(row: dict[str, Any]) -> str:
    """Linha curta "batch · método · seed=N · M exps" — puro."""
    seed = row.get("seed")
    seed_txt = f"seed={seed}" if seed is not None else "seed=—"
    return (
        f"{row.get('id', '—')} · {row.get('method', '—')} · "
        f"{seed_txt} · {row.get('n_experiments', 0)} exps"
    )


class BatchHistoryDialog(QDialog):
    """Lista lotes (list_batches) + clipboard/e reuso da seed."""

    useRequested = Signal(int)

    def __init__(self, exp_repo, parent=None):
        """Método `BatchHistoryDialog.__init__`.
            Parâmetros: `self`, `exp_repo`, `parent`."""
        super().__init__(parent)
        self.setWindowTitle("Histórico de lotes")
        self.resize(560, 340)
        self.exp_repo = exp_repo

        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 6, 8, 6)
        layout.setSpacing(4)

        self.lbl_summary = QLabel("—")
        layout.addWidget(self.lbl_summary)

        self.table = QTableWidget()
        try:
            self._rows = list(self.exp_repo.list_batches(limit=100))
        except Exception:  # noqa: BLE001
            self._rows = []
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Lote", "Método", "Seed", "N exps", "Criação"])
        self.table.setEditTriggers(self.table.editTriggers().__class__.NoEditTriggers)
        self.table.setSelectionBehavior(self.table.selectionBehavior().__class__.SelectRows)
        self.table.setRowCount(len(self._rows))
        for i, row in enumerate(self._rows):
            self.table.setItem(i, 0, QTableWidgetItem(str(row.get("id", ""))))
            self.table.setItem(i, 1, QTableWidgetItem(str(row.get("method", ""))))
            self.table.setItem(i, 2, QTableWidgetItem(str(row.get("seed", ""))))
            self.table.setItem(i, 3, QTableWidgetItem(str(row.get("n_experiments", ""))))
            self.table.setItem(i, 4, QTableWidgetItem(str(row.get("created_at", ""))))
        if self._rows:
            self.table.selectRow(0)
        layout.addWidget(self.table, 1)

        self.lbl_row = QLabel("—")
        layout.addWidget(self.lbl_row)

        bar = QHBoxLayout()
        self.btn_copy = QPushButton("Copiar seed")
        self.btn_copy.setToolTip("Copia a seed do lote selecionado para o clipboard.")
        self.btn_use = QPushButton("Usar na próxima amostragem")
        self.btn_use.setToolTip("A seed será preenchida no diálogo de amostragem.")
        btn_close = QPushButton("Fechar")
        btn_close.clicked.connect(self.accept)
        bar.addWidget(self.btn_copy)
        bar.addWidget(self.btn_use)
        bar.addStretch()
        bar.addWidget(btn_close)
        layout.addLayout(bar)

        self._refresh_labels()
        self.table.itemSelectionChanged.connect(self._refresh_labels)
        self.btn_copy.clicked.connect(self._copy_seed)
        self.btn_use.clicked.connect(self._use_seed)

    # ---------- helpers ----------
    @property
    def selected_row(self) -> dict[str, Any] | None:
        """Método `BatchHistoryDialog.selected_row`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        i = self.table.currentRow()
        return self._rows[i] if 0 <= i < len(self._rows) else None

    def _refresh_labels(self, *_):
        """Método `BatchHistoryDialog._refresh_labels`.
            Parâmetros: `self`, `*_`."""
        row = self.selected_row
        total = len(self._rows)
        if row is None:
            self.lbl_summary.setText(f"{total} lotes.")
            self.lbl_row.setText("Nenhum lote selecionado.")
            self.btn_copy.setEnabled(False)
            self.btn_use.setEnabled(False)
            return
        self.lbl_summary.setText(f"{total} lotes.")
        self.lbl_row.setText(format_batch_row(row))
        self.btn_copy.setEnabled(True)
        self.btn_use.setEnabled(True)

    def _selected_seed(self) -> int | None:
        """Método `BatchHistoryDialog._selected_seed`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        row = self.selected_row
        if row is None:
            return None
        seed = row.get("seed")
        try:
            return int(seed)
        except (TypeError, ValueError):
            return None

    def _copy_seed(self):
        """Método `BatchHistoryDialog._copy_seed`.
            Parâmetros: `self`."""
        seed = self._selected_seed()
        if seed is None:
            return
        QGuiApplication.clipboard().setText(str(seed))

    def _use_seed(self):
        """Método `BatchHistoryDialog._use_seed`.
            Parâmetros: `self`."""
        seed = self._selected_seed()
        if seed is None:
            return
        self.useRequested.emit(seed)
        self.accept()
