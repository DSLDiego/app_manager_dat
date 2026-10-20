"""Worker: roda SamplingService em thread separada, com ProcessPool interno."""

from __future__ import annotations

import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from typing import Optional

import numpy as np
from PySide6.QtCore import Signal

from app.domain.entities import SamplingRequest, SamplingResult
from app.services.sampling_service import SamplingService
from app.workers.base_worker import BaseWorker


def _chunk_worker(args):
    """Top-level: necessária para ser picklable."""
    request, start, size = args
    partial = SamplingRequest(
        var_ids=request.var_ids,
        specs=request.specs,
        n_experiments=size,
        seed=request.seed + start,
        strategy=request.strategy,
        workers=1,
        correlation=request.correlation,
    )
    from app.infrastructure.distribution_registry import build_registry

    service = SamplingService(build_registry(request.plugins_dir))
    result = service.run(partial)
    return start, result.matrix


class SamplingWorker(BaseWorker):
    """Classe `SamplingWorker` do módulo."""
    progress = Signal(int, str)
    completed = Signal(object)
    failed = Signal(str)

    def __init__(self, service: SamplingService, request: SamplingRequest, parent=None):
        """Método `SamplingWorker.__init__`.
            Parâmetros: `self`, `service`, `request`, `parent`."""
        super().__init__(parent)
        self.service = service
        self.request = request

    def run(self):
        """Método `SamplingWorker.run`.
            Parâmetros: `self`."""
        try:
            req = self.request

            if req.workers <= 1 or req.n_experiments < 500:
                result = self.service.run(req, progress_cb=self.progress.emit)
                self.completed.emit(result)
                return

            chunk_size = max(1, req.n_experiments // (req.workers * 4))
            starts = list(range(0, req.n_experiments, chunk_size))
            tasks = [(req, s, min(chunk_size, req.n_experiments - s)) for s in starts]

            results = [None] * len(tasks)
            started = time.perf_counter()

            with ProcessPoolExecutor(max_workers=req.workers) as pool:
                futures = {pool.submit(_chunk_worker, t): i for i, t in enumerate(tasks)}
                done = 0
                for fut in as_completed(futures):
                    i = futures[fut]
                    start, matrix = fut.result()
                    results[i] = (start, matrix)
                    done += 1
                    self.progress.emit(
                        int(100 * done / len(tasks)), f"Bloco {done}/{len(tasks)}"
                    )

            ordered = sorted(results, key=lambda x: x[0])
            full = np.vstack([np.array(m) for _, m in ordered])

            self.completed.emit(
                SamplingResult(
                    var_ids=list(req.var_ids),
                    matrix=full.tolist(),
                    seed_used=req.seed,
                    duration_seconds=time.perf_counter() - started,
                )
            )

        except Exception as exc:
            import traceback

            traceback.print_exc()
            self.failed.emit(str(exc))
