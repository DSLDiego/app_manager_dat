"""Exemplo completo: sampling LHS 10 exps → batch no sqlite → export .dat."""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.container import Container
from app.core.parsing import find_variables
from app.domain.entities import DistributionSpec, SamplingRequest


def main() -> int:
    project_root = ROOT
    spec_file = project_root / "examples" / "variables.json"
    template_file = project_root / "examples" / "template.dat"

    with open(template_file, encoding="utf-8") as f:
        template_text = f.read()
    with open(spec_file, encoding="utf-8") as f:
        config = json.load(f)

    container = Container(base_dir=str(tempfile.mkdtemp(prefix="ds_example_")))
    container.ensure_services()
    var_ids = find_variables(template_text)
    print(f"Variáveis detectadas: ${{{', '.join(str(v) for v in var_ids)}}}")

    specs = {}
    for key, payload in config["specs"].items():
        specs[int(key)] = DistributionSpec(
            provider=payload["provider"],
            name=payload["name"],
            params=payload["params"],
        )
    missing = [v for v in var_ids if v not in specs]
    if missing:
        print(f"[AVISO] Sem spec para: {missing} — usando fixed=0.")
        for v in missing:
            specs[v] = DistributionSpec(provider="fixed", name="value", params={"value": 0})

    request = SamplingRequest(
        var_ids=var_ids,
        specs=specs,
        n_experiments=int(config["n_experiments"]),
        seed=int(config["seed"]),
        strategy=config["strategy"],
    )
    print(f"Amostrando {request.n_experiments} experimentos ({request.strategy})…")
    result = container.sampling_service.run(request, progress_cb=lambda p, m: print(f"  {p}% — {m}"))
    print(f"Matriz: {len(result.matrix)} x {len(result.var_ids)} em {result.duration_seconds:.3f}s")

    batch_id = "example_batch"
    container.exp_repo.create_batch(batch_id, request.strategy, request.seed, len(result.matrix))
    container.exp_repo.insert_result(batch_id, result.var_ids, result.matrix)

    container.template_repo.create_template("example")
    version_id = container.template_repo.save_version(1, template_text, comment="exemplo")

    output_root = project_root / "output"
    manifest = container.batch_export_service.export(
        batch_id, version_id, output_root,
        progress_cb=lambda p, m: print(f"  export {p}% — {m}"),
    )
    print(f"Arquivos .dat: {manifest.n_files}")
    print(f"Saída: {manifest.output_dir}")
    print(f"Manifest: {manifest.manifest_path}")

    container.shutdown()
    return 0


if __name__ == "__main__":
    sys.exit(main())
