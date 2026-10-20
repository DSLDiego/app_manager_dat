"""Log service: fachada de escrita de logs (category + event bus)."""

from __future__ import annotations

from typing import Any, Dict, Optional

from app.domain.events import LogCreatedEvent
from app.infrastructure.async_log_repository import AsyncLogRepository
from app.infrastructure.event_bus import EventBus


class LogService:
    """Fachada de logs. Nunca bloqueia: escreve somente na fila async."""

    def __init__(
        self,
        event_bus: Optional[EventBus] = None,
        repo: Optional[AsyncLogRepository] = None,
    ):
        """Método `LogService.__init__`.
            Parâmetros: `self`, `event_bus`, `repo`."""
        self.event_bus = event_bus
        self.repo = repo

    def _emit(
        self,
        level: str,
        category: str,
        action: str,
        message: str = "",
        entity_type: Optional[str] = None,
        entity_id: Optional[int] = None,
        payload: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Método `LogService._emit`.
            Parâmetros: `self`, `level`, `category`, `action`, `message`, `entity_type`, `entity_id`, `payload`."""
        if self.repo is not None:
            self.repo.log(
                level=level,
                category=category,
                action=action,
                entity_type=entity_type,
                entity_id=entity_id,
                message=message,
                payload=payload,
            )
        if self.event_bus is not None:
            self.event_bus.publish(
                LogCreatedEvent(level=level, category=category, action=action, message=message)
            )

    def info(self, category: str, action: str, message: str = "", **kw) -> None:
        """Método `LogService.info`.
            Parâmetros: `self`, `category`, `action`, `message`, `**kw`."""
        self._emit("INFO", category, action, message, **kw)

    def warning(self, category: str, action: str, message: str = "", **kw) -> None:
        """Método `LogService.warning`.
            Parâmetros: `self`, `category`, `action`, `message`, `**kw`."""
        self._emit("WARNING", category, action, message, **kw)

    def error(self, category: str, action: str, message: str = "", **kw) -> None:
        """Método `LogService.error`.
            Parâmetros: `self`, `category`, `action`, `message`, `**kw`."""
        self._emit("ERROR", category, action, message, **kw)

    def usage(self, action: str, message: str = "", **kw) -> None:
        """Método `LogService.usage`.
            Parâmetros: `self`, `action`, `message`, `**kw`."""
        self._emit("INFO", "USAGE", action, message, **kw)

    def audit(self, action: str, message: str = "", **kw) -> None:
        """Método `LogService.audit`.
            Parâmetros: `self`, `action`, `message`, `**kw`."""
        self._emit("INFO", "AUDIT", action, message, **kw)
