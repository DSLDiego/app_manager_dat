"""Analisa dependências instaladas vs requirements.txt e escreve versions.txt.

Uso:
    python tools/analyze_versions.py            # escreve output/versions.txt
    python tools/analyze_versions.py --json     # imprime JSON no stdout
"""

from __future__ import annotations

import argparse
import importlib.metadata
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQ = ROOT / "requirements.txt"
OUT = ROOT / "output" / "versions.txt"


def parse_requirement(line: str) -> str:
    """Nome do pacote a partir de uma linha de requirements ('pkg>=1'...)."""
    name = str(line or "").strip()
    if not name or name.startswith("#"):
        return ""
    for sep in ("=", ">", "<", "[", ";"):
        if sep in name:
            name = name.split(sep)[0]
    return name.strip().lower()


def version_of(package: str) -> str:
    """Versão instalada; 'NÃO INSTALADO' quando ausente."""
    try:
        return importlib.metadata.version(package)
    except importlib.metadata.PackageNotFoundError:
        return "NÃO INSTALADO"


def build_report(pairs: list[tuple[str, str]]) -> str:
    """Relatório em texto estável (ordenado) — puro, usado por testes."""
    lines = ["# versions.txt — versões instaladas do ambiente", ""]
    for pkg, ver in sorted(pairs):
        lines.append(f"{pkg}=={ver}")
    return "\n".join(lines) + "\n"


def main(argv=None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)

    lines = [parse_requirement(l) for l in REQ.read_text(encoding="utf-8").splitlines()]
    pkgs = [p for p in lines if p]
    report = [(p, version_of(p)) for p in pkgs]

    if args.json:
        print(json.dumps({k: v for k, v in report}, indent=2))
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(build_report(report), encoding="utf-8")
    print(f"relatório gravado em {OUT.relative_to(ROOT)} ({len(report)} pacotes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
