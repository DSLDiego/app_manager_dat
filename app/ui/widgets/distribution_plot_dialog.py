"""Plot de distribuições (linha/barras) e de função definida pelo usuário.

Renderiza com QPainter — zero dependência de matplotlib.
"""

from __future__ import annotations

import ast
import math
from typing import Callable, Optional

import numpy as np
from PySide6.QtCore import QPointF, QRectF, Qt
from PySide6.QtGui import QColor, QPainter, QPen, QPaintDevice

from app.ui.colors import palette_gradient

_SERIES_COLORS = tuple(palette_gradient("roxo\u2192verde", steps=9))
from PySide6.QtWidgets import (
    QComboBox,
    QDialog,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)

_SAFE_NAMES = {
    "np": np, "math": math,
    "abs": abs, "min": min, "max": max, "round": round, "exp": np.exp,
    "log": np.log, "sqrt": np.sqrt, "sin": np.sin, "cos": np.cos,
    "tan": np.tan, "pi": np.pi, "e": np.e,
}


# ---------- avaliação segura de f(x) ----------
_ALLOWED_NAMES = {
    "x", "np", "math", "abs", "min", "max", "round",
    "exp", "log", "log10", "sqrt", "sin", "cos", "tan",
    "asin", "acos", "atan", "sinh", "cosh", "tanh", "pi", "e",
}
_ALLOWED_LOS = {"np", "math"}


def safe_eval_function(expr: str) -> Callable[[np.ndarray], np.ndarray]:
    """Compila f(x) do usuário com escopo fechado.

    - blocos: import/from ( SyntaxError cai no validate_function )
    - atributo apenas em np.* / math.*
    - qualquer identificador fora da whitelist é rejeitado
    """
    tree = ast.parse(expr, mode="eval")
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            raise ValueError("Expressão não permitida (import bloqueado)")
        if isinstance(node, ast.Attribute):
            base = node
            while isinstance(base, ast.Attribute):
                base = base.value
            if not (isinstance(base, ast.Name) and base.id in _ALLOWED_LOS):
                raise ValueError("Acesso a atributo só é permitido em np.* / math.*")
        if isinstance(node, ast.Name) and node.id not in _ALLOWED_NAMES:
            raise ValueError(f"Identificador não permitido: '{node.id}'")
    code = compile(tree, "<f(x)>", "eval")

    def f(xs: np.ndarray) -> np.ndarray:
        """Função `f`.
            Parâmetros: `xs`.
            Retorna o resultado calculado a partir do estado local."""
        x = np.asarray(xs, dtype=float)
        local_env = dict(_SAFE_NAMES)
        local_env["x"] = x
        with np.errstate(all="ignore"):
            y = eval(code, {"__builtins__": {}}, local_env)
        return np.asarray(y, dtype=float)

    return f


def validate_function(expr: str) -> Optional[str]:
    """Função `validate_function`.
        Parâmetros: `expr`.
        Retorna o resultado calculado a partir do estado local."""
    try:
        f = safe_eval_function(expr)
        f(np.array([0.0, 1.0, 2.0]))
    except ValueError as exc:
        return str(exc)
    except Exception as exc:  # noqa: BLE001
        return f"Erro na expressão: {exc}"
    return None


# ---------- canvas ----------
def format_tick(value: float) -> str:
    """Tick compacto: 1234→'1.2k', 0.0012→'1.2m', −56.789→'−56.8'."""
    if value == 0:
        return "0"
    a = abs(value)
    if a >= 1_000_000:
        return f"{value / 1_000_000:.1f}M"
    if a >= 1_000:
        return f"{value / 1_000:.1f}".rstrip("0").rstrip(".") + "k"
    if a >= 1:
        return f"{value:.2f}".rstrip("0").rstrip(".")
    if a >= 0.001:
        return f"{value * 1_000:.1f}m"
    return f"{value:.2e}"


