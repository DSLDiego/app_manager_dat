from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QHBoxLayout,
    QLabel,
    QSlider,
    QSpinBox,
    QVBoxLayout,
)

from app.ui.editor.themes import MAX_FONT_SCALE, MIN_FONT_SCALE

PREVIEW_DEVICE_POINT = 14  # pt de referência p/ estimar o tamanho aplicado


class SystemScaleDialog(QDialog):
    """r28 (T5179): escolha da escala da fonte do sistema COM preview.

    Nada é aplicado no app até o aceite — o caller só persiste/chama
    _apply_system_font se exec() == Accepted (cancelar restaura nada,
    pois nada mudou). result_scale() devolve o valor como float clampado.
    """

    def __init__(self, current_scale: float = 1.0, parent=None):
        """Método `SystemScaleDialog.__init__`.
            Parâmetros: `self`, `current_scale`, `parent`."""
        super().__init__(parent)
        self.setWindowTitle("Escala da fonte do sistema — preview")
        self.setMinimumWidth(380)

        self._slider = QSlider(Qt.Orientation.Horizontal, self)
        self._slider.setRange(int(MIN_FONT_SCALE * 100), int(MAX_FONT_SCALE * 100))
        self._slider.setSingleStep(5)
        self._slider.valueChanged.connect(self._on_slider)

        self._spin = QSpinBox(self)
        self._spin.setRange(int(MIN_FONT_SCALE * 100), int(MAX_FONT_SCALE * 100))
        self._spin.setSuffix(" %")
        self._spin.valueChanged.connect(self._on_spin)

        self.lbl_preview = QLabel("Aa 123 — Template CMG $var1", self)
        self.lbl_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_preview.setMinimumHeight(48)

        self.btn_apply = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok
            | QDialogButtonBox.StandardButton.Cancel,
            parent=self,
        )
        self.btn_apply.accepted.connect(self.accept)
        self.btn_apply.rejected.connect(self.reject)

        row = QHBoxLayout()
        row.addWidget(self._spin)
        self._col = QVBoxLayout(self)
        self._col.addWidget(QLabel("Escala (100% = padrão do sistema):", self))
        self._col.addWidget(self._slider)
        self._col.addLayout(row)
        self._col.addWidget(self.lbl_preview)
        self._col.addWidget(self.btn_apply)

        self._set_value(float(current_scale))

    # ---------- API ----------
    def result_scale(self) -> float:
        """Método `SystemScaleDialog.result_scale`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        return round(self._slider.value() / 100.0, 2)

    def preview_point_size(self) -> int:
        """Método `SystemScaleDialog.preview_point_size`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        return max(6, round(PREVIEW_DEVICE_POINT * self.result_scale()))

    def preview_family(self) -> str:
        """Método `SystemScaleDialog.preview_family`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        return self.lbl_preview.font().family()

    # ---------- interno ----------
    def _set_value(self, scale: float):
        """Método `SystemScaleDialog._set_value`.
            Parâmetros: `self`, `scale`."""
        self._on_slider(int(round(max(MIN_FONT_SCALE, min(MAX_FONT_SCALE, scale)) * 100)))

    def _on_slider(self, percent: int):
        """Método `SystemScaleDialog._on_slider`.
            Parâmetros: `self`, `percent`."""
        self._slider.blockSignals(True)
        self._slider.setValue(percent)
        self._slider.blockSignals(False)
        self._spin.blockSignals(True)
        self._spin.setValue(percent)
        self._spin.blockSignals(False)
        self._update_preview(percent / 100.0)

    def _on_spin(self, percent: int):
        """Método `SystemScaleDialog._on_spin`.
            Parâmetros: `self`, `percent`."""
        self._on_slider(percent)

    def _update_preview(self, scale: float):
        """Método `SystemScaleDialog._update_preview`.
            Parâmetros: `self`, `scale`."""
        font = QFont()
        font.setPointSizeF(max(6.0, PREVIEW_DEVICE_POINT * scale))
        self.lbl_preview.setFont(font)
        self.lbl_preview.setText(
            f"Aa 123 — preview em {round(scale * 100)}% (a fonte real aplica após o OK)"
        )
