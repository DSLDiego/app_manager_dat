"""Serviço de amostragem. PURO — sem Qt, sem SQL, sem GUI."""

from __future__ import annotations

import time
from typing import Callable, Dict, List, Optional

import numpy as np

from app.domain.entities import (
    DistributionSpec,
    SamplingRequest,
    SamplingResult,
)
from app.core.spec_validation import validate_spec_params
from app.infrastructure.distribution_registry import DistributionRegistry
from app.services.sampling_cache import SamplingCache, cache_key
from app.services.strategies.correlated import iman_conover_reorder
from app.services.strategies.halton import HaltonStrategy

PPF_BLOCK_SIZE = 200_000  # T5452: blocos de pré-computo de ppf
from app.services.strategies.latin_hypercube import (
    LatinHypercubeStrategy,
    MonteCarloStrategy,
)
from app.services.strategies.sobol import SobolStrategy


class SamplingService:
    """Amostragem vetorizada: cada variável é amostrada em UMA chamada."""

    def __init__(self, registry: DistributionRegistry,
                 cache: Optional[SamplingCache] = None):
        """Método `SamplingService.__init__`.
            Parâmetros: `self`, `registry`, `cache`."""
        self.registry = registry
        self.cache = cache
        self._strategies = {
            "monte_carlo": MonteCarloStrategy(),
            "lhs": LatinHypercubeStrategy(),
            "sobol": SobolStrategy(),
            "halton": HaltonStrategy(),
        }

    def register_strategy(self, name: str, strategy) -> None:
        """Extensível: plugue Sobol, Halton, etc."""
        self._strategies[name] = strategy

    def run(
        self,
        request: SamplingRequest,
        progress_cb: Optional[Callable[[int, str], None]] = None,
    ) -> SamplingResult:
        """Método `SamplingService.run`.
            Parâmetros: `self`, `request`, `progress_cb`.
            Retorna o resultado calculado a partir do estado local.
            Levanta: ValueError."""
        start = time.perf_counter()

        strategy = self._strategies.get(request.strategy)
        if strategy is None and request.strategy != "correlated":
            raise ValueError(f"Estratégia desconhecida: {request.strategy}")

        var_ids = list(request.var_ids)
        n = request.n_experiments
        d = len(var_ids)

        if n <= 0 or d == 0:
            return SamplingResult(var_ids, [], request.seed, 0.0)

        missing = [v for v in var_ids if v not in request.specs]
        if missing:
            raise ValueError(
                "Todas as variáveis devem ter valores. "
                "Sem distribuição definida para: "
                + ", ".join(f"${v}" for v in missing[:10])
            )

        # R31: validação fina antes de qualquer amostragem
        spec_errors: list[str] = []
        for var_id in var_ids:
            spec = request.specs[var_id]
            for message in validate_spec_params(spec.provider, spec.params):
                spec_errors.append(f"{var_id}: {message}")
        if spec_errors:
            raise ValueError(
                "Parâmetros inválidos: " + "; ".join(spec_errors[:10])
            )

        key = None
        if self.cache is not None:
            key = cache_key(var_ids, request.specs, n, request.strategy, request.seed)
            cached = self.cache.get(key)
            if cached is not None:
                return cached

        rng = np.random.default_rng(request.seed)
        matrix = np.empty((n, d), dtype=float)

        if request.strategy == "correlated":
            matrix = self._sample_correlated(request, rng)
        else:
            uniforms = strategy.generate_uniforms(n, d, rng)

            # provider + spec resolvidos UMA vez por coluna (sem lookup no loop quente)
            col_plans = [
                (
                    int(var_id),
                    self.registry.get_provider(request.specs[var_id].provider),
                    request.specs[var_id],
                )
                for var_id in var_ids
            ]

            PPF_BLOCK = int(PPF_BLOCK_SIZE)
            for col, (var_id, provider, spec) in enumerate(col_plans):
                try:
                    if spec.provider == "fixed":
                        matrix[:, col] = spec.params.get("value", 0.0)
                    else:
                        u_col = uniforms[:, col]
                        if u_col.size <= PPF_BLOCK:
                            matrix[:, col] = provider.ppf(spec, u_col)
                        else:
                            # T5452: pré-computar ppf em blocos grandes —
                            # evita pico de memória intermediário da lib
                            for s0 in range(0, u_col.size, PPF_BLOCK):
                                matrix[s0 : s0 + PPF_BLOCK, col] = provider.ppf(
                                    spec, u_col[s0 : s0 + PPF_BLOCK]
                                )
                except Exception:
                    matrix[:, col] = provider.sample(spec, n, rng)

                if progress_cb:
                    percent = int(100 * (col + 1) / d)
                    progress_cb(percent, f"Variável {var_id} amostrada")

        duration = time.perf_counter() - start
        self._validate_complete(var_ids, matrix)

        result = SamplingResult(
            var_ids=var_ids,
            matrix=matrix.tolist(),
            seed_used=request.seed,
            duration_seconds=duration,
        )
        if key is not None:
            self.cache.put(key, result)
        return result

    @staticmethod
    def _validate_complete(var_ids, matrix: np.ndarray) -> None:
        """Garantia: TODA variável de TODO experimento precisa ter valor finito."""
        arr = np.asarray(matrix, dtype=float)
        if arr.size == 0:
            return
        if arr.ndim != 2 or arr.shape[1] != len(var_ids):
            raise ValueError("Matriz de amostragem incompleta.")
        if not np.isfinite(arr).all():
            bad = sorted(
                {int(var_ids[c]) for c in range(arr.shape[1]) if not np.isfinite(arr[:, c]).all()}
            )
            raise ValueError(
                "Todas as variáveis devem ter valores. "
                "Colunas com valores inválidos: " + ", ".join(f"${v}" for v in bad[:10])
            )

    def _sample_correlated(self, request: SamplingRequest, rng) -> np.ndarray:
        """Iman-Conover: induz correlação de posto mantendo marginais."""
        n = request.n_experiments
        d = len(request.var_ids)

        base = np.empty((n, d), dtype=float)
        for col, var_id in enumerate(request.var_ids):
            spec = request.specs[var_id]
            provider = self.registry.get_provider(spec.provider)
            base[:, col] = provider.sample(spec, n, rng)

        if request.correlation is None or d <= 1:
            return base

        corr = np.asarray(request.correlation, dtype=float)
        return iman_conover_reorder(base, corr)

    @staticmethod
    def p10_p50_p90(values: np.ndarray) -> Dict[str, float]:
        """Método `SamplingService.p10_p50_p90`.
            Parâmetros: `values`.
            Retorna o resultado calculado a partir do estado local."""
        if len(values) == 0:
            return {"p10": float("nan"), "p50": float("nan"), "p90": float("nan")}
        p10, p50, p90 = np.quantile(values, [0.10, 0.50, 0.90])
        return {"p10": float(p10), "p50": float(p50), "p90": float(p90)}
