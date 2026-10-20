"""Model que lê páginas do SQLite. Memória O(page_size), não O(N)."""

from __future__ import annotations

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt

from app.core.parsing import var_label
from app.infrastructure.experiment_repository import ExperimentRepository


class RepositoryPagedModel(QAbstractTableModel):
    """Classe `RepositoryPagedModel` do módulo."""
    def __init__(
        self,
        repo: ExperimentRepository,
        page_size: int = 200,
        parent=None,
    ):
        """Método `RepositoryPagedModel.__init__`.
            Parâmetros: `self`, `repo`, `page_size`, `parent`."""
        super().__init__(parent)
        self.repo = repo
        self.page_size = page_size
        self._page = 0
        self._var_filter: int | None = None
        self._batch_filter: str | None = None
        self._var_ids: list[int] = []
        self._rows: list[dict] = []
        self._total = 0
        self._reload()

    def _reload(self):
        """Método `RepositoryPagedModel._reload`.
            Parâmetros: `self`."""
        self.beginResetModel()
        all_var_ids = self.repo.var_ids(batch_id=self._batch_filter)
        if self._var_filter is not None:
            self._shown_var_ids = [v for v in all_var_ids if v == self._var_filter]
        else:
            self._shown_var_ids = all_var_ids
        self._rows = self.repo.fetch_page(
            self._page, self.page_size, self._shown_var_ids, batch_id=self._batch_filter
        )
        self._total = self.repo.count(batch_id=self._batch_filter)
        self.endResetModel()

    def set_var_filter(self, var_id: int | None):
        """Filtra a tabela para UMA variável (None = todas)."""
        self._var_filter = var_id
        self._page = 0
        self._reload()

    def set_batch_filter(self, batch_id: str | None):
        """Filtra a tabela para UM lote de amostragem (None = todos)."""
        self._batch_filter = batch_id
        self._page = 0
        self._reload()

    @property
    def batch_filter(self) -> str | None:
        """Método `RepositoryPagedModel.batch_filter`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        return self._batch_filter

    @property
    def var_filter(self) -> int | None:
        """Método `RepositoryPagedModel.var_filter`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        return self._var_filter

    @property
    def shown_var_ids(self) -> list[int]:
        """Método `RepositoryPagedModel.shown_var_ids`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        return list(self._shown_var_ids)

    def rowCount(self, parent=QModelIndex()):
        """Método `RepositoryPagedModel.rowCount`.
            Parâmetros: `self`, `parent`.
            Retorna o resultado calculado a partir do estado local."""
        return len(self._rows)

    def columnCount(self, parent=QModelIndex()):
        """Método `RepositoryPagedModel.columnCount`.
            Parâmetros: `self`, `parent`.
            Retorna o resultado calculado a partir do estado local."""
        return len(self._shown_var_ids) + 1

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        """Método `RepositoryPagedModel.headerData`.
            Parâmetros: `self`, `section`, `orientation`, `role`.
            Retorna o resultado calculado a partir do estado local."""
        if role != Qt.ItemDataRole.DisplayRole or orientation != Qt.Orientation.Horizontal:
            return None
        if section == 0:
            return "Experimento"
        return var_label(self._shown_var_ids[section - 1])

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        """Método `RepositoryPagedModel.data`.
            Parâmetros: `self`, `index`, `role`.
            Retorna o resultado calculado a partir do estado local."""
        if not index.isValid() or role != Qt.ItemDataRole.DisplayRole:
            return None
        row = self._rows[index.row()]
        col = index.column()
        if col == 0:
            return row["external_id"]
        var_id = self._shown_var_ids[col - 1]
        value = row["values"].get(var_id)
        return f"{value:.10g}" if value is not None else ""

    def next_page(self):
        """Método `RepositoryPagedModel.next_page`.
            Parâmetros: `self`."""
        if (self._page + 1) * self.page_size < self._total:
            self._page += 1
            self._reload()

    def prev_page(self):
        """Método `RepositoryPagedModel.prev_page`.
            Parâmetros: `self`."""
        if self._page > 0:
            self._page -= 1
            self._reload()

    def refresh(self):
        """Método `RepositoryPagedModel.refresh`."""
        self._reload()

    @property
    def current_page(self) -> int:
        """Método `RepositoryPagedModel.current_page`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        return self._page

    @property
    def total_pages(self) -> int:
        """Método `RepositoryPagedModel.total_pages`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        if self._total == 0:
            return 1
        return (self._total + self.page_size - 1) // self.page_size

    @property
    def total_rows(self) -> int:
        """Método `RepositoryPagedModel.total_rows`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        return self._total

    @property
    def page_rows(self) -> list[dict]:
        """(external_id, values) da página atual — usado pelo formato 'Cartões'."""
        return list(self._rows)
