"""Funções puras da rodada 34: comparação/preview/estudos (facilita testes)."""

from __future__ import annotations

import difflib
import re
from typing import Dict, List, Optional, Sequence, Tuple

TOKEN_RE_PURE = re.compile(r"\$((?:var|[vV])?\d+)\b")


# ---------- T5436: diff lado a lado (puro) ----------

def side_by_side_lines(
    text_a: str, text_b: str, width: int = 40
) -> List[Tuple[str, str, str]]:
    """Emparelha as linhas dos dois textos com marcador de divergência.

    Retorna [(marker, left, right)] onde marker ∈ {' ', '-', '+', '!'}:
    ' ' iguais, '-' só à esquerda, '+' só à direita, '!' diferentes.
    """
    a = str(text_a or "").splitlines()
    b = str(text_b or "").splitlines()
    matcher = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    rows: List[Tuple[str, str, str]] = []
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                rows.append((" ", a[i1 + k][:width], b[j1 + k][:width]))
        elif tag == "delete":
            for k in range(i1, i2):
                rows.append(("-", a[k][:width], ""))
        elif tag == "insert":
            for k in range(j1, j2):
                rows.append(("+", "", b[k][:width]))
        else:  # replace
            for k in range(max(i2 - i1, j2 - j1)):
                la = a[i1 + k] if i1 + k < i2 else ""
                lb = b[j1 + k] if j1 + k < j2 else ""
                rows.append(("!" if la != lb else " ", la[:width], lb[:width]))
    return rows


def format_side_by_side(
    text_a: str, text_b: str, width: int = 40,
    highlight: str = "»",
) -> str:
    """Renderiza colunas fixas; linhas divergentes com marca '>' na margem."""
    rows = side_by_side_lines(text_a, text_b, width)
    out: List[str] = []
    for marker, left, right in rows:
        mark = highlight if marker in {"-", "+", "!"} else " "
        out.append(
            f"{mark} {left.ljust(width)}| {right.ljust(width)}".rstrip()
        )
    return "\n".join(out)


def count_differences(text_a: str, text_b: str) -> int:
    """Número de linhas divergentes (visual: '-', '+', '!')."""
    return sum(
        1 for m, _, _ in side_by_side_lines(text_a, text_b) if m in {"-", "+", "!"}
    )


# ---------- T5437: múltiplas seeds em lote (puro) ----------

def multi_seed_values(
    render_fn, template: str, specs: Dict[int, object], seeds: Sequence[int]
) -> List[Tuple[int, str]]:
    """[(seed, texto renderizado)] na ordem pedida."""
    return [(seed, render_fn(template, specs, seed)) for seed in seeds]


def summarize_multi_seed(
    pairs: List[Tuple[int, str]]
) -> str:
    """Sumário textual; linhas divergentes entre seeds marcadas com '*'.
    Ignora seeds de diferença na célula de valores amostrados — compara texto."""
    if not pairs:
        return ""
    base_seed, base_text = pairs[0]
    lines = [f"seed {base_seed}: base"]
    for seed, text in pairs[1:]:
        n = count_differences(base_text, text)
        lines.append(f"seed {seed}: {n} linha(s) diferente(s) da base")
    return "\n".join(lines)


# ---------- T5439: diff textual com janela de contexto ajustável ----------

def unified_with_context(
    text_a: str, text_b: str, context: int = 3
) -> str:
    """unified_diff com n linhas de contexto (0 = só as mudanças)."""
    n = max(0, int(context))
    diff = difflib.unified_diff(
        str(text_a or "").splitlines(keepends=True),
        str(text_b or "").splitlines(keepends=True),
        n=n,
    )
    return "".join(diff)


def diff_changed_line_range(diff_text: str) -> Tuple[int, int]:
    """(primeira, última) linha alterada segundo os hunks; (-1,-1) se vazio."""
    first = last = -1
    line_a = 0
    for raw in str(diff_text or "").splitlines():
        m = re.match(r"@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@", raw)
        if m:
            start = int(m.group(3))
            count = int(m.group(4) or 1) if m.group(4) is not None else 1
            if count > 0:
                if first == -1:
                    first = start
                last = start + count - 1
    return first, last


# ---------- T5441: scatter por variável (matriz pura p/ plot) ----------

def scatter_points(
    values_a: Sequence[float], values_b: Sequence[float]
) -> Tuple[List[float], List[float], float]:
    """Pares (a, b) alinhados por índice + correlação de Pearson (0 se n<2)."""
    n = min(len(values_a), len(values_b))
    xs = [float(values_a[i]) for i in range(n)]
    ys = [float(values_b[i]) for i in range(n)]
    if n < 2:
        return xs, ys, 0.0
    mx = sum(xs) / n
    my = sum(ys) / n
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    vx = sum((x - mx) ** 2 for x in xs)
    vy = sum((y - my) ** 2 for y in ys)
    denom = (vx * vy) ** 0.5
    return xs, ys, (cov / denom if denom > 1e-300 else 0.0)


# ---------- T5442: ranking de variáveis divergentes entre batches ----------

def batch_divergence_ranking(
    stats: Sequence[dict], top: Optional[int] = None
) -> List[dict]:
    """Ordena stats de variáveis pela divergência relativa.

    stats: [{'var_id', 'mean_a', 'mean_b', 'std_a', 'std_b'}, ...]
    score = |mean_a - mean_b| / (|mean_a| + |mean_b|); std maior pesa um pouco.
    """
    def score(s: dict) -> float:
        ma = float(s.get("mean_a") or 0.0)
        mb = float(s.get("mean_b") or 0.0)
        base = abs(ma) + abs(mb)
        if base <= 1e-300:
            return -1.0
        rel = abs(ma - mb) / base
        pooled = ((float(s.get("std_a") or 0.0) ** 2 + float(s.get("std_b") or 0.0) ** 2) ** 0.5)
        penalty = pooled / base
        return rel + penalty * 0.1

    ranked = sorted(stats, key=score, reverse=True)
    return ranked[:top] if top is not None else ranked


def format_batch_ranking(ranked: Sequence[dict], width: int = 60) -> List[str]:
    """Linhas de texto do ranking (à esquerda a mais divergente)."""
    labels = [f"$var{s['var_id']}" if int(s["var_id"]) >= 10000 else f"${s['var_id']}" for s in ranked]
    scores: List[float] = []
    for s in ranked:
        ma, mb = float(s.get("mean_a") or 0.0), float(s.get("mean_b") or 0.0)
        base = abs(ma) + abs(mb) or 1.0
        scores.append(abs(ma - mb) / base)
    scale = max(scores) or 1.0
    lines = []
    for label, sc in zip(labels, scores):
        bar = "█" * max(0, int(round(20 * sc / scale)))
        lines.append(f"{label:<12} {sc:8.3%} {bar}")
    return lines[:width] if width else list(lines)
