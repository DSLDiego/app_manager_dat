"""Lista de arquivos em edição (estilo Notepad++): dock sincronizado com as abas.

Mostra: ordem, título da aba, marcador ● quando há alteração não salva e
hachura antes de salvar (ItemMarker). Clique simples ativa a aba.
"""

from __future__ import annotations

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QHBoxLayout,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

DIRTY_MARK = "●"


class FilesListPanel(QWidget):
    """Painel-clique: ativa a aba; só emite, não carrega nada pesado."""

    fileActivated = Signal(int)      # index da aba
    closeRequested = Signal(int)     # index da aba (fechar arquivo)
    statusMessage = Signal(str)
    diffRequested = Signal()         # abrir diff de arquivos (r16)

    def __init__(self, editor_tabs, parent=None):
        """Método `FilesListPanel.__init__`.
            Parâmetros: `self`, `editor_tabs`, `parent`."""
        super().__init__(parent)
        self.editor_tabs = editor_tabs

        layout = QVBoxLayout(self)
        layout.setContentsMargins(6, 3, 6, 3)
        layout.setSpacing(2)

        self.list = QListWidget()
        self.list.setToolTip("Arquivos em edição — clique para ativar a aba.")
        self.list.itemClicked.connect(self._on_item_clicked)
        layout.addWidget(self.list, 1)

        bar = QHBoxLayout()
        self.btn_activate = QPushButton("Ativar")
        self.btn_activate.setToolTip("Ativa a aba selecionada na lista.")
        self.btn_close_file = QPushButton("Fechar arquivo")
        self.btn_close_file.setToolTip("Fecha a aba selecionada (confirma se houver mudanças).")
        bar.addWidget(self.btn_activate)
        bar.addWidget(self.btn_close_file)
        self.btn_diff = QPushButton("Diff…")
        self.btn_diff.setToolTip("Compara 2 arquivos (abas abertas ou do disco) lado a lado.")
        bar.addWidget(self.btn_diff)
        bar.addStretch()
        layout.addLayout(bar)

        self.btn_activate.clicked.connect(self._on_activate)
        self.btn_close_file.clicked.connect(self._on_close_file)
        self.btn_diff.clicked.connect(self.diffRequested.emit)

        # sincronia com as abas existentes
        self.editor_tabs.currentChanged.connect(lambda _i: self.refresh())
        self.editor_tabs.tab_dirty_changed.connect(lambda *_: self.refresh())
        if hasattr(self.editor_tabs, "tabsChanged"):
            self.editor_tabs.tabsChanged.connect(lambda: self.refresh())
        self.refresh()

    # ---------- sincronia ----------
    def refresh(self):
        """Método `FilesListPanel.refresh`.
            Parâmetros: `self`."""
        self.list.blockSignals(True)
        self.list.clear()
        tabs = self.editor_tabs
        for i in range(tabs.count()):
            widget = tabs.widget(i)
            title = tabs.tabText(i).strip()
            if hasattr(widget, "is_modified") and widget.is_modified():
                title = f"{title} {DIRTY_MARK}"
            item = QListWidgetItem(title)
            if widget is not None and getattr(widget, "file_path", ""):
                item.setToolTip(str(widget.file_path))
            else:
                item.setToolTip("(sem arquivo no disco)")
            self.list.addItem(item)
        current = tabs.currentIndex()
        if 0 <= current < self.list.count():
            self.list.setCurrentRow(current)
        self.list.blockSignals(False)

    # ---------- ações ----------
    def _on_item_clicked(self, item: QListWidgetItem):
        """Método `FilesListPanel._on_item_clicked`.
            Parâmetros: `self`, `item`."""
        row = self.list.row(item)
        self.fileActivated.emit(row)

    def _on_activate(self):
        """Método `FilesListPanel._on_activate`.
            Parâmetros: `self`."""
        row = self.list.currentRow()
        if row >= 0:
            self.editor_tabs.setCurrentIndex(row)
            self.statusMessage.emit(f"Aba {row + 1} ativada.")

    def _on_close_file(self):
        """Método `FilesListPanel._on_close_file`.
            Parâmetros: `self`."""
        row = self.list.currentRow()
        if row >= 0:
            self.closeRequested.emit(row)
