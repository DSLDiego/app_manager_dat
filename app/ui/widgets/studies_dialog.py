"""Dialog de estudos: lista, carregar, clonar, versionar, exportar, importar."""

from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QDialog,
    QHBoxLayout,
    QInputDialog,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
)


class StudiesDialog(QDialog):
    """Gestão dos casos estudados (tupla dat-template-variáveis-lote-saída)."""

    studyLoaded = Signal(int)
    statusMessage = Signal(str)

    def __init__(self, study_service, parent=None):
        """Método `StudiesDialog.__init__`.
            Parâmetros: `self`, `study_service`, `parent`."""
        super().__init__(parent)
        self.study_service = study_service
        self.setWindowTitle("Estudos — Gestão e Versionamento")
        self.setMinimumWidth(600)

        layout = QVBoxLayout(self)
        self.lbl_info = QLabel("Estudos salvos (clique em carregar para reabrir):")
        layout.addWidget(self.lbl_info)

        self.btn_format = QPushButton("Formato: Árvore")
        self.btn_format.setToolTip("Alternar lista → árvore (estudo → versões, lista de listas).")
        self.btn_format.clicked.connect(self._toggle_format)
        btns_top = QHBoxLayout()
        btns_top.addStretch()
        btns_top.addWidget(self.btn_format)
        layout.addLayout(btns_top)

        from PySide6.QtWidgets import QStackedWidget

        self.view_stack = QStackedWidget()
        self.list_widget = QListWidget()
        self.list_widget.itemDoubleClicked.connect(self._load_selected)
        from app.ui.widgets.studies_tree_view import StudiesTreeView

        self.tree_view = StudiesTreeView()
        self.view_stack.addWidget(self.list_widget)  # 0
        self.view_stack.addWidget(self.tree_view)    # 1
        self.tree_view.itemDoubleClicked.connect(self._load_selected)
        layout.addWidget(self.view_stack, 1)

        self.btn_load = QPushButton("Carregar estudo")
        self.btn_load.clicked.connect(self._load_selected)
        self.btn_clone = QPushButton("Clonar…")
        self.btn_clone.clicked.connect(self._clone_selected)
        self.btn_snapshot = QPushButton("Salvar versão do estudo")
        self.btn_snapshot.clicked.connect(self._snapshot_selected)
        self.btn_delete = QPushButton("Excluir")
        self.btn_delete.clicked.connect(self._delete_selected)
        self.btn_export = QPushButton("Exportar JSON…")
        self.btn_export.clicked.connect(self._export_selected)
        self.btn_import = QPushButton("Importar JSON…")
        self.btn_import.clicked.connect(self._import_json)
        self.btn_diff = QPushButton("Diff de versões…")
        self.btn_diff.clicked.connect(self._diff_versions)
        self.btn_compare = QPushButton("Comparar estudos…")
        self.btn_compare.setToolTip("Diferenças de especificações entre dois estudos.")
        self.btn_compare.clicked.connect(self._compare_studies)
        self.btn_open_output = QPushButton("Abrir pasta de saída")
        self.btn_open_output.clicked.connect(self._open_output_dir)
        self.btn_rename = QPushButton("Renomear…")
        self.btn_rename.setToolTip("Renomeia o estudo selecionado (sem quebrar o histórico de versões).")
        self.btn_rename.clicked.connect(self._rename_selected)
        self.btn_desc = QPushButton("Editar descrição…")
        self.btn_desc.setToolTip("Edita a descrição do estudo selecionado, preservando specs e versões.")
        self.btn_desc.clicked.connect(self._edit_description)

        buttons_row = QHBoxLayout()
        for btn in (self.btn_load, self.btn_snapshot, self.btn_clone):
            buttons_row.addWidget(btn)
        layout.addLayout(buttons_row)

        buttons_row2 = QHBoxLayout()
        for btn in (self.btn_delete, self.btn_export, self.btn_import):
            buttons_row2.addWidget(btn)
        layout.addLayout(buttons_row2)

        buttons_row3 = QHBoxLayout()
        buttons_row3.addWidget(self.btn_diff)
        buttons_row3.addWidget(self.btn_compare)
        buttons_row3.addWidget(self.btn_rename)
        buttons_row3.addWidget(self.btn_desc)
        buttons_row3.addWidget(self.btn_open_output)
        layout.addLayout(buttons_row3)

        self.refresh()

    def _toggle_format(self):
        """Método `StudiesDialog._toggle_format`.
            Parâmetros: `self`."""
        to_tree = self.view_stack.currentIndex() == 0
        self.view_stack.setCurrentIndex(1 if to_tree else 0)
        self.btn_format.setText("Formato: Lista" if to_tree else "Formato: Árvore")
        if to_tree:
            self._fill_tree()

    def _fill_tree(self):
        """Método `StudiesDialog._fill_tree`.
            Parâmetros: `self`."""
        studies = self._studies_safe()
        versions_by = {}
        for study in studies:
            try:
                versions_by[int(study["id"])] = list(
                    self.study_service.list_versions(study["id"])
                )
            except Exception:  # noqa: BLE001
                versions_by[int(study["id"])] = []
        self.tree_view.populate(studies, versions_by)

    def _studies_safe(self) -> list:
        """Método `StudiesDialog._studies_safe`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        try:
            return list(self.study_service.list_studies())
        except Exception:  # noqa: BLE001
            return []

    def _current_index(self) -> int | None:
        """Índice do estudo — resolve conforme o formato ativo (lista/árvore)."""
        if self.view_stack.currentIndex() == 1:
            return self.tree_view.selected_study_row()
        item = self.list_widget.currentItem()
        return self.list_widget.row(item) if item is not None else None

    def refresh(self):
        """Método `StudiesDialog.refresh`.
            Parâmetros: `self`."""
        self.list_widget.clear()
        studies = self._studies_safe()
        for study in studies:
            ident = study["id"]
            description = study.get("description", "")
            meta = study.get("meta") or {}
            text = (
                f"#{ident} — {study['name']}"
                f"   [v{self._count_versions(ident)}]   "
                f"template_v{meta.get('template_version_id', '—')} · "
                f"batch {meta.get('batch_id', '—')} · "
                f"out {meta.get('output_dir', '—')}"
            )
            if description:
                text += f"  ({description})"
            self.list_widget.addItem(QListWidgetItem(text))
        if self.view_stack.currentIndex() == 1:
            self._fill_tree()

    def _count_versions(self, study_id: int) -> int:
        """Método `StudiesDialog._count_versions`.
            Parâmetros: `self`, `study_id`.
            Retorna o resultado calculado a partir do estado local."""
        try:
            return len(self.study_service.list_versions(study_id))
        except Exception:  # noqa: BLE001
            return 0

    def _current_study(self):
        """Método `StudiesDialog._current_study`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        idx = self._current_index()
        if idx is None:
            QMessageBox.information(self, "Sem estudo", "Selecione um estudo.")
            return None
        studies = self.study_service.list_studies()
        if 0 <= idx < len(studies):
            return studies[idx]
        return None

    def _load_selected(self, *_):
        """Método `StudiesDialog._load_selected`.
            Parâmetros: `self`, `*_`."""
        study = self._current_study()
        if study is None:
            return
        self.studyLoaded.emit(study["id"])
        self.statusMessage.emit(f"Estudo #{study['id']} '{study['name']}' carregado.")
        self.accept()

    def _clone_selected(self):
        """Método `StudiesDialog._clone_selected`.
            Parâmetros: `self`."""
        study = self._current_study()
        if study is None:
            return
        name, ok = QInputDialog.getText(
            self, "Clonar estudo",
            f"Nome do novo estudo (clone de '{study['name']}'):"
        )
        if not ok or not str(name).strip():
            return
        try:
            new_id = self.study_service.clone(study["id"], str(name).strip())
        except Exception as exc:  # noqa: BLE001
            QMessageBox.critical(self, "Erro", str(exc))
            return
        self.statusMessage.emit(f"Estudo clonado como #{new_id} '{name}'.")
        self.refresh()

    def _rename_selected(self):
        """Método `StudiesDialog._rename_selected`.
            Parâmetros: `self`."""
        study = self._current_study()
        if study is None:
            return
        name, ok = QInputDialog.getText(
            self, "Renomear estudo", f"Novo nome para '{study['name']}':"
        )
        if not ok or not str(name).strip():
            return
        try:
            ok_rename = self.study_service.rename(study["id"], str(name).strip())
        except Exception as exc:  # noqa: BLE001
            QMessageBox.critical(self, "Erro", str(exc))
            return
        if not ok_rename:
            QMessageBox.warning(
                self, "Nome em uso", f"Já existe um estudo chamado '{name}'."
            )
            return
        self.statusMessage.emit(f"Estudo #{study['id']} renomeado para '{name}'.")
        self.refresh()

    def _edit_description(self):
        """Método `StudiesDialog._edit_description`.
            Parâmetros: `self`."""
        study = self._current_study()
        if study is None:
            return
        text, ok = QInputDialog.getMultiLineText(
            self,
            "Editar descrição",
            f"Descrição de '{study['name']}':",
            str(study.get("description") or ""),
        )
        if not ok:
            return
        try:
            self.study_service.set_description(study["id"], text)
        except Exception as exc:  # noqa: BLE001
            QMessageBox.critical(self, "Erro", str(exc))
            return
        self.statusMessage.emit(f"Descrição do estudo #{study['id']} atualizada.")
        self.refresh()

    def _snapshot_selected(self):
        """Método `StudiesDialog._snapshot_selected`.
            Parâmetros: `self`."""
        study = self._current_study()
        if study is None:
            return
        comment, ok = QInputDialog.getText(
            self, "Salvar versão", "Comentário da versão:"
        )
        if not ok:
            return
        try:
            version = self.study_service.snapshot(study["id"], comment)
        except Exception as exc:  # noqa: BLE001
            QMessageBox.critical(self, "Erro", str(exc))
            return
        self.statusMessage.emit(f"Estudo #{study['id']} → versão {version} salva.")
        self.refresh()

    def _delete_selected(self):
        """Método `StudiesDialog._delete_selected`.
            Parâmetros: `self`."""
        study = self._current_study()
        if study is None:
            return
        confirm = QMessageBox.question(
            self, "Excluir estudo",
            f"Excluir o estudo '{study['name']}' e todo o histórico?",
        )
        if confirm != QMessageBox.StandardButton.Yes:
            return
        self.study_service.delete(study["id"])
        self.statusMessage.emit(f"Estudo '{study['name']}' excluído.")
        self.refresh()

    def _export_selected(self):
        """Método `StudiesDialog._export_selected`.
            Parâmetros: `self`."""
        study = self._current_study()
        if study is None:
            return
        from PySide6.QtWidgets import QFileDialog

        path, _ = QFileDialog.getSaveFileName(
            self, "Exportar estudo", f"{study['name']}.json", "JSON (*.json)"
        )
        if not path:
            return
        try:
            out = self.study_service.export(study["id"], path)
        except Exception as exc:  # noqa: BLE001
            QMessageBox.critical(self, "Erro", str(exc))
            return
        self.statusMessage.emit(f"Estudo exportado para {out}.")

    def _import_json(self):
        """Método `StudiesDialog._import_json`.
            Parâmetros: `self`."""
        from PySide6.QtWidgets import QFileDialog

        path, _ = QFileDialog.getOpenFileName(
            self, "Importar estudo", "", "JSON (*.json)"
        )
        if not path:
            return
        try:
            study_id = self.study_service.import_study(path)
        except Exception as exc:  # noqa: BLE001
            QMessageBox.critical(self, "Erro", str(exc))
            return
        self.statusMessage.emit(f"Estudo #{study_id} importado.")
        self.refresh()

    # ---------- comparação entre estudos (r22) ----------
    def _compare_studies(self):
        """Método `StudiesDialog._compare_studies`.
            Parâmetros: `self`."""
        from app.ui.widgets.studies_compare_dialog import StudiesCompareDialog

        studies = self._studies_safe()
        if len(studies) < 2:
            QMessageBox.information(
                self, "Comparar", "Cadastre pelo menos 2 estudos para comparar."
            )
            return
        StudiesCompareDialog(self.study_service, studies, parent=self).exec()

    # ---------- diff de versões ----------
    def _diff_versions(self):
        """Método `StudiesDialog._diff_versions`.
            Parâmetros: `self`."""
        study = self._current_study()
        if study is None:
            return
        study_id = study["id"]
        versions = self.study_service.list_versions(study_id)
        if len(versions) < 2:
            QMessageBox.information(
                self, "Diff", "O estudo precisa de pelo menos 2 versões salvas."
            )
            return
        a, _ = QInputDialog.getInt(self, "Diff", "Versão antiga:", versions[-1]["version_number"])
        b, _ = QInputDialog.getInt(self, "Diff", "Versão nova:", versions[0]["version_number"])
        try:
            va = self.study_service.get_version(study_id, a)
            vb = self.study_service.get_version(study_id, b)
        except Exception as exc:  # noqa: BLE001
            QMessageBox.critical(self, "Erro", str(exc))
            return
        lines = self._build_diff(va, vb)
        QMessageBox.information(self, f"Diff v{a} → v{b}", "\n".join(lines) or "Sem diferenças.")

    @staticmethod
    def _build_diff(va: dict, vb: dict) -> list:
        """Método `StudiesDialog._build_diff`.
            Parâmetros: `va`, `vb`.
            Retorna o resultado calculado a partir do estado local."""
        import json

        lines: list = []
        specs_a = va.get("specs") or {}
        specs_b = vb.get("specs") or {}

        def order(key: str):
            """Função `order`.
                Parâmetros: `key`.
                Retorna o resultado calculado a partir do estado local."""
            try:
                return (0, int(key))
            except ValueError:
                return (1, str(key))

        for key in sorted(set(specs_a) | set(specs_b), key=order):
            sa = json.dumps(specs_a.get(key), sort_keys=True)
            sb = json.dumps(specs_b.get(key), sort_keys=True)
            if sa != sb:
                marker = "− " if sb == "null" else ("+ " if sa == "null" else "~ ")
                lines.append(f"{marker}{key}: {sb if sa == 'null' else sa} → {sb}")
        meta_a = va.get("meta") or {}
        meta_b = vb.get("meta") or {}
        for key in sorted(set(meta_a) | set(meta_b)):
            if meta_a.get(key) != meta_b.get(key):
                marker = "− " if key not in meta_b else ("+ " if key not in meta_a else "~ ")
                lines.append(f"{marker}meta.{key}: '{meta_a.get(key)}' → '{meta_b.get(key)}'")
        return lines

    # ---------- abrir pasta de saída ----------
    def _open_output_dir(self):
        """Método `StudiesDialog._open_output_dir`.
            Parâmetros: `self`."""
        study = self._current_study()
        if study is None:
            return
        output = (study.get("meta") or {}).get("output_dir")
        if not output:
            QMessageBox.information(
                self, "Sem pasta", "Este estudo não tem pasta de saída registrada."
            )
            return
        import os
        import subprocess

        try:
            if os.name == "nt":
                os.startfile(output)  # noqa: S606
            else:
                subprocess.Popen(["xdg-open", output])  # noqa: S606
        except OSError as exc:
            QMessageBox.warning(self, "Erro", f"Não foi possível abrir: {exc}")
