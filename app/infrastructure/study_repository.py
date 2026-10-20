"""Repositório de estudos (gestão/versionamento dos casos estudados).

Estudo = tupla:
    (arquivo .dat, template_version, variáveis+distribuições, lote de
    experimentos, pasta de destino).
Cada estudo é versionado: snapshot imutável com comentário.
"""

from __future__ import annotations

import dataclasses
import json
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional


def _ensure_store(specs: Dict[int, Any]) -> str:
    """Aceita Dict[int, DistributionSpec] ou Dict[int, dict] e serializa p/ JSON."""
    converted: Dict[str, Any] = {}
    for var_id, spec in (specs or {}).items():
        if isinstance(spec, dict):
            converted[str(var_id)] = spec
        elif dataclasses.is_dataclass(spec):
            converted[str(var_id)] = dataclasses.asdict(spec)
        else:
            converted[str(var_id)] = dict(spec)
    return json.dumps(converted, ensure_ascii=False)


_SCHEMA = """
CREATE TABLE IF NOT EXISTS studies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL DEFAULT '',
    meta_json TEXT NOT NULL DEFAULT '{}',
    specs_json TEXT NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS study_versions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    study_id INTEGER NOT NULL REFERENCES studies(id),
    version_number INTEGER NOT NULL,
    meta_json TEXT NOT NULL,
    specs_json TEXT NOT NULL,
    comment TEXT NOT NULL DEFAULT '',
    created_at TEXT NOT NULL,
    UNIQUE (study_id, version_number)
);
"""


