"""Versionamento imutável de templates em SQLite."""

from __future__ import annotations

import hashlib
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


class TemplateRepository:
    """Classe `TemplateRepository` do módulo."""
    def __init__(self, db_path: str = "data/templates.db"):
        """Método `TemplateRepository.__init__`.
            Parâmetros: `self`, `db_path`."""
        if db_path != ":memory:":
            Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self._enable_wal()
        self._create_schema()

    def _enable_wal(self) -> None:
        """Método `TemplateRepository._enable_wal`.
            Parâmetros: `self`."""
        try:
            self.conn.execute("PRAGMA journal_mode=WAL")
        except sqlite3.DatabaseError:
            pass

    def _create_schema(self):
        """Método `TemplateRepository._create_schema`.
            Parâmetros: `self`."""
        with self.conn:
            self.conn.executescript(
                """
                PRAGMA foreign_keys = ON;

                CREATE TABLE IF NOT EXISTS templates (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    current_version_id INTEGER,
                    created_at TEXT,
                    updated_at TEXT
                );

                CREATE TABLE IF NOT EXISTS template_versions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    template_id INTEGER NOT NULL,
                    version_number INTEGER NOT NULL,
                    content TEXT NOT NULL,
                    content_hash TEXT NOT NULL,
                    comment TEXT,
                    created_by TEXT,
                    created_at TEXT,
                    FOREIGN KEY(template_id) REFERENCES templates(id),
                    UNIQUE(template_id, version_number)
                );
                """
            )

    def create_template(self, name: str, description: str = "", user: str = "user") -> int:
        """Método `TemplateRepository.create_template`.
            Parâmetros: `self`, `name`, `description`, `user`.
            Retorna o resultado calculado a partir do estado local."""
        now = datetime.now().isoformat()
        with self.conn:
            cur = self.conn.execute(
                "INSERT INTO templates(name, description, created_at, updated_at) "
                "VALUES (?, ?, ?, ?)",
                (name, description, now, now),
            )
        return int(cur.lastrowid)

    def list_templates(self) -> List[Dict]:
        """Método `TemplateRepository.list_templates`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        rows = self.conn.execute(
            """
            SELECT t.*, v.version_number AS current_version
            FROM templates t
            LEFT JOIN template_versions v ON v.id = t.current_version_id
            ORDER BY t.updated_at DESC
            """
        ).fetchall()
        return [dict(r) for r in rows]

    def save_version(
        self,
        template_id: int,
        content: str,
        comment: str = "",
        user: str = "user",
    ) -> int:
        """Método `TemplateRepository.save_version`.
            Parâmetros: `self`, `template_id`, `content`, `comment`, `user`.
            Retorna o resultado calculado a partir do estado local."""
        chash = hashlib.sha256(content.encode("utf-8")).hexdigest()

        row = self.conn.execute(
            "SELECT COALESCE(MAX(version_number), 0) AS n "
            "FROM template_versions WHERE template_id = ?",
            (template_id,),
        ).fetchone()
        next_ver = int(row["n"]) + 1
        now = datetime.now().isoformat()

        with self.conn:
            cur = self.conn.execute(
                """
                INSERT INTO template_versions
                (template_id, version_number, content, content_hash, comment, created_by, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (template_id, next_ver, content, chash, comment, user, now),
            )
            vid = int(cur.lastrowid)
            self.conn.execute(
                "UPDATE templates SET current_version_id = ?, updated_at = ? WHERE id = ?",
                (vid, now, template_id),
            )
        return vid

    def list_versions(self, template_id: int) -> List[Dict]:
        """Método `TemplateRepository.list_versions`.
            Parâmetros: `self`, `template_id`.
            Retorna o resultado calculado a partir do estado local."""
        rows = self.conn.execute(
            "SELECT * FROM template_versions WHERE template_id = ? "
            "ORDER BY version_number ASC",
            (template_id,),
        ).fetchall()
        return [dict(r) for r in rows]

    def get_version(self, version_id: int) -> Optional[Dict]:
        """Método `TemplateRepository.get_version`.
            Parâmetros: `self`, `version_id`.
            Retorna o resultado calculado a partir do estado local."""
        r = self.conn.execute(
            "SELECT * FROM template_versions WHERE id = ?", (version_id,)
        ).fetchone()
        return dict(r) if r else None

    def get_current(self, template_id: int) -> Optional[Dict]:
        """Método `TemplateRepository.get_current`.
            Parâmetros: `self`, `template_id`.
            Retorna o resultado calculado a partir do estado local."""
        r = self.conn.execute(
            """
            SELECT v.*
            FROM templates t
            JOIN template_versions v ON v.id = t.current_version_id
            WHERE t.id = ?
            """,
            (template_id,),
        ).fetchone()
        return dict(r) if r else None

    def close(self):
        """Método `TemplateRepository.close`."""
        self.conn.close()
