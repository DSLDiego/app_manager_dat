"""Testes do orquestrador de tarefas: fila persistente + execução de export."""

from pathlib import Path

import pytest

from app.domain.tasks import TaskKind, TaskState


def _make_scheduler(container, tmp_path):
    from app.infrastructure.task_repository import TaskRepository
    from app.services.task_scheduler import TaskScheduler

    repo = TaskRepository(str(tmp_path / "tasks.db"))
    return TaskScheduler(repo, container.batch_export_service)


def test_scheduler_execute_export(container, populated_batch, tmp_path):
    scheduler = _make_scheduler(container, tmp_path)
    task = scheduler.enqueue_export(
        populated_batch["batch_id"],
        populated_batch["version_id"],
        str(container.base_dir / "queue_out"),
    )
    assert task.state == TaskState.PENDING

    claimed = scheduler.claim_next()
    assert claimed is not None

    progress_seen = []

    scheduler.execute(
        claimed,
        progress_cb=lambda p, m: progress_seen.append(p),
        checkpoint_cb=lambda cursor: scheduler.persist_cursor(claimed.id, cursor),
        stop_check=lambda: False,
    )
    scheduler.mark_completed(claimed.id)

    out = Path(container.base_dir) / "queue_out" / populated_batch["batch_id"] / "v1"
    assert len(list(out.glob("*.dat"))) == 12
    assert scheduler.state_of(claimed.id) == TaskState.COMPLETED
    assert progress_seen


def test_scheduler_pause_resume(container, populated_batch, tmp_path):
    scheduler = _make_scheduler(container, tmp_path)
    task = scheduler.enqueue_export(
        populated_batch["batch_id"], populated_batch["version_id"],
        str(container.base_dir / "queue_pause"),
    )
    scheduler.pause(task.id)
    assert scheduler.state_of(task.id) == TaskState.PAUSED
    scheduler.resume(task.id)
    assert scheduler.state_of(task.id) == TaskState.PENDING


def test_scheduler_unknown_kind_supported(container, populated_batch, tmp_path):
    scheduler = _make_scheduler(container, tmp_path)
    fake = type("TaskTest", (), {})()
    fake.kind = "import"
    with pytest.raises(ValueError):
        scheduler.execute(
            fake,
            progress_cb=lambda *_: None,
            checkpoint_cb=lambda c: None,
            stop_check=lambda: False,
        )
