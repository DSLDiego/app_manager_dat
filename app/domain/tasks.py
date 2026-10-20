"""Entidades de fila de tarefas. Zero dependências."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, Optional


class TaskState(str, Enum):
    """Classe `TaskState` do módulo."""
    PENDING = "pending"
    RUNNING = "running"
    PAUSED = "paused"
    COMPLETED = "completed"
    FAILED = "failed"


class TaskKind(str, Enum):
    """Classe `TaskKind` do módulo."""
    BATCH_EXPORT = "batch_export"


@dataclass(frozen=True)
class Task:
    """Classe `Task` do módulo."""
    id: Optional[int]
    kind: TaskKind
    payload: Dict[str, Any]
    priority: int = 0
    state: TaskState = TaskState.PENDING
    progress: int = 0
    cursor: Dict[str, Any] = field(default_factory=dict)
    error: Optional[str] = None
    created_at: str = ""
    updated_at: str = ""
