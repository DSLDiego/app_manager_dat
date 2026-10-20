"""Regressões da rodada 4: otimizações, plots, matriz n×m e sistema de estudos."""

import json
import time
from pathlib import Path

import numpy as np
import pytest

pytest.importorskip("pytestqt")


def _repo(tmp_path):
    from app.infrastructure.experiment_repository import ExperimentRepository

    return ExperimentRepository(str(tmp_path / "exp.db"))


def _populate(repo, batch, n, var_ids=(1, 10002)):
    repo.create_batch(batch, "sampling", 1, n)
    matrix = [[float(i + 1) for _ in var_ids] for i in range(n)]
    repo.insert_result(batch, list(var_ids), matrix)


# ---------- (3) otimizações: TemplateCompiler ----------
def test_compiled_template_matches_render_template():
    from app.core.parsing import compile_template, render_template

    text = "PVAR $1 NLTP $2 COMPFLAGLR $var2/$var1 * &$1.5 '<REV1' $v1"
    values = {1: 1.5, 2: 0.001, 10001: 12.0, 10002: 3.75}
    compiled = compile_template(text)
    assert compiled.render(values) == render_template(text, values)


def test_compiled_template_missing_value():
    from app.core.parsing import compile_template

    compiled = compile_template("X $1 Y $var2")
    with pytest.raises(ValueError, match="sem valor definido"):
        compiled.render({1: 0.0})


def test_compiled_template_render_is_fast_and_correct():
    from app.core.parsing import compile_template, render_template

    text = "\n".join(
        f"keyword_bloc_$i $var{i} auxiliar &$1 {i}" for i in range(1, 201)
    )
    values = {i: 2.5 for i in range(1, 201)} | {10_000 + i: 3.75 for i in range(1, 201)}
    compiled = compile_template(text)
    assert compiled.render(values) == render_template(text, values)

    t0 = time.perf_counter()
    for _ in range(2000):
        compiled.render(values)
    elapsed = time.perf_counter() - t0
    # render compilado precisa ser rápido (< 10s p/ 2k renders, tipicamente < 1s)
    assert elapsed < 10.0


def test_batch_export_uses_compiler(container, populated_batch):
    template_text = container.template_repo.get_version(populated_batch["version_id"])["content"]
    out = container.base_dir / "out_compiled"
    manifest = container.batch_export_service.export(
        populated_batch["batch_id"], populated_batch["version_id"], out
    )
    assert manifest.n_files == 12
    raw = next(iter(sorted(out.glob("**/*.dat"))))
    assert "$1" not in raw.read_text(encoding="utf-8")
    assert populated_batch["batch_id"] == "batch_x"


def test_batch_export_falls_back_to_injected_renderer(container, populated_batch):
    from app.services.batch_export_service import BatchExportService

    calls = []

    def custom(template, values):
        calls.append(1)
        return "X"

    svc = BatchExportService(container.exp_repo, container.template_repo, renderer=custom)
    assert svc._compile("t $1") is None  # renderer injetado: sem compilador
    out = container.base_dir / "out_custom"
    manifest = svc.export(populated_batch["batch_id"], populated_batch["version_id"], out)
    assert manifest.n_files == 12
    assert len(calls) == 12
    raw = next(iter(sorted(out.glob("**/*.dat"))))
    assert raw.read_text(encoding="utf-8") == "X"


# ---------- (3) insert_result em lote contínuo ----------
def test_bulk_insert_ids_continue_across_batches(tmp_path):
    repo = _repo(tmp_path)
    _populate(repo, "b1", 5)
    rows = repo.fetch_page(0, 10)
    assert len(rows) == 5
    _populate(repo, "b2", 3)
    rows = repo.fetch_page(0, 10)
    assert len(rows) == 8
    # os dois lotes convivem no mesmo banco (ids externos recomeçam em cada lote)
    assert sorted(r["external_id"] for r in rows) == [1, 1, 2, 2, 3, 3, 4, 5]
    repo.close()


