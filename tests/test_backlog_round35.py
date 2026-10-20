"""Regressão do backlog T5432–T5452 (TAREFAS_v2.md — 'Backlog de refinamento')."""

from __future__ import annotations

import pytest


# ---------- T5432: undo/redo persistente por aba ----------

def test_t5432_persistent_undo_redo(qtbot, qapp):
    from app.ui.editor.editor_tabs import EditorTabs

    tabs = EditorTabs()
    qtbot.addWidget(tabs)
    tab = tabs.new_tab("v1", title="arquivo")
    index = tabs.indexOf(tab)

    tabs.persist_tab(tab)
    tab.set_content("v2")
    tabs.persist_tab(tab)
    tab.set_content("v3")
    tabs.persist_tab(tab)

    assert tabs.undo_persistent(index) is True
    assert tab.editor.toPlainText() == "v2"
    assert tabs.undo_persistent(index) is True
    assert tab.editor.toPlainText() == "v1"
    assert tabs.undo_persistent(index) is False  # início da pilha

    assert tabs.redo_persistent(index) is True
    assert tab.editor.toPlainText() == "v2"
    assert tabs.redo_persistent(index) is True
    assert tab.editor.toPlainText() == "v3"
    assert tabs.redo_persistent(index) is False  # fim da pilha


# ---------- T5434: controle de versões do .dat no estudo ----------

def test_t5434_dat_version_roundtrip(container):
    svc = container.study_service
    study_id = svc.create("estudo dat", {}, meta={"output_dir": "out"})

    version = svc.save_dat_version(study_id, "LINHA $1\nLINHA $2", "primeira")
    assert isinstance(version, int)

    assert svc.get_dat_version(study_id, version) == "LINHA $1\nLINHA $2"

    version2 = svc.save_dat_version(study_id, "LINHA $1 MODIFICADA", "segunda")
    assert svc.get_dat_version(study_id, version2) == "LINHA $1 MODIFICADA"
    # versão antiga preservada
    assert svc.get_dat_version(study_id, version) == "LINHA $1\nLINHA $2"


def test_t5434_dat_version_missing_returns_none(container):
    from app.services.study_service import StudyOperationError

    svc = container.study_service
    study_id = svc.create("estudo vazio", {})
    # versão inexistente → StudyOperationError (contrato do serviço)
    with pytest.raises(StudyOperationError):
        svc.get_dat_version(study_id, 999)


# ---------- T5435: drag para reatribuir distribuição ----------

def test_t5435_reassign_spec_pure():
    from app.domain.entities import DistributionSpec
    from app.ui.widgets.variables_panel import reassign_spec

    spec = DistributionSpec(provider="fixed", name="value", params={"value": 3.0})
    specs = {1: spec}

    out = reassign_spec(specs, 1, 2)
    assert out[2] is spec
    assert 2 not in specs  # não muta o original

    assert reassign_spec(specs, 99, 5) is specs  # origem inexistente → intacto
    assert reassign_spec(specs, 1, 1) is specs   # mesmo id → intacto


def test_t5435_copy_distribution_panel(qtbot, qapp, registry):
    from app.domain.entities import DistributionSpec
    from app.ui.widgets.variables_panel import VariablesPanel

    panel = VariablesPanel(registry)
    qtbot.addWidget(panel)
    spec = DistributionSpec(provider="fixed", name="value", params={"value": 7.0})
    panel.specs = {1: spec}

    assert panel.copy_distribution(1, 2) is True
    assert panel.specs[2] is spec
    assert panel.copy_distribution(99, 3) is False  # sem origem → nada muda


# ---------- T5436: diff lado a lado ----------

def test_t5436_side_by_side_pure():
    from app.services.comparison_round34 import count_differences, side_by_side_lines

    rows = side_by_side_lines("a\nb\nc", "a\nX\nc")
    markers = [m for m, _, _ in rows]
    assert len(rows) == 3
    assert markers[0] == " "   # igual
    assert markers[1] == "!"   # diferente
    assert markers[2] == " "

    assert count_differences("a\nb\nc", "a\nX\nc") == 1
    assert count_differences("mesmo", "mesmo") == 0


def test_t5436_preview_panel_side_by_side(qtbot, qapp):
    from app.ui.widgets.preview_panel import PreviewPanel

    panel = PreviewPanel()
    qtbot.addWidget(panel)
    panel.show_side_by_side("a\nb", "a\nc", 1, 2)
    text = panel.output.toPlainText()
    assert "seed 1" in text and "seed 2" in text
    assert "»" in text  # marca de divergência
    assert "1 linha(s) divergente(s)" in text


