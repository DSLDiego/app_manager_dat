"""Validação de results de amostragem: TODA variável de TODO experimento com valor."""

from __future__ import annotations

from typing import List, Sequence


def find_incomplete_variables(result) -> List[int]:
    """Retorna var_ids com coluna incompleta/inválida (nan/inf/ausente) no result."""
    var_ids: Sequence[int] = list(getattr(result, "var_ids", []) or [])
    matrix = getattr(result, "matrix", []) or []
    if not matrix:
        return list(var_ids)

    bad: set[int] = set()
    for row in matrix:
        if len(row) != len(var_ids):
            # linha mais curta: todas as colunas a partir do fim estão ausentes
            for pos in range(len(row), len(var_ids)):
                bad.add(int(var_ids[pos]))
            for pos, value in enumerate(row):
                if not _finite(value):
                    bad.add(int(var_ids[pos]))
            continue
        for pos, value in enumerate(row):
            if not _finite(value):
                bad.add(int(var_ids[pos]))
    return sorted(bad)


def _finite(value) -> bool:
    """Função `_finite`.
        Parâmetros: `value`.
        Retorna o resultado calculado a partir do estado local."""
    try:
        return bool(float(value) == float(value)) and abs(float(value)) != float("inf")
    except (TypeError, ValueError):
        return False