def test_bulk_insert_1k_perf(tmp_path):
    repo = _repo(tmp_path)
    _populate(repo, "big", 1000)
    assert repo.count() == 1000
    rows = repo.fetch_page(1, 500, [1, 10002])  # 2ª página de 500
    assert len(rows) == 500
    assert rows[-1]["external_id"] == 1000
    assert rows[-1]["values"] == {10002: 1000.0, 1: 1000.0}
    repo.close()


# ---------- (2) gráficos ----------
def test_safe_eval_function_and_forbidden():
    from app.ui.widgets.distribution_plot_dialog import safe_eval_function

    f = safe_eval_function("x**2 + np.sin(x)")
    ys = f(np.array([0.0, 1.0]))
    assert ys[0] == pytest.approx(0.0)
    assert ys[1] == pytest.approx(1.0 + np.sin(1.0))


def test_safe_eval_forbidden_import():
    from app.ui.widgets.distribution_plot_dialog import validate_function

    assert validate_function("import os") is not None  # bloqueia
    assert validate_function("__import__('os')") is not None
    assert validate_function("exec('x')") is not None  # nome livre bloqueado
    assert validate_function("x**2") is None


def test_plot_dialog_spec_series_smoke(qtbot, tmp_path):
    from PySide6.QtGui import QImage
    from PySide6.QtWidgets import QApplication

    QApplication.instance() or QApplication([])
    from app.infrastructure.distribution_registry import build_default_registry
    from app.ui.widgets.distribution_plot_dialog import DistributionPlotDialog

    registry = build_default_registry()
    dialog = DistributionPlotDialog(registry)
    assert dialog.combo_distcombo.count() > 0

    # escolhe norma da lista e desenha
    code_opt = [i for i in range(dialog.combo_distcombo.count())
                if dialog.combo_distcombo.itemText(i) == "scipy.norm"]
    assert code_opt, "norm rpm não disponível no dialog"
    dialog.combo_distcombo.setCurrentIndex(code_opt[0])
    series = dialog._series_for_spec("scipy.norm", bars=False)
    assert series and np.isfinite(np.asarray(series[0][2])).all()
    dialog.redraw()

    img = QImage(400, 300, QImage.Format.Format_ARGB32)
    dialog.canvas.render(img)
    assert not img.isNull()

    # barras a partir de amostra fixa
    series_fixed = dialog._series_for_spec("fixed.value", bars=True)
    assert len(series_fixed) == 1 and series_fixed[0][3]


def test_plot_dialog_user_function(qtbot, tmp_path):
    from PySide6.QtWidgets import QApplication

    QApplication.instance() or QApplication([])
    from app.ui.widgets.distribution_plot_dialog import DistributionPlotDialog

    dialog = DistributionPlotDialog(None)
    dialog.combo_kind.setCurrentIndex(2)
    series = dialog._series_for_user_function()
    assert series
    label, xs, ys, valid = series[0]
    assert valid
    assert ys.max() > 30  # x² até 10
    assert label == "f(x)"


# ---------- (1) matriz n×m ----------
def test_heat_matrix_panel(qtbot, tmp_path):
    from PySide6.QtWidgets import QApplication

    QApplication.instance() or QApplication([])
    from app.ui.widgets.heat_matrix_panel import HeatMatrixPanel, color_for_value

    repo = _repo(tmp_path)
    _populate(repo, "b1", 30)
    panel = HeatMatrixPanel()
    panel.load_from_repo(repo)
    assert panel.table.columnCount() == 3
    assert panel.table.rowCount() == 30
    assert panel.table.horizontalHeaderItem(0).text() == "#"
    assert panel.table.horizontalHeaderItem(2).text() == "$var2"
    assert panel.lbl_info.text().startswith("Matriz 30×2")

    # células pintadas com cor válida (gradiente)
    assert panel.table.item(0, 1).background().color().isValid()
    assert panel.table.item(0, 0).background().color().isValid()

    # gradiente monotônico na escala de valor
    blue = color_for_value(0.0, 0.0, 10.0)
    yellow = color_for_value(10.0, 0.0, 10.0)
    assert blue.red() < yellow.red() and blue.green() < yellow.green()
    mid = color_for_value(5.0, 0.0, 10.0)
    assert blue.red() < mid.red() < yellow.red()

    # sem dados
    from app.infrastructure.experiment_repository import ExperimentRepository as ER

    empty = ER(str(tmp_path / "empty2.db"))
    panel.load_from_repo(empty)
    assert panel.lbl_info.text() == "Matriz sem dados"


