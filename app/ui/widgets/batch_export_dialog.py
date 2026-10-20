"""Dialog: escolhe batch + versão do template + pasta de saída; inicia export."""

from __future__ import annotations

from pathlib import Path
from typing import List, Tuple

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QComboBox,
    QDialog,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)

from app.services.batch_export_service import BatchExportService


class BatchExportDialog(QDialog):
    """Classe `BatchExportDialog` do módulo."""
    exportRequested = Signal(str, int, str)  # batch_id, template_version_id, output_root

    def __init__(
        self,
        batches: List[str],
        template_versions: List[Tuple[int, str]],
        last_output_root: str | None = None,
        parent=None,
    ):
        """Método `BatchExportDialog.__init__`.
            Parâmetros: `self`, `batches`, `template_versions`, `last_output_root`, `parent`."""
        super().__init__(parent)
        self.setWindowTitle("Exportar Batch de Experimentos")
        layout = QVBoxLayout(self)

        row1 = QHBoxLayout()
        row1.addWidget(QLabel("Batch:"))
        self.combo_batch = QComboBox()
        self.combo_batch.addItems(batches)
        row1.addWidget(self.combo_batch)
        layout.addLayout(row1)

        row2 = QHBoxLayout()
        row2.addWidget(QLabel("Versão do template:"))
        self.combo_version = QComboBox()
        for version_id, label in template_versions:
            self.combo_version.addItem(label, version_id)
        row2.addWidget(self.combo_version)
        layout.addLayout(row2)

        row3 = QHBoxLayout()
        row3.addWidget(QLabel("Saída:"))
        self.input_dir = QLineEdit(last_output_root or str(Path.cwd() / "output"))
        btn_browse = QPushButton("Procurar…")
        btn_browse.clicked.connect(self._browse)
        row3.addWidget(self.input_dir)
        row3.addWidget(btn_browse)
        layout.addLayout(row3)

        btn_go = QPushButton("Exportar")
        btn_go.setDefault(True)
        btn_go.clicked.connect(self._emit)
        layout.addWidget(btn_go)

    def _browse(self):
        """Método `BatchExportDialog._browse`.
            Parâmetros: `self`."""
        directory = QFileDialog.getExistingDirectory(self, "Pasta de saída")
        if directory:
            self.input_dir.setText(directory)

    def _emit(self):
        """Método `BatchExportDialog._emit`.
            Parâmetros: `self`."""
        version_id = self.combo_version.currentData()
        if not self.combo_batch.currentText() or version_id is None:
            return
        self.exportRequested.emit(
            self.combo_batch.currentText(),
            int(version_id),
            self.input_dir.text(),
        )
        self.accept()