def zoom_span(lo: float, hi: float, factor: float) -> tuple[float, float]:
    """Amplia (factor<1 aproxima) mantendo o centro — puro, testável."""
    mid = (lo + hi) / 2.0
    half = (hi - lo) * factor / 2.0
    return mid - half, mid + half


def pan_span(lo: float, hi: float, frac: float) -> tuple[float, float]:
    """Desloca a janela por frac do próprio tamanho (frac>0 → direita) — puro."""
    span = hi - lo
    return lo + frac * span, hi + frac * span


def zoom_at(lo: float, hi: float, frac: float, factor: float) -> tuple[float, float]:
    """Amplia mantendo o ponto `frac` (0..1 horizontal) fixo — puro."""
    anchor = lo + frac * (hi - lo)
    lo2, hi2 = zoom_span(lo, hi, factor)
    frac2 = frac if (hi - lo) < 1e-12 else frac
    anchor2 = lo2 + frac2 * (hi2 - lo2)
    shift = anchor - anchor2
    return lo2 + shift, hi2 + shift


def clamp_zoom(lo: float, hi: float, lo0: float, hi0: float, min_frac: float = 0.002) -> tuple[float, float]:
    """Impede zoom além de min_frac do total ou afastar além dos dados — puro."""
    span0 = hi0 - lo0
    if hi - lo > span0:
        return lo0, hi0
    if (hi - lo) / span0 < min_frac:
        mid = (lo + hi) / 2.0
        half = span0 * min_frac / 2.0
        return mid - half, mid + half
    return lo, hi


def compute_ticks(xmin: float, xmax: float, n: int = 5) -> list:
    """n valores igualmente espaçados no eixo X (usados nas linhas da grade)."""
    if xmax - xmin < 1e-12:
        return [xmin] * n
    return [xmin + (xmax - xmin) * i / (n - 1) for i in range(n)]


class PlotCanvas(QWidget):
    """Série como linha ou barras; grade n×m de ticks nos eixos."""

    def __init__(self, parent=None):
        """Método `PlotCanvas.__init__`.
            Parâmetros: `self`, `parent`."""
        super().__init__(parent)
        self.setMinimumHeight(260)
        self._series: list[tuple[str, np.ndarray, np.ndarray, bool]] = []
        self._xlabel = "x"
        self._ylabel = "f"
        self._title = ""
        self.mode = "line"  # "line" | "bar"
        self._zoom: tuple[float, float, float, float] | None = None  # xmin,xmax,ymin,ymax
        self._drag_x0: int | None = None
        self._drag_zoom0: tuple | None = None

    def set_title(self, title: str):
        """Método `PlotCanvas.set_title`.
            Parâmetros: `self`, `title`."""
        self._title = title
        self.update()

    def set_mode(self, mode: str):
        """Método `PlotCanvas.set_mode`.
            Parâmetros: `self`, `mode`."""
        self.mode = mode
        self.update()

    def clear_series(self):
        """Método `PlotCanvas.clear_series`.
            Parâmetros: `self`."""
        self._series = []
        self.update()

    def add_series(self, label: str, xs: np.ndarray, ys: np.ndarray, is_valid: bool = True):
        """Método `PlotCanvas.add_series`.
            Parâmetros: `self`, `label`, `xs`, `ys`, `is_valid`."""
        self._series.append((label, np.asarray(xs, dtype=float), np.asarray(ys, dtype=float), is_valid))
        self.update()

    def set_labels(self, xlabel: str, ylabel: str):
        """Método `PlotCanvas.set_labels`.
            Parâmetros: `self`, `xlabel`, `ylabel`."""
        self._ylabel = ylabel
        self.update()

    # ---------- zoom / pan ----------
    def data_extents(self) -> tuple[float, float, float, float]:
        """(xmin,xmax,ymin,ymax) dos dados (sem zoom) — usado p/ limitar o zoom."""
        if not self._series:
            return 0.0, 1.0, 0.0, 1.0
        all_x = np.concatenate([s[1] for s in self._series])
        all_y = np.concatenate([s[2] for s in self._series])
        xmin, xmax = float(all_x.min()), float(all_x.max())
        ymin, ymax = float(all_y.min()), float(all_y.max())
        if xmax - xmin < 1e-12:
            xmax = xmin + 1e-12
        if ymax - ymin < 1e-12:
            ymax = ymin + 1e-12
        return xmin, xmax, ymin, ymax

    def reset_view(self):
        """Método `PlotCanvas.reset_view`.
            Parâmetros: `self`."""
        self._zoom = None
        self.update()

    def wheel_zoom(self, angle_delta: int, x_frac: float) -> bool:
        """Scroll: aproxima (delta>0) mantendo o ponto sob o cursor fixo."""
        if not self._series:
            return False
        z = self._zoom or self.data_extents()
        factor = 0.85 if angle_delta > 0 else 1.18
        x2 = zoom_at(z[0], z[1], x_frac, factor)
        x2 = clamp_zoom(x2[0], x2[1], *self.data_extents()[:2])
        self._zoom = (x2[0], x2[1], z[2], z[3])
        self.update()
        return True

    def drag_offset(self, dx_px: int, width: float) -> bool:
        """Pan horizontal pelo arrasto (dx em px → fração da janela)."""
        if not self._series or width <= 0 or self._drag_zoom0 is None:
            return False
        z0 = self._drag_zoom0
        frac = -dx_px / width * (z0[1] - z0[0])
        full = self.data_extents()
        x2 = pan_span(z0[0], z0[1], frac / max(1e-12, z0[1] - z0[0]))
        # borda: não passear além dos dados
        span = z0[1] - z0[0]
        if x2[1] > full[1]:
            x2 = (full[1] - span, full[1])
        if x2[0] < full[0]:
            x2 = (full[0], full[0] + span)
        self._zoom = (x2[0], x2[1], z0[2], z0[3])
        self.update()
        return True

    def paintEvent(self, event):
        """Método `PlotCanvas.paintEvent`.
            Parâmetros: `self`, `event`."""
        painter = QPainter(self)
        painter.fillRect(0, 0, self.width(), self.height(), QColor("#ffffff"))
        margin_l, margin_r, margin_t, margin_b = 56, 12, 18, 26
        plot = QRectF(
            margin_l, margin_t,
            self.width() - margin_l - margin_r,
            self.height() - margin_t - margin_b,
        )

        if not self._series:
            painter.setPen(QPen(QColor("#888888")))
            painter.drawText(plot, Qt.AlignmentFlag.AlignCenter, "sem série para desenhar")
            return

        # título no topo
        if self._title:
            painter.setPen(QPen(QColor("#222222")))
            painter.drawText(
                QRectF(plot.left(), 2, plot.width(), 16),
                Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter,
                self._title[:80],
            )

        all_x = np.concatenate([s[1] for s in self._series])
        all_y = np.concatenate([s[2] for s in self._series])
        ymax_data = float(all_y.max())
        ymin_data = float(all_y.min())
        if ymax_data - ymin_data < 1e-12:
            ymax_data = ymin_data + 1e-12
        if self._zoom is not None:
            ymin, ymax = self._zoom[2], self._zoom[3]
        else:
            ymin, ymax = ymin_data, ymax_data

        painter.fillRect(plot, QColor("#fafafa"))

        # grade n×m de ticks (4×4 linhas)
        painter.setPen(QPen(QColor("#dddddd"), 1))
        for i in range(5):
            tx = x = plot.left() + plot.width() * i / 4.0
            y = plot.top() + plot.height() * i / 4.0
            painter.drawLine(QPointF(tx, plot.top()), QPointF(tx, plot.bottom()))
            painter.drawLine(QPointF(plot.left(), y), QPointF(plot.right(), y))

        # eixos
        painter.setPen(QPen(QColor("#333333"), 1.4))
        painter.drawLine(plot.bottomLeft(), plot.bottomRight())
        painter.drawLine(plot.bottomLeft(), plot.topLeft())

        # ticks do eixo Y (min → max em 5 marcas)
        painter.setPen(QPen(QColor("#555555")))
        for i in range(5):
            value = ymin + (ymax - ymin) * i / 4.0
            py = float(plot.bottom() - (value - ymin) / (ymax - ymin) * plot.height())
            painter.drawLine(QPointF(plot.left() - 4, py), QPointF(plot.left(), py))
            painter.drawText(
                QRectF(0, py - 8, margin_l - 6, 14),
                Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter,
                format_tick(value),
            )

        painter.setPen(QPen(QColor("#333333")))
        painter.drawText(
            QRectF(plot.left(), self.height() - 20, plot.width(), 18),
            Qt.AlignmentFlag.AlignCenter, self._xlabel,
        )
        painter.save()
        painter.translate(12, plot.center().y())
        painter.rotate(-90)
        painter.drawText(QRectF(-60, -10, 120, 16), Qt.AlignmentFlag.AlignCenter, self._ylabel)
        painter.restore()

        # ticks com valores — UMA faixa para todas as séries (antes duplicava)
        painter.setPen(QPen(QColor("#555555")))
        xmin = float(all_x.min())
        xmax = float(all_x.max())
        if xmax - xmin < 1e-12:
            xmax = xmin + 1e-12
        if self._zoom is not None:
            xmin, xmax = self._zoom[0], self._zoom[1]
        lane = QRectF(0, plot.bottom() + 2, self.width(), 16)
        for i, tick_value in enumerate(compute_ticks(xmin, xmax, 5)):
            px = plot.left() + plot.width() * i / 4.0
            painter.drawText(
                QRectF(float(px) - 24, float(lane.top()), 48, 14),
                Qt.AlignmentFlag.AlignCenter, format_tick(tick_value),
            )

        # preenchimento de área sob a UMA série de linha válida (visual PDF)
        valid_line_series = [
            (xs, ys) for _, xs, ys, ok in self._series if ok and self.mode == "line"
        ]
        if len(valid_line_series) == 1:
            fill_xs, fill_ys = valid_line_series[0]
            fill_color = QColor(_SERIES_COLORS[0])
            fill_color.setAlpha(38)
            pts = [
                QPointF(float(plot.left()), float(plot.bottom())),
                *(
                    QPointF(
                        float(plot.left() + (x - xmin) / (xmax - xmin) * plot.width()),
                        float(plot.bottom() - (y - ymin) / (ymax - ymin) * plot.height()),
                    )
                    for x, y in zip(fill_xs, fill_ys)
                ),
                QPointF(float(plot.right()), float(plot.bottom())),
            ]
            painter.setPen(Qt.PenStyle.NoPen)
            painter.setBrush(fill_color)
            from PySide6.QtGui import QPolygonF

            painter.drawPolygon(QPolygonF(pts))
            painter.setBrush(Qt.BrushStyle.NoBrush)

        painter.setRenderHint(QPainter.RenderHint.Antialiasing, self.mode == "line")
        for idx, (label, xs, ys, is_valid) in enumerate(self._series):
            color = QColor(_SERIES_COLORS[idx % len(_SERIES_COLORS)])
            pen = QPen(color, 2.2 if is_valid else 1.0, Qt.PenStyle.DashLine if not is_valid else Qt.PenStyle.SolidLine)
            painter.setPen(pen)
            if self.mode == "line" or not is_valid:
                path = [
                    QPointF(
                        float(plot.left() + (x - xmin) / (xmax - xmin) * plot.width()),
                        float(plot.bottom() - (y - ymin) / (ymax - ymin) * plot.height()),
                    )
                    for x, y in zip(xs, ys)
                ]
                for a, b in zip(path, path[1:]):
                    painter.drawLine(a, b)
                # marcadores discretos em séries curtas (≤120 pontos)
                if len(path) <= 120:
                    marker_color = color.darker(120)
                    painter.setPen(QPen(marker_color, 1))
                    painter.setBrush(Qt.BrushStyle.SolidPattern)
                    r = 2.2
                    for pt in path:
                        painter.drawEllipse(pt, r, r)
                    painter.setBrush(Qt.BrushStyle.NoBrush)
                    painter.setPen(pen)
            else:
                bar_w = max(2.0, plot.width() / max(1, len(xs)) * 0.8)
                outline = color.darker(150)
                draw_outline = len(xs) <= 400
                show_values = len(xs) <= 30
                for x, y in zip(xs, ys):
                    px = plot.left() + (x - xmin) / (xmax - xmin) * plot.width()
                    h = (y - ymin) / (ymax - ymin) * plot.height()
                    painter.fillRect(QRectF(px - bar_w / 2, plot.bottom() - h, bar_w, h), color)
                    if draw_outline and h >= 1.0:
                        painter.setPen(QPen(outline, 1))
                        painter.setBrush(Qt.BrushStyle.NoBrush)
                        painter.drawRect(QRectF(px - bar_w / 2, plot.bottom() - h, bar_w, h))
                        painter.setPen(pen)
                    if show_values and h >= 1.0 and y != 0:
                        painter.setPen(QPen(QColor("#444444"), 1))
                        painter.drawText(
                            QRectF(float(px) - 22, float(plot.bottom() - h - 14), 44, 12),
                            Qt.AlignmentFlag.AlignCenter, format_tick(y),
                        )

        # legenda no canto superior direito
        if len(self._series) > 1:
            painter.setPen(QPen(QColor("#333333")))
            label_w = 150
            box_h = 16 * len(self._series) + 8
            legend_topleft = QPointF(plot.right() - label_w - 6, plot.top() + 6)
            painter.fillRect(
                QRectF(legend_topleft, QPointF(legend_topleft.x() + label_w, legend_topleft.y() + box_h)),
                QColor(255, 255, 255, 220),
            )
            for idx, (label, _, _, _) in enumerate(self._series):
                color = QColor(_SERIES_COLORS[idx % len(_SERIES_COLORS)])
                sw_y = legend_topleft.y() + 8 + 16 * idx
                painter.fillRect(QRectF(legend_topleft.x() + 6, sw_y, 10, 10), color)
                painter.drawText(
                    QRectF(legend_topleft.x() + 20, sw_y - 3, label_w - 24, 14),
                    Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter,
                    label[:18],
                )


