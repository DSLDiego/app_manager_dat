"""Teste do worker: singleton execução em QThread (offscreen)."""

import pytest

pytest.importorskip("pytestqt")

from app.domain.entities import DistributionSpec, SamplingRequest


def test_sampling_worker_run_to_completion(qtbot, qapp):
    from PySide6.QtCore import QObject, Slot

    from app.infrastructure.distribution_registry import build_default_registry
    from app.services.sampling_service import SamplingService
    from app.workers.sampling_worker import SamplingWorker

    class Capture(QObject):
        def __init__(self):
            super().__init__()
            self.results = []

        @Slot(object)
        def on_completed(self, result):
            self.results.append(result)

    specs = {
        1: DistributionSpec(provider="scipy", name="norm", params={"loc": 0.0, "scale": 1.0}),
        2: DistributionSpec(provider="fixed", name="value", params={"value": 3.0}),
    }
    request = SamplingRequest(var_ids=[1, 2], specs=specs, n_experiments=50, seed=5)
    worker = SamplingWorker(SamplingService(build_default_registry()), request)
    cap = Capture()

    worker.completed.connect(cap.on_completed)
    worker.start()
    worker.wait(20000)
    qtbot.waitUntil(lambda: bool(cap.results), timeout=20000)
    assert cap.results and len(cap.results[0].matrix) == 50
