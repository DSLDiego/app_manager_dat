"""Event bus. Desacopla completamente UI de services e workers."""

from __future__ import annotations

import threading
import traceback
from collections import defaultdict
from typing import Callable, Dict, List, Type, TypeVar

from app.domain.events import AppEvent

E = TypeVar("E", bound=AppEvent)


class EventBus:
    """Classe `EventBus` do módulo."""
    def __init__(self):
        """Método `EventBus.__init__`.
            Parâmetros: `self`."""
        self._subscribers: Dict[Type[AppEvent], List[Callable]] = defaultdict(list)
        self._lock = threading.Lock()

    def subscribe(self, event_type: Type[E], handler: Callable[[E], None]) -> None:
        """Método `EventBus.subscribe`.
            Parâmetros: `self`, `event_type`, `handler`."""
        with self._lock:
            self._subscribers[event_type].append(handler)

    def unsubscribe(self, event_type: Type[E], handler: Callable[[E], None]) -> None:
        """Método `EventBus.unsubscribe`.
            Parâmetros: `self`, `event_type`, `handler`."""
        with self._lock:
            if handler in self._subscribers[event_type]:
                self._subscribers[event_type].remove(handler)

    def publish(self, event: AppEvent) -> None:
        """Método `EventBus.publish`.
            Parâmetros: `self`, `event`."""
        handlers = list(self._subscribers.get(type(event), []))
        for handler in handlers:
            try:
                handler(event)
            except Exception:
                traceback.print_exc()
