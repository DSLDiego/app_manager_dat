"""Compara estatísticas de dois batches."""

from __future__ import annotations

from typing import Dict, List

import numpy as np

from app.domain.batch_comparison import (
    BatchComparisonResult,
    BatchVariableStats,
)
from app.infrastructure.experiment_repository import ExperimentRepository


class BatchComparisonService:
    """Classe `BatchComparisonService` do módulo."""
    def __init__(self, exp_repo: ExperimentRepository):
        """Método `BatchComparisonService.__init__`.
            Parâmetros: `self`, `exp_repo`."""
        self.exp_repo = exp_repo

    def compare(self, batch_a_id: str, batch_b_id: str) -> BatchComparisonResult:
        """Método `BatchComparisonService.compare`.
            Parâmetros: `self`, `batch_a_id`, `batch_b_id`.
            Retorna o resultado calculado a partir do estado local."""
        values_a = self._values_by_var(batch_a_id)
        values_b = self._values_by_var(batch_b_id)

        all_vars = sorted(set(values_a) | set(values_b))
        variables = [
            self._compute(var_id, values_a.get(var_id, []), values_b.get(var_id, []))
            for var_id in all_vars
        ]

        return BatchComparisonResult(
            batch_a_id=batch_a_id,
            batch_b_id=batch_b_id,
            n_a=self._count(batch_a_id),
            n_b=self._count(batch_b_id),
            variables=variables,
        )

    def values_by_var_aligned(self, batch_id: str) -> Dict[int, List[float]]:
        """Valores por variável ordenados por external_id (alinhável)."""
        rows = self.exp_repo.conn.execute(
            """
            SELECT v.var_id AS var_id, v.value AS value
            FROM experiment_values v
            JOIN experiments e ON e.id = v.experiment_id
            WHERE e.batch_id = ?
            ORDER BY e.external_id, v.var_id
            """,
            (batch_id,),
        ).fetchall()
        grouped: Dict[int, List[float]] = {}
        for r in rows:
            grouped.setdefault(int(r["var_id"]), []).append(float(r["value"]))
        return grouped

    def scatter(self, batch_a_id: str, batch_b_id: str, var_id: int):
        """T5441: pares (a, b) de uma variável, alinhados por experimento.
        Retorna {xs, ys, pearson} para o plot (QPainter/matplotlib)."""
        from app.services.comparison_round34 import scatter_points

        va = self.values_by_var_aligned(batch_a_id).get(int(var_id), [])
        vb = self.values_by_var_aligned(batch_b_id).get(int(var_id), [])
        xs, ys, pearson = scatter_points(va, vb)
        return {"xs": xs, "ys": ys, "pearson": pearson}

    def rank_divergent(self, batch_a_id: str, batch_b_id: str, top=None):
        """T5442: variáveis mais divergentes entre dois batches (puro)."""
        from app.services.comparison_round34 import (
            batch_divergence_ranking,
            format_batch_ranking,
        )

        va = self.values_by_var_aligned(batch_a_id)
        vb = self.values_by_var_aligned(batch_b_id)
        stats = []
        for var_id in sorted(set(va) | set(vb)):
            a_, b_ = va.get(var_id, []), vb.get(var_id, [])
            if not a_ or not b_:
                continue
            stats.append({
                "var_id": int(var_id),
                "mean_a": float(np.mean(a_)),
                "mean_b": float(np.mean(b_)),
                "std_a": float(np.std(a_)),
                "std_b": float(np.std(b_)),
            })
        ranked = batch_divergence_ranking(stats, top=top)
        for row in ranked:
            row["bar"] = format_batch_ranking([row])[0]
        return ranked

    def _count(self, batch_id: str) -> int:
        """Método `BatchComparisonService._count`.
            Parâmetros: `self`, `batch_id`.
            Retorna o resultado calculado a partir do estado local."""
        r = self.exp_repo.conn.execute(
            "SELECT COUNT(*) FROM experiments WHERE batch_id=?", (batch_id,),
        ).fetchone()
        return int(r[0]) if r else 0

    def _values_by_var(self, batch_id: str) -> Dict[int, List[float]]:
        """Método `BatchComparisonService._values_by_var`.
            Parâmetros: `self`, `batch_id`.
            Retorna o resultado calculado a partir do estado local."""
        rows = self.exp_repo.conn.execute(
            """
            SELECT v.var_id AS var_id, v.value AS value
            FROM experiment_values v
            JOIN experiments e ON e.id = v.experiment_id
            WHERE e.batch_id = ?
            """,
            (batch_id,),
        ).fetchall()

        grouped: Dict[int, List[float]] = {}
        for r in rows:
            grouped.setdefault(int(r["var_id"]), []).append(float(r["value"]))
        return grouped

    @staticmethod
    def _safe_mean(arr: List[float]) -> float:
        """Método `BatchComparisonService._safe_mean`.
            Parâmetros: `arr`.
            Retorna o resultado calculado a partir do estado local."""
        return float(np.mean(arr)) if arr else float("nan")

    @staticmethod
    def _safe_q(arr: List[float], q: float) -> float:
        """Método `BatchComparisonService._safe_q`.
            Parâmetros: `arr`, `q`.
            Retorna o resultado calculado a partir do estado local."""
        return float(np.quantile(arr, q)) if arr else float("nan")

    def _compute(self, var_id: int, a: List[float], b: List[float]) -> BatchVariableStats:
        """Método `BatchComparisonService._compute`.
            Parâmetros: `self`, `var_id`, `a`, `b`.
            Retorna o resultado calculado a partir do estado local."""
        mean_a = self._safe_mean(a)
        mean_b = self._safe_mean(b)

        delta = mean_b - mean_a
        if np.isnan(delta) or mean_a == 0:
            delta_pct = None
        else:
            delta_pct = 100.0 * delta / abs(mean_a)

        return BatchVariableStats(
            var_id=var_id,
            mean_a=mean_a,
            mean_b=mean_b,
            p10_a=self._safe_q(a, 0.1),
            p10_b=self._safe_q(b, 0.1),
            p50_a=self._safe_q(a, 0.5),
            p50_b=self._safe_q(b, 0.5),
            p90_a=self._safe_q(a, 0.9),
            p90_b=self._safe_q(b, 0.9),
            mean_delta=delta,
            mean_delta_pct=delta_pct,
        )
