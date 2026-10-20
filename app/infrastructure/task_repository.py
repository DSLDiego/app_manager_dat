"""Fila persistente de tarefas em SQLite. Resumível a partir do cursor."""

from __future__ import annotations

import json
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from app.domain.tasks import Task, TaskKind, TaskState


class TaskRepository:
    """Classe `TaskRepository` do módulo."""
    def __init__(self, db_path: str = "data/tasks.db"):
        """Método `TaskRepository.__init__`.
            Parâmetros: `self`, `db_path`."""
        if db_path != ":memory:":
            Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self._enable_wal()
        self._create_schema()

    def _enable_wal(self) -> None:
        """Método `TaskRepository._enable_wal`.
            Parâmetros: `self`."""
        try:
            self.conn.execute("PRAGMA journal_mode=WAL")
        except sqlite3.DatabaseError:
            pass

    def _create_schema(self) -> None:
        """Método `TaskRepository._create_schema`.
            Parâmetros: `self`."""
        with self.conn:
            self.conn.executescript(
                """
                PRAGMA journal_mode = WAL;
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    kind TEXT NOT NULL,
                    payload_json TEXT NOT NULL,
                    state TEXT NOT NULL,
                    priority INTEGER DEFAULT 0,
                    progress INTEGER DEFAULT 0,
                    cursor_json TEXT,
                    error TEXT,
                    created_at TEXT,
                    updated_at TEXT
                );
                CREATE INDEX IF NOT EXISTS idx_tasks_state ON tasks(state, created_at);
                """
            )
            # migração para bancos criados antes da prioridade (R32)
            columns = {
                row["name"]
                for row in self.conn.execute("PRAGMA table_info(tasks)").fetchall()
            }
            if "priority" not in columns:
                self.conn.execute(
                    "ALTER TABLE tasks ADD COLUMN priority INTEGER DEFAULT 0"
                )

    def create(
        self, kind: TaskKind, payload: Dict[str, Any], priority: int = 0
    ) -> Task:
        """Método `TaskRepository.create`.
            Parâmetros: `self`, `kind`, `payload`, `priority`.
            Retorna o resultado calculado a partir do estado local."""
        now = datetime.now().isoformat()
        with self.conn:
            cur = self.conn.execute(
                """
                INSERT INTO tasks(kind, payload_json, state, priority, progress,
                                  cursor_json, created_at, updated_at)
                VALUES (?, ?, ?, ?, 0, '{}', ?, ?)
                """,
                (kind.value, json.dumps(payload, ensure_ascii=False),
                 TaskState.PENDING.value, int(priority), now, now),
            )
        return self.get(int(cur.lastrowid))

    def get(self, task_id: int) -> Optional[Task]:
        """Método `TaskRepository.get`.
            Parâmetros: `self`, `task_id`.
            Retorna o resultado calculado a partir do estado local."""
        r = self.conn.execute("SELECT * FROM tasks WHERE id=?", (task_id,)).fetchone()
        return self._to_task(r) if r else None

    def next_pending(self) -> Optional[Task]:
        """Método `TaskRepository.next_pending`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        r = self.conn.execute(
            "SELECT * FROM tasks WHERE state=? "
            "ORDER BY priority DESC, created_at ASC, id ASC LIMIT 1",
            (TaskState.PENDING.value,),
        ).fetchone()
        return self._to_task(r) if r else None

    def list_all(self, limit: int = 300) -> List[Task]:
        """Método `TaskRepository.list_all`.
            Parâmetros: `self`, `limit`.
            Retorna o resultado calculado a partir do estado local."""
        rows = self.conn.execute(
            "SELECT * FROM tasks ORDER BY id DESC LIMIT ?", (limit,)
        ).fetchall()
        return [self._to_task(r) for r in rows]

    def update_progress(self, task_id: int, percent: int, cursor: Dict[str, Any]) -> None:
        """Método `TaskRepository.update_progress`.
            Parâmetros: `self`, `task_id`, `percent`, `cursor`."""
        with self.conn:
            self.conn.execute(
                """
                UPDATE tasks SET state=?, progress=?, cursor_json=?, updated_at=?
                WHERE id=?
                """,
                (TaskState.RUNNING.value, int(percent),
                 json.dumps(cursor, ensure_ascii=False),
                 datetime.now().isoformat(), task_id),
            )

    def complete(self, task_id: int) -> None:
        """Método `TaskRepository.complete`.
            Parâmetros: `self`, `task_id`."""
        with self.conn:
            self.conn.execute(
                "UPDATE tasks SET state=?, progress=100, updated_at=? WHERE id=?",
                (TaskState.COMPLETED.value, datetime.now().isoformat(), task_id),
            )

    def fail(self, task_id: int, error: str) -> None:
        """Método `TaskRepository.fail`.
            Parâmetros: `self`, `task_id`, `error`."""
        with self.conn:
            self.conn.execute(
                "UPDATE tasks SET state=?, error=?, updated_at=? WHERE id=?",
                (TaskState.FAILED.value, error, datetime.now().isoformat(), task_id),
            )

    def pause(self, task_id: int) -> None:
        """Método `TaskRepository.pause`.
            Parâmetros: `self`, `task_id`."""
        with self.conn:
            self.conn.execute(
                "UPDATE tasks SET state=?, updated_at=? WHERE id=?",
                (TaskState.PAUSED.value, datetime.now().isoformat(), task_id),
            )

    def resume(self, task_id: int) -> None:
        """Método `TaskRepository.resume`.
            Parâmetros: `self`, `task_id`."""
        with self.conn:
            self.conn.execute(
                "UPDATE tasks SET state=?, updated_at=? WHERE id=?",
                (TaskState.PENDING.value, datetime.now().isoformat(), task_id),
            )

    def recover_interrupted(self) -> int:
        """Chamado no startup: RUNNING → PENDING (crash recovery)."""
        with self.conn:
            cur = self.conn.execute(
                "UPDATE tasks SET state=?, updated_at=? WHERE state=?",
                (TaskState.PENDING.value, datetime.now().isoformat(),
                 TaskState.RUNNING.value),
            )
            return cur.rowcount

    @staticmethod
    def _to_task(r: sqlite3.Row) -> Task:
        """Método `TaskRepository._to_task`.
            Parâmetros: `r`.
            Retorna o resultado calculado a partir do estado local."""
        return Task(
            id=int(r["id"]),
            kind=TaskKind(r["kind"]),
            payload=json.loads(r["payload_json"]),
            priority=int(r["priority"] or 0) if "priority" in r.keys() else 0,
            state=TaskState(r["state"]),
            progress=int(r["progress"] or 0),
            cursor=json.loads(r["cursor_json"] or "{}"),
            error=r["error"],
            created_at=r["created_at"] or "",
            updated_at=r["updated_at"] or "",
        )

    def close(self) -> None:
        """Método `TaskRepository.close`.
            Parâmetros: `self`."""
        self.conn.close()
