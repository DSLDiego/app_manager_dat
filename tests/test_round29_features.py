"""Rodada 29: API REST de estudos, token local e OpenAPI estático."""

import json
import urllib.error
import urllib.request

import pytest


def _request(url, method="GET", payload=None, token=None):
    data = None
    headers = {}
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        return exc.code, json.loads(exc.read().decode("utf-8"))


@pytest.fixture()
def api(container):
    from app.infrastructure.api.routes import build_api_routes
    from app.infrastructure.api.server import ApiServer

    server = ApiServer(host="127.0.0.1", port=0, token="segredo-local")
    build_api_routes(
        server,
        container.exp_repo,
        container.template_repo,
        study_repo=container.study_repo,
    )
    server.start()
    yield server
    server.stop()


def test_openapi_static_document(api):
    base = f"http://127.0.0.1:{api.port}/api"
    status, body = _request(
        f"{base}/openapi.json?token=", token="segredo-local"
    )
    assert status == 200
    assert body["openapi"] == "3.0.3"
    assert "/api/studies" in body["paths"]
    assert "get" in body["paths"]["/api/studies"]
    assert "post" in body["paths"]["/api/studies"]
    assert "/api/studies/{study_id}/versions" in body["paths"]
    assert all("<" not in path for path in body["paths"])


def test_token_blocks_api_without_header(api):
    base = f"http://127.0.0.1:{api.port}/api"
    status, body = _request(f"{base}/batches")
    assert status == 401
    assert "não autorizado" in body["error"]


def test_token_allows_health_without_header(api):
    base = f"http://127.0.0.1:{api.port}/api"
    status, body = _request(f"{base}/health")
    assert status == 200
    assert body["status"] == "ok"


def test_token_allows_with_header(api):
    base = f"http://127.0.0.1:{api.port}/api"
    status, body = _request(f"{base}/batches", token="segredo-local")
    assert status == 200
    assert isinstance(body, list)


def test_studies_list_empty_then_created(api):
    base = f"http://127.0.0.1:{api.port}/api"
    status, body = _request(f"{base}/studies", token="segredo-local")
    assert status == 200
    assert body == []

    status, body = _request(
        f"{base}/studies",
        method="POST",
        payload={"name": "Estudo REST", "specs": {"1": {"dist": "normal"}}},
        token="segredo-local",
    )
    assert status == 200
    assert body["name"] == "Estudo REST"
    study_id = body["study_id"]

    status, body = _request(f"{base}/studies", token="segredo-local")
    assert status == 200
    assert [s["id"] for s in body] == [study_id]

    status, body = _request(f"{base}/studies/{study_id}", token="segredo-local")
    assert status == 200
    assert body["name"] == "Estudo REST"

    status, body = _request(
        f"{base}/studies/{study_id}/versions", token="segredo-local"
    )
    assert status == 200
    assert len(body) == 1
    assert body[0]["version_number"] == 1


def test_studies_get_missing_is_404(api):
    base = f"http://127.0.0.1:{api.port}/api"
    status, body = _request(f"{base}/studies/9999", token="segredo-local")
    assert status == 404
    assert "não encontrado" in body["error"]


def test_studies_create_requires_name(api):
    base = f"http://127.0.0.1:{api.port}/api"
    status, body = _request(
        f"{base}/studies",
        method="POST",
        payload={"specs": {}},
        token="segredo-local",
    )
    assert status in (400, 404)
    assert "name" in body["error"]


def test_study_repo_optional_keeps_legacy_routes(container):
    from app.infrastructure.api.routes import build_api_routes
    from app.infrastructure.api.server import ApiServer

    server = ApiServer(host="127.0.0.1", port=0)
    build_api_routes(server, container.exp_repo, container.template_repo)
    patterns = [p for _, p in server.route_list()]
    assert "/api/studies" not in patterns
    assert "/api/health" in patterns