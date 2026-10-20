"""Eventos de domínio. UI reage via event bus, sem dependência direta."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AppEvent:
    """Evento base."""


@dataclass(frozen=True)
class TemplateDetectedEvent(AppEvent):
    """Classe `TemplateDetectedEvent` do módulo."""
    template_text: str
    var_ids: tuple


@dataclass(frozen=True)
class DistributionChangedEvent(AppEvent):
    """Classe `DistributionChangedEvent` do módulo."""
    var_id: int
    spec: dict


@dataclass(frozen=True)
class SamplingStartedEvent(AppEvent):
    """Classe `SamplingStartedEvent` do módulo."""
    n_experiments: int
    seed: int


@dataclass(frozen=True)
class SamplingProgressEvent(AppEvent):
    """Classe `SamplingProgressEvent` do módulo."""
    percent: int
    message: str


@dataclass(frozen=True)
class SamplingCompletedEvent(AppEvent):
    """Classe `SamplingCompletedEvent` do módulo."""
    var_ids: tuple
    matrix: tuple
    seed_used: int
    duration_seconds: float


@dataclass(frozen=True)
class SamplingFailedEvent(AppEvent):
    """Classe `SamplingFailedEvent` do módulo."""
    error: str


@dataclass(frozen=True)
class LogCreatedEvent(AppEvent):
    """Classe `LogCreatedEvent` do módulo."""
    level: str
    category: str
    action: str
    message: str