class StudyRepository:
    """Classe `StudyRepository` do módulo."""
    def __init__(self, db_path: str = "data/studies.db"):
        """Método `StudyRepository.__init__`.
            Parâmetros: `self`, `db_path`."""
        if db_path != ":memory:":
            Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row

        try:
            self.conn.execute("PRAGMA journal_mode=WAL")
        except sqlite3.DatabaseError:
            pass

        with self.conn:
            self.conn.executescript(_SCHEMA)

    # ---------- CRUD ----------
    def create_study(
        self,
        name: str,
        specs: Dict[int, Any],
        meta: Optional[Dict[str, Any]] = None,
        description: str = "",
    ) -> int:
        """Método `StudyRepository.create_study`.
            Parâmetros: `self`, `name`, `specs`, `meta`, `description`.
            Retorna o resultado calculado a partir do estado local."""
        now = datetime.now().isoformat()
        meta = dict(meta or {})
        specs_json = _ensure_store(specs)
        with self.conn:
            cur = self.conn.execute(
                """
                INSERT INTO studies (name, description, meta_json, specs_json,
                                     created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (name, description, json.dumps(meta, ensure_ascii=False),
                 specs_json, now, now),
            )
            study_id = int(cur.lastrowid)
            self._snapshot(study_id, "versão inicial", created_at=now)
        return study_id

    def update_study(self, study_id: int, specs: Dict[int, Any],
                     meta: Optional[Dict[str, Any]] = None,
                     description: Optional[str] = None) -> None:
        """Método `StudyRepository.update_study`.
            Parâmetros: `self`, `study_id`, `specs`, `meta`, `description`."""
        now = datetime.now().isoformat()
        with self.conn:
            if description is not None:
                self.conn.execute(
                    "UPDATE studies SET description = ?, updated_at = ? WHERE id = ?",
                    (description, now, study_id),
                )
            if specs or meta:
                if meta is not None:
                    self.conn.execute(
                        "UPDATE studies SET meta_json = ?, updated_at = ? WHERE id = ?",
                        (json.dumps(meta, ensure_ascii=False), now, study_id),
                    )
                if specs:
                    specs_json = _ensure_store(specs)
                    self.conn.execute(
                        "UPDATE studies SET specs_json = ?, updated_at = ? WHERE id = ?",
                        (specs_json, now, study_id),
                    )

    def get_study(self, study_id: int) -> Optional[Dict[str, Any]]:
        """Método `StudyRepository.get_study`.
            Parâmetros: `self`, `study_id`.
            Retorna o resultado calculado a partir do estado local."""
        row = self.conn.execute(
            "SELECT * FROM studies WHERE id = ?", (study_id,)
        ).fetchone()
        if row is None:
            return None
        return self._row_to_dict(row)

    def find_by_name(self, name: str) -> Optional[Dict[str, Any]]:
        """Método `StudyRepository.find_by_name`.
            Parâmetros: `self`, `name`.
            Retorna o resultado calculado a partir do estado local."""
        row = self.conn.execute(
            "SELECT * FROM studies WHERE name = ?", (name,)
        ).fetchone()
        if row is None:
            return None
        return self._row_to_dict(row)

    def list_studies(self) -> List[Dict[str, Any]]:
        """Método `StudyRepository.list_studies`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        rows = self.conn.execute(
            "SELECT * FROM studies ORDER BY updated_at DESC"
        ).fetchall()
        return [self._row_to_dict(row) for row in rows]

    def rename_study(self, study_id: int, new_name: str) -> bool:
        """Renomeia; não permite nome duplicado de outro estudo."""
        new_name = (new_name or "").strip()
        if not new_name:
            return False
        other = self.find_by_name(new_name)
        if other is not None and int(other["id"]) != int(study_id):
            return False
        with self.conn:
            cur = self.conn.execute(
                "UPDATE studies SET name = ?, updated_at = ? WHERE id = ?",
                (new_name, datetime.now().isoformat(), study_id),
            )
        return cur.rowcount > 0

    def delete_study(self, study_id: int) -> bool:
        """Método `StudyRepository.delete_study`.
            Parâmetros: `self`, `study_id`.
            Retorna o resultado calculado a partir do estado local."""
        with self.conn:
            cur = self.conn.execute(
                "DELETE FROM study_versions WHERE study_id = ?", (study_id,)
            )
            cur2 = self.conn.execute("DELETE FROM studies WHERE id = ?", (study_id,))
            return cur2.rowcount > 0

    # ---------- versionamento ----------
    def _snapshot(self, study_id: int, comment: str,
                  created_at: Optional[str] = None):
        """Método `StudyRepository._snapshot`.
            Parâmetros: `self`, `study_id`, `comment`, `created_at`.
            Retorna o resultado calculado a partir do estado local."""
        study = self.conn.execute(
            "SELECT meta_json, specs_json FROM studies WHERE id = ?", (study_id,)
        ).fetchone()
        if study is None:
            return
        nxt = self.conn.execute(
            "SELECT COALESCE(MAX(version_number), 0) + 1 AS v "
            "FROM study_versions WHERE study_id = ?",
            (study_id,),
        ).fetchone()
        version_number = int(nxt["v"])
        self.conn.execute(
            """
            INSERT INTO study_versions
            (study_id, version_number, meta_json, specs_json, comment, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                study_id,
                version_number,
                study["meta_json"],
                study["specs_json"],
                comment,
                created_at or datetime.now().isoformat(),
            ),
        )
        return version_number

    def snapshot_study(self, study_id: int, comment: str = "") -> Optional[int]:
        """Método `StudyRepository.snapshot_study`.
            Parâmetros: `self`, `study_id`, `comment`.
            Retorna o resultado calculado a partir do estado local."""
        with self.conn:
            return self._snapshot(study_id, comment)

    def list_versions(self, study_id: int) -> List[Dict[str, Any]]:
        """Método `StudyRepository.list_versions`.
            Parâmetros: `self`, `study_id`.
            Retorna o resultado calculado a partir do estado local."""
        rows = self.conn.execute(
            """
            SELECT id, study_id, version_number, comment, created_at
            FROM study_versions WHERE study_id = ?
            ORDER BY version_number DESC
            """,
            (study_id,),
        ).fetchall()
        return [dict(row) for row in rows]

    def get_version(self, study_id: int, version_number: int) -> Optional[Dict[str, Any]]:
        """Método `StudyRepository.get_version`.
            Parâmetros: `self`, `study_id`, `version_number`.
            Retorna o resultado calculado a partir do estado local."""
        row = self.conn.execute(
            """
            SELECT * FROM study_versions WHERE study_id = ? AND version_number = ?
            """,
            (study_id, version_number),
        ).fetchone()
        if row is None:
            return None
        meta = json.loads(row["meta_json"] or "{}")
        specs = json.loads(row["specs_json"] or "{}")
        return {
            "version_number": int(row["version_number"]),
            "comment": row["comment"],
            "created_at": row["created_at"],
            "meta": meta,
            "specs": specs,
        }

    # ---------- import/export ----------
    def _row_to_dict(self, row) -> Dict[str, Any]:
        """Método `StudyRepository._row_to_dict`.
            Parâmetros: `self`, `row`.
            Retorna o resultado calculado a partir do estado local."""
        return {
            "id": int(row["id"]),
            "name": row["name"],
            "description": row["description"],
            "meta": json.loads(row["meta_json"] or "{}"),
            "specs": json.loads(row["specs_json"] or "{}"),
            "created_at": row["created_at"],
            "updated_at": row["updated_at"],
        }

    def close(self):
        """Método `StudyRepository.close`."""
        self.conn.close()
