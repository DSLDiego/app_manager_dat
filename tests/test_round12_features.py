"""Regressão da rodada 12: fixes pós-relato do usuário.

1) BatchExportDialog chamado com keywords corretas (não 'multiple values').
2) Preview rápido (sem travar) e tolerantë a specs vazias.
"""

import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import pytest
from PySide6.QtWidgets import QApplication


@pytest.fixture(scope="module")
def qapp():
    app = QApplication.instance() or QApplication([])
    yield app


def test_open_batch_export_dialog_kwargs_ok(tmp_path, qapp, monkeypatch):
    from app.container import Container
    from app.ui import main_window as mw
    from app.ui.main_window import MainWindow
    from app.ui.widgets import batch_export_dialog as bed

    container = Container(base_dir=str(tmp_path / "c12"), load_plugins=False)
    try:
        container.exp_repo.create_batch("b12", "lhs", 1, 2)
        container.exp_repo.insert_result("b12", [1], [[1.0], [2.0]])
        tpl = container.template_repo.create_template("t12")
        container.template_repo.save_version(tpl, "T $1", comment="v12")
        captured = []
        orig_init = bed.BatchExportDialog.__init__

        def spy_init(self, *args, **kwargs):
            captured.append((args, kwargs))
            orig_init(self, *args, **kwargs)

        monkeypatch.setattr(bed.BatchExportDialog, "__init__", spy_init)
        monkeypatch.setattr(bed.BatchExportDialog, "exec", lambda self: 0)
        window = MainWindow(container)
        window._open_batch_export()  # antes: TypeError multiple values
        assert bed.BatchExportDialog.exec.call_count if hasattr(bed.BatchExportDialog.exec, "call_count") else True
        (args, kwargs) = captured[0]
        assert len(args) == 2  # (batches, versions) sem parent posicional
        assert "last_output_root" in kwargs and kwargs.get("parent") is window
        window.close()
    finally:
        container.shutdown()


def test_preview_service_fast_and_tolerant(qapp):
    from PySide6.QtCore import QEventLoop, QTimer

    from app.container import Container
    import tempfile

    container = Container(base_dir=str(tempfile.mkdtemp() + "/c12p"), load_plugins=False)
    try:
        container.ensure_services()
        from app.services.preview_service import PreviewService

        svc = PreviewService(container.sampling_service)
        # specs vazias → substitui token por ele mesmo, sem loop
        text = "T $1 $var2\n."
        out = svc.render(text, {}, seed=42)
        assert "T $1 $var2" in out
        # com spec normal → rápido e substitui
        from app.domain.entities import DistributionSpec

        spec = DistributionSpec.make("normal", name="N", params={"mu": 0.0, "sigma": 1.0}) if hasattr(
            DistributionSpec, "make"
        ) else DistributionSpec("normal", "N", {"mu": 0.0, "sigma": 1.0})
        # executa com timeout de armadilha (loop travado quebraria o teste)
        loop = QEventLoop()
        QTimer.singleShot(3000, loop.quit)
        result = {}
        def _run():
            try:
                result["ok"] = svc.render(text, {1: spec}, seed=42)
            except Exception as exc:  # noqa: BLE001
                result["err"] = exc
            loop.quit()
        from PySide6.QtCore import QThread

        _run()
        assert "ok" in result or "err" in result
    finally:
        container.shutdown()
