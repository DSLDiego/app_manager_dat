"""Teste de presença/contrato mínimo das unidades de app/ (gerado por AST).

Cada caso verifica que a unidade existe no módulo correspondente e que
classes/def/descriptors expostos têm o tipo esperado. Regenerado por
tools/gen_presence_test.py — não edite à mão.
"""

from __future__ import annotations

import importlib

import pytest

from test_presence_index import UNITS

N = len(UNITS)


@pytest.mark.parametrize("module", sorted({m for m, _, _ in UNITS}))
def test_module_imports(module: str) -> None:
    importlib.import_module(module)


@pytest.mark.parametrize("module,name,kind", UNITS)
def test_unit_exists(module: str, name: str, kind: str) -> None:
    mod = importlib.import_module(module)
    qual = name.split(".")
    obj = mod
    for part in qual:
        obj = getattr(obj, part)
    if kind == "classe":
        assert isinstance(obj, type)
    else:
        assert callable(obj) or isinstance(obj, property), (module, name, kind)
