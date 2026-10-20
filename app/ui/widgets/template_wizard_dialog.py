"""Assistente (wizard) de criação de template .dat em passos.

Puro em wizard_scan()/wizard_suggest()/SAMPLE_TEMPLATE; diálogo com 3 passos:
texto base → variáveis detectadas com distribuições sugeridas → revisão.
Ao concluir, emite templateReady(texto) — MainWindow cria a aba.
"""

from __future__ import annotations

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QComboBox,
    QDialog,
    QHBoxLayout,
    QLabel,
    QPlainTextEdit,
    QPushButton,
    QStackedWidget,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from app.core.parsing import find_variables, var_label

SUGGESTED_DISTS = ("uniform", "norm", "triang", "lognorm")

SAMPLE_TEMPLATE = """-- Exemplo: template com variáveis
PERMX = $1
PORO  = $2
WGR   = $var3
"""


def wizard_scan(text: str) -> dict:
    """Resumo das variáveis do texto — puro."""
    var_ids = find_variables(text)
    return {
        "var_ids": var_ids,
        "n_regular": len([v for v in var_ids if v < 10000]),
        "n_namespace": len([v for v in var_ids if v >= 10000]),
        "empty": not text.strip(),
    }


def wizard_suggest(var_ids: list[int]) -> dict[int, str]:
    """Distribuição sugerida por variável — puro (uniform por padrão)."""
    return {int(v): SUGGESTED_DISTS[0] for v in var_ids}


class TemplateWizardDialog(QDialog):
    """3 passos: texto base → variáveis/distribuições → pronto."""

    templateReady = Signal(str)

    def __init__(self, parent=None):
        """Método `TemplateWizardDialog.__init__`.
            Parâmetros: `self`, `parent`."""
        super().__init__(parent)
        self.setWindowTitle("Assistente de template — 3 passos")
        self.resize(640, 480)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 6, 8, 6)
        layout.setSpacing(4)

        self.lbl_step = QLabel("Passo 1 de 3 — texto base do template:")
        layout.addWidget(self.lbl_step)

        self.stack = QStackedWidget()
        layout.addWidget(self.stack, 1)

        # passo 1: texto
        page1 = QWidget()
        l1 = QVBoxLayout(page1)
        l1.setContentsMargins(0, 0, 0, 0)
        self.txt_base = QPlainTextEdit()
        self.txt_base.setPlaceholderText("Cole ou digite o template com tokens $N / $varN…")
        l1.addWidget(self.txt_base, 1)
        bar1 = QHBoxLayout()
        self.btn_sample = QPushButton("Inserir exemplo")
        self.btn_sample.setToolTip("Preenche com um template de exemplo com $1, $2 e $var3.")
        bar1.addWidget(self.btn_sample)
        bar1.addStretch()
        l1.addLayout(bar1)
        self.stack.addWidget(page1)  # 0

        # passo 2: variáveis detectadas + sugestão de distribuição
        page2 = QWidget()
        l2 = QVBoxLayout(page2)
        l2.setContentsMargins(0, 0, 0, 0)
        self.lbl_vars = QLabel("Nenhuma variável detectada.")
        l2.addWidget(self.lbl_vars)
        self.tbl_vars = QTableWidget()
        self.tbl_vars.setColumnCount(2)
        self.tbl_vars.setHorizontalHeaderLabels(["Variável", "Distribuição sugerida"])
        l2.addWidget(self.tbl_vars, 1)
        self.stack.addWidget(page2)  # 1

        # passo 3: revisão
        page3 = QWidget()
        l3 = QVBoxLayout(page3)
        l3.setContentsMargins(0, 0, 0, 0)
        self.lbl_review = QLabel("Revise e conclua:")
        l3.addWidget(self.lbl_review)
        self.txt_review = QPlainTextEdit()
        self.txt_review.setReadOnly(True)
        l3.addWidget(self.txt_review, 1)
        self.stack.addWidget(page3)  # 2

        nav = QHBoxLayout()
        self.btn_back = QPushButton("◀ Voltar")
        self.btn_next = QPushButton("Avançar ▶")
        self.btn_finish = QPushButton("Criar template")
        self.btn_finish.setDefault(True)
        nav.addWidget(self.btn_back)
        nav.addStretch()
        nav.addWidget(self.btn_next)
        nav.addWidget(self.btn_finish)
        layout.addLayout(nav)

        self.btn_sample.clicked.connect(self._insert_sample)
        self.btn_back.clicked.connect(self._go_back)
        self.btn_next.clicked.connect(self._go_next)
        self.btn_finish.clicked.connect(self._finish)
        self._sync_nav()

    # ---------- navegação de passos ----------
    def _sync_nav(self):
        """Método `TemplateWizardDialog._sync_nav`.
            Parâmetros: `self`."""
        step = self.stack.currentIndex()
        total = self.stack.count()
        self.lbl_step.setText(f"Passo {step + 1} de {total} — {self._step_label(step)}")
        self.btn_back.setEnabled(step > 0)
        self.btn_next.setEnabled(step < total - 1)
        self.btn_finish.setEnabled(not wizard_scan(self.txt_base.toPlainText())["empty"])

    @staticmethod
    def _step_label(step: int) -> str:
        """Método `TemplateWizardDialog._step_label`.
            Parâmetros: `step`.
            Retorna o resultado calculado a partir do estado local."""
        return ("texto base do template", "variáveis detectadas", "revisão e conclusão")[min(2, step)]

    def _insert_sample(self):
        """Método `TemplateWizardDialog._insert_sample`.
            Parâmetros: `self`."""
        self.txt_base.setPlainText(SAMPLE_TEMPLATE)

    def _go_back(self):
        """Método `TemplateWizardDialog._go_back`.
            Parâmetros: `self`."""
        if self.stack.currentIndex() > 0:
            self.stack.setCurrentIndex(self.stack.currentIndex() - 1)
        self._sync_nav()

    def _go_next(self):
        """Método `TemplateWizardDialog._go_next`.
            Parâmetros: `self`."""
        cur = self.stack.currentIndex()
        if cur == 0:
            self._fill_vars()
        self.stack.setCurrentIndex(min(self.stack.count() - 1, cur + 1))
        self._sync_nav()

    # ---------- passos ----------
    def _fill_vars(self):
        """Método `TemplateWizardDialog._fill_vars`.
            Parâmetros: `self`."""
        scan = wizard_scan(self.txt_base.toPlainText())
        var_ids = scan["var_ids"]
        self._suggest = wizard_suggest(var_ids)
        self.lbl_vars.setText(
            f"{len(var_ids)} variável(is) — {scan['n_regular']} $N · {scan['n_namespace']} $varN"
        )
        self.tbl_vars.setRowCount(len(var_ids))
        for i, var_id in enumerate(var_ids):
            self.tbl_vars.setItem(i, 0, QTableWidgetItem(var_label(var_id)))
            combo = QComboBox()
            combo.addItems(list(SUGGESTED_DISTS))
            combo.setCurrentText(self._suggest[var_id])
            self.tbl_vars.setCellWidget(i, 1, combo)

    def _finish(self):
        """Método `TemplateWizardDialog._finish`.
            Parâmetros: `self`."""
        text = self.txt_base.toPlainText()
        scan = wizard_scan(text)
        if scan["empty"]:
            self.lbl_review.setText("Template vazio — volte ao passo 1.")
            return
        self.templateReady.emit(text)
        self.accept()
