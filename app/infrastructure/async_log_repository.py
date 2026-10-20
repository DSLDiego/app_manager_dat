"""Log repository com fila em background — não trava a UI."""

from __future__ import annotations

import json
import queue
import sqlite3
import threading
from datetime import datetime, timedelta as _timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional

_BATCH_SQL = """
INSERT INTO logs (created_at, level, category, action,
                  entity_type, entity_id, message, payload_json)
VALUES (:created_at, :level, :category, :action,
        :entity_type, :entity_id, :message, :payload_json)
"""

_SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    level TEXT,
    category TEXT,
    action TEXT,
    entity_type TEXT,
    entity_id INTEGER,
    message TEXT,
    payload_json TEXT
);
CREATE INDEX IF NOT EXISTS idx_logs_category ON logs(category);
CREATE INDEX IF NOT EXISTS idx_logs_level ON logs(level);
"""


_FLUSH_ALL = object()  # marcador: drena a fila sem encerrar o writer


class AsyncLogRepository:
    """Escrita em thread separada. Grava em lotes; leitura nunca bloqueia."""

    def __init__(self, db_path: str = "logs/studio_logs.db", batch_size: int = 100):
        """Método `AsyncLogRepository.__init__`.
            Parâmetros: `self`, `db_path`, `batch_size`."""
        if db_path != ":memory:":
            Path(db_path).parent.mkdir(parents=True, exist_ok=True)

        self.db_path = db_path
        self.batch_size = batch_size
        self._queue: "queue.Queue[Any]" = queue.Queue()
        self._stop = threading.Event()
        self._drained = threading.Event()

        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self._lock = threading.Lock()

        self._create_schema()

        self._writer_thread = threading.Thread(target=self._writer_loop, daemon=True)
        self._writer_thread.start()

    def _create_schema(self) -> None:
        """Método `AsyncLogRepository._create_schema`.
            Parâmetros: `self`."""
        with self._lock, self.conn:
            self.conn.executescript(_SCHEMA_SQL)

    def log(
        self,
        level: str,
        category: str,
        action: str,
        entity_type: Optional[str] = None,
        entity_id: Optional[int] = None,
        message: str = "",
        payload: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Não-bloqueante. Retorna imediatamente."""
        self._queue.put(
            {
                "created_at": datetime.now().isoformat(),
                "level": level,
                "category": category,
                "action": action,
                "entity_type": entity_type,
                "entity_id": entity_id,
                "message": message,
                "payload_json": json.dumps(payload or {}, ensure_ascii=False),
            }
        )

    def _writer_loop(self) -> None:
        """Método `AsyncLogRepository._writer_loop`.
            Parâmetros: `self`."""
        try:
            while True:
                batch: List[dict] = []
                try:
                    item = self._queue.get(timeout=0.5)
                except queue.Empty:
                    if self._stop.is_set():
                        break
                    continue
                if item is None:
                    self._flush(batch)
                    break
                if item is _FLUSH_ALL:
                    self._flush(batch)
                    self._drained.set()
                    continue
                batch.append(item)
                while len(batch) < self.batch_size:
                    try:
                        item = self._queue.get_nowait()
                    except queue.Empty:
                        break
                    if item is None:
                        self._flush(batch)
                        return
                    if item is _FLUSH_ALL:
                        self._flush(batch)
                        self._drained.set()
                        batch = []
                        break
                    batch.append(item)
                self._flush(batch)
                batch = []
                if self._stop.is_set():
                    break
        finally:
            while True:
                try:
                    item = self._queue.get_nowait()
                except queue.Empty:
                    break
                if item is not None and item is not _FLUSH_ALL:
                    self._flush([item])

    def wait_pending(self, timeout: float = 2.0) -> bool:
        """Aguarda a fila ser totalmente gravada. True = drenada a tempo."""
        self._drained.clear()
        self._queue.put(_FLUSH_ALL)
        return self._drained.wait(timeout)

    def _flush(self, batch: List[dict]) -> None:
        """Método `AsyncLogRepository._flush`.
            Parâmetros: `self`, `batch`."""
        if not batch:
            return
        try:
            with self._lock, self.conn:
                self.conn.executemany(_BATCH_SQL, batch)
        except Exception:
            import traceback

            traceback.print_exc()

    def fetch(
        self,
        category: Optional[str] = None,
        level: Optional[str] = None,
        search: Optional[str] = None,
        limit: int = 1000,
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """Método `AsyncLogRepository.fetch`.
            Parâmetros: `self`, `category`, `level`, `search`, `limit`, `date_from`, `date_to`.
            Retorna o resultado calculado a partir do estado local."""
        sql = "SELECT * FROM logs WHERE 1=1"
        params: List[Any] = []

        if category and category != "Todos":
            sql += " AND category = ?"
            params.append(category)
        if level and level != "Todos":
            sql += " AND level = ?"
            params.append(level)
        if search:
            sql += " AND (action LIKE ? OR message LIKE ? OR entity_type LIKE ?)"
            like = f"%{search}%"
            params.extend([like, like, like])
        if date_from:
            sql += " AND created_at >= ?"
            params.append(date_from)
        if date_to:
            sql += " AND created_at <= ?"
            params.append(date_to)

        sql += " ORDER BY id DESC LIMIT ?"
        params.append(limit)

        with self._lock:
            rows = self.conn.execute(sql, params).fetchall()

        return [dict(r) for r in rows]

    def purge_old(self, days: int = 30) -> int:
        """Apaga logs mais antigos que N dias. Retorna a quantidade apagada."""
        cutoff = (datetime.now() - _timedelta(days=days)).isoformat()
        with self._lock, self.conn:
            cur = self.conn.execute("DELETE FROM logs WHERE created_at < ?", (cutoff,))
            return int(cur.rowcount or 0)

    def count(self) -> int:
        """Método `AsyncLogRepository.count`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        with self._lock:
            row = self.conn.execute("SELECT COUNT(*) AS n FROM logs").fetchone()
        return int(row["n"]) if row else 0

    def close(self) -> None:
        """Método `AsyncLogRepository.close`.
            Parâmetros: `self`."""
        self._queue.put(None)
        self._stop.set()
        self._writer_thread.join(timeout=3.0)
        with self._lock:
            self.conn.close()
