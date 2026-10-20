"""Lógica de negócio para versionamento (diff, restore)."""

from __future__ import annotations

import difflib
from typing import List

from app.infrastructure.template_repository import TemplateRepository


class TemplateService:
    """Classe `TemplateService` do módulo."""
    def __init__(self, repo: TemplateRepository):
        """Método `TemplateService.__init__`.
            Parâmetros: `self`, `repo`."""
        self.repo = repo

    def save(self, template_id: int, content: str, comment: str = "", user: str = "user") -> int:
        """Método `TemplateService.save`.
            Parâmetros: `self`, `template_id`, `content`, `comment`, `user`.
            Retorna o resultado calculado a partir do estado local."""
        return self.repo.save_version(template_id, content, comment, user)

    def diff(self, v1_id: int, v2_id: int) -> str:
        """Método `TemplateService.diff`.
            Parâmetros: `self`, `v1_id`, `v2_id`.
            Retorna o resultado calculado a partir do estado local."""
        a = self.repo.get_version(v1_id)
        b = self.repo.get_version(v2_id)
        if not a or not b:
            return ""
        return "".join(
            difflib.unified_diff(
                a["content"].splitlines(keepends=True),
                b["content"].splitlines(keepends=True),
                fromfile=f"v{a['version_number']}",
                tofile=f"v{b['version_number']}",
            )
        )

    def restore(self, template_id: int, version_id: int, user: str = "user") -> int:
        """Restaurar nunca apaga: cria nova versão com conteúdo antigo."""
        old = self.repo.get_version(version_id)
        if not old:
            raise ValueError("Versão não encontrada.")
        return self.repo.save_version(
            template_id,
            old["content"],
            comment=f"Restaurado a partir da v{old['version_number']}",
            user=user,
        )
