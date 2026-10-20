"""Testes do export em lote: chunking, manifest, checkpoint e stop."""

from pathlib import Path


def test_export_all_files_and_manifest(container, populated_batch):
    out_root = container.base_dir / "out"
    manifest = container.batch_export_service.export(
        populated_batch["batch_id"], populated_batch["version_id"], out_root
    )
    assert manifest.n_files == 12
    assert manifest.template_version_number == 1
    files = sorted(Path(manifest.output_dir).glob("*.dat"))
    assert len(files) == 12
    assert files[0].name == "experimento_000001.dat"
    manifest_file = Path(manifest.manifest_path)
    assert manifest_file.exists()
    contents = manifest_file.read_text(encoding="utf-8").splitlines()
    assert len(contents) == 13  # header + 12


def test_export_checkpoint_can_resume(container, populated_batch):
    captured_checkpoints = []

    manifest = container.batch_export_service.export(
        populated_batch["batch_id"],
        populated_batch["version_id"],
        container.base_dir / "out_full",
        checkpoint_cb=lambda done, last_id: captured_checkpoints.append(last_id),
    )
    assert captured_checkpoints, "checkpoint_cb nunca chamado"
    last_id = captured_checkpoints[-1]

    second = container.batch_export_service.export(
        populated_batch["batch_id"],
        populated_batch["version_id"],
        container.base_dir / "out_resume",
        start_external_id=last_id + 1,
    )
    names_full = {p.name for p in Path(manifest.output_dir).glob("*.dat")}
    names_resume = {p.name for p in Path(second.output_dir).glob("*.dat")}
    assert not (names_full & names_resume)
    assert second.n_files == 12 - last_id


def test_export_stop_check(container, populated_batch):
    calls = {"n": 0}

    def stop():
        calls["n"] += 1
        return calls["n"] > 3

    import pytest

    with pytest.raises(InterruptedError):
        container.batch_export_service.export(
            populated_batch["batch_id"], populated_batch["version_id"],
            container.base_dir / "out_stop", stop_check=stop,
        )


def test_export_raises_for_missing_version(container):
    import pytest

    with pytest.raises(ValueError):
        container.batch_export_service.export("b", 999, container.base_dir / "out_none")


def test_export_empty_batch_raises(container):
    import pytest

    container.template_repo.create_template("vazio")
    vid = container.template_repo.save_version(1, "sem nada $1")
    with pytest.raises(ValueError):
        container.batch_export_service.export("nada", vid, container.base_dir / "out_empty")
