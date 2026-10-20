"""Grade n×m de mini-histogramas (small multiples) — um por variável amostrada.

Novo formato de matriz visual: cada célula mostra o histograma da variável
em QPainter puro (sem matplotlib). Paginação: 12 células por página (4×3).
"""

from __future__ import annotations

from typing import Optional

import numpy as np
from PySide6.QtCore import QPointF, QRectF, Qt
from PySide6.QtGui import QColor, QPainter, QPen
from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from app.core.parsing import var_label
from app.ui.colors import PALETTES, color_with_palette


def histogram_bins(values, bins: int = 20):
    """[(centro, altura_normalizada), ...] do histograma da variável."""
    arr = np.asarray(values, dtype=float)
    arr = arr[np.isfinite(arr)]
    if arr.size == 0:
        return [], 0
    counts, edges = np.histogram(arr, bins=bins)
    centers = (edges[:-1] + edges[1:]) / 2.0
    total = counts.sum()
    if total == 0:
        return [], 0
    heights = counts / total
    return list(zip(centers.tolist(), heights.tolist())), int(total)


def normal_curve(values, bins: int = 20, n: int = 64):
    """(xs, ys) curva normal ajustada na escala do histograma — puro.

    ys já multiplicado pela largura do bin p/ casar com as alturas
    normalizadas de histogram_bins(). Sem dados suficientes ⇒ ([], []).
    """
    arr = np.asarray(values, dtype=float)
    arr = arr[np.isfinite(arr)]
    if arr.size < 3:
        return [], []
    mu = float(arr.mean())
    sd = float(arr.std())
    if sd < 1e-15:
        return [], []
    lo, hi = float(arr.min()), float(arr.max())
    pad = (hi - lo) * 0.05 or 1.0
    xs = np.linspace(lo - pad, hi + pad, n)
    bin_w = (hi - lo) / max(1, bins)
    ys = np.exp(-0.5 * ((xs - mu) / sd) ** 2) / (sd * np.sqrt(2 * np.pi)) * bin_w
    return xs.tolist(), ys.tolist()


class MiniHistogram(QWidget):
    """Célula: barras + rótulo '$varN (n=…)' + eixo base + curva normal opcional."""

    def __init__(self, var_id: int = 0, parent=None):
        """Método `MiniHistogram.__init__`.
            Parâmetros: `self`, `var_id`, `parent`."""
        super().__init__(parent)
        self.setMinimumSize(160, 110)
        self.var_id = var_id
        self._bins: list[(float, float)] = []
        self._n = 0
        self._vmin = 0.0
        self._vmax = 1.0
        self._values: list = []
        self.show_fit = False
        self.setPaletteName("azul→amarelo")

    def setPaletteName(self, name: str):
        """Método `MiniHistogram.setPaletteName`.
            Parâmetros: `self`, `name`."""
        self._palette = name

    def set_show_fit(self, show: bool):
        """Método `MiniHistogram.set_show_fit`.
            Parâmetros: `self`, `show`."""
        self.show_fit = bool(show)
        self.update()

    def set_values(self, values, bins: int = 20):
        """Método `MiniHistogram.set_values`.
            Parâmetros: `self`, `values`, `bins`."""
        self._values = list(values) if values is not None else []
        self._bins, self._n = histogram_bins(self._values, bins)
        if self._bins:
            self._vmin = min(c for c, _ in self._bins)
            self._vmax = max(c for c, _ in self._bins)
            if self._vmax - self._vmin < 1e-15:
                self._vmax = self._vmin + 1e-15
        self.update()

    def paintEvent(self, event):
        """Método `MiniHistogram.paintEvent`.
            Parâmetros: `self`, `event`."""
        painter = QPainter(self)
        painter.fillRect(0, 0, self.width(), self.height(), QColor("#ffffff"))

        label_rect = QRectF(2, 0, self.width() - 4, 18)
        painter.setPen(QPen(QColor("#333333")))
        painter.drawText(
            label_rect, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter,
            f"{var_label(self.var_id)}  (n={self._n})",
        )

        top = 20.0
        margin_b = 6.0
        plot_height = self.height() - top - margin_b
        plot = QRectF(4, top, self.width() - 8, plot_height)

        if not self._bins:
            painter.setPen(QPen(QColor("#aaaaaa")))
            painter.drawText(plot, Qt.AlignmentFlag.AlignCenter, "sem valores")
            return
        if self._n == 1:
            painter.setPen(QPen(QColor("#aaaaaa")))
            painter.drawText(plot, Qt.AlignmentFlag.AlignCenter, "único valor")
            return

        painter.setBrush(Qt.BrushStyle.NoBrush)
        width = plot.width() / len(self._bins)
        for index, (center, height) in enumerate(self._bins):
            bar_height = height * plot.height()
            color = color_with_palette(center, self._vmin, self._vmax, self._palette)
            painter.setBrush(QColor(color))
            painter.setPen(Qt.PenStyle.NoPen)
            x = plot.left() + index * width
            painter.fillRect(
                QRectF(x + 1, plot.bottom() - bar_height, max(2.0, width - 2), bar_height),
                QColor(color),
            )
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.setPen(QPen(QColor("#999999"), 1))
        painter.drawLine(
            QPointF(plot.left(), plot.bottom()), QPointF(plot.right(), plot.bottom())
        )

        # r19: curva normal ajustada sobreposta (opcional)
        if self.show_fit:
            xs, ys = normal_curve(self._values, bins=len(self._bins) or 20)
            if xs and ys:
                lo, hi = min(xs), max(xs)
                painter.setPen(QPen(QColor("#c0392b"), 1.6))
                prev = None
                for x, y in zip(xs, ys):
                    px = plot.left() + (x - lo) / max(1e-15, hi - lo) * plot.width()
                    py = plot.bottom() - min(1.0, y) * plot.height()
                    if prev is not None:
                        painter.drawLine(prev, QPointF(px, py))
                    prev = QPointF(px, py)


