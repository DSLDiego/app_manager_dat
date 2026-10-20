"""Estratégias de amostragem (uniformes em [0,1] + correlação de postos)."""

from app.services.strategies.base import UnionSamplingStrategy, make_strategy_fn
from app.services.strategies.correlated import CorrelatedStrategy, iman_conover_reorder
from app.services.strategies.halton import HaltonStrategy
from app.services.strategies.latin_hypercube import LatinHypercubeStrategy, MonteCarloStrategy
from app.services.strategies.sobol import SobolStrategy

__all__ = [
    "CorrelatedStrategy",
    "HaltonStrategy",
    "LatinHypercubeStrategy",
    "MonteCarloStrategy",
    "SobolStrategy",
    "UnionSamplingStrategy",
    "iman_conover_reorder",
    "make_strategy_fn",
]
