"""Regressão da rodada 26: higiene de código e auditoria por arquivo.

Cobre T5127 (sem self.list), T5128 (sem __import__) e T5117 (audit.csv).
"""

import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import ast as _ast
from pathlib import Path

import pytest
from PySide6.QtWidgets import QApplication


@pytest.fixture(scope="module")
def qapp():
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    return app


@pytest.fixture()
def exp_container(tmp_path):
    from app.container import Container

    return Container(base_dir=str(tmp_path / "c26"), load_plugins=False)


# ---------- T5128: nenhum hack __import__ no app/ ----------

def test_no_dynamic_import_hacks_in_app():
    offenders = []
    for path in Path("app").rglob("*.py"):
        source = path.read_text(encoding="utf-8")
        if "__import__" in source:
            offenders.append(str(path))
    assert offenders == []


def test_preview_panel_uses_real_qfont(qapp):
    from PySide6.QtGui import QFont

    from app.ui.widgets.preview_panel import PreviewPanel

    panel = PreviewPanel()
    assert panel.output.font().family() == QFont("Consolas").family()
    assert panel.output.font().family() == "Consolas"
    panel.close()


def test_distribution_plot_safe_names_math(qapp):
    from app.ui.widgets.distribution_plot_dialog import _SAFE_NAMES

    assert _SAFE_NAMES["math"] is __import__("math")
    assert _SAFE_NAMES["np"].pi == _SAFE_NAMES["pi"]


def test_export_done_dialog_text_selectable(qapp, tmp_path):
    from PySide6.QtCore import Qt

    from app.ui.widgets.export_done_dialog import ExportDoneDialog

    dlg = ExportDoneDialog(tmp_path / "out", 3, None)
    labels = [c for c in dlg.children() if c.metaObject().className().endswith("QLabel")]
    rich = [l for l in labels if l.text().startswith("<b>") or "Pasta" in l.text()]
    assert rich
    assert all(
        l.textInteractionFlags() & Qt.TextInteractionFlag.TextSelectableByMouse
        for l in rich
    )
    dlg.close()


# ---------- T5127: variables_panel sem colisão com builtin ----------

def test_variables_panel_uses_var_map(exp_container, qapp):
    wrapper = VariablesPanelForTest(exp_container)
    assert not hasattr(wrapper, "list")  # renomeado
    assert hasattr(wrapper, "var_map")
    import ast as _ast2

    source = Path("app/ui/widgets/variables_panel.py").read_text(encoding="utf-8")
    tree = _ast2.parse(source)
    broken = [
        n.targets[0].attr
        for n in _ast2.walk(tree)
        if isinstance(n, _ast2.Assign)
        and isinstance(n.targets[0], _ast2.Attribute)
        and n.targets[0].attr == "list"
        and getattr(n.targets[0].value, "id", "") == "self"
    ]
    assert broken == []


class VariablesPanelForTest:
    """Camada mínima: instância real através da janela é cara; aqui UIPanel pura."""

    def __init__(self, container):
        from app.infrastructure.distribution_registry import build_default_registry

        from app.ui.widgets.variables_panel import VariablesPanel

        self.panel = VariablesPanel(build_default_registry())

    def __getattr__(self, name):
        return getattr(self.panel, name)


def test_variables_panel_update_tokens_returns_var_map(exp_container, qapp):
    wrapper = VariablesPanelForTest(exp_container)
    result = wrapper.update_tokens("$1 = 0\n$var2")
    assert sorted(result) == [1, 10002]
    assert wrapper.specs == {}
    assert wrapper.missing_count() == 2


# ---------- T5117: auditoria por arquivo no export ----------

def _svc(container):
    from app.services.batch_export_service import BatchExportService

    return BatchExportService(
        container.exp_repo, container.template_repo,
        renderer=lambda tid, vals: f"T {vals[1]:.0f}",
    )


def _populate(container):
    container.exp_repo.create_batch("b26", method="sampling", seed=42, n_experiments=2)
    container.exp_repo.insert_result("b26", [1], [[10.0], [20.0]])


def test_export_writes_audit_csv(exp_container, tmp_path):
    _populate(exp_container)
    tpl = exp_container.template_repo.create_template("t")
    vid = exp_container.template_repo.save_version(tpl, "T $1", comment="v1")
    out = tmp_path / "out26_audit"
    manifest = _svc(exp_container).export("b26", vid, out)
    audit_path = Path(manifest.output_dir) / "audit.csv"
    assert audit_path.exists()
    lines = audit_path.read_text(encoding="utf-8").strip().splitlines()
    assert lines[0] == "external_id,file,written_at,action"
    assert len(lines) == 3  # header + 2 experimentos
    assert "experimento_000001.dat" in lines[1]
    assert "created" in lines[1]
    # segunda exportação por cima (overwrite default) → "overwritten"
    manifest2 = _svc(exp_container).export("b26", vid, out)
    lines2 = (Path(manifest2.output_dir) / "audit.csv").read_text(encoding="utf-8").strip().splitlines()
    assert "overwritten" in lines2[1]


def test_export_audit_can_be_disabled(exp_container, tmp_path):
    _populate(exp_container)
    tpl = exp_container.template_repo.create_template("t")
    vid = exp_container.template_repo.save_version(tpl, "T $1", comment="v1")
    out = tmp_path / "out26_noaudit"
    manifest = _svc(exp_container).export("b26", vid, out, audit_log=False)
    assert not (Path(manifest.output_dir) / "audit.csv").exists()
    # manifest.csv continua presente
    assert (Path(manifest.output_dir) / "manifest.csv").exists()
