"""QTabWidget de Editores — guarda estado de modified por aba."""

from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import QTimer, Signal

RECENT_CAP = 8
AUTOSAVE_INTERVAL_MS = 60_000  # T5433: backup .bak a cada 60s


def backup_name(file_path: str) -> str:
    """Caminho do backup (.bak) para o arquivo informado — puro."""
    return str(file_path) + ".bak"


def write_backup(file_path: str, content: str) -> str:
    """Grava `<caminho>.bak`. Retorna o caminho gravado (vazio se inválido)."""
    if not file_path:
        return ""
    target = backup_name(file_path)
    try:
        Path(target).write_text(content, encoding="utf-8")
    except OSError:
        return ""
    return target


def recent_push(items: list[str], path: str, cap: int = RECENT_CAP) -> list[str]:
    """Lista de recentes: dedupe, novo na frente, cap — puro."""
    out = [str(path)] + [x for x in items if x != str(path)]
    return out[: max(0, cap)]


def recent_join(items: list[str]) -> str:
    """Serializa a lista p/ QSettings (um por linha) — puro."""
    return "\n".join(str(x) for x in items)


def recent_split(blob) -> list[str]:
    """Desserializa o blob do QSettings — puro; ignora vazios."""
    return [x for x in str(blob or "").split("\n") if x.strip()]
from PySide6.QtWidgets import QFileDialog, QMessageBox, QTabWidget, QWidget

from app.ui.editor.editor_widget import EditorWidget


