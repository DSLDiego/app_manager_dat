"""Painel de variáveis: lista tokens detectados + botão para editar distribuição."""

from __future__ import annotations

from typing import Dict, List, Optional

from PySide6.QtCore import QMimeData, Qt, Signal
from PySide6.QtGui import QColor, QCursor
from PySide6.QtWidgets import (
    QAbstractItemView,
    QHeaderView,
    QHBoxLayout,
    QMenu,
    QMessageBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from app.core.parsing import find_variables, var_label
from app.domain.entities import DistributionSpec
from app.infrastructure.distribution_registry import DistributionRegistry
from app.services import spec_bulk_service
from app.ui.widgets.distribution_dialog import DistributionDialog


def reassign_spec(specs: Dict[int, object], src_var: int, dst_var: int) -> Dict[int, object]:
    """T5435 (puro): copia a distribuição de `src_var` para `dst_var`.
    Retorna novo dict (não muta o original); inválido → dict intacto."""
    src = specs.get(int(src_var))
    if src is None or src_var == dst_var:
        return specs
    out = dict(specs)
    out[int(dst_var)] = src
    return out


class VariablesTableWidget(QTableWidget):
    """Tabela de variáveis com 2 colunas: Variável e Arquivo.
    Ao soltar, copia a distribuição da linha de origem para a de destino.
    """

    MIME_KIND = "application/x-dtengine-varspec"

    def __init__(self, panel: "VariablesPanel", parent=None):
        super().__init__(2, 0, parent)  # 2 colunas, 0 linhas iniciais
        self._panel = panel
        self.setColumnCount(2)
        self.setHorizontalHeaderLabels(["Variável", "Arquivo"])
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.horizontalHeader().setStretchLastSection(True)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.setDefaultDropAction(Qt.DropAction.CopyAction)
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

    def clear(self) -> None:
        """Método `VariablesTableWidget.clear`.
            Parâmetros: `self`."""
        self.setRowCount(0)

    def count(self) -> int:
        """Método `VariablesTableWidget.count`.
            Parâmetros: `self`.
            Retorna o número de linhas na tabela."""
        return self.rowCount()

    def add_item(self, var_id: int, label: str, source: str | None) -> None:
        """Método `VariablesTableWidget.add_item`.
            Parâmetros: `self`, `var_id`, `label`, `source`."""
        row = self.rowCount()
        self.insertRow(row)
        # Coluna 0: Variável
        var_item = QTableWidgetItem(label)
        var_item.setData(Qt.ItemDataRole.UserRole, var_id)
        var_item.setForeground(QColor("#27ae60") if self._panel.specs.get(var_id) else QColor("#c0392b"))
        self.setItem(row, 0, var_item)
        # Coluna 1: Arquivo
        source_text = source or "-"
        source_item = QTableWidgetItem(source_text)
        source_item.setData(Qt.ItemDataRole.UserRole, var_id)
        self.setItem(row, 1, source_item)

    def current_var_id(self) -> int | None:
        """Método `VariablesTableWidget.current_var_id`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        current_row = self.currentRow()
        if current_row < 0:
            return None
        item = self.item(current_row, 0)
        if item is None:
            return None
        return item.data(Qt.ItemDataRole.UserRole)

    def current_var_label(self) -> str | None:
        """Método `VariablesTableWidget.current_var_label`.
            Parâmetros: `self`."""
        current_row = self.currentRow()
        if current_row < 0:
            return None
        item = self.item(current_row, 0)
        if item is None:
            return None
        return item.text()

    def current_source(self) -> str | None:
        """Método `VariablesTableWidget.current_source`.
            Parâmetros: `self`."""
        current_row = self.currentRow()
        if current_row < 0:
            return None
        item = self.item(current_row, 1)
        if item is None:
            return None
        return item.data(Qt.ItemDataRole.UserRole)

    def startDrag(self, actions):  # noqa: N802 (override Qt)
        item = self.currentItem()
        if item is None:
            return
        # Drag da linha inteira - usa a coluna 0 (Variável)
        var_id_item = item(self.currentRow(), 0)
        if var_id_item is None:
            return
        var_id = int(var_id_item.data(Qt.ItemDataRole.UserRole))
        drag = QDrag(self)
        mime = QMimeData()
        mime.setData(self.MIME_KIND, str(var_id).encode())
        drag.setMimeData(mime)
        drag.exec(actions)

    def dragEnterEvent(self, event):  # noqa: N802
        if event.source() is self and event.mimeData().hasFormat(self.MIME_KIND):
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self, event):  # noqa: N802
        event.acceptProposedAction() if event.mimeData().hasFormat(self.MIME_KIND) else event.ignore()

    def dropEvent(self, event):  # noqa: N802
        if not event.mimeData().hasFormat(self.MIME_KIND):
            event.ignore()
            return
        row = self.currentRow()
        if row < 0:
            event.ignore()
            return
        src_var = int(bytes(event.mimeData().data(self.MIME_KIND)).decode())
        dst_var = int(item(row, 0).data(Qt.ItemDataRole.UserRole))
        self._panel.copy_distribution(src_var, dst_var)
        event.acceptProposedAction()


class VariablesPanel(QWidget):
    """Sem dependência de scipy/SQL. Emite sinais para o Main Window."""

    variables_changed = Signal(object)   # dict[int, DistributionSpec]
    sampleRequested = Signal(object)     # dict[int, DistributionSpec]
    reloadDatRequested = Signal()        # re-ler .dat do disco (novas variáveis)

    def __init__(self, registry: DistributionRegistry, parent=None, exp_repo=None):
        """Método `VariablesPanel.__init__`.
            Parâmetros: `self`, `registry`, `parent`, `exp_repo`."""
        super().__init__(parent)
        self.registry = registry
        self.exp_repo = exp_repo
        self.var_map: Dict[int, object] = {}
        self.specs: Dict[int, object] = {}
        self._sample_count = 10

        layout = QVBoxLayout(self)
        layout.setContentsMargins(6, 3, 6, 3)
        layout.setSpacing(2)
        self.list_widget = VariablesTableWidget(self)
        self.list_widget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.list_widget.customContextMenuRequested.connect(self._show_menu)
        self.list_widget.itemDoubleClicked.connect(self._edit_current)
        layout.addWidget(self.list_widget)

        bar = QHBoxLayout()
        self.btn_edit = QPushButton("Definir Distribuição…")
        self.btn_bulk = QPushButton("Distribuições em lote…")
        self.btn_bulk.setToolTip("Janela secundária: mesma distribuição para todas ou para as selecionadas.")
        self.btn_reload_dat = QPushButton("Re-ler .dat")
        self.btn_reload_dat.setToolTip("Recarrega o .dat do disco e atualiza as variáveis (novos tokens).")
        self.btn_sample = QPushButton(f"Amostrar ({self._sample_count})")
        bar.addWidget(self.btn_edit)
        bar.addWidget(self.btn_bulk)
        bar.addWidget(self.btn_reload_dat)
        bar.addWidget(self.btn_sample)
        layout.addLayout(bar)

        self.btn_edit.clicked.connect(self._edit_current)
        self.btn_bulk.clicked.connect(self._open_bulk_dialog)
        self.btn_reload_dat.clicked.connect(self.reloadDatRequested.emit)
        self.btn_sample.clicked.connect(
            lambda: self.sampleRequested.emit(self.specs or {})
        )
        self._persist_sample_count()

    # ---------- contagem mínima de amostras ----------
    def _persist_sample_count(self) -> None:
        """Método `VariablesPanel._persist_sample_count`.
            Parâmetros: `self`."""
        from PySide6.QtCore import QSettings

        settings = QSettings("datstudio", "dtengine")
        try:
            saved = int(settings.value("sampling/min_count", self._sample_count))
        except (TypeError, ValueError):
            saved = self._sample_count
        self.set_sample_count(max(1, saved))

    def set_sample_count(self, count: int) -> None:
        """Método `VariablesPanel.set_sample_count`.
            Parâmetros: `self`, `count`."""
        from PySide6.QtCore import QSettings

        self._sample_count = max(1, int(count))
        self.btn_sample.setText(f"Amostrar ({self._sample_count})")
        QSettings("datstudio", "dtengine").setValue(
            "sampling/min_count", self._sample_count
        )

    def cycle_sample_count(self) -> None:
        """Método `VariablesPanel.cycle_sample_count`.
            Parâmetros: `self`."""
        for option in (10, 100, 1000, 10):
            if option > self._sample_count:
                self.set_sample_count(option)
                return
        self.set_sample_count(10)

    def _show_scipy_helper(self, *_):
        """Método `VariablesPanel._show_scipy_helper`.
            Parâmetros: `self`, `*_`."""
        from PySide6.QtWidgets import QMessageBox

        item = self.list_widget.currentItem()
        var_id = item.data(Qt.ItemDataRole.UserRole) if item else None
        spec = self.specs.get(var_id) if var_id is not None else None
        provider_name = spec.provider if spec else "scipy"
        provider = self.registry.get(provider_name)
        if provider is None:
            QMessageBox.information(
                self, "Helper SciPy", "Provider não encontrado."
            )
            return
        dists = provider.list_distributions()
        sample = ", ".join(dists[:25]) + ("…" if len(dists) > 25 else "")
        QMessageBox.information(
            self,
            f"Helper de {provider_name}",
            f"Distribuições disponíveis ({len(dists)}):\n{sample}",
        )

    # ---------- tokens ----------
    def update_tokens(self, var_sources: dict | str | None = None) -> None:
        """Método `VariablesPanel.update_tokens`.
            Parâmetros: `self`, `var_sources`.
            `var_sources` pode ser:
            - Um dicionário retornado por `MainWindow._collect_variables_with_sources` (modo rastreado).
            - Um texto string com tokens $N/$varN (modo compatível).
            - None ou vazio (modo compatível sem texto).
            Retorna o resultado calculado a partir do estado local."""
        # Modo compatível: texto vazio ou None - preserva cache e retorna var_map
        if var_sources is None or var_sources == "":
            return self.var_map if hasattr(self, "var_map") and self.var_map else None
        # Populate var_map with variable IDs from the text
        from app.core.parsing import find_variables
        if isinstance(var_sources, str):
            # Modo compatível: texto string passado diretamente
            self.list_widget.clear()
            var_ids = find_variables(var_sources)
            for var_id in sorted(var_ids):
                label = var_label(var_id)
                disp_label = f"{label}"
                spec = self.specs.get(var_id)
                if spec:
                    color = QColor("#27ae60")
                else:
                    color = QColor("#c0392b")
                self.list_widget.add_item(var_id, disp_label, "-")
            # Set var_map as sorted list of all variable IDs found
            self.var_map = sorted(var_ids)
        elif isinstance(var_sources, dict):
            # Modo rastreado: dicionário com rastreamento de origem
            for var_id in sorted(var_sources):
                info = var_sources[var_id]
                label = info.get("label", var_label(var_id))
                source = info.get("source", "main")
                # Monta label com origem
                if source == "main":
                    disp_label = f"{label}  →  (main)"
                else:
                    disp_label = f"{label}  →  {source}"
                spec = self.specs.get(var_id)
                if spec:
                    color = QColor("#27ae60")
                else:
                    color = QColor("#c0392b")
                self.list_widget.add_item(var_id, disp_label, source)
            # Set var_map as list of var_ids from var_sources
            # IMPORTANT: Keep existing var_map entries and only add new ones
            existing = set(self.var_map) if hasattr(self, "var_map") and self.var_map else set()
            new_map = set(var_sources.keys())
            self.var_map = sorted(existing | new_map)

        # Return var_ids for string/compat mode, or None for dict mode
        if isinstance(var_sources, str):
            return self.var_map
        return None

    def _edit_current(self, *_):
        """Método `VariablesPanel._edit_current`.
            Parâmetros: `self`, `*_`."""
        var_id = self.list_widget.current_var_id()
        if var_id is not None:
            self.edit_variable(int(var_id))

    def edit_variable(self, var_id: int):
        """Método `VariablesPanel.edit_variable`.
            Parâmetros: `self`, `var_id`."""
        dialog = DistributionDialog(self.registry, var_id, self.specs.get(var_id), self)
        if dialog.exec() == DistributionDialog.DialogCode.Accepted:
            self.specs[var_id] = dialog.collect()
            self.update_tokens("")

    # ---------- aplicar em lote (1.1 / 1.2) ----------
    def _open_bulk_dialog(self):
        """Método `VariablesPanel._open_bulk_dialog`.
            Parâmetros: `self`."""
        from app.ui.widgets.distribution_bulk_dialog import DistributionBulkDialog

        if not self.var_map:
            QMessageBox.information(
                self, "Sem variáveis",
                "Abra um template com tokens $varN antes de usar o lote.",
            )
            return
        dialog = DistributionBulkDialog(self.registry, sorted(self.var_map), self.specs, self)
        dialog.specsChanged.connect(self._apply_specs_map)
        dialog.exec()

    def _apply_specs_map(self, specs: dict):
        """Método `VariablesPanel._apply_specs_map`.
            Parâmetros: `self`, `specs`."""
        self.specs = dict(specs or {})
        self.update_tokens("")
        self.variables_changed.emit(self.specs)

    def apply_current_to_all(self):
        """Menu de contexto: mesma distribuição da variável selecionada para TODAS."""
        var_id = self.list_widget.current_var_id()
        if var_id is None:
            return False
        spec = self.specs.get(int(var_id))
        if spec is None:
            QMessageBox.information(
                self, "Sem distribuição",
                "Defina a distribuição da variável selecionada antes de replicá-la.",
            )
            return False
        self.specs = spec_bulk_service.apply_spec_to_all(self.specs, sorted(self.var_map), spec)
        self.update_tokens("")
        self.variables_changed.emit(self.specs)
        return True

    def clear_all_specs(self):
        """Método `VariablesPanel.clear_all_specs`.
            Parâmetros: `self`."""
        self.specs = spec_bulk_service.clear_specs(self.specs)
        self.update_tokens("")
        self.variables_changed.emit(self.specs)

    def missing_count(self) -> int:
        """Método `VariablesPanel.missing_count`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        return len(spec_bulk_service.missing_of(list(self.var_map), self.specs))

    def _plot_current(self, *_):
        """Método `VariablesPanel._plot_current`.
            Parâmetros: `self`, `*_`."""
        var_id = self.list_widget.current_var_id()
        if var_id is None:
            return

        from app.ui.widgets.distribution_plot_dialog import DistributionPlotDialog

        dialog = DistributionPlotDialog(self.registry, self, exp_repo=self.exp_repo)
        dialog.setWindowTitle(f"Gráficos — {var_label(var_id) if var_id is not None else 'distribuição'}")
        dialog.exec()

    def copy_distribution(self, src_var: int, dst_var: int) -> bool:
        """T5435: copia a distribuição de `src_var` para `dst_var` (drag&drop).
        Emite variables_changed. True se algo mudou."""
        new_specs = reassign_spec(self.specs, src_var, dst_var)
        if new_specs is self.specs:
            return False
        self.specs = new_specs
        self.update_tokens()
        return True

    def _show_menu(self, pos):
        """Método `VariablesPanel._show_menu`.
            Parâmetros: `self`, `pos`."""
        from PySide6.QtGui import QAction

        menu = QMenu(self)
        act_min = QAction(f"Amostras mínimas: {self._sample_count} (clique p/ alternar)", self)
        current_spec = None
        var_id = self.list_widget.current_var_id()
        if var_id is not None:
            current_spec = self.specs.get(int(var_id))
        label = (
            f"Aplicar '{current_spec.provider}.{current_spec.name}' para TODAS as variáveis"
            if current_spec is not None
            else "Aplicar para todas (defina a distribuição primeiro)"
        )
        act_apply_all = QAction(label, self)
        act_apply_all.setEnabled(current_spec is not None)
        act_bulk = QAction("Definir distribuições em lote…", self)
        act_clear = QAction("Limpar todas as distribuições", self)
        act_helper = QAction("Abrir helper SciPy…", self)
        act_plot = QAction("Plotar distribuição / f(x)…", self)
        act_min.triggered.connect(self.cycle_sample_count)
        act_apply_all.triggered.connect(self.apply_current_to_all)
        act_bulk.triggered.connect(self._open_bulk_dialog)
        act_clear.triggered.connect(self.clear_all_specs)
        act_helper.triggered.connect(self._show_scipy_helper)
        act_plot.triggered.connect(self._plot_current)
        menu.addActions([act_min, act_apply_all])
        menu.addAction(act_bulk)
        menu.addAction(act_clear)
        menu.addActions([act_helper])
        menu.addAction(act_plot)
        menu.exec(self.list_widget.mapToGlobal(pos))

    def specs_snapshot(self):
        """Método `VariablesPanel.specs_snapshot`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        return dict(self.specs)