class HistogramGridPanel(QWidget):
    """Dock "Histogramas por variável": grade n×m paginada (2/3/4/6 colunas), paleta compartilhada."""

    ROWS_PER_PAGE = 3

    @classmethod
    def cells_per_page(cls, cols: int) -> int:
        """Método `HistogramGridPanel.cells_per_page`.
            Parâmetros: `cls`, `cols`.
            Retorna o resultado calculado a partir do estado local."""
        return max(1, int(cols or 4)) * cls.ROWS_PER_PAGE

    @staticmethod
    def grid_layout(n_items: int, cols: int = 4):
        """(linhas_totais, cols, células_por_página) — lógica de grade n×m pura."""
        cols = max(1, int(cols or 4))
        rows = HistogramGridPanel.ROWS_PER_PAGE
        cells = cols * rows
        pages = max(1, (n_items + cells - 1) // cells)
        return pages * rows, cols, cells

    def __init__(self, parent=None):
        """Método `HistogramGridPanel.__init__`.
            Parâmetros: `self`, `parent`."""
        super().__init__(parent)
        self.repo = None
        self._var_ids: list[int] = []
        self._page = 0
        self._cols = 4
        self._palette_name = "azul→amarelo"
        self._show_fit = False

        layout = QVBoxLayout(self)
        layout.setContentsMargins(6, 3, 6, 3)
        layout.setSpacing(2)
        header = QHBoxLayout()
        self.lbl_info = QLabel("Histogramas sem dados")
        self.combo = QComboBox()
        self.combo.addItems(list(PALETTES.keys()))
        self.combo.setToolTip("Esquema de cores dos histogramas.")
        self.combo.currentTextChanged.connect(self._on_palette)
        self.combo_cols = QComboBox()
        self.combo_cols.addItems([str(c) for c in (2, 3, 4, 6)])
        self.combo_cols.setCurrentText("4")
        self.combo_cols.setToolTip("Colunas da grade n×m de histogramas (2 a 6).")
        self.combo_cols.currentTextChanged.connect(self._on_cols)
        btn_prev = QPushButton("◀")
        btn_next = QPushButton("▶")
        btn_prev.clicked.connect(self._prev)
        btn_next.clicked.connect(self._next)
        header.addWidget(self.lbl_info)
        header.addStretch()
        header.addWidget(QLabel("colunas:"))
        header.addWidget(self.combo_cols)
        header.addWidget(QLabel("cores:"))
        header.addWidget(self.combo)
        self.btn_flow = QPushButton("Fluxo")
        self.btn_flow.setToolTip("Mostra a cadeia var1 → var2 → var3 como fluxo de mini-histogramas.")
        self.btn_flow.clicked.connect(self._open_flow)
        header.addWidget(self.btn_flow)
        from PySide6.QtWidgets import QCheckBox

        self.chk_fit = QCheckBox("Curva normal")
        self.chk_fit.setToolTip("Sobrepõe a curva normal ajustada (média/desvio dos dados) em cada histograma.")
        self.chk_fit.toggled.connect(self.set_show_fit_all)
        header.addWidget(self.chk_fit)
        self.btn_png = QPushButton("Salvar página (PNG)")
        self.btn_png.setToolTip("Salva a página atual da grade de histogramas como imagem.")
        self.btn_png.clicked.connect(self._save_page_png)
        header.addWidget(self.btn_png)
        header.addWidget(btn_prev)
        header.addWidget(btn_next)
        layout.addLayout(header)

        self.table = QTableWidget()
        self.table.setMinimumSize(150, 100)
        self.table.horizontalHeader().setVisible(False)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.table.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        layout.addWidget(self.table)

    # ---------- dados ----------
    def load_from_repo(self, repo, var_ids: Optional[list[int]] = None):
        """Método `HistogramGridPanel.load_from_repo`.
            Parâmetros: `self`, `repo`, `var_ids`."""
        self.repo = repo
        self._var_ids = sorted(int(v) for v in (var_ids if var_ids else repo.var_ids()))
        self._page = 0
        self._reload()

    def set_values_map(self, values_map: dict):
        """Alternativa sem repositório (útil em testes): {var_id: [valores]}."""
        self._var_ids = sorted(values_map)
        if self.repo is None:
            self._reload(values_map)
        else:
            self._reload()

    def _cells(self) -> int:
        """Método `HistogramGridPanel._cells`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        return max(1, self._cols) * self.ROWS_PER_PAGE

    def _current_ids(self) -> list:
        """Método `HistogramGridPanel._current_ids`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        start = self._page * self._cells()
        return self._var_ids[start : start + self._cells()]

    def _total_pages(self) -> int:
        """Método `HistogramGridPanel._total_pages`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        cells = self._cells()
        return max(1, (len(self._var_ids) + cells - 1) // cells)

    def _reload(self, values_map: Optional[dict] = None):
        """Método `HistogramGridPanel._reload`.
            Parâmetros: `self`, `values_map`."""
        if self._var_ids == []:
            self.table.setRowCount(0)
            self.table.setColumnCount(0)
            self.lbl_info.setText("Histogramas sem dados")
            return

        slots = [None] * self._cells()
        for i, var_id in enumerate(self._current_ids()):
            values = None
            if values_map is not None:
                values = values_map.get(var_id)
            elif self.repo is not None:
                values = self.repo.get_variable_values(var_id)
            slots[i] = (var_id, values)

        self.table.setRowCount(self.ROWS_PER_PAGE)
        self.table.setColumnCount(self._cols)
        total_pages = self._total_pages()
        self.lbl_info.setText(
            f"Variáveis {len(self._var_ids)} — página {self._page + 1}/{total_pages}"
        )

        for i, slot in enumerate(slots):
            r, c = divmod(i, self._cols)
            var_id = None if slot is None else slot[0]
            if var_id is None:
                self.table.removeCellWidget(r, c)
                self.table.setItem(r, c, QTableWidgetItem(""))
                continue
            cell = self.table.cellWidget(r, c)
            if not isinstance(cell, MiniHistogram):
                cell = MiniHistogram(var_id)
                self.table.setCellWidget(r, c, cell)
            cell.var_id = var_id
            cell.setPaletteName(self._palette_name)
            cell.set_show_fit(self._show_fit)
            if slot[1]:
                cell.set_values(slot[1])

    def _on_palette(self, name: str):
        """Método `HistogramGridPanel._on_palette`.
            Parâmetros: `self`, `name`."""
        self._palette_name = name
        self._reload()

    def set_show_fit_all(self, show: bool):
        """'Curva normal' no header — aplica nas células existentes e futuras."""
        self._show_fit = bool(show)
        for i in range(self.table.rowCount()):
            for j in range(self.table.columnCount()):
                cell = self.table.cellWidget(i, j)
                if isinstance(cell, MiniHistogram):
                    cell.set_show_fit(self._show_fit)

    def _save_page_png(self):
        """'Salvar página (PNG)' — snapshot da grade atual."""
        from PySide6.QtWidgets import QFileDialog

        path, _ = QFileDialog.getSaveFileName(
            self, "Salvar página de histogramas", "histogramas.png", "PNG (*.png)"
        )
        if not path:
            return
        if not path.lower().endswith(".png"):
            path += ".png"
        ok = self.table.grab().save(path, "PNG")
        self.lbl_info.setText(
            f"PNG salvo: {path}" if ok else "Falha ao salvar PNG."
        )

    def _prev(self):
        """Método `HistogramGridPanel._prev`.
            Parâmetros: `self`."""
        if self._page > 0:
            self._page -= 1
            self._reload()

    def _on_cols(self, text: str):
        """Método `HistogramGridPanel._on_cols`.
            Parâmetros: `self`, `text`."""
        try:
            self._cols = max(2, min(6, int(text)))
        except (TypeError, ValueError):
            self._cols = 4
        self._page = 0
        self._reload()

    def _next(self):
        """Método `HistogramGridPanel._next`.
            Parâmetros: `self`."""
        total = self._total_pages()
        if self._page + 1 < total:
            self._page += 1
            self._reload()

    def _flow_values_map(self) -> dict:
        """Dados para o fluxo — todas as variáveis amostradas."""
        values_map = {}
        for var_id in self._var_ids:
            if self.repo is not None:
                values_map[var_id] = self.repo.get_variable_values(var_id)
        return values_map

    def _open_flow(self):
        """Método `HistogramGridPanel._open_flow`.
            Parâmetros: `self`."""
        n_stages = self._flow_values_map()
        if not n_stages:
            from PySide6.QtWidgets import QMessageBox

            QMessageBox.information(self, "Sem dados", "Amostrar experimentos primeiro.")
            return
        from PySide6.QtWidgets import QDialog, QVBoxLayout

        from app.ui.widgets.hist_flow_view import HistFlowView

        dlg = QDialog(self)
        dlg.setWindowTitle("Histogramas — fluxo var1 → var2 → …")
        lay = QVBoxLayout(dlg)
        lay.setContentsMargins(6, 6, 6, 6)
        view = HistFlowView()
        n = view.set_values_map(n_stages)
        lay.addWidget(view)
        dlg.resize(min(1200, 170 + 160 * max(1, n)), 220)
        dlg.exec()
