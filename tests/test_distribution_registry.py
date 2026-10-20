"""Testes do registro de distribuições: providers scipy/fixed, validação e plugins."""

import pytest

import numpy as np

from app.domain.entities import DistributionSpec


def test_scipy_list_distributions(registry):
    provider = registry.get("scipy")
    names = provider.list_distributions()
    assert "norm" in names and "uniform" in names and "triang" in names


def test_scipy_parameter_names(registry):
    provider = registry.get("scipy")
    assert provider.parameter_names("norm") == ("loc", "scale")
    triang = provider.parameter_names("triang")
    assert "c" in triang and "loc" in triang and "scale" in triang


def test_fixed_sample(registry):
    provider = registry.get("fixed")
    spec = DistributionSpec(provider="fixed", name="value", params={"value": 3})
    values = provider.sample(spec, 5, np.random.default_rng(0))
    assert list(values) == [3.0] * 5


def test_fixed_validate(registry):
    spec = DistributionSpec(provider="fixed", name="value", params={})
    assert registry.validate(spec) != []


def test_scipy_validate(registry):
    spec = DistributionSpec(provider="scipy", name="norm", params={"loc": 0, "scale": 1})
    assert registry.validate(spec) == []


def test_registry_get_unknown():
    from app.infrastructure.distribution_registry import DistributionRegistry

    r = DistributionRegistry()
    assert r.get("nao_existe") is None
    with pytest.raises(KeyError):
        r.get_provider("nao_existe")


def test_plugin_loader_registers_provider(tmp_path, registry):
    from app.infrastructure.plugins.loader import PluginLoader

    plugin_code = '''
from typing import List

import numpy as np
from app.domain.entities import DistributionSpec
from app.infrastructure.providers.base import BaseDistributionProvider


class Beta0Provider(BaseDistributionProvider):
    provider_name = "beta0"
    description = "Constante beta0."

    def list_distributions(self) -> List[str]:
        return ["generic"]

    def parameter_names(self, dist_name: str) -> List[str]:
        return ["value"]

    def sample(self, spec: DistributionSpec, size: int, rng: np.random.Generator):
        return np.full(size, float(spec.params.get("value", 0.0)))

    def validate(self, spec: DistributionSpec) -> List[str]:
        return []
'''
    dir_path = tmp_path / "plugins"
    dir_path.mkdir()
    (dir_path / "beta0_plugin.py").write_text(plugin_code, encoding="utf-8")
    (dir_path / "_skip_me.py").write_text("raise SystemExit(1)", encoding="utf-8")

    loader = PluginLoader(dir_path)
    report = loader.register_all(registry)

    assert len(report.loaded) == 1
    assert report.loaded[0].ok
    provider = registry.get("beta0")
    spec = DistributionSpec(provider="beta0", name="generic", params={"value": 9})
    assert provider.sample(spec, 4, np.random.default_rng(0)).tolist() == [9.0] * 4


def test_plugin_loader_reports_failure(tmp_path):
    from app.infrastructure.plugins.loader import PluginLoader

    dir_path = tmp_path / "plugins_bad"
    dir_path.mkdir()
    (dir_path / "broken.py").write_text("raise RuntimeError('erro plugin')", encoding="utf-8")

    from app.infrastructure.distribution_registry import DistributionRegistry

    loader = PluginLoader(dir_path)
    report = loader.register_all(DistributionRegistry())

    assert len(report.failed) == 1
    assert report.failed[0].error
