"""Regressões backend: providers, registry, parsing, workers, bus, repos."""

import io
import sys
from contextlib import redirect_stderr

import numpy as np
import pytest

from app.domain.entities import DistributionSpec, SamplingRequest
from app.infrastructure.distribution_registry import (
    DistributionRegistry,
    build_default_registry,
    build_registry,
)
from app.infrastructure.event_bus import EventBus
from app.infrastructure.providers.fixed_provider import FixedProvider
from app.infrastructure.providers.scipy_provider import ScipyProvider
from app.core.parsing import TOKEN_RE, format_value, render_template

pytest.importorskip("numpy")


# ---------- format_value / render ----------
def test_format_value_rejects_nan_and_inf():
    with pytest.raises(ValueError):
        format_value(float("nan"))
    with pytest.raises(ValueError):
        format_value(float("inf"))
    with pytest.raises(ValueError):
        format_value(float("-inf"))


def test_format_value_basic_types():
    assert format_value(1.5) == "1.5"
    assert format_value(2.0) == "2"
    assert format_value(3) == "3"
    assert format_value(True) == "1"
    assert format_value(False) == "0"
    assert format_value(0.00000125) == "1.25e-06"


def test_render_template_rejects_nan_values():
    with pytest.raises(ValueError):
        render_template("A $1", {1: float("nan")})


def test_render_template_very_small_and_large_values():
    out = render_template("a=$1 b=$var2", {1: 1e-11, 10002: 1.5e15})
    assert "1e-11" in out
    assert "1.5e+15" in out


def test_token_regex_namespaces(data=None):
    text = "$1 $var1 $V2 $v3 VAR $4"
    var_ids = {TOKEN_RE.search: None}  # sanity placeholder
    from app.core.parsing import find_variables

    assert find_variables(text) == [1, 4, 10001, 10002, 10003]


# ---------- registry ----------
def test_registry_remove_and_provider_names():
    reg = build_default_registry()
    assert "fixed" in reg.provider_names()
    reg.remove("fixed")
    assert "fixed" not in reg.provider_names()
    assert reg.get("fixed") is None
    with pytest.raises(KeyError):
        reg.get_provider("fixed")


def test_registry_code_roundtrip():
    spec = DistributionRegistry.parse_code("scipy.norm")
    assert spec.provider == "scipy" and spec.name == "norm"
    assert DistributionRegistry.get_spec_code("scipy", "norm") == "scipy.norm"


def test_build_registry_with_plugins_dir(tmp_path):
    plugin = tmp_path / "z_my_plugin.py"
    plugin.write_text(
        "from app.infrastructure.providers.base import BaseDistributionProvider\n"
        "class ZFixed(BaseDistributionProvider):\n"
        "    provider_name = 'zfixed'\n"
        "    def list_distributions(self):\n"
        "        return ['constant']\n"
        "    def parameter_names(self, dist_name):\n"
        "        return ['value']\n"
        "    def sample(self, spec, size, rng):\n"
        "        import numpy as np\n"
        "        return np.full(size, 7.0)\n"
        "    def validate(self, spec):\n"
        "        return []\n",
        encoding="utf-8",
    )
    reg = build_registry(str(tmp_path))
    assert "zfixed" in reg.provider_names()
    spec = DistributionSpec(provider="zfixed", name="constant", params={"value": 1})
    assert reg.sample(spec, 3, None).tolist() == [7.0, 7.0, 7.0]


# ---------- providers ----------
def test_scipy_parameter_names_shapes():
    provider = ScipyProvider()
    assert "loc" in provider.parameter_names("norm")
    assert "scale" in provider.parameter_names("norm")
    names_beta = provider.parameter_names("beta")
    assert "a" in names_beta and "b" in names_beta
    assert "loc" in names_beta and "scale" in names_beta


