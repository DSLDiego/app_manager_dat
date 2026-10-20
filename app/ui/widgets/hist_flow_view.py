"""Histogramas em formato fluxo — cadeia horizontal var1 → var2 → var3 → …

Cada estágio é um mini-gráfico de barras da distribuição daquela variável;
setas ligam os estágios. Ordem: pure `flow_order(var_ids)` (ordem natural).
Reaproveita os dados do HistogramGridPanel (repo.get_variable_values).
"""

from __future__ import annotations

import numpy as np
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from app.core.parsing import var_label
from app.ui.widgets.distribution_plot_dialog import PlotCanvas

ARR = "\u2192"  # →
MAX_FLOW_STAGES = 8


def flow_order(var_ids: list[int]) -> list[int]:
    """Ordem da cadeia do fluxo — puro (ordem natural, clampado)."""
    return list(var_ids)[:MAX_FLOW_STAGES]


def hist_values(values: list | None, bins: int = 12) -> tuple[list, list]:
    """Valores contínuos → (centros, contagens) — puro, sem dados ⇒ ([],[])."""
    if not values:
        return [], []
    xs = np.asarray([float(v) for v in values], dtype=float)
    counts, edges = np.histogram(xs, bins=min(bins, max(2, xs.size)))
    centers = [(float(a) + float(b)) / 2.0 for a, b in zip(edges[:-1], edges[1:])]
    return centers, [int(c) for c in counts]


class HistFlowView(QWidget):
    """Fluxo horizontal de histogramas ligados por setas."""

    def __init__(self, parent=None):
        """Método `HistFlowView.__init__`.
            Parâmetros: `self`, `parent`."""
        super().__init__(parent)
        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(2)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        from PySide6.QtWidgets import QFrame as _QFrame

        self.scroll.setFrameShape(_QFrame.Shape.NoFrame)
        outer.addWidget(self.scroll, 1)

        self.stage_strip = QWidget()
        self.strip_layout = QHBoxLayout(self.stage_strip)
        self.strip_layout.setContentsMargins(6, 4, 6, 4)
        self.strip_layout.setSpacing(2)
        self.scroll.setWidget(self.stage_strip)

        self.lbl_note = QLabel("")
        outer.addWidget(self.lbl_note)
        self._stages: list[tuple[int, PlotCanvas, QLabel]] = []

    def set_values_map(self, values_map: dict) -> int:
        """Monta a cadeia — retorna nº de estágios."""
        while self.strip_layout.count():
            item = self.strip_layout.takeAt(0)
            w = item.widget()
            if w is not None:
                w.deleteLater()
        self._stages.clear()
        ids = flow_order(sorted(values_map))
        for i, var_id in enumerate(ids):
            centers, counts = hist_values(values_map.get(var_id))
            stage = PlotCanvas()
            stage.mode = "bar"
            stage.set_title(var_label(var_id)[:24])
            stage.set_labels(var_label(var_id), "n")
            if centers:
                stage.add_series(var_label(var_id), np.asarray(centers), np.asarray(counts, dtype=float), True)
            stage.setMinimumSize(150, 120)
            self.strip_layout.addWidget(stage, 1)
            if i < len(ids) - 1:
                arrow = QLabel(ARR)
                arrow.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.strip_layout.addWidget(arrow)
            self._stages.append((var_id, stage))
        if len(values_map) > MAX_FLOW_STAGES:
            self.lbl_note.setText(f"fluxo: só as primeiras {MAX_FLOW_STAGES} variáveis")
        else:
            self.lbl_note.setText("")
        return len(ids)


def arrow_next_label(centers: list) -> str:
    """Rótulo das setas: faixa estimada entre estágios — puro, opcional."""
    if len(centers) < 2:
        return ARR
    return ARR
