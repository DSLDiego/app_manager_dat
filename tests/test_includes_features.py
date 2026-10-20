"""Testes do suporte a INCLUDE/*INCLUDE e navegação de variáveis."""

import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from pathlib import Path

import pytest
from PySide6.QtWidgets import QApplication

from app.container import Container
from app.core.includes import (
    clean_include_path,
    collect_includes,
    find_named_variables,
    include_summary,
    is_absolute_include,
    normalize_include_path,
    parse_include_paths,
    read_include,
    resolve_include_path,
    variables_by_source,
)
from app.ui.widgets.includes_dialog import (
    IncludesDialog,
    format_include_row,
    status_text,
    variables_text,
)


@pytest.fixture()
def qapp():
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    return app


# ---------- parsing de caminhos ----------

def test_parse_include_paths_variants():
    text = (
        "*TITLE\n"
        "INCLUDE 'includes/infos.inc'\n"
        '*include "C:\\dados\\infos2.inc" -- comentário\n'
        "  *INCLUDE   'outro.inc'  \n"
        "INCLUDED 'nao.inc'\n"
        "-- INCLUDE 'comentado.inc'\n"
    )
    entries = parse_include_paths(text)
    assert [e["raw"] for e in entries] == [
        "includes/infos.inc",
        "C:\\dados\\infos2.inc",
        "outro.inc",
    ]
    assert [e["line"] for e in entries] == [2, 3, 4]


def test_clean_include_path_quotes_and_comment():
    assert clean_include_path(" 'a/b.inc' -- x") == "a/b.inc"
    assert clean_include_path('"C:\\x\\y.inc"') == "C:\\x\\y.inc"
    assert clean_include_path("  ") == ""


def test_absolute_detection_windows_and_posix():
    assert is_absolute_include("C:\\dados\\x.inc")
    assert is_absolute_include("c:/dados/x.inc")
    assert is_absolute_include("\\\\servidor\\share\\x.inc")
    assert is_absolute_include("/home/user/x.inc")
    assert not is_absolute_include("includes/x.inc")
    assert not is_absolute_include("./x.inc")


def test_normalize_mixed_separators():
    raw = "includes\\sub/infos.inc"
    normalized = normalize_include_path(raw)
    if os.sep == "\\":
        assert normalized == "includes\\sub\\infos.inc"
    else:
        assert normalized == "includes/sub/infos.inc"


def test_resolve_relative_and_absolute(tmp_path):
    assert resolve_include_path("includes/x.inc", tmp_path) == Path(
        tmp_path
    ) / "includes" / "x.inc"
    abs_posix = "/tmp/abs.inc"
    assert resolve_include_path(abs_posix, tmp_path) == Path(abs_posix)


def test_read_include_missing_returns_none(tmp_path):
    assert read_include("nao_existe.inc", tmp_path) is None


def test_find_named_variables_excludes_numeric():
    text = "$1 $var2 $V3 $nome $idade2 $cpf"
    assert find_named_variables(text) == ["cpf", "idade2", "nome"]


# ---------- coleta recursiva ----------

def test_collect_includes_recursive_and_variables(tmp_path):
    inc = tmp_path / "includes"
    inc.mkdir()
    (inc / "a.inc").write_text("valor $1\nINCLUDE 'b.inc'\n", encoding="utf-8")
    (inc / "b.inc").write_text("nome: $nome\noutro $var2\n", encoding="utf-8")
    text = "*TITLE\nINCLUDE 'includes/a.inc'\n"

    entries = collect_includes(text, tmp_path)
    assert len(entries) == 2
    a, b = entries
    assert a["exists"] and a["depth"] == 1
    assert a["variables"] == [1]
    assert a["named_variables"] == []
    assert b["depth"] == 2
    assert b["parent"] == "includes/a.inc"
    assert b["variables"] == [10002]
    assert b["named_variables"] == ["nome"]
    assert include_summary(entries).startswith("2 INCLUDE(s): 2 ok")


def test_collect_includes_missing_and_cycle(tmp_path):
    (tmp_path / "a.inc").write_text("INCLUDE 'b.inc'\n", encoding="utf-8")
    (tmp_path / "b.inc").write_text("INCLUDE 'a.inc'\n", encoding="utf-8")
    text = "INCLUDE 'a.inc'\nINCLUDE 'sumiu.inc'\n"

    entries = collect_includes(text, tmp_path)
    by_raw = {e["raw"]: e for e in entries}
    assert by_raw["sumiu.inc"]["exists"] is False
    assert "não encontrado" in by_raw["sumiu.inc"]["error"]
    assert any(e["cycle"] for e in entries)


def test_collect_includes_max_depth(tmp_path):
    (tmp_path / "a.inc").write_text("INCLUDE 'b.inc'\n", encoding="utf-8")
    (tmp_path / "b.inc").write_text("INCLUDE 'c.inc'\n", encoding="utf-8")
    entries = collect_includes("INCLUDE 'a.inc'\n", tmp_path, max_depth=1)
    assert any(
        e["error"] == "profundidade máxima excedida" for e in entries
    )


def test_variables_by_source(tmp_path):
    (tmp_path / "a.inc").write_text("$1 $2\n", encoding="utf-8")
    text = "$3\nINCLUDE 'a.inc'\n"
    mapping = variables_by_source(text, tmp_path)
    assert mapping["(template)"] == [3]
    assert mapping[str(tmp_path / "a.inc")] == [1, 2]


# ---------- dialog ----------

def test_format_include_row_and_status(tmp_path):
    (tmp_path / "a.inc").write_text("$5 $nome\n", encoding="utf-8")
    entry = collect_includes("INCLUDE 'a.inc'\n", tmp_path)[0]
    row = format_include_row(entry)
    assert row[0] == "a.inc"
    assert row[2] == "ok"
    assert row[3] == "1"
    assert "$5" in row[4] and "$nome" in row[4]
    assert status_text({"exists": False}) == "ausente"
    assert variables_text({"variables": [], "named_variables": []}) == "—"


def test_includes_dialog_lists_and_previews(qapp, tmp_path):
    (tmp_path / "a.inc").write_text("conteudo $7\n", encoding="utf-8")
    entries = collect_includes("INCLUDE 'a.inc'\n", tmp_path)
    dialog = IncludesDialog(entries)
    assert dialog.table.rowCount() == 1
    assert "a.inc" in dialog.table.item(0, 0).text()
    assert "conteudo $7" in dialog.selected_content()
    dialog.close()


def test_mainwindow_includes_action(qapp, tmp_path, monkeypatch):
    from app.ui.widgets.includes_dialog import IncludesDialog as Dlg

    inc = tmp_path / "includes"
    inc.mkdir()
    (inc / "infos.inc").write_text("idade: $idade\n", encoding="utf-8")

    from app.ui.main_window import MainWindow

    window = MainWindow(Container(base_dir=str(tmp_path / "cinc"), load_plugins=False))
    editor = window.editor_tabs.current_editor()
    editor.file_path = str(tmp_path / "t.dat")
    editor.editor.setPlainText("INCLUDE 'includes/infos.inc'\n")
    monkeypatch.setattr(Dlg, "exec", lambda self: 0)
    entries = window._open_includes_dialog()
    assert len(entries) == 1
    assert entries[0]["exists"] is True
    assert entries[0]["named_variables"] == ["idade"]
    assert window._last_includes == entries
    window.close()