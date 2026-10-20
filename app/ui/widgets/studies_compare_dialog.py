"""Diálogo: comparar 2 estudos (specs) lado a lado — tabela de diferenças."""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QComboBox,
    QDialog,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
)

from app.core.parsing import var_label
from app.services.specs_diff import diff_is_empty, specs_diff


class StudiesCompareDialog(QDialog):
    """Escolhe dois estudos e mostra added/removed/changed entre as specs."""

    def __init__(self, study_service, studies: list, parent=None):
        """Método `StudiesCompareDialog.__init__`.
            Parâmetros: `self`, `study_service`, `studies`, `parent`."""
        super().__init__(parent)
        self.setWindowTitle("Comparar estudos — especificações")
        self.resize(620, 380)
        self.study_service = study_service

        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 6, 8, 6)
        layout.setSpacing(4)

        bar = QHBoxLayout()
        self.lbl_a = QLabel("A:")
        self.combo_a = QComboBox()
        self.lbl_b = QLabel("B:")
        self.combo_b = QComboBox()
        for combo in (self.combo_a, self.combo_b):
            for s in studies:
                combo.addItem(f"#{s['id']} — {s['name']}", int(s["id"]))
        if self.combo_a.count() >= 2:
            self.combo_b.setCurrentIndex(1)
        self.btn_compare = QPushButton("Comparar")
        self.btn_compare.setDefault(True)
        self.btn_swap = QPushButton("Trocar A ↔ B")
        bar.addWidget(self.lbl_a)
        bar.addWidget(self.combo_a, 1)
        bar.addWidget(self.lbl_b)
        bar.addWidget(self.combo_b, 1)
        bar.addWidget(self.btn_swap)
        bar.addWidget(self.btn_compare)
        layout.addLayout(bar)

        self.lbl_summary = QLabel("—")
        layout.addWidget(self.lbl_summary)

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Variável · campo", "A → B"])
        self.table.setEditTriggers(self.table.editTriggers().__class__.NoEditTriggers)
        layout.addWidget(self.table, 1)

        btn_close = QPushButton("Fechar")
        btn_close.clicked.connect(self.accept)
        layout.addWidget(btn_close, 0, Qt.AlignmentFlag.AlignRight)

        self.btn_compare.clicked.connect(self.compare)
        self.btn_swap.clicked.connect(self._swap)
        self.compare()

    # ---------- seleção ----------
    def _study_id(self, combo) -> int | None:
        """Método `StudiesCompareDialog._study_id`.
            Parâmetros: `self`, `combo`.
            Retorna o resultado calculado a partir do estado local."""
        data = combo.currentData()
        return None if data is None else int(data)

    def _specs_of(self, study_id: int | None) -> dict:
        """Método `StudiesCompareDialog._specs_of`.
            Parâmetros: `self`, `study_id`.
            Retorna o resultado calculado a partir do estado local."""
        if study_id is None:
            return {}
        try:
            return dict(self.study_service.get(study_id).get("specs") or {})
        except Exception:  # noqa: BLE001
            return {}

    def _swap(self):
        """Método `StudiesCompareDialog._swap`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        ia, ib = self.combo_a.currentIndex(), self.combo_b.currentIndex()
        self.combo_a.setCurrentIndex(ib)
        self.combo_b.setCurrentIndex(ia)
        return self.compare()

    def compare(self) -> dict:
        """Compara e preenche a tabela; retorna o diff puro p/ testes."""
        diff = specs_diff(
            self._specs_of(self._study_id(self.combo_a)),
            self._specs_of(self._study_id(self.combo_b)),
        )
        rows = []
        for var in diff["added"]:
            rows.append((f"{var_label(int(var))} (adicionada em B)", "+"))
        for var in diff["removed"]:
            rows.append((f"{var_label(int(var))} (removida em B)", "−"))
        for ch in diff["changed"]:
            rows.append(
                (
                    f"{var_label(int(ch['var']))} · {ch['field']}",
                    f"{ch['a']} → {ch['b']}",
                )
            )
        self.table.setRowCount(len(rows))
        for i, (left, right) in enumerate(rows):
            self.table.setItem(i, 0, QTableWidgetItem(left))
            self.table.setItem(i, 1, QTableWidgetItem(str(right)))
        self.lbl_summary.setText(
            "Estudos idênticos."
            if diff_is_empty(diff)
            else f"{len(diff['added'])} adicionadas · {len(diff['removed'])} removidas · {len(diff['changed'])} alteradas"
        )
        return diff
