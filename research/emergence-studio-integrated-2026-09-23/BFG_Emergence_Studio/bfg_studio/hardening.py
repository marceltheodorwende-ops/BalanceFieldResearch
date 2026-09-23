from __future__ import annotations

from pathlib import Path
import json

from .benchmarks import run_benchmark_suite, write_benchmark_report
from .robustness import run_robustness_suite, write_robustness_report
from .seeds import make_random_seed_state
from .carrier import ReferenceGramCarrier
from .simulate import simulate
from .stability import run_master_stability_audit, write_stability_audit
from .source_integration import run_github_math_integration_audit, write_github_math_integration_audit
from .session import (
    ProvenanceManifest,
    save_bfg_checkpoint,
    load_bfg_checkpoint,
)


def run_hardening(
    outdir:str|Path,
    randomized_trials:int=200,
    seed:int=20260923,
    workers:int|None=None,
):
    outdir=Path(outdir)
    outdir.mkdir(parents=True,exist_ok=True)

    benchmark=run_benchmark_suite()
    benchmark_files=write_benchmark_report(
        benchmark,outdir/"benchmarks"
    )

    robustness=run_robustness_suite(
        randomized_trials=randomized_trials,
        commuting_controls=40,
        noncommuting_controls=40,
        seed=seed,
        workers=workers,
    )
    robustness_files=write_robustness_report(
        robustness,outdir/"robustness"
    )

    stability=run_master_stability_audit(
        horizon=64,
    )
    stability_files=write_stability_audit(
        stability,outdir/"stability"
    )

    source_math=run_github_math_integration_audit()
    source_math_files=write_github_math_integration_audit(
        source_math,outdir/"source_math"
    )

    # Genuine save -> load -> continue roundtrip.
    initial=make_random_seed_state(dim=6,persistent_rank=4,seed=17)
    pre=simulate(initial,ReferenceGramCarrier(),steps=2)
    checkpoint_state=pre.states[-1]
    manifest=ProvenanceManifest.build(
        experiment="hardening_checkpoint_roundtrip",
        seed=17,
        parameters={"pre_steps":2,"post_steps":2},
    )
    checkpoint_files=save_bfg_checkpoint(
        checkpoint_state,
        outdir/"checkpoint",
        name="master_state",
        manifest=manifest,
        extra={"pre_summary":pre.summary()},
    )
    loaded,loaded_manifest,extra=load_bfg_checkpoint(
        outdir/"checkpoint",name="master_state"
    )
    post=simulate(loaded,ReferenceGramCarrier(),steps=2)

    checkpoint_pass=(
        loaded.generation==checkpoint_state.generation
        and loaded.dim==checkpoint_state.dim
        and post.states[0].generation==checkpoint_state.generation
        and len(post.steps)>=1
    )

    summary={
        "hardening_passed":bool(
            benchmark.passed
            and robustness.passed
            and stability["audit_passed"]
            and source_math["audit_passed"]
            and checkpoint_pass
        ),
        "benchmark_passed":benchmark.passed,
        "robustness_passed":robustness.passed,
        "recursive_stability_audit_passed":stability["audit_passed"],
        "github_math_integration_audit_passed":source_math["audit_passed"],
        "checkpoint_roundtrip_passed":checkpoint_pass,
        "benchmark_count":len(benchmark.results),
        "randomized_trials":robustness.randomized_trials,
        "source_fingerprint":benchmark.source_fingerprint,
        "checkpoint_loaded_generation":loaded.generation,
        "checkpoint_post_steps":len(post.steps),
        "benchmark_files":benchmark_files,
        "robustness_files":robustness_files,
        "stability_files":stability_files,
        "source_math_files":source_math_files,
        "checkpoint_files":checkpoint_files,
    }
    summary_path=outdir/"hardening_summary.json"
    summary_path.write_text(
        json.dumps(summary,indent=2,default=str),
        encoding="utf-8"
    )
    return summary
