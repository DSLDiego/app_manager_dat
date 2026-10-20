"""API REST local usando stdlib http.server (zero deps)."""

from __future__ import annotations

import json
import threading
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Callable, Dict, Optional, Tuple
from urllib.parse import parse_qs, urlparse


class ApiServer:
    """Classe `ApiServer` do módulo."""
    def __init__(
        self,
        host: str = "127.0.0.1",
        port: int = 8000,
        routes: Optional[Dict[Tuple[str, str], Callable]] = None,
        token: Optional[str] = None,
    ):
        """Método `ApiServer.__init__`.
            Parâmetros: `self`, `host`, `port`, `routes`, `token`."""
        self.host = host
        self.port = port
        self._routes: Dict[Tuple[str, str], Callable] = dict(routes or {})
        self._httpd: Optional[ThreadingHTTPServer] = None
        self._thread: Optional[threading.Thread] = None
        self.jobs: Dict[str, dict] = {}
        self._jobs_lock = threading.Lock()
        self.token = token

    # ---------- jobs assíncronos ----------
    def submit_job(self, fn: Callable[[], dict]) -> str:
        """Executa fn em thread daemon; status visível em GET /api/jobs/<job_id>."""
        job_id = uuid.uuid4().hex
        with self._jobs_lock:
            self.jobs[job_id] = {"job_id": job_id, "status": "running"}
        worker = threading.Thread(target=self._run_job, args=(job_id, fn), daemon=True)
        worker.start()
        return job_id

    def _run_job(self, job_id: str, fn: Callable[[], dict]) -> None:
        """Método `ApiServer._run_job`.
            Parâmetros: `self`, `job_id`, `fn`."""
        try:
            result = fn()
            result.update({"job_id": job_id, "status": "done"})
            with self._jobs_lock:
                self.jobs[job_id] = result
        except Exception as exc:
            with self._jobs_lock:
                self.jobs[job_id] = {
                    "job_id": job_id,
                    "status": "failed",
                    "error": str(exc),
                }

    def get_job(self, job_id: str) -> Optional[dict]:
        """Método `ApiServer.get_job`.
            Parâmetros: `self`, `job_id`.
            Retorna o resultado calculado a partir do estado local."""
        with self._jobs_lock:
            job = self.jobs.get(job_id)
        return dict(job) if job else None

    def route(self, method: str, pattern: str):
        """Método `ApiServer.route`.
            Parâmetros: `self`, `method`, `pattern`.
            Retorna o resultado calculado a partir do estado local."""
        def deco(fn):
            """Função `deco`.
                Parâmetros: `fn`.
                Retorna o resultado calculado a partir do estado local."""
            self._routes[(method.upper(), pattern)] = fn
            return fn
        return deco

    def route_list(self) -> list[tuple[str, str]]:
        """T5178: (método, padrão) registrados — usado pelo OpenAPI estático."""
        return sorted(self._routes.keys())

    def _handler_factory(self):
        """Método `ApiServer._handler_factory`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        routes = self._routes
        api = self

        class Handler(BaseHTTPRequestHandler):
            """Classe `Handler` do módulo."""
            def log_message(self, *args, **kwargs):
                """Método `Handler.log_message`.
                    Parâmetros: `self`, `*args`, `**kwargs`."""
                pass

            def _authorized(self, path: str) -> bool:
                """T5177: token local via 'Authorization: Bearer <token>'."""
                if not api.token:
                    return True
                if not path.startswith("/api/"):
                    return True
                if path == "/api/health":
                    return True
                header = self.headers.get("Authorization") or ""
                return header == f"Bearer {api.token}"

            def _dispatch(self, method: str):
                """Método `Handler._dispatch`.
                    Parâmetros: `self`, `method`.
                    Retorna o resultado calculado a partir do estado local."""
                import inspect

                parsed = urlparse(self.path)
                path = parsed.path
                if not self._authorized(path):
                    return self._send_json(401, {"error": "não autorizado"})
                qs = parse_qs(parsed.query)

                body_raw = None
                if method == "POST":
                    length = int(self.headers.get("Content-Length") or 0)
                    body_raw = self.rfile.read(length) if length else b""

                for (m, pattern), fn in routes.items():
                    if m != method:
                        continue
                    params = self._match(pattern, path)
                    if params is None:
                        continue
                    try:
                        try:
                            body = json.loads(body_raw) if body_raw else None
                        except json.JSONDecodeError:
                            return self._send_json(400, {"error": "JSON inválido"})
                        sig_len = len(inspect.signature(fn).parameters)
                        if sig_len >= 3:
                            result = fn(params, qs, body)
                        else:
                            result = fn(params, qs)
                        self._send_json(200, result)
                    except ValueError as e:
                        self._send_json(404, {"error": str(e)})
                    except Exception as e:
                        self._send_json(500, {"error": str(e)})
                    return
                self._send_json(404, {"error": "not found"})

            @staticmethod
            def _match(pattern: str, path: str):
                """Método `Handler._match`.
                    Parâmetros: `pattern`, `path`.
                    Retorna o resultado calculado a partir do estado local."""
                pp = pattern.strip("/").split("/")
                ap = path.strip("/").split("/")
                if len(pp) != len(ap):
                    return None
                params = {}
                for a, b in zip(pp, ap):
                    if a.startswith("<") and a.endswith(">"):
                        params[a[1:-1]] = b
                    elif a != b:
                        return None
                return params

            def _send_json(self, code: int, payload):
                """Método `Handler._send_json`.
                    Parâmetros: `self`, `code`, `payload`."""
                body = json.dumps(payload, ensure_ascii=False, default=str).encode("utf-8")
                self.send_response(code)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def do_GET(self):
                """Método `Handler.do_GET`.
                    Parâmetros: `self`."""
                self._dispatch("GET")

            def do_POST(self):
                """Método `Handler.do_POST`.
                    Parâmetros: `self`."""
                self._dispatch("POST")

        return Handler

    def start(self) -> int:
        """Método `ApiServer.start`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        if self._httpd:
            return self.port
        self._httpd = ThreadingHTTPServer(
            (self.host, self.port), self._handler_factory(),
        )
        self.port = self._httpd.server_address[1]
        self._thread = threading.Thread(
            target=self._httpd.serve_forever, daemon=True,
        )
        self._thread.start()
        return self.port

    def stop(self) -> None:
        """Método `ApiServer.stop`.
            Parâmetros: `self`."""
        if self._httpd:
            self._httpd.shutdown()
            self._httpd.server_close()
            self._httpd = None
            self._thread = None