# ---------- diálogo ----------
class DistributionPlotDialog(QDialog):
    """Gráfico de PDF/PMF de distribuição ou função f(x) definida pelo usuário."""

    def __init__(self, registry=None, parent=None, exp_repo=None):
        """Método `DistributionPlotDialog.__init__`.
            Parâmetros: `self`, `registry`, `parent`, `exp_repo`."""
        super().__init__(parent)
        self.setWindowTitle("Gráficos de distribuição")
        self.setMinimumWidth(560)
        self.registry = registry
        self.exp_repo = exp_repo

        form = QFormLayout()
        self.combo_kind = QComboBox()
        self.combo_kind.addItems(
            ["PDF (linha)", "PDF (barras)", "f(x) definida pelo usuário", "Histograma (experimentos)"]
        )
        self.combo_kind.currentIndexChanged.connect(self._kind_changed)

        self.combo_distcombo = QComboBox()
        if registry is not None:
            codes = [
                f"{provider}.{dist}"
                for provider, dist in registry.list_all()
            ]
            # triagem para a lista não ficar gigantesca
            if len(codes) > 400:
                codes = [c for c in codes if c.startswith("scipy.norm")] + [
                    c for c in codes if not c.startswith("scipy.norm")][:390]
            self.combo_distcombo.addItems(codes)
        self.combo_distcombo.currentIndexChanged.connect(lambda *_: self.redraw())

        self.line_expr = QLineEdit("x**2")
        self.line_expr.setEnabled(False)

        self.combo_var = QComboBox()
        self.combo_var.setEnabled(False)
        if exp_repo is not None:
            from app.core.parsing import var_label

            self.combo_var.addItems(
                [var_label(v) for v in exp_repo.var_ids()]
            )
            self.combo_var.currentIndexChanged.connect(lambda *_: self.redraw())

        form.addRow("Tipo:", self.combo_kind)
        form.addRow("Distribuição:", self.combo_distcombo)
        form.addRow("f(x) =", self.line_expr)
        form.addRow("Variável amostrada:", self.combo_var)

        self.spin_n = QSpinBox()
        self.spin_n.setRange(16, 2000)
        self.spin_n.setValue(220)
        self.spin_bars = QSpinBox()
        self.spin_bars.setRange(8, 200)
        self.spin_bars.setValue(32)
        form.addRow("Pontos (linha):", self.spin_n)
        form.addRow("Barras (hist.):", self.spin_bars)

        self.canvas = PlotCanvas(self)
        self.canvas.setMouseTracking(True)
        self.canvas.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.canvas.wheelEvent = self._canvas_wheel
        self.canvas.mousePressEvent = self._canvas_press
        self.canvas.mouseMoveEvent = self._canvas_move
        self.canvas.mouseReleaseEvent = self._canvas_release
        self.canvas.mouseDoubleClickEvent = self._canvas_double

        buttons = QHBoxLayout()
        self.btn_zoom_in = QPushButton("+")
        self.btn_zoom_in.setToolTip("Aproximar no centro (Também: scroll do mouse).")
        self.btn_zoom_in.setFixedWidth(28)
        self.btn_zoom_out = QPushButton("−")
        self.btn_zoom_out.setToolTip("Afasta no centro (Também: scroll — oposto).")
        self.btn_zoom_out.setFixedWidth(28)
        self.btn_zoom_reset = QPushButton("Reset zoom")
        self.btn_zoom_reset.setToolTip("Volta à vista completa dos dados. (Duplo clique também.)")
        self.btn_zoom_in.clicked.connect(lambda: self.canvas.wheel_zoom(120, 0.5))
        self.btn_zoom_out.clicked.connect(lambda: self.canvas.wheel_zoom(-120, 0.5))
        self.btn_zoom_reset.clicked.connect(self.canvas.reset_view)
        buttons.addWidget(self.btn_zoom_in)
        buttons.addWidget(self.btn_zoom_out)
        buttons.addWidget(self.btn_zoom_reset)
        self.btn_save_png = QPushButton("Salvar PNG…")
        self.btn_save_png.setToolTip("Salva o gráfico atual como imagem PNG.")
        self.btn_save_png.clicked.connect(self._save_png)
        buttons.addWidget(self.btn_save_png)
        btn_draw = QPushButton("Desenhar")
        btn_draw.clicked.connect(self.redraw)
        btn_add = QPushButton("Adicionar ao gráfico")
        btn_add.setToolTip("Sobrepõe a série atual ao gráfico (comparar distribuições ou f(x)).")
        btn_add.clicked.connect(lambda: self.redraw(keep_existing=True))
        btn_close = QPushButton("Fechar")
        btn_close.clicked.connect(self.reject)
        buttons.addWidget(btn_draw)
        buttons.addWidget(btn_add)
        buttons.addStretch()
        buttons.addWidget(btn_close)

        lay = QVBoxLayout(self)
        lay.addLayout(form)
        lay.addWidget(self.canvas)
        lay.addLayout(buttons)
        self.combo_kind.currentIndexChanged.emit(self.combo_kind.currentIndex())

    def _kind_changed(self, index: int):
        """Método `DistributionPlotDialog._kind_changed`.
            Parâmetros: `self`, `index`."""
        is_user = index == 2
        is_empirical = index == 3
        self.line_expr.setEnabled(is_user)
        self.combo_distcombo.setEnabled(not is_user and not is_empirical)
        self.combo_var.setEnabled(is_empirical)

    # ---------- cálculo das séries ----------
    def _series(self):
        """Método `DistributionPlotDialog._series`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        kind = self.combo_kind.currentIndex()
        if kind in (0, 1):
            code = self.combo_distcombo.currentText()
            return self._series_for_spec(code, kind == 1)
        if kind == 3:
            return self._series_for_experiments()
        return self._series_for_user_function()

    def _series_for_experiments(self):
        """Método `DistributionPlotDialog._series_for_experiments`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        if self.exp_repo is None or self.exp_repo.count() == 0:
            return []
        from app.core.parsing import var_label

        index = self.combo_var.currentIndex()
        ids = self.exp_repo.var_ids()
        if index < 0 or index >= len(ids):
            return []
        var_id = ids[index]
        values = np.asarray(self.exp_repo.get_variable_values(var_id), dtype=float)
        if values.size == 0:
            return []
        hist, edges = np.histogram(values, bins=self.spin_bars.value())
        centers = (edges[:-1] + edges[1:]) / 2.0
        density = hist / hist.sum()
        valid = hist.sum() > 0 and np.isfinite(density).all()
        return [(f"amostra {var_label(var_id)}", centers, density if valid else centers * 0, valid)]

    def _series_for_spec(self, code: str, bars: bool):
        """Método `DistributionPlotDialog._series_for_spec`.
            Parâmetros: `self`, `code`, `bars`.
            Retorna o resultado calculado a partir do estado local."""
        if self.registry is None:
            return []
        spec = self.registry.parse_code(code)
        provider = self.registry.get_provider(spec.provider)
        xs: np.ndarray
        ys: np.ndarray

        if bars:
            if provider is None:
                return []
            rng = np.random.default_rng(7)
            sample = provider.sample(spec, 400, rng)
            hist, edges = np.histogram(np.asarray(sample, dtype=float).ravel(), bins=self.spin_bars.value())
            centers = (edges[:-1] + edges[1:]) / 2.0
            density = hist / hist.sum()
            valid = hist.sum() > 0 and np.isfinite(density).all()
            return [("pdf", centers, density if valid else (centers * 0), valid)]

        from scipy import stats as scipy_stats

        if spec.provider == "scipy" and spec.name in scipy_stats.__dir__():
            dist = getattr(scipy_stats, spec.name)
            try:
                lo, hi = dist.ppf(1e-3, **spec.params), dist.ppf(0.999, **spec.params)
                if not np.isfinite([lo, hi]).all() or hi <= lo:
                    lo, hi = dist.ppf(0.01, **spec.params), dist.ppf(0.99, **spec.params)
                xs = np.linspace(float(lo), float(hi), self.spin_n.value())
                ys = dist.pdf(xs, **spec.params)
                return [(f"pdf({code})", xs, ys, True)]
            except Exception:  # noqa: BLE001
                return []
        if spec.provider == "triangular":
            low, mode, high = (
                float(spec.params.get(k, 0.0)) for k in ("low", "mode", "high")
            )
            if high <= low:
                return []
            xs = np.linspace(low, high, self.spin_n.value())
            ys = np.zeros_like(xs)
            left = xs <= mode
            span = high - low
            ys[left] = 2.0 * (xs[left] - low) / ((mode - low) * span) if mode > low else 0.0
            ys[~left] = 2.0 * (high - xs[~left]) / ((high - mode) * span) if high > mode else 0.0
            return [("pdf(binária triangular)", xs, ys, True)]
        if spec.provider == "fixed":
            value = float(spec.params.get("value", 0.0))
            xs = np.array([value - 1, value - 1e-9, value, value + 1e-9, value + 1])
            ys = np.array([0, 0, 1, 0, 0], dtype=float)
            return [("pmf(fixo)", xs, ys, True)]
        return []

    def _series_for_user_function(self):
        """Método `DistributionPlotDialog._series_for_user_function`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        expr = self.line_expr.text()
        err = validate_function(expr)
        if err:
            self.canvas.set_mode("line")
            self.canvas.clear_series()
            self.canvas.set_labels("x", "f(x)")
            return []
        f = safe_eval_function(expr)
        xs = np.linspace(0.0, 10.0, self.spin_n.value())
        ys = f(xs)
        valid = bool(np.isfinite(ys).all())
        return [("f(x)", xs, np.nan_to_num(ys, nan=0.0, posinf=0.0, neginf=0.0), valid)]

    # ---------- eventos do canvas (zoom/pan) ----------
    def _canvas_x_frac(self, x: int) -> float:
        """Método `DistributionPlotDialog._canvas_x_frac`.
            Parâmetros: `self`, `x`.
            Retorna o resultado calculado a partir do estado local."""
        margin_l, margin_r = 56, 12
        plot_w = max(1.0, self.canvas.width() - margin_l - margin_r)
        return min(1.0, max(0.0, (x - margin_l) / plot_w))

    def _canvas_wheel(self, event):
        """Método `DistributionPlotDialog._canvas_wheel`.
            Parâmetros: `self`, `event`."""
        d = int(event.angleDelta().y())
        if self.canvas.wheel_zoom(d, self._canvas_x_frac(int(event.position().x()))):
            event.accept()
        else:
            event.ignore()

    def _canvas_press(self, event):
        """Método `DistributionPlotDialog._canvas_press`.
            Parâmetros: `self`, `event`."""
        if event.button() == Qt.MouseButton.LeftButton and self.canvas._series:
            self.canvas._drag_x0 = int(event.position().x())
            self.canvas._drag_zoom0 = self.canvas._zoom or self.canvas.data_extents()
        event.ignore()

    def _canvas_move(self, event):
        """Método `DistributionPlotDialog._canvas_move`.
            Parâmetros: `self`, `event`."""
        if self.canvas._drag_x0 is not None:
            dx = int(event.position().x()) - self.canvas._drag_x0
            w = float(self.canvas.width())
            self.canvas._drag_x0 = int(event.position().x())
            self.canvas.drag_offset(dx, w)
        event.ignore()

    def _canvas_release(self, event):
        """Método `DistributionPlotDialog._canvas_release`.
            Parâmetros: `self`, `event`."""
        self.canvas._drag_x0 = None
        self.canvas._drag_zoom0 = None
        event.ignore()

    def _canvas_double(self, event):
        """Método `DistributionPlotDialog._canvas_double`.
            Parâmetros: `self`, `event`."""
        self.canvas.reset_view()
        event.accept()

    def _save_png(self):
        """Método `DistributionPlotDialog._save_png`.
            Parâmetros: `self`."""
        from PySide6.QtWidgets import QFileDialog

        path, _ = QFileDialog.getSaveFileName(
            self, "Salvar gráfico como PNG", "grafico.png", "PNG (*.png)"
        )
        if not path:
            return
        if not path.lower().endswith(".png"):
            path += ".png"
        ok = self.canvas.grab().save(path, "PNG")
        self.setWindowTitle(
            f"Gráfico — salvo em {path}" if ok else "Gráfico — falha ao salvar PNG"
        )

    def redraw(self, keep_existing: bool = False):
        """Método `DistributionPlotDialog.redraw`.
            Parâmetros: `self`, `keep_existing`."""
        if not keep_existing:
            self.canvas.clear_series()
        series = self._series()
        if not series:
            self.canvas.set_mode("line")
            self.canvas.add_series("(nenhuma)", np.array([0.0, 1.0]), np.array([0.0, 0.0]), False)
            self.canvas.set_labels("x", "f")
            return
        for label, xs, ys, valid in series:
            self.canvas.add_series(label, xs, ys, valid)
        self.canvas.set_mode("bar" if self.combo_kind.currentIndex() in (1, 3) else "line")
        kind = self.combo_kind.currentIndex()
        if kind == 2:
            title = f"f(x) = {self.line_expr.text()}"
        elif kind == 3:
            title = f"Histograma — {self.combo_var.currentText()}"
        else:
            title = f"{self.combo_distcombo.currentText()} (pdf)"
        self.canvas.set_title(title)
        self.canvas.set_labels(
            "x",
            "pdf" if self.combo_kind.currentIndex() != 2 else "f(x)",
        )
