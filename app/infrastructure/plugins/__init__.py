"""Sistema de plugins (hot-load de providers)."""

from app.infrastructure.plugins.loader import LoadedPlugin, PluginLoadReport, PluginLoader

__all__ = ["LoadedPlugin", "PluginLoadReport", "PluginLoader"]
