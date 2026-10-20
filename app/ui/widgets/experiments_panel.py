"""Panel de experimentos: emite sinais, não decide nada."""

from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QComboBox,
    QFileDialog,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)

from app.core.parsing import var_label
from app.ui.models.repository_paged_model import RepositoryPagedModel


class ExperimentsPanel(QWidget):
    """Classe `ExperimentsPanel` do módulo."""
    compareRequested = Signal(int, int)
    compareTripleRequested = Signal(int, int, int)   # T5438: A/B/C
    clearRequested = Signal()
    saveTemplateRequested = Signal()    # grava versão no repositório de templates
    generateDatsRequested = Signal()    # abre export de .dats (barra de status)
    openOutputRequested = Signal(str)   # abre a pasta de .dats no explorer

    def __init__(self, model: RepositoryPagedModel, parent=None):
        """Método `ExperimentsPanel.__init__`.
            Parâmetros: `self`, `model`, `parent`."""
        super().__init__(parent)
        self.model = model

        layout = QVBoxLayout(self)
        layout.setContentsMargins(6, 3, 6, 3)
        layout.setSpacing(2)

        header = QHBoxLayout()
        self.lbl_info = QLabel("0 experimentos — página 1/1")
        btn_prev = QPushButton("◀ Anterior")
        btn_next = QPushButton("Próxima ▶")
        btn_prev.clicked.connect(self._prev)
        btn_next.clicked.connect(self._next)
        self.combo_var_filter = QComboBox()
        self.combo_var_filter.setToolTip("Filtrar tabela por variável")
        self.combo_var_filter.currentIndexChanged.connect(self._apply_var_filter)
        self.btn_generate = QPushButton("Gerar .dats")
        self.btn_generate.setToolTip("Exporta os .dats do lote — barra de execução na barra de status.")
        self.btn_save_tpl = QPushButton("Salvar template")
        self.btn_save_tpl.setToolTip("Grava o texto atual como nova versão do template no banco de versões.")
        self.btn_open_output = QPushButton("Pasta output")
        self.btn_open_output.setToolTip("Abre a pasta dos .dats gerados no explorador.")
        self.btn_open_output.setEnabled(False)
        header.addWidget(self.lbl_info)
        header.addWidget(self.combo_var_filter)
        self.combo_format = QComboBox()
        self.combo_format.addItems(["Tabela", "Cartões (grid)", "Lista compacta", "Matriz"])
        self.combo_format.setToolTip("Formato de exibição: tabela paginada ou grade n×m de cartões.")
        self.combo_format.currentIndexChanged.connect(self._switch_format)
        header.addWidget(self.combo_format)
        header.addWidget(self.btn_generate)
        header.addWidget(self.btn_save_tpl)
        header.addWidget(self.btn_open_output)
        header.addStretch()
        header.addWidget(btn_prev)
        header.addWidget(btn_next)
        layout.addLayout(header)

        from app.ui.widgets.experiment_cards_view import ExperimentCardsView
        from app.ui.widgets.experiment_list_view import ExperimentListView
        from app.ui.widgets.experiment_matrix_view import ExperimentMatrixView
        from PySide6.QtWidgets import QStackedWidget

        self.table = QTableView()
        self.table.setMinimumSize(170, 100)
        self.table.setModel(model)
        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents
        )
        self.cards_view = ExperimentCardsView(cols=4)
        self.list_view = ExperimentListView()
        self.matrix_view = ExperimentMatrixView()
        self.view_stack = QStackedWidget()
        self.view_stack.addWidget(self.table)        # index 0
        self.view_stack.addWidget(self.cards_view)   # index 1
        self.view_stack.addWidget(self.list_view)    # index 2
        self.view_stack.addWidget(self.matrix_view)  # index 3
        layout.addWidget(self.view_stack, 1)

        self._new_button = QPushButton("Comparar selecionados…")
        layout.addWidget(self._new_button)
        self._new_button.clicked.connect(self._emit_compare)

        self.btn_generate.clicked.connect(self.generateDatsRequested.emit)
        self.btn_save_tpl.clicked.connect(self.saveTemplateRequested.emit)
        self.btn_open_output.clicked.connect(self._open_output)

        self._clear_button = QPushButton("Limpar tabela")
        self._clear_button.setToolTip("Apaga todos os experimentos e lotes gerados.")
        layout.addWidget(self._clear_button)
        self._clear_button.clicked.connect(self.clearRequested.emit)

        self._csv_button = QPushButton("Exportar CSV")
        self.btn_csv_matrix = QPushButton("Exportar matriz (CSV)")
        self.btn_csv_matrix.setToolTip("Salva a matriz experimentos × variáveis da página atual como CSV (';' como separador).")
        self.btn_csv_matrix.clicked.connect(self._export_matrix_csv)
        self._csv_button.setToolTip("Exporta todos os experimentos (página corrente do filtro) para CSV.")
        layout.addWidget(self._csv_button)
        self._csv_button.clicked.connect(self._export_csv)
        layout.addWidget(self.btn_csv_matrix)
        self.btn_stats = QPushButton("Estatísticas")
        self.btn_stats.setToolTip("Resumo descritivo (n, mín, média, desvio, máx) das variáveis da página atual.")
        self.btn_stats.clicked.connect(self._open_stats)
        layout.addWidget(self.btn_stats)

        model.dataChanged.connect(lambda *_: self._refresh_label())
        model.modelReset.connect(self._refresh_label)
        model.modelReset.connect(self._sync_filter_combo)
        model.modelReset.connect(lambda: self._sync_views())
        self._sync_filter_combo()
        self._refresh_label()
        self._sync_views()

    def set_last_output_dir(self, path: str | None):
        """Habilita 'Pasta output' só quando existe pasta com .dats."""
        self._last_output_dir = path
        self.btn_open_output.setEnabled(bool(path))

    def _open_output(self):
        """Método `ExperimentsPanel._open_output`.
            Parâmetros: `self`."""
        path = getattr(self, "_last_output_dir", None)
        if path:
            self.openOutputRequested.emit(str(path))

    def _switch_format(self, index: int):
        """Método `ExperimentsPanel._switch_format`.
            Parâmetros: `self`, `index`."""
        self.view_stack.setCurrentIndex(index if index in (0, 1, 2, 3) else 0)
        if index in (1, 2, 3):
            self._sync_views()

    def _sync_views(self):
        """Método `ExperimentsPanel._sync_views`.
            Parâmetros: `self`."""
        rows = self.model.page_rows
        var_ids = self.model.shown_var_ids
        self.cards_view.set_data(rows, var_ids)
        self.list_view.set_data(rows, var_ids)
        self.matrix_view.set_data(rows, var_ids)

    def _sync_filter_combo(self):
        """Método `ExperimentsPanel._sync_filter_combo`.
            Parâmetros: `self`."""
        combo = self.combo_var_filter
        combo.blockSignals(True)
        combo.clear()
        combo.addItem("Todas as variáveis")
        var_ids = self.model.repo.var_ids() if self.model.repo is not None else []
        for var_id in var_ids:
            combo.addItem(var_label(var_id), userData=var_id)
        if self.model.var_filter is not None:
            index = combo.findData(self.model.var_filter)
            combo.setCurrentIndex(index if index >= 0 else 0)
        else:
            combo.setCurrentIndex(0)
        combo.blockSignals(False)

    def _apply_var_filter(self, index: int):
        """Método `ExperimentsPanel._apply_var_filter`.
            Parâmetros: `self`, `index`."""
        var_id = self.combo_var_filter.itemData(index)
        self.model.set_var_filter(var_id)

    def _export_csv(self):
        """Método `ExperimentsPanel._export_csv`.
            Parâmetros: `self`."""
        from app.services.experiments_export_service import export_experiments_csv

        path, _ = QFileDialog.getSaveFileName(
            self, "Exportar experimentos", "experiments.csv", "CSV (*.csv)"
        )
        if not path:
            return
        export_experiments_csv(self.model.repo, path, var_ids=self.model.shown_var_ids)

    def _export_matrix_csv(self):
        """'Exportar matriz (CSV)' — grava a matriz exp×var da página atual."""
        from app.ui.widgets.experiment_matrix_view import matrix_csv

        path, _ = QFileDialog.getSaveFileName(
            self, "Exportar matriz", "matriz.csv", "CSV (*.csv)"
        )
        if not path:
            return
        content = matrix_csv(self.model.page_rows, self.model.shown_var_ids)
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(content)

    def _open_stats(self):
        """'Estatísticas' — diálogo com resumo descritivo por variável."""
        from app.ui.widgets.stats_dialog import StatsDialog

        dlg = StatsDialog(self.model.page_rows, self.model.shown_var_ids, parent=self)
        dlg.show()

    def _refresh_label(self):
        """Método `ExperimentsPanel._refresh_label`.
            Parâmetros: `self`."""
        m = self.model
        self.lbl_info.setText(
            f"{m.total_rows} experimentos — página {m.current_page + 1}/{m.total_pages}"
        )

    def _prev(self):
        """Método `ExperimentsPanel._prev`.
            Parâmetros: `self`."""
        self.model.prev_page()
        self._refresh_label()
        self._sync_views()

    def _next(self):
        """Método `ExperimentsPanel._next`.
            Parâmetros: `self`."""
        self.model.next_page()
        self._refresh_label()
        self._sync_views()

    def selected_rows(self):
        """Método `ExperimentsPanel.selected_rows`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        from PySide6.QtCore import Qt

        selection = self.table.selectionModel().selectedRows(0)
        rows = sorted(
            int(self.model.data(index, Qt.ItemDataRole.DisplayRole)) or 0
            for index in selection
        )
        return rows

    def _emit_compare(self):
        """Método `ExperimentsPanel._emit_compare`.
            Parâmetros: `self`."""
        rows = self.selected_rows()
        if not rows:
            return
        if len(rows) >= 3:
            # T5438: seleção tripla — comparação A/B/C
            self.compareTripleRequested.emit(rows[0], rows[1], rows[2])
            return
        self.compareRequested.emit(rows[0], rows[-1])
