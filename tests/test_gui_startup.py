"""Testes de inicialização da GUI: boot do container, MainWindow e subp pwd."""

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

pytest.importorskip("pytestqt")

PROJECT_ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture()
def boot():
    """Aplicação + Container + MainWindow prontos para uso."""

    def _boot(tmp_path, **_kwargs):
        from PySide6.QtWidgets import QApplication

        app = QApplication.instance() or QApplication([])

        from app.container import Container
        from app.ui.main_window import MainWindow

        container = Container(base_dir=str(tmp_path), load_plugins=False)
        window = MainWindow(container)
        window.show()
        return app, container, window

    return _boot


# -------------------------------------------------------------------------
# 1. Bootstrap mínimo
# -------------------------------------------------------------------------
def test_application_and_window_created(boot, tmp_path, qtbot):
    app, container, window = boot(tmp_path)
    qtbot.addWidget(window)

    assert window.windowTitle() == "DAT Engineering Studio"
    assert window.windowTitle() != ""
    assert window.centralWidget() is not None


def test_window_has_editor_and_variables(boot, tmp_path, qtbot):
    _, _, window = boot(tmp_path)
    qtbot.addWidget(window)
    editor = window.editor_tabs.current_editor()
    assert editor is not None
    window._sync_variables()
    assert not window.variables_panel.var_map  # sem tokens
    assert window.variables_panel.list_widget.count() == 0


# -------------------------------------------------------------------------
# 2. Janela principal: título, componentes e docks
# -------------------------------------------------------------------------
def test_main_window_components(boot, tmp_path, qtbot):
    _, _, window = boot(tmp_path)
    qtbot.addWidget(window)

    assert window.editor_tabs.count() == 1
    assert window.variables_panel.list_widget.count() == 0
    assert window.logs_panel is not None
    assert window.experiments_panel is not None
    assert window.preview_panel is not None


def test_main_window_menus(boot, tmp_path, qtbot):
    _, _, window = boot(tmp_path)
    qtbot.addWidget(window)

    menubar = window.menuBar()
    actions = menubar.actions()
    names = [a.text() for a in actions]
    assert "Arquivo" in names
    assert "Ferramentas" in names

    file_menu = menubar.actions()[0].menu()
    file_names = [a.text() for a in file_menu.actions()]
    assert "Novo" in file_names
    assert any(name.startswith("Abrir") for name in file_names)
    assert "Salvar" in file_names


def test_main_window_first_new_tab(boot, tmp_path, qtbot):
    _, _, window = boot(tmp_path)
    qtbot.addWidget(window)
    editor = window.editor_tabs.current_editor()
    assert editor is not None
    editor.set_content("")
    window._sync_variables()
    assert not window.variables_panel.var_map
    assert window.variables_panel.list_widget.count() == 0


def test_container_loads_storages(boot, tmp_path, qtbot):
    _, container, window = boot(tmp_path)
    qtbot.addWidget(window)
    assert container.log_repo.count() >= 0
    assert container.exp_repo.count() == 0
    assert container.template_repo.list_templates() == []
    assert list(container.registry.provider_names()) != []
    window.close()


def test_container_shutdown_closes_all_repos(boot, tmp_path, qtbot):
    _, container, window = boot(tmp_path)
    qtbot.addWidget(window)
    window.close()
    container.shutdown()
    with pytest.raises(Exception):
        container.log_repo.count()


# -------------------------------------------------------------------------
# 3. Shutdown e fechamento limpo da MainWindow
# -------------------------------------------------------------------------
def test_close_event_triggers_shutdown(boot, tmp_path, qtbot):
    _, container, window = boot(tmp_path)
    qtbot.addWidget(window)
    window.close()
    assert window.isVisible() is False
    container.shutdown()


def test_repeated_instance_boot(boot, tmp_path, qtbot):
    _, container, window1 = boot(tmp_path)
    qtbot.addWidget(window1)
    window2 = boot(tmp_path)[2]
    qtbot.addWidget(window2)
    assert window1 is not window2
    window2.close()
    window1.close()
    container.shutdown()


