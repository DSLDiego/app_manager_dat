"""Diff de arquivos — o usuário escolhe 2 arquivos (ou abas abertas) e compara.

Puro em diff_lines()/count_changes(); UI: dois QPlainTextEdit lado a lado + resumo.
"""

from __future__ import annotations

import difflib

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDialog,
    QFileDialog,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QPlainTextEdit,
    QVBoxLayout,
)

MAX_DIFF_LINES = 20_000


def diff_lines(a: str, b: str, n: int = 2) -> list[str]:
    """Diff unificado (estável, cap de linhas) — puro."""
    lines = list(
        difflib.unified_diff(
            a.splitlines(), b.splitlines(), fromfile="A", tofile="B", lineterm="", n=n
        )
    )
    return lines[:MAX_DIFF_LINES]


def count_changes(a: str, b: str) -> tuple[int, int, int]:
    """(linhas adicionadas, removidas, iguais) — puro, via SequenceMatcher."""
    sm = difflib.SequenceMatcher(None, a.splitlines(), b.splitlines(), autojunk=False)
    added = removed = same = 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            same += i2 - i1
        elif tag == "insert":
            added += j2 - j1
        elif tag == "delete":
            removed += i2 - i1
        else:  # replace
            added += j2 - j1
            removed += i2 - i1
    return added, removed, same


def is_different(a: str, b: str) -> bool:
    """Função `is_different`.
        Parâmetros: `a`, `b`.
        Retorna o resultado calculado a partir do estado local."""
    return a != b