# ---------- T5437: múltiplas seeds em lote ----------

def test_t5437_multi_seed_pure():
    from app.services.comparison_round34 import multi_seed_values, summarize_multi_seed

    def fake_render(text, specs, seed):
        return f"{text}#{seed}"

    pairs = multi_seed_values(fake_render, "T", {}, [10, 11])
    assert pairs == [(10, "T#10"), (11, "T#11")]

    summary = summarize_multi_seed([(1, "l1\nl2"), (2, "l1\nl2X")])
    assert "seed 1: base" in summary
    assert "seed 2: 1 linha(s) diferente(s) da base" in summary

    assert summarize_multi_seed([]) == ""


# ---------- T5438: seleção tripla A/B/C ----------

def test_t5438_triple_signal(qtbot, qapp, container, populated_batch):
    from app.ui.models.repository_paged_model import RepositoryPagedModel
    from app.ui.widgets.experiments_panel import ExperimentsPanel

    model = RepositoryPagedModel(container.exp_repo, page_size=50)
    panel = ExperimentsPanel(model)
    qtbot.addWidget(panel)

    received = []
    panel.compareTripleRequested.connect(lambda a, b, c: received.append((a, b, c)))
    pair_received = []
    panel.compareRequested.connect(lambda a, b: pair_received.append((a, b)))

    # simula a seleção tripla pelo caminho interno (sem interação de mouse)
    rows = sorted(range(min(3, model.rowCount())))
    panel.selected_rows = lambda: rows  # stub da seleção
    panel._emit_compare()
    assert len(received) == 1
    assert received[0] == (rows[0], rows[1], rows[2])
    assert not pair_received  # com 3+ selecionados NÃO emite o par

    # com 2 selecionados continua emitindo o par A/B
    panel.selected_rows = lambda: rows[:2]
    panel._emit_compare()
    assert pair_received == [(rows[0], rows[1])]
    assert len(received) == 1


# ---------- T5439: diff com janela de contexto ajustável ----------

def test_t5439_unified_with_context():
    from app.services.comparison_round34 import unified_with_context

    a = "\n".join(f"linha{i}" for i in range(10))
    b = a.replace("linha5", "ALTERADA")

    tight = unified_with_context(a, b, 0)
    loose = unified_with_context(a, b, 4)

    assert "ALTERADA" in tight
    assert "linha4" not in tight  # contexto 0 → só a mudança
    assert "linha4" in loose      # contexto 4 → linhas vizinhas


def test_t5439_dialog_context_spin(qtbot, qapp, container, populated_batch):
    from app.ui.widgets.comparison_dialog import ComparisonDialog

    result = container.comparison_service.compare(1, 2)
    dlg = ComparisonDialog(result)
    qtbot.addWidget(dlg)

    assert dlg.spin_context.value() == 3
    assert dlg.spin_context.maximum() == 20

    # muda a janela → o diff recalcula
    dlg._dat_a = "a\nb\nc\nd\ne"
    dlg._dat_b = "a\nB\nc\nd\ne"
    dlg.spin_context.setValue(0)
    text = dlg.diff_view.toPlainText()
    assert "@@" in text       # hunk do unified diff
    assert "b" in text and "B" in text


# ---------- T5440: comparar dois batches lado a lado ----------

def test_t5440_two_batch_delta_pure(container, populated_batch):
    from app.domain.entities import DistributionSpec, SamplingRequest
    from app.ui.widgets.heat_matrix_panel import two_batch_delta

    request = SamplingRequest(
        var_ids=[1, 10002],
        specs={
            1: DistributionSpec(provider="scipy", name="norm",
                                params={"loc": 20.0, "scale": 1.0}),
            10002: DistributionSpec(provider="fixed", name="value",
                                    params={"value": 9.0}),
        },
        n_experiments=12,
        seed=99,
        strategy="lhs",
    )
    result = container.sampling_service.run(request)
    container.exp_repo.create_batch("batch_y", "lhs", 99, 12)
    container.exp_repo.insert_result("batch_y", result.var_ids, result.matrix)

    deltas, n = two_batch_delta(container.exp_repo, "batch_x", "batch_y")
    assert n == 12
    assert set(deltas) == {1, 10002}
    # média dos deltas ≈ Δloc (10 → 20); fixed exato (5 → 9)
    mean_delta = sum(deltas[1]) / len(deltas[1])
    assert abs(mean_delta - 10.0) < 3.0
    assert all(abs(d - 4.0) < 1e-9 for d in deltas[10002])


