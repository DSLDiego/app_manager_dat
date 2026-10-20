"""Testes do SamplingService: MC, LHS, correlação (Iman-Conover) e erros."""

import numpy as np
import pytest

from app.domain.entities import DistributionSpec, SamplingRequest


def _spec_norm(mu, sigma):
    return DistributionSpec(provider="scipy", name="norm", params={"loc": mu, "scale": sigma})


SPECS = {
    1: _spec_norm(10.0, 1.0),
    2: _spec_norm(20.0, 3.0),
    3: DistributionSpec(provider="fixed", name="value", params={"value": 5.0}),
}


def test_monte_carlo_shape_and_reproducibility(sampling_service):
    r1 = sampling_service.run(
        SamplingRequest(var_ids=[1, 2, 3], specs=SPECS, n_experiments=200, seed=3)
    )
    r2 = sampling_service.run(
        SamplingRequest(var_ids=[1, 2, 3], specs=SPECS, n_experiments=200, seed=3)
    )
    assert len(r1.matrix) == 200
    assert all(len(row) == 3 for row in r1.matrix)
    assert r1.matrix == r2.matrix
    assert r1.seed_used == 3


def test_lhs_marginals_reduced_dispersion(sampling_service):
    lhs = sampling_service.run(
        SamplingRequest(var_ids=[1, 2], specs=SPECS, n_experiments=500, seed=11, strategy="lhs")
    )
    mc = sampling_service.run(
        SamplingRequest(var_ids=[1, 2], specs=SPECS, n_experiments=500, seed=11, strategy="monte_carlo")
    )
    b_lhs = np.asarray(lhs.matrix)
    b_mc = np.asarray(mc.matrix)
    assert b_lhs.shape == b_mc.shape
    per_bin_lhs = np.zeros(10)
    values = np.sort(b_lhs[:, 0])
    bins = np.quantile(values, np.linspace(0, 1, 11))
    for i in range(10):
        per_bin_lhs[i] = ((values >= bins[i]) & (values <= bins[i + 1])).sum()
    # LHS garante aproximadamente um ponto por "faixa" — muito mais uniforme que MC
    assert per_bin_lhs.min() >= 30


def test_empty_request_returns_empty(sampling_service):
    result = sampling_service.run(
        SamplingRequest(var_ids=[], specs={}, n_experiments=10, seed=1)
    )
    assert result.matrix == []
    result = sampling_service.run(
        SamplingRequest(var_ids=[1], specs={1: _spec_norm(0, 1)}, n_experiments=0, seed=1)
    )
    assert result.matrix == []


def test_unknown_strategy_raises(sampling_service):
    with pytest.raises(ValueError):
        sampling_service.run(
            SamplingRequest(var_ids=[1], specs={1: _spec_norm(0, 1)}, n_experiments=5, seed=1, strategy="nao_existe")
        )


def test_pearson_correlated(sampling_service):
    specs = {1: _spec_norm(0.0, 1.0), 2: _spec_norm(30.0, 3.0)}
    result = sampling_service.run(
        SamplingRequest(
            var_ids=[1, 2], specs=specs, n_experiments=4000, seed=42,
            strategy="correlated", correlation=[[1.0, 0.9], [0.9, 1.0]],
        )
    )
    matrix = np.asarray(result.matrix)
    pearson = np.corrcoef(matrix.T)[0, 1]
    assert pearson > 0.55


def test_register_strategy_extensibility(sampling_service):
    class HaltonLike:
        name = "fake_halton"

        def generate_uniforms(self, n, d, rng):
            return np.full((n, d), 0.5)

    sampling_service.register_strategy("fake_halton", HaltonLike())
    result = sampling_service.run(
        SamplingRequest(var_ids=[1], specs={1: _spec_norm(5, 1)}, n_experiments=8, seed=1, strategy="fake_halton")
    )
    assert all(abs(row[0] - 5.0) < 1e-9 for row in result.matrix)
