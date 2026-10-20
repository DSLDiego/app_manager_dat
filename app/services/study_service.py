"""Serviço de estudos: gestão, controle e versionamento dos casos.

Um estudo contém a tupla:
    (arquivo .dat, template_version_id, variáveis+distribuições, batch_id,
     pasta de destino)
com clonagem e snapshots para reabrir/adaptar posteriormente.
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

from app.domain.entities import DistributionSpec
from app.infrastructure.study_repository import StudyRepository


class StudyOperationError(Exception):
    """Classe `StudyOperationError` do módulo."""
    pass


class StudyService:
    """Fachada sobre StudyRepository. Sem Qt, sem SQL."""

    def __init__(self, repo: StudyRepository):
        """Método `StudyService.__init__`.
            Parâmetros: `self`, `repo`."""
        self.repo = repo

    # ---------- CRUD ----------
    def create(self, name, specs, meta=None, description="") -> int:
        """Método `StudyService.create`.
            Parâmetros: `self`, `name`, `specs`, `meta`, `description`.
            Retorna o resultado calculado a partir do estado local.
            Levanta: StudyOperationError."""
        name = str(name).strip()
        if not name:
            raise StudyOperationError("Estudo precisa de um nome.")
        if self.repo.find_by_name(name) is not None:
            raise StudyOperationError(f"Já existe um estudo chamado '{name}'.")
        return self.repo.create_study(name, spec_to_store(specs), meta=meta, description=description)

    def get(self, study_id: int) -> Dict[str, Any]:
        """Método `StudyService.get`.
            Parâmetros: `self`, `study_id`.
            Retorna o resultado calculado a partir do estado local.
            Levanta: StudyOperationError."""
        study = self.repo.get_study(study_id)
        if study is None:
            raise StudyOperationError(f"Estudo {study_id} não encontrado.")
        return study

    def list_studies(self) -> list:
        """Método `StudyService.list_studies`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        return self.repo.list_studies()

    def delete(self, study_id: int) -> bool:
        """Método `StudyService.delete`.
            Parâmetros: `self`, `study_id`.
            Retorna o resultado calculado a partir do estado local."""
        return self.repo.delete_study(study_id)

    def find_by_name(self, name) -> Optional[Dict[str, Any]]:
        """Método `StudyService.find_by_name`.
            Parâmetros: `self`, `name`.
            Retorna o resultado calculado a partir do estado local."""
        return self.repo.find_by_name(str(name))

    # ---------- estado atual ----------
    def save(self, study_id: int, specs: Dict[int, DistributionSpec],
             meta: Optional[Dict[str, Any]] = None,
             description: Optional[str] = None) -> None:
        """Método `StudyService.save`.
            Parâmetros: `self`, `study_id`, `specs`, `meta`, `description`."""
        self.repo.update_study(study_id, spec_to_store(specs), meta=meta, description=description)

    def rename(self, study_id: int, new_name: str) -> bool:
        """Nome vazio ou duplicado de outro estudo → False."""
        return self.repo.rename_study(study_id, new_name)

    def set_description(self, study_id: int, description: str) -> None:
        """R30: edita só a descrição, preservando specs/meta e o snapshot atual."""
        if self.repo.get_study(study_id) is None:
            raise StudyOperationError(f"Estudo {study_id} não encontrado.")
        self.repo.update_study(study_id, {}, description=str(description or ""))

    def register_batch(self, study_id: int, batch_id: str, comment: str = "") -> int:
        """T5444: estado atual como novo batch no estudo aberto.
        Anexa o batch ao meta e cria uma nova versão. Retorna nº da versão."""
        study = self.get(study_id)
        meta = dict(study.get("meta") or {})
        batches = list(meta.get("batches") or [])
        batches.append({
            "batch_id": str(batch_id),
            "registered_at": datetime.now().isoformat(timespec="seconds"),
        })
        meta["batches"] = batches
        meta["batch_id"] = str(batch_id)
        self.repo.update_study(study_id, {}, meta=meta)
        return self.repo._snapshot(study_id, comment or f"batch {batch_id}")

    def save_dat_version(self, study_id: int, dat_text: str, comment: str = "") -> int:
        """T5434: guarda o template .dat na versão do estudo (com specs atuais)."""
        meta = dict((self.get(study_id) or {}).get("meta") or {})
        meta["dat_text"] = str(dat_text or "")
        self.repo.update_study(study_id, {}, meta=meta)
        return self.repo._snapshot(study_id, comment or "dat version")

    def get_dat_version(self, study_id: int, version_number: int) -> Optional[str]:
        """Retorna o texto .dat da versão pedida (ou None)."""
        ver = self.get_version(study_id, version_number)
        if not ver:
            return None
        return (ver.get("meta") or {}).get("dat_text")

    def _specs(self, study) -> Dict[int, DistributionSpec]:
        """Specs atuais do estudo normalizadas para store."""
        specs = spec_from_store(study.get("specs") or {})
        return specs

    def snapshot(self, study_id: int, comment: str = "") -> int:
        """Método `StudyService.snapshot`.
            Parâmetros: `self`, `study_id`, `comment`.
            Retorna o resultado calculado a partir do estado local.
            Levanta: StudyOperationError."""
        version = self.repo.snapshot_study(study_id, comment)
        if version is None:
            raise StudyOperationError(f"Estudo {study_id} não encontrado.")
        return version

    def list_versions(self, study_id: int) -> list:
        """Método `StudyService.list_versions`.
            Parâmetros: `self`, `study_id`.
            Retorna o resultado calculado a partir do estado local."""
        return self.repo.list_versions(study_id)

    def get_version(self, study_id: int, version_number: int) -> Dict[str, Any]:
        """Método `StudyService.get_version`.
            Parâmetros: `self`, `study_id`, `version_number`.
            Retorna o resultado calculado a partir do estado local.
            Levanta: StudyOperationError."""
        snapshot = self.repo.get_version(study_id, version_number)
        if snapshot is None:
            raise StudyOperationError(f"Versão {version_number} não encontrada.")
        return snapshot

    # ---------- clone / import / export ----------
    def clone(self, study_id: int, new_name: str,
              meta_overrides: Optional[Dict[str, Any]] = None,
              specs_overrides: Optional[Dict[int, DistributionSpec]] = None,
              description: str = "clonagem adaptada") -> int:
        """Mesmo template/variáveis com overrides para adaptar o novo estudo."""
        source = self.get(study_id)
        specs = spec_from_store(source["specs"])
        if specs_overrides:
            specs = {**specs, **specs_overrides}
        meta = {**source["meta"], **(meta_overrides or {})}
        return self.create(new_name, specs, meta=meta, description=description)

    def export(self, study_id: int, path) -> str:
        """Estudo completo (specs + meta + históricos) num JSON portátil."""
        data = self.get(study_id)
        data["versions"] = self.repo.list_versions(study_id)
        for i, version in enumerate(data["versions"]):
            snapshot = self.repo.get_version(study_id, version["version_number"])
            data["versions"][i] = snapshot
        import datetime as _dt

        data["exported_at"] = _dt.datetime.now().isoformat()
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return str(path)

    def import_study(self, path, new_name=None) -> int:
        """Importa JSON portátil; novo estudo com nome novo."""
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        name = new_name or data.get("name", "importado")
        if not new_name and self.repo.find_by_name(name) is not None:
            raise StudyOperationError(f"Nome '{name}' já existente; informe um nome novo.")
        specs = spec_from_store(data.get("specs") or {})
        study_id = self.create(name, specs, meta=data.get("meta") or {},
                               description=f"importado de {path}")
        for version in data.get("versions") or []:
            self.repo.snapshot_study(study_id, f"importado: {version.get('comment', '')}")
        return study_id


def spec_to_store(specs: Dict[int, DistributionSpec]) -> Dict[str, Dict[str, Any]]:
    """Função `spec_to_store`.
        Parâmetros: `specs`.
        Retorna o resultado calculado a partir do estado local."""
    converted: Dict[str, Dict[str, Any]] = {}
    for var_id, spec in specs.items():
        if isinstance(spec, DistributionSpec):
            converted[str(var_id)] = {
                "provider": spec.provider,
                "name": spec.name,
                "params": spec.params,
            }
        else:
            converted[str(var_id)] = dict(spec)
    return converted


def spec_from_store(raw: Dict[str, Any]) -> Dict[int, DistributionSpec]:
    """Função `spec_from_store`.
        Parâmetros: `raw`.
        Retorna o resultado calculado a partir do estado local."""
    out: Dict[int, DistributionSpec] = {}
    for var_id, spec in (raw or {}).items():
        out[int(var_id)] = DistributionSpec(
            provider=spec.get("provider", "scipy"),
            name=spec.get("name", "uniform"),
            params=dict(spec.get("params") or {}),
        )
    return out
