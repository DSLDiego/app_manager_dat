"""Painel de tarefas (fila persistente):pause/resume/cancel."""

from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QHBoxLayout,
    QProgressBar,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from app.domain.tasks import TaskState


class TasksPanel(QWidget):
    """Classe `TasksPanel` do módulo."""
    pauseRequested = Signal(int)
    resumeRequested = Signal(int)
    cancelRequested = Signal(int)

    def __init__(self, repo, parent=None):
        """Método `TasksPanel.__init__`.
            Parâmetros: `self`, `repo`, `parent`."""
        super().__init__(parent)
        self.repo = repo

        layout = QVBoxLayout(self)
        layout.setContentsMargins(6, 3, 6, 3)
        layout.setSpacing(2)

        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels(
            ["id", "tipo", "status", "progresso", "erro"]        )
        self.table.verticalHeader().setVisible(False)
        layout.addWidget(self.table)

        bar = QHBoxLayout()
        self.btn_pause = QPushButton("Pausar")
        self.btn_resume = QPushButton("Retomar")
        self.btn_cancel = QPushButton("Cancelar")
        bar.addWidget(self.btn_pause)
        bar.addWidget(self.btn_resume)
        bar.addWidget(self.btn_cancel)
        bar.addStretch()
        layout.addLayout(bar)

        self.btn_pause.clicked.connect(self._emit(self.pauseRequested))
        self.btn_resume.clicked.connect(self._emit(self.resumeRequested))
        self.btn_cancel.clicked.connect(self._emit(self.cancelRequested))
        self.refresh()

    def _emit(self, signal):
        """Método `TasksPanel._emit`.
            Parâmetros: `self`, `signal`.
            Retorna o resultado calculado a partir do estado local."""
        def inner():
            """Função `inner`."""
            row = self.table.currentRow()
            if row < 0:
                return
            task_id = int(self.table.item(row, 0).text())
            signal.emit(task_id)
        return inner

    def add_task_row(self, task_id: int, kind: str, state: str):
        """Método `TasksPanel.add_task_row`.
            Parâmetros: `self`, `task_id`, `kind`, `state`."""
        self.refresh()

    def update_task_progress(self, task_id: int, percent: int, message: str):
        """Método `TasksPanel.update_task_progress`.
            Parâmetros: `self`, `task_id`, `percent`, `message`."""
        self.refresh()

    def refresh(self):
        """Método `TasksPanel.refresh`.
            Parâmetros: `self`."""
        if self.repo is None:
            return
        tasks = self.repo.list_all()
        self.table.setRowCount(len(tasks))
        for r, task in enumerate(tasks):
            values = [
                str(task.id),
                getattr(task.kind, "value", str(task.kind)),
                getattr(task.state, "value", str(task.state)),
                str(task.progress) + "%",
                task.error or "",
            ]
            for c, v in enumerate(values):
                item = QTableWidgetItem(v)
                if "running" in v.lower() and c == 2:
                    item.setBackground(self.table.palette().window())
                self.table.setItem(r, c, item)
