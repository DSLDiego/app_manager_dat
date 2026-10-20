"""Matriz de experimentos (grade N×M) com células coloridas por escala da coluna.

Cada coluna de variável é normalizada min–max e pintada num gradiente azul
(baixa) → amarelo (alta), para leitura visual de padrões na amostragem.
"""

from __future__ import annotations

from typing import Optional

import numpy as np
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QFileDialog,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QMessageBox,
    QPushButton,
    QStackedWidget,
    QSpinBox,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from app.core.parsing import var_label
from app.services.statistics_service import StatisticsService
from app.ui.colors import PALETTES, color_with_palette


def two_batch_delta(repo, batch_a: str, batch_b: str):
    """T5440 (puro): delta b−a alinhado por posição do experimento.
    Retorna ({var_id: [deltas]}, n_linhas) comparando os dois batches."""
    out: dict[int, list[float]] = {}
    n = 0
    if repo is None:
        return out, 0
    grouped = {}
    for batch_id, tag in ((batch_a, "a"), (batch_b, "b")):
        rows = repo.conn.execute(
            """
            SELECT v.var_id AS var_id, v.value AS value
            FROM experiment_values v
            JOIN experiments e ON e.id = v.experiment_id
            WHERE e.batch_id = ?
            ORDER BY e.external_id, v.var_id
            """,
            (batch_id,),
        ).fetchall()
        per_var: dict[int, list[float]] = {}
        for r in rows:
            per_var.setdefault(int(r["var_id"]), []).append(float(r["value"]))
        grouped[tag] = per_var
    va, vb = grouped["a"], grouped["b"]
    for var_id in sorted(set(va) | set(vb)):
        a_, b_ = va.get(var_id, []), vb.get(var_id, [])
        m = min(len(a_), len(b_))
        n = max(n, m)
        deltas = [b_[i] - a_[i] for i in range(m)]
        if deltas:
            out[var_id] = deltas
    return out, n


def color_for_value(v: float, vmin: float, vmax: float, palette: Optional[str] = None) -> QColor:
    """Gradiente conforme paleta escolhida; default azul → amarelo."""
    from PySide6.QtGui import QColor as _QColor

    return _QColor(color_with_palette(v, vmin, vmax, palette or "azul→amarelo"))


class HeatMatrixPanel(QWidget):
    """Grade N experimentos × M variáveis, com heatmap por coluna.

    Formatos: normal (N×M), transposta (M×N) e 'Resumo por variável'
    (matriz M×5: n, média, σ, mín, máx). Tamanho de página e paleta ajustáveis.
    """

    DEFAULT_PAGE_SIZE = 120

    def __init__(self, parent=None):
        """Método `HeatMatrixPanel.__init__`.
            Parâmetros: `self`, `parent`."""
        super().__init__(parent)
        self.repo = None
        self._var_ids: list[int] = []
        self._page = 0
        self._transposed = False
        self._show_summary = False
        self._page_size = self.DEFAULT_PAGE_SIZE

        layout = QVBoxLayout(self)
        layout.setContentsMargins(6, 3, 6, 3)
        layout.setSpacing(2)
        header = QHBoxLayout()
        self.lbl_info = QLabel("Matriz sem dados")
        self.chk_transpose = QCheckBox("Transposta (variáveis × experimentos)")
        self.chk_transpose.setToolTip("Alterna os formatos de grade: experimento×variável ←→ variável×experimento.")
        self.chk_transpose.toggled.connect(self._on_transpose)
        self.spin_page_size = QSpinBox()
        self.spin_page_size.setRange(1, 1000)
        self.spin_page_size.setValue(self.DEFAULT_PAGE_SIZE)
        self.spin_page_size.setToolTip("Experimental por página (página de 1 eixo da grade).")
        self.spin_page_size.valueChanged.connect(self._on_page_size)
        self.chk_stretch = QCheckBox("Esticar colunas (grade uniforme)")
        self.chk_stretch.setToolTip("Formato n\u00d7m uniforme: todas as colunas com a mesma largura, ocupando 100% do painel.")
        self.chk_stretch.toggled.connect(self._on_stretch)
        self.combo_palette = QComboBox()
        self.combo_palette.addItems(list(PALETTES.keys()))
        self.combo_palette.setToolTip("Esquema de cores do heatmap.")
        self.combo_palette.currentTextChanged.connect(self._on_palette)
        self.btn_summary = QPushButton("Resumo por variável")
        self.btn_summary.setToolTip("Formato matriz M×5: n, média, σ, mín, máx por variável.")
        self.btn_summary.setCheckable(True)
        self.btn_summary.clicked.connect(self._on_summary)
        self.btn_export_png = QPushButton("Exportar PNG…")
        self.btn_export_png.setToolTip("Salva a grade de calor visível como imagem PNG.")
        self.btn_export_png.clicked.connect(self._export_png_dialog)
        btn_prev = QPushButton("◀")
        btn_next = QPushButton("▶")
        btn_prev.clicked.connect(self._prev)
        btn_next.clicked.connect(self._next)
        header.addWidget(self.lbl_info)
        header.addWidget(self.chk_stretch)
        header.addWidget(self.chk_transpose)
        header.addWidget(QLabel("por página:"))
        header.addWidget(self.spin_page_size)
        header.addStretch()
        header.addWidget(QLabel("cores:"))
        header.addWidget(self.combo_palette)
        header.addWidget(self.btn_summary)
        header.addWidget(self.btn_export_png)
        header.addWidget(btn_prev)
        header.addWidget(btn_next)
        layout.addLayout(header)

        self.lbl_legend = QLabel("Escala por variável: esquerda = menor, direita = maior")
        layout.addWidget(self.lbl_legend)

        self.stack = QStackedWidget()
        layout.addWidget(self.stack, 1)

        self.table = QTableWidget()
        self.table.setMinimumSize(150, 100)
        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents
        )
        self.table.verticalHeader().setVisible(True)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.stack.addWidget(self.table)

        self.summary_table = QTableWidget()
        self.summary_table.setMinimumSize(150, 100)
        self.summary_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents
        )
        self.summary_table.verticalHeader().setVisible(True)
        self.summary_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.stack.addWidget(self.summary_table)

    # ---------- dados ----------
    def load_delta_view(self, repo, batch_a: str, batch_b: str) -> int:
        """T5440: grade de delta (b−a) dos batches lado a lado. Retorna nº de linhas.
        Azul = b abaixo de a; vermelho = b acima; branco ≈ 0."""
        deltas, n = two_batch_delta(repo, batch_a, batch_b)
        all_values = [v for col in deltas.values() for v in col]
        vmax = max((abs(x) for x in all_values), default=0.0) or 1.0

        var_ids = sorted(deltas)
        headers = ["Δ"] + [var_label(v) for v in var_ids]
        grid: list[list[tuple[str, QColor]]] = []
        for i in range(n):
            cells = [(f"linha {i + 1}", QColor("#eef2f7"))]
            for var_id in var_ids:
                col = deltas.get(var_id, [])
                value = col[i] if i < len(col) else 0.0
                t = max(-1.0, min(1.0, value / vmax))
                if t > 0.02:
                    color = QColor(200 + int(50 * t), 235, 235 - int(120 * t))
                elif t < -0.02:
                    color = QColor(230, 235, 200 - int(-120 * t))
                else:
                    color = QColor(255, 255, 255)
                cells.append((f"{value:.4g}", color))
            grid.append(cells)

        self.stack.setCurrentIndex(0)
        self._show_summary = False
        self.table.setRowCount(len(grid))
        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(headers)
        for r, cells in enumerate(grid):
            for c, (text, color) in enumerate(cells):
                item = QTableWidgetItem(text)
                item.setBackground(color)
                self.table.setItem(r, c, item)
        self.lbl_info.setText(
            f"Δ batches '{batch_a}' → '{batch_b}' ({len(var_ids)}×{n})"
        )
        return n

    def load_from_repo(self, repo, var_ids: Optional[list[int]] = None):
        """Método `HeatMatrixPanel.load_from_repo`.
            Parâmetros: `self`, `repo`, `var_ids`."""
        self.repo = repo
        self._var_ids = list(var_ids) if var_ids else repo.var_ids()
        self._page = 0
        self._reload()

    def _on_stretch(self, checked: bool):
        """Grade uniforme: colunas esticam at\u00e9 preencher todo o painel."""
        mode = (
            QHeaderView.ResizeMode.Stretch
            if checked
            else QHeaderView.ResizeMode.ResizeToContents
        )
        self.table.horizontalHeader().setSectionResizeMode(mode)
        self.summary_table.horizontalHeader().setSectionResizeMode(mode)
        self._reload()

    def _on_transpose(self, checked: bool):
        """Método `HeatMatrixPanel._on_transpose`.
            Parâmetros: `self`, `checked`."""
        self._transposed = checked
        self._reload()

    def _on_page_size(self, value: int):
        """Método `HeatMatrixPanel._on_page_size`.
            Parâmetros: `self`, `value`."""
        self._page_size = int(value)
        self._page = 0
        self._reload()

    def _on_palette(self, name: str):
        """Método `HeatMatrixPanel._on_palette`.
            Parâmetros: `self`, `name`."""
        self._reload()

        # _on_summary permanece; hook abaixo
    def _on_summary(self, checked: bool):
        """Método `HeatMatrixPanel._on_summary`.
            Parâmetros: `self`, `checked`."""
        self._show_summary = bool(checked)
        self.stack.setCurrentIndex(1 if self._show_summary else 0)
        self._reload()

    # ---------- R30: exportar PNG ----------
    def export_png(self, path: str) -> bool:
        """Salva a grade visível (heatmap ou resumo) como PNG; False se vazia."""
        widget = self.stack.currentWidget()
        if widget is None or widget.rowCount() == 0 or widget.columnCount() == 0:
            return False
        pixmap = widget.grab()
        if pixmap.isNull():
            return False
        return bool(pixmap.save(str(path), "PNG"))

    def _export_png_dialog(self):
        """Método `HeatMatrixPanel._export_png_dialog`.
            Parâmetros: `self`."""
        if self.stack.currentWidget().rowCount() == 0:
            QMessageBox.information(self, "Exportar PNG", "Não há dados para exportar.")
            return
        path, _ = QFileDialog.getSaveFileName(
            self, "Exportar heatmap como PNG", "heatmap.png", "Imagem PNG (*.png)"
        )
        if not path:
            return
        if not path.lower().endswith(".png"):
            path += ".png"
        ok = self.export_png(path)
        if ok:
            QMessageBox.information(self, "Exportar PNG", f"Imagem salva em:\n{path}")
        else:
            QMessageBox.warning(self, "Exportar PNG", "Falha ao salvar a imagem.")

    def _reload(self):
        """Método `HeatMatrixPanel._reload`.
            Parâmetros: `self`."""
        if self._show_summary:
            self._reload_summary()
            return
        if self.repo is None or self.repo.count() == 0:
            self.table.setRowCount(0)
            self.table.setColumnCount(0)
            self.lbl_info.setText("Matriz sem dados")
            return
        rows = self.repo.fetch_page(self._page, self._page_size, self._var_ids)
        if self._var_ids:
            totals = self.repo.get_all_values_by_var(self._var_ids)
            mins = {v: float(np.min(totals.get(v, [0.0]))) for v in self._var_ids}
            maxs = {v: float(np.max(totals.get(v, [0.0]))) for v in self._var_ids}
        else:
            mins, maxs = {}, {}

        palette = self.combo_palette.currentText()
        color = lambda v, lo, hi: color_for_value(v, lo, hi, palette)

        # células normalizadas: lista [(texto, cor), ...] por linha
        grid_rows: list[list[tuple[str, QColor]]] = []

        if self._transposed:
            col_headers = ["Variável"] + [f"exp {row['external_id']}" for row in rows]
            for var_id in self._var_ids:
                row_cells: list[tuple[str, QColor]] = [
                    (var_label(var_id), QColor("#eef2f7"))
                ]
                for row in rows:
                    value = row["values"].get(var_id)
                    text = f"{value:.6g}" if value is not None else "—"
                    if value is not None:
                        row_cells.append((text, color(value, mins[var_id], maxs[var_id])))
                    else:
                        row_cells.append((text, QColor("#f7dcd4")))
                grid_rows.append(row_cells)
        else:
            col_headers = ["#"] + [var_label(v) for v in self._var_ids]
            for row in rows:
                row_cells: list[tuple[str, QColor]] = [
                    (str(row["external_id"]), QColor("#eef2f7"))
                ]
                for var_id in self._var_ids:
                    value = row["values"].get(var_id)
                    text = f"{value:.6g}" if value is not None else "—"
                    if value is not None:
                        row_cells.append((text, color(value, mins[var_id], maxs[var_id])))
                    else:
                        row_cells.append((text, QColor("#f7dcd4")))
                grid_rows.append(row_cells)

        self.table.setRowCount(len(grid_rows))
        self.table.setColumnCount(len(col_headers))
        self.table.setHorizontalHeaderLabels(col_headers)
        for r, cells in enumerate(grid_rows):
            for c, (text, color) in enumerate(cells):
                item = QTableWidgetItem(text)
                item.setBackground(color)
                self.table.setItem(r, c, item)

        total = self.repo.count()
        pages = max(1, (total + self._page_size - 1) // self._page_size)
        shape = (
            f"{len(self._var_ids)}×{len(rows)}"
            if self._transposed
            else f"{len(rows)}×{len(self._var_ids)}"
        )
        self.lbl_info.setText(f"Matriz {shape} — página {self._page + 1}/{pages}")

    def _prev(self):
        """Método `HeatMatrixPanel._prev`.
            Parâmetros: `self`."""
        if self.repo is None or self._page == 0:
            return
        self._page -= 1
        self._reload()
    def _next(self):
        """Método `HeatMatrixPanel._next`.
            Parâmetros: `self`."""
        if self.repo is None:
            return
        total_pages = max(1, (self.repo.count() + self._page_size - 1) // self._page_size)
        if self._page + 1 < total_pages:
            self._page += 1
            self._reload()

    # ---------- formato "Resumo por variável" (matriz M×stats) ----------
    _STAT_LABELS = ["n", "média", "σ", "mín", "máx"]

    def _reload_summary(self):
        """Método `HeatMatrixPanel._reload_summary`.
            Parâmetros: `self`."""
        if self.repo is None or self.repo.count() == 0 or not self._var_ids:
            self.summary_table.setRowCount(0)
            self.summary_table.setColumnCount(0)
            self.lbl_info.setText("Resumo sem dados")
            return
        service = StatisticsService()
        totals = self.repo.get_all_values_by_var(self._var_ids)
        rows: list[list[tuple[str, QColor]]] = []
        palette = self.combo_palette.currentText()

        # escala por coluna de estatística (por variável-colorida, coluna fixa)
        by_stat: dict[int, list[float]] = {i: [] for i in range(len(self._STAT_LABELS))}
        computed: list[tuple[int, list[float]]] = []
        for var_id in self._var_ids:
            values = totals.get(var_id, [])
            if not values:
                computed.append((var_id, [float("nan")] * len(self._STAT_LABELS)))
                continue
            stats = service.compute(var_id, values)
            computed.append(
                (
                    var_id,
                    [
                        float(stats.count),
                        stats.mean,
                        stats.std,
                        stats.minimum,
                        stats.maximum,
                    ],
                )
            )
            for i, stat_value in enumerate(computed[-1][1]):
                if np.isfinite(stat_value):
                    by_stat[i].append(stat_value)

        stat_hues = {
            i: (min(vals) if vals else 0.0, max(vals) if vals else 0.0)
            for i, vals in by_stat.items()
        }

        rows: list[list[tuple[str, QColor]]] = []
        for var_id, stats in computed:
            cells = [(var_label(var_id), QColor("#eef2f7"))]
            for i, stat_value in enumerate(stats):
                if not np.isfinite(stat_value):
                    cells.append(("—", QColor("#f7dcd4")))
                    continue
                lo, hi = stat_hues[i]
                cells.append((f"{stat_value:.6g}", color_for_value(stat_value, lo, hi, palette)))
            rows.append(cells)

        self.summary_table.setRowCount(len(rows))
        self.summary_table.setColumnCount(len(self._STAT_LABELS) + 1)
        self.summary_table.setHorizontalHeaderLabels(["Variável", *self._STAT_LABELS])
        for r, cells in enumerate(rows):
            for c, (text, color) in enumerate(cells):
                item = QTableWidgetItem(text)
                item.setBackground(color)
                self.summary_table.setItem(r, c, item)
        self.lbl_info.setText(
            f"Resumo {len(self._var_ids)}×{len(self._STAT_LABELS)} — n, média, σ, mín, máx"
        )