def test_matrix_panel_in_main_window(main_window_offscreen, qtbot):
    window = main_window_offscreen
    state = window._current_study_state()
    assert state.get("template_text") is not None  # editor novo tem texto vazio
    # arrange não deve explodir
    window._arrange_docks_grid()


# ---------- (4) estudos ----------
def _reg():
    from app.infrastructure.study_repository import StudyRepository

    return StudyRepository(":memory:")


def test_study_service_crud_and_duplicate():
    from app.services.study_service import StudyOperationError, StudyService
    from app.domain.entities import DistributionSpec

    svc = StudyService(_reg())
    specs = {
        1: DistributionSpec(provider="scipy", name="norm", params={"loc": 1, "scale": 0.5}),
        10002: DistributionSpec(provider="fixed", name="value", params={"value": 2}),
    }
    study_id = svc.create("Estudo A", specs, meta={"batch_id": "b1", "output_dir": "out/"})
    assert study_id > 0
    stored = svc.get(study_id)
    assert stored["name"] == "Estudo A"
    assert stored["specs"]["1"]["provider"] == "scipy"
    assert stored["specs"]["10002"]["params"] == {"value": 2}
    assert stored["meta"]["batch_id"] == "b1"
    assert len(svc.list_studies()) == 1

    with pytest.raises(StudyOperationError):
        svc.create("Estudo A", specs)  # nome repetido
    with pytest.raises(StudyOperationError):
        svc.create("   ", specs)  # nome vazio

    assert svc.delete(study_id)
    assert svc.list_studies() == []
    assert not svc.delete(study_id)


def test_study_versioning_snapshots():
    from app.services.study_service import StudyService
    from app.domain.entities import DistributionSpec

    svc = StudyService(_reg())
    specs_v1 = {1: DistributionSpec(provider="scipy", name="norm", params={"loc": 0})}
    study_id = svc.create("E", specs_v1, meta={"x": 1})

    # snapshot inicial (v1) + um novo snapshot v2 com specs modificados
    specs_v2 = {1: DistributionSpec(provider="scipy", name="uniform", params={"a": -1})}
    svc.save(study_id, specs_v2, meta={"x": 2})
    assert svc.snapshot(study_id, "adaptado para outro bloco") == 2

    history = svc.list_versions(study_id)
    assert history[0]["version_number"] == 2
    assert history[1]["version_number"] == 1

    v1 = svc.get_version(study_id, 1)
    assert v1["specs"]["1"]["name"] == "norm"
    assert v1["meta"]["x"] == 1
    v2 = svc.get_version(study_id, 2)
    assert v2["specs"]["1"]["name"] == "uniform"


