"""Temas do editor: Dracula (padrão) e Claro."""

from __future__ import annotations

from PySide6.QtGui import QColor
from PySide6.QtCore import QSettings

DRACULA = {
    "editor_background": "#282a36",
    "editor_foreground": "#f8f8f2",
    "line_number_area": "#21222c",
    "line_number": "#7583af",
    "line_number_active": "#8be9fd",
    "current_line": "#44475a",
    "cursor": "#f8f8f2",
    "selection_background": "#44475a",
    "selection_foreground": "#f8f8f2",
    "keyword": "#ff79c6",
    "keyword_unknown": "#ffb86c",
    "token": "#8be9fd",
    "comment": "#7d8bb4",
    "number": "#bd93f9",
    "string": "#50fa7b",
}

LIGHT = {
    "editor_background": "#ffffff",
    "editor_foreground": "#2c3e50",
    "line_number_area": "#f5f5f5",
    "line_number": "#757575",
    "line_number_active": "#1e6bb8",
    "current_line": "#fff8e1",
    "cursor": "#2c3e50",
    "selection_background": "#a8d8ff",
    "selection_foreground": "#111111",
    "keyword": "#1e6bb8",
    "keyword_unknown": "#c0392b",
    "token": "#8e44ad",
    "comment": "#208d4e",
    "number": "#d05300",
    "string": "#138a72",
}

NORD = {
    "editor_background": "#2e3440",
    "editor_foreground": "#eceff4",
    "line_number_area": "#242933",
    "line_number": "#7e8aa3",
    "line_number_active": "#88c0d0",
    "current_line": "#3b4252",
    "cursor": "#eceff4",
    "selection_background": "#434c5e",
    "selection_foreground": "#eceff4",
    "keyword": "#81a1c1",
    "keyword_unknown": "#d08770",
    "token": "#88c0d0",
    "comment": "#8b97ad",
    "number": "#b48ead",
    "string": "#a3be8c",
}

SOLARIZED = {
    "editor_background": "#fdf6e3",
    "editor_foreground": "#586e75",
    "line_number_area": "#eee8d5",
    "line_number": "#617070",
    "line_number_active": "#227bba",
    "current_line": "#eee8d5",
    "cursor": "#586e75",
    "selection_background": "#d3d3c4",
    "selection_foreground": "#073642",
    "keyword": "#227bba",
    "keyword_unknown": "#cb4b16",
    "token": "#22837b",
    "comment": "#697979",
    "number": "#d33682",
    "string": "#6d7d00",
}

THEMES = {
    "dracula": DRACULA,
    "light": LIGHT,
    "nord": NORD,
    "solarized": SOLARIZED,
}
DEFAULT_THEME = "dracula"


def theme_colors(name: str) -> dict:
    """Função `theme_colors`.
        Parâmetros: `name`.
        Retorna o resultado calculado a partir do estado local."""
    return THEMES.get(name, DRACULA)


def theme_qcolor(name: str, key: str) -> QColor:
    """Função `theme_qcolor`.
        Parâmetros: `name`, `key`.
        Retorna o resultado calculado a partir do estado local."""
    return QColor(theme_colors(name).get(key, DRACULA.get(key, "#000000")))


# ---------- r28: contraste WCAG (puro, sem Qt) ----------
def _srgb_channel(c: int) -> float:
    """Função `_srgb_channel`.
        Parâmetros: `c`.
        Retorna o resultado calculado a partir do estado local."""
    c = c / 255.0
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def relative_luminance(hex_color: str) -> float:
    """Função `relative_luminance`.
        Parâmetros: `hex_color`.
        Retorna o resultado calculado a partir do estado local."""
    text = str(hex_color).lstrip("#")
    if len(text) != 6:
        return 0.5
    r, g, b = (int(text[i:i + 2], 16) for i in (0, 2, 4))
    return (
        0.2126 * _srgb_channel(r)
        + 0.7152 * _srgb_channel(g)
        + 0.0722 * _srgb_channel(b)
    )


