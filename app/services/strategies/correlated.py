from __future__ import annotations

from typing import List

import numpy as np
from scipy import stats


class CorrelatedStrategy:
    """Estratégia correlacionada (Iman-Conover)."""

    name = "correlated"

    @staticmethod
    def apply(base: np.ndarray, correlation: List[List[float]]) -> np.ndarray:
        """Método `CorrelatedStrategy.apply`.
            Parâmetros: `base`, `correlation`.
            Retorna o resultado calculado a partir do estado local."""
        return iman_conover_reorder(base, correlation)

    @staticmethod
    def validate(corr: List[List[float]]) -> List[str]:
        """Método `CorrelatedStrategy.validate`.
            Parâmetros: `corr`.
            Retorna o resultado calculado a partir do estado local."""
        m = np.asarray(corr, dtype=float)
        if m.ndim != 2 or m.shape[0] != m.shape[1]:
            return ["Matriz de correlação não é quadrada."]
        if np.any(np.abs(m) > 1.0):
            return ["Correlações fora de [-1, 1]."]
        return []


def iman_conover_reorder(base: np.ndarray, corr) -> np.ndarray:
    """Reordena colunas de base pelos postos de escores normais correlacionados.

    Mantém os mesmos valores em cada coluna (marginais preservadas),
    apenas reorganiza as linhas para induzir correlação de postos.
    """
    n, d = base.shape
    corr = np.asarray(corr, dtype=float)

    rng = np.random.default_rng(0)
    mvn = stats.multivariate_normal(
        mean=np.zeros(d), cov=corr, allow_singular=True,
    )
    scores = mvn.rvs(size=n, random_state=rng)
    if scores.ndim == 1:
        scores = scores.reshape(-1, 1)

    result = np.empty_like(base)
    for col in range(d):
        order = np.argsort(scores[:, col], kind="stable")
        sorted_vals = np.sort(base[:, col], kind="mergesort")
        result[order, col] = sorted_vals

    return result
