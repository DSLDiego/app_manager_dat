# Arquitetura — DAT Engineering Studio

Visão geral (mermaid). A UI não fala com SQL/scipy diretamente: só services e workers.

```mermaid
flowchart LR
    subgraph UI["UI (PySide6)"]
        MW[MainWindow] --> ET[EditorTabs]
        MW --> VP[VariablesPanel]
        MW --> PP[PreviewPanel]
        MW --> LP[LogsPanel]
        MW --> EP[ExperimentsPanel]
        MW --> DLG[Dialogs/Widgets]
    end

    subgraph SERVICES["Services (puros, testáveis)"]
        SS[SamplingService]
        TS[TemplateService]
        CS[ComparisonService]
        BCS[BatchComparisonService]
        STST[StatisticsService]
        COP[CorrelationService]
        BES[BatchExportService]
        MS[MetricsService]
        SCH[TaskScheduler]
    end

    subgraph INFRA["Infrastructure"]
        REG[DistributionRegistry + Providers]
        EDB[(experiments.db)]
        TDB[(templates.db)]
        LDB[(logs.db)]
        TTB[(tasks.db)]
        BUS[EventBus]
        PLG[PluginLoader]
        API[ApiServer]
    end

    subgraph WORKERS["Workers (QThread)"]
        SW[SamplingWorker]
        EW[ExportWorker]
        BEW[BatchExportWorker]
        TW[TaskWorker]
    end

    UI -->|"sinais"| WORKERS
    WORKERS --> SERVICES
    SERVICES --> INFRA
    VP --> DLG
    DLG --> REG
    UI -->|"queries paginadas"| EDB
    INFRA -->|"LogCreatedEvent..."| BUS
    BUS -->|ControlEvents| UI
```

## Namespaces de variáveis

- `$1` → var_id `1`
- `$var1` / `$v1` / `$V1` → var_id `10000 + n` (`VAR_PREFIX_OFFSET`)
- Cada id é uma variável aleatória independente, com sua própria distribuição.

## Decisões relevantes

1. **Amostragem vetorizada**: uma chamada por variável (não por experimento). Suporta MC, LHS, Sobol e correlacionada (Iman-Conover).
2. **Export em lote**: paginação SQLite + tempo O(page), checkpoint por página e cancelamento cooperativo.
3. **Logs assíncronos**: fila em thread de background; leitura nunca bloqueia; `wait_pending()` drena para leituras determinísticas.
4. **Plugins**: `PluginLoader` carrega providers de `plugins/*.py`; subprocessos reconstruem o registry com `build_registry(plugins_dir)`.
