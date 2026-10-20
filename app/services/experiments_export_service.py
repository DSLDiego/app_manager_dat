"""Export CSV dos experimentos paginados (todas as páginas, com filtro opcional)."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Optional

from app.core.parsing import var_label
from app.infrastructure.experiment_repository import ExperimentRepository


def export_experiments_csv(
    repo: ExperimentRepository,
    path,
    var_ids: Optional[list[int]] = None,
    page_size: int = 1000,
) -> int:
    """Grava CSV largo ('experimento' + $var por coluna). Retorna nº de linhas."""
    shown = var_ids if var_ids else repo.var_ids()
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    total_rows = 0

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["experimento"] + [var_label(v) for v in shown])

        page = 0
        while True:
            rows = repo.fetch_page(page, page_size, shown)
            if not rows:
                break
            for row in rows:
                writer.writerow(
                    [row["external_id"]]
                    + [row["values"].get(v, "") for v in shown]
                )
                total_rows += 1
            page += 1

    return total_rows
