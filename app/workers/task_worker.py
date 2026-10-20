"""Worker QThread que consome a fila em loop até ser parado."""

from __future__ import annotations

from PySide6.QtCore import Signal

from app.services.task_scheduler import TaskScheduler
from app.workers.base_worker import BaseWorker


class TaskWorker(BaseWorker):
    """Classe `TaskWorker` do módulo."""
    taskStarted = Signal(int)
    taskProgress = Signal(int, int, str)
    taskCompleted = Signal(int)
    taskFailed = Signal(int, str)
    idle = Signal()

    def __init__(self, scheduler: TaskScheduler, poll_ms: int = 500, parent=None):
        """Método `TaskWorker.__init__`.
            Parâmetros: `self`, `scheduler`, `poll_ms`, `parent`."""
        super().__init__(parent)
        self.scheduler = scheduler
        self.poll_ms = poll_ms
        self._stop = False

    def stop(self):
        """Método `TaskWorker.stop`."""
        self._stop = True

    def run(self):
        """Método `TaskWorker.run`.
            Parâmetros: `self`."""
        while not self._stop:
            task = self.scheduler.claim_next()
            if task is None:
                self.idle.emit()
                self.msleep(self.poll_ms)
                continue

            self.taskStarted.emit(task.id)
            try:
                self.scheduler.execute(
                    task,
                    progress_cb=lambda p, m, tid=task.id: self.taskProgress.emit(tid, p, m),
                    checkpoint_cb=lambda c, tid=task.id: self.scheduler.persist_cursor(tid, c),
                    stop_check=lambda: self._stop,
                )
                self.scheduler.mark_completed(task.id)
                self.taskCompleted.emit(task.id)
            except InterruptedError:
                self.scheduler.pause(task.id)
            except Exception as e:
                import traceback

                traceback.print_exc()
                self.scheduler.mark_failed(task.id, str(e))
                self.taskFailed.emit(task.id, str(e))
