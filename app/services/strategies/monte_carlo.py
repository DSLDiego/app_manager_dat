from __future__ import annotations

import numpy as np


class MonteCarloStrategy:
    """Classe `MonteCarloStrategy` do módulo."""
    name = "monte_carlo"

    def generate_uniforms(self, n_samples: int, n_dims: int, rng) -> np.ndarray:
        """Método `MonteCarloStrategy.generate_uniforms`.
            Parâmetros: `self`, `n_samples`, `n_dims`, `rng`.
            Retorna o resultado calculado a partir do estado local."""
        return rng.random((n_samples, n_dims))