# -------------------------------------------------------------------------
# 4. Integração de amostragem/sampling no startup
# -------------------------------------------------------------------------
def test_main_window_loads_data_template(boot, tmp_path, qtbot):
    _, _, window = boot(tmp_path)
    qtbot.addWidget(window)
    editor = window.editor_tabs.current_editor()
    editor.set_content("*TITLE\nFOO $1 -- $var2 *DATES\n/CMD $V3")

    window._sync_variables()
    assert window.variables_panel.var_map == [1, 10002, 10003]


def test_starting_with_dock_layout(boot, tmp_path, qtbot):
    _, _, window = boot(tmp_path)
    qtbot.addWidget(window)
    docks = window.findChildren(__import__(
        "PySide6.QtWidgets", fromlist=["QDockWidget"]
    ).QDockWidget)
    titles = [d.windowTitle() for d in docks]
    assert "Variáveis" in titles
    assert "Logs" in titles
    window.close()


def test_startup_updates_progress_bar(boot, tmp_path, qtbot):
    from app.domain.events import SamplingProgressEvent

    _, container, window = boot(tmp_path)
    qtbot.addWidget(window)
    container.event_bus.publish(SamplingProgressEvent(52, "meio do caminho"))
    assert window.progress.value() == 52


def test_startup_pipeline_sample_template(boot, tmp_path, qtbot):
    from app.domain.entities import DistributionSpec, SamplingRequest

    _, container, window = boot(tmp_path)
    qtbot.addWidget(window)
    editor = window.editor_tabs.current_editor()
    editor.set_content("*DADOS $1 $var2")

    from app.core.parsing import find_variables

    var_ids = find_variables(editor.text())
    assert var_ids == [1, 10002]

    specs = {
        1: DistributionSpec(provider="scipy", name="norm", params={"loc": 5.0, "scale": 1.0}),
        10002: DistributionSpec(provider="fixed", name="value", params={"value": 100.0}),
    }
    request = SamplingRequest(var_ids=var_ids, specs=specs, n_experiments=8, seed=3)
    result = container.sampling_service.run(request)
    container.exp_repo.create_batch("test_batch", "mc", 3, 8)
    container.exp_repo.insert_result("test_batch", result.var_ids, result.matrix)
    window.exp_model.refresh()

    assert window.exp_model.total_rows == 8
    window.close()


# -------------------------------------------------------------------------
# 5. main() subprocess real (offscreen): pipes de auto-fechamento
# -------------------------------------------------------------------------
RUNNER = r"""
import json, os, sys, tempfile

os.environ["QT_QPA_PLATFORM"] = "offscreen"
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication

from app import APP_NAME
from app.container import Container
from app.ui.main_window import MainWindow

app = QApplication(sys.argv)
app.setApplicationName(APP_NAME)

boot_dir = sys.argv[1] if len(sys.argv) > 1 else tempfile.mkdtemp()
container = Container(base_dir=boot_dir, load_plugins=False)
window = MainWindow(container)
window.show()

QTimer.singleShot(1200, app.quit)
exit_code = app.exec()
window.hide()
container.shutdown()

report = {
    "title": window.windowTitle(),
    "visible": window.isVisible(),
    "progress_max": window.progress.maximum(),
    "menubar_actions": len(window.menuBar().actions()),
}
print("REPORT:" + json.dumps(report))
sys.exit(0 if exit_code == 0 else 1)
"""


def test_subprocess_full_gui_startup(tmp_path):
    runner = tmp_path / "_startup_runner.py"
    runner.write_text(RUNNER, encoding="utf-8")

    boot_dir = tmp_path / "boot"
    boot_dir.mkdir()

    env = dict(os.environ)
    env["QT_QPA_PLATFORM"] = "offscreen"
    env["PYTHONPATH"] = str(PROJECT_ROOT)

    result = subprocess.run(
        [sys.executable, str(runner), str(boot_dir)],
        capture_output=True, text=True, timeout=90,
        cwd=str(PROJECT_ROOT), env=env,
    )

    assert result.returncode == 0, result.stderr or result.stdout
    report_line = next(
        line for line in result.stdout.splitlines() if line.startswith("REPORT:")
    )
    report = json.loads(report_line[len("REPORT:"):])
    assert report["title"] == "DAT Engineering Studio"
    assert report["menubar_actions"] >= 2
    assert report["progress_max"] == 100
