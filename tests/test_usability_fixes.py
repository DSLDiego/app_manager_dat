"""Regressões dos ajustes de usabilidade: amostragem completa, destino nos logs, limpar experimentos."""

from types import SimpleNamespace

import numpy as np
import pytest

pytest.importorskip("pytestqt")


def _repo(tmp_path):
    from app.infrastructure.experiment_repository import ExperimentRepository

    return ExperimentRepository(str(tmp_path / "exp.db"))


# ---------- 1) amostragem só cria experimento com TODAS as variáveis ----------
def test_sampling_service_raises_when_specs_missing():
    from app.domain.entities import DistributionSpec, SamplingRequest
    from app.infrastructure.distribution_registry import build_default_registry
    from app.services.sampling_service import SamplingService

    service = SamplingService(build_default_registry())
    request = SamplingRequest(
        var_ids=[1, 10002],
        specs={
            1: DistributionSpec(provider="fixed", name="value", params={"value": 1.0}),
        },
        n_experiments=5,
        seed=1,
        strategy="monte_carlo",
    )
    with pytest.raises(ValueError, match="Todas as variáveis"):
        service.run(request)


def test_sampling_service_raises_on_nonfinite_column(tmp_path):
    from app.domain.entities import DistributionSpec, SamplingRequest
    from app.infrastructure.distribution_registry import DistributionRegistry
    from app.infrastructure.providers.base import BaseDistributionProvider
    from app.infrastructure.distribution_registry import build_default_registry
    from app.services.sampling_service import SamplingService

    class NaNProvider(BaseDistributionProvider):
        provider_name = "nan"
        description = "sempre nan (fake de teste)"

        def list_distributions(self):
            return ["x"]

        def parameter_names(self, dist_name):
            return []

        def sample(self, spec, size, rng=None):
            return np.full(int(size), np.nan)

        def validate(self, spec):
            return []

        def ppf(self, spec, u):
            return np.full(len(np.atleast_1d(np.asarray(u))), np.nan)

    base = build_default_registry()
    registry = DistributionRegistry()
    registry._providers = dict(base._providers)
    registry.register(NaNProvider())
    service = SamplingService(registry)

    spec = DistributionSpec(provider="nan", name="x", params={})
    request = SamplingRequest(
        var_ids=[1, 10002],
        specs={
            1: DistributionSpec(provider="fixed", name="value", params={"value": 2.0}),
            10002: spec,
        },
        n_experiments=4,
        seed=3,
        strategy="monte_carlo",
    )
    with pytest.raises(ValueError, match="10002"):
        service.run(request)


def test_insert_result_rejects_ragged_rows(tmp_path):
    repo = _repo(tmp_path)
    repo.create_batch("b", "sampling", 1, 2)
    with pytest.raises(ValueError, match="Todas as variáveis"):
        repo.insert_result("b", [1, 10002], [[1.0, 2.0], [3.0]])  # segunda linha curta
    assert repo.count() == 0
    repo.close()


def test_find_incomplete_variables_matrix_semantics():
    from app.core.validation import find_incomplete_variables

    ok = SimpleNamespace(var_ids=[1, 2], matrix=[[1.0, 2.0], [3.0, 4.0]])
    assert find_incomplete_variables(ok) == []

    nan_col = SimpleNamespace(var_ids=[1, 10002], matrix=[[1.0, 2.0], [3.0, np.nan]])
    assert find_incomplete_variables(nan_col) == [10002]

    short = SimpleNamespace(var_ids=[1, 10002, 3], matrix=[[1.0, 2.0]])
    assert find_incomplete_variables(short) == [3]

    empty = SimpleNamespace(var_ids=[5], matrix=[])
    assert find_incomplete_variables(empty) == [5]

    inf = SimpleNamespace(var_ids=[7], matrix=[[float("inf")]])
    assert find_incomplete_variables(inf) == [7]


