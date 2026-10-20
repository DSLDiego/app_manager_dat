"""R31: validação fina de parâmetros de distribuição (puro)."""

from __future__ import annotations

import math

MAX_ABS_LOC = 1e15
MAX_SCALE = 1e12
MIN_SCALE = 1e-12


def _as_float(value):
    """Função `_as_float`.
        Parâmetros: `value`.
        Retorna o resultado calculado a partir do estado local."""
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def validate_spec_params(provider: str, params: dict) -> list[str]:
    """Lista de erros de domínio para loc/scale e afins; vazia = válido."""
    errors: list[str] = []
    params = dict(params or {})

    scale = params.get("scale")
    if scale is not None:
        value = _as_float(scale)
        if value is None:
            errors.append("scale deve ser numérico")
        elif not math.isfinite(value):
            errors.append("scale deve ser finito")
        elif value <= 0:
            errors.append("scale deve ser > 0")
        elif value < MIN_SCALE:
            errors.append(f"scale muito pequeno (mínimo {MIN_SCALE:g})")
        elif value > MAX_SCALE:
            errors.append(f"scale muito grande (máximo {MAX_SCALE:g})")

    loc = params.get("loc")
    if loc is not None:
        value = _as_float(loc)
        if value is None:
            errors.append("loc deve ser numérico")
        elif not math.isfinite(value):
            errors.append("loc deve ser finito")
        elif abs(value) > MAX_ABS_LOC:
            errors.append(f"|loc| excede o máximo {MAX_ABS_LOC:g}")

    low, mode, high = params.get("low"), params.get("mode"), params.get("high")
    if low is not None or mode is not None or high is not None:
        low_v, mode_v, high_v = _as_float(low), _as_float(mode), _as_float(high)
        if low_v is None or mode_v is None or high_v is None:
            errors.append("triangular requer low, mode e high numéricos")
        elif not (low_v <= mode_v <= high_v):
            errors.append("triangular exige low <= mode <= high")
        elif low_v == high_v:
            errors.append("triangular exige low < high")

    a, b = params.get("a"), params.get("b")
    if a is not None and b is not None:
        a_v, b_v = _as_float(a), _as_float(b)
        if a_v is not None and b_v is not None and a_v >= b_v:
            errors.append("uniforme exige a < b")

    value = params.get("value")
    if provider == "fixed" and value is not None:
        value_v = _as_float(value)
        if value_v is None or not math.isfinite(value_v):
            errors.append("valor fixo deve ser finito")

    return errors
