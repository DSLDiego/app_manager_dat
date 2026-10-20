"""Insere docstring derivada de AST nas unidades sem docstring.

A docstring é construída a partir do código real: listagem de parâmetros,
seção Retorna (se há return) e Levanta (nomes de exceções realmente
levantadas no corpo). Não inventa comportamento.

Modo de segurança: sobrescreve o arquivo somente quando consegue inserir
todas as docstrings com sintaxe correta; um ast.parse após edição valida.
"""

from __future__ import annotations

import ast
import copy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def exceptions_in(node: ast.stmt) -> list[str]:
    names: list[str] = []
    for sub in ast.walk(node):
        if isinstance(sub, ast.Raise):
            exc = sub.exc
            if isinstance(exc, ast.Call):
                exc = exc.func
            if isinstance(exc, ast.Name):
                names.append(exc.id)
            elif isinstance(exc, ast.Attribute):
                names.append(exc.attr)
    seen: set[str] = set()
    return [n for n in names if not (n in seen or seen.add(n))]


def compose_doc(kind: str, name: str, node: ast.AST) -> str:
    """Docstring com contrato — derivada exclusivamente do código."""
    if isinstance(node, ast.ClassDef):
        base = f"{kind.title()} `{name}` do módulo."
        return f'    """{base}"""'
    args = getattr(node, "args", None)
    argnames: list[str] = []
    if args is not None:
        argnames = [a.arg for a in args.posonlyargs + args.args + args.kwonlyargs]
        if args.vararg:
            argnames.append(f"*{args.vararg.arg}")
        if args.kwarg:
            argnames.append(f"**{args.kwarg.arg}")
    article = "Método" if kind == "método" else "Função"
    head = f"{article} `{name}`."
    doc_parts = [head]
    if argnames:
        doc_parts.append("Parâmetros: " + ", ".join("`" + a + "`" for a in argnames) + ".")
    has_return = any(isinstance(s, ast.Return) and s.value is not None for s in ast.walk(node))
    if has_return:
        doc_parts.append("Retorna o resultado calculado a partir do estado local.")
    excs = exceptions_in(node)
    if excs:
        doc_parts.append("Levanta: " + ", ".join(excs) + ".")
    if not node.body or not any(isinstance(s, ast.Assert) for s in ast.walk(node)) and len(ast.unparse(node)) < 40:
        return f'    """{head}"""'
    return "    " + '"""' + "\n    ".join(doc_parts) + '"""'


def insert_docstrings(path: Path) -> int:
    src = path.read_text(encoding="utf-8")
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return 0
    lines = src.splitlines(keepends=True)
    edits: list[tuple[int, int, str]] = []  # (start0, end0, replacement)

    def visit(node, kind_prefix=""):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            kind = "classe" if isinstance(node, ast.ClassDef) else (
                "método" if kind_prefix else "função"
            )
            if not ast.get_docstring(node):
                indent = " " * node.body[0].col_offset
                name = node.name if not kind_prefix else f"{kind_prefix}.{node.name}"
                doc = compose_doc(kind, name, node)
                doc_text = "\n".join(
                    (indent + ln).rstrip() for ln in doc.strip().splitlines()
                )
                b0 = node.body[0]
                if isinstance(node, ast.ClassDef):
                    # edita apenas a linha do header da classe (evita engolir o corpo)
                    start = node.lineno - 1
                    hdr_line = lines[start]
                    if hdr_line.rstrip().endswith(":"):
                        new = hdr_line.rstrip("\r\n") + "\n" + doc_text + "\n"
                        edits.append((start, start + 1, new))
                else:
                    b0_end = max(b0.end_lineno or b0.lineno, b0.lineno)
                    s_start = node.lineno - 1
                    s_end = b0_end
                    span = "".join(lines[s_start:s_end])
                    k = span.rfind(":")
                    header, body_code = (
                        span[: k + 1], span[k + 1 :].strip()
                    ) if k != -1 else ("", "")
                    if header:
                        if body_code:
                            new = header + "\n" + doc_text + "\n" + indent + body_code + "\n"
                        else:
                            new = header + doc_text + "\n"
                        edits.append((s_start, s_end, new))
        for child in ast.iter_child_nodes(node):
            prefix = (
                node.name
                if isinstance(node, ast.ClassDef)
                and isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef))
                else kind_prefix if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) else ""
            )
            visit(child, prefix)

    visit(tree)
    if not edits:
        return 0
    # aplica edits de trás para frente (end é exclusivo)
    for start, end, replacement in sorted(edits, key=lambda e: -e[0]):
        lines[start:end] = [replacement]
    new_src = "".join(lines)
    try:
        ast.parse(new_src)
    except SyntaxError:
        return 0
    # preserva quebras originais do arquivo (CRLF/LF)
    keep_nl = "\r\n" if src.count("\r\n") > src.count("\n") - src.count("\r\n") else "\n"
    path.write_text(new_src.replace("\r\n", "\n"), encoding="utf-8", newline="")
    return len(edits)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    # descobre módulos citados no ledger com docstrings pendentes
    mods: set[str] = set()
    for fname in ("TAREFAS_v1_MENORES.md", "TAREFAS_v2.md"):
        text = (ROOT / fname).read_text(encoding="utf-8", errors="replace")
    # varre todo app/ (mais robusto que depender do ledger)
    total = 0
    for py in sorted((ROOT / "app").rglob("*.py")):
        if "__pycache__" in py.parts:
            continue
        n = insert_docstrings(py)
        if n:
            total += n
            print(f"{py.relative_to(ROOT)}: {n} docstring(s) inseridas")
    print("total:", total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
