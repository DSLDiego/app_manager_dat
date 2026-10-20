"""Análise estatística sobre valores de uma variável."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple

import numpy as np


@dataclass(frozen=True)
class VariableStats:
    """Classe `VariableStats` do módulo."""
    var_id: int
    count: int
    mean: float
    std: float
    minimum: float
    maximum: float
    p10: float
    p50: float
    p90: float


class StatisticsService:
    """Classe `StatisticsService` do módulo."""
    def compute(self, var_id: int, values: List[float]) -> VariableStats:
        """Método `StatisticsService.compute`.
            Parâmetros: `self`, `var_id`, `values`.
            Retorna o resultado calculado a partir do estado local."""
        if not values:
            return VariableStats(var_id, 0, *([float("nan")] * 7))

        arr = np.asarray(values, dtype=float)
        p10, p50, p90 = np.quantile(arr, [0.10, 0.50, 0.90])

        return VariableStats(
            var_id=var_id,
            count=int(arr.size),
            mean=float(arr.mean()),
            std=float(arr.std(ddof=1)) if arr.size > 1 else 0.0,
            minimum=float(arr.min()),
            maximum=float(arr.max()),
            p10=float(p10),
            p50=float(p50),
            p90=float(p90),
        )

    def histogram(
        self,
        values: List[float],
        bins: int = 50,
    ) -> Tuple[np.ndarray, np.ndarray]:
        """Método `StatisticsService.histogram`.
            Parâmetros: `self`, `values`, `bins`.
            Retorna o resultado calculado a partir do estado local."""
        arr = np.asarray(values, dtype=float)
        counts, edges = np.histogram(arr, bins=bins)
        return counts, edges
