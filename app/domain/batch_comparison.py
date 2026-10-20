"""Entidades de comparação entre batches."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class BatchVariableStats:
    """Classe `BatchVariableStats` do módulo."""
    var_id: int
    mean_a: float
    mean_b: float
    p10_a: float
    p10_b: float
    p50_a: float
    p50_b: float
    p90_a: float
    p90_b: float
    mean_delta: float
    mean_delta_pct: Optional[float]


@dataclass(frozen=True)
class BatchComparisonResult:
    """Classe `BatchComparisonResult` do módulo."""
    batch_a_id: str
    batch_b_id: str
    n_a: int
    n_b: int
    variables: List[BatchVariableStats]
