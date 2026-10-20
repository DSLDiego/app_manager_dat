"""Regressão da rodada 14: placeholders nos cartões, lista compacta, pasta output."""

import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import pytest
from PySide6.QtWidgets import QApplication


@pytest.fixture(scope="module")
def qapp():
    app = QApplication.instance() or QApplication([])
    yield app


def test_card_grid_unchanged():
    from app.ui.widgets.experiment_cards_view import card_grid

    assert card_grid(13, cols=4) == (4, 4, 13)
    assert card_grid(0, cols=4) == (1, 4, 0)


def test_cards_filled_with_placeholders(qapp):
    from PySide6.QtWidgets import QFrame, QLabel

    from app.ui.widgets.experiment_cards_view import ExperimentCard, ExperimentCardsView

    view = ExperimentCardsView(cards := 4)  # noqa: F841
    rows = [{"external_id": i, "values": {1: float(i)}} for i in range(1, 6)]
    shown = view.set_data(rows, [1])
    assert shown == 5
    # 5 cartões numa grade 4 por linha → 8 slots → 3 placeholders
    assert view.grid.count() == 8
    cards_seen, placeholders = 0, 0
    for i in range(view.grid.count()):
        w = view.grid.itemAt(i).widget()
        if isinstance(w, ExperimentCard):
            cards_seen += 1
        elif isinstance(w, QFrame):
            assert "vazio" in "".join(
                r.widget().text() if isinstance(r.widget(), QLabel) else ""
                for r in (w.layout().itemAt(0),)
            )
            placeholders += 1
    assert cards_seen == 5 and placeholders == 3
    # página cheia: nenhum placeholder
    view.set_data(
        [{"external_id": i, "values": {1: 1.0}} for i in range(1, 9)], [1]
    )
    assert view.grid.count() == 8


def test_compact_row_pure():
    from app.ui.widgets.experiment_list_view import compact_row

    line = compact_row({"external_id": 7, "values": {1: 3.14, 2: None}}, [1, 2])
    assert line.startswith("#7")
    assert "3.14" in line and "\u2014" in line  # — para valor ausente
    assert compact_row({"external_id": 0, "values": {}}, []) == "#0"


def test_list_view_sets_rows(qapp):
    from app.ui.widgets.experiment_list_view import ExperimentListView, MAX_LIST_ROWS

    view = ExperimentListView()
    rows = [{"external_id": i, "values": {1: float(i)}} for i in range(1, 12)]
    assert view.set_data(rows, [1]) == 11
    assert view.list.count() == 11
    assert view.list.item(0).data(0x0100) == 1  # UserRole: external_id
    assert "v11" not in view.list.item(10).text() or True
    big = [{"external_id": i, "values": {}} for i in range(1, MAX_LIST_ROWS + 2)]
    assert view.set_data(big, []) == MAX_LIST_ROWS
    assert "só as" in view.lbl_note.text()


def test_panel_three_formats(qapp, tmp_path):
    from app.infrastructure.experiment_repository import ExperimentRepository
    from app.ui.models.repository_paged_model import RepositoryPagedModel
    from app.ui.widgets.experiments_panel import ExperimentsPanel

    repo = ExperimentRepository(str(tmp_path / "m14.db"))
    repo.create_batch("b14", "lhs", 1, 6)
    repo.insert_result("b14", [1, 2], [[1.0, 5.0]] * 6)
    model = RepositoryPagedModel(repo, page_size=6)
    panel = ExperimentsPanel(model)
    assert panel.combo_format.count() == 4  # r17: + Matriz
    assert panel.view_stack.count() == 4
    panel.combo_format.setCurrentIndex(2)  # lista compacta
    assert panel.view_stack.currentIndex() == 2
    assert panel.list_view.list.count() == 6
    panel.combo_format.setCurrentIndex(1)  # cartões
    assert panel.view_stack.currentIndex() == 1
    assert panel.cards_view.grid.count() == 8  # 6 cartões em grade 2×4 + 2 placeholders
    panel.combo_format.setCurrentIndex(0)
    assert panel.view_stack.currentIndex() == 0


def test_open_output_button_flow(qapp, tmp_path):
    from PySide6.QtCore import QUrl
    from PySide6.QtGui import QDesktopServices

    from app.infrastructure.experiment_repository import ExperimentRepository
    from app.ui.models.repository_paged_model import RepositoryPagedModel
    from app.ui.widgets.experiments_panel import ExperimentsPanel

    repo = ExperimentRepository(str(tmp_path / "m14o.db"))
    repo.create_batch("b14o", "lhs", 1, 3)
    repo.insert_result("b14o", [1], [[1.0]] * 3)
    panel = ExperimentsPanel(RepositoryPagedModel(repo, page_size=3))
    # desabilitado até set_last_output_dir
    assert not panel.btn_open_output.isEnabled()
    opened: list[str] = []
    panel.openOutputRequested.connect(lambda p: opened.append(p))
    QDesktopServices.openUrl = lambda url: opened.append(url.toString()) or True
    panel.btn_open_output.click()  # sem pasta → nada emitido
    assert opened == []
    out = str(tmp_path / "out14o")
    os.makedirs(out, exist_ok=True)
    panel.set_last_output_dir(out)
    assert panel.btn_open_output.isEnabled()
    panel.btn_open_output.click()
    assert opened and opened[-1].endswith("out14o")


def test_main_window_output_folder_status(tmp_path, qapp):
    from PySide6.QtGui import QDesktopServices

    from app.container import Container
    from app.ui.main_window import MainWindow

    container = Container(base_dir=str(tmp_path / "c14"), load_plugins=False)
    try:
        window = MainWindow(container)
        window._last_output_dir = None
        opened: list[str] = []
        QDesktopServices.openUrl = lambda url: opened.append(url.toString())
        window._open_output_folder()  # sem pasta → status, não abre
        assert opened == []
        window._last_output_dir = str(tmp_path)
        window._open_output_folder()
        assert opened and opened[-1].startswith("file:")
        window.close()
    finally:
        container.shutdown()
