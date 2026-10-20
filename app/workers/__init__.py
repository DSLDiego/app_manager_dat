"""Workers: execução em background (QThread/threads) para a UI."""

from app.workers.sampling_worker import SamplingWorker

__all__ = ["SamplingWorker"]
