"""Seed reprodutível — puro (sem Qt).

seed_from_text:
- vazio     → aleatório de SystemRandom (1..2^31-1), cada chamada diferente
- "424242"  → 424242 (reprodutível)
- "abc"     → ValueError (o validador da UI impede na prática)
"""

from __future__ import annotations

_SEED_MAX = 2_147_483_647


def seed_from_text(raw: str | None) -> int:
    """Função `seed_from_text`.
        Parâmetros: `raw`.
        Retorna o resultado calculado a partir do estado local.
        Levanta: ValueError."""
    text = (raw or "").strip()
    if not text:
        from random import SystemRandom

        return SystemRandom().randrange(1, _SEED_MAX + 1)
    if not text.isdigit():
        raise ValueError(f"seed inválida: {raw!r}")
    value = int(text)
    if value < 1:
        return 1
    return min(value, _SEED_MAX)
