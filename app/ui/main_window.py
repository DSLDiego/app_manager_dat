"""MainWindow apenas compõe (DI + Event Bus). Toda lógica está em services/workers."""

from __future__ import annotations

from PySide6.QtCore import QTimer, Qt, Signal
from PySide6.QtGui import QAction, QActionGroup, QIntValidator, QKeySequence
from PySide6.QtWidgets import (
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QDockWidget,
    QFormLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QProgressBar,
    QSpinBox,
    QStatusBar,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from app.container import Container
from app.core.parsing import find_variables, var_label, vars_status_text
from app.core.validation import find_incomplete_variables
from app.domain.entities import DistributionSpec, SamplingRequest
from app.domain.events import (
    SamplingCompletedEvent,
    SamplingFailedEvent,
    SamplingProgressEvent,
    SamplingStartedEvent,
    TemplateDetectedEvent,
)
from app.ui.editor.editor_tabs import EditorTabs
from app.ui.widgets.experiments_panel import ExperimentsPanel
from app.ui.widgets.logs_panel import LogsPanel
from app.ui.widgets.preview_panel import PreviewPanel
from app.ui.widgets.variables_panel import VariablesPanel


class _SampleInputDialog(QDialog):
    """Pedido de n Experiments e Strategy; apenas coleção pura de valores."""

    def __init__(self, parent=None):
        """Método `_SampleInputDialog.__init__`.
            Parâmetros: `self`, `parent`."""
        super().__init__(parent)
        self.setWindowTitle("Amostragem")

        form = QFormLayout()
        self.spin_n = QSpinBox()
        self.spin_n.setRange(1, 1_000_000)
        self.spin_n.setValue(10)
        self.combo_strategy = _StrategyCombo()
        self.spin_workers = QSpinBox()
        self.spin_workers.setRange(1, 64)
        self.spin_workers.setValue(1)
        # r23: seed configurável — vazio = aleatório por execução
        self.edit_seed = QLineEdit()
        self.edit_seed.setPlaceholderText("vazio = aleatório")
        self.edit_seed.setValidator(QIntValidator(1, 2_147_483_647))
        form.addRow("Experiments:", self.spin_n)
        form.addRow("Estratégia:", self.combo_strategy)
        form.addRow("Escolhas de cores (workers):", self.spin_workers)
        form.addRow("Seed:", self.edit_seed)
        lay = QVBoxLayout(self)
        lay.addLayout(form)
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        lay.addWidget(buttons)

    def result_values(self):
        """Método `_SampleInputDialog.result_values`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        from app.core.seed_utils import seed_from_text

        try:
            seed = seed_from_text(self.edit_seed.text())
        except ValueError:
            seed = seed_from_text("")  # texto inválido → aleatório
        return (
            self.spin_n.value(),
            self.combo_strategy.currentText(),
            self.spin_workers.value(),
            seed,
        )


class _StrategyCombo(QWidget):
    """Combo simples de estratégia (para evitar import circular)."""

    def __init__(self, parent=None):
        """Método `_StrategyCombo.__init__`.
            Parâmetros: `self`, `parent`."""
        from PySide6.QtWidgets import QComboBox

        super().__init__(parent)
        self._combo = QComboBox(self)
        self._combo.addItems(["monte_carlo", "lhs", "sobol", "halton"])
        lay = QVBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self._combo)

    def currentText(self) -> str:
        """Método `_StrategyCombo.currentText`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        return self._combo.currentText()


class MainWindow(QMainWindow):
    """Classe `MainWindow` do módulo."""
    def __init__(self, container: Container):
        """Método `MainWindow.__init__`.
            Parâmetros: `self`, `container`."""
        super().__init__()
        self.container = container
        self.last_sampling = None

        self.setWindowTitle("DAT Engineering Studio")
        self.resize(1280, 800)
        self.setMinimumSize(860, 560)

        # ----- escala de fonte do sistema (persistida) -----
        from PySide6.QtWidgets import QApplication

        from app.ui.editor.themes import saved_system_scale

        self._base_app_font = QApplication.instance().font()
        self._system_font_scale = saved_system_scale()
        if self._system_font_scale != 1.0:
            self._apply_system_font()

        # ----- widgets principais -----
        self.editor_tabs = EditorTabs(self)
        self.variables_panel = VariablesPanel(container.registry, self, exp_repo=container.exp_repo)
        self.variables_panel.list_widget.clear()
        self.preview_panel = PreviewPanel(self)
        self.logs_panel = LogsPanel(container.log_repo, self)

        container.ensure_services
        from app.ui.models.repository_paged_model import RepositoryPagedModel
        from app.ui.widgets.experiments_panel import ExperimentsPanel
        from app.ui.widgets.heat_matrix_panel import HeatMatrixPanel
        from app.ui.widgets.histogram_grid_panel import HistogramGridPanel

        self.exp_model = RepositoryPagedModel(container.exp_repo)
        self.experiments_panel = ExperimentsPanel(self.exp_model, self)
        self.matrix_panel = HeatMatrixPanel(self)
        self.matrix_panel.load_from_repo(container.exp_repo)
        self.hist_panel = HistogramGridPanel(self)
        self.hist_panel.load_from_repo(container.exp_repo)
        from app.ui.widgets.files_list_panel import FilesListPanel

        self.files_panel = FilesListPanel(self.editor_tabs, self)
        from app.ui.widgets.usage_flow_panel import UsageFlowPanel

        self.flow_panel = UsageFlowPanel(self)

        tabs = QTabWidget()
        tabs.addTab(self.editor_tabs, "Editor")
        tabs.addTab(self.preview_panel, "Preview")
        self.setCentralWidget(tabs)

        self._dock_variables = self._add_dock("Variáveis", self.variables_panel)
        self._dock_experiments = self._add_dock("Experimentos", self.experiments_panel)
        self._dock_matrix = self._add_dock(
            "Matriz de experimentos", self.matrix_panel,
            area=Qt.DockWidgetArea.BottomDockWidgetArea,
        )
        self._dock_logs = self._add_dock(
            "Logs", self.logs_panel, area=Qt.DockWidgetArea.BottomDockWidgetArea
        )
        self._dock_hists = self._add_dock(
            "Histogramas por variável", self.hist_panel,
            area=Qt.DockWidgetArea.BottomDockWidgetArea,
        )
        self._dock_files = self._add_dock(
            "Arquivos em edição", self.files_panel,
            area=Qt.DockWidgetArea.LeftDockWidgetArea,
        )
        self._dock_flow = self._add_dock(
            "Fluxo de uso", self.flow_panel,
            area=Qt.DockWidgetArea.LeftDockWidgetArea,
        )

        # ----- 1.1: docks preenchem mais área na primeira abertura -----
        # Aumenta espaço para o editor/central; reduz largura dos docks
        self.resizeDocks(
            [self._dock_matrix, self._dock_hists, self._dock_logs],
            [200, 200, 200], Qt.Orientation.Horizontal,
        )
        self.resizeDocks(
            [self._dock_variables, self._dock_experiments],
            [300, 300], Qt.Orientation.Vertical,
        )
        self.resizeDocks([self._dock_files], [180], Qt.Orientation.Vertical)
        self.resizeDocks(
            [self._dock_files, self._dock_flow], [180, 160], Qt.Orientation.Vertical
        )

        # ----- barra de status -----
        self.status = QStatusBar()
        from app.ui.layout_presets import LAYOUT_PRESETS

        self.combo_layout = QComboBox()
        self.combo_layout.addItems(list(LAYOUT_PRESETS))
        self.combo_layout.setToolTip("Padrão de layout dos painéis: grade, abas, metades ou 4 quadrantes.")
        self.combo_layout.currentTextChanged.connect(self._apply_layout_preset)
        self.status.addWidget(QLabel("Layout:"))
        self.status.addWidget(self.combo_layout)
        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        self.progress.setValue(0)
        self.status.addPermanentWidget(self.progress)
        # r22: contagem de variáveis da aba ativa
        self.lbl_vars_status = QLabel("— vars")
        self.lbl_vars_status.setToolTip(
            "Variáveis do template ativo: $N (posicionais) + $varN (namespace)."
        )
        self.status.addPermanentWidget(self.lbl_vars_status)
        self._vars_timer = QTimer(self)
        self._vars_timer.setInterval(700)
        self._vars_timer.timeout.connect(self._update_vars_status)
        self._vars_timer.start()
        self.setStatusBar(self.status)

        self._build_menus()

        self._wire_events()
        self.editor_tabs.new_tab()
        self.editor_tabs.currentChanged.connect(self._sync_variables)

    # ---------- build ----------
    def _add_dock(self, title: str, widget: QWidget, area=Qt.DockWidgetArea.RightDockWidgetArea):
        """Método `MainWindow._add_dock`.
            Parâmetros: `self`, `title`, `widget`, `area`.
            Retorna o resultado calculado a partir do estado local."""
        dock = QDockWidget(title, self)
        dock.setWidget(widget)
        self.addDockWidget(area, dock)
        return dock

    def _build_menus(self):
        """Método `MainWindow._build_menus`.
            Parâmetros: `self`."""
        menu_file = self.menuBar().addMenu("Arquivo")
        act_new = QAction("Novo", self)
        act_new.triggered.connect(self.editor_tabs.new_tab)
        act_open = QAction("Abrir…", self)
        act_open.triggered.connect(self.editor_tabs.open_dialog)
        act_save = QAction("Salvar", self)
        act_save.triggered.connect(self.editor_tabs.save_current)
        menu_file.addActions([act_new, act_open, act_save])
        act_save.setShortcut(QKeySequence("Ctrl+S"))
        # r19/r21: arquivos recentes (persistem entre sessões via QSettings)
        from PySide6.QtCore import QSettings

        from app.ui.editor.editor_tabs import recent_split

        settings = QSettings("datstudio", "dtengine")
        self._recent = recent_split(settings.value("recent/files", ""))
        self.menu_recent = self.menuBar().addMenu("Recentes")
        self.menu_recent.setToolTip("Últimos arquivos abertos (persistem entre sessões).")
        self._refresh_recent_menu()
        self.editor_tabs.fileOpened.connect(self._push_recent)
        act_wizard = QAction("Assistente de template…", self)
        act_wizard.setToolTip("Cria um template .dat em 3 passos: texto → variáveis → revisão.")
        act_wizard.triggered.connect(self._open_template_wizard)
        menu_file.addAction(act_wizard)

        menu_tools = self.menuBar().addMenu("Ferramentas")
        act_save_tpl = QAction("Salvar template (versão no repositório)", self)
        act_save_tpl.setToolTip("Grava o texto atual como nova versão do template no banco de versões.")
        act_save_tpl.triggered.connect(self._save_template_version)
        act_reload_dat = QAction("Re-ler .dat do disco (novas variáveis)", self)
        act_reload_dat.setToolTip("Recarrega o arquivo .dat da aba atual e atualiza os tokens de variáveis.")
        act_reload_dat.triggered.connect(self._reload_dat_file)
        act_validate_tpl = QAction("Validar template CMG", self)
        act_validate_tpl.setToolTip("Heurística de seções/tokens do .dat da aba atual.")
        act_validate_tpl.triggered.connect(self._validate_template_action)
        act_includes = QAction("INCLUDEs do template…", self)
        act_includes.setToolTip(
            "Navega pelos arquivos INCLUDE/*INCLUDE e lê as variáveis de cada um."
        )
        act_includes.triggered.connect(self._open_includes_dialog)
        act_includes.setShortcut(QKeySequence("Alt+D"))
        act_open_include = QAction("Abrir INCLUDE no editor", self)
        act_open_include.setToolTip(
            "Abra o arquivo INCLUDE selecionado no editor para edição"
        )
        act_open_include.triggered.connect(self._open_selected_include_in_editor)
        act_preview = QAction("Preview (amostra 1)", self)
        act_preview.triggered.connect(self._run_preview)
        act_export_builder = QAction("Exportar batch de .dats…", self)
        act_export_builder.triggered.connect(self._open_batch_export)
        act_logs = QAction("Exportar Logs", self)
        act_logs.triggered.connect(self.logs_panel.export_csv)
        menu_tools.addAction(act_preview)
        menu_tools.addAction(act_export_builder)
        menu_tools.addAction(act_save_tpl)
        menu_tools.addAction(act_reload_dat)
        menu_tools.addAction(act_validate_tpl)
        menu_tools.addAction(act_includes)
        menu_tools.addSeparator()
        act_plot = QAction("Plotar distribuição / f(x)…", self)
        act_plot.triggered.connect(self._open_distribution_plot)
        menu_tools.addAction(act_plot)
        menu_tools.addAction(act_logs)
        menu_tools.addSeparator()
        # r24: reexecução rápida da última amostragem
        self.act_rerun_same = QAction("Reexecutar amostragem (mesma seed)", self)
        self.act_rerun_same.setToolTip(
            "Repete a última amostragem com a MESMA seed — results idênticos."
        )
        self.act_rerun_same.triggered.connect(lambda: self._rerun_sampling(True))
        self.act_rerun_new = QAction("Reexecutar amostragem (nova seed aleatória)", self)
        self.act_rerun_new.setToolTip(
            "Repete a última amostragem com nova seed — variações independentes."
        )
        self.act_rerun_new.triggered.connect(lambda: self._rerun_sampling(False))
        menu_tools.addAction(self.act_rerun_same)
        menu_tools.addAction(self.act_rerun_new)
        menu_tools.addSeparator()
        act_batch_hist = QAction("Histórico de lotes…", self)
        act_batch_hist.setToolTip("Lotes anteriores com seed/método/n — copie ou reuse a seed.")
        act_batch_hist.triggered.connect(self._open_batch_history)
        menu_tools.addAction(act_batch_hist)
        act_plugins = QAction("Plugins & Providers…", self)
        act_plugins.setToolTip("Providers carregados, relatório de carga e recarga a quente.")
        act_plugins.triggered.connect(self._open_plugins_dialog)
        menu_tools.addAction(act_plugins)

        menu_studies = self.menuBar().addMenu("Estudos")
        act_studies = QAction("Gerenciar estudos…", self)
        act_studies.triggered.connect(self._open_studies_dialog)
        menu_studies.addAction(act_studies)
        act_study_new = QAction("Novo estudo a partir do estado atual…", self)
        act_study_new.triggered.connect(self._create_study_from_state)
        menu_studies.addAction(act_study_new)

        menu_view = self.menuBar().addMenu("Ver")
        self._theme_group = QActionGroup(self)
        from app.ui.editor.themes import DEFAULT_THEME

        for theme_name, label in (
            ("dracula", "Tema Dracula"),
            ("light", "Tema Claro"),
            ("nord", "Tema Nord"),
            ("solarized", "Tema Solarized"),
        ):
            act_theme = QAction(label, self)
            act_theme.setCheckable(True)
            act_theme.setChecked(theme_name == DEFAULT_THEME)
            act_theme.triggered.connect(lambda _, t=theme_name: self._set_theme(t))
            self._theme_group.addAction(act_theme)
            menu_view.addAction(act_theme)

        menu_view.addSeparator()
        act_dock_grid = QAction("Organizar docks em grade n×m", self)
        act_dock_grid.triggered.connect(self._arrange_docks_grid)
        menu_view.addAction(act_dock_grid)
        act_dock_tabs = QAction("Empilhar docks em abas (aproveitar espaço)", self)
        act_dock_tabs.setToolTip(
            "Agrupa Variáveis+Experimentos (direita) e Matriz+Logs (embaixo) como abas — reduz áreas vazias."
        )
        act_dock_tabs.triggered.connect(self._tabify_docks)
        menu_view.addAction(act_dock_tabs)
        act_show_all_experiments = QAction("Mostrar todos os experimentos (sem filtro de lote)", self)
        act_show_all_experiments.triggered.connect(self._clear_batch_filter)
        menu_view.addAction(act_show_all_experiments)
        act_zoom_in = QAction("Aumentar fonte do editor", self)
        act_zoom_in.setShortcut(QKeySequence("Ctrl++"))
        act_zoom_in.triggered.connect(lambda: self._zoom_editors(1))
        menu_view.addAction(act_zoom_in)
        act_zoom_out = QAction("Reduzir fonte do editor", self)
        act_zoom_out.setShortcut(QKeySequence("Ctrl+-"))
        act_zoom_out.triggered.connect(lambda: self._zoom_editors(-1))
        menu_view.addAction(act_zoom_out)
        act_zoom_reset = QAction("Restaurar fonte do editor", self)
        act_zoom_reset.setShortcut(QKeySequence("Ctrl+0"))
        act_zoom_reset.triggered.connect(self._reset_zoom_editors)
        menu_view.addAction(act_zoom_reset)
        self.act_minimap = QAction("Minimapa do editor", self, checkable=True)
        self.act_minimap.setChecked(True)
        self.act_minimap.setToolTip("Mostra/oculta a coluna de minimapa ao lado do editor.")
        self.act_minimap.toggled.connect(self._toggle_minimap)
        menu_view.addAction(self.act_minimap)

        menu_view.addSeparator()
        act_sys_in = QAction("Aumentar fonte do sistema", self)
        act_sys_in.triggered.connect(lambda: self._change_system_font(1))
        menu_view.addAction(act_sys_in)
        act_sys_out = QAction("Reduzir fonte do sistema", self)
        act_sys_out.triggered.connect(lambda: self._change_system_font(-1))
        menu_view.addAction(act_sys_out)
        act_sys_reset = QAction("Restaurar fonte do sistema", self)
        act_sys_reset.triggered.connect(self._reset_system_font)
        menu_view.addAction(act_sys_reset)
        act_sys_opts = QAction("Escala da fonte do sistema (com preview)…", self)
        act_sys_opts.triggered.connect(self._open_system_scale_dialog)
        menu_view.addAction(act_sys_opts)

        menu_view.addSeparator()
        act_grid = QAction("Organizar docks em grade n×m", self)
        act_grid.triggered.connect(self._arrange_docks_grid)
        menu_view.addAction(act_grid)

    # ---------- grade n×m ----------
    def _dock_names(self) -> dict[str, QDockWidget]:
        """Método `MainWindow._dock_names`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        return {
            "variables": self._dock_variables,
            "files": self._dock_files,
            "experiments": self._dock_experiments,
            "matrix": self._dock_matrix,
            "hists": self._dock_hists,
            "logs": self._dock_logs,
            "flow": self._dock_flow,
        }

    def _execute_layout_plan(self, plan: list):
        """Executa [(op, a, b)] de layout_presets — reset por float/unfloat."""
        named = self._dock_names()
        for name in ("variables", "files", "experiments", "matrix", "hists", "logs", "flow"):
            dock = named.get(name)
            if dock is None:
                continue
            dock.setFloating(True)
            dock.setFloating(False)
        for op, a, b in plan:
            da, db = named.get(a), named.get(b)
            if da is None or db is None:
                continue
            if op == "split_h":
                self.splitDockWidget(da, db, Qt.Orientation.Horizontal)
            elif op == "split_v":
                self.splitDockWidget(da, db, Qt.Orientation.Vertical)
            elif op == "tabify":
                self.tabifyDockWidget(da, db)
        for dock in named.values():
            if dock is not None:
                dock.show()

    def _apply_layout_preset(self, preset: str):
        """Combo 'Layout:' da status bar — aplica o padrão escolhido."""
        from app.ui.layout_presets import layout_plan

        order = ["files", "flow", "variables", "experiments", "matrix", "hists", "logs"]
        plan = layout_plan(preset, order)
        if preset in ("Abas", "Editor | Painéis"):
            named = self._dock_names()
            for name in order:
                dock = named.get(name)
                if dock is not None:
                    self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock)
        self._execute_layout_plan(plan)
        self.set_status(f"Layout aplicado: {preset} ({len(plan)} ops).")

    # ---------- r17: docks estreitos — cap = 20% da largura da janela ----------
    def _enforce_dock_width_caps(self):
        """Baixa mínimos explícitos que forcem dock > 20% da largura da janela."""
        from app.ui.layout_presets import dock_width_cap, widgets_over_cap

        cap = dock_width_cap(self.width())
        widgets = []
        for dock in self._dock_names().values():
            if dock is None or dock.widget() is None:
                continue
            widgets.append(dock.widget())
            widgets.extend(dock.widget().findChildren(QWidget))
        for w in widgets_over_cap(widgets, cap):
            w.setMinimumWidth(cap)

    def resizeEvent(self, event):
        """Método `MainWindow.resizeEvent`.
            Parâmetros: `self`, `event`."""
        super().resizeEvent(event)
        if hasattr(self, "_dock_variables"):
            self._enforce_dock_width_caps()

    def _arrange_docks_grid(self):
        """Distribui docks em grade n×m via split (linhas=ceil(n/cols))."""
        docks = [
            self._dock_variables,
            self._dock_files,
            self._dock_experiments,
            self._dock_matrix,
            self._dock_hists,
            self._dock_logs,
        ]
        count = len(docks)
        if count == 0:
            return
        import math as _math

        cols = max(1, int(_math.ceil(_math.sqrt(count))))
        rows = max(1, int(_math.ceil(count / cols)))
        for dock in docks:
            dock.setFloating(False)
        for i, dock in enumerate(docks):
            if (i + 1) < count and (i + 1) % cols != 0:
                self.splitDockWidget(dock, docks[i + 1], Qt.Orientation.Horizontal)
        for i in range(0, count - cols):
            self.splitDockWidget(docks[i], docks[i + cols], Qt.Orientation.Vertical)
        for dock in docks:
            dock.show()
        self.set_status(f"Docks em grade {rows}×{cols}.")

    # ---------- estudos ----------
    def _open_studies_dialog(self):
        """Método `MainWindow._open_studies_dialog`.
            Parâmetros: `self`."""
        from app.ui.widgets.studies_dialog import StudiesDialog

        self.container.ensure_services()
        dialog = StudiesDialog(self.container.study_service, self)
        dialog.studyLoaded.connect(self._load_study)
        dialog.statusMessage.connect(self.set_status)
        dialog.exec()
        self._refresh_all_panels()

    def _refresh_all_panels(self):
        """Método `MainWindow._refresh_all_panels`.
            Parâmetros: `self`."""
        self.exp_model.refresh()
        self.logs_panel.refresh()

    def _snapshot_current_study(self):
        """Método `MainWindow._snapshot_current_study`.
            Parâmetros: `self`."""
        QMessageBox.information(
            self,
            "Salvar versão",
            "Abra 'Gerenciar estudos…', selecione um estudo e clique em "
            "'Salvar versão do estudo' com um comentário.",
        )

    # ---------- estudo a partir do estado atual ----------
    def _current_study_state(self) -> dict:
        """Método `MainWindow._current_study_state`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        editor = self.editor_tabs.current_editor()
        dat_path = ""
        if editor is not None and getattr(editor, "file_path", None):
            dat_path = str(editor.file_path)
        return {
            "dat_path": dat_path,
            "template_text": self._current_text() or "",
            "template_version_id": getattr(self, "_last_template_version_id", None),
            "batch_id": getattr(self, "_last_batch_id", None),
            "output_dir": getattr(self, "_last_output_dir", None),
        }

    def _create_study_from_state(self):
        """Método `MainWindow._create_study_from_state`.
            Parâmetros: `self`."""
        from PySide6.QtWidgets import QInputDialog

        self.container.ensure_services()
        state = self._current_study_state()
        if not state.get("template_text"):
            QMessageBox.warning(
                self, "Sem template", "Abra ou digite um template antes de criar o estudo."
            )
            return
        name, ok = QInputDialog.getText(self, "Novo estudo", "Nome do estudo:")
        name = str(name).strip()
        if not ok or not name:
            return
        try:
            specs = self.variables_panel.specs_snapshot()
            study_id = self.container.study_service.create(
                name, specs, meta=state, description="estado atual"
            )
        except Exception as exc:  # noqa: BLE001
            QMessageBox.critical(self, "Erro", str(exc))
            return
        self.set_status(f"Estudo #{study_id} '{name}' salvo (dat+template+variáveis+batch+saída).")
        self._open_study_id = int(study_id)
        try:  # T5434: versão inicial do .dat dentro do estudo
            self.container.study_service.save_dat_version(
                study_id, state.get("template_text") or "", "estado inicial"
            )
        except Exception as exc:  # noqa: BLE001
            self.set_status(f"Aviso: versão do .dat não gravada ({exc}).")
        self.container.log_service.audit(
            "study.created", name, entity_type="study", entity_id=int(study_id)
        )

    def _load_study(self, study_id: int):
        """Abre o estudo: editor com template, specs e metadata do estudo."""
        study = self.container.study_service.get(study_id)
        meta = study.get("meta") or {}
        self._open_study_id = int(study_id)  # T5444: estudo aberto recebe batches
        template_text = meta.get("template_text")

        from app.domain.entities import DistributionSpec

        specs: dict[int, DistributionSpec] = {}
        for raw_var_id, raw_spec in (study.get("specs") or {}).items():
            specs[int(raw_var_id)] = DistributionSpec(
                provider=raw_spec.get("provider", "scipy"),
                name=raw_spec.get("name", "uniform"),
                params=dict(raw_spec.get("params") or {}),
            )

        if template_text:
            self.editor_tabs.new_tab(template_text, title=f"Estudo #{study_id}")
            self.variables_panel.specs = specs
            self.variables_panel.update_tokens(template_text)

        batch_id = meta.get("batch_id")
        if batch_id and self.container.exp_repo.count(batch_id) > 0:
            self.exp_model.set_batch_filter(batch_id)
            self.statusBar().showMessage(
                f"Tabela de experimentos filtrada no lote '{batch_id}'.", 8000
            )

        self.set_status(
            f"Estudo #{study_id} '{study['name']}' aberto "
            f"(batch {meta.get('batch_id', '—')} → {meta.get('output_dir', '—')})."
        )

    def _tabify_docks(self):
        """1.1: docks do mesmo lado viram ABAS — menos espaço vazio na janela."""
        self.tabifyDockWidget(self._dock_variables, self._dock_experiments)
        self.tabifyDockWidget(self._dock_variables, self._dock_files)
        self.tabifyDockWidget(self._dock_matrix, self._dock_hists)
        self.tabifyDockWidget(self._dock_hists, self._dock_logs)
        self._dock_variables.raise_()
        self._dock_matrix.raise_()
        self.set_status("Docks empilhados em abas — Ver › grade n×m para dispersar de novo.")

    def _clear_batch_filter(self):
        """Método `MainWindow._clear_batch_filter`.
            Parâmetros: `self`."""
        self.exp_model.set_batch_filter(None)
        self.set_status("Filtro de lote removido.")

    def _close_editor_tab(self, index: int):
        """Usado pela lista de arquivos (Notepad++-style)."""
        self.editor_tabs._handle_close_request(index)

    def _open_template_wizard(self):
        """'Assistente de template…' no menu Arquivo — cria aba ao concluir."""
        from app.ui.widgets.template_wizard_dialog import TemplateWizardDialog

        dlg = TemplateWizardDialog(self)
        dlg.templateReady.connect(self._create_template_tab)
        dlg.show()

    # ---------- r22: contagem de variáveis (barra de status) ----------
    def _update_vars_status(self):
        """Método `MainWindow._update_vars_status`.
            Parâmetros: `self`."""
        editor = self.editor_tabs.current_editor()
        text = editor.text() if editor is not None else ""
        self.lbl_vars_status.setText(vars_status_text(text))

    # ---------- r21: preferências de UI persistidas ----------
    def _restore_ui_choices(self):
        """Lembra formato de experimentos e curva normal entre sessões."""
        from app.ui.ui_prefs import load_ui_choice

        try:
            fmt = int(load_ui_choice("experiments/format", 0))
        except (TypeError, ValueError):
            fmt = 0
        if 0 <= fmt < self.experiments_panel.combo_format.count():
            self.experiments_panel.combo_format.setCurrentIndex(fmt)
        fit = load_ui_choice("hists/fit", "false")
        self.hist_panel.chk_fit.setChecked(str(fit).lower() in ("1", "true", "yes"))
        self.hist_panel.chk_fit.toggled.connect(
            lambda on: self._save_ui_choice("hists/fit", on)
        )
        self.experiments_panel.combo_format.currentIndexChanged.connect(
            lambda i: self._save_ui_choice("experiments/format", int(i))
        )

    @staticmethod
    def _save_ui_choice(key: str, value):
        """Método `MainWindow._save_ui_choice`.
            Parâmetros: `key`, `value`."""
        from app.ui.ui_prefs import save_ui_choice

        save_ui_choice(key, value)

    # ---------- r19/r21: arquivos recentes ----------
    def _persist_recent(self):
        """Método `MainWindow._persist_recent`.
            Parâmetros: `self`."""
        from PySide6.QtCore import QSettings

        from app.ui.editor.editor_tabs import recent_join

        QSettings("datstudio", "dtengine").setValue(
            "recent/files", recent_join(self._recent)
        )

    def _push_recent(self, path: str):
        """Método `MainWindow._push_recent`.
            Parâmetros: `self`, `path`."""
        from app.ui.editor.editor_tabs import recent_push

        self._recent = recent_push(self._recent, path)
        self._refresh_recent_menu()
        self._persist_recent()

    def _refresh_recent_menu(self):
        """Método `MainWindow._refresh_recent_menu`.
            Parâmetros: `self`."""
        from pathlib import Path

        self.menu_recent.clear()
        if not self._recent:
            empty = self.menu_recent.addAction("(sem arquivos recentes)")
            empty.setEnabled(False)
            return
        for path in self._recent:
            act = self.menu_recent.addAction(Path(path).name)
            act.setToolTip(path)
            act.triggered.connect(lambda _=False, p=path: self.editor_tabs.open_file(p))
        self.menu_recent.addSeparator()
        act_clear = self.menu_recent.addAction("Limpar recentes")
        act_clear.triggered.connect(self._clear_recent)

    def _clear_recent(self):
        """Método `MainWindow._clear_recent`.
            Parâmetros: `self`."""
        self._recent = []
        self._refresh_recent_menu()
        self._persist_recent()

    def _create_template_tab(self, text: str):
        """Método `MainWindow._create_template_tab`.
            Parâmetros: `self`, `text`."""
        self.editor_tabs.new_tab(content=text, title="novo_template.dat")
        self.set_status("Template criado pelo assistente — defina as distribuições.")

    def _toggle_minimap(self, visible: bool):
        """'Minimapa do editor' no menu Ver — aplica em todas as abas."""
        for i in range(self.editor_tabs.count()):
            w = self.editor_tabs.widget(i)
            if hasattr(w, "set_minimap_visible"):
                w.set_minimap_visible(visible)

    def _open_files_diff(self):
        """'Diff…' na lista de arquivos: 2 abas abertas (ou disco) lado a lado."""
        from app.ui.widgets.diff_dialog import DiffDialog

        open_files = [
            (self.editor_tabs.tabText(i), self.editor_tabs.widget(i).text())
            for i in range(self.editor_tabs.count())
            if hasattr(self.editor_tabs.widget(i), "text")
        ]
        dlg = DiffDialog(open_files=open_files, parent=self)
        dlg.show()

    # ---------- fluxo de uso (checklist) ----------
    def _flow_state(self) -> dict:
        """Estado mínimo para o checklist gestos (usado por UsageFlowPanel)."""
        state = {
            "template_hash": bool(self._current_text()),
            "dat_path": bool(getattr(self.editor_tabs.current_editor(), "file_path", None)),
            "specs": bool(self.variables_panel.specs),
            "sampling": bool(getattr(self, "last_sampling", None)),
            "output_dir": bool(getattr(self, "_last_output_dir", None)),
            "template_version_id": bool(getattr(self, "_last_template_version_id", None)),
            "has_studies": False,
        }
        try:
            studies = self.container.study_service.list_studies()
            state["has_studies"] = bool(studies)
        except Exception:  # noqa: BLE001
            state["has_studies"] = False
        return state

    def refresh_flow(self):
        """Método `MainWindow.refresh_flow`.
            Parâmetros: `self`."""
        self.flow_panel.refresh(self._flow_state())

    def _on_bus_sampling_completed(self, event):
        """r23: registra seed na barra de status (reprodutibilidade)."""
        self.refresh_flow()
        self.set_status(
            f"Amostragem concluída · seed={event.seed_used} · "
            f"{event.duration_seconds:.1f}s"
        )

    def _on_flow_action(self, step_id: str):
        """Método `MainWindow._on_flow_action`.
            Parâmetros: `self`, `step_id`."""
        if step_id == "tpl":
            if self.editor_tabs.current_editor() and getattr(
                self.editor_tabs.current_editor(), "file_path", None
            ):
                self._reload_dat_file()
            else:
                self.editor_tabs.open_dialog(self)
        elif step_id == "dist":
            self.variables_panel._edit_current()
        elif step_id == "sample":
            self.variables_panel.btn_sample.click()
        elif step_id == "dats":
            self._open_batch_export()
        elif step_id == "vers":
            self._save_template_version()
        elif step_id == "study":
            self._create_study_from_state()
        else:
            self.set_status(f"Etapa desconhecida: {step_id}")
            return
        from PySide6.QtCore import QTimer as _QTimer

        _QTimer.singleShot(200, self.refresh_flow)

    # ---------- template: salvar versão + re-ler .dat ----------
    def _save_template_version(self):
        """Método `MainWindow._save_template_version`.
            Parâmetros: `self`."""
        self.container.ensure_services()
        text = self._current_text()
        if not text.strip():
            QMessageBox.warning(self, "Vazio", "Nada para salvar: a aba atual está vazia.")
            return
        repo = self.container.template_repo
        if getattr(self, "_main_template_id", None) is None:
            templates = repo.list_templates()
            if templates:
                self._main_template_id = int(templates[0]["id"])
            else:
                self._main_template_id = repo.create_template("templates-do-app")
        version_id = repo.save_version(self._main_template_id, text, comment="via botão Salvar template")
        self._last_template_version_id = version_id
        self.set_status(f"Template salvo — versão registrada #{version_id}.")

    # ---------- INCLUDEs ----------
    def _template_base_dir(self):
        """Método `MainWindow._template_base_dir`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        from pathlib import Path as _Path

        editor = self.editor_tabs.current_editor()
        path = getattr(editor, "file_path", None) if editor is not None else None
        if path:
            return _Path(path).parent
        return _Path.cwd()

    def _open_includes_dialog(self) -> list:
        """R: coleta a árvore de INCLUDEs da aba atual e abre o navegador."""
        from app.core.includes import collect_includes
        from app.ui.widgets.includes_dialog import IncludesDialog

        editor = self.editor_tabs.current_editor()
        text = editor.text() if editor is not None else ""
        base_dir = self._template_base_dir()
        entries = collect_includes(text, base_dir)
        self._last_includes = entries
        dialog = IncludesDialog(entries, self)
        dialog.exec()
        return entries

    def _open_selected_include_in_editor(self) -> None:
        """Abre o include selecionado no include browser para edição."""
        from app.core.includes import collect_includes
        from app.ui.widgets.includes_dialog import IncludesDialog
        from pathlib import Path as _Path
        from PySide6.QtWidgets import QMessageBox

        editor = self.editor_tabs.current_editor()
        text = editor.text() if editor is not None else ""
        base_dir = self._template_base_dir()
        entries = collect_includes(text, base_dir)
        if not entries:
            return
        dialog = IncludesDialog(entries, self)
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return
        # Usuário selecionou uma linha na tabela
        selected_row = dialog.table.currentRow()
        if 0 <= selected_row < len(entries):
            entry = entries[selected_row]
            include_path = _Path(entry.get("resolved")) or _Path(entry.get("raw"))
            if include_path and include_path.exists():
                # Abre o caminho do include no editor
                resolved_str = str(include_path)
                # Tenta abrir como arquivo existente
                self.editor_tabs.open_file(resolved_str)
            else:
                QMessageBox.information(
                    self, "INCLUDE não encontrado",
                    f"O arquivo Include não existe:\n{include_path}"
                )

    def _validate_template_action(self) -> list:
        """R31: valida o texto da aba atual; guarda o último resultado."""
        from app.core.parsing import validate_template, validation_summary

        editor = self.editor_tabs.current_editor()
        text = editor.text() if editor is not None else ""
        issues = validate_template(text)
        self._last_validation = issues
        summary = validation_summary(issues)
        has_error = any(i.get("severity") == "error" for i in issues)
        if has_error:
            QMessageBox.warning(self, "Validação do template CMG", summary)
        else:
            QMessageBox.information(self, "Validação do template CMG", summary)
        self.set_status(
            "Template CMG: "
            + ("validação com erros." if has_error else "nenhum erro encontrado.")
        )
        return issues

    def _reload_dat_file(self):
        """Método `MainWindow._reload_dat_file`.
            Parâmetros: `self`."""
        from app.core.includes import parse_include_paths

        editor = self.editor_tabs.current_editor()
        path = getattr(editor, "file_path", None)
        if not path:
            QMessageBox.information(
                self, "Sem arquivo",
                "A aba atual não está ligada a um arquivo .dat. Salve-a ou abra um arquivo.",
            )
            return
        from pathlib import Path as _Path

        try:
            new_text = _Path(path).read_text(encoding="utf-8")
        except OSError as exc:
            QMessageBox.critical(self, "Erro ao ler", f"Não foi possível re-ler {path}:\n{exc}")
            return
        # Apenas recarrega o texto do .dat atual; includes já foram processados
        # anteriormente e não devem ser re-injetados no texto.
        # O usuário pode reabrir o arquivo se quiser incluir os paths novamente.
        if new_text != editor.text():
            editor.editor.setPlainText(new_text)
            self.container.log_service.audit("template.reloaded", f"{path}")
        self._sync_variables()
        self.set_status(f".dat re-lido de {path} — tokens atualizados")

    def _collect_variables_with_sources(self, text: str) -> dict:
        """Coleta variáveis do texto e rastreia a origem de cada uma.

        Retorna um dicionário mapeando var_id -> {'source': source_label, 'raw_var': var_id}.
        source_label pode ser 'main' (do .dat atual) ou o caminho do include.
        """
        from app.core.includes import collect_includes, parse_include_paths
        from app.core.parsing import find_variables, token_var_id
        from pathlib import Path as _Path
        from PySide6.QtCore import QSettings

        # 1. Encontra todas as variáveis no texto combinado
        all_var_ids = find_variables(text)
        # 2. Descobre quais includes foram usados
        editor = self.editor_tabs.current_editor()
        base_dir = self._template_base_dir() if editor else None
        include_entries = []
        if base_dir:
            try:
                include_entries = collect_includes(text, base_dir)
            except Exception:
                include_entries = []
        # 3. Mapeia cada variável para sua origem
        # Primeiro, identifica variáveis nos includes
        include_var_sources: dict[int, str] = {}  # var_id -> caminho do include
        for entry in include_entries:
            for var_id in entry.get("variables") or []:
                include_var_sources[var_id] = entry.get("resolved") or ""
        # 4. Para cada variável encontrada, determina a origem
        var_sources: dict = {}
        for var_id in sorted(all_var_ids):
            label = var_label(var_id)
            # Verifica se a variável vem de um include
            if var_id in include_var_sources:
                source = include_var_sources[var_id]
                if source:
                    source_label = f"INCLUDE: {_Path(source).name}"
                else:
                    source_label = "INCLUDE (caminho inválido)"
            else:
                source_label = "main"
            var_sources[var_id] = {
                "source": source_label,
                "var_id": var_id,
                "label": label,
            }
        return var_sources

    # ---------- plot de distribuições ----------
    def _open_distribution_plot(self):
        """Método `MainWindow._open_distribution_plot`.
            Parâmetros: `self`."""
        from app.ui.widgets.distribution_plot_dialog import DistributionPlotDialog

        self.container.ensure_services()
        dialog = DistributionPlotDialog(self.container.registry, self, exp_repo=self.container.exp_repo)
        dialog.redraw()
        dialog.exec()

    def _set_theme(self, theme_name: str):
        """Método `MainWindow._set_theme`.
            Parâmetros: `self`, `theme_name`."""
        from app.ui.editor.themes import persist_theme

        for i in range(self.editor_tabs.count()):
            tab = self.editor_tabs.widget(i)
            if tab is not None and hasattr(tab, "set_theme"):
                tab.set_theme(theme_name)
        persist_theme(theme_name)

    # ---------- zoom ----------
    def _zoom_editors(self, delta: int):
        """Método `MainWindow._zoom_editors`.
            Parâmetros: `self`, `delta`."""
        for i in range(self.editor_tabs.count()):
            tab = self.editor_tabs.widget(i)
            if tab is not None and hasattr(tab, "zoom"):
                tab.zoom(delta)

    def _reset_zoom_editors(self):
        """Método `MainWindow._reset_zoom_editors`.
            Parâmetros: `self`."""
        for i in range(self.editor_tabs.count()):
            tab = self.editor_tabs.widget(i)
            if tab is not None and hasattr(tab, "zoom_reset"):
                tab.zoom_reset()

    # ---------- fonte do sistema ----------
    def _apply_system_font(self):
        """Método `MainWindow._apply_system_font`.
            Parâmetros: `self`."""
        from PySide6.QtGui import QFont
        from PySide6.QtWidgets import QApplication

        app = QApplication.instance()
        base = self._base_app_font
        font = QFont(base.family(), max(6, round(base.pointSize() * self._system_font_scale)))
        font.setBold(self._base_app_font.bold())
        app.setFont(font)

    def _change_system_font(self, direction: int):
        """Método `MainWindow._change_system_font`.
            Parâmetros: `self`, `direction`."""
        from app.ui.editor.themes import ZOOM_STEP, persist_system_scale

        if direction > 0:
            self._system_font_scale = min(4.0, self._system_font_scale + ZOOM_STEP)
        else:
            self._system_font_scale = max(0.5, self._system_font_scale - ZOOM_STEP)
        self._apply_system_font()
        persist_system_scale(self._system_font_scale)

    def _reset_system_font(self):
        """Método `MainWindow._reset_system_font`.
            Parâmetros: `self`."""
        from app.ui.editor.themes import DEFAULT_SYSTEM_SCALE, persist_system_scale

        self._system_font_scale = DEFAULT_SYSTEM_SCALE
        self._apply_system_font()

    # ---------- r28 (T5179): escolha com preview ----------
    def _open_system_scale_dialog(self):
        """Método `MainWindow._open_system_scale_dialog`.
            Parâmetros: `self`."""
        from app.ui.widgets.scale_preview_dialog import SystemScaleDialog
        from app.ui.editor.themes import persist_system_scale

        dialog = SystemScaleDialog(self._system_font_scale, self)
        if dialog.exec() != QDialog.DialogCode.Accepted.value:
            self.set_status("Escala da fonte: cancelado (nada alterado).")
            return
        value = dialog.result_scale()
        self._system_font_scale = value
        self._apply_system_font()
        persist_system_scale(value)
        self.set_status(f"Escala da fonte do sistema: {round(value * 100)}% aplicada.")

    # ---------- r28 (T5180): teclado nos docks ----------
    def _setup_dock_shortcuts(self):
        """Método `MainWindow._setup_dock_shortcuts`.
            Parâmetros: `self`."""
        from PySide6.QtGui import QShortcut, QKeySequence

        self._dock_shortcuts = []
        for number in range(1, 10):
            sc = QShortcut(QKeySequence(f"Ctrl+{number}"), self)
            sc.setContext(Qt.ShortcutContext.WindowShortcut)
            sc.activated.connect(lambda checked=False, n=number: self._focus_dock_by_number(n))
            self._dock_shortcuts.append(sc)

    def _focus_dock_by_number(self, number: int) -> QDockWidget | None:
        """Ctrl+N: foca/ativa o N-ésimo dock (ordem determinística).

        Ordem em _dock_names(): 1=Variáveis, 2=Arquivos, 3=Experimentos,
        4=Matriz, 5=Histogramas, 6=Logs, 7=Fluxo. Retorna o dock (None se
        índice sem dock).
        """
        dock = list(self._dock_names().values())[number - 1] if 1 <= number <= len(self._dock_names()) else None
        if dock is None:
            return None
        dock.show()
        dock.raise_()
        widget = dock.widget()
        if widget is not None:
            widget.setFocus()
        self.set_status(f"Foco no dock {number}: {dock.windowTitle()}.")
        return dock

    # ---------- export batch ----------
    def _open_batch_export(self):
        """Método `MainWindow._open_batch_export`.
            Parâmetros: `self`."""
        container = self.container.ensure_services()
        batches = [row["id"] for row in container.exp_repo.list_batches(100)]
        versions = []
        for template_row in container.template_repo.list_templates():
            template_id = int(template_row["id"])
            versions_list = container.template_repo.list_versions(template_id)
            for version in versions_list:
                versions.append((int(version["id"]), f"template {template_id} — v{version['version_number']}"))
        if not batches:
            QMessageBox.information(
                self, "Sem experimentos", "Nenhum batch de experimentos salvo ainda."
            )
            return
        if not versions:
            QMessageBox.information(
                self, "Sem templates", "Salve um template para poder exportar."
            )
            return

        from pathlib import Path as _Path

        from app.ui.widgets.batch_export_dialog import BatchExportDialog

        default_output = _Path(self.container.base_dir) / "output"
        default_output.mkdir(parents=True, exist_ok=True)
        dialog = BatchExportDialog(
            batches, versions,
            last_output_root=str(getattr(self, "_last_output_root_used", None) or default_output),
            parent=self,
        )
        dialog.exportRequested.connect(self._start_batch_export)
        dialog.exec()

    def _start_batch_export(self, batch_id: str, version_id: int, output_root: str):
        """Método `MainWindow._start_batch_export`.
            Parâmetros: `self`, `batch_id`, `version_id`, `output_root`."""
        from PySide6.QtWidgets import QProgressDialog

        from app.workers.batch_export_worker import BatchExportWorker

        self._export_cancelled = False
        self._export_worker = BatchExportWorker(
            self.container.batch_export_service,
            batch_id,
            version_id,
            output_root,
            stop_check=lambda: self._export_cancelled,
        )

        progress_dialog = QProgressDialog("Exportando…", "Cancelar", 0, 100, self)
        progress_dialog.setWindowModality(Qt.WindowModality.WindowModal)
        progress_dialog.setMinimumDuration(0)
        progress_dialog.setValue(0)
        self._export_progress = progress_dialog

        progress_dialog.canceled.connect(lambda: setattr(self, "_export_cancelled", True))
        self._export_worker.progress.connect(progress_dialog.setValue)
        self._export_worker.progress.connect(self._update_status_progress)
        self._export_worker.completed.connect(self._on_batch_export_done)
        self._export_worker.failed.connect(self._on_batch_export_failed)
        self._export_worker.start()

    def _update_status_progress(self, percent: int):
        """Barra de execução inline na status bar (self.progress, sempre visível)."""
        self.progress.setValue(max(0, min(int(percent), 100)))

    def _on_batch_export_done(self, manifest):
        """Método `MainWindow._on_batch_export_done`.
            Parâmetros: `self`, `manifest`."""
        if hasattr(self, "_export_progress") and self._export_progress is not None:
            self._export_progress.cancel()
            self._export_progress.close()
        self.progress.setValue(100)
        container = self.container
        self._last_output_dir = str(manifest.output_dir)  # usado pelo sistema de estudos
        self.experiments_panel.set_last_output_dir(self._last_output_dir)
        from pathlib import Path as _Path

        # output_dir = <root>/<batch>/vN → root = pai do pai
        self._last_output_root_used = str(_Path(manifest.output_dir).parent.parent)
        self._last_template_version_id = getattr(manifest, "template_version_id", None)
        self._last_batch_id = getattr(manifest, "batch_id", getattr(self, "_last_batch_id", None))
        self.refresh_flow()
        self._notify_tray(
            "DAT Engineering Studio",
            f"Export concluído: {manifest.n_files} arquivos em {manifest.output_dir}",
        )
        container.log_service.audit(
            "export.done",
            f"{manifest.n_files} .dats em {manifest.output_dir}",
            payload={"output_dir": str(manifest.output_dir)},
        )
        from app.ui.widgets.export_done_dialog import ExportDoneDialog

        dialog = ExportDoneDialog(manifest.output_dir, manifest.n_files, manifest.manifest_path, self)
        dialog.exec()

    def _open_output_folder(self):
        """'Pasta output' no painel de experimentos."""
        path = getattr(self, "_last_output_dir", None)
        if not path:
            self.set_status("Nenhuma pasta de .dats ainda — gere os .dats primeiro.")
            return
        from PySide6.QtCore import QUrl
        from PySide6.QtGui import QDesktopServices

        QDesktopServices.openUrl(QUrl.fromLocalFile(str(path)))

    def _on_batch_export_failed(self, error: str):
        """Método `MainWindow._on_batch_export_failed`.
            Parâmetros: `self`, `error`."""
        if hasattr(self, "_export_progress") and self._export_progress is not None:
            self._export_progress.close()
        self.progress.setValue(0)
        QMessageBox.critical(self, "Erro na exportação", str(error))

    # ---------- eventos ----------
    def _wire_events(self):
        """Método `MainWindow._wire_events`.
            Parâmetros: `self`."""
        bus = self.container.event_bus
        self._restore_ui_choices()
        self._setup_dock_shortcuts()
        bus.subscribe(SamplingStartedEvent, lambda e: self.set_status("Amostragem iniciada…"))
        bus.subscribe(SamplingProgressEvent, lambda e: self.set_progress(e.percent, e.message))
        bus.subscribe(SamplingCompletedEvent, self._on_bus_sampling_completed)
        bus.subscribe(SamplingFailedEvent, lambda e: self.set_status(f"Erro: {e.error}"))
        bus.subscribe(
            TemplateDetectedEvent,
            lambda e: self.set_status(f"{len(e.var_ids)} variáveis detectadas"),
        )
        self.variables_panel.reloadDatRequested.connect(self._reload_dat_file)
        self.experiments_panel.saveTemplateRequested.connect(self._save_template_version)
        self.experiments_panel.generateDatsRequested.connect(self._open_batch_export)
        self.experiments_panel.openOutputRequested.connect(self._open_output_folder)
        self.files_panel.fileActivated.connect(self.editor_tabs.setCurrentIndex)
        self.files_panel.closeRequested.connect(self._close_editor_tab)
        self.files_panel.statusMessage.connect(self.set_status)
        self.files_panel.diffRequested.connect(self._open_files_diff)
        self.flow_panel.actionRequested.connect(self._on_flow_action)
        self.flow_panel.statusMessage.connect(self.set_status)
        self.flow_panel.refresh(self._flow_state())

        self.variables_panel.sampleRequested.connect(self._run_sampling)
        self.preview_panel.previewRequested.connect(self._run_preview)
        self.preview_panel.sideDiffRequested.connect(self._run_side_diff_preview)
        self.preview_panel.seedsBatchRequested.connect(self._run_seeds_batch_preview)
        self.experiments_panel.compareRequested.connect(self._compare_experiments)
        self.experiments_panel.compareTripleRequested.connect(
            self._compare_experiments_triple
        )
        self.experiments_panel.clearRequested.connect(self._confirm_clear_experiments)
        self.exp_model.modelReset.connect(
            lambda: (
                self.matrix_panel.load_from_repo(
                    self.container.exp_repo, self.exp_model.shown_var_ids
                ),
                self.hist_panel.load_from_repo(
                    self.container.exp_repo, self.exp_model.shown_var_ids
                ),
            )
        )
        self.editor_tabs.tab_dirty_changed.connect(
            lambda _i, dirty: self.set_status(
                "Alterações não salvas" if dirty else ""
            )
        )

    def _compare_experiments(self, id_a: int, id_b: int):
        """Método `MainWindow._compare_experiments`.
            Parâmetros: `self`, `id_a`, `id_b`."""
        self.container.ensure_services()
        text = self._current_text()
        try:
            from app.core.parsing import render_template

            renderer = (lambda t, v: render_template(t, v)) if text else None
            result = self.container.comparison_service.compare(
                id_a, id_b,
                template_text=text or None,
                renderer=renderer,
            )
            from app.ui.widgets.comparison_dialog import ComparisonDialog

            ComparisonDialog(result, self).exec()
        except Exception as exc:
            QMessageBox.critical(self, "Erro na comparação", str(exc))

    def _compare_experiments_triple(self, id_a: int, id_b: int, id_c: int):
        """T5438: compara A/B/C colocando a tabela tripla + scatter side."""
        self.container.ensure_services()
        try:
            from app.ui.widgets.triple_compare_dialog import TripleCompareDialog

            rows = []
            for label, exp_id in (("A", id_a), ("B", id_b), ("C", id_c)):
                fetched = self.container.comparison_service._fetch(exp_id)
                rows.append((label, dict(fetched["values"])))
            dialog = TripleCompareDialog(rows, self.container.comparison_service, self)
            dialog.set_scatter(rows[0][1].get(1, []), rows[1][1].get(1, []), "$1")
            dialog.exec()
        except Exception as exc:
            QMessageBox.critical(self, "Erro na comparação A/B/C", str(exc))

    # ---------- editor / variáveis ----------
    def _sync_variables(self, _index: int = 0):
        """Método `MainWindow._sync_variables`.
            Parâmetros: `self`, `_index`."""
        editor = self.editor_tabs.current_editor()
        if editor is None:
            return
        # Text principal + includes já lidos
        editor_text = editor.text() if editor else ""
        # Coleta variáveis com rastreamento de origem
        var_sources = self._collect_variables_with_sources(editor_text)
        self.variables_panel.update_tokens(var_sources)

    def _current_text(self) -> str:
        """Método `MainWindow._current_text`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        editor = self.editor_tabs.current_editor()
        return editor.text() if editor else ""

    # ---------- amostragem ----------
    def _run_sampling(self, specs: dict):
        """Método `MainWindow._run_sampling`.
            Parâmetros: `self`, `specs`."""
        text = self._current_text()
        if not text:
            QMessageBox.warning(self, "Sem template", "Abra um template primeiro.")
            return

        var_ids = find_variables(text)
        if not var_ids:
            QMessageBox.warning(self, "Sem variáveis", "Nenhum token $varN no template.")
            return

        specs_found: dict[int, DistributionSpec] = {
            var_id: spec
            for var_id, spec in specs.items()
            if var_id in var_ids
        }
        missing = [v for v in var_ids if v not in specs_found]
        if missing:
            QMessageBox.warning(
                self,
                "Distribuição ausente",
                f"Defina distribuições para: "
                f"{', '.join('$%d' % v for v in missing[:10])}",
            )
            return

        dialog = _SampleInputDialog(self)
        if getattr(self, "_pending_seed", None) is not None:
            self._prefill_seed_input(dialog)
        if dialog.exec() != dialog.DialogCode.Accepted:
            return
        n, strategy, workers, seed = dialog.result_values()
        self._pending_seed = None  # uso único

        from pathlib import Path as _Path

        plugins_dir = _Path(self.container.base_dir) / "plugins"
        request = SamplingRequest(
            var_ids=list(var_ids),
            specs=specs_found,
            n_experiments=n,
            strategy=strategy,
            workers=workers,
            seed=seed,
            plugins_dir=str(plugins_dir) if plugins_dir.exists() else None,
        )
        # r24: memoriza a última configuração p/ reexecução
        self._last_sampling_params = {
            "var_ids": list(var_ids),
            "specs": dict(specs_found),
            "n": n,
            "strategy": strategy,
            "workers": workers,
            "seed": seed,
        }
        self._launch_sampling(request)
        self.container.log_service.usage("sampling.run", f"{n} exps, {strategy}")
        self.set_status(
            f"Amostragem de {n} experimentos iniciada · seed={seed}"
        )

    def _launch_sampling(self, request):
        """Inicia o worker de amostragem (comum a run/reexecução — r24)."""
        from app.workers.sampling_worker import SamplingWorker

        self._worker = SamplingWorker(self.container.sampling_service, request)
        self._worker.progress.connect(lambda p, m: self.set_progress(p, m))
        self._worker.completed.connect(self._on_sampling_completed)
        self._worker.failed.connect(self._on_sampling_failed)
        self._worker.start()

    def _rerun_sampling(self, reuse_seed: bool):
        """r24: reexecuta a última amostragem sem reabrir o diálogo."""
        params = getattr(self, "_last_sampling_params", None)
        if not params:
            QMessageBox.information(
                self, "Reexecutar", "Amostre uma vez primeiro para guardar a configuração."
            )
            return
        if not reuse_seed:
            from random import SystemRandom

            params = dict(params, seed=SystemRandom().randrange(1, 2_147_483_647))
        request = SamplingRequest(
            var_ids=params["var_ids"],
            specs=params["specs"],
            n_experiments=params["n"],
            strategy=params["strategy"],
            workers=params["workers"],
            seed=params["seed"],
        )
        self._launch_sampling(request)
        self.set_status(
            f"Reexecutando amostragem ({params['n']} exps) · seed={params['seed']}"
        )

    # ---------- histórico de lotes (r25) ----------
    def _open_batch_history(self):
        """Método `MainWindow._open_batch_history`.
            Parâmetros: `self`."""
        from app.ui.widgets.batch_history_dialog import BatchHistoryDialog

        dialog = BatchHistoryDialog(self.container.exp_repo, parent=self)
        dialog.useRequested.connect(self._apply_pending_seed)
        dialog.exec()

    # ---------- plugins (r27) ----------
    def _open_plugins_dialog(self):
        """Método `MainWindow._open_plugins_dialog`.
            Parâmetros: `self`."""
        from app.ui.widgets.plugins_dialog import PluginsDialog

        container = self.container
        dialog = PluginsDialog(
            container.registry,
            container.plugin_report,
            parent=self,
            plugin_loader=container.plugin_loader,
        )
        dialog.exec()
        if container.plugin_loader is not None:
            container.plugin_report = container.plugin_loader._last_report  # noqa: SLF001

    def _apply_pending_seed(self, seed: int, dialog=None):
        """Guarda a seed para preencher o próximo diálogo de amostragem."""
        self._pending_seed = int(seed)
        self.set_status(
            f"Seed {seed} memorizada — será usada na próxima amostragem."
        )
        if dialog is not None:
            self._prefill_seed_input(dialog)

    def _prefill_seed_input(self, dialog):
        """Preenche o campo Seed do diálogo (testável com fake)."""
        pending = getattr(self, "_pending_seed", None)
        if pending is None:
            return False
        try:
            edit = dialog.edit_seed
        except AttributeError:
            return False
        edit.setText(str(pending))
        return True

    def _on_sampling_completed(self, result):
        """Método `MainWindow._on_sampling_completed`.
            Parâmetros: `self`, `result`."""
        self._notify_tray(
            "DAT Engineering Studio",
            f"Amostragem concluída: {len(result.matrix)} experimentos.",
        )
        incomplete = find_incomplete_variables(result)
        if incomplete:
            message = (
                "Todas as variáveis devem ter valores. "
                "Experimento não criado; variáveis sem valor: "
                + ", ".join(f"${v}" for v in incomplete[:10])
            )
            self.container.log_service.error("sampling.incomplete", message)
            QMessageBox.warning(self, "Amostragem incompleta", message)
            return

        self.last_sampling = result
        self.set_status(
            f"{len(result.matrix)} experimentos em {result.duration_seconds:.2f}s"
        )
        specs = self.variables_panel.specs
        names = {v: (specs[v].provider if v in specs else "?") for v in result.var_ids}
        for i in range(self.editor_tabs.count()):
            editor = self.editor_tabs.widget(i)
            if editor is not None:
                editor.set_variables(names)

        import time as _time

        batch_id = f"batch_{_time.strftime('%Y%m%d_%H%M%S')}"
        self._last_batch_id = batch_id  # usado pelo sistema de estudos
        self.container.exp_repo.create_batch(
            batch_id, method="sampling", seed=result.seed_used,
            n_experiments=len(result.matrix),
        )
        self.container.exp_repo.insert_result(batch_id, result.var_ids, result.matrix)
        self.exp_model.refresh()
        if getattr(self, "_open_study_id", None):  # T5444: estado atual → estudo
            try:
                version = self.container.study_service.register_batch(
                    self._open_study_id, batch_id, "amostragem da sessão"
                )
                self.set_status(f"Batch {batch_id} registrado no estudo (v{version}).")
            except Exception as exc:  # noqa: BLE001
                self.set_status(f"Aviso: batch não registrado no estudo ({exc}).")
        self.container.log_service.usage(
            "sampling.done", f"{len(result.matrix)} exps salvos em {batch_id}"
        )

    def _on_sampling_failed(self, error: str):
        """Método `MainWindow._on_sampling_failed`.
            Parâmetros: `self`, `error`."""
        QMessageBox.critical(self, "Erro na amostragem", str(error))

    def _notify_tray(self, title: str, message: str) -> None:
        """T5446: notificação na system tray de conclusão de tarefas.
        Silenciosa em ambientes sem tray (ex.: CI/offscreen)."""
        try:
            from PySide6.QtWidgets import QStyle, QSystemTrayIcon

            if not QSystemTrayIcon.isSystemTrayAvailable():
                return
            tray = getattr(self, "_tray", None)
            if tray is None:
                tray = QSystemTrayIcon(self)
                icon = self.style().standardIcon(QStyle.StandardPixmap.SP_ComputerIcon)
                tray.setIcon(icon)
                tray.setToolTip(self.windowTitle())
                self._tray = tray
            tray.show()
            tray.showMessage(title, message, QSystemTrayIcon.MessageIcon.Information)
        except Exception:
            return

    def _confirm_clear_experiments(self):
        """Método `MainWindow._confirm_clear_experiments`.
            Parâmetros: `self`."""
        answer = QMessageBox.question(
            self,
            "Limpar experimentos",
            "Apagar TODOS os experimentos e lotes gerados? Esta ação não pode ser desfeita.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if answer == QMessageBox.StandardButton.Yes:
            self._clear_experiments()

    def _clear_experiments(self):
        """Método `MainWindow._clear_experiments`.
            Parâmetros: `self`."""
        n_batches = self.container.exp_repo.clear_all()
        self.exp_model.refresh()
        self.container.log_service.audit(
            "experiments.clear", f"todos os experimentos apagados ({n_batches} lotes)"
        )
        self.set_status("Tabela de experimentos limpa.")

    # ---------- preview ----------
    def _run_preview(self, seed: int = 42):
        """Método `MainWindow._run_preview`.
            Parâmetros: `self`, `seed`."""
        text = self._current_text()
        if not text:
            return
        specs = self.variables_panel.specs or {}
        from app.services.preview_service import PreviewService

        svc = PreviewService(self.container.sampling_service)
        try:
            self.preview_panel.show_text(svc.render(text, specs, seed=seed))
        except Exception as exc:
            self.preview_panel.show_text(f"Erro: {exc}")

    def _run_side_diff_preview(self, seed_a: int, seed_b: int):
        """T5436: diff lado a lado das duas seeds do preview."""
        text = self._current_text()
        if not text:
            return
        specs = self.variables_panel.specs or {}
        from app.services.preview_service import PreviewService

        svc = PreviewService(self.container.sampling_service)
        try:
            ta = svc.render(text, specs, seed=seed_a)
            tb = svc.render(text, specs, seed=seed_b)
        except Exception as exc:
            self.preview_panel.show_text(f"Erro: {exc}")
            return
        self.preview_panel.show_side_by_side(ta, tb, seed_a, seed_b)

    def _run_seeds_batch_preview(self, base_seed: int):
        """T5437: preview para N seeds consecutivas com resumo de divergências."""
        text = self._current_text()
        if not text:
            return
        specs = self.variables_panel.specs or {}
        from app.services.preview_service import PreviewService
        from app.services.comparison_round34 import multi_seed_values, summarize_multi_seed

        svc = PreviewService(self.container.sampling_service)
        seeds = list(range(base_seed, base_seed + 10))
        try:
            pairs = multi_seed_values(svc.render, text, specs, seeds)
        except Exception as exc:
            self.preview_panel.show_text(f"Erro: {exc}")
            return
        summary = summarize_multi_seed(pairs)
        self.preview_panel.show_text(
            "\n".join(f"== seed {s} ==\n{t}" for s, t in pairs)
            + "\n\n--- resumo comparando com a seed base ---\n" + summary
        )

    # ---------- status ----------
    def set_status(self, message: str):
        """Método `MainWindow.set_status`.
            Parâmetros: `self`, `message`."""
        self._last_status = message
        self.status.showMessage(message, 5000)

    def status_message(self) -> str:
        """Última mensagem da barra de status (testável)."""
        return getattr(self, "_last_status", "")

    def set_progress(self, percent: int, message: str = ""):
        """Método `MainWindow.set_progress`.
            Parâmetros: `self`, `percent`, `message`."""
        self.progress.setValue(percent)
        self.progress.setFormat(f"{percent}% {message}")

    # ---------- encerramento ----------
    def closeEvent(self, event):
        """Método `MainWindow.closeEvent`.
            Parâmetros: `self`, `event`."""
        self.container.shutdown()
        super().closeEvent(event)
