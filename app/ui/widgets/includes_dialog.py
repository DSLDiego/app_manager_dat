"""R: navegação dos arquivos INCLUDE do template (leitura e variáveis)."""

from __future__ import annotations

from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QHeaderView,
    QLabel,
    QPlainTextEdit,
    QSplitter,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
)
from PySide6.QtCore import Qt

from app.core.includes import include_summary
from app.core.parsing import var_label


def status_text(entry: dict) -> str:
    """Função `status_text`.
        Parâmetros: `entry`.
        Retorna o resultado calculado a partir do estado local."""
    if entry.get("cycle"):
        return "ciclo"
    if not entry.get("exists"):
        return "ausente"
    if entry.get("error"):
        return "erro"
    return "ok"


def variables_text(entry: dict) -> str:
    """Função `variables_text`.
        Parâmetros: `entry`.
        Retorna o resultado calculado a partir do estado local."""
    labels = [var_label(v) for v in entry.get("variables") or []]
    named = [f"${n}" for n in entry.get("named_variables") or []]
    if not labels and not named:
        return "—"
    return ", ".join(labels + named)


def format_include_row(entry: dict) -> list[str]:
    """Colunas da tabela — puro, usado pelos testes."""
    return [
        str(entry.get("raw") or ""),
        str(entry.get("resolved") or ""),
        status_text(entry),
        str(entry.get("depth") or ""),
        variables_text(entry),
    ]


class IncludesDialog(QDialog):
    """Lista a árvore de INCLUDEs e mostra o conteúdo do arquivo selecionado."""

    def __init__(self, entries: list[dict], parent=None):
        """Método `IncludesDialog.__init__`.
            Parâmetros: `self`, `entries`, `parent`."""
        super().__init__(parent)
        self.entries = list(entries)
        self.setWindowTitle(
            f"INCLUDEs do template ({len(self.entries)}) — {include_summary(self.entries)}"
        )
        self.resize(900, 520)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(
            "Caminhos relativos são resolvidos pela pasta do template; "
            "absolutos (Windows/Linux) são usados como estão."
        ))

        self.table = QTableWidget(len(self.entries), 5, self)
        self.table.setHorizontalHeaderLabels(
            ["Arquivo (INCLUDE)", "Caminho resolvido", "Status", "Prof.", "Variáveis"]
        )
        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents
        )
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        for row, entry in enumerate(self.entries):
            for col, text in enumerate(format_include_row(entry)):
                self.table.setItem(row, col, QTableWidgetItem(text))
        self.table.itemSelectionChanged.connect(self._on_select)

        self.preview = QPlainTextEdit(self)
        self.preview.setReadOnly(True)
        self.preview.setPlaceholderText(
            "Selecione um INCLUDE para ver o conteúdo lido do arquivo."
        )
        self.preview.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)

        splitter = QSplitter(Qt.Orientation.Vertical, self)
        splitter.addWidget(self.table)
        splitter.addWidget(self.preview)
        splitter.setStretchFactor(0, 3)
        splitter.setStretchFactor(1, 2)
        layout.addWidget(splitter, 1)

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Close, parent=self)
        buttons.rejected.connect(self.reject)
        buttons.accepted.connect(self.accept)
        layout.addWidget(buttons)

        if self.entries:
            self.table.selectRow(0)
            self._on_select()

    def _on_select(self):
        """Método `IncludesDialog._on_select`.
            Parâmetros: `self`."""
        row = self.table.currentRow()
        if not (0 <= row < len(self.entries)):
            return
        entry = self.entries[row]
        if entry.get("text") is not None:
            self.preview.setPlainText(entry["text"])
        else:
            self.preview.setPlainText(
                f"[{status_text(entry)}] {entry.get('resolved')}\n"
                f"{entry.get('error') or 'conteúdo indisponível'}"
            )

    def selected_content(self) -> str:
        """Método `IncludesDialog.selected_content`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        return self.preview.toPlainText()
