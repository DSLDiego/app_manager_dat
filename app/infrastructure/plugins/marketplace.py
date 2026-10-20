"""Marketplace local de templates de provider (v1).

Pasta `plugins/marketplace/` com snippets `.py` listados, instaláveis no
código, com os `plugins/` chave do PluginLoader. Sem rede: cópia local.
"""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Optional

MARKET_TEMPLATE = """# Template de provider — {name}
# Edite e regnifique nos plugins/: implemente provider_name,
# list_distributions, parameter_names, sample, ppf, validate, param_schema.

from __future__ import annotations

from typing import List

import numpy as np

from app.infrastructure.providers.base import BaseDistributionProvider


class {class_name}(BaseDistributionProvider):
    \"\"\"Provider gerado a partir do marketplace local.\"\"\"

    provider_name = "{key}"

    def list_distributions(self) -> List[str]:
        return ["custom"]

    def parameter_names(self, dist_name: str) -> List[str]:
        return ["loc", "scale"]

    def ppf(self, spec, u: np.ndarray) -> np.ndarray:
        params = spec.params
        loc = float(params.get("loc", 0.0))
        scale = float(params.get("scale", 1.0))
        return loc + scale * np.asarray(u, dtype=float)

    def sample(self, spec, size: int, rng: np.random.Generator) -> np.ndarray:
        u = rng.random(size)
        return self.ppf(spec, u)
"""


def safe_name(name: str) -> str:
    """Nome sanitizado para arquivo de marketplace (puro)."""
    keep = "".join(c if (c.isalnum() or c in "_-") else "_" for c in str(name or "").strip().lower())
    return keep or "provider_template"


def marketplace_dir(base_dir) -> Path:
    """Pasta padrão `plugins/marketplace` sob o projeto."""
    return Path(base_dir) / "plugins" / "marketplace"


def list_templates(market_dir) -> list[dict]:
    """Templates disponíveis: [{file, name, size_bytes}]."""
    base = Path(market_dir)
    if not base.exists():
        return []
    out = []
    for f in sorted(base.glob("*.py")):
        out.append({
            "file": f.name,
            "name": f.stem,
            "size_bytes": f.stat().st_size,
        })
    return out


def create_template(market_dir, name: str, key: Optional[str] = None) -> Path:
    """Cria um snippet novo de provider no marketplace. Retorna o caminho."""
    base = Path(market_dir)
    base.mkdir(parents=True, exist_ok=True)
    safe = safe_name(name)
    path = base / f"{safe}.py"
    class_name = "Provider" + "".join(p.capitalize() for p in safe.split("_")[:3])
    path.write_text(
        MARKET_TEMPLATE.format(name=name, key=key or safe, class_name=class_name),
        encoding="utf-8",
    )
    return path


def install_template(market_dir, name: str, plugins_dir) -> Path:
    """Copia `marketplace/<name>.py` para `plugins/` (carregável a quente)."""
    src = Path(market_dir) / f"{safe_name(name)}.py"
    if not src.exists():
        raise FileNotFoundError(f"template não encontrado: {src}")
    dest = Path(plugins_dir) / src.name
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dest)
    return dest
