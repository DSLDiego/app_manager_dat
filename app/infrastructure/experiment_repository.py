"""Persistência de experimentos. Suporta milhões de linhas sem carregar nada."""

from __future__ import annotations

import json
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional


class ExperimentRepository:
    """Classe `ExperimentRepository` do módulo."""
    def __init__(self, db_path: str = "data/experiments.db"):
        """Método `ExperimentRepository.__init__`.
            Parâmetros: `self`, `db_path`."""
        if db_path != ":memory:":
            Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self._enable_wal()
        self._create_schema()

    def _enable_wal(self) -> None:
        """WAL + cache de memória para leitura concorrente e queries rápidas."""
        try:
            self.conn.execute("PRAGMA journal_mode=WAL")
            self.conn.execute("PRAGMA synchronous=NORMAL")
            self.conn.execute("PRAGMA temp_store=MEMORY")
            self.conn.execute("PRAGMA cache_size=-16000")  # 16 MB de page cache
            self.conn.execute("PRAGMA mmap_size=268435456")  # 256 MB de mmap
        except sqlite3.DatabaseError:
            pass

    def _create_schema(self):
        """Método `ExperimentRepository._create_schema`.
            Parâmetros: `self`."""
        with self.conn:
            self.conn.executescript(
                """
                PRAGMA journal_mode=WAL;
                PRAGMA synchronous=NORMAL;

                CREATE TABLE IF NOT EXISTS batches (
                    id TEXT PRIMARY KEY,
                    created_at TEXT,
                    method TEXT,
                    seed INTEGER,
                    n_experiments INTEGER,
                    correlation_json TEXT,
                    meta_json TEXT
                );

                CREATE TABLE IF NOT EXISTS experiments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    batch_id TEXT NOT NULL,
                    external_id INTEGER NOT NULL,
                    FOREIGN KEY(batch_id) REFERENCES batches(id)
                );

                CREATE TABLE IF NOT EXISTS experiment_values (
                    experiment_id INTEGER NOT NULL,
                    var_id INTEGER NOT NULL,
                    value REAL NOT NULL,
                    PRIMARY KEY (experiment_id, var_id),
                    FOREIGN KEY(experiment_id) REFERENCES experiments(id)
                );

                CREATE INDEX IF NOT EXISTS idx_exp_batch
                    ON experiments(batch_id, external_id);
                CREATE INDEX IF NOT EXISTS idx_vals_var
                    ON experiment_values(var_id);
                """
            )

    def create_batch(
        self,
        batch_id: str,
        method: str,
        seed: int,
        n_experiments: int,
        correlation: Optional[List[List[float]]] = None,
        meta: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Método `ExperimentRepository.create_batch`.
            Parâmetros: `self`, `batch_id`, `method`, `seed`, `n_experiments`, `correlation`, `meta`."""
        with self.conn:
            self.conn.execute(
                """
                INSERT OR REPLACE INTO batches
                (id, created_at, method, seed, n_experiments, correlation_json, meta_json)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    batch_id,
                    datetime.now().isoformat(),
                    method,
                    seed,
                    n_experiments,
                    json.dumps(correlation) if correlation else None,
                    json.dumps(meta or {}, ensure_ascii=False),
                ),
            )

    def list_batches(self, limit: int = 100) -> List[Dict[str, Any]]:
        """Método `ExperimentRepository.list_batches`.
            Parâmetros: `self`, `limit`.
            Retorna o resultado calculado a partir do estado local."""
        rows = self.conn.execute(
            """
            SELECT id, created_at, method, seed, n_experiments
            FROM batches ORDER BY created_at DESC LIMIT ?
            """,
            (limit,),
        ).fetchall()
        return [dict(r) for r in rows]

    def insert_result(
        self,
        batch_id: str,
        var_ids: List[int],
        matrix: List[List[float]],
    ) -> None:
        """Transação única em dois executemany — rápido para 1M linhas."""
        for i, row in enumerate(matrix):
            if len(row) != len(var_ids):
                raise ValueError(
                    f"Todas as variáveis devem ter valores. Experimento {i + 1} "
                    f"tem {len(row)} valores; esperado {len(var_ids)}."
                )

        with self.conn:
            start_id = self.conn.execute(
                "SELECT COALESCE(MAX(id), 0) + 1 AS next FROM experiments"
            ).fetchone()
            base_id = int(start_id["next"])

            exp_rows = [(base_id + i, batch_id, i + 1) for i in range(len(matrix))]
            self.conn.executemany(
                "INSERT INTO experiments(id, batch_id, external_id) VALUES (?, ?, ?)",
                exp_rows,
            )

            values_rows = []
            for offset, row in enumerate(matrix):
                exp_id = base_id + offset
                for vid, v in zip(var_ids, row):
                    values_rows.append((exp_id, int(vid), float(v)))
            self.conn.executemany(
                """
                INSERT INTO experiment_values(experiment_id, var_id, value)
                VALUES (?, ?, ?)
                """,
                values_rows,
            )

    def count(self, batch_id: Optional[str] = None) -> int:
        """Método `ExperimentRepository.count`.
            Parâmetros: `self`, `batch_id`.
            Retorna o resultado calculado a partir do estado local."""
        if batch_id is not None:
            row = self.conn.execute(
                "SELECT COUNT(*) AS n FROM experiments WHERE batch_id = ?",
                (batch_id,),
            ).fetchone()
        else:
            row = self.conn.execute("SELECT COUNT(*) AS n FROM experiments").fetchone()
        return int(row["n"]) if row else 0

    def clear_all(self) -> int:
        """Apaga todos os experimentos e lotes gerados. Retorna lotes removidos."""
        with self.conn:
            batches = self.conn.execute("SELECT COUNT(*) AS n FROM batches").fetchone()
            self.conn.execute("DELETE FROM experiment_values")
            self.conn.execute("DELETE FROM experiments")
            self.conn.execute("DELETE FROM batches")
            try:
                self.conn.execute(
                    "DELETE FROM sqlite_sequence WHERE name IN "
                    "('experiments', 'experiment_values')"
                )
            except sqlite3.OperationalError:
                pass  # sqlite_sequence não existe (sem AUTOINCREMENT usado ainda)
        return int(batches["n"]) if batches else 0

    def var_ids(self, batch_id: Optional[str] = None) -> List[int]:
        """Método `ExperimentRepository.var_ids`.
            Parâmetros: `self`, `batch_id`.
            Retorna o resultado calculado a partir do estado local."""
        if batch_id is not None:
            rows = self.conn.execute(
                """
                SELECT DISTINCT ev.var_id
                FROM experiment_values ev
                JOIN experiments e ON e.id = ev.experiment_id
                WHERE e.batch_id = ?
                ORDER BY ev.var_id
                """,
                (batch_id,),
            ).fetchall()
        else:
            rows = self.conn.execute(
                "SELECT DISTINCT var_id FROM experiment_values ORDER BY var_id"
            ).fetchall()
        return [int(r["var_id"]) for r in rows]

    def fetch_page(
        self,
        page_index: int,
        page_size: int,
        var_ids: Optional[List[int]] = None,
        batch_id: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """Método `ExperimentRepository.fetch_page`.
            Parâmetros: `self`, `page_index`, `page_size`, `var_ids`, `batch_id`.
            Retorna o resultado calculado a partir do estado local."""
        offset = max(0, page_index) * page_size
        if batch_id is not None:
            rows = self.conn.execute(
                """
                SELECT id, external_id, batch_id
                FROM experiments
                WHERE batch_id = ?
                ORDER BY external_id
                LIMIT ? OFFSET ?
                """,
                (batch_id, page_size, offset),
            ).fetchall()
        else:
            rows = self.conn.execute(
                """
                SELECT id, external_id, batch_id
                FROM experiments
                ORDER BY external_id
                LIMIT ? OFFSET ?
                """,
                (page_size, offset),
            ).fetchall()

        if not rows:
            return []

        ids = [r["id"] for r in rows]
        ph = ",".join("?" * len(ids))

        if var_ids:
            vph = ",".join("?" * len(var_ids))
            sql = f"""
                SELECT experiment_id, var_id, value
                FROM experiment_values
                WHERE experiment_id IN ({ph}) AND var_id IN ({vph})
            """
            params: List[Any] = list(ids) + list(var_ids)
        else:
            sql = f"""
                SELECT experiment_id, var_id, value
                FROM experiment_values
                WHERE experiment_id IN ({ph})
            """
            params = list(ids)

        vrows = self.conn.execute(sql, params).fetchall()

        by_exp: Dict[int, Dict[int, float]] = {}
        for vr in vrows:
            by_exp.setdefault(int(vr["experiment_id"]), {})[int(vr["var_id"])] = float(vr["value"])

        return [
            {
                "db_id": int(r["id"]),
                "external_id": int(r["external_id"]),
                "batch_id": r["batch_id"],
                "values": by_exp.get(int(r["id"]), {}),
            }
            for r in rows
        ]

    def get_variable_values(
        self, var_id: int, limit: Optional[int] = None, batch_id: Optional[str] = None
    ) -> List[float]:
        """Método `ExperimentRepository.get_variable_values`.
            Parâmetros: `self`, `var_id`, `limit`, `batch_id`.
            Retorna o resultado calculado a partir do estado local."""
        sql = "SELECT value FROM experiment_values"
        joins = " JOIN experiments e ON e.id = experiment_values.experiment_id"
        params: List[Any] = []
        if batch_id is not None:
            sql += joins + " WHERE experiment_values.var_id = ? AND e.batch_id = ?"
            params = [int(var_id), batch_id]
        else:
            sql += " WHERE experiment_values.var_id = ?"
            params = [int(var_id)]
        sql += " ORDER BY experiment_id"
        if limit is not None:
            sql += " LIMIT ?"
            params.append(int(limit))
        return [float(r["value"]) for r in self.conn.execute(sql, params).fetchall()]

    def get_all_values_by_var(self, var_ids: Optional[List[int]] = None) -> Dict[int, List[float]]:
        """Todos os valores por var_id (para min–max global no heatmap)."""
        result: Dict[int, List[float]] = {}
        if var_ids:
            ph = ",".join("?" * len(var_ids))
            sql = f"SELECT var_id, value FROM experiment_values WHERE var_id IN ({ph})"
            params: List[Any] = list(var_ids)
        else:
            sql = "SELECT var_id, value FROM experiment_values"
            params = []
        for r in self.conn.execute(sql, params).fetchall():
            result.setdefault(int(r["var_id"]), []).append(float(r["value"]))
        return result

    def get_experiment_values(self, external_id: int) -> Dict[int, float]:
        """Método `ExperimentRepository.get_experiment_values`.
            Parâmetros: `self`, `external_id`.
            Retorna o resultado calculado a partir do estado local.
            Levanta: ValueError."""
        row = self.conn.execute(
            "SELECT id FROM experiments WHERE external_id = ? LIMIT 1", (external_id,)
        ).fetchone()
        if not row:
            raise ValueError(f"Experimento {external_id} não encontrado.")
        vrows = self.conn.execute(
            "SELECT var_id, value FROM experiment_values WHERE experiment_id = ?",
            (row["id"],),
        ).fetchall()
        return {int(r["var_id"]): float(r["value"]) for r in vrows}

    def list_experiment_ids(self, limit: int = 200) -> List[int]:
        """Método `ExperimentRepository.list_experiment_ids`.
            Parâmetros: `self`, `limit`.
            Retorna o resultado calculado a partir do estado local."""
        rows = self.conn.execute(
            "SELECT external_id FROM experiments ORDER BY external_id LIMIT ?", (limit,)
        ).fetchall()
        return [int(r["external_id"]) for r in rows]

    def close(self):
        """Método `ExperimentRepository.close`."""
        self.conn.close()
