"""Renderiza um template versionado com N experimentos e salva em disco."""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Callable, Dict, List, Optional

from app.core.parsing import render_template
from app.infrastructure.experiment_repository import ExperimentRepository
from app.infrastructure.template_repository import TemplateRepository


def _next_free_path(out_dir: Path, filename_pattern: str, ext_id: int) -> Path:
    """Primeiro caminho livre: base.dat -> base-1.dat, base-2.dat, ..."""
    base = out_dir / filename_pattern.format(id=ext_id)
    candidate = base.with_suffix(".dat")
    suffix = 1
    while candidate.exists():
        candidate = base.with_name(f"{base.name}-{suffix}.dat")
        suffix += 1
    return candidate


@dataclass(frozen=True)
class BatchExportManifest:
    """Classe `BatchExportManifest` do módulo."""
    batch_id: str
    template_version_id: int
    template_version_number: int
    template_hash: str
    n_files: int
    output_dir: Path
    manifest_path: Path
    completed_at: str


class BatchExportService:
    """Classe `BatchExportService` do módulo."""
    def __init__(
        self,
        exp_repo: ExperimentRepository,
        template_repo: TemplateRepository,
        renderer: Optional[Callable[[str, Dict[int, float]], str]] = None,
    ):
        """Método `BatchExportService.__init__`.
            Parâmetros: `self`, `exp_repo`, `template_repo`, `renderer`."""
        self.exp_repo = exp_repo
        self.template_repo = template_repo
        self.renderer = renderer or self._default_render

    @staticmethod
    def _default_render(template: str, values: Dict[int, float]) -> str:
        """Método `BatchExportService._default_render`.
            Parâmetros: `template`, `values`.
            Retorna o resultado calculado a partir do estado local."""
        return render_template(template, values)

    def _compile(self, template_text: str):
        """Renderer compilado (regex 1x) quando possível; fallback: renderer injetado."""
        if self.renderer is self._default_render:
            from app.core.parsing import compile_template

            compiled = compile_template(template_text)
            return compiled.render
        return None

    def export(
        self,
        batch_id: str,
        template_version_id: int,
        output_root,
        start_external_id: int = 1,
        batch_meta: Optional[Dict] = None,
        progress_cb: Optional[Callable[[int, str], None]] = None,
        checkpoint_cb: Optional[Callable[[int, int], None]] = None,
        stop_check: Optional[Callable[[], bool]] = None,
        batch_size: int = 500,
        include_manifest: bool = True,
        filename_pattern: str = "experimento_{id:06d}",
        overwrite: bool = True,
        rename_existing: bool = False,
        audit_log: bool = True,
    ) -> BatchExportManifest:
        """Método `BatchExportService.export`.
            Parâmetros: `self`, `batch_id`, `template_version_id`, `output_root`, `start_external_id`, `batch_meta`, `progress_cb`, `checkpoint_cb`, `stop_check`, `batch_size`, `include_manifest`, `filename_pattern`, `overwrite`, `rename_existing`, `audit_log`.
            Retorna o resultado calculado a partir do estado local.
            Levanta: ValueError, InterruptedError."""
        version = self.template_repo.get_version(template_version_id)
        if not version:
            raise ValueError(f"Versão {template_version_id} não encontrada.")

        template_text = version["content"]
        template_id = version["template_id"]
        version_number = int(version["version_number"])
        template_hash = version["content_hash"]

        var_ids = self.exp_repo.var_ids(batch_id=batch_id)
        total = self.exp_repo.count(batch_id=batch_id)

        if total == 0:
            raise ValueError(f"O lote '{batch_id}' não tem experimentos para exportar.")

        remaining = max(1, total - (start_external_id - 1))
        compiled_render = self._compile(template_text)

        # fail-fast: variáveis do template presentes, mas sem valores no lote
        from app.core.parsing import find_variables, var_label

        template_var_ids = sorted(find_variables(template_text))
        missing = [var_label(v) for v in template_var_ids if v not in var_ids]
        if missing:
            raise ValueError(
                f"O lote '{batch_id}' não tem valores para: {', '.join(missing[:8])}"
                f"{'…' if len(missing) > 8 else ''}. "
                "Refaça a amostragem (Amostrar) com o template atual antes de exportar."
            )

        out_dir = Path(output_root) / batch_id / f"v{version_number}"
        out_dir.mkdir(parents=True, exist_ok=True)

        manifest_rows: List[List] = [["external_id", "values"]]
        audit_rows: List[List] = [["external_id", "file", "written_at", "action"]]
        written = 0
        page = 0
        now_iso = datetime.now().isoformat(timespec="seconds")

        while True:
            rows = self.exp_repo.fetch_page(page, batch_size, var_ids, batch_id=batch_id)
            if not rows:
                break

            for row in rows:
                if stop_check and stop_check():
                    raise InterruptedError("Cancelado pelo usuário.")

                ext_id = int(row["external_id"])
                if ext_id < start_external_id:
                    continue

                if compiled_render is not None:
                    text = compiled_render(row["values"])
                else:
                    text = self.renderer(template_text, row["values"])
                filename = out_dir / (filename_pattern.format(id=ext_id) + ".dat")
                if filename.exists():
                    if overwrite:
                        filename.write_text(text, encoding="utf-8")
                        action = "overwritten"
                    elif rename_existing:
                        filename = _next_free_path(out_dir, filename_pattern, ext_id)
                        filename.write_text(text, encoding="utf-8")
                        action = "renamed_to_free_path"
                    # senão: "skip" — arquivo existente é reutilizado
                    else:
                        action = "skipped_existing"
                else:
                    filename.write_text(text, encoding="utf-8")
                    action = "created"

                manifest_rows.append([
                    ext_id,
                    json.dumps({str(k): v for k, v in row["values"].items()},
                               ensure_ascii=False),
                ])
                if audit_log:
                    audit_rows.append([ext_id, filename.name, now_iso, action])

                written += 1

                if checkpoint_cb and written % 50 == 0:
                    checkpoint_cb(written, ext_id)

                if progress_cb:
                    progress_cb(int(100 * written / remaining), f"{written}/{remaining}")

            page += 1
            if checkpoint_cb and rows:
                checkpoint_cb(written, int(rows[-1]["external_id"]))

        if include_manifest:
            manifest_path = out_dir / "manifest.csv"
            with open(manifest_path, "w", newline="", encoding="utf-8") as f:
                csv.writer(f).writerows(manifest_rows)
        else:
            manifest_path = out_dir / "manifest.csv"

        if audit_log and audit_rows:
            with open(out_dir / "audit.csv", "w", newline="", encoding="utf-8") as f:
                csv.writer(f).writerows(audit_rows)

        (out_dir / "metadata.json").write_text(
            json.dumps(
                {
                    "batch_id": batch_id,
                    "template_id": template_id,
                    "template_version_id": template_version_id,
                    "template_version_number": version_number,
                    "template_hash": template_hash,
                    "n_files": written + (start_external_id - 1),
                    "start_external_id": start_external_id,
                    "exported_at": datetime.now().isoformat(),
                    "batch_meta": batch_meta or {},
                },
                indent=2,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

        return BatchExportManifest(
            batch_id=batch_id,
            template_version_id=template_version_id,
            template_version_number=version_number,
            template_hash=template_hash,
            n_files=written,
            output_dir=out_dir,
            manifest_path=manifest_path,
            completed_at=datetime.now().isoformat(),
        )
