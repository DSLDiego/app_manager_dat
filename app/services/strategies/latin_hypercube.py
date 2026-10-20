from __future__ import annotations

import numpy as np
from scipy.stats import qmc


class MonteCarloStrategy:
    """Classe `MonteCarloStrategy` do módulo."""
    name = "monte_carlo"

    def generate_uniforms(self, n_samples: int, n_dims: int, rng) -> np.ndarray:
        """Método `MonteCarloStrategy.generate_uniforms`.
            Parâmetros: `self`, `n_samples`, `n_dims`, `rng`.
            Retorna o resultado calculado a partir do estado local."""
        return rng.random((n_samples, n_dims))


class LatinHypercubeStrategy:
    """Classe `LatinHypercubeStrategy` do módulo."""
    name = "lhs"

    def generate_uniforms(self, n_samples: int, n_dims: int, rng) -> np.ndarray:
        """Método `LatinHypercubeStrategy.generate_uniforms`.
            Parâmetros: `self`, `n_samples`, `n_dims`, `rng`.
            Retorna o resultado calculado a partir do estado local."""
        sampler = qmc.LatinHypercube(d=n_dims, seed=rng)
        return sampler.random(n=n_samples)
