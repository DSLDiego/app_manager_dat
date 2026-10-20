"""Base de workers: guarda referência ao último worker ativo."""

from __future__ import annotations

from PySide6.QtCore import QThread


class BaseWorker(QThread):
    """Classe-base; subclasses definem o método run de fato."""

    def run(self):
        """Método `BaseWorker.run`.
            Parâmetros: `self`.
            Levanta: NotImplementedError."""
        raise NotImplementedError
