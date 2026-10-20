"""Regressão da rodada 27: plugins hot-reload, schema tipado, helper."

Cobre T5131 (recarregar a quente) e T5132 (param_schema tipado).
"""

import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import pytest
from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QApplication, QDialogButtonBox, QDoubleSpinBox, QSpinBox

from app.container import Container
from app.ui.main_window import MainWindow


@pytest.fixture(scope="module")
def qapp():
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    return app


# ---------- T5132: schema tipado ----------

def test_base_provider_param_schema_default_empty(qapp):
    from app.infrastructure.providers.base import BaseDistributionProvider

    class DummyProvider(BaseDistributionProvider):
        provider_name = "dummy"

        def list_distributions(self):
            return ["value"]

        def parameter_names(self, dist_name):
            return []

        def sample(self, spec, size, rng):
            return None

        def validate(self, spec):
            return []

    assert DummyProvider().param_schema("value") == []
    # contrato genérico: deriva de parameter_names com float/default
    class Dummy3(BaseDistributionProvider):
        provider_name = "dummy3"

        def list_distributions(self):
            return ["value"]

        def parameter_names(self, dist_name):
            return ["alpha", "beta"]

        def sample(self, spec, size, rng):
            return None

        def validate(self, spec):
            return []

    schema = Dummy3().param_schema("value")
    assert schema == [
        {"name": "alpha", "type": "float", "default": 1.0},
        {"name": "beta", "type": "float", "default": 1.0},
    ]


def test_triangular_provider_param_schema(qapp):
    from app.infrastructure.providers.triangular_provider import TriangularProvider

    schema = TriangularProvider().param_schema("value")
    names = [p["name"] for p in schema]
    assert names == ["low", "mode", "high"]
    assert all(p.get("type") == "float" for p in schema)
    assert schema[1]["default"] == 1.0


def test_distribution_dialog_typed_fields_int(qapp):
    from app.infrastructure.providers import BaseDistributionProvider
    from app.ui.widgets.distribution_dialog import DistributionDialog
    from app.infrastructure.distribution_registry import DistributionRegistry

    class SchemaProvider(BaseDistributionProvider):
        provider_name = "esquema"
        description = "provider com schema"

        def list_distributions(self):
            return ["value"]

        def parameter_names(self, dist_name):
            return ["fator", "n_eixos"]

        def sample(self, spec, size, rng):
            return None

        def validate(self, spec):
            return []

        def param_schema(self, dist_name):
            return [
                {"name": "fator", "default": 2.5, "type": "float"},
                {"name": "n_eixos", "default": 3, "type": "int"},
            ]

    registry = DistributionRegistry()
    registry.register(SchemaProvider())
    dlg = DistributionDialog(registry, 10001, None)
    dlg.combo_provider.setCurrentText("esquema")
    dlg.combo_dist.setCurrentText("value")  # dispara rebuild
    kinds = [type(w).__name__ for w in dlg._widgets]
    assert kinds == ["QDoubleSpinBox", "QSpinBox"]
    vals = dlg.collect()
    assert vals.params == {"fator": 2.5, "n_eixos": 3}
    # coleta int
    dlg._widgets[1].setValue(7)
    assert dlg.collect().params["n_eixos"] == 7
    assert isinstance(dlg.collect().params["n_eixos"], int)
    dlg.close()


def test_distribution_dialog_prefill_params(qapp):
    from app.infrastructure.distribution_registry import DistributionRegistry
    from app.infrastructure.providers.triangular_provider import TriangularProvider
    from app.domain.entities import DistributionSpec
    from app.ui.widgets.distribution_dialog import DistributionDialog

    registry = DistributionRegistry()
    registry.register(TriangularProvider())
    spec = DistributionSpec(provider="triangular", name="value",
                            params={"low": 1.0, "mode": 2.0, "high": 5.0})
    dlg = DistributionDialog(registry, 10001, spec)
    dlg.combo_provider.setCurrentText("triangular")
    dlg.combo_dist.setCurrentText("value")
    values = {w._param_name: w.value() for w in dlg._widgets}
    assert values == {"low": 1.0, "mode": 2.0, "high": 5.0}
    dlg.close()


# ---------- T5131: reload a quente ----------

def _plugin_dir(tmp_path, content_suffix=""):
    plug_dir = tmp_path / "plugins27"
    plug_dir.mkdir(exist_ok=True)
    (plug_dir / "plg_a.py").write_text(
        "from app.infrastructure.providers.base import BaseDistributionProvider\n"
        "class ProvA(BaseDistributionProvider):\n"
        "    provider_name = 'prov_a'\n"
        f"    description = 'meu plugin {content_suffix}'\n"
        "    def list_distributions(self): return ['value']\n"
        "    def parameter_names(self, d): return ['x']\n"
        "    def sample(self, s, n, rng): return rng.uniform(0, 1, n)\n"
        "    def validate(self, s): return []\n",
        encoding="utf-8")
    return plug_dir


def test_plugin_loader_reload(tmp_path, qapp):
    from app.infrastructure.distribution_registry import DistributionRegistry
    from app.infrastructure.plugins.loader import PluginLoader

    plug_dir = _plugin_dir(tmp_path)
    registry = DistributionRegistry()
    registry.register(type("Builtin", (), {"provider_name": "builtin_x"}))

    loader = PluginLoader(plug_dir)
    report = loader.register_all(registry)
    assert "prov_a" in registry.provider_names()
    assert "builtin_x" in registry.provider_names()

    # reload: builtin permanece, plugin volta ao vivo
    report2 = loader.reload_all(registry)
    assert "prov_a" in registry.provider_names()
    assert "builtin_x" in registry.provider_names()
    assert len(report2.loaded) == 1
    assert loader._last_report is report2

    # plugin editado no disco: descrição atualiza após reload
    _plugin_dir(tmp_path, content_suffix="v2")
    loader.reload_all(registry)
    assert "meu plugin v2" == registry.get("prov_a").description


def test_main_window_plugins_menu_action(tmp_path, qapp):
    container = Container(base_dir=str(tmp_path / "c27a"), load_plugins=False)
    QSettings("datstudio", "dtengine").remove("recent/files")
    try:
        window = MainWindow(container)
        acts = []
        for menu_action in window.menuBar().actions():
            sub = menu_action.menu()
            if sub is not None:
                acts.extend(a.text() for a in sub.actions())
        assert "Plugins & Providers…" in acts
        window.close()
    finally:
        QSettings("datstudio", "dtengine").remove("recent/files")


def test_container_keeps_plugin_loader(tmp_path):
    container = Container(base_dir=str(tmp_path / "c27b"), load_plugins=True)
    try:
        assert container.plugin_loader is not None
        assert container.plugin_report is not None
    finally:
        container.shutdown()
