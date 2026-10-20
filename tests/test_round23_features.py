"""Regressão da rodada 23: seed configurável + status com seed usada."""

import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import pytest
from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QApplication


@pytest.fixture(scope="module")
def qapp():
    app = QApplication.instance() or QApplication([])
    yield app


# ---------- puro: reprodutibilidade com seed ----------

def _tiny_specs():
    from app.domain.entities import DistributionSpec

    return {1: DistributionSpec(provider="scipy", name="norm", params={"loc": 0.0, "scale": 1.0})}


def _svc():
    from app.infrastructure.distribution_registry import build_default_registry
    from app.services.sampling_service import SamplingService

    return SamplingService(build_default_registry())


def test_same_seed_same_matrix():
    from app.domain.entities import SamplingRequest

    svc = _svc()
    req = SamplingRequest(var_ids=[1], specs=_tiny_specs(), n_experiments=25, seed=777)
    r1 = svc.run(req)
    r2 = svc.run(req)
    assert r1.seed_used == 777
    assert r1.matrix == r2.matrix  # mesma seed → mesma matriz (reprodutível)


def test_different_seed_different_matrix():
    from app.domain.entities import SamplingRequest

    svc = _svc()
    req_a = SamplingRequest(var_ids=[1], specs=_tiny_specs(), n_experiments=25, seed=1)
    req_b = SamplingRequest(var_ids=[1], specs=_tiny_specs(), n_experiments=25, seed=2)
    assert svc.run(req_a).matrix != svc.run(req_b).matrix


# ---------- puro: seed de texto ----------

def test_seed_from_text_empty_is_random_in_range():
    from app.core.seed_utils import seed_from_text

    seeds = {seed_from_text("") for _ in range(5)}
    assert len(seeds) >= 2  # aleatório quase nunca repete
    assert all(1 <= s <= 2_147_483_647 for s in seeds)
    assert seed_from_text(None) >= 1


def test_seed_from_text_fixed_is_reproducible():
    from app.core.seed_utils import seed_from_text

    assert seed_from_text("424242") == 424242
    assert seed_from_text(" 19999 ") == 19999  # espaços ignorados
    assert seed_from_text("999999999999") == 2_147_483_647  # clamp no topo
    assert seed_from_text("0") == 1  # mínimo coerente


def test_seed_from_text_rejects_junk():
    import pytest as _pytest

    from app.core.seed_utils import seed_from_text

    with _pytest.raises(ValueError):
        seed_from_text("abc")
    with _pytest.raises(ValueError):
        seed_from_text("12.5")
    with _pytest.raises(ValueError):
        seed_from_text("-3")


# ---------- main window: status com seed ----------

def test_on_sampling_completed_sets_status_with_seed(tmp_path, qapp):
    from PySide6.QtCore import QSettings

    from app.container import Container
    from app.domain.events import SamplingCompletedEvent
    from app.ui.main_window import MainWindow

    try:
        QSettings("datstudio", "dtengine").remove("recent/files")
        container = Container(base_dir=str(tmp_path / "c23"), load_plugins=False)
        window = MainWindow(container)
        event = SamplingCompletedEvent(var_ids=(1,), matrix=((1.0,),), seed_used=31337, duration_seconds=0.42)
        window._on_bus_sampling_completed(event)
        assert "seed=31337" in window.status_message()
        assert "0.4s" in window.status_message() or "0.42s" in window.status_message()
        window.close()
    finally:
        QSettings("datstudio", "dtengine").remove("recent/files")
