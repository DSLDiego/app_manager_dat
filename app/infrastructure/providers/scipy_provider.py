from __future__ import annotations

import functools
from typing import Dict, List, Tuple

import numpy as np
from scipy import stats

from app.domain.entities import DistributionSpec
from app.infrastructure.providers.base import BaseDistributionProvider


class ScipyProvider(BaseDistributionProvider):
    """Provider SciPy com cache de descoberta e de nomes de parâmetros."""

    provider_name = "scipy"

    _EXCLUDE = {"rv_continuous", "rv_discrete", "rv_histogram"}
    _CACHE: Dict[str, object] = {}

    @classmethod
    @functools.lru_cache(maxsize=1)
    def _discover(cls) -> Dict[str, object]:
        """Método `ScipyProvider._discover`.
            Parâmetros: `cls`.
            Retorna o resultado calculado a partir do estado local."""
        discovered: Dict[str, object] = {}
        for name in dir(stats):
            if name.startswith("_") or name in cls._EXCLUDE:
                continue
            obj = getattr(stats, name)
            if isinstance(obj, (stats.rv_continuous, stats.rv_discrete)):
                discovered[name] = obj
        return discovered

    def list_distributions(self) -> List[str]:
        """Método `ScipyProvider.list_distributions`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        return sorted(self._discover().keys())

    @functools.lru_cache(maxsize=256)
    def parameter_names(self, dist_name: str) -> Tuple[str, ...]:
        """Método `ScipyProvider.parameter_names`.
            Parâmetros: `self`, `dist_name`.
            Retorna o resultado calculado a partir do estado local."""
        dist = self._discover()[dist_name]
        shapes = getattr(dist, "shapes", None) or ""
        names = [s.strip() for s in shapes.split(",") if s.strip()]
        names.append("loc")
        if isinstance(dist, stats.rv_continuous):
            names.append("scale")
        return tuple(names)

    def _build(self, spec: DistributionSpec):
        """Método `ScipyProvider._build`.
            Parâmetros: `self`, `spec`.
            Retorna o resultado calculado a partir do estado local.
            Levanta: ValueError."""
        dist = self._discover().get(spec.name)
        if dist is None:
            raise ValueError(f"Distribuição SciPy desconhecida: {spec.name}")
        params = spec.params
        shapes = [s.strip() for s in (getattr(dist, "shapes", "") or "").split(",") if s.strip()]
        args = [float(params.get(s, 1.0)) for s in shapes]
        kwargs = {"loc": float(params.get("loc", 0.0))}
        if isinstance(dist, stats.rv_continuous):
            kwargs["scale"] = float(params.get("scale", 1.0))
        return dist, args, kwargs

    def sample(self, spec, size, rng):
        """Método `ScipyProvider.sample`.
            Parâmetros: `self`, `spec`, `size`, `rng`.
            Retorna o resultado calculado a partir do estado local."""
        dist, args, kwargs = self._build(spec)
        return dist.rvs(*args, size=size, random_state=rng, **kwargs)

    def ppf(self, spec, u):
        """Método `ScipyProvider.ppf`.
            Parâmetros: `self`, `spec`, `u`.
            Retorna o resultado calculado a partir do estado local."""
        dist, args, kwargs = self._build(spec)
        return dist.ppf(np.asarray(u, dtype=float), *args, **kwargs)

    def validate(self, spec):
        """Método `ScipyProvider.validate`.
            Parâmetros: `self`, `spec`.
            Retorna o resultado calculado a partir do estado local."""
        errors = []
        if spec.name not in self._discover():
            return [f"Distribuição SciPy desconhecida: {spec.name}"]
        try:
            self.sample(spec, 3, np.random.default_rng(0))
        except Exception as exc:
            errors.append(str(exc))
        return errors
