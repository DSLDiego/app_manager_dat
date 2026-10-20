"""Entidades do domínio. Não importa PySide6, sqlite, scipy — nada."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass(frozen=True)
class Token:
    """Token detectado no template."""

    var_id: int
    raw: str
    start: int
    line: int
    column: int


@dataclass(frozen=True)
class DistributionSpec:
    """Especificação imutável de uma distribuição."""

    provider: str
    name: str
    params: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class VariableSpec:
    """Classe `VariableSpec` do módulo."""
    var_id: int
    name: str
    distribution: DistributionSpec


@dataclass(frozen=True)
class SamplingRequest:
    """Requisição imutável de amostragem (thread-safe e picklable)."""

    var_ids: List[int]
    specs: Dict[int, DistributionSpec]
    n_experiments: int
    seed: int
    strategy: str = "monte_carlo"
    workers: int = 1
    correlation: Optional[List[List[float]]] = None
    plugins_dir: Optional[str] = None


@dataclass(frozen=True)
class SamplingResult:
    """Resultado imutável."""

    var_ids: List[int]
    matrix: List[List[float]]
    seed_used: int
    duration_seconds: float
