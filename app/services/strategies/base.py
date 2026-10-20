from __future__ import annotations

from typing import Protocol, Union, runtime_checkable

import numpy as np


@runtime_checkable
class UnionSamplingStrategy(Protocol):
    """Contrato das estratégias de amostragem."""

    name: str

    def generate_uniforms(self, n_samples: int, n_dims: int, rng) -> np.ndarray:
                                                                                 """Método `UnionSamplingStrategy.generate_uniforms`.
                                                                                     Parâmetros: `self`, `n_samples`, `n_dims`, `rng`."""
                                                                                 ...


def make_strategy_fn(name: str, fn):
    """Anota uma função com propriedade name (auxiliar p/ extensões)."""
    fn.name = name
    return fn
