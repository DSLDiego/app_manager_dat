"""Domínio puro do DAT Engineering Studio (sem dependências externas)."""

from app.domain.entities import DistributionSpec, SamplingRequest, SamplingResult, Token, VariableSpec
from app.domain.events import AppEvent

__all__ = [
    "AppEvent",
    "DistributionSpec",
    "SamplingRequest",
    "SamplingResult",
    "Token",
    "VariableSpec",
]
