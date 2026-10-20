"""Benchmark opt-in de 1M experimentos. Rode com $env:DAT_BENCH="1"."""

import os
import time

import pytest

DAT_BENCH = os.environ.get("DAT_BENCH", "")

pytestmark = pytest.mark.skipif(
    DAT_BENCH != "1",
    reason="benchmark manual: rode com DAT_BENCH=1 (demora minutos)",
)


def test_benchmark_1m_experiments(tmp_path):
    from app.domain.entities import DistributionSpec, SamplingRequest
    from app.infrastructure.distribution_registry import build_default_registry
    from app.infrastructure.experiment_repository import ExperimentRepository
    from app.services.sampling_service import SamplingService

    service = SamplingService(build_default_registry())
    request = SamplingRequest(
        var_ids=[1, 10002],
        specs={
            1: DistributionSpec(provider="scipy", name="norm", params={"loc": 20, "scale": 4}),
            10002: DistributionSpec(provider="fixed", name="value", params={"value": 1.0}),
        },
        n_experiments=1_000_000,
        seed=7,
        strategy="lhs",
    )

    t0 = time.perf_counter()
    result = service.run(request)
    t_sample = time.perf_counter() - t0

    repo = ExperimentRepository(str(tmp_path / "bench.db"))
    repo.create_batch("bench", method="lhs", seed=7, n_experiments=1_000_000)

    t1 = time.perf_counter()
    repo.insert_result("bench", result.var_ids, result.matrix)
    t_insert = time.perf_counter() - t1

    t2 = time.perf_counter()
    total = repo.count()
    page = repo.fetch_page(999_000, 1000, result.var_ids)
    t_read = time.perf_counter() - t2

    assert total == 1_000_000
    assert len(page) == 1000
    print(
        f"\n[1M benchmark] amostragem={t_sample:.2f}s "
        f"insert={t_insert:.2f}s read-page={t_read:.3f}s"
    )
    # teto de sanidade (máquina dev varia): nada acima de 10 min
    assert t_sample < 600
    assert t_insert < 600
    repo.close()
