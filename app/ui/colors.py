"""Utilitários de escala/gradiente reutilizáveis (heatmap, plots, futuras matrizes)."""

from __future__ import annotations

from typing import Optional, Tuple


def rescale01(value: float, vmin: float, vmax: float) -> float:
    """Escala linear [0,1]; degenerado (vmax ≈ vmin) → 0.5."""
    if vmax - vmin < 1e-15:
        return 0.5
    t = (value - vmin) / (vmax - vmin)
    return min(max(t, 0.0), 1.0)


def lerp_hex(a: Tuple[int, int, int], b: Tuple[int, int, int], t: float) -> str:
    """Interpolação linear entre duas cores RGB → '#rrggbb'."""
    r = int(a[0] + (b[0] - a[0]) * t)
    g = int(a[1] + (b[1] - a[1]) * t)
    bl = int(a[2] + (b[2] - a[2]) * t)
    return f"#{r:02x}{g:02x}{bl:02x}"


_LOW = (33, 102, 172)     # azul
_HIGH = (247, 247, 177)   # amarelo claro

# Paletas (low → mid → high) para heatmap/plots; shared entre painéis.
PALETTES = {
    "azul→amarelo": ((33, 102, 172), (190, 200, 222), (247, 247, 177)),
    "roxo→verde": ((74, 52, 130), (235, 235, 235), (35, 159, 88)),
    "cinza→destaque": ((60, 60, 66), (130, 130, 138), (255, 160, 40)),
}


def palette_names():
    """Função `palette_names`.
        Retorna o resultado calculado a partir do estado local."""
    return list(PALETTES)


def palette_gradient(name: str, steps: int = 64):
    """Lista '#rrggbb' do low ao high da paleta (para legenda)."""
    low, mid, high = PALETTES.get(name, PALETTES["azul→amarelo"])
    out = []
    for i in range(max(2, steps)):
        t = i / (max(2, steps) - 1)
        src, dst, k = (low, mid, 2.0) if t < 0.5 else (mid, high, 2.0)
        tt = (t * 2.0) if t < 0.5 else (t - 0.5) * 2.0
        r = int(src[0] + (dst[0] - src[0]) * tt)
        g = int(src[1] + (dst[1] - src[1]) * tt)
        b = int(src[2] + (dst[2] - src[2]) * tt)
        out.append(f"#{r:02x}{g:02x}{b:02x}")
    return out


def color_hex(value: float, vmin: float, vmax: float) -> str:
    """Gradiente azul → amarelo do min ao max da coluna (heatmap)."""
    return lerp_hex(_LOW, _HIGH, rescale01(value, vmin, vmax))


def color_with_palette(value: float, vmin: float, vmax: float, palette: str) -> str:
    """Cor da paleta escolhida para value em [-min, max] da coluna."""
    low, mid, high = PALETTES.get(palette, PALETTES["azul→amarelo"])
    t = rescale01(value, vmin, vmax)
    if t < 0.5:
        return lerp_hex(low, mid, t * 2.0)
    return lerp_hex(mid, high, (t - 0.5) * 2.0)


def color_for_value(value: float, vmin: float, vmax: float) -> Optional[str]:
    """Atalho com 'None' para células ausentes (—)."""
    if value is None:
        return None
    return color_hex(value, vmin, vmax)
