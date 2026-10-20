"""Registra todas as rotas da API nos repositórios."""

from __future__ import annotations

import re

import numpy as np

from app.infrastructure.api.server import ApiServer
from app.infrastructure.experiment_repository import ExperimentRepository
from app.infrastructure.template_repository import TemplateRepository


def openapi_document(server: ApiServer) -> dict:
    """T5178: documento OpenAPI 3 estático derivado das rotas registradas."""
    paths: dict = {}
    for method, pattern in server.route_list():
        path = "/" + pattern.strip("/")
        path = re.sub(r"<([^>]+)>", r"{\1}", path)
        paths.setdefault(path, {})[method.lower()] = {
            "summary": f"{method} {path}",
            "responses": {"200": {"description": "OK"}},
        }
    return {
        "openapi": "3.0.3",
        "info": {
            "title": "DAT Engineering Studio API",
            "version": "1.0.0",
            "description": "API REST local do DAT Engineering Studio.",
        },
        "paths": paths,
    }


def build_api_routes(
    server: ApiServer,
    exp_repo: ExperimentRepository,
    template_repo: TemplateRepository,
    study_repo=None,
) -> None:
    """Registra as rotas da API nos handlers do server.

    Parâmetros: `server` (ApiServer alvo), `exp_repo` e `template_repo`
    (repositórios consultados pelas rotas) e `study_repo` (opcional, rotas
    de estudos). Levanta nada: rotas já registradas são simplesmente
    reutilizadas pelo server.
    """

    @server.route("GET", "/api/openapi.json")
    def openapi(params, qs):
        return openapi_document(server)

    @server.route("GET", "/api/health")
    def health(params, qs):
        n_batches = exp_repo.conn.execute("SELECT COUNT(*) FROM batches").fetchone()[0]
        return {"status": "ok", "batches": n_batches}

    @server.route("GET", "/api/batches")
    def list_batches(params, qs):
        rows = exp_repo.conn.execute(
            "SELECT id, created_at, method, seed, n_experiments "
            "FROM batches ORDER BY created_at DESC"
        ).fetchall()
        return [dict(r) for r in rows]

    @server.route("GET", "/api/batches/<batch_id>")
    def get_batch(params, qs):
        r = exp_repo.conn.execute(
            "SELECT * FROM batches WHERE id=?", (params["batch_id"],),
        ).fetchone()
        if not r:
            raise ValueError("batch não encontrado")
        return dict(r)

    @server.route("GET", "/api/batches/<batch_id>/experiments")
    def list_experiments(params, qs):
        page = int(qs.get("page", ["0"])[0])
        size = int(qs.get("size", ["100"])[0])

        rows = exp_repo.conn.execute(
            """
            SELECT e.external_id AS eid, ev.var_id AS vid, ev.value AS val
            FROM experiments e
            JOIN experiment_values ev ON ev.experiment_id = e.id
            WHERE e.batch_id = ?
            ORDER BY e.external_id, ev.var_id
            LIMIT ? OFFSET ?
            """,
            (params["batch_id"], size * 8, page * size * 8),
        ).fetchall()

        grouped: dict[int, dict] = {}
        for r in rows:
            eid = int(r["eid"])
            grouped.setdefault(eid, {"external_id": eid, "values": {}})
            grouped[eid]["values"][int(r["vid"])] = float(r["val"])

        return list(grouped.values())[:size]

    @server.route("GET", "/api/batches/<batch_id>/stats")
    def batch_stats(params, qs):
        rows = exp_repo.conn.execute(
            """
            SELECT v.var_id AS vid, v.value AS val
            FROM experiment_values v
            JOIN experiments e ON e.id = v.experiment_id
            WHERE e.batch_id = ?
            """,
            (params["batch_id"],),
        ).fetchall()

        buckets: dict[int, list] = {}
        for r in rows:
            buckets.setdefault(int(r["vid"]), []).append(float(r["val"]))

        return {
            str(vid): {
                "count": len(arr),
                "mean": float(np.mean(arr)),
                "p10": float(np.quantile(arr, 0.1)),
                "p50": float(np.quantile(arr, 0.5)),
                "p90": float(np.quantile(arr, 0.9)),
            }
            for vid, arr in buckets.items()
        }

    @server.route("GET", "/api/templates")
    def list_templates(params, qs):
        return template_repo.list_templates()

    @server.route("GET", "/api/templates/<template_id>/versions")
    def list_versions(params, qs):
        return template_repo.list_versions(int(params["template_id"]))

    if study_repo is not None:
        @server.route("GET", "/api/studies")
        def list_studies(params, qs):
            return study_repo.list_studies()

        @server.route("GET", "/api/studies/<study_id>")
        def get_study(params, qs):
            study = study_repo.get_study(int(params["study_id"]))
            if study is None:
                raise ValueError("estudo não encontrado")
            return study

        @server.route("GET", "/api/studies/<study_id>/versions")
        def list_study_versions(params, qs):
            return study_repo.list_versions(int(params["study_id"]))

        @server.route("POST", "/api/studies")
        def create_study(params, qs, body=None):
            if not isinstance(body, dict):
                raise ValueError("corpo JSON obrigatório: {name, specs}")
            name = (body.get("name") or "").strip()
            if not name:
                raise ValueError("name é obrigatório")
            specs = body.get("specs") or {}
            if not isinstance(specs, dict):
                raise ValueError("specs deve ser um objeto {var_id: spec}")
            study_id = study_repo.create_study(
                name,
                specs,
                meta=body.get("meta"),
                description=body.get("description", ""),
            )
            return {"study_id": study_id, "name": name}

    @server.route("GET", "/api/jobs/<job_id>")
    def get_job(params, qs):
        job = server.get_job(params["job_id"])
        if job is None:
            raise ValueError("job não encontrado")
        return job

    @server.route("POST", "/api/batches/<batch_id>/export-async")
    def export_batch_async(params, qs, body=None):
        if not isinstance(body, dict):
            raise ValueError(
                "corpo JSON obrigatório: {template_version_id, output_root}"
            )
        template_version_id = body.get("template_version_id")
        output_root = body.get("output_root")
        if template_version_id is None or not output_root:
            raise ValueError("template_version_id e output_root são obrigatórios")

        from app.services.batch_export_service import BatchExportService

        batch_id = params["batch_id"]
        service = BatchExportService(exp_repo, template_repo)

        def _run() -> dict:
            manifest = service.export(
                batch_id=batch_id,
                template_version_id=int(template_version_id),
                output_root=output_root,
                overwrite=bool(body.get("overwrite", True)),
            )
            return {
                "batch_id": manifest.batch_id,
                "n_files": manifest.n_files,
                "output_dir": str(manifest.output_dir),
                "manifest_path": str(manifest.manifest_path),
            }

        job_id = server.submit_job(_run)
        return {"job_id": job_id, "status": "running"}

    @server.route("POST", "/api/batches/<batch_id>/export")
    def export_batch(params, qs, body=None):
        if not isinstance(body, dict):
            raise ValueError("corpo JSON obrigatório: {template_version_id, output_root}")
        template_version_id = body.get("template_version_id")
        output_root = body.get("output_root")
        if template_version_id is None or not output_root:
            raise ValueError("template_version_id e output_root são obrigatórios")

        from app.services.batch_export_service import BatchExportService

        service = BatchExportService(exp_repo, template_repo)
        manifest = service.export(
            batch_id=params["batch_id"],
            template_version_id=int(template_version_id),
            output_root=output_root,
            overwrite=bool(body.get("overwrite", True)),
        )
        return {
            "batch_id": manifest.batch_id,
            "n_files": manifest.n_files,
            "output_dir": str(manifest.output_dir),
            "manifest_path": str(manifest.manifest_path),
            "template_version_number": manifest.template_version_number,
        }
