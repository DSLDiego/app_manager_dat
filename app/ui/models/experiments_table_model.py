"""Model paginado: nunca carrega tudo na UI, mesmo com 1M experimentos."""

from __future__ import annotations

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt


class PagedExperimentsModel(QAbstractTableModel):
    """Classe `PagedExperimentsModel` do módulo."""
    def __init__(self, page_size: int = 200, parent=None):
        """Método `PagedExperimentsModel.__init__`.
            Parâmetros: `self`, `page_size`, `parent`."""
        super().__init__(parent)
        self._var_ids: list[int] = []
        self._matrix: list[list[float]] = []
        self._page = 0
        self._page_size = page_size

    def set_data(self, var_ids: list[int], matrix: list[list[float]]):
        """Método `PagedExperimentsModel.set_data`.
            Parâmetros: `self`, `var_ids`, `matrix`."""
        self.beginResetModel()
        self._var_ids = var_ids
        self._matrix = matrix
        self._page = 0
        self.endResetModel()

    def rowCount(self, parent=QModelIndex()):
        """Método `PagedExperimentsModel.rowCount`.
            Parâmetros: `self`, `parent`.
            Retorna o resultado calculado a partir do estado local."""
        n = len(self._matrix)
        return min(self._page_size, max(0, n - self._page * self._page_size))

    def columnCount(self, parent=QModelIndex()):
        """Método `PagedExperimentsModel.columnCount`.
            Parâmetros: `self`, `parent`.
            Retorna o resultado calculado a partir do estado local."""
        return len(self._var_ids) + 1

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        """Método `PagedExperimentsModel.headerData`.
            Parâmetros: `self`, `section`, `orientation`, `role`.
            Retorna o resultado calculado a partir do estado local."""
        if role != Qt.ItemDataRole.DisplayRole or orientation != Qt.Orientation.Horizontal:
            return None
        if section == 0:
            return "Experimento"
        return f"V{self._var_ids[section - 1]}"

    def data(self, index: QModelIndex, role=Qt.ItemDataRole.DisplayRole):
        """Método `PagedExperimentsModel.data`.
            Parâmetros: `self`, `index`, `role`.
            Retorna o resultado calculado a partir do estado local."""
        if not index.isValid() or role != Qt.ItemDataRole.DisplayRole:
            return None
        row = self._page * self._page_size + index.row()
        col = index.column()
        if col == 0:
            return row + 1
        try:
            return f"{self._matrix[row][col - 1]:.10g}"
        except (IndexError, TypeError):
            return ""

    def next_page(self):
        """Método `PagedExperimentsModel.next_page`.
            Parâmetros: `self`."""
        if (self._page + 1) * self._page_size < len(self._matrix):
            self.beginResetModel()
            self._page += 1
            self.endResetModel()

    def prev_page(self):
        """Método `PagedExperimentsModel.prev_page`.
            Parâmetros: `self`."""
        if self._page > 0:
            self.beginResetModel()
            self._page -= 1
            self.endResetModel()

    @property
    def current_page(self) -> int:
        """Método `PagedExperimentsModel.current_page`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        return self._page

    @property
    def total_pages(self) -> int:
        """Método `PagedExperimentsModel.total_pages`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        if not self._matrix:
            return 1
        return (len(self._matrix) + self._page_size - 1) // self._page_size
