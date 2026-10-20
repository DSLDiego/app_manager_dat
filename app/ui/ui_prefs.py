"""Preferências de UI lembradas entre sessões (QSettings "datstudio/dtengine").

save_ui_choice/load_ui_choice são finos sobre QSettings — teste usa chaves
únicas e limpa no finally.
"""

from __future__ import annotations

from PySide6.QtCore import QSettings

ORG = "datstudio"
APP = "dtengine"


def _settings() -> QSettings:
    """Função `_settings`.
        Retorna o resultado calculado a partir do estado local."""
    return QSettings(ORG, APP)


def save_ui_choice(key: str, value):
    """Função `save_ui_choice`.
        Parâmetros: `key`, `value`."""
    _settings().setValue(f"ui/{key}", value)


def load_ui_choice(key: str, default=None):
    """Função `load_ui_choice`.
        Parâmetros: `key`, `default`.
        Retorna o resultado calculado a partir do estado local."""
    value = _settings().value(f"ui/{key}", default)
    if value is None:
        return default
    return value


def drop_ui_choice(key: str):
    """Função `drop_ui_choice`.
        Parâmetros: `key`."""
    _settings().remove(f"ui/{key}")