def test_study_clone_with_overrides():
    from app.services.study_service import StudyService
    from app.domain.entities import DistributionSpec

    svc = StudyService(_reg())
    specs = {
        1: DistributionSpec(provider="scipy", name="norm", params={"loc": 0, "scale": 1}),
        10002: DistributionSpec(provider="fixed", name="value", params={"value": 9}),
    }
    study_id = svc.create("base", specs, meta={"batch_id": "b1", "output_dir": "old"})
    clone_id = svc.clone(
        study_id, "adaptado",
        meta_overrides={"batch_id": "b_novo", "output_dir": "novo"},
        specs_overrides={10002: DistributionSpec(provider="fixed", name="value", params={"value": 0})},
    )
    clone = svc.get(clone_id)
    assert clone["name"] == "adaptado"
    assert clone["meta"]["batch_id"] == "b_novo"
    assert clone["meta"]["output_dir"] == "novo"
    assert clone["specs"]["1"]["params"] == {"loc": 0, "scale": 1}  # herda
    assert clone["specs"]["10002"]["params"] == {"value": 0}  # overridden


def test_study_export_import_roundtrip(tmp_path):
    from app.services.study_service import StudyOperationError, StudyService
    from app.domain.entities import DistributionSpec

    svc = StudyService(_reg())
    specs = {1: DistributionSpec(provider="scipy", name="norm", params={"loc": 5})}
    study_id = svc.create("Estudinho", specs, meta={"batch_id": "b1"})
    svc.snapshot(study_id, "v1")
    out = tmp_path / "study.json"
    svc.export(study_id, out)

    other = StudyService(_reg())
    import_id = other.import_study(out)
    assert import_id > 0
    imported = other.get(import_id)
    assert imported["name"] == "Estudinho"
    assert "norm" == imported["specs"]["1"]["name"]

    with pytest.raises(StudyOperationError):
        other.import_study(out)  # colisão no mesmo banco
    renamed_id = other.import_study(out, new_name="Estudinho 2")
    assert other.get(renamed_id)["name"] == "Estudinho 2"


def test_studies_dialog_signals(qtbot, tmp_path):
    from PySide6.QtWidgets import QApplication

    QApplication.instance() or QApplication([])
    from app.services.study_service import StudyService
    from app.domain.entities import DistributionSpec
    from app.ui.widgets.studies_dialog import StudiesDialog

    svc = StudyService(_reg())
    specs = {1: DistributionSpec(provider="scipy", name="norm", params={"loc": 0})}
    svc.create("S1", specs, meta={"batch_id": "b1", "output_dir": "out"})
    dialog = StudiesDialog(svc)
    texts = [dialog.list_widget.item(i).text() for i in range(dialog.list_widget.count())]
    assert any("S1" in text for text in texts)

    loaded = []
    dialog.studyLoaded.connect(loaded.append)
    dialog.list_widget.setCurrentRow(0)
    dialog._load_selected()
    assert loaded == [1]


def test_container_has_study_service(container):
    assert container.study_service is not None
    assert container.study_repo is not None
    studies = container.study_service.list_studies()
    assert studies == []


def test_main_window_load_and_create_study(main_window_offscreen, qtbot):
    window = main_window_offscreen

    # prepara estado: template com variáveis, uma dist. atribuída e um batch
    editor = window.editor_tabs.current_editor()
    editor.set_content("PVAR $1 NLTP $2\n")
    from app.domain.entities import DistributionSpec

    window.variables_panel.specs[1] = DistributionSpec(
        provider="fixed", name="value", params={"value": 2.0}
    )
    window.variables_panel.update_tokens(editor.text())
    window.container.exp_repo.create_batch("b_atual", "sampling", 1, 0)
    window._last_batch_id = "b_atual"

    state = window._current_study_state()
    assert state["template_text"].startswith("PVAR")
    assert state["batch_id"] == "b_atual"

    # cria estudo
    window.container.study_service.create(
        "Estudo do Editor",
        window.variables_panel.specs_snapshot(),
        meta=state,
        description="estado atual",
    )
    study = window.container.study_service.find_by_name("Estudo do Editor")

    # carregar em nova aba
    tabs_before = window.editor_tabs.count()
    window._load_study(study["id"])
    assert window.editor_tabs.count() == tabs_before + 1
    new_editor = window.editor_tabs.current_editor()
    assert "$1" in new_editor.text()
    assert 1 in window.variables_panel.specs