def test_main_window_refuses_incomplete_experiment(main_window_offscreen, qtbot, monkeypatch):
    from PySide6.QtWidgets import QMessageBox

    warned = []

    def fake_warning(parent, title, text):
        warned.append(text)
        return QMessageBox.StandardButton.Ok

    monkeypatch.setattr(QMessageBox, "warning", staticmethod(fake_warning))

    window = main_window_offscreen
    bad = SimpleNamespace(
        var_ids=[1, 10002],
        matrix=[[1.0, 2.0], [3.0, np.nan]],
        seed_used=1,
        duration_seconds=0.0,
    )
    window._on_sampling_completed(bad)

    assert window.container.exp_repo.count() == 0
    assert window.container.exp_repo.list_batches() == []
    assert getattr(window, "last_sampling", None) is not bad
    assert warned and "10002" in warned[0]


def test_main_window_accepts_complete_experiment(main_window_offscreen, qtbot):
    window = main_window_offscreen
    good = SimpleNamespace(
        var_ids=[1, 10002],
        matrix=[[1.0, 2.0], [3.0, 4.0]],
        seed_used=1,
        duration_seconds=0.0,
    )
    window._on_sampling_completed(good)

    assert window.container.exp_repo.count() == 2
    assert len(window.container.exp_repo.list_batches()) == 1


# ---------- 2) coluna "destino" na tabela de logs ----------
def test_log_row_has_output_dir_column(log_repo, qtbot):
    from app.ui.widgets.logs_panel import LogsPanel

    log_repo.log(
        level="INFO",
        category="AUDIT",
        action="export.done",
        message="12 .dats gerados",
        payload={"output_dir": "C:\\erudit\\out\\v1"},
    )
    log_repo.wait_pending()

    panel = LogsPanel(log_repo)
    panel.refresh()
    assert panel.table.columnCount() == len(panel.COLUMNS)
    assert "DESTINO" in [panel.table.horizontalHeaderItem(c).text() for c in range(panel.table.columnCount())]
    assert panel.table.item(0, panel.COLUMNS.index("destino")).text() == "C:\\erudit\\out\\v1"


def test_parse_log_destino_fallbacks():
    from app.ui.widgets.logs_panel import parse_log_destino

    payload_row = {"payload_json": '{"output_dir": "D:\\\\x\\\\y"}'}
    assert parse_log_destino(payload_row) == "D:\\x\\y"

    message_row = {"payload_json": None, "message": "salvo em C:\\out\\batch"}
    assert parse_log_destino(message_row) == "C:\\out\\batch"

    nothing = {"payload_json": None, "message": "sem caminho aqui"}
    assert parse_log_destino(nothing) == ""

    broken = {"payload_json": "{não é json", "message": ""}
    assert parse_log_destino(broken) == ""


# ---------- 3) botão limpar tabela de experimentos ----------
def test_experiment_repository_clear_all(tmp_path):
    repo = _repo(tmp_path)
    repo.create_batch("b1", "sampling", 1, 3)
    repo.insert_result("b1", [1, 10002], [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
    assert repo.count() == 3
    assert repo.var_ids() == [1, 10002]

    removed_batches = repo.clear_all()
    assert removed_batches == 1
    assert repo.count() == 0
    assert repo.var_ids() == []
    assert repo.list_batches() == []
    assert repo.fetch_page(0, 10) == []

    # novo ciclo começa em external_id 1 novamente
    repo.create_batch("b2", "sampling", 7, 1)
    repo.insert_result("b2", [1], [[9.0]])
    rows = repo.fetch_page(0, 10, [1])
    assert rows[0]["external_id"] == 1
    assert rows[0]["values"] == {1: 9.0}
    repo.close()


def test_experiments_panel_has_clear_button(qtbot, tmp_path):
    from PySide6.QtWidgets import QApplication

    QApplication.instance() or QApplication([])
    from app.infrastructure.experiment_repository import ExperimentRepository
    from app.ui.models.repository_paged_model import RepositoryPagedModel
    from app.ui.widgets.experiments_panel import ExperimentsPanel

    repo = ExperimentRepository(str(tmp_path / "exp2.db"))
    model = RepositoryPagedModel(repo)
    panel = ExperimentsPanel(model)

    clicked = []
    panel.clearRequested.connect(lambda: clicked.append(True))
    panel._clear_button.click()
    assert clicked == [True]
    repo.close()
