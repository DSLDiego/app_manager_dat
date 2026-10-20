"""Testes do log service/repo async: fila, busca e CSV-safe types."""

import time


def test_log_write_and_fetch(log_service):
    log_service["svc"].info("SAMPLING", "start", "n=10")
    log_service["svc"].warning("EDITOR", "missing", "token $5 sem dist")
    time.sleep(0.3)

    repo = log_service["repo"]
    assert repo.count() == 2

    rows = repo.fetch()
    assert len(rows) >= 2
    assert rows[0]["level"] in ("INFO", "WARNING")

    errors = repo.fetch(level="WARNING")
    assert len(errors) == 1
    assert errors[0]["category"] == "EDITOR"

    search = repo.fetch(search="token")
    assert len(search) == 1


def test_log_write_does_not_block(log_repo):
    from app.services.log_service import LogService

    svc = LogService(repo=log_repo)
    t0 = time.perf_counter()
    for i in range(2000):
        svc.info("USAGE", f"action_{i}", f"msg {i}")
    elapsed = time.perf_counter() - t0
    assert elapsed < 0.25


def test_event_bus_sanity(log_service):
    from app.domain.events import LogCreatedEvent
    from app.infrastructure.event_bus import EventBus

    bus = EventBus()
    received = []
    bus.subscribe(LogCreatedEvent, lambda e: received.append(e.message))
    bus.publish(LogCreatedEvent("INFO", "TESTE", "pub", "Olá"))
    assert received == ["Olá"]