def test_scipy_ppf_accuracy():
    provider = ScipyProvider()
    spec = DistributionSpec(provider="scipy", name="norm", params={"loc": 0.0, "scale": 1.0})
    out = provider.ppf(spec, np.array([0.5]))
    assert out[0] == pytest.approx(0.0, abs=1e-6)


def test_scipy_validate_unknown_dist():
    provider = ScipyProvider()
    errors = provider.validate(
        DistributionSpec(provider="scipy", name="nao_existe", params={})
    )
    assert len(errors) == 1 and "desconhecida" in errors[0]


def test_fixed_ppf_and_validate():
    provider = FixedProvider()
    spec = DistributionSpec(provider="fixed", name="value", params={"value": 5})
    out = provider.ppf(spec, np.array([0.1, 0.9]))
    assert out.tolist() == [5.0, 5.0]
    assert provider.validate(spec) == []
    assert provider.validate(DistributionSpec("fixed", "value")) == ["Parâmetro 'value' obrigatório"]


# ---------- correlação / strategies ----------
def test_iman_conover_preserves_marginals():
    from app.services.strategies.correlated import iman_conover_reorder

    rng = np.random.default_rng(0)
    base = rng.normal(size=(400, 2))
    out = iman_conover_reorder(base, [[1.0, 0.6], [0.6, 1.0]])
    for col in range(2):
        assert sorted(out[:, col].tolist()) == pytest.approx(
            sorted(base[:, col].tolist())
        )


def test_correlated_strategy_validate():
    from app.services.strategies.correlated import CorrelatedStrategy

    ok = CorrelatedStrategy.validate([[1.0, 0.5], [0.5, 1.0]])
    assert ok == []
    bad = CorrelatedStrategy.validate([[1.0, 2.0], [2.0, 1.0]])
    assert len(bad) == 1


def test_sampling_correlated_without_matrix():
    from app.services.sampling_service import SamplingService

    service = SamplingService(build_default_registry())
    request = SamplingRequest(
        var_ids=[1, 10002],
        specs={
            1: DistributionSpec(provider="scipy", name="norm", params={"loc": 0, "scale": 1}),
            10002: DistributionSpec(provider="fixed", name="value", params={"value": 3.0}),
        },
        n_experiments=10,
        seed=1,
        strategy="correlated",
    )
    result = service.run(request)
    assert len(result.matrix) == 10
    matrix = np.asarray(result.matrix)
    assert np.all(matrix[:, 1] == 3.0)


def test_register_strategy_via_protocol():
    from app.services.sampling_service import SamplingService
    from app.services.strategies.base import UnionSamplingStrategy

    class _Custom:
        name = "custom"

        def generate_uniforms(self, n, d, rng):
            return np.full((n, d), 0.5)

    service = SamplingService(build_default_registry())
    assert isinstance(_Custom(), UnionSamplingStrategy)
    service.register_strategy("custom", _Custom())
    request = SamplingRequest(
        var_ids=[1],
        specs={1: DistributionSpec(provider="scipy", name="expon", params={"loc": 2})},
        n_experiments=5,
        seed=0,
        strategy="custom",
    )

    result = service.run(request)
    matrix = np.asarray(result.matrix)
    assert np.allclose(matrix, 2.0 + np.log(2.0))  # ppf(0.5) da expon(loc=2)


# ---------- event bus ----------
def test_event_bus_unsubscribe_and_exception_isolation():
    from app.domain.events import LogCreatedEvent

    bus = EventBus()
    calls = []
    errors = []

    def handler(_event):
        calls.append(1)

    def broken(_event):
        raise RuntimeError("boom")

    bus.subscribe(LogCreatedEvent, broken)
    bus.subscribe(LogCreatedEvent, handler)
    stderr = io.StringIO()
    with redirect_stderr(stderr):
        bus.publish(LogCreatedEvent(level="INFO", category="X", action="a", message="m"))
    assert calls == [1]
    assert "boom" in stderr.getvalue()
    bus.unsubscribe(LogCreatedEvent, handler)
    bus.publish(LogCreatedEvent(level="INFO", category="X", action="a", message="m"))
    assert len(calls) == 1  # handler não chamado de novo


