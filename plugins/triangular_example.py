"""Exemplo de plugin: provider Triangular plugável (BaseDistributionProvider)."""

from __future__ import annotations

from typing import List

import numpy as np

from app.domain.entities import DistributionSpec
from app.infrastructure.providers.base import BaseDistributionProvider


class TriangularProvider(BaseDistributionProvider):
    provider_name = "triangular"
    description = "Triângulo entre mínimo (a), mais provável (c) e máximo (b)."

    def list_distributions(self) -> List[str]:
        return ["generic"]

    def parameter_names(self, dist_name: str) -> List[str]:
        return ["a", "c", "b"]

    def sample(self, spec: DistributionSpec, size: int, rng: np.random.Generator):
        a = float(spec.params.get("a", 0.0))
        c = float(spec.params.get("c", 0.5))
        b = float(spec.params.get("b", 1.0))
        return rng.triangular(a, c, b, size)

    def ppf(self, spec: DistributionSpec, u):
        u = np.asarray(u, dtype=float)
        a = float(spec.params.get("a", 0.0))
        c = float(spec.params.get("c", 0.5))
        b = float(spec.params.get("b", 1.0))
        from scipy import stats

        return stats.triang.ppf(u, (c - a) / (b - a), loc=a, scale=b - a)

    def validate(self, spec: DistributionSpec) -> List[str]:
        if not all(k in spec.params for k in ("a", "c", "b")):
            return ["Parâmetros 'a', 'c', 'b' obrigatórios"]
        return []
