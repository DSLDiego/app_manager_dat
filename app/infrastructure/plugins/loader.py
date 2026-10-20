"""Sistema de plugins: hot-load de providers externos."""

from __future__ import annotations

import importlib.util
import sys
import traceback
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Tuple, Type

from app.infrastructure.providers.base import BaseDistributionProvider


@dataclass(frozen=True)
class LoadedPlugin:
    """Classe `LoadedPlugin` do módulo."""
    path: Path
    provider_class: Type[BaseDistributionProvider]
    ok: bool = True
    error: str = ""


@dataclass
class PluginLoadReport:
    """Classe `PluginLoadReport` do módulo."""
    loaded: List[LoadedPlugin] = field(default_factory=list)
    failed: List[LoadedPlugin] = field(default_factory=list)

    def collect(self) -> List[LoadedPlugin]:
        """Método `PluginLoadReport.collect`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        return self.loaded + self.failed


class PluginLoader:
    """Hot-load de providers a partir de arquivos .py."""

    def __init__(self, plugins_dir):
        """Método `PluginLoader.__init__`.
            Parâmetros: `self`, `plugins_dir`."""
        self.plugins_dir = Path(plugins_dir)
        self._already_loaded = set()
        self._plugin_names: set = set()  # r27: nomes registrados por plugins
        self._last_report = None

    def discover(self) -> PluginLoadReport:
        """Método `PluginLoader.discover`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        report = PluginLoadReport()
        if not self.plugins_dir.exists():
            return report

        for file in sorted(self.plugins_dir.glob("*.py")):
            if file.name.startswith("_"):
                continue

            for cls, err in self._load_file(file):
                plugin = LoadedPlugin(path=file, provider_class=cls, ok=not err, error=err)
                if err:
                    report.failed.append(plugin)
                else:
                    report.loaded.append(plugin)
                    self._already_loaded.add(file)

        return report

    def _load_file(self, file: Path) -> List[Tuple[Type[BaseDistributionProvider], str]]:
        """Método `PluginLoader._load_file`.
            Parâmetros: `self`, `file`.
            Retorna o resultado calculado a partir do estado local."""
        module_name = f"user_plugin_{file.stem}"
        results: List[Tuple[Type[BaseDistributionProvider], str]] = []

        try:
            spec = importlib.util.spec_from_file_location(module_name, file)
            if spec is None or spec.loader is None:
                results.append((None, "Não foi possível carregar o módulo"))
                return results

            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)
        except Exception as exc:
            traceback.print_exc()
            results.append((None, f"Erro ao executar: {exc}"))
            return results

        found = False
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if (
                isinstance(attr, type)
                and issubclass(attr, BaseDistributionProvider)
                and attr is not BaseDistributionProvider
                and getattr(attr, "provider_name", "")
            ):
                results.append((attr, ""))
                found = True

        if not found:
            results.append((None, "Nenhum provider encontrado"))

        return results

    def register_all(self, registry) -> PluginLoadReport:
        """Método `PluginLoader.register_all`.
            Parâmetros: `self`, `registry`.
            Retorna o resultado calculado a partir do estado local."""
        report = self.discover()
        survivors: List[LoadedPlugin] = []
        for plugin in report.loaded:
            try:
                registry.register(plugin.provider_class())
                self._plugin_names.add(plugin.provider_class().provider_name)
                survivors.append(plugin)
            except Exception as exc:
                report.failed.append(
                    LoadedPlugin(path=plugin.path, provider_class=plugin.provider_class,
                                 ok=False, error=str(exc))
                )
        report.loaded = survivors
        return report

    def reload_all(self, registry) -> PluginLoadReport:
        """r27: recarga a quente — remove os providers de plugins e recarrega.

        Providers builtin (não-plugin) não são afetados.
        """
        for name in sorted(self._plugin_names):
            registry.remove(name)
        self._plugin_names.clear()
        self._already_loaded.clear()
        self._last_report = self.register_all(registry)
        return self._last_report
