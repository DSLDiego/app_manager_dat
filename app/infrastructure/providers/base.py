from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List

import numpy as np

from app.domain.entities import DistributionSpec


class BaseDistributionProvider(ABC):
    """Qualquer novo provider herda desta classe e é registrado automaticamente."""

    provider_name: str = ""
    description: str = ""

    @abstractmethod
    def list_distributions(self) -> List[str]:
                                               """Método `BaseDistributionProvider.list_distributions`.
                                                   Parâmetros: `self`."""
                                               ...

    @abstractmethod
    def parameter_names(self, dist_name: str) -> List[str]:
                                                            """Método `BaseDistributionProvider.parameter_names`.
                                                                Parâmetros: `self`, `dist_name`."""
                                                            ...

    @abstractmethod
    def sample(
        self,
        spec: DistributionSpec,
        size: int,
        rng: np.random.Generator,
    ) -> np.ndarray:
                     """Método `BaseDistributionProvider.sample`.
                         Parâmetros: `self`, `spec`, `size`, `rng`."""
                     ...

    @abstractmethod
    def validate(self, spec: DistributionSpec) -> List[str]:
                                                             """Método `BaseDistributionProvider.validate`.
                                                                 Parâmetros: `self`, `spec`."""
                                                             ...

    def ppf(self, spec: DistributionSpec, u: np.ndarray) -> np.ndarray:
        """Método `BaseDistributionProvider.ppf`.
            Parâmetros: `self`, `spec`, `u`.
            Levanta: NotImplementedError."""
        raise NotImplementedError("Provider não suporta PPF")

    def param_schema(self, dist_name: str) -> List[dict]:
        """T5132: schema tipado usado pelos dialogs: [{name, default, type, min, max}].

        type é "float" (padrão) ou "int" — o helper cria QDoubleSpinBox
        ou QSpinBox e a coleta converte o valor. Sobrescreva para
        defaults/ranges específicos; o genérico deriva de parameter_names.
        """
        return [
            {"name": pname, "type": "float", "default": 1.0}
            for pname in self.parameter_names(dist_name)
        ]
