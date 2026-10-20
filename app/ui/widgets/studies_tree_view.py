"""Lista de listas: estudos → versões (árvore com 2 níveis).

Puro em study_tree(); UI: QTreeWidget com sub-itens de versões.
"""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTreeWidget, QTreeWidgetItem


def study_tree(studies: list, versions_by_study: dict[int, list]) -> list[list]:
    """Lista de listas: [study_label, [version_label, …]] — puro.

    studies: [{id, name, meta…}]; versions_by_study: {study_id: [v…]}.
    Sem versões ⇒ sub-lista ["v (nenhuma)"].
    """
    rows: list[list] = []
    for study in studies:
        sid = int(study.get("id", 0))
        name = str(study.get("name", f"estudo {sid}"))
        meta = study.get("meta") or {}
        batch = meta.get("batch_id", "—")
        versions = [str(v) for v in (versions_by_study.get(sid) or [])]
        if not versions:
            versions = ["(nenhuma versão)"]
        rows.append([f"#{sid} — {name} · batch={batch}", versions])
    return rows


class StudiesTreeView(QTreeWidget):
    """Árvore estudos → versões (formato lista de listas do diálogo de estudos)."""

    def __init__(self, parent=None):
        """Método `StudiesTreeView.__init__`.
            Parâmetros: `self`, `parent`."""
        super().__init__(parent)
        self.setHeaderLabels(["Estudo · batch", "Versões"])
        self.setAlternatingRowColors(True)
        self.setToolTip("Clique num estudo para selecioná-lo — versões aninhadas embaixo.")

    def populate(self, studies: list, versions_by_study: dict[int, list]) -> int:
        """Monta árvore — retorna nº de estudos."""
        self.clear()
        n = 0
        for study_label, versions in study_tree(studies, versions_by_study):
            top = QTreeWidgetItem([study_label, str(len(versions))])
            top.setData(0, Qt.ItemDataRole.UserRole, True)  # é estudo
            for v in versions:
                child = QTreeWidgetItem([v, ""])
                top.addChild(child)
            self.addTopLevelItem(top)
            top.setExpanded(True)
            n += 1
        return n

    def selected_study_row(self) -> int | None:
        """Índice do estudo selecionado na árvore (None se numa versão)."""
        item = self.currentItem()
        if item is None:
            return None
        if not item.data(0, Qt.ItemDataRole.UserRole):
            item = item.parent()
        if item is None:
            return None
        row = self.indexOfTopLevelItem(item)
        return row if row >= 0 else None
