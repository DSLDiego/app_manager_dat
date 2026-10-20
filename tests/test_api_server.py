"""Testes da API REST local via HTTP real (toda a topologia de rotas)."""

import json
import threading
import urllib.error
import urllib.request


def _get(url):
    try:
        with urllib.request.urlopen(url, timeout=5) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        return exc.code, json.loads(exc.read().decode("utf-8"))


def _start_api(container):
    from app.infrastructure.api.routes import build_api_routes
    from app.infrastructure.api.server import ApiServer

    server = ApiServer(host="127.0.0.1", port=0)
    build_api_routes(server, container.exp_repo, container.template_repo)
    server.start()
    return server


def test_api_health_and_batches(container, populated_batch):
    server = _start_api(container)
    try:
        base = f"http://127.0.0.1:{server.port}/api"

        status, body = _get(f"{base}/health")
        assert status == 200
        assert body["status"] == "ok"
        assert body["batches"] == 1

        status, body = _get(f"{base}/batches")
        assert status == 200
        ids = [b["id"] for b in body]
        assert "batch_x" in ids

        status, body = _get(f"{base}/batches/batch_x")
        assert status == 200
        assert body["method"] == "lhs"
    finally:
        server.stop()


def test_api_experiments_pagination(container, populated_batch):
    server = _start_api(container)
    try:
        base = f"http://127.0.0.1:{server.port}/api"

        status, body = _get(f"{base}/batches/batch_x/experiments?page=0&size=5")
        assert status == 200
        assert len(body) == 5
        first = body[0]
        assert first["external_id"] == 1
        assert set(first["values"]) == {"1", "10002"}

        status, body = _get(f"{base}/batches/batch_x/experiments?page=999&size=5")
        assert status == 200
        assert body == []
    finally:
        server.stop()


def test_api_stats_and_templates(container, populated_batch):
    server = _start_api(container)
    try:
        base = f"http://127.0.0.1:{server.port}/api"

        status, body = _get(f"{base}/batches/batch_x/stats")
        assert status == 200
        assert "1" in body and "10002" in body
        assert body["10002"]["count"] == 12

        status, body = _get(f"{base}/templates")
        assert status == 200
        template_id = body[0]["id"]

        status, body = _get(f"{base}/templates/{template_id}/versions")
        assert status == 200
        assert len(body) == 1
    finally:
        server.stop()


def test_api_unknown_batch_404(container, populated_batch):
    server = _start_api(container)
    try:
        status, body = _get(f"http://127.0.0.1:{server.port}/api/batches/nao_existe")
        assert status == 404
    finally:
        server.stop()