# ---------- workers: pickling e chunk ----------
def test_chunk_worker_pickles_request_with_plugin(tmp_path):
    from app.workers.sampling_worker import _chunk_worker

    plugin_dir = tmp_path / "plugins"
    plugin_dir.mkdir()
    (plugin_dir / "p.py").write_text(
        "from app.infrastructure.providers.base import BaseDistributionProvider\n"
        "import numpy as np\n"
        "class PFixed(BaseDistributionProvider):\n"
        "    provider_name = 'pfixed'\n"
        "    def list_distributions(self):\n"
        "        return ['value']\n"
        "    def parameter_names(self, dist_name):\n"
        "        return ['value']\n"
        "    def sample(self, spec, size, rng):\n"
        "        return np.full(size, 11.0)\n"
        "    def validate(self, spec):\n"
        "        return []\n",
        encoding="utf-8",
    )
    import pickle

    request = SamplingRequest(
        var_ids=[1],
        specs={1: DistributionSpec(provider="pfixed", name="value", params={"value": 1})},
        n_experiments=5,
        seed=0,
        plugins_dir=str(plugin_dir),
    )
    pickled = pickle.dumps(request)
    restored = pickle.loads(pickled)
    start, matrix = _chunk_worker((restored, 0, 5))
    assert start == 0
    assert np.asarray(matrix).size == 5


def test_export_worker_empty_matrix_completion(qtbot, qapp, tmp_path):
    import pytestqt.qtbot  # noqa

    from app.workers.export_worker import ExportWorker

    out_dir = tmp_path / "out_empty"
    worker = ExportWorker("RUNZ $1", [1], [], str(out_dir))
    worker.start()
    worker.wait(5000)
    assert out_dir.exists()


def test_export_worker_writes_files(qtbot, qapp, tmp_path):
    from app.workers.export_worker import ExportWorker

    out_dir = tmp_path / "out_full"
    worker = ExportWorker(
        "RANZ $1 -- $var2",
        [1, 10002],
        [[1.0, 5.0], [2.0, 5.0], [3.0, 5.0]],
        str(out_dir),
        io_workers=2,
    )
    worker.start()
    worker.wait(8000)
    files = sorted(out_dir.glob("experimento_*.dat"))
    assert len(files) == 3
    text = files[0].read_text(encoding="utf-8")
    assert "$" not in text


# ---------- metrics detalhes ----------
def test_metrics_top_actions_and_days(container, populated_batch):
    container.log_repo.wait_pending()
    container.log_service.usage("app.open", "boot")
    container.log_repo.wait_pending()
    container.ensure_services()
    actions = container.metrics_service.top_actions(5)
    assert isinstance(actions, list) and len(actions) >= 1
    assert all(isinstance(a[1], int) for a in actions)
    days = container.metrics_service.actions_per_day(3)
    assert isinstance(days, list)


# ---------- experiment repo extras ----------
def test_experiment_repo_count_var_ids_pagination(repos):
    exp_repo, template_repo = repos["exp"], repos["tpl"]
    exp_repo.create_batch("b_pag", "lhs", 1, 15)
    var_ids = [1, 2]
    matrix = [[float(i), float(i) * 2] for i in range(1, 16)]
    exp_repo.insert_result("b_pag", var_ids, matrix)
    assert exp_repo.count() == 15
    ids = exp_repo.var_ids()
    assert ids == var_ids
    page0 = exp_repo.fetch_page(0, 10, var_ids)
    page1 = exp_repo.fetch_page(1, 10, var_ids)
    assert len(page0) == 10 and len(page1) == 5
    assert page1[0]["values"][1] == 11.0
    assert exp_repo.get_variable_values(2)[:3] == pytest.approx(
        [2.0, 4.0, 6.0]
    )
