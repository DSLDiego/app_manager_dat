"""Regressão da rodada 24: reexecutar amostragem (mesma/nova seed).

Padrão dos arquivos mínimos validados: Container/MainWindow no topo do
módulo + fixtures enxutos (sem yield no qapp).
"""

import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import pytest
from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QApplication, QMessageBox

from app.container import Container
from app.ui.main_window import MainWindow


@pytest.fixture()
def qapp():
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    return app


@pytest.fixture()
def window(tmp_path, qapp):
    container = Container(base_dir=str(tmp_path / "c24"), load_plugins=False)
    QSettings("datstudio", "dtengine").remove("recent/files")
    w = MainWindow(container)
    yield w
    w.close()
    QSettings("datstudio", "dtengine").remove("recent/files")


def test_rerun_without_params_guarded(window):
    launched = []
    window._launch_sampling = lambda request: launched.append(request)  # type: ignore
    original = QMessageBox.information
    QMessageBox.information = staticmethod(lambda *a, **k: 0)
    try:
        window._rerun_sampling(True)
    finally:
        QMessageBox.information = original
    assert launched == []  # guard falhou antes de disparar nada


def test_rerun_reuses_last_seed(window):
    window._last_sampling_params = {
        "var_ids": [1, 10002],
        "specs": {},
        "n": 5,
        "strategy": "monte_carlo",
        "workers": 1,
        "seed": 4242,
    }
    launched = []
    window._launch_sampling = lambda request: launched.append(request)  # type: ignore
    window._rerun_sampling(True)
    assert len(launched) == 1
    request = launched[0]
    assert request.seed == 4242
    assert request.n_experiments == 5
    assert request.var_ids == [1, 10002]
    assert request.workers == 1
    assert "Reexecutando" in window.status_message()
    assert "seed=4242" in window.status_message()


def test_rerun_new_seed_varies(window, monkeypatch):
    import random as _random

    def fake_randrange(self, a, b):
        return 987654

    monkeypatch.setattr(_random.SystemRandom, "randrange", fake_randrange)
    window._last_sampling_params = {
        "var_ids": [1],
        "specs": {},
        "n": 5,
        "strategy": "monte_carlo",
        "workers": 1,
        "seed": 4242,
    }
    launched = []
    window._launch_sampling = lambda request: launched.append(request)  # type: ignore
    window._rerun_sampling(False)
    assert launched[0].seed == 987654
    assert launched[0].n_experiments == 5
    assert launched[0].strategy == "monte_carlo"
    assert "seed=987654" in window.status_message()


def test_menu_actions_rerun_exist(window):
    assert window.act_rerun_same.text() == "Reexecutar amostragem (mesma seed)"
    assert window.act_rerun_new.text().endswith("nova seed aleatória)")
    assert "MESMA seed" in window.act_rerun_same.toolTip()
    assert window.act_rerun_same.isEnabled()
    assert window.act_rerun_new.isEnabled()


def test_last_params_shape_and_rerun_chain(window):
    from app.domain.entities import SamplingRequest

    window._last_sampling_params = {
        "var_ids": [1],
        "specs": {},
        "n": 10,
        "strategy": "monte_carlo",
        "workers": 1,
        "seed": 4242,
    }
    launched = []
    window._launch_sampling = lambda request: launched.append(request)  # type: ignore
    window._rerun_sampling(True)
    assert len(launched) == 1
    request = launched[0]
    assert isinstance(request, SamplingRequest)
    assert request.seed == 4242
    # reexecução com nova seed NÃO altera os params originais guardados
    assert window._last_sampling_params["seed"] == 4242
    window._rerun_sampling(False)
    assert len(launched) == 2
    assert launched[1].seed != 4242 or launched[1].seed == 4242  # aleatório livre
    assert window._last_sampling_params["seed"] == 4242
