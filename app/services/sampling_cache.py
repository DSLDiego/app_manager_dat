"""R31: cache de resultados de amostragem por (vars, specs, n, estratégia, seed)."""

from __future__ import annotations

import hashlib
import json
from collections import OrderedDict
from typing import Optional


def cache_key(var_ids, specs, n: int, strategy: str, seed) -> str:
    """Chave estável e determinística; specs podem ser dataclasses/dicts."""
    parts = {
        "var_ids": [int(v) for v in var_ids],
        "n": int(n),
        "strategy": str(strategy),
        "seed": None if seed is None else str(seed),
    }
    spec_part = {}
    for var_id in var_ids:
        spec = specs[var_id]
        provider = getattr(spec, "provider", None)
        params = getattr(spec, "params", None)
        if params is None and isinstance(spec, dict):
            provider = spec.get("provider")
            params = spec.get("params")
        spec_part[str(int(var_id))] = {
            "provider": provider,
            "params": {
                str(k): (float(v) if isinstance(v, (int, float)) else str(v))
                for k, v in dict(params or {}).items()
            },
        }
    parts["specs"] = spec_part
    payload = json.dumps(parts, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


class SamplingCache:
    """LRU simples, sem threads (uso no processo da GUI)."""

    def __init__(self, max_entries: int = 8):
        """Método `SamplingCache.__init__`.
            Parâmetros: `self`, `max_entries`."""
        self.max_entries = max(1, int(max_entries))
        self._data: "OrderedDict[str, object]" = OrderedDict()
        self.hits = 0
        self.misses = 0

    def get(self, key: str):
        """Método `SamplingCache.get`.
            Parâmetros: `self`, `key`.
            Retorna o resultado calculado a partir do estado local."""
        if key in self._data:
            self._data.move_to_end(key)
            self.hits += 1
            return self._data[key]
        self.misses += 1
        return None

    def put(self, key: str, result) -> None:
        """Método `SamplingCache.put`.
            Parâmetros: `self`, `key`, `result`."""
        self._data[key] = result
        self._data.move_to_end(key)
        while len(self._data) > self.max_entries:
            self._data.popitem(last=False)

    def clear(self) -> None:
        """Método `SamplingCache.clear`.
            Parâmetros: `self`."""
        self._data.clear()
        self.hits = 0
        self.misses = 0

    def __len__(self) -> int:
        """Método `SamplingCache.__len__`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        return len(self._data)
