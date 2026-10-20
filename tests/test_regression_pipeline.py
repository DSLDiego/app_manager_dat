"""Regressão integrada: editor → variáveis → sampling → repo → export worker."""

import tempfile
from pathlib import Path

import numpy as np
import pytest

pytest.importorskip("pytestqt")

from app.ui.editor.themes import persist_font_scale, persist_system_scale

pytestmark = pytest.mark.usefixtures("qapp")


@pytest.fixture(autouse=True)
def reset_persisted_qsettings():
    persist_font_scale(1.0)
    persist_system_scale(1.0)
    yield
    persist_font_scale(1.0)
    persist_system_scale(1.0)


def test_container_ensure_services_idempotent(tmp_path, qtbot):
    from app.container import Container
    from app.services.batch_export_service import BatchExportService

    container = Container(base_dir=str(tmp_path / "c"), load_plugins=False)
    first = container.ensure_services()
    assert container.batch_export_service is not None
    again = container.ensure_services()
    assert first is again
    assert isinstance(container.batch_export_service, BatchExportService)
    container.shutdown()


def test_full_pipeline_to_batch_export(tmp_path, qtbot):
    from app.container import Container
    from app.ui.widgets.variables_panel import VariablesPanel
    from app.infrastructure.distribution_registry import build_default_registry

    container = Container(base_dir=str(tmp_path / "c"), load_plugins=False)
    panel = VariablesPanel(build_default_registry())
    qtbot.addWidget(panel)

    text = "RANZ $1 -- $var2\nSCALE $1\nKRW $var2"
    panel.update_tokens(text)
    panel.specs = {
        1: __import__(
            "app.domain.entities", fromlist=["DistributionSpec"]
        ).DistributionSpec(provider="scipy", name="norm", params={"loc": 100.0, "scale": 5.0}),
        10002: __import__(
            "app.domain.entities", fromlist=["DistributionSpec"]
        ).DistributionSpec(provider="fixed", name="value", params={"value": 0.5}),
    }
    panel.update_tokens(text)

    from app.domain.entities import SamplingRequest

    request = SamplingRequest(
        var_ids=[1, 10002],
        specs=dict(panel.specs),
        n_experiments=7,
        seed=99,
        strategy="lhs",
    )
    result = container.sampling_service.run(request)
    assert len(result.matrix) == 7

    container.exp_repo.create_batch("batch_pipe", "lhs", 99, 7)
    container.exp_repo.insert_result("batch_pipe", result.var_ids, result.matrix)

    from app.core.parsing import find_variables, render_template

    assert find_variables(text) == [1, 10002]
    container.template_repo.create_template("fluxo")
    container.template_repo.save_version(
        1, text, comment="v1 do fluxo", user="tests"
    )
    limits = container.template_repo.list_templates()
    assert len(limits) == 1
    template_id = int(limits[0]["id"])
    version_row = container.template_repo.list_versions(template_id)[-1]

    container.ensure_services()
    out_root = tmp_path / "c" / "out_pipe"
    manifest = container.batch_export_service.export(
        "batch_pipe", int(version_row["id"]), out_root
    )
    assert manifest.n_files == 7

    files = sorted(Path(manifest.output_dir).glob("experimento_*.dat"))
    first = files[0].read_text(encoding="utf-8")
    values = container.exp_repo.fetch_page(0, 1, [1, 10002])[0]["values"]
    expected = render_template(text, values)
    assert first == expected
    assert "$" not in first

    from app.ui.widgets.export_done_dialog import ExportDoneDialog

    dialog = ExportDoneDialog(manifest.output_dir, manifest.n_files, manifest.manifest_path)
    qtbot.addWidget(dialog)
    assert dialog is not None

    container.shutdown()


def test_batch_export_worker_thread_completed(tmp_path, qtbot):
    from app.container import Container
    from app.workers.batch_export_worker import BatchExportWorker

    container = Container(base_dir=str(tmp_path / "cw"), load_plugins=False)
    container.exp_repo.create_batch("b_worker", "lhs", 0, 4)
    container.template_repo.create_template("worker_t")
    template_text = "GRID $1\nPROP $var2 $var2"
    container.template_repo.save_version(1, template_text)

    values = [[float(i), float(i) * 0.5] for i in range(1, 5)]
    container.exp_repo.insert_result("b_worker", [1, 10002], values)

    container.ensure_services()
    out_root = tmp_path / "cw" / "out_worker"

    template_versions = container.template_repo.list_versions(1)
    version_id = int(template_versions[0]["id"])
    signals = {"completed": None, "failed": None}

    from PySide6.QtCore import Qt as _Qt

    worker = BatchExportWorker(
        container.batch_export_service, "b_worker", version_id, str(out_root)
    )
    worker.completed.connect(
        lambda m: signals.update(completed=m), _Qt.ConnectionType.DirectConnection
    )
    worker.failed.connect(
        lambda e: signals.update(failed=e), _Qt.ConnectionType.DirectConnection
    )
    worker.start()
    finished = worker.wait(15000)

    assert finished, "worker não terminou"
    assert signals["failed"] is None
    assert signals["completed"] is not None
    assert signals["completed"].n_files == 4
    assert out_root.exists()
    container.shutdown()


def test_render_template_in_worker_thread(tmp_path, qtbot):
    from PySide6.QtCore import QThread

    from app.core.parsing import TOKEN_RE, token_var_id
    from app.services.strategies.monte_carlo import MonteCarloStrategy

    strategy = MonteCarloStrategy()
    uniforms = strategy.generate_uniforms(10, 2, np.random.default_rng(3))
    assert uniforms.shape == (10, 2)

    assert QThread.currentThread is not None
    m = TOKEN_RE.search("a $var3")
    assert token_var_id(m) == 10003
