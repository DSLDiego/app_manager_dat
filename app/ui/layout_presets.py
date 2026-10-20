"""Presets de layout dos painéis (docks) — planos puros executados pelo MainWindow.

Presets:
  "Grade"            — docks em grade n×m (algoritmo atual)
  "Abas"             — todos os docks empilhados em abas
  "Editor | Painéis" — metade: editor à esquerda, todos os docks em abas à direita
  "4 quadrantes"     — editor central + 4 docks nos cantos
"""

from __future__ import annotations

LAYOUT_PRESETS = ("Grade", "Abas", "Editor | Painéis", "4 quadrantes")

# op: "split_h" (b à direita de a) | "split_v" (b abaixo de a) | "tabify" (b em aba de a)
Op = tuple[str, str, str]


def grid_plan(docks: list[str]) -> list[Op]:
    """Grade n×m — mesmo algoritmo do _arrange_docks_grid, puro."""
    n = len(docks)
    if n == 0:
        return []
    import math

    cols = max(1, int(math.ceil(math.sqrt(n))))
    ops: list[Op] = []
    for i in range(n):
        if (i + 1) < n and (i + 1) % cols != 0:
            ops.append(("split_h", docks[i], docks[i + 1]))
    for i in range(0, n - cols):
        ops.append(("split_v", docks[i], docks[i + cols]))
    return ops


def tabs_plan(docks: list[str]) -> list[Op]:
    """Todos empilhados em abas no primeiro dock."""
    if not docks:
        return []
    return [("tabify", docks[0], d) for d in docks[1:]]


def half_plan(docks: list[str]) -> list[Op]:
    """Editor | Painéis: um único stack de docks (implicitamente à direita)."""
    return tabs_plan(docks)


def quadrants_plan(docks: list[str]) -> list[Op]:
    """4 quadrantes com os primeiros 4 docks (extras vão em aba do 4º)."""
    if len(docks) < 4:
        return tabs_plan(docks)
    a, b, c, d = docks[0], docks[1], docks[2], docks[3]
    ops: list[Op] = [
        ("split_v", a, b),   # coluna esquerda: a em cima, b embaixo
        ("split_h", a, c),   # c à direita de a
        ("split_v", c, d),   # coluna direita: c em cima, d embaixo
    ]
    for extra in docks[4:]:
        ops.append(("tabify", d, extra))
    return ops


def layout_plan(preset: str, docks: list[str]) -> list[Op]:
    """Plano de ops para o preset — puro, validado contra LAYOUT_PRESETS."""
    if preset == "Grade":
        return grid_plan(docks)
    if preset == "Abas":
        return tabs_plan(docks)
    if preset == "Editor | Painéis":
        return half_plan(docks)
    if preset == "4 quadrantes":
        return quadrants_plan(docks)
    raise ValueError(f"preset desconhecido: {preset}")


DOCK_WIDTH_FRACTION = 0.20  # r17: dock não força mais que 20% da largura da janela


def dock_width_cap(window_width: int, frac: float = DOCK_WIDTH_FRACTION) -> int:
    """Largura mínima máxima permitida p/ um dock (puro, piso de 90px)."""
    return max(90, int(window_width * frac))


def widgets_over_cap(widgets: list, cap: int) -> list:
    """Widgets com largura mínima EXPLÍCITA acima do cap — puro (lista de Qt widgets)."""
    over = []
    for w in widgets:
        try:
            if w.minimumSize().width() > cap:
                over.append(w)
        except RuntimeError:  # widget C++ já deletado
            continue
    return over
