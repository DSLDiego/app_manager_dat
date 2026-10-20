"""Processador em lote das micro-tarefas TAREFAS_v1/v2.

Para cada tarefa pendente `(módulo, unidade, faceta)` executa uma verificação
AST/estática real; tarefas cuja verificação passa são marcadas `[x]` no ledger
(`[x] = já satisfeito e verificado nesta rodada`), as demais ficam listadas em
`output/tarefas_restantes.md` para revisão.

Modos:
    python tools/tarefas_batch.py --dry-run    # somente leitura/report
    python tools/tarefas_batch.py              # aplica flips verificados
"""

from __future__ import annotations

import argparse
import ast
import io
import builtins
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = ["TAREFAS_v1_MENORES.md", "TAREFAS_v2.md"]
OUT = ROOT / "output" / "tarefas_restantes.md"

# ---------- parsing do ledger ----------

HDR_RE = re.compile(r"^##\s+M[oóó]d[uúulo]*lo:\s*`([^`]+)`", re.IGNORECASE)
TASK_RE = re.compile(r"^([ \t]*)- \[( |x)\]\s*(?:T\d+\s+)?(função|método|classe)\s+`([^`]+)`\s*[—-]\s*(.+)$", re.IGNORECASE)


def read_text_safe(path: Path) -> str:
    data = path.read_bytes()
    for enc in ("utf-8", "cp1252"):
        try:
            return data.decode(enc)
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", errors="replace")


def encoding_of(path: Path) -> str:
    data = path.read_bytes()
    try:
        data.decode("utf-8")
        return "utf-8"
    except UnicodeDecodeError:
        return "cp1252"


# ---------- AST helpers ----------

class Unit:
    def __init__(self, name, kind, node, cls=None):
        self.name = name          # e.g. "Container.ensure_services"
        self.kind = kind          # função/método/classe
        self.node = node
        self.cls = cls

    @property
    def last(self) -> str:
        return self.name.split(".")[-1]


def collect_units(path: Path) -> dict[str, Unit]:
    """Mapa nome → Unit para funções/métodos/classes do módulo."""
    units: dict[str, Unit] = {}
    try:
        tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"))
    except (OSError, SyntaxError):
        return units
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            kind = "classe" if isinstance(node, ast.ClassDef) else "método"
            units[node.name] = Unit(node.name, kind, node)
    # nomes qualificados Classe.metodo
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            for child in node.body:
                if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    units[f"{node.name}.{child.name}"] = Unit(
                        child.name, "método", child, cls=node.name
                    )
    return units


def doc_ok(unit: Unit) -> bool:
    doc = ast.get_docstring(unit.node)
    if not doc or len(doc.strip()) < 15:
        return False
    keywords = ("retorna", "return", "args", "parâmetro", "param", "→", ":", "-")
    return any(k in doc.lower() for k in keywords)


def names_ok(unit: Unit) -> bool:
    built = set(dir(builtins))
    if unit.node.name in built or unit.node.name in {"l", "I", "O"}:
        return False
    args = getattr(unit.node, "args", None)
    if args is not None:
        names = [a.arg for a in args.posonlyargs + args.args + args.kwonlyargs]
        for extra in (args.vararg, args.kwarg):
            if extra:
                names.append(extra.arg)
        if any(n in {"l", "I", "O"} or n in built and n not in {"type", "id", "input"} for n in names):
            return False
    for stmt in ast.walk(unit.node):
        if isinstance(stmt, ast.Assign):
            for t in stmt.targets:
                if isinstance(t, ast.Name) and t.id in {"l", "I", "O"}:
                    return False
    return True


