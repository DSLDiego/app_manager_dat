"""Config pytest: path do projeto + fixtures de container/repositórios."""

import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


@pytest.fixture()
def registry():
    from app.infrastructure.distribution_registry import build_default_registry

    return build_default_registry()


@pytest.fixture()
def sampling_service(registry):
    from app.services.sampling_service import SamplingService

    return SamplingService(registry)


@pytest.fixture()
def repos(tmp_path):
    from app.infrastructure.experiment_repository import ExperimentRepository
    from app.infrastructure.template_repository import TemplateRepository

    exp = ExperimentRepository(str(tmp_path / "exp.db"))
    tpl = TemplateRepository(str(tmp_path / "tpl.db"))
    return {"exp": exp, "tpl": tpl}


@pytest.fixture()
def log_repo(tmp_path):
    from app.infrastructure.async_log_repository import AsyncLogRepository

    repo = AsyncLogRepository(str(tmp_path / "logs.db"))
    yield repo
    repo.close()


@pytest.fixture()
def log_service(log_repo):
    module = __import__("app.services.log_service", fromlist=["LogService"])
    return {"repo": log_repo, "svc": module.LogService(repo=log_repo)}


@pytest.fixture()
def container(tmp_path):
    from app.container import Container

    c = Container(base_dir=str(tmp_path), load_plugins=False)
    c.ensure_services()
    yield c
    c.shutdown()


@pytest.fixture()
def populated_batch(container):
    from app.domain.entities import DistributionSpec, SamplingRequest

    request = SamplingRequest(
        var_ids=[1, 10002],
        specs={
            1: DistributionSpec(provider="scipy", name="norm", params={"loc": 10.0, "scale": 2.0}),
            10002: DistributionSpec(provider="fixed", name="value", params={"value": 5.0}),
        },
        n_experiments=12,
        seed=7,
        strategy="lhs",
    )
    result = container.sampling_service.run(request)
    container.exp_repo.create_batch("batch_x", "lhs", 7, 12)
    container.exp_repo.insert_result("batch_x", result.var_ids, result.matrix)
    container.template_repo.create_template("t1")
    version_id = container.template_repo.save_version(1, "TEMP $1 $V2")
    return {"batch_id": "batch_x", "version_id": version_id}


@pytest.fixture()
def main_window_offscreen(tmp_path):
    """MainWindow pronta para uso em Qt offscreen."""
    from PySide6.QtWidgets import QApplication

    QApplication.instance() or QApplication([])

    from app.container import Container
    from app.ui.main_window import MainWindow

    container = Container(base_dir=str(tmp_path / "mw"), load_plugins=False)
    window = MainWindow(container)
    yield window
    window.close()
    container.shutdown()
