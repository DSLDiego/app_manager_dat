"""Diff de specs entre dois estudos — puro, sem Qt.

Formatos aceitos (ambos conversíveis a {str(var): {provider,name,params}}):
  {var_id: DistributionSpec}    (serviço)
  {str(var_id): {provider,name,params}}  (store / JSON)
"""

from __future__ import annotations


def _normalize(specs) -> dict[str, dict]:
    """Função `_normalize`.
        Parâmetros: `specs`.
        Retorna o resultado calculado a partir do estado local."""
    out: dict[str, dict] = {}
    for var_id, spec in (specs or {}).items():
        if isinstance(spec, dict):
            fields = dict(spec)
        else:  # DistributionSpec ou afins
            fields = {
                "provider": getattr(spec, "provider", None),
                "name": getattr(spec, "name", getattr(spec, "type", None)),
                "params": getattr(spec, "params", {}),
            }
        out[str(var_id)] = fields
    return out


def specs_diff(specs_a, specs_b) -> dict:
    """{"added": [var…], "removed": [var…], "changed": [{var, field, a, b}…]} — puro."""
    a = _normalize(specs_a)
    b = _normalize(specs_b)
    added = sorted(set(b) - set(a), key=lambda x: float(x) if x.replace(".", "", 1).isdigit() else 0)
    removed = sorted(set(a) - set(b), key=lambda x: float(x) if x.replace(".", "", 1).isdigit() else 0)
    changed = []
    for key in sorted(set(a) & set(b)):
        sa, sb = a[key], b[key]
        for field in ("provider", "name", "params"):
            if sa.get(field) != sb.get(field):
                changed.append(
                    {"var": key, "field": field, "a": sa.get(field), "b": sb.get(field)}
                )
    return {"added": added, "removed": removed, "changed": changed}


def diff_is_empty(diff: dict) -> bool:
    """True se estudos idênticos — puro."""
    return not (diff["added"] or diff["removed"] or diff["changed"])


def diff_line(entry: dict) -> str:
    """Linha curta p/ tabela/tooltip — puro."""
    field = entry["field"]
    return f"$var{entry['var']} · {field}: {entry['a']} → {entry['b']}"
