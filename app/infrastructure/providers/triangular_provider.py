from __future__ import annotations

from typing import List

import numpy as np

from app.domain.entities import DistributionSpec
from app.infrastructure.providers.base import BaseDistributionProvider


class TriangularProvider(BaseDistributionProvider):
    """Distribuição triangular builtin: low, mode, high."""

    provider_name = "triangular"

    def param_schema(self, dist_name: str) -> list[dict]:
        """Método `TriangularProvider.param_schema`.
            Parâmetros: `self`, `dist_name`.
            Retorna o resultado calculado a partir do estado local."""
        return [
            {"name": "low", "default": 0.0, "type": "float"},
            {"name": "mode", "default": 1.0, "type": "float"},
            {"name": "high", "default": 2.0, "type": "float"},
        ]

    def list_distributions(self) -> List[str]:
        """Método `TriangularProvider.list_distributions`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        return ["value"]

    def parameter_names(self, dist_name: str) -> List[str]:
        """Método `TriangularProvider.parameter_names`.
            Parâmetros: `self`, `dist_name`.
            Retorna o resultado calculado a partir do estado local."""
        return ["low", "mode", "high"]

    def sample(self, spec, size, rng):
        """Método `TriangularProvider.sample`.
            Parâmetros: `self`, `spec`, `size`, `rng`.
            Retorna o resultado calculado a partir do estado local."""
        params = self._params(spec)
        low, mode, high = params
        n = size if isinstance(size, int) else len(np.asarray(size))
        base = rng.triangular(low, high, mode, size=n)
        return np.atleast_1d(np.asarray(base, dtype=float))

    def ppf(self, spec, u):
        """Método `TriangularProvider.ppf`.
            Parâmetros: `self`, `spec`, `u`.
            Retorna o resultado calculado a partir do estado local."""
        low, mode, high = self._params(spec)
        u = np.atleast_1d(np.asarray(u, dtype=float))
        if high <= low:
            return np.full(u.shape, low)
        c = (mode - low) / (high - low)
        result = np.empty_like(u)
        left = u < c
        with np.errstate(divide="ignore", invalid="ignore"):
            result[left] = low + (mode - low) * np.sqrt(u[left] / c)
            result[~left] = high - (high - mode) * np.sqrt((1.0 - u[~left]) / (1.0 - c))
        return np.clip(result, low, high)

    def validate(self, spec) -> List[str]:
        """Método `TriangularProvider.validate`.
            Parâmetros: `self`, `spec`.
            Retorna o resultado calculado a partir do estado local."""
        errors: List[str] = []
        for key in self.parameter_names("value"):
            if key not in spec.params:
                errors.append(f"Parâmetro '{key}' obrigatório")
        if errors:
            return errors
        low, mode, high = self._params(spec)
        if not (low < mode < high):
            errors.append("Espera-se low < mode < high")
        return errors

    @staticmethod
    def _params(spec: DistributionSpec):
        """Método `TriangularProvider._params`.
            Parâmetros: `spec`.
            Retorna o resultado calculado a partir do estado local."""
        p = spec.params
        return (
            float(p.get("low", 0.0)),
            float(p.get("mode", 0.0)),
            float(p.get("high", 0.0)),
        )