class DiffDialog(QDialog):
    """Seleção de 2 arquivos (abas abertas ou disco) e diff lado a lado."""

    def __init__(self, open_files: list[tuple[str, str]] | None = None, parent=None):
        """open_files: [(título, conteúdo)] das abas abertas — opcional."""
        super().__init__(parent)
        self.setWindowTitle("Diff de arquivos")
        self.resize(980, 620)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(6, 4, 6, 4)
        layout.setSpacing(3)

        sel = QGridLayout()
        self.combo_a = QComboBox()
        self.combo_b = QComboBox()
        self.btn_browse_a = QPushButton("Procurar A…")
        self.btn_browse_b = QPushButton("Procurar B…")
        self.btn_browse_a.clicked.connect(lambda: self._browse(self.combo_a))
        self.btn_browse_b.clicked.connect(lambda: self._browse(self.combo_b))
        sel.addWidget(QLabel("Arquivo A:"), 0, 0)
        sel.addWidget(self.combo_a, 0, 1)
        sel.addWidget(self.btn_browse_a, 0, 2)
        sel.addWidget(QLabel("Arquivo B:"), 1, 0)
        sel.addWidget(self.combo_b, 1, 1)
        sel.addWidget(self.btn_browse_b, 1, 2)
        layout.addLayout(sel)

        bar = QHBoxLayout()
        self.btn_compare = QPushButton("Comparar")
        self.btn_compare.setDefault(True)
        self.btn_swap = QPushButton("Trocar A ↔ B")
        self.btn_swap.setToolTip("Inverte as fontes A e B e recompara.")
        self.chk_sync = QCheckBox("Sincronizar rolagem")
        self.chk_sync.setChecked(True)
        self.chk_sync.setToolTip("Rolagem vertical dos dois painéis anda junta.")
        self.lbl_summary = QLabel("—")
        bar.addWidget(self.btn_compare)
        bar.addWidget(self.btn_swap)
        bar.addWidget(self.chk_sync)
        bar.addStretch()
        bar.addWidget(self.lbl_summary)
        layout.addLayout(bar)

        self.txt_a = QPlainTextEdit()
        self.txt_a.setReadOnly(True)
        self.txt_b = QPlainTextEdit()
        self.txt_b.setReadOnly(True)
        self.txt_diff = QPlainTextEdit()
        self.txt_diff.setReadOnly(True)
        for t in (self.txt_a, self.txt_b, self.txt_diff):
            t.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)
        grid = QGridLayout()
        grid.addWidget(self.txt_a, 0, 0)
        grid.addWidget(self.txt_b, 0, 1)
        grid.addWidget(self.txt_diff, 1, 0, 1, 2)
        grid.setRowStretch(0, 3)
        grid.setRowStretch(1, 2)
        layout.addLayout(grid, 1)

        self._disk_files: dict[str, str] = {}  # caminho → conteúdo
        for title, content in open_files or []:
            self.combo_a.addItem(str(title))
            self.combo_b.addItem(str(title))
        self._open_titles: list[tuple[str, str]] = list(open_files or [])
        self.btn_compare.clicked.connect(self.compare)
        self.btn_swap.clicked.connect(self.swap_sides)
        if self.combo_a.count() >= 2:
            self.combo_b.setCurrentIndex(1)
        self._syncing = False
        self.chk_sync.toggled.connect(self._on_sync_toggled)
        self.txt_a.verticalScrollBar().valueChanged.connect(self._follow_a)
        self.txt_b.verticalScrollBar().valueChanged.connect(self._follow_b)

    # ---------- rolagem sincronizada + troca (r21) ----------
    def _on_sync_toggled(self, on: bool):
        """Método `DiffDialog._on_sync_toggled`.
            Parâmetros: `self`, `on`."""
        if on:  # realinha imediatamente ao ligar
            self._follow_a(self.txt_a.verticalScrollBar().value())

    def _follow_a(self, value: int):
        """Método `DiffDialog._follow_a`.
            Parâmetros: `self`, `value`."""
        if self.chk_sync.isChecked() and not self._syncing:
            self._syncing = True
            self.txt_b.verticalScrollBar().setValue(value)
            self._syncing = False

    def _follow_b(self, value: int):
        """Método `DiffDialog._follow_b`.
            Parâmetros: `self`, `value`."""
        if self.chk_sync.isChecked() and not self._syncing:
            self._syncing = True
            self.txt_a.verticalScrollBar().setValue(value)
            self._syncing = False

    def swap_sides(self) -> dict:
        """Troca A ↔ B e recompara (o diff invertido também é útil)."""
        ia, ib = self.combo_a.currentIndex(), self.combo_b.currentIndex()
        self.combo_a.setCurrentIndex(ib)
        self.combo_b.setCurrentIndex(ia)
        return self.compare()

    # ---------- fontes de texto ----------
    def _text_for(self, combo: QComboBox) -> tuple[str, str]:
        """(rótulo, texto) da fonte selecionada — aba aberta ou arquivo do disco."""
        title = combo.currentText()
        if title in self._disk_files:
            return title, self._disk_files[title]
        for t, content in self._open_titles:
            if t == title:
                return t, content
        return title, ""

    def _browse(self, combo: QComboBox):
        """Método `DiffDialog._browse`.
            Parâmetros: `self`, `combo`."""
        from PySide6.QtWidgets import QFileDialog as _QFD

        path, _ = _QFD.getOpenFileName(self, "Arquivo para diff", "", "Todos (*)")
        if not path:
            return
        try:
            content = open(path, "r", encoding="utf-8", errors="replace").read()
        except OSError as exc:
            self.lbl_summary.setText(f"Erro lendo {path}: {exc}")
            return
        title = f"[disco] {path}"
        self._disk_files[title] = content
        if combo.findText(title) < 0:
            combo.addItem(title)
        combo.setCurrentText(title)

    def set_texts(self, a: str, b: str) -> dict:
        """Preenche os painéis + diff; retorna resumo (puro-friendly p/ testes)."""
        self.txt_a.setPlainText(a)
        self.txt_b.setPlainText(b)
        dl = diff_lines(a, b)
        self.txt_diff.setPlainText("\n".join(dl) if dl else "(sem diferenças)")
        added, removed, same = count_changes(a, b)
        summary = {
            "added": added,
            "removed": removed,
            "same": same,
            "different": is_different(a, b),
        }
        self.lbl_summary.setText(
            f"+{added} / −{removed} · {same} iguais"
            + ("" if summary["different"] else " · IDÊNTICOS")
        )
        return summary

    def compare(self) -> dict:
        """Método `DiffDialog.compare`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        _, ta = self._text_for(self.combo_a)
        _, tb = self._text_for(self.combo_b)
        return self.set_texts(ta, tb)
