"""Dialog secundário: define distribuições de probabilidade em lotes.

- mesma distribuição para TODAS as variáveis (1 clique)
- mesma distribuição para as variáveis SELECIONADAS (multi-seleção)
- limpar tudo
"""

from __future__ import annotations

from typing import Dict, Optional

from PySide6.QtCore import Signal
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDialog,
    QDoubleSpinBox,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from app.core.parsing import var_label
from app.domain.entities import DistributionSpec
from app.infrastructure.distribution_registry import DistributionRegistry
from app.services import spec_bulk_service


class DistributionBulkDialog(QDialog):
    """Janela secundária para definir dist. de prob em lote."""

    specsChanged = Signal(object)  # dict[int, DistributionSpec]
    statusMessage = Signal(str)

    def __init__(
        self,
        registry: DistributionRegistry,
        var_ids,
        specs: Optional[Dict[int, DistributionSpec]] = None,
        parent=None,
    ):
        """Método `DistributionBulkDialog.__init__`.
            Parâmetros: `self`, `registry`, `var_ids`, `specs`, `parent`."""
        super().__init__(parent)
        self.setWindowTitle("Distribuições em lote")
        self.setMinimumWidth(520)
        self.registry = registry
        self.var_ids = sorted(int(v) for v in var_ids)
        self.specs: Dict[int, DistributionSpec] = dict(specs or {})
        self._pending_dist = None
        self._pending_params = {}

        layout = QVBoxLayout(self)

        self.lbl_count = QLabel("")
        layout.addWidget(self.lbl_count)

        self.list_widget = QListWidget()
        self.list_widget.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        self._fill_list()
        layout.addWidget(self.list_widget)

        self.chk_all = QCheckBox("Aplicar em TODAS as variáveis (ignora seleção)")
        self.chk_all.setChecked(True)
        layout.addWidget(self.chk_all)

        form = QFormLayout()
        self.combo_provider = QComboBox()
        self.combo_provider.addItems(registry.provider_names())
        self.combo_provider.currentTextChanged.connect(self._rebuild_dists)
        form.addRow("Provider:", self.combo_provider)

        self.combo_dist = QComboBox()
        self.combo_dist.currentTextChanged.connect(self._rebuild_fields)
        form.addRow("Distribuição:", self.combo_dist)

        self.spin_fixed = QDoubleSpinBox()
        self.spin_fixed.setDecimals(6)
        self.spin_fixed.setRange(-10**9, 10**9)
        self.spin_fixed.setValue(1.0)
        form.addRow("Valor fixo:", self.spin_fixed)
        layout.addLayout(form)

        self._field_area = QWidget()
        self._field_form = QFormLayout(self._field_area)
        layout.addWidget(self._field_area)
        self._widgets = []

        buttons = QHBoxLayout()
        self.btn_apply = QPushButton("Aplicar")
        self.btn_apply.setDefault(True)
        self.btn_apply.clicked.connect(self._apply)
        self.btn_clear = QPushButton("Limpar todas as distribuições")
        self.btn_clear.clicked.connect(self._clear_all)
        self.btn_close = QPushButton("Fechar")
        self.btn_close.clicked.connect(self.reject)
        buttons.addWidget(self.btn_apply)
        buttons.addWidget(self.btn_clear)
        buttons.addStretch()
        buttons.addWidget(self.btn_close)
        layout.addLayout(buttons)

        self.combo_provider.setCurrentText("scipy")
        self._rebuild_dists(self.combo_provider.currentText())
        self.combo_dist.setCurrentText("norm")

    # ---------- listagem ----------
    def _fill_list(self):
        """Método `DistributionBulkDialog._fill_list`.
            Parâmetros: `self`."""
        self.list_widget.clear()
        for var_id in self.var_ids:
            spec = self.specs.get(var_id)
            suffix = f" → {spec.provider}.{spec.name}" if spec else " → (sem distribuição)"
            self.list_widget.addItem(f"{var_label(var_id)}{suffix}")
        total = len(self.var_ids)
        defined = sum(1 for v in self.var_ids if v in self.specs)
        self.lbl_count.setText(
            f"{total} variáveis — {defined} com distribuição "
            f"({spec_bulk_service.coverage(self.var_ids, self.specs):.0%} cobertas)"
        )

    # ---------- cascata provider → dist → campos ----------
    def _rebuild_dists(self, provider_name: str):
        """Método `DistributionBulkDialog._rebuild_dists`.
            Parâmetros: `self`, `provider_name`."""
        provider = self.registry.get(provider_name)
        if provider is None:
            return
        self.combo_dist.blockSignals(True)
        self.combo_dist.clear()
        self.combo_dist.addItems(provider.list_distributions())
        if self._pending_dist is not None:
            index = self.combo_dist.findText(self._pending_dist)
            if index >= 0:
                self.combo_dist.setCurrentIndex(index)
        self.combo_dist.blockSignals(False)
        self._rebuild_fields(self.combo_dist.currentText())

    def _rebuild_fields(self, dist_name: str):
        """Método `DistributionBulkDialog._rebuild_fields`.
            Parâmetros: `self`, `dist_name`."""
        while self._field_form.count():
            item = self._field_form.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        self._widgets = []
        provider = self.registry.get(self.combo_provider.currentText())
        if provider is None or not dist_name:
            return
        schema = (
            provider.param_schema(dist_name)
            if hasattr(provider, "param_schema")
            else []
        )
        for param in schema:
            name = param["name"]
            default = param.get("default", 1.0)
            widget = QDoubleSpinBox()
            widget.setDecimals(6)
            widget.setRange(-10**9, 10**9)
            widget.setValue(float(self._pending_params.get(name, default)))
            self._field_form.addRow(name, widget)
            self._widgets.append((name, widget))
        self._pending_params = {}

    # ---------- resultado ----------
    def collect(self) -> DistributionSpec:
        """Método `DistributionBulkDialog.collect`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        provider = self.combo_provider.currentText()
        name = self.combo_dist.currentText()
        if provider == "fixed" and name == "value":
            return spec_bulk_service.make_fixed_spec(self.spin_fixed.value())
        params = {n: w.value() for n, w in self._widgets}
        return DistributionSpec(provider=provider, name=name, params=params)

    def _targets(self):
        """Método `DistributionBulkDialog._targets`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        if self.chk_all.isChecked():
            return list(self.var_ids)
        return [
            self.var_ids[row]
            for row in range(self.list_widget.count())
            if self.list_widget.item(row).isSelected()
        ]

    def _apply(self):
        """Método `DistributionBulkDialog._apply`.
            Parâmetros: `self`."""
        targets = self._targets()
        if not targets:
            self.statusMessage.emit("Selecione ao menos uma variável (ou marque 'todas').")
            return
        spec = self.collect()
        self.specs = spec_bulk_service.apply_spec_to_selected(self.specs, targets, spec)
        self._fill_list()
        self.specsChanged.emit(dict(self.specs))
        self.statusMessage.emit(f"{len(targets)} variáveis → {spec.provider}.{spec.name}")

    def _clear_all(self):
        """Método `DistributionBulkDialog._clear_all`.
            Parâmetros: `self`."""
        self.specs = spec_bulk_service.clear_specs(self.specs)
        self._fill_list()
        self.specsChanged.emit(dict(self.specs))
        self.statusMessage.emit("Distribuições limpas.")
