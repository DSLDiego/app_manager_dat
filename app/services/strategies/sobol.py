from __future__ import annotations

import numpy as np
from scipy.stats import qmc


class SobolStrategy:
    """Sobol low-discrepancy sequence (scipy.stats.qmc.Sobol com scramble)."""

    name = "sobol"

    def generate_uniforms(self, n_samples: int, n_dims: int, rng) -> np.ndarray:
        """Método `SobolStrategy.generate_uniforms`.
            Parâmetros: `self`, `n_samples`, `n_dims`, `rng`.
            Retorna o resultado calculado a partir do estado local."""
        sampler = qmc.Sobol(d=n_dims, scramble=True, seed=rng)
        return sampler.random(n=n_samples)
