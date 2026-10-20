"""Testes do parser de tokens e renderização de templates."""

import pytest

from app.core.parsing import TOKEN_RE, find_variables, render_template, var_label


TEMPLATE = """*TITLE
RUNTEST $1
PERMZ $V2/$var3
-- comentario com $1
PATH 'out_$4.dat'
"""


def test_variation_forms_detected():
    # sorted ids: [1, 4, 10002, 10003]
    var_ids = find_variables(TEMPLATE)
    assert var_ids == [1, 4, 10002, 10003]


def test_dollar_and_var_are_distinct_variables():
    assert find_variables("X $1 e $var1") == [1, 10001]
    assert find_variables("X $1 e $V1 e $v1") == [1, 10001]


def test_token_regex_does_not_match_prefix():
    m = TOKEN_RE.search("$var10")
    assert m.group("num") == "10"
    d = TOKEN_RE.search("$1")
    assert d.group("prefix") is None and d.group("num") == "1"


def test_token_match_dollar_number():
    text = "X=$7"
    m = TOKEN_RE.search(text)
    assert m.group("num") == "7"


def test_render_template_substitutes_values():
    text = "RANZ $V1 $var2 $3"
    out = render_template(text, {10001: 0.5, 10002: 12.0, 3: 7})
    assert "0.5" in out
    assert "12" in out
    assert "7" in out
    assert "$" not in out


def test_render_template_missing_raises():
    with pytest.raises(ValueError) as exc:
        render_template("$1 $var2", {1: 1.0})
    assert "$var2" in str(exc.value)


def test_render_template_namespaced_values():
    out = render_template("A: $1 B: $var1", {1: 2.5, 10001: 9.0})
    assert "2.5" in out and "9" in out
    assert "$" not in out


def test_var_label_roundtrip():
    assert var_label(1) == "$1"
    assert var_label(10001) == "$var1"
    assert var_label(10002) == "$var2"


def test_render_without_variables_unchanged():
    text = "*DATES 01 'JAN' 2024\n-- nada aqui"
    assert render_template(text, {}) == text
