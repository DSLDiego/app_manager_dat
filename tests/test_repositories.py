"""Testes dos repositórios: experimentos, templates, tarefas --- paginação e versionamento."""

import pytest


def test_experiment_repository_roundtrip(repos):
    exp = repos["exp"]
    exp.create_batch("b1", "monte_carlo", seed=42, n_experiments=3)
    exp.insert_result("b1", [1, 2], [[1.0, 4.0], [2.0, 5.0], [3.0, 6.0]])

    assert exp.count() == 3
    var_ids = exp.var_ids()
    assert var_ids == [1, 2]

    page_rows = exp.fetch_page(0, 2, var_ids)
    assert len(page_rows) == 2
    assert page_rows[0]["values"] == {1: 1.0, 2: 4.0}

    values = exp.get_variable_values(1)
    assert values == [1.0, 2.0, 3.0]

    row = exp.get_experiment_values(1)
    assert row == {1: 1.0, 2: 4.0}


def test_template_repository_versions_and_current(repos):
    tpl = repos["tpl"]
    template_id = tpl.create_template("base", "descrição")
    assert template_id == 1

    v1 = tpl.save_version(template_id, "conteudo v1", comment="primeiro")
    v2 = tpl.save_version(template_id, "conteudo v2")

    versions = tpl.list_versions(template_id)
    assert [v["version_number"] for v in versions] == [1, 2]

    current = tpl.get_current(template_id)
    assert current["content"] == "conteudo v2"
    assert current["content_hash"] == versions[-1]["content_hash"]
    assert v1 != v2


def test_template_repository_get_version(repos):
    tpl = repos["tpl"]
    template_id = tpl.create_template("t")
    version_id = tpl.save_version(template_id, "abc")
    version = tpl.get_version(version_id)
    assert version["content"] == "abc"
    assert tpl.get_version(999) is None


def test_task_repository_create_and_flow(tmp_path):
    from app.domain.tasks import TaskKind, TaskState
    from app.infrastructure.task_repository import TaskRepository

    repo = TaskRepository(str(tmp_path / "tasks.db"))

    task = repo.create(TaskKind.BATCH_EXPORT, {"batch_id": "b", "template_version_id": 1, "output_root": "out"})
    assert task.state == TaskState.PENDING

    claimed = repo.next_pending()
    assert claimed is not None
    assert claimed.id == task.id

    repo.update_progress(task.id, 50, {"last_external_id": 5})
    updated = repo.get(task.id)
    assert updated.progress == 50
    assert updated.state == TaskState.RUNNING
    assert updated.cursor == {"last_external_id": 5}

    repo.complete(task.id)
    done = repo.get(task.id)
    assert done.state == TaskState.COMPLETED
    assert done.progress == 100
    assert repo.next_pending() is None
    repo.close()


def test_task_repository_fail_pause_recover(tmp_path):
    from app.domain.tasks import TaskKind, TaskState
    from app.infrastructure.task_repository import TaskRepository

    repo = TaskRepository(str(tmp_path / "tasks2.db"))
    t1 = repo.create(TaskKind.BATCH_EXPORT, {})
    t2 = repo.create(TaskKind.BATCH_EXPORT, {})

    repo.fail(t1.id, "boom")
    assert repo.get(t1.id).state == TaskState.FAILED

    repo.pause(t2.id)
    assert repo.get(t2.id).state == TaskState.PAUSED

    # simula crash com processo travado em RUNNING — recovery volta para PENDING
    repo.update_progress(t2.id, 30, {"last_external_id": 3})
    recovered = repo.recover_interrupted()
    assert recovered == 1
    assert repo.get(t2.id).state == TaskState.PENDING

    task = repo.next_pending()
    assert task is not None
    assert task.progress == 30
    repo.close()
