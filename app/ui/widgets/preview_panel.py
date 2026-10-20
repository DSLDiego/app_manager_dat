"""Preview: textarea + sample 1 exp + diff, sem bloquear a UI."""

from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QHBoxLayout,
    QPlainTextEdit,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class PreviewPanel(QWidget):
    """Classe `PreviewPanel` do módulo."""
    previewRequested = Signal(int)  # seed
    sideDiffRequested = Signal(int, int)  # seeds A, B (T5436)
    seedsBatchRequested = Signal(int)  # nº de seeds (T5437)

    def __init__(self, parent=None):
        """Método `PreviewPanel.__init__`.
            Parâmetros: `self`, `parent`."""
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(6, 3, 6, 3)
        layout.setSpacing(2)

        bar = QHBoxLayout()
        self.spin_seed = QSpinBox()
        self.spin_seed.setRange(-999999, 999999)
        self.spin_seed.setValue(42)
        self.btn_preview = QPushButton("Gerar Preview")
        bar.addWidget(self.spin_seed)
        bar.addWidget(self.btn_preview)

        self.spin_seed_b = QSpinBox()
        self.spin_seed_b.setRange(-999999, 999999)
        self.spin_seed_b.setValue(43)
        self.btn_side_diff = QPushButton("Diff lado a lado")
        self.btn_side_diff.setToolTip(
            "T5436: renderiza duas seeds e mostra as variações com marcação."
        )
        bar.addWidget(self.spin_seed_b)
        bar.addWidget(self.btn_side_diff)

        self.btn_seeds_batch = QPushButton("Seeds em lote")
        self.btn_seeds_batch.setToolTip(
            "T5437: gera o preview para N seeds consecutivas e resume as diferenças."
        )
        bar.addWidget(self.btn_seeds_batch)
        bar.addStretch()
        layout.addLayout(bar)

        self.output = QPlainTextEdit()
        self.output.setReadOnly(True)
        self.output.setFont(QFont("Consolas"))
        layout.addWidget(self.output)

        self.btn_preview.clicked.connect(
            lambda: self.previewRequested.emit(self.spin_seed.value())
        )
        self.btn_side_diff.clicked.connect(
            lambda: self.sideDiffRequested.emit(
                self.spin_seed.value(), self.spin_seed_b.value()
            )
        )
        self.btn_seeds_batch.clicked.connect(
            lambda: self.seedsBatchRequested.emit(self.spin_seed.value())
        )

    def show_text(self, text: str):
        """Método `PreviewPanel.show_text`.
            Parâmetros: `self`, `text`."""
        self.output.setPlainText(text)

    def show_side_by_side(self, text_a: str, text_b: str, seed_a: int, seed_b: int):
        """T5436: mostra as duas versões lado a lado com marcação de divergência."""
        from app.services.comparison_round34 import count_differences, format_side_by_side

        rendered = format_side_by_side(text_a, text_b, width=46)
        n = count_differences(text_a, text_b)
        header = (
            f"Comparando seed {seed_a} ← seed {seed_b}: "
            f"{n} linha(s) divergente(s) (» = diferente)\n\n"
        )
        self.output.setPlainText(header + rendered)
