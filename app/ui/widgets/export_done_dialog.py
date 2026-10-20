"""Dialog de sucesso do export: caminho da pasta de destino clicável."""

from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import (
    QDialog,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
)


class ExportDoneDialog(QDialog):
    """Mostra onde os .dats foram gravados e abre a pasta no Explorer."""

    def __init__(self, output_dir, n_files: int, manifest_path=None, parent=None):
        """Método `ExportDoneDialog.__init__`.
            Parâmetros: `self`, `output_dir`, `n_files`, `manifest_path`, `parent`."""
        super().__init__(parent)
        self.setWindowTitle("Exportação concluída")
        self.setMinimumSize(560, 240)

        self.output_dir = Path(output_dir) if not isinstance(output_dir, Path) else output_dir
        self.manifest_path = (
            Path(manifest_path) if manifest_path is not None
            else self.output_dir / "manifest.csv"
        )

        layout = QVBoxLayout(self)

        header = QLabel("✅ Os arquivos .dat foram gerados com sucesso.")
        layout.addWidget(header)

        n_label = QLabel(f"Arquivos gerados: {n_files}")
        layout.addWidget(n_label)

        destino = QLabel(f"<b>Pasta de destino:</b><br>{self.output_dir}")
        destino.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        destino.setWordWrap(True)
        layout.addWidget(destino)

        layout.addSpacing(8)

        buttons = QHBoxLayout()
        btn_open = QPushButton("📂 Abrir no Explorer")
        btn_open.setDefault(True)
        btn_manifest = QPushButton("Abrir manifest.csv")
        btn_close = QPushButton("Fechar")
        buttons.addWidget(btn_open)
        buttons.addWidget(btn_manifest)
        buttons.addStretch()
        buttons.addWidget(btn_close)
        layout.addLayout(buttons)

        btn_open.clicked.connect(self._open_folder)
        btn_manifest.clicked.connect(self._open_manifest)
        btn_close.clicked.connect(self.accept)

    def _open_folder(self) -> None:
        """Método `ExportDoneDialog._open_folder`.
            Parâmetros: `self`."""
        self.output_dir.mkdir(parents=True, exist_ok=True)
        QDesktopServices.openUrl(QUrl.fromLocalFile(str(self.output_dir)))

    def _open_manifest(self) -> None:
        """Método `ExportDoneDialog._open_manifest`.
            Parâmetros: `self`."""
        if self.manifest_path.exists():
            QDesktopServices.openUrl(QUrl.fromLocalFile(str(self.manifest_path)))
