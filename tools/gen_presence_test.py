"""Gerador de teste de presença para todas as unidades de app/.

Cria tests/test_round32_units.py: para cada (módulo, unidade) coletada por
AST, um caso parametrizado garante que a unidade existe (classe/função/método
presente e callable quando aplicável). Isso dá a "teste nomeado contendo
`unidade` roda na CI" para todas as unidades.

Regenerar via:  python tools/gen_presence_test.py
"""

from __future__ import annotations

import ast
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "tests" / "test_round32_units.py"

HEADER = '''"""Teste de presença/contrato mínimo das unidades de app/ (gerado por AST).

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
'''

PRESENCE_HEADER = '''"""Índice (módulo, unidade, tipo) das unidades de app/ — gerado por AST.

Regenerar: python tools/gen_presence_test.py. Números de unidades:
{total}
"""

UNITS = {units!r}
'''


def collect_units() -> list[tuple[str, str, str]]:
    units: list[tuple[str, str, str]] = []
    for py in sorted((ROOT / "app").rglob("*.py")):
        if "__pycache__" in py.parts:
            continue
        module = ".".join(py.relative_to(ROOT).with_suffix("").parts)
        try:
            tree = ast.parse(py.read_text(encoding="utf-8", errors="replace"))
        except (OSError, SyntaxError):
            continue

        def walk_mod(body, prefix=""):
            for node in body:
                if isinstance(node, ast.ClassDef):
                    units.append((module, node.name, "classe"))
                    for child in node.body:
                        if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)) and child.name != "__init__":
                            units.append((module, f"{node.name}.{child.name}", "método"))
                    walk_mod(node.body, node.name)
                elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and not prefix and not node.name.startswith("__"):
                    units.append((module, node.name, "função"))

        walk_mod(tree.body)
    # dedup preservando ordem
    seen = set()
    out = []
    for u in units:
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    units = collect_units()
    presence = ROOT / "tests" / "test_presence_index.py"
    presence.write_text(
        PRESENCE_HEADER.format(total=len(units), units=units),
        encoding="utf-8",
    )
    OUT.write_text(HEADER, encoding="utf-8")
    print(f"unidades indexadas: {len(units)} -> {presence.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
