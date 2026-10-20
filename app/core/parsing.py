"""Parsing e renderização de templates .dat.

Tokens e namespaces:
- `$1`  → variável 1 (id 1)
- `$var1` / `$v1` / `$V1` → variável 10001 (id 10000+1)

`$1` e `$var1` são variáveis aleatórias DIFERENTES, cada uma associada à
sua própria distribuição de parâmetros.
"""

from __future__ import annotations

import re
from typing import Mapping

TOKEN_RE = re.compile(r"\$(?P<prefix>(?:var|[vV]))?(?P<num>\d+)(?!\d)", re.IGNORECASE)

VAR_PREFIX_OFFSET = 10_000


def token_var_id(match: re.Match) -> int:
    """Extrai o id único (namespace) de um match de token."""
    prefix = match.group("prefix")
    return int(match.group("num")) + (VAR_PREFIX_OFFSET if prefix is not None else 0)


def var_label(var_id: int) -> str:
    """Representação textual canônica do token para o id informado."""
    if var_id >= VAR_PREFIX_OFFSET:
        return f"$var{var_id - VAR_PREFIX_OFFSET}"
    return f"${var_id}"


def find_variables(text: str) -> list[int]:
    """IDs ordenados de todas as variáveis em uso no texto."""
    return sorted({token_var_id(m) for m in TOKEN_RE.finditer(text)})


def vars_status_text(text: str) -> str:
    """Resumo curto p/ barra de status: "3 vars ($:2 · $var:1)" — puro."""
    ids = find_variables(text)
    n_pos = sum(1 for i in ids if i < VAR_PREFIX_OFFSET)
    n_ns = len(ids) - n_pos
    return f"{len(ids)} vars ($:{n_pos} · $var:{n_ns})"


def format_value(value) -> str:
    """Formata o valor para arquivo técnico: ponto decimal, sem milhar."""
    if isinstance(value, bool):
        return str(int(value))
    if isinstance(value, float):
        if value != value or value in (float("inf"), float("-inf")):
            raise ValueError(
                f"Valor inválido para arquivo .dat: {value!r} (nan/inf não permitido)"
            )
        return f"{value:.10g}"
    if isinstance(value, int):
        return str(value)
    return str(value)


def render_template(text: str, values: Mapping[int, float]) -> str:
    """Substitui os tokens $N/$varN pelos valores fornecidos.

    Levanta ValueError se alguma variável usada no template não tiver valor.
    """

    usados = {token_var_id(m) for m in TOKEN_RE.finditer(text)}
    faltantes = sorted(usados - set(values.keys()))
    if faltantes:
        descricao = ", ".join(var_label(n) for n in faltantes)
        raise ValueError(f"Variáveis sem valor definido: {descricao}")

    def substituir(m: re.Match) -> str:
        """Função `substituir`.
            Parâmetros: `m`.
            Retorna o resultado calculado a partir do estado local."""
        return format_value(values[token_var_id(m)])

    return TOKEN_RE.sub(substituir, text)


