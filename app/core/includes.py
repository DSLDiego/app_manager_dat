"""Leitura e navegação de arquivos INCLUDE de templates CMG (.dat).

Sintaxe aceita (case-insensitive, com ou sem `*`):

    INCLUDE 'includes/infos.inc'
    *INCLUDE "C:\\dados\\infos2.inc"

Caminhos relativos são resolvidos a partir do diretório do template;
caminhos absolutos (POSIX, Windows `C:\\...` ou UNC `\\\\servidor\\...`)
são usados como estão. Ambos os separadores são aceitos em qualquer SO.
Este módulo é puro (sem Qt/SQL).
"""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Optional

from app.core.parsing import find_variables

INCLUDE_RE = re.compile(
    r"^[ \t]*\*?INCLUDE\b[ \t]+(?P<path>[^\r\n]+?)[ \t]*(?:--.*)?$",
    re.IGNORECASE | re.MULTILINE,
)

NAMED_TOKEN_RE = re.compile(
    r"\$(?!(?:var|[vV])\d)(?P<name>[A-Za-z_][A-Za-z0-9_]*)", re.IGNORECASE
)

_WINDOWS_ABS_RE = re.compile(r"^(?:[A-Za-z]:[\\/]|\\\\)")


def clean_include_path(raw: str) -> str:
    """Remove espaços, comentário final e aspas simples/duplas do caminho."""
    text = str(raw or "").strip()
    text = text.split("--", 1)[0].strip()
    if len(text) >= 2 and text[0] == text[-1] and text[0] in "\"'":
        text = text[1:-1]
    return text.strip()


def is_absolute_include(raw: str) -> bool:
    """Absoluto POSIX (`/...`), Windows (`C:\\...`) ou UNC (`\\\\...`)."""
    text = clean_include_path(raw)
    if not text:
        return False
    return text.startswith("/") or bool(_WINDOWS_ABS_RE.match(text))


def normalize_include_path(raw: str) -> str:
    """Normaliza separadores para o SO atual (aceita `\\` e `/`)."""
    text = clean_include_path(raw)
    if not text:
        return ""
    if os.sep == "/":
        return text.replace("\\", "/")
    return text.replace("/", "\\")


def resolve_include_path(raw: str, base_dir) -> Path:
    """Resolve o caminho do INCLUDE contra `base_dir` quando relativo."""
    text = normalize_include_path(raw)
    if not text:
        return Path("")
    path = Path(text)
    if is_absolute_include(raw) or path.is_absolute():
        return path
    return Path(base_dir) / path


def read_include(raw: str, base_dir, encoding: str = "utf-8") -> Optional[str]:
    """Lê o arquivo incluído; None se não existir/ilegível."""
    path = resolve_include_path(raw, base_dir)
    try:
        return path.read_text(encoding=encoding, errors="replace")
    except (OSError, ValueError):
        return None


def parse_include_paths(text: str) -> list[dict]:
    """[{line, raw}] de todas as linhas INCLUDE/*INCLUDE do texto."""
    entries = []
    for match in INCLUDE_RE.finditer(str(text or "")):
        raw = clean_include_path(match.group("path"))
        if not raw:
            continue
        line = str(text).count("\n", 0, match.start()) + 1
        entries.append({"line": line, "raw": raw})
    return entries


def find_named_variables(text: str) -> list[str]:
    """Tokens nomeados (`$nome`) — fora do padrão numérico `$N`/`$varN`."""
    names = {m.group("name") for m in NAMED_TOKEN_RE.finditer(str(text or ""))}
    return sorted(names)


def collect_includes(
    text: str,
    base_dir,
    max_depth: int = 10,
    encoding: str = "utf-8",
) -> list[dict]:
    """Árvore (DFS) de INCLUDEs: status, profundidade, texto e variáveis.

    Cada entrada:
      {raw, line, path, resolved, exists, depth, parent, cycle, error,
       text, variables, named_variables}
    Ciclos e arquivos ausentes não interrompem a coleta.
    """
    base = Path(base_dir)
    results: list[dict] = []
    seen: set[str] = set()

    def _walk(source_text: str, source_dir: Path, depth: int, parent):
        """Função `_walk`.
            Parâmetros: `source_text`, `source_dir`, `depth`, `parent`."""
        if depth > max_depth:
            results.append({
                "raw": "", "line": None, "path": Path(""), "resolved": "",
                "exists": False, "depth": depth, "parent": parent,
                "cycle": False, "error": "profundidade máxima excedida",
                "text": None, "variables": [], "named_variables": [],
            })
            return
        for item in parse_include_paths(source_text):
            resolved = resolve_include_path(item["raw"], source_dir)
            key = str(resolved).lower() if os.name == "nt" else str(resolved)
            entry = {
                "raw": item["raw"],
                "line": item["line"],
                "path": resolved,
                "resolved": str(resolved),
                "exists": resolved.exists(),
                "depth": depth,
                "parent": parent,
                "cycle": key in seen,
                "error": None,
                "text": None,
                "variables": [],
                "named_variables": [],
            }
            if entry["cycle"]:
                entry["error"] = "ciclo de INCLUDE detectado"
                results.append(entry)
                continue
            if not entry["exists"]:
                entry["error"] = "arquivo não encontrado"
                results.append(entry)
                continue
            try:
                content = resolved.read_text(encoding=encoding, errors="replace")
            except (OSError, ValueError) as exc:
                entry["exists"] = False
                entry["error"] = f"ilegível: {exc}"
                results.append(entry)
                continue
            seen.add(key)
            entry["text"] = content
            entry["variables"] = find_variables(content)
            entry["named_variables"] = find_named_variables(content)
            results.append(entry)
            _walk(content, resolved.parent, depth + 1, item["raw"])

    _walk(str(text or ""), base, 1, None)
    return results


def variables_by_source(text: str, base_dir) -> dict[str, list[int]]:
    """Mapa 'fonte' → variáveis numéricas ($N/$varN) encontradas."""
    mapping: dict[str, list[int]] = {"(template)": find_variables(str(text or ""))}
    for entry in collect_includes(text, base_dir):
        if entry["text"] is None:
            continue
        label = entry["resolved"]
        values = mapping.setdefault(label, [])
        for var_id in entry["variables"]:
            if var_id not in values:
                values.append(var_id)
    for values in mapping.values():
        values.sort()
    return {k: v for k, v in mapping.items() if v}


def include_summary(entries: list[dict]) -> str:
    """Resumo textual da coleta (usado pela GUI e por testes)."""
    if not entries:
        return "Nenhum INCLUDE encontrado no template."
    ok = sum(1 for e in entries if e.get("exists") and not e.get("cycle"))
    problems = len(entries) - ok
    return f"{len(entries)} INCLUDE(s): {ok} ok, {problems} com problema."
