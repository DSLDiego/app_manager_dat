"""Testes r33: autosave .bak, i18n, trayhelper, versions.txt, spec PyInstaller, manual PDF."""

import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from pathlib import Path

import pytest
from PySide6.QtWidgets import QApplication

# ---------- T5433: auto-save .bak ----------


@pytest.fixture()
def qapp():
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    return app


def test_write_backup_creates_bak(tmp_path):
    from app.ui.editor.editor_tabs import backup_name, write_backup

    file = tmp_path / "t.dat"
    file.write_text("X $1", encoding="utf-8")
    target = write_backup(str(file), "conteudo $2")
    assert target == backup_name(str(file))
    assert Path(target).read_text(encoding="utf-8") == "conteudo $2"
    assert write_backup("", "x") == ""


def test_autosave_backups_writes_for_open_tabs(qapp, tmp_path):
    from app.ui.editor.editor_tabs import EditorTabs

    file = tmp_path / "a.dat"
    file.write_text("original $1\n", encoding="utf-8")
    tabs = EditorTabs()
    tab = tabs.open_file(str(file))
    tab.editor.setPlainText("editado $2\n")
    n = tabs.autosave_backups()
    assert n >= 1
    assert (tmp_path / "a.dat.bak").read_text(encoding="utf-8") == "editado $2\n"
    tabs.close()


# ---------- T5447: i18n ----------


def test_i18n_translate_and_passthrough():
    from app.ui.i18n import PT2EN, LANGS, has_translation, translate

    assert translate("Abrir", "en") == "Open"
    assert translate("Não tenho tradução", "en") == "Não tenho tradução"
    assert has_translation("Abrir", "en")
    assert not has_translation("Abrir", "es")
    # a tabela EN→PT cobrir o inverso em LANGS
    assert LANGS == ("pt-BR", "en")
    assert PT2EN["Exportar"] == "Export"


# ---------- T5446: tray helper ----------


def test_notify_tray_is_safe_offscreen(qapp, tmp_path):
    from app.container import Container
    from app.ui.main_window import MainWindow

    window = MainWindow(Container(base_dir=str(tmp_path / "tray"), load_plugins=False))
    # não deve levantar mesmo sem tray (offscreen/CI)
    window._notify_tray("DAT Engineering Studio", "mensagem de teste")
    window.close()


# ---------- T5450: versions.txt ----------


def test_analyze_versions_report(tmp_path, monkeypatch):
    import tools.analyze_versions as av

    monkeypatch.setattr(av, "REQ", Path(__file__).parent / "data_requires_none.txt")
    av.REQ.write_text("PySide6>=6.6\n# comentario\nnumpy>=1.26\n", encoding="utf-8")
    monkeypatch.setattr(av, "REQ", Path(__file__).parent / "data_requires_none.txt")
    pairs = []
    for line in av.REQ.read_text(encoding="utf-8").splitlines():
        p = av.parse_requirement(line)
        if p:
            pairs.append((p, av.version_of(p)))
    report = av.build_report(pairs)
    assert "pyside6==" in report.lower()
    assert "numpy==" in report.lower()
    assert "comentario" not in report


def test_analyze_versions_cli(tmp_path, monkeypatch):
    import subprocess, sys

    proc = subprocess.run(
        [sys.executable, "tools/analyze_versions.py", "--json"],
        capture_output=True, text=True, cwd=str(Path(__file__).parents[1]),
    )
    assert proc.returncode == 0
    assert '"pyside6"' in proc.stdout.lower()


# ---------- T5448/T5449: spec PyInstaller ----------


def test_pyinstaller_spec_structure():
    spec = (Path(__file__).parents[1] / "app" / "packaging" / "pyinstaller.spec")
    text = spec.read_text(encoding="utf-8")
    for tok in ("Analysis(", "COLLECT(", "onedir", "icon=", "version=", "hiddenimports"):
        assert tok in text, tok


# ---------- T5451: manual PDF ----------


def test_make_manual_pdf(tmp_path):
    from tools.make_manual_pdf import render_pdf

    out = tmp_path / "manual.pdf"
    pages = render_pdf(out)
    assert pages >= 1
    assert out.exists() and out.stat().st_size > 5000


# ---------- T5453: benchmark render compilado ----------


def test_benchmark_plot_quick():
    from tests.test_benchmark_plot import LINES, _scan_precompiled, _scan_recompiled
    from app.core.parsing import TOKEN_RE

    template = "".join(LINES.format(i=i) for i in range(2_000))
    assert _scan_recompiled(TOKEN_RE.pattern, template) == _scan_precompiled(TOKEN_RE, template)
    assert len(_scan_precompiled(TOKEN_RE, template)) == 4_000
