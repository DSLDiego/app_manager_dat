"""Formulário dinâmico universal: provider → distribuição → parâmetros."""

from __future__ import annotations

from typing import List, Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QDoubleSpinBox,
    QFormLayout,
    QLabel,
    QLineEdit,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)

from app.core.parsing import var_label
from app.domain.entities import DistributionSpec
from app.infrastructure.distribution_registry import DistributionRegistry


class DistributionDialog(QDialog):
    """Mostra apenas campos relevantes ao provider/distribuição escolhida."""

    def __init__(
        self,
        registry: DistributionRegistry,
        var_id: int,
        current: Optional[DistributionSpec] = None,
        parent=None,
    ):
        """Método `DistributionDialog.__init__`.
            Parâmetros: `self`, `registry`, `var_id`, `current`, `parent`."""
        super().__init__(parent)
        self.setWindowTitle(f"Variável {var_label(var_id)}")
        self.registry = registry
        self.var_id = var_id
        self._pending_dist = None
        self._pending_params = {}

        layout = QVBoxLayout(self)
        self.form = QFormLayout()
        layout.addLayout(self.form)

        self.combo_provider = QComboBox()
        self.combo_provider.addItems(registry.provider_names())
        self.combo_provider.currentTextChanged.connect(self._rebuild_dists)
        self.form.addRow("Provider:", self.combo_provider)

        self.combo_dist = QComboBox()
        self.combo_dist.currentTextChanged.connect(self._rebuild_fields)
        self.form.addRow("Distribuição:", self.combo_dist)
        self._widgets = []

        self.info_label = QLabel("")
        self.info_label.setWordWrap(True)
        self.form.addRow("", self.info_label)
        self._field_area = QWidget()
        self._field_form = QFormLayout(self._field_area)
        self.form.addRow(self._field_area)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        if current is not None:
            self.combo_provider.setCurrentText(current.provider)
            self._pending_dist = current.name
            self._pending_params = dict(current.params)
        self._rebuild_dists(self.combo_provider.currentText())

    # ---------- cascata ----------
    def _rebuild_dists(self, provider_name: str):
        """Método `DistributionDialog._rebuild_dists`.
            Parâmetros: `self`, `provider_name`."""
        provider = self.registry.get(provider_name)
        if provider is None:
            self.info_label.setText("Provider não encontrado.")
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
        """Método `DistributionDialog._rebuild_fields`.
            Parâmetros: `self`, `dist_name`."""
        while self._field_form.count():
            item = self._field_form.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        self._widgets = []

        provider = self.registry.get(self.combo_provider.currentText())
        if provider is None or not dist_name:
            return

        self.info_label.setText(getattr(provider, "description", ""))

        for param in provider.param_schema(dist_name):
            name = param["name"]
            default = param.get("default", 1.0)
            ptype = param.get("type", "float")
            if ptype == "int":
                widget = QSpinBox()
                widget.setRange(param.get("min", -10**6), param.get("max", 10**6))
                widget.setValue(int(self._pending_params.get(name, default)))
            else:
                widget = QDoubleSpinBox()
                widget.setDecimals(6)
                widget.setRange(param.get("min", -10**9), param.get("max", 10**9))
                widget.setValue(float(self._pending_params.get(name, default)))
            widget._param_type = ptype
            widget._param_name = name
            self._field_form.addRow(name, widget)
            self._widgets.append(widget)

        self._pending_params = {}

    # ---------- resultado ----------
    def collect(self) -> DistributionSpec:
        """Método `DistributionDialog.collect`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        params: dict[str, float] = {}
        for widget in self._widgets:
            value = widget.value()
            if getattr(widget, "_param_type", "float") == "int":
                value = int(value)
            params[widget._param_name] = value
        return DistributionSpec(
            provider=self.combo_provider.currentText(),
            name=self.combo_dist.currentText(),
            params=params,
        )
