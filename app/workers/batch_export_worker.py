"""Worker para BatchExportService (queue de tarefas)."""

from __future__ import annotations

from typing import Dict, Optional

from PySide6.QtCore import Signal

from app.services.batch_export_service import BatchExportManifest, BatchExportService
from app.workers.base_worker import BaseWorker


class BatchExportWorker(BaseWorker):
    """Classe `BatchExportWorker` do módulo."""
    progress = Signal(int, str)
    completed = Signal(object)
    failed = Signal(str)

    def __init__(
        self,
        service: BatchExportService,
        batch_id: str,
        template_version_id: int,
        output_root: str,
        batch_meta: Optional[Dict] = None,
        stop_check=None,
        parent=None,
    ):
        """Método `BatchExportWorker.__init__`.
            Parâmetros: `self`, `service`, `batch_id`, `template_version_id`, `output_root`, `batch_meta`, `stop_check`, `parent`."""
        super().__init__(parent)
        self.service = service
        self.batch_id = batch_id
        self.template_version_id = template_version_id
        self.output_root = output_root
        self.batch_meta = batch_meta
        self.stop_check = stop_check

    def run(self):
        """Método `BatchExportWorker.run`.
            Parâmetros: `self`."""
        try:
            manifest = self.service.export(
                batch_id=self.batch_id,
                template_version_id=self.template_version_id,
                output_root=self.output_root,
                batch_meta=self.batch_meta,
                progress_cb=self.progress.emit,
                stop_check=self.stop_check,
            )
            self.completed.emit(manifest)
        except Exception as exc:
            import traceback

            traceback.print_exc()
            self.failed.emit(str(exc))
