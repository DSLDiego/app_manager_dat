"""Dialog de plugins: providers carregados, relatório e recarga a quente (r27)."""

from __future__ import annotations

from PySide6.QtWidgets import (
    QDialog,
    QHBoxLayout,
    QListWidget,
    QListWidgetItem,
    QPlainTextEdit,
    QPushButton,
    QVBoxLayout,
)


class PluginsDialog(QDialog):
    """Classe `PluginsDialog` do módulo."""
    def __init__(self, registry, plugin_report, parent=None, plugin_loader=None):
        """Método `PluginsDialog.__init__`.
            Parâmetros: `self`, `registry`, `plugin_report`, `parent`, `plugin_loader`."""
        super().__init__(parent)
        self.setWindowTitle("Plugins & Providers")
        self.setMinimumSize(600, 400)
        self.registry = registry
        self.plugin_loader = plugin_loader

        layout = QVBoxLayout(self)
        self.list = QListWidget()
        layout.addWidget(self.list)

        self.report = QPlainTextEdit()
        self.report.setReadOnly(True)
        layout.addWidget(self.report)

        bar = QHBoxLayout()
        self.btn_reload = QPushButton("Recarregar plugins")
        self.btn_reload.setToolTip(
            "Remove providers de arquivos da pasta plugins/ e recarrega do disco."
        )
        self.btn_close = QPushButton("Fechar")
        self.btn_close.clicked.connect(self.accept)
        bar.addWidget(self.btn_reload)
        bar.addStretch()
        bar.addWidget(self.btn_close)
        layout.addLayout(bar)

        self.btn_reload.clicked.connect(self._reload)
        self._populate(plugin_report)

    # ---------- helpers ----------
    def _populate(self, plugin_report):
        """Método `PluginsDialog._populate`.
            Parâmetros: `self`, `plugin_report`."""
        self.list.clear()
        for name in self.registry.provider_names():
            provider = self.registry.get(name)
            item = QListWidgetItem(f"{name} — {provider.__class__.__name__}")
            self.list.addItem(item)
        lines: list[str] = []
        if plugin_report:
            for plugin in getattr(plugin_report, "loaded", []):
                lines.append(f"OK: {plugin.path.name} → {plugin.provider_class.provider_name}")
            for plugin in getattr(plugin_report, "failed", []):
                lines.append(f"FALHA: {plugin.path.name} — {plugin.error}")
        self.report.setPlainText("\n".join(lines))

    def _reload(self):
        """Método `PluginsDialog._reload`.
            Parâmetros: `self`."""
        if self.plugin_loader is None:
            self.report.setPlainText(
                self.report.toPlainText() + "\nRecarga indisponível (sem loader)."
            )
            return
        new_report = self.plugin_loader.reload_all(self.registry)
        self._populate(new_report)
        names = [p.provider_class.provider_name for p in new_report.loaded]
        self.setWindowTitle(
            f"Plugins & Providers — {len(names)} recarregados"
        )