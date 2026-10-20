"""Rodada 31: validador CMG, limites de parâmetros e cache de amostragem."""

import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import pytest
from PySide6.QtWidgets import QApplication, QMessageBox

from app.container import Container
from app.core.parsing import (
    template_sections,
    validate_template,
    validation_summary,
)
from app.core.spec_validation import validate_spec_params
from app.domain.entities import DistributionSpec, SamplingRequest
from app.infrastructure.distribution_registry import build_default_registry
from app.services.sampling_cache import SamplingCache, cache_key
from app.services.sampling_service import SamplingService


@pytest.fixture()
def qapp():
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    return app


# ---------- template CMG ----------

def test_template_sections_ignores_comments():
    text = "*TITLE\n-- *FAKE\n**GRID\n*GRID 10 10 1\n"
    assert template_sections(text) == ["*TITLE", "*GRID"]


def test_validate_template_ok():
    text = "*TITLE\nTeste\n*GRID\n10 10 1\n*ROCK\n1\n$1\n"
    assert validate_template(text) == []
    assert "válido" in validation_summary([])


def test_validate_template_empty_is_error():
    issues = validate_template("   \n")
    assert issues and issues[0]["severity"] == "error"


def test_validate_template_warns_missing_title_and_unknown_section():
    issues = validate_template("*GRID\n10 10 1\n*FOOBAR\n1\n")
    messages = " ".join(i["message"] for i in issues)
    assert "*TITLE" in messages
    assert "FOOBAR" in messages
    assert all(i["severity"] == "warning" for i in issues)


def test_validate_template_invalid_token_has_line():
    issues = validate_template("*TITLE\nx\n*GRID\n$abc\n")
    errs = [i for i in issues if i["severity"] == "error"]
    assert len(errs) == 1
    assert errs[0]["line"] == 4
    assert "$abc" in errs[0]["message"]
    assert "erro" in validation_summary(issues)


def test_mainwindow_validate_action(qapp, tmp_path):
    from app.ui.main_window import MainWindow

    window = MainWindow(Container(base_dir=str(tmp_path / "c31"), load_plugins=False))
    shown = []
    original_info = QMessageBox.information
    QMessageBox.information = staticmethod(lambda *a, **k: shown.append(a[2]))
    try:
        window.editor_tabs.current_editor().editor.setPlainText("*TITLE\nok $1\n")
        issues = window._validate_template_action()
    finally:
        QMessageBox.information = original_info
    assert issues == []
    assert window._last_validation == []
    assert shown and "válido" in shown[0]
    window.close()


# ---------- limites de parâmetros ----------

def test_validate_spec_params_ok():
    assert validate_spec_params("normal", {"loc": 0.0, "scale": 1.0}) == []


@pytest.mark.parametrize("scale", [0, -1, float("nan"), float("inf"), 1e13])
def test_validate_spec_params_bad_scale(scale):
    assert validate_spec_params("normal", {"loc": 0.0, "scale": scale})


def test_validate_spec_params_bad_loc():
    assert validate_spec_params("normal", {"loc": 1e16, "scale": 1.0})


def test_validate_spec_params_triangular_order():
    assert validate_spec_params(
        "triangular", {"low": 0.0, "mode": 5.0, "high": 1.0}
    )
    assert validate_spec_params(
        "triangular", {"low": 0.0, "mode": 0.5, "high": 1.0}
    ) == []


def test_validate_spec_params_uniform_order():
    assert validate_spec_params("uniform", {"a": 2, "b": 1})
    assert validate_spec_params("uniform", {"a": 1, "b": 2}) == []


def test_sampling_rejects_invalid_scale():
    service = SamplingService(build_default_registry())
    request = SamplingRequest(
        var_ids=[1],
        specs={1: DistributionSpec("scipy", "norm", {"loc": 0.0, "scale": -3.0})},
        n_experiments=5,
        seed=1,
    )
    with pytest.raises(ValueError, match="scale"):
        service.run(request)


# ---------- cache de amostragem ----------

def _request(n=10, seed=7):
    return SamplingRequest(
        var_ids=[1],
        specs={1: DistributionSpec("scipy", "norm", {"loc": 0.0, "scale": 1.0})},
        n_experiments=n,
        seed=seed,
    )


def test_cache_key_stable_and_sensitive():
    specs = _request().specs
    k1 = cache_key([1], specs, 10, "monte_carlo", 7)
    k2 = cache_key([1], specs, 10, "monte_carlo", 7)
    k3 = cache_key([1], specs, 10, "monte_carlo", 8)
    assert k1 == k2
    assert k1 != k3


def test_sampling_cache_hit_returns_same_result():
    cache = SamplingCache(max_entries=4)
    service = SamplingService(build_default_registry(), cache=cache)
    first = service.run(_request())
    second = service.run(_request())
    assert cache.hits == 1
    assert cache.misses == 1
    assert second is first


def test_sampling_cache_miss_on_different_n():
    cache = SamplingCache(max_entries=4)
    service = SamplingService(build_default_registry(), cache=cache)
    service.run(_request(n=10))
    service.run(_request(n=11))
    assert cache.hits == 0
    assert cache.misses == 2
    assert len(cache) == 2


def test_sampling_cache_lru_bounded():
    cache = SamplingCache(max_entries=2)
    service = SamplingService(build_default_registry(), cache=cache)
    for n in (5, 6, 7):
        service.run(_request(n=n))
    assert len(cache) == 2


def test_container_exposes_sampling_cache(tmp_path):
    container = Container(base_dir=str(tmp_path / "c31b"), load_plugins=False)
    assert container.sampling_service.cache is container.sampling_cache
    assert container.sampling_cache.max_entries == 8