"""Exportação paralela (I/O-bound) em ThreadPoolExecutor."""

from __future__ import annotations

from pathlib import Path
from typing import Callable, List, Optional

from PySide6.QtCore import Signal

from app.workers.base_worker import BaseWorker


class ExportWorker(BaseWorker):
    """Classe `ExportWorker` do módulo."""
    progress = Signal(int, str)
    completed = Signal(str)
    failed = Signal(str)

    def __init__(
        self,
        template: str,
        var_ids: List[int],
        matrix: List[List[float]],
        output_dir: str,
        io_workers: int = 8,
        renderer: Optional[Callable] = None,
        parent=None,
    ):
        """Método `ExportWorker.__init__`.
            Parâmetros: `self`, `template`, `var_ids`, `matrix`, `output_dir`, `io_workers`, `renderer`, `parent`."""
        super().__init__(parent)
        self.template = template
        self.var_ids = var_ids
        self.matrix = matrix
        self.output_dir = Path(output_dir)
        self.io_workers = io_workers
        self.renderer = renderer

    def run(self):
        """Método `ExportWorker.run`.
            Parâmetros: `self`."""
        try:
            from concurrent.futures import ThreadPoolExecutor, as_completed

            self.output_dir.mkdir(parents=True, exist_ok=True)
            total = len(self.matrix)
            done = 0

            with ThreadPoolExecutor(max_workers=self.io_workers) as pool:
                futures = [
                    pool.submit(self._write_one, i + 1, row)
                    for i, row in enumerate(self.matrix)
                ]
                for fut in as_completed(futures):
                    fut.result()
                    done += 1
                    if done % 10 == 0 or done == total:
                        self.progress.emit(int(100 * done / total), f"{done}/{total}")

            self.completed.emit(str(self.output_dir))
        except Exception as exc:
            import traceback

            traceback.print_exc()
            self.failed.emit(str(exc))

    def _write_one(self, exp_id: int, row: List[float]):
        """Método `ExportWorker._write_one`.
            Parâmetros: `self`, `exp_id`, `row`."""
        from app.core.parsing import render_template

        values = dict(zip(self.var_ids, row))
        text = self.renderer(self.template, values) if self.renderer else render_template(
            self.template, values
        )
        (self.output_dir / f"experimento_{exp_id:06d}.dat").write_text(
            text, encoding="utf-8",
        )