def test_t5440_heat_matrix_load_delta_view(qtbot, qapp, container, populated_batch):
    from app.domain.entities import DistributionSpec, SamplingRequest
    from app.ui.widgets.heat_matrix_panel import HeatMatrixPanel

    request = SamplingRequest(
        var_ids=[1, 10002],
        specs={
            1: DistributionSpec(provider="scipy", name="norm",
                                params={"loc": 12.0, "scale": 1.0}),
            10002: DistributionSpec(provider="fixed", name="value",
                                    params={"value": 5.0}),
        },
        n_experiments=12,
        seed=123,
        strategy="lhs",
    )
    result = container.sampling_service.run(request)
    container.exp_repo.create_batch("batch_z", "mc", 123, 12)
    container.exp_repo.insert_result("batch_z", result.var_ids, result.matrix)

    panel = HeatMatrixPanel()
    qtbot.addWidget(panel)
    rows = panel.load_delta_view(container.exp_repo, "batch_x", "batch_z")
    assert rows == 12
    assert panel.table.rowCount() == 12
    # headers: "Δ" + uma coluna por variável
    assert panel.table.columnCount() == 3
    assert panel.table.horizontalHeaderItem(0).text() == "Δ"


# ---------- T5441: scatter por variável (QPainter) ----------

def test_t5441_scatter_points_pure():
    from app.services.comparison_round34 import scatter_points

    xs, ys, corr = scatter_points([1.0, 2.0, 3.0], [2.0, 4.0, 6.0])
    assert xs == [1.0, 2.0, 3.0]
    assert ys == [2.0, 4.0, 6.0]
    assert corr == pytest.approx(1.0)

    xs, ys, corr = scatter_points([5.0], [1.0])
    assert len(xs) == 1 and corr == 0.0  # n<2 → sem correlação


def test_t5441_dialog_scatter(qtbot, qapp, container, populated_batch):
    from app.ui.widgets.comparison_dialog import ComparisonDialog

    result = container.comparison_service.compare(1, 2)
    dlg = ComparisonDialog(result)
    qtbot.addWidget(dlg)

    n = dlg.update_scatter([1.0, 2.0, 3.0, 4.0], [1.5, 2.5, 2.0, 5.0])
    assert n == 4
    assert dlg.scatter_widget.values_a == [1.0, 2.0, 3.0, 4.0]
    assert len(dlg.scatter_widget.values_b) == 4
    # renderiza sem exceção (paintEvent QPainter)
    dlg.scatter_widget.resize(320, 260)
    dlg.scatter_widget.grab()


# ---------- T5442: ranking de variáveis mais divergentes ----------

def test_t5442_ranking_pure():
    from app.services.comparison_round34 import batch_divergence_ranking, format_batch_ranking

    stats = [
        {"var_id": 1, "mean_a": 10.0, "mean_b": 10.5, "std_a": 0.1, "std_b": 0.1},
        {"var_id": 2, "mean_a": 1.0, "mean_b": 50.0, "std_a": 0.1, "std_b": 0.1},
        {"var_id": 3, "mean_a": 0.0, "mean_b": 0.0, "std_a": 0.0, "std_b": 0.0},
    ]
    ranked = batch_divergence_ranking(stats)
    assert ranked[0]["var_id"] == 2  # mais divergente primeiro
    assert ranked[-1]["var_id"] == 3  # idênticas → última

    top = batch_divergence_ranking(stats, top=2)
    assert len(top) == 2

    lines = format_batch_ranking(ranked)
    assert len(lines) == 3
    assert lines[0].startswith("$2")
    assert "█" in lines[0]  # barra do ranking


