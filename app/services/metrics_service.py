"""Agrega métricas de uso. Consultas SQL otimizadas com índices."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Tuple

from app.infrastructure.async_log_repository import AsyncLogRepository
from app.infrastructure.experiment_repository import ExperimentRepository


@dataclass(frozen=True)
class KpiSummary:
    """Classe `KpiSummary` do módulo."""
    total_batches: int
    total_experiments: int
    total_templates: int
    total_versions: int
    total_logs: int
    logs_24h: int
    logs_7d: int


class MetricsService:
    """Classe `MetricsService` do módulo."""
    def __init__(
        self,
        exp_repo: ExperimentRepository,
        template_conn,
        log_repo: AsyncLogRepository,
    ):
        """Método `MetricsService.__init__`.
            Parâmetros: `self`, `exp_repo`, `template_conn`, `log_repo`."""
        self.exp_repo = exp_repo
        self._template_conn = template_conn
        self.log_repo = log_repo

    def summary(self) -> KpiSummary:
        """Método `MetricsService.summary`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        if hasattr(self.log_repo, "wait_pending"):
            self.log_repo.wait_pending(timeout=2.0)
        exp_conn = self.exp_repo.conn

        total_batches = exp_conn.execute("SELECT COUNT(*) FROM batches").fetchone()[0]
        total_experiments = exp_conn.execute("SELECT COUNT(*) FROM experiments").fetchone()[0]
        total_templates = self._template_conn.execute(
            "SELECT COUNT(*) FROM templates"
        ).fetchone()[0]
        total_versions = self._template_conn.execute(
            "SELECT COUNT(*) FROM template_versions"
        ).fetchone()[0]
        total_logs = self.log_repo.count()

        now = datetime.now()
        cutoff_24 = (now - timedelta(hours=24)).isoformat()
        cutoff_7d = (now - timedelta(days=7)).isoformat()

        logs_24h = self._log_count_since(cutoff_24)
        logs_7d = self._log_count_since(cutoff_7d)

        return KpiSummary(
            total_batches, total_experiments, total_templates,
            total_versions, total_logs, logs_24h, logs_7d,
        )

    def _log_count_since(self, cutoff: str) -> int:
        """Método `MetricsService._log_count_since`.
            Parâmetros: `self`, `cutoff`.
            Retorna o resultado calculado a partir do estado local."""
        row = self.log_repo.conn.execute(
            "SELECT COUNT(*) FROM logs WHERE created_at >= ?", (cutoff,),
        ).fetchone()
        return int(row[0])

    def experiments_per_batch(self, limit: int = 10) -> List[Tuple[str, int]]:
        """Método `MetricsService.experiments_per_batch`.
            Parâmetros: `self`, `limit`.
            Retorna o resultado calculado a partir do estado local."""
        rows = self.exp_repo.conn.execute(
            """
            SELECT b.id AS batch_id, COUNT(e.id) AS n
            FROM batches b
            LEFT JOIN experiments e ON e.batch_id = b.id
            GROUP BY b.id
            ORDER BY b.created_at DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
        return [(r["batch_id"], int(r["n"])) for r in rows]

    def actions_per_day(self, days: int = 14) -> List[Tuple[str, int]]:
        """Método `MetricsService.actions_per_day`.
            Parâmetros: `self`, `days`.
            Retorna o resultado calculado a partir do estado local."""
        cutoff = (datetime.now() - timedelta(days=days)).isoformat()
        rows = self.log_repo.conn.execute(
            """
            SELECT substr(created_at, 1, 10) AS day, COUNT(*) AS n
            FROM logs
            WHERE created_at >= ?
            GROUP BY day
            ORDER BY day
            """,
            (cutoff,),
        ).fetchall()
        return [(r["day"], int(r["n"])) for r in rows]

    def top_actions(self, limit: int = 10) -> List[Tuple[str, int]]:
        """Método `MetricsService.top_actions`.
            Parâmetros: `self`, `limit`.
            Retorna o resultado calculado a partir do estado local."""
        rows = self.log_repo.conn.execute(
            """
            SELECT action, COUNT(*) AS n
            FROM logs
            WHERE action IS NOT NULL AND action != ''
            GROUP BY action
            ORDER BY n DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
        return [(r["action"], int(r["n"])) for r in rows]
