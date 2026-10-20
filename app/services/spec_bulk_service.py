"""Aplicação de distribuições em lote — lógica pura, sem Qt.

Regras centralizadas para o menu de contexto (1 var → todas)
e o dialog secundário de lotes (1.1 / 1.2 do produto).
"""

from __future__ import annotations

from typing import Dict, Iterable, Optional

from app.domain.entities import DistributionSpec


def apply_spec_to_all(
    specs: Dict[int, DistributionSpec],
    var_ids: Iterable[int],
    spec: DistributionSpec,
) -> Dict[int, DistributionSpec]:
    """Mesma distribuição para todas as variáveis (poucos cliques)."""
    return {int(var_id): spec for var_id in var_ids}


def apply_spec_to_selected(
    specs: Dict[int, DistributionSpec],
    target_ids: Iterable[int],
    spec: DistributionSpec,
) -> Dict[int, DistributionSpec]:
    """Mesma distribuição apenas para as variáveis selecionadas (lote parcial)."""
    result = dict(specs)
    for var_id in target_ids:
        result[int(var_id)] = spec
    return result


def clear_specs(
    specs: Dict[int, DistributionSpec],
    var_ids: Optional[Iterable[int]] = None,
) -> Dict[int, DistributionSpec]:
    """Remove distribuições: todas, ou apenas as informadas."""
    result = dict(specs)
    if var_ids is None:
        return {}
    for var_id in var_ids:
        result.pop(int(var_id), None)
    return result


def make_fixed_spec(value: float) -> DistributionSpec:
    """Função `make_fixed_spec`.
        Parâmetros: `value`.
        Retorna o resultado calculado a partir do estado local."""
    return DistributionSpec(provider="fixed", name="value", params={"value": float(value)})


def missing_of(var_ids: Iterable[int], specs: Dict[int, DistributionSpec]) -> list:
    """Variáveis do template que ainda estão sem distribuição."""
    return [int(v) for v in var_ids if int(v) not in specs]


def coverage(var_ids: Iterable[int], specs: Dict[int, DistributionSpec]) -> float:
    """Fração [0,1] de variáveis com distribuição definida (0 se vazio)."""
    ids = [int(v) for v in var_ids]
    if not ids:
        return 0.0
    return sum(1 for v in ids if v in specs) / len(ids)
