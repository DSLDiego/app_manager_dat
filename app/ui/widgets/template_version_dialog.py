"""Dialog de versionamento de templates: lista, diff, restore."""

from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QDialog,
    QHBoxLayout,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QPlainTextEdit,
    QVBoxLayout,
)

from app.services.template_service import TemplateService


class TemplateVersionDialog(QDialog):
    """Classe `TemplateVersionDialog` do módulo."""
    restoreRequested = Signal(int)  # version_id

    def __init__(self, template_service: TemplateService, template_id: int, parent=None):
        """Método `TemplateVersionDialog.__init__`.
            Parâmetros: `self`, `template_service`, `template_id`, `parent`."""
        super().__init__(parent)
        self.setWindowTitle("Histórico de Versões")
        self.service = template_service
        self.template_id = template_id

        layout = QVBoxLayout(self)
        self.list = QListWidget()
        self.refresh_list()
        layout.addWidget(self.list)

        self.diff_view = QPlainTextEdit()
        self.diff_view.setReadOnly(True)
        layout.addWidget(self.diff_view)

        bar = QHBoxLayout()
        btn_diff = QPushButton("Ver Diff (selecione 2)")
        btn_restore = QPushButton("Restaurar selecionada")
        btn_diff.clicked.connect(self._show_diff)
        btn_restore.clicked.connect(self._restore)
        bar.addWidget(btn_diff)
        bar.addWidget(btn_restore)
        bar.addStretch()
        layout.addLayout(bar)

        self.list.itemDoubleClicked.connect(lambda _item: self._restore())

    def refresh_list(self):
        """Método `TemplateVersionDialog.refresh_list`.
            Parâmetros: `self`."""
        self.list.clear()
        versions = self.service.repo.list_versions(self.template_id)
        for v in versions:
            label = (
                f"v{v['version_number']} — {v['created_at']} — "
                f"{v['comment'] or 'sem comentário'} ({v['user']})"
            )
            item = QListWidgetItem(label)
            item.setData(256, v["id"])  # Qt.UserRole custom
            item.setData(257, v["version_number"])
            self.list.addItem(item)

    def _selected_versions(self):
        """Método `TemplateVersionDialog._selected_versions`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        return [
            self.list.item(index)
            for index in self.list.selectedIndexes()
        ]

    def _show_diff(self):
        """Método `TemplateVersionDialog._show_diff`.
            Parâmetros: `self`."""
        selected = self._selected_versions()
        if len(selected) != 2:
            self.diff_view.setPlainText("Selecione exatamente 2 versões.")
            return
        v1 = selected[0].data(256)
        v2 = selected[1].data(256)
        self.diff_view.setPlainText(self.service.diff(v1, v2))

    def _restore(self):
        """Método `TemplateVersionDialog._restore`.
            Parâmetros: `self`."""
        selected = self.list.selectedIndexes()
        if not selected:
            return
        item = self.list.item(selected[-1])
        version_id = item.data(256)
        self.service.restore(self.template_id, version_id)
        self.refresh_list()
        self.restoreRequested.emit(version_id)
