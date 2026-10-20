"""Orquestra fila persistente. Não conhece Qt."""

from __future__ import annotations

from typing import Any, Callable, Dict, Optional

from app.domain.tasks import Task, TaskKind, TaskState
from app.infrastructure.task_repository import TaskRepository


class TaskScheduler:
    """Classe `TaskScheduler` do módulo."""
    def __init__(self, repo: TaskRepository, export_svc):
        """Método `TaskScheduler.__init__`.
            Parâmetros: `self`, `repo`, `export_svc`."""
        self.repo = repo
        self.export_svc = export_svc

    def recover(self) -> int:
        """Método `TaskScheduler.recover`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        return self.repo.recover_interrupted()

    def enqueue_export(
        self, batch_id: str, template_version_id: int, output_root: str,
        priority: int = 0,
    ) -> Task:
        """Método `TaskScheduler.enqueue_export`.
            Parâmetros: `self`, `batch_id`, `template_version_id`, `output_root`, `priority`.
            Retorna o resultado calculado a partir do estado local."""
        return self.repo.create(TaskKind.BATCH_EXPORT, {
            "batch_id": batch_id,
            "template_version_id": template_version_id,
            "output_root": output_root,
        }, priority=priority)

    def claim_next(self) -> Optional[Task]:
        """Método `TaskScheduler.claim_next`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        task = self.repo.next_pending()
        if task:
            self.repo.update_progress(task.id, task.progress, task.cursor)
        return task

    def execute(
        self,
        task: Task,
        progress_cb: Callable[[int, str], None],
        checkpoint_cb: Callable[[Dict[str, Any]], None],
        stop_check: Callable[[], bool],
    ) -> None:
        """Método `TaskScheduler.execute`.
            Parâmetros: `self`, `task`, `progress_cb`, `checkpoint_cb`, `stop_check`.
            Levanta: ValueError."""
        if task.kind == TaskKind.BATCH_EXPORT:
            self._run_export(task, progress_cb, checkpoint_cb, stop_check)
        else:
            raise ValueError(f"Kind não suportado: {task.kind}")

    def _run_export(self, task, progress_cb, checkpoint_cb, stop_check) -> None:
        """Método `TaskScheduler._run_export`.
            Parâmetros: `self`, `task`, `progress_cb`, `checkpoint_cb`, `stop_check`."""
        payload = task.payload
        start = int(task.cursor.get("last_external_id", 0)) + 1

        self.export_svc.export(
            batch_id=payload["batch_id"],
            template_version_id=int(payload["template_version_id"]),
            output_root=payload["output_root"],
            start_external_id=start,
            progress_cb=progress_cb,
            checkpoint_cb=lambda done, last_id: checkpoint_cb(
                {"last_external_id": last_id}
            ),
            stop_check=stop_check,
        )

    def persist_cursor(self, task_id: int, cursor: Dict[str, Any]) -> None:
        """Método `TaskScheduler.persist_cursor`.
            Parâmetros: `self`, `task_id`, `cursor`."""
        task = self.repo.get(task_id)
        if task:
            self.repo.update_progress(task_id, task.progress, cursor)

    def mark_completed(self, task_id: int) -> None:
        """Método `TaskScheduler.mark_completed`.
            Parâmetros: `self`, `task_id`."""
        self.repo.complete(task_id)

    def mark_failed(self, task_id: int, error: str) -> None:
        """Método `TaskScheduler.mark_failed`.
            Parâmetros: `self`, `task_id`, `error`."""
        self.repo.fail(task_id, error)

    def pause(self, task_id: int) -> None:
        """Método `TaskScheduler.pause`.
            Parâmetros: `self`, `task_id`."""
        self.repo.pause(task_id)

    def resume(self, task_id: int) -> None:
        """Método `TaskScheduler.resume`.
            Parâmetros: `self`, `task_id`."""
        self.repo.resume(task_id)

    def state_of(self, task_id: int) -> Optional[TaskState]:
        """Método `TaskScheduler.state_of`.
            Parâmetros: `self`, `task_id`.
            Retorna o resultado calculado a partir do estado local."""
        task = self.repo.get(task_id)
        return task.state if task else None