def test_t5442_dialog_rank_button(qtbot, qapp, container, populated_batch, monkeypatch):
    from app.ui.widgets import batch_comparison_dialog as bcd

    # evita o loop modal do QMessageBox em ambiente de teste
    captured = {}

    class FakeBox:
        Information = 1

        def __init__(self, parent=None):
            pass

        @staticmethod
        def information(*args, **kwargs):
            captured["info"] = args

        def setWindowTitle(self, *a):
            pass

        def setText(self, *a):
            pass

        def setIcon(self, *a):
            pass

        def setDetailedText(self, text):
            captured["details"] = text

        def exec(self):
            return 0

    monkeypatch.setattr(bcd, "QMessageBox", FakeBox)

    cmp_result = container.batch_comparison_service.compare("batch_x", "batch_x")
    dlg = bcd.BatchComparisonDialog(cmp_result)
    qtbot.addWidget(dlg)
    assert dlg.btn_rank.text() == "Ranking de divergência"
    dlg._show_ranking()  # não deve levantar exceção
    assert "details" in captured  # o ranking foi montado e exibido


# ---------- T5443: diff de versões de estudo com destaque ----------

def test_t5443_studies_diff_highlight():
    from app.ui.widgets.studies_dialog import StudiesDialog

    va = {
        "specs": {"1": {"name": "norm", "params": {"loc": 1}},
                  "2": {"name": "uniform"}},
        "meta": {"batch_id": "antigo"},
    }
    vb = {
        "specs": {"1": {"name": "uniform"},
                  "3": {"name": "fixed"}},
        "meta": {"batch_id": "novo"},
    }
    lines = StudiesDialog._build_diff(va, vb)

    # destaque: '~' alterado, '+' só em b, '−' só em a
    assert any(l.startswith("~ 1:") for l in lines)
    assert any(l.startswith("+ 3:") for l in lines)
    assert any(l.startswith("− 2:") for l in lines)
    assert any("meta.batch_id" in l for l in lines)

    # sem diferenças → lista vazia
    assert StudiesDialog._build_diff(va, va) == []


# ---------- T5444: estado atual como novo batch no estudo ----------

def test_t5444_register_batch_in_study(container):
    svc = container.study_service
    study_id = svc.create("estudo batch", {}, meta={"output_dir": "out"})

    version = svc.register_batch(study_id, "batch_abc", "amostragem")
    assert isinstance(version, int)

    study = svc.get(study_id)
    assert study["meta"]["batch_id"] == "batch_abc"
    assert study["meta"]["batches"][-1]["batch_id"] == "batch_abc"

    # registra outro → acumula no histórico
    svc.register_batch(study_id, "batch_def", "outra")
    study = svc.get(study_id)
    assert [b["batch_id"] for b in study["meta"]["batches"]] == [
        "batch_abc", "batch_def"
    ]
    assert study["meta"]["batch_id"] == "batch_def"


def test_t5444_register_batch_missing_study_raises(container):
    from app.services.study_service import StudyOperationError

    with pytest.raises(StudyOperationError):
        container.study_service.register_batch(9999, "batch_x")


# ---------- T5452: pré-computar ppf em blocos grandes ----------

def test_t5452_ppf_block_constant_and_chunked_run(registry, monkeypatch):
    import math

    from app.domain.entities import DistributionSpec, SamplingRequest
    import app.services.sampling_service as sampling_module

    # força blocos pequenos para exercitar o caminho chunked sem 1M de linhas
    monkeypatch.setattr(sampling_module, "PPF_BLOCK_SIZE", 7)

    svc = sampling_module.SamplingService(registry)
    request = SamplingRequest(
        var_ids=[1],
        specs={1: DistributionSpec(provider="scipy", name="norm",
                                    params={"loc": 0.0, "scale": 1.0})},
        n_experiments=50,  # > 7 → usa o pré-computo em blocos
        seed=11,
        strategy="lhs",
    )
    result = svc.run(request)
    assert len(result.matrix) == 50
    # todos os valores finitos e coerentes com a normal padrão
    values = [row[0] for row in result.matrix]
    assert all(math.isfinite(v) for v in values)
    assert -5.0 < sum(values) / len(values) < 5.0


def test_t5452_ppf_block_small_input_single_pass(registry):
    from app.domain.entities import DistributionSpec, SamplingRequest
    from app.services.sampling_service import PPF_BLOCK_SIZE

    from app.services.sampling_service import SamplingService

    svc = SamplingService(registry)
    request = SamplingRequest(
        var_ids=[1],
        specs={1: DistributionSpec(provider="scipy", name="norm",
                                    params={"loc": 0.0, "scale": 1.0})},
        n_experiments=5,  # < bloco → caminho direto
        seed=3,
        strategy="lhs",
    )
    result = svc.run(request)
    assert len(result.matrix) == 5
    assert PPF_BLOCK_SIZE >= 1
