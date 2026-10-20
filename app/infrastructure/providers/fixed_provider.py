from __future__ import annotations

from typing import List

import numpy as np

from app.domain.entities import DistributionSpec
from app.infrastructure.providers.base import BaseDistributionProvider


class FixedProvider(BaseDistributionProvider):
    """Distribuição degenerada: valor constante (útil p/ std = 0)."""

    provider_name = "fixed"

    def list_distributions(self) -> List[str]:
        """Método `FixedProvider.list_distributions`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        return ["value"]

    def parameter_names(self, dist_name: str) -> List[str]:
        """Método `FixedProvider.parameter_names`.
            Parâmetros: `self`, `dist_name`.
            Retorna o resultado calculado a partir do estado local."""
        return ["value"]

    def sample(self, spec, size, rng):
        """Método `FixedProvider.sample`.
            Parâmetros: `self`, `spec`, `size`, `rng`.
            Retorna o resultado calculado a partir do estado local."""
        return np.full(size, float(spec.params.get("value", 0.0)))

    def ppf(self, spec, u):
        """Método `FixedProvider.ppf`.
            Parâmetros: `self`, `spec`, `u`.
            Retorna o resultado calculado a partir do estado local."""
        return np.full(np.asarray(u).shape, float(spec.params.get("value", 0.0)))

    def validate(self, spec):
        """Método `FixedProvider.validate`.
            Parâmetros: `self`, `spec`.
            Retorna o resultado calculado a partir do estado local."""
        return [] if "value" in spec.params else ["Parâmetro 'value' obrigatório"]