def contrast_ratio(hex_a: str, hex_b: str) -> float:
    """Função `contrast_ratio`.
        Parâmetros: `hex_a`, `hex_b`.
        Retorna o resultado calculado a partir do estado local."""
    la = relative_luminance(hex_a)
    lb = relative_luminance(hex_b)
    lighter, darker = max(la, lb), min(la, lb)
    return (lighter + 0.05) / (darker + 0.05)


# pares de texto/fundo relevantes por legibilidade (r28)
TEXT_PAIRS = (
    ("editor_foreground", "editor_background"),
    ("line_number", "line_number_area"),
    ("line_number_active", "editor_background"),
    ("comment", "editor_background"),
    ("keyword", "editor_background"),
    ("keyword_unknown", "editor_background"),
    ("token", "editor_background"),
    ("number", "editor_background"),
    ("string", "editor_background"),
    ("selection_foreground", "selection_background"),
)

MIN_CONTRAST = 4.0  # WCAG AA exige 4.5 em texto normal; 4.0 é o piso do app


def theme_contrast_issues(name: str, min_ratio: float = MIN_CONTRAST) -> list[tuple]:
    """[(bg, fg, ratio)] abaixo do piso — puro, usado pelo teste de a11y."""
    colors = theme_colors(name)
    issues = []
    for fg_key, bg_key in TEXT_PAIRS:
        fg = colors.get(fg_key)
        bg = colors.get(bg_key)
        if not fg or not bg:
            continue
        ratio = contrast_ratio(fg, bg)
        if ratio < min_ratio:
            issues.append((bg_key, fg_key, round(ratio, 2)))
    return issues


def saved_theme() -> str:
    """Função `saved_theme`.
        Retorna o resultado calculado a partir do estado local."""
    settings = QSettings("datstudio", "dtengine")
    return str(settings.value("editor/theme", DEFAULT_THEME))


def persist_theme(name: str) -> None:
    """Função `persist_theme`.
        Parâmetros: `name`."""
    settings = QSettings("datstudio", "dtengine")
    settings.setValue("editor/theme", name)


DEFAULT_FONT_SCALE = 1.0
MIN_FONT_SCALE = 0.5
MAX_FONT_SCALE = 4.0
ZOOM_STEP = 0.1


def _clamp_scale(value) -> float:
    """Função `_clamp_scale`.
        Parâmetros: `value`.
        Retorna o resultado calculado a partir do estado local."""
    try:
        scale = float(value)
    except (TypeError, ValueError):
        scale = DEFAULT_FONT_SCALE
    return max(MIN_FONT_SCALE, min(MAX_FONT_SCALE, scale))


def saved_font_scale() -> float:
    """Função `saved_font_scale`.
        Retorna o resultado calculado a partir do estado local."""
    settings = QSettings("datstudio", "dtengine")
    return _clamp_scale(settings.value("editor/font_scale", DEFAULT_FONT_SCALE))


def persist_font_scale(scale: float) -> None:
    """Função `persist_font_scale`.
        Parâmetros: `scale`."""
    settings = QSettings("datstudio", "dtengine")
    settings.setValue("editor/font_scale", _clamp_scale(scale))


DEFAULT_SYSTEM_SCALE = 1.0


def saved_system_scale() -> float:
    """Função `saved_system_scale`.
        Retorna o resultado calculado a partir do estado local."""
    settings = QSettings("datstudio", "dtengine")
    return _clamp_scale(settings.value("app/system_font_scale", DEFAULT_SYSTEM_SCALE))


def persist_system_scale(scale: float) -> None:
    """Função `persist_system_scale`.
        Parâmetros: `scale`."""
    settings = QSettings("datstudio", "dtengine")
    settings.setValue("app/system_font_scale", _clamp_scale(scale))
