"""Gera diretivo docs/manual_rapido.pdf (T5451) a partir de docs/*.md.

Usa apenas matplotlib (PdfPages) já presente em requirements.txt.
Rodar:  python tools/make_manual_pdf.py
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "manual_rapido.pdf"
SOURCES = [
    ROOT / "docs" / "ARCHITECTURE.md",
    ROOT / "main.dat",
]

SECTIONS = [
    (
        "DAT Engineering Studio — Manual Rápido",
        "GUI: python main.py (ou main.bat)\n"
        "Testes: python -m pytest tests -q (QT_QPA_PLATFORM=offscreen)\n"
        "Exemplo: main.bat → opção 7",
    ),
    (
        "Templates .dat e variáveis",
        "*INCLUDE 'includes/x.inc'  — inclui arquivo (cam. Windows/Linux)\n"
        "Tokens: $1  $var1  $V1   ($1 e $var1 são variáveis independentes)\n"
        "$nome — token nomeado (fora da numeração $N/$varN)",
    ),
    (
        "Amostragem",
        "Estratégias: monte_carlo, lhs, sobol, halton (+ correlação Iman-Conover)\n"
        "Seeds determinísticas; cache no Container p/ re-render rápido.",
    ),
    (
        "Export em lote",
        "Serviço paginado O(página) com checkpoint e cancelamento cooperativo;\n"
        "máscara de nome de arquivo, política overwrite/rename/skip e audit.",
    ),
    (
        "Arquitetura",
        "UI (PySide6) → workers (QThread) → services puros → infra (SQLite,\n"
        "EventBus, plugins de distribuição). Nada fala com scipy/sql da UI.",
    ),
]


def render_pdf(path: Path) -> int:
    """Renders as páginas do manual (matplotlib PdfPages). Retorna nº de páginas."""
    from matplotlib.backends.backend_pdf import PdfPages
    from matplotlib.figure import Figure

    pages = 0
    with PdfPages(str(path)) as pdf:
        for title, body in SECTIONS:
            fig = Figure(figsize=(8.27, 11.69), dpi=100)
            ax = fig.add_axes([0.1, 0.05, 0.85, 0.88])
            ax.axis("off")
            ax.text(0.02, 0.96, title, fontsize=17, weight="bold", va="top")
            ax.text(0.02, 0.88, body, fontsize=11.5, va="top", family="monospace",
                    linespacing=1.7)
            pdf.savefig(fig)
            pages += 1
    return pages


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pages = render_pdf(OUT)
    print(f"manual gerado: {OUT.relative_to(ROOT)} ({pages} páginas)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
