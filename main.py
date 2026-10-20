"""Entrada da aplicação: cria QApplication + Container + MainWindow."""

from __future__ import annotations

import platform
import sys


def main(modules: list = []):
    """Ponto de entrada. `modules` mantido p/ compatibilidade de testes."""
    from PySide6.QtWidgets import QApplication
    from sys import argv as _unused

    from app import APP_NAME
    from app.container import Container
    from app.ui.main_window import MainWindow


    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)

    container = Container()
    window = MainWindow(container)
    window.show()

    exit_code = app.exec()
    container.shutdown()
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