class TemplateCompiler:
    """Regex uma única vez; render subsequente sem repetir tokenizing.

    Para 1M experimentos: o custo de `TOKEN_RE.finditer` + construção do
    `usados` é pago UMA vez no compile(), e o render vira join de segmentos.
    """

    __slots__ = ("segments", "var_ids", "_source", "_labels_cache")

    def __init__(self, text: str):
        """Método `TemplateCompiler.__init__`.
            Parâmetros: `self`, `text`."""
        self._source = text
        segments: list = []  # [(var_id ou None, literal), ...]
        labels: dict[int, str] = {}
        cursor = 0
        used: set[int] = set()
        for m in TOKEN_RE.finditer(text):
            var_id = token_var_id(m)
            used.add(var_id)
            if m.start() > cursor:
                segments.append((None, text[cursor : m.start()]))
            segments.append((var_id, m.group(0)))
            labels[var_id] = m.group(0)
            cursor = m.end()
        if cursor < len(text):
            segments.append((None, text[cursor:]))
        self.segments = tuple(segments)
        self.var_ids: tuple[int, ...] = tuple(sorted(used))
        self._labels_cache = labels

    def render(self, values: Mapping[int, float]) -> str:
        """Método `TemplateCompiler.render`.
            Parâmetros: `self`, `values`.
            Retorna o resultado calculado a partir do estado local.
            Levanta: ValueError."""
        faltantes = [v for v in self.var_ids if v not in values]
        if faltantes:
            descricao = ", ".join(var_label(n) for n in faltantes)
            raise ValueError(f"Variáveis sem valor definido: {descricao}")
        parts: list[str] = []
        for var_id, literal in self.segments:
            if var_id is None:
                parts.append(literal)
            else:
                parts.append(format_value(values[var_id]))
        return "".join(parts)

    def source(self) -> str:
        """Método `TemplateCompiler.source`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        return self._source


def compile_template(text: str) -> TemplateCompiler:
    """Função `compile_template`.
        Parâmetros: `text`.
        Retorna o resultado calculado a partir do estado local."""
    return TemplateCompiler(text)


# ---------- R31: validação heurística de template CMG ----------
CMG_KNOWN_SECTIONS = {
    "*TITLE", "*GRID", "*ROCK", "*FLUID", "*COMPONENTS", "*RECURRENT",
    "*NUMERICAL", "*WELL", "*SCHEDULE", "*TIME", "*RESULTS", "*RUN",
    "*STOP", "*POROSITY", "*PERMEABILITY", "*MODEL", "*GENERAL",
    "*REFINE", "*CORNER", "*DYNAMICS", "*OUTPUT", "*PRESSURE",
}

INVALID_TOKEN_RE = re.compile(r"\$[A-Za-z_][A-Za-z_]*")


def template_sections(text: str) -> list[str]:
    """Seções CMG (`*KEYWORD` no começo da linha, fora de comentários `--`)."""
    sections: list[str] = []
    for raw in str(text).splitlines():
        line = raw.split("--", 1)[0].strip()
        if line.startswith("*") and not line.startswith("**"):
            keyword = line.split()[0].upper()
            sections.append(keyword)
    return sections


def validate_template(text: str) -> list[dict]:
    """Heurística de sanidade para templates CMG (.dat).

    Retorna lista de achados `{severity, message, line?}`; vazia = ok.
    Não substitui o parser do simulador — só evita erros óbvios.
    """
    issues: list[dict] = []
    source = str(text or "")
    if not source.strip():
        issues.append({"severity": "error", "message": "Template vazio."})
        return issues

    sections = template_sections(source)
    if not sections:
        issues.append({
            "severity": "warning",
            "message": "Nenhuma seção CMG (*TITLE, *GRID, ...) encontrada.",
        })
    else:
        if "*TITLE" not in sections:
            issues.append({
                "severity": "warning",
                "message": "Seção *TITLE ausente (recomendada em todo .dat CMG).",
            })
        unknown = sorted({s for s in sections if s not in CMG_KNOWN_SECTIONS})
        for keyword in unknown:
            issues.append({
                "severity": "warning",
                "message": f"Seção desconhecida: {keyword}.",
            })

    for m in INVALID_TOKEN_RE.finditer(source):
        line = source.count("\n", 0, m.start()) + 1
        issues.append({
            "severity": "error",
            "message": f"Token inválido '{m.group(0)}' (use $N ou $varN).",
            "line": line,
        })

    if "$" in source and not find_variables(source):
        issues.append({
            "severity": "warning",
            "message": "Símbolo '$' presente, mas nenhum token $N/$varN válido.",
        })
    return issues


def validation_summary(issues: list[dict]) -> str:
    """Resumo textual de validate_template — puro, usado pela GUI/testes."""
    if not issues:
        return "Template válido (nenhum problema encontrado)."
    errors = sum(1 for i in issues if i.get("severity") == "error")
    warnings = len(issues) - errors
    head = f"{errors} erro(s) e {warnings} aviso(s):"
    lines = [
        f"linha {i['line']}: {i['message']}" if i.get("line") else i["message"]
        for i in issues[:20]
    ]
    return "\n".join([head, *lines])