class EditorTabs(QTabWidget):
    """Classe `EditorTabs` do módulo."""
    tab_dirty_changed = Signal(int, bool)
    close_tab_requested = Signal(int)
    tabsChanged = Signal()  # aba criada/fechada/renomeada (dock de lista de arquivos)
    fileOpened = Signal(str)  # r19: caminho aberto com sucesso (menu de recentes)

    def __init__(self, parent=None):
        """Método `EditorTabs.__init__`.
            Parâmetros: `self`, `parent`."""
        super().__init__(parent)
        self.setTabsClosable(True)
        self.setMovable(True)
        self.setDocumentMode(True)
        self.tabCloseRequested.connect(self._handle_close_request)

        # T5433: auto-save (backup .bak) a cada 60s
        self._autosave_timer = QTimer(self)
        self._autosave_timer.setInterval(AUTOSAVE_INTERVAL_MS)
        self._autosave_timer.timeout.connect(self.autosave_backups)
        self._autosave_timer.start()

        # T5432: histórico persistente (undo/redo entre trocas de aba)
        self._persist_history: dict[int, dict] = {}
        self._last_current_tab = None
        self.currentChanged.connect(self._capture_on_switch)

    # ---------- T5432: undo/redo persistente entre abas ----------

    def _capture_on_switch(self, index: int) -> None:
        """Ao trocar de aba, captura o texto da aba ANTERIOR (persistência)."""
        previous = self._last_current_tab
        self._last_current_tab = self.widget(index)
        if isinstance(previous, EditorWidget) and previous.file_path:
            self.persist_tab(previous)

    def persist_tab(self, tab: EditorWidget) -> int:
        """Empurra o texto atual da aba na pilha persistente (dedupe)."""
        text = tab.editor.toPlainText() if hasattr(tab, "editor") else ""
        entry = self._persist_history.setdefault(id(tab), {"stack": [], "i": -1})
        if entry["stack"] and entry["stack"][entry["i"]] == text:
            return entry["i"]
        entry["stack"] = entry["stack"][: entry["i"] + 1]
        entry["stack"].append(text)
        entry["i"] = len(entry["stack"]) - 1
        return entry["i"]

    def undo_persistent(self, index: int) -> bool:
        """Volta para o snapshot anterior da aba (history persistente)."""
        tab = self.widget(index)
        entry = self._persist_history.get(id(tab))
        if not entry or entry["i"] <= 0:
            return False
        entry["i"] -= 1
        tab.set_content(entry["stack"][entry["i"]])
        return True

    def redo_persistent(self, index: int) -> bool:
        """Avança para o snapshot seguinte da aba (history persistente)."""
        tab = self.widget(index)
        entry = self._persist_history.get(id(tab))
        if not entry or entry["i"] >= len(entry["stack"]) - 1:
            return False
        entry["i"] += 1
        tab.set_content(entry["stack"][entry["i"]])
        return True

    def autosave_backups(self) -> int:
        """Grava `<arquivo>.bak` para cada aba não modificada pendente.
        Retorna a quantidade de backups gravados."""
        written = 0
        for i in range(self.count()):
            tab = self.widget(i)
            if isinstance(tab, EditorWidget) and tab.file_path:
                content = tab.editor.toPlainText() if hasattr(tab, "editor") else ""
                if content and write_backup(tab.file_path, content):
                    written += 1
        return written

    # ---------- abas ----------
    def open_file(self, path: str) -> EditorWidget:
        """Método `EditorTabs.open_file`.
            Parâmetros: `self`, `path`.
            Retorna o resultado calculado a partir do estado local."""
        existing = self.find_tab_by_path(path)
        if existing:
            self.setCurrentWidget(existing)
            self.fileOpened.emit(str(path))
            return existing
        tab = EditorWidget(path)
        tab.load_file(path)
        self._add_tab(tab)
        self.fileOpened.emit(str(path))
        return tab

    def new_tab(self, content: str = "", title: str = "Sem título") -> EditorWidget:
        """Método `EditorTabs.new_tab`.
            Parâmetros: `self`, `content`, `title`.
            Retorna o resultado calculado a partir do estado local."""
        tab = EditorWidget()
        if content:
            tab.set_content(content)
        self._add_tab(tab, title)
        return tab

    def _add_tab(self, tab: EditorWidget, title: str | None = None) -> None:
        """Método `EditorTabs._add_tab`.
            Parâmetros: `self`, `tab`, `title`."""
        if title is None:
            from pathlib import Path

            title = Path(tab.file_path).name if tab.file_path else "Sem título"
        index = self.addTab(tab, title)
        self.setCurrentIndex(index)
        tab.modified_changed.connect(
            lambda dirty, t=tab: self._mark_dirty(self.indexOf(t), dirty)
        )
        tab.saved.connect(lambda _path, t=tab: self._mark_dirty(self.indexOf(t), False))
        self.tabsChanged.emit()

    def _mark_dirty(self, index: int, dirty: bool) -> None:
        """Método `EditorTabs._mark_dirty`.
            Parâmetros: `self`, `index`, `dirty`."""
        if index < 0:
            return
        base = self.tabText(index).lstrip("• ")
        self.setTabText(index, f"• {base}" if dirty else base)
        self.tab_dirty_changed.emit(index, dirty)

    def find_tab_by_path(self, path: str) -> EditorWidget | None:
        """Método `EditorTabs.find_tab_by_path`.
            Parâmetros: `self`, `path`.
            Retorna o resultado calculado a partir do estado local."""
        for i in range(self.count()):
            tab = self.widget(i)
            if isinstance(tab, EditorWidget) and tab.file_path == path:
                return tab
        return None

    def current_editor(self) -> EditorWidget | None:
        """Método `EditorTabs.current_editor`.
            Parâmetros: `self`.
            Retorna o resultado calculado a partir do estado local."""
        w = self.currentWidget()
        return w if isinstance(w, EditorWidget) else None

    # ---------- fechamento ----------
    def _handle_close_request(self, index: int) -> None:
        """Método `EditorTabs._handle_close_request`.
            Parâmetros: `self`, `index`."""
        self.close_tab_requested.emit(index)
        self._close_tab(index)

    def _close_tab(self, index: int) -> None:
        """Método `EditorTabs._close_tab`.
            Parâmetros: `self`, `index`."""
        tab = self.widget(index)
        if isinstance(tab, EditorWidget) and tab.is_modified():
            answer = QMessageBox.question(
                self, "Alterações não salvas",
                f"Fechar '{self.tabText(index)}' sem salvar?",
                QMessageBox.StandardButton.Save
                | QMessageBox.StandardButton.Discard
                | QMessageBox.StandardButton.Cancel,
            )
            if answer == QMessageBox.StandardButton.Save:
                if not tab.file_path:
                    path, _ = QFileDialog.getSaveFileName(
                        self, "Salvar arquivo", "", "DAT (*.dat);;Texto (*.txt)"
                    )
                    if not path:
                        return
                    tab.file_path = path
                tab.save()
            elif answer == QMessageBox.StandardButton.Cancel:
                return
        self.removeTab(index)
        self.tabsChanged.emit()

    def open_dialog(self, parent: QWidget | None = None) -> None:
        """Método `EditorTabs.open_dialog`.
            Parâmetros: `self`, `parent`."""
        paths, _ = QFileDialog.getOpenFileNames(
            self, "Abrir arquivos", "", "DAT (*.dat);;Texto (*.txt);;Todos (*)"
        )
        for p in paths:
            self.open_file(p)

    def save_current(self) -> None:
        """Método `EditorTabs.save_current`.
            Parâmetros: `self`."""
        tab = self.current_editor()
        if tab:
            if not tab.file_path:
                path, _ = QFileDialog.getSaveFileName(
                    self, "Salvar arquivo", "", "DAT (*.dat);;Texto (*.txt)"
                )
                if not path:
                    return
                tab.file_path = path
                self.setTabText(self.indexOf(tab), Path(path).name)
                self.tabsChanged.emit()
            tab.save()