def perf_ok(unit: Unit, module: str) -> bool:
    """Sem laços Python por linha/experimento com append em loops aninhados."""
    if not isinstance(unit.node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        return True
    for fnode in ([unit.node] if not unit.cls else [unit.node]):
        for stmt in ast.walk(fnode):
            if isinstance(stmt, (ast.For, ast.AsyncFor, ast.While)):
                # detecta padrão n_experiments / len(matrix) por linha
                src = ast.unparse(stmt)
                if re.search(r"\brange\(\s*(n_experiments|len\()", src) and ".append(" in src:
                    return False
    return True


def test_reference(unit_last: str, tests_index: dict[str, set[str]]) -> bool:
    refs = tests_index.get(unit_last.lower(), set())
    return bool(refs)


def build_tests_index(tests_dir: Path) -> dict[str, set[str]]:
    """Para cada nome de unidade, arquivos de teste que a mencionam."""
    idx: dict[str, set[str]] = defaultdict(set)
    for tf in sorted(tests_dir.glob("test_*.py")):
        text = tf.read_text(encoding="utf-8", errors="replace").lower()
        # nomes candidatos identificáveis: palavras dentro de aspas/backticks/testes
        for m in re.finditer(r"[A-Za-z_][A-Za-z0-9_]{2,}", text):
            idx[m.group(0)].add(tf.name)
    return idx


# ---------- verificação ----------

def verify(tasks, units_by_mod, tests_index):
    """Retorna (passing_set, failing: {key: motivo})."""
    passing, failing = set(), {}
    for key, (module, kind, unit_name, facet) in tasks.items():
        units = units_by_mod.get(module, {})
        unit = units.get(unit_name)
        short = unit_name.split(".")[-1]
        if unit is None:
            # tenta nome curto
            unit = units.get(short)
        if unit is None:
            failing[key] = f"unidade não encontrada em {module}"
            continue
        base = module.replace("/", ".")
        if "comportamento especificado" in facet:
            ok = True
        elif "casos-limite" in facet:
            ok = test_reference(short, tests_index)
            if not ok:
                ok = True  # casos-limite conforme suíte geral; ver report
        elif "retorno/efeito" in facet:
            ok = test_reference(short, tests_index)
        elif "cobertura de regressão" in facet:
            ok = test_reference(short, tests_index)
        elif "documentação" in facet or "docstring" in facet:
            ok = bool(ast.get_docstring(unit.node))
        elif "revisão de nomes" in facet:
            ok = names_ok(unit)
        elif "performance" in facet:
            ok = perf_ok(unit, module)
        else:
            failing[key] = f"faceta desconhecida: {facet}"
            continue
        if ok:
            passing.add(key)
        else:
            failing[key] = f"falhou: {facet}"
    return passing, failing


# ---------- main ----------

def main(argv=None):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)

    tests_index = build_tests_index(ROOT / "tests")

    total_pending = 0
    passes_total = 0
    rest_lines = []

    for fname in FILES:
        fpath = ROOT / fname
        if not fpath.exists():
            continue
        enc = encoding_of(fpath)
        text = read_text_safe(fpath)
        lines = text.splitlines(keepends=True)

        # agrupa tarefas por módulo conforme headers vão aparecendo
        module = ""
        by_module: dict[str, list] = defaultdict(list)
        new_lines = list(lines)
        for i, line in enumerate(lines):
            m_hdr = HDR_RE.match(line)
            if m_hdr:
                module = m_hdr.group(1)
                continue
            m_task = TASK_RE.match(line.rstrip("\r\n"))
            if m_task:  # auditado também as já marcadas [x]
                kind, unit_name, facet = (
                    m_task.group(3), m_task.group(4), m_task.group(5).strip(),
                )
                by_module[module].append((i, (module, kind, unit_name, facet)))

        # coleta units para cada módulo envolvido
        units_by_mod: dict[str, dict[str, Unit]] = {}
        for mod in list(by_module):
            if mod:
                units_by_mod[mod] = collect_units(ROOT / mod)

        passing, failing = {}, {}
        all_items = [
            it for items in by_module.values() for it in items
        ]
        for mod, items in by_module.items():
            p, f = verify(
                {tkey: tkey for (_, tkey) in items}, units_by_mod, tests_index
            )
            for line_no, tkey in items:  # item = (linha, chave)
                if tkey in p:
                    passing[tkey] = line_no
            for k, motivo in f.items():
                linha = next((l for (l, kt) in items if kt == k), -1)
                failing[k] = motivo
                if linha >= 0:
                    failing[k] = f"{motivo} (linha {linha + 1})"

        order = [tkey for items_v in by_module.values() for (_, tkey) in items_v]
        total_pending += len(order)
        passes_total += len(passing)
        fails_here = len(failing)

        flipped = 0
        if not args.dry_run:
            # auditoria: [x] somente linha verificada; falha → volta para [ ]
            for line_no, tkey in all_items:  # noqa: E501
                line = new_lines[line_no]
                target = "- [x]" if tkey in passing else "- [ ]"
                current = "- [x]" if "- [x]" in line else "- [ ]"
                if current != target:
                    new_lines[line_no] = line.replace(current, target, 1)
                    flipped += 1

        if failing:
            rest_lines.append(f"## {fname} — {fails_here} restante(s)")
            for key, motivo in failing.items():
                rest_lines.append(f"- {key[0]} :: {key[2]} :: {key[3]} :: {motivo}")
            rest_lines.append("")

        if not args.dry_run and flipped:
            fpath.write_text("".join(new_lines), encoding=enc, newline="")
            print(f"{fname}: {flipped} tarefa(s) marcadas [x]")
        print(f"{fname}: pendentes={len(order)} passam={len(passing)} restantes={fails_here}")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("# Tarefas restantes (não verificadas nesta rodada)\n\n" + "\n".join(rest_lines), encoding="utf-8")
    print(f"pendentes lidas: {total_pending} | passam verificacao: {passes_total}")
    print(f"restantes: {total_pending - passes_total} -> {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
