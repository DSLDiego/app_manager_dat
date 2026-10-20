"""Protocolos. Qualquer classe pode implementar sem herdar."""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Protocol

import numpy as np

from app.domain.entities import DistributionSpec


class DistributionProvider(Protocol):
    """Qualquer provider de distribuição."""

    provider_name: str

    def list_distributions(self) -> List[str]:
                                               """Método `DistributionProvider.list_distributions`.
                                                   Parâmetros: `self`."""
                                               ...

    def parameter_names(self, dist_name: str) -> List[str]:
                                                            """Método `DistributionProvider.parameter_names`.
                                                                Parâmetros: `self`, `dist_name`."""
                                                            ...

    def sample(
        self,
        spec: DistributionSpec,
        size: int,
        rng: np.random.Generator,
    ) -> np.ndarray:
                     """Método `DistributionProvider.sample`.
                         Parâmetros: `self`, `spec`, `size`, `rng`."""
                     ...

    def ppf(self, spec: DistributionSpec, u: np.ndarray) -> np.ndarray:
                                                                        """Método `DistributionProvider.ppf`.
                                                                            Parâmetros: `self`, `spec`, `u`."""
                                                                        ...

    def validate(self, spec: DistributionSpec) -> List[str]:
                                                             """Método `DistributionProvider.validate`.
                                                                 Parâmetros: `self`, `spec`."""
                                                             ...


class LogRepository(Protocol):
    """Classe `LogRepository` do módulo."""
    def log(
        self,
        level: str,
        category: str,
        action: str,
        entity_type: Optional[str] = None,
        entity_id: Optional[int] = None,
        message: str = "",
        payload: Optional[Dict[str, Any]] = None,
    ) -> None:
               """Método `LogRepository.log`.
                   Parâmetros: `self`, `level`, `category`, `action`, `entity_type`, `entity_id`, `message`, `payload`."""
               ...

    def fetch(
        self,
        category: Optional[str] = None,
        level: Optional[str] = None,
        search: Optional[str] = None,
        limit: int = 1000,
    ) -> List[Dict[str, Any]]:
                               """Método `LogRepository.fetch`.
                                   Parâmetros: `self`, `category`, `level`, `search`, `limit`."""
                               ...


class SamplingStrategy(Protocol):
    """Classe `SamplingStrategy` do módulo."""
    name: str

    def generate_uniforms(
        self,
        n_samples: int,
        n_dims: int,
        rng: np.random.Generator,
    ) -> np.ndarray:
        """Retorna matriz (n_samples, n_dims) em [0,1]."""
        ...
