"""Gera uma amostra de 1 experimento para o preview do editor."""

from __future__ import annotations

from typing import Dict

from app.domain.entities import DistributionSpec, SamplingRequest
from app.services.sampling_service import SamplingService


class PreviewService:
    """Classe `PreviewService` do módulo."""
    def __init__(self, sampling_svc: SamplingService):
        """Método `PreviewService.__init__`.
            Parâmetros: `self`, `sampling_svc`."""
        self.sampling_svc = sampling_svc

    def sample_one(
        self,
        specs: Dict[int, DistributionSpec],
        seed: int = 42,
    ) -> Dict[int, float]:
        """Método `PreviewService.sample_one`.
            Parâmetros: `self`, `specs`, `seed`.
            Retorna o resultado calculado a partir do estado local."""
        from app.core.parsing import TOKEN_RE, token_var_id

        if not specs:
            request = SamplingRequest(
                var_ids=[],
                specs={},
                n_experiments=0,
                seed=seed,
                strategy="monte_carlo",
                workers=1,
            )
            return {}

        request = SamplingRequest(
            var_ids=list(specs.keys()),
            specs=specs,
            n_experiments=1,
            seed=seed,
            strategy="monte_carlo",
            workers=1,
        )
        result = self.sampling_svc.run(request)

        return {
            var_id: result.matrix[0][col]
            for col, var_id in enumerate(result.var_ids)
        }


    def render(
        self,
        template: str,
        specs: Dict[int, DistributionSpec],
        seed: int = 42,
    ) -> str:
        """Método `PreviewService.render`.
            Parâmetros: `self`, `template`, `specs`, `seed`.
            Retorna o resultado calculado a partir do estado local."""
        from app.core.parsing import TOKEN_RE, token_var_id

        values = self.sample_one(specs, seed)

        def replace(m):
            """Função `replace`.
                Parâmetros: `m`.
                Retorna o resultado calculado a partir do estado local."""
            var_id = token_var_id(m)
            value = values.get(var_id)
            return f"{value:.10g}" if value is not None else m.group(0)

        return TOKEN_RE.sub(replace, template)
