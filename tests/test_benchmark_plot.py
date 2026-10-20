"""T5453: benchmark do render — regex compilada uma vez vs re-fetch a cada linha.

Roda rápido por padrão (20k linhas); benchmark grande fica opt-in via DAT_BENCH=1
(test_benchmark_1m.py). Verifica CORRETUDE igual e desempenho da pré-compilação.
"""

import os
import re
import time

import pytest

from app.core.parsing import TOKEN_RE

MAX_S = pytest.mark.skipif(
    os.environ.get("DAT_BENCH", "") != "1", reason="benchmark manual opt-in"
)

N_LINES = 20_000 if os.environ.get("DAT_BENCH", "") != "1" else 200_000
LINES = "PERMJ 101 $var{i} 320.2481 66.7978 -- token $1\n"


def _scan_recompiled(pattern: str, text: str):
    """Compile a cada chamada (caminho 'ingênuo')."""
    return [m.span() for m in re.finditer(pattern, text)]


def _scan_precompiled(pattern: re.Pattern, text: str):
    """Compile uma vez, reutilize (caminho do app)."""
    return [m.span() for m in pattern.finditer(text)]


@pytest.mark.parametrize("kind", ["correto", "benchmark"])
def test_benchmark_render_compiled_vs_regex(kind):
    template = "".join(LINES.format(i=i) for i in range(N_LINES))
    pattern_str = TOKEN_RE.pattern
    assert "(?P<prefix>" in pattern_str

    # correntude: mesmos spans
    spans_a = _scan_recompiled(pattern_str, template)
    spans_b = _scan_precompiled(TOKEN_RE, template)
    assert spans_a == spans_b
    assert len(spans_a) == 2 * N_LINES

    if kind == "correto":
        return

    t0 = time.perf_counter()
    _scan_recompiled(pattern_str, template)
    naive = time.perf_counter() - t0

    t0 = time.perf_counter()
    _scan_precompiled(TOKEN_RE, template)
    pre = time.perf_counter() - t0

    # benchmark anotado (register evidence): log os tempos
    print(f"[bench-render] naively-compiled={naive:.4f}s precompiled={pre:.4f}s n={N_LINES}")
    # pré-compilada não pode ser pior com margem de ruído (GC/OS)
    assert pre <= naive * 1.5, (naive, pre)
