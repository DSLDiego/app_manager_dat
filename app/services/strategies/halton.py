"""Halton: sequência quasi-aleatória de baixa discrepância."""

from __future__ import annotations

from typing import List

import numpy as np


class HaltonStrategy:
    """Uniformes em [0,1) via scipy.stats.qmc.Halton (scramble + seed)."""

    name = "halton"

    def generate_uniforms(self, n: int, d: int, rng) -> np.ndarray:
        """Método `HaltonStrategy.generate_uniforms`.
            Parâmetros: `self`, `n`, `d`, `rng`.
            Retorna o resultado calculado a partir do estado local."""
        from scipy.stats import qmc

        sampler = qmc.Halton(d, scramble=True, seed=int(rng.integers(0, 2**31 - 1)))
        return sampler.random(n)


__all__ = ["HaltonStrategy"]
