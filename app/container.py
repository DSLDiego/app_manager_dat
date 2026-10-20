"""Container DI — um único lugar para montar tudo."""

from __future__ import annotations

from pathlib import Path

from app.infrastructure.async_log_repository import AsyncLogRepository
from app.infrastructure.distribution_registry import (
    DistributionRegistry,
    build_default_registry,
)
from app.infrastructure.event_bus import EventBus
from app.infrastructure.experiment_repository import ExperimentRepository
from app.infrastructure.plugins.loader import PluginLoader
from app.infrastructure.template_repository import TemplateRepository
from app.services.log_service import LogService
from app.services.sampling_cache import SamplingCache
from app.services.sampling_service import SamplingService


class Container:
    """Classe `Container` do módulo."""
    def __init__(self, base_dir=str(Path.cwd()), load_plugins: bool = False):
        """Método `Container.__init__`.
            Parâmetros: `self`, `base_dir`, `load_plugins`."""
        base = Path(base_dir)
        base.mkdir(parents=True, exist_ok=True)

        self.base_dir = base

        self.event_bus = EventBus()
        self.log_repo = AsyncLogRepository(str(base / "logs" / "studio_logs.db"))
        self.log_repo.purge_old(days=30)  # retenção automática
        self.registry: DistributionRegistry = build_default_registry()
        self.sampling_cache = SamplingCache(max_entries=8)
        self.sampling_service = SamplingService(self.registry, cache=self.sampling_cache)
        self.log_service = LogService(self.event_bus, self.log_repo)

        self.exp_repo = ExperimentRepository(str(base / "data" / "experiments.db"))
        self.template_repo = TemplateRepository(str(base / "data" / "templates.db"))

        from app.infrastructure.study_repository import StudyRepository
        from app.services.study_service import StudyService

        self.study_repo = StudyRepository(str(base / "data" / "studies.db"))
        self.study_service = StudyService(self.study_repo)

        self.template_service = None
        self.comparison_service = None
        self.batch_comparison_service = None
        self.statistics_service = None
        self.batch_export_service = None
        self.metrics_service = None

        self.plugin_report = None
        self.plugin_loader = None
        if load_plugins:
            loader = PluginLoader(base / "plugins")
            self.plugin_report = loader.register_all(self.registry)
            self.plugin_loader = loader

    def ensure_services(self):
        """Cria serviços que dependem de repos (lazy, custo baixo)."""
        if self.template_service is None:
            from app.services.batch_comparison_service import (
                BatchComparisonService,
            )
            from app.services.batch_export_service import BatchExportService
            from app.services.comparison_service import ComparisonService
            from app.services.correlation_service import (
                CorrelationService,
            )
            from app.services.metrics_service import MetricsService
            from app.services.statistics_service import (
                StatisticsService,
            )
            from app.services.template_service import TemplateService

            self.template_service = TemplateService(self.template_repo)
            self.comparison_service = ComparisonService(self.exp_repo)
            self.batch_comparison_service = BatchComparisonService(self.exp_repo)
            self.statistics_service = StatisticsService()
            self.correlation_service = CorrelationService()
            self.batch_export_service = BatchExportService(self.exp_repo, self.template_repo)
            self.metrics_service = MetricsService(self.exp_repo, self.template_repo.conn, self.log_repo)
        return self

    def shutdown(self):
        """Método `Container.shutdown`.
            Parâmetros: `self`."""
        self.log_repo.close()
        self.exp_repo.close()
        self.template_repo.close()
        self.study_repo.close()
