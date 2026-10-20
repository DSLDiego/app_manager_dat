"""Compara dois experimentos: valores por variável + diff de .dat renderizado."""

from __future__ import annotations

import difflib
from dataclasses import dataclass
from typing import Dict, List, Optional

from app.infrastructure.experiment_repository import ExperimentRepository


@dataclass(frozen=True)
class VariableDiff:
    """Classe `VariableDiff` do módulo."""
    var_id: int
    value_a: Optional[float]
    value_b: Optional[float]
    abs_diff: Optional[float]
    rel_diff: Optional[float]


@dataclass(frozen=True)
class ComparisonResult:
    """Classe `ComparisonResult` do módulo."""
    exp_a_id: int
    exp_b_id: int
    diffs: List[VariableDiff]
    dat_text_a: str = ""
    dat_text_b: str = ""
    dat_diff: str = ""


class ComparisonService:
    """Classe `ComparisonService` do módulo."""
    def __init__(self, exp_repo: ExperimentRepository):
        """Método `ComparisonService.__init__`.
            Parâmetros: `self`, `exp_repo`."""
        self.exp_repo = exp_repo

    # ---------- ranking de divergência ----------
    @staticmethod
    def divergence_ranking(
        diffs: List[VariableDiff], top: Optional[int] = None
    ) -> List[VariableDiff]:
        """Diffs ordenados por divergência relativa (|Δ|/(|a|+|b|)). Determinístico."""
        def norm(d: VariableDiff) -> float:
            """Função `norm`.
                Parâmetros: `d`.
                Retorna o resultado calculado a partir do estado local."""
            if d.abs_diff is None:
                return -1.0  # faltantes por último
            sum_abs = abs(d.value_a or 0.0) + abs(d.value_b or 0.0)
            return 2.0 * abs(d.abs_diff) / (sum_abs + 1e-12)

        ranked = sorted(diffs, key=norm, reverse=True)
        return ranked[:top] if top is not None else ranked

    def compare(
        self,
        exp_a_id: int,
        exp_b_id: int,
        template_text: Optional[str] = None,
        renderer=None,
    ) -> ComparisonResult:
        """Método `ComparisonService.compare`.
            Parâmetros: `self`, `exp_a_id`, `exp_b_id`, `template_text`, `renderer`.
            Retorna o resultado calculado a partir do estado local."""
        a = self._fetch(exp_a_id)
        b = self._fetch(exp_b_id)

        var_ids = sorted(set(a["values"].keys()) | set(b["values"].keys()))

        diffs = [self._diff(var_id, a["values"], b["values"]) for var_id in var_ids]

        dat_a = dat_b = dat_diff = ""
        if template_text and renderer:
            dat_a = renderer(template_text, a["values"])
            dat_b = renderer(template_text, b["values"])
            dat_diff = "".join(difflib.unified_diff(
                dat_a.splitlines(keepends=True),
                dat_b.splitlines(keepends=True),
                fromfile=f"exp_{exp_a_id}",
                tofile=f"exp_{exp_b_id}",
            ))

        return ComparisonResult(exp_a_id, exp_b_id, diffs, dat_a, dat_b, dat_diff)

    @staticmethod
    def _diff(var_id: int, values_a: Dict[int, float], values_b: Dict[int, float]) -> VariableDiff:
        """Método `ComparisonService._diff`.
            Parâmetros: `var_id`, `values_a`, `values_b`.
            Retorna o resultado calculado a partir do estado local."""
        value_a = values_a.get(var_id)
        value_b = values_b.get(var_id)
        abs_diff = None
        rel_diff = None
        if value_a is not None and value_b is not None:
            abs_diff = value_b - value_a
            if value_a != 0:
                rel_diff = 100.0 * abs_diff / abs(value_a)
        return VariableDiff(var_id, value_a, value_b, abs_diff, rel_diff)

    def _fetch(self, external_id: int) -> Dict:
        """Método `ComparisonService._fetch`.
            Parâmetros: `self`, `external_id`.
            Retorna o resultado calculado a partir do estado local."""
        values = self.exp_repo.get_experiment_values(external_id)
        return {"external_id": external_id, "values": values}
