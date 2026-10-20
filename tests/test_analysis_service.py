"""Testes de comparação, estatísticas, metrics e serviços derivados."""

import numpy as np
import pytest


def test_comparison_service(container, populated_batch):
    svc = container.comparison_service
    result = svc.compare(1, 2, template_text="TEMP $1 V2", renderer=lambda t, v: t.replace("$1", "1"))
    assert result.exp_a_id == 1
    diffs = {d.var_id: d for d in result.diffs}
    assert 1 in diffs and 10002 in diffs
    assert diffs[10002].abs_diff == 0.0  # fixed value igual entre experimentos


def test_batch_comparison_service(container, populated_batch):
    container.exp_repo.create_batch("batch_y", "lhs", 8, 12)
    values = container.exp_repo.fetch_page(0, 12, [1, 10002])
    new_matrix = [[row["values"][1] * 1.5, row["values"][10002]] for row in values]
    container.exp_repo.insert_result("batch_y", [1, 10002], new_matrix)

    cmp = container.batch_comparison_service.compare("batch_x", "batch_y")
    assert cmp.n_a == 12
    var1 = next(v for v in cmp.variables if v.var_id == 1)
    assert var1.mean_b == pytest.approx(var1.mean_a * 1.5)
    assert var1.mean_delta_pct == pytest.approx(50.0)
    assert not np.isnan(var1.p50_a)


def test_statistics_service(container, populated_batch):
    values = container.exp_repo.get_variable_values(10002)
    stats = container.statistics_service.compute(10002, values)
    assert stats.count == 12
    assert stats.minimum == stats.maximum == 5.0
    assert not np.isnan(stats.p50)

    stats_empty = container.statistics_service.compute(3, [])
    assert np.isnan(stats_empty.mean)


def test_metrics_service(container, populated_batch, log_service=None):
    container.log_service.info("SAMPLING", "start", "x")
    summary = container.metrics_service.summary()
    assert summary.total_batches == 1
    assert summary.total_experiments == 12
    assert summary.total_versions == 1
    assert summary.total_logs >= 1
    assert summary.logs_24h >= 1

    per_batch = container.metrics_service.experiments_per_batch()
    assert per_batch == [("batch_x", 12)]


def test_preview_service_scales(container, populated_batch):
    from app.services.preview_service import PreviewService

    svc = PreviewService(container.sampling_service)
    specs = {
        1: __import__(
            "app.domain.entities", fromlist=["DistributionSpec"]
        ).DistributionSpec(provider="scipy", name="norm", params={"loc": 10, "scale": 2}),
    }
    values = svc.sample_one(specs, seed=42)
    assert 5 < values[1] < 15
    text = svc.render("RUNZ $1", specs, seed=42)
    assert "$1" not in text
