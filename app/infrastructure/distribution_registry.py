from __future__ import annotations

from typing import Dict, List, Optional, Tuple

from app.domain.entities import DistributionSpec
from app.infrastructure.providers.base import BaseDistributionProvider
from app.infrastructure.providers.fixed_provider import FixedProvider
from app.infrastructure.providers.scipy_provider import ScipyProvider
from app.infrastructure.providers.triangular_provider import TriangularProvider


class DistributionRegistry:
    """Registro extensível. Novos providers podem ser plugados em runtime."""

    def __init__(self):
        """Método `DistributionRegistry.__init__`.
            Parâmetros: `self`."""
        self._providers: Dict[str, BaseDistributionProvider] = {}

    def register(self, provider: BaseDistributionProvider) -> None:
        """Método `DistributionRegistry.register`.
            Parâmetros: `self`, `provider`."""
        self._providers[provider.provider_name] = provider

    def remove(self, provider_name: str) -> None:
        """Método `DistributionRegistry.remove`.
            Parâmetros: `self`, `provider_name`."""
        self._providers.pop(provider_name, None)

    def get_provider(self, name: str) -> BaseDistributionProvider:
        """Método `DistributionRegistry.get_provider`.
            Parâmetros: `self`, `name`.
            Retorna o resultado calculado a partir do estado local.
            Levanta: KeyError."""
        if name not in self._providers:
            raise KeyError(f"Provider desconhecido: {name}")
        return self._providers[name]

    def get(self, name: str) -> Optional[BaseDistributionProvider]:
        """Alias tolerante para get_provider (retorna None se ausente)."""
        return self._providers.get(name)

    def provider_names(self) -> List[str]:
        """Método `DistributionRegistry.provider_names`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        return sorted(self._providers.keys())

    def list_all(self) -> List[Tuple[str, str]]:
        """Método `DistributionRegistry.list_all`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        result: List[Tuple[str, str]] = []
        for pname, prov in self._providers.items():
            for dname in prov.list_distributions():
                result.append((pname, dname))
        return sorted(result)

    @staticmethod
    def get_spec_code(provider: str, dist: str) -> str:
        """Método `DistributionRegistry.get_spec_code`.
            Parâmetros: `provider`, `dist`.
            Retorna o resultado calculado a partir do estado local."""
        return f"{provider}.{dist}"

    @staticmethod
    def parse_code(code: str) -> DistributionSpec:
        """Método `DistributionRegistry.parse_code`.
            Parâmetros: `code`.
            Retorna o resultado calculado a partir do estado local."""
        provider, _, name = code.partition(".")
        return DistributionSpec(provider=provider, name=name, params={})

    def sample(self, spec: DistributionSpec, size, rng):
        """Método `DistributionRegistry.sample`.
            Parâmetros: `self`, `spec`, `size`, `rng`.
            Retorna o resultado calculado a partir do estado local."""
        return self.get_provider(spec.provider).sample(spec, size, rng)

    def ppf(self, spec: DistributionSpec, u):
        """Método `DistributionRegistry.ppf`.
            Parâmetros: `self`, `spec`, `u`.
            Retorna o resultado calculado a partir do estado local."""
        return self.get_provider(spec.provider).ppf(spec, u)

    def validate(self, spec: DistributionSpec) -> List[str]:
        """Método `DistributionRegistry.validate`.
            Parâmetros: `self`, `spec`.
            Retorna o resultado calculado a partir do estado local."""
        return self.get_provider(spec.provider).validate(spec)


def build_default_registry() -> DistributionRegistry:
    """Função `build_default_registry`.
        Retorna o resultado calculado a partir do estado local."""
    reg = DistributionRegistry()
    reg.register(ScipyProvider())
    reg.register(FixedProvider())
    reg.register(TriangularProvider())
    return reg


def build_registry(plugins_dir=None) -> DistributionRegistry:
    """Registry completo: builtin + plugins de um diretório (usada em subprocessos)."""
    reg = build_default_registry()
    if plugins_dir is not None:
        from app.infrastructure.plugins.loader import PluginLoader

        PluginLoader(plugins_dir).register_all(reg)
    return reg

