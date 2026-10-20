"""Fluxo de uso guiado (checklist): etapas do app com saltos e status vivo.

Etapas: template → distribuições → amostragem → .dats → versão do template → estudos.
Puro em flow_model(); MainWindow conecta os botões aos handlers existentes.
"""

from __future__ import annotations

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

STEP_DONE = "✔"
STEP_PEND = "○"

FLOW_STEPS = [
    ("tpl", "Abrir ou criar o template .dat"),
    ("dist", "Definir distribuições das variáveis"),
    ("sample", "Amostrar experimentos"),
    ("dats", "Gerar os .dats (output)"),
    ("vers", "Salvar versão do template"),
    ("study", "Criar um estudo para reabrir"),
]


def flow_model(state: dict) -> list[tuple[str, str, bool]]:
    """[(step_id, texto, feito)…] — junta o ESTADO REAL do MainWindow às etapas."""
    state = state or {}
    checks = {
        "tpl": bool(state.get("template_hash") or state.get("dat_path")),
        "dist": bool(state.get("specs")),
        "sample": bool(state.get("sampling")),
        "dats": bool(state.get("output_dir")),
        "vers": bool(state.get("template_version_id")),
        "study": bool(state.get("has_studies")),
    }
    labels = dict(FLOW_STEPS)
    return [
        (sid, f"{STEP_DONE if checks[sid] else STEP_PEND}  {labels[sid]}", checks[sid])
        for sid, _ in FLOW_STEPS
    ]


def next_pending(state: dict) -> str | None:
    """Primeira etapa pendente (guia 1 clique)."""
    for sid, _, done in flow_model(state):
        if not done:
            return sid
    return None


class UsageFlowPanel(QWidget):
    """Checklist clicável — clique na etapa emite actionRequested(step_id)."""

    actionRequested = Signal(str)   # step_id
    statusMessage = Signal(str)

    def __init__(self, parent=None):
        """Método `UsageFlowPanel.__init__`.
            Parâmetros: `self`, `parent`."""
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(6, 3, 6, 3)
        layout.setSpacing(2)

        self.lbl_head = QLabel("Fluxo de uso:")
        layout.addWidget(self.lbl_head)

        self.list = QListWidget()
        self.list.setToolTip("✔ feito · ○ pendente — clique para executar a etapa.")
        self.list.itemClicked.connect(self._on_step_clicked)
        layout.addWidget(self.list, 1)

        bar = QHBoxLayout()
        self.btn_next_step = QPushButton("Ir para próxima pendente")
        self.btn_next_step.setToolTip("Executa a próxima etapa em falta no fluxo.")
        bar.addWidget(self.btn_next_step)
        bar.addStretch()
        layout.addLayout(bar)

        self.btn_next_step.clicked.connect(self._go_next)
        self.refresh({})

    # ---------- estado ----------
    def refresh(self, state: dict):
        """Método `UsageFlowPanel.refresh`.
            Parâmetros: `self`, `state`."""
        self._state = dict(state or {})
        model = flow_model(self._state)
        self.list.clear()
        for sid, text, _done in model:
            item = QListWidgetItem(text)
            item.setData(Qt.ItemDataRole.UserRole, sid)
            self.list.addItem(item)
        pend = next_pending(self._state)
        if pend is None:
            self.lbl_head.setText("Fluxo completo ✔")
        else:
            labels = dict(FLOW_STEPS)
            self.lbl_head.setText(f"Próxima etapa: {labels[pend]}")

    # ---------- ações ----------
    def _step_of_row(self, row: int) -> str | None:
        """Método `UsageFlowPanel._step_of_row`.
            Parâmetros: `self`, `row`.
            Retorna o resultado calculado a partir do estado local."""
        if 0 <= row < self.list.count():
            return str(self.list.item(row).data(Qt.ItemDataRole.UserRole))
        return None

    def _on_step_clicked(self, item: QListWidgetItem):
        """Método `UsageFlowPanel._on_step_clicked`.
            Parâmetros: `self`, `item`."""
        sid = str(item.data(Qt.ItemDataRole.UserRole))
        self.actionRequested.emit(sid)

    def _go_next(self):
        """Método `UsageFlowPanel._go_next`.
            Parâmetros: `self`."""
        pend = next_pending(self._state)
        if pend is None:
            self.statusMessage.emit("Fluxo já completo — nada pendente.")
            return
        self.actionRequested.emit(pend)
