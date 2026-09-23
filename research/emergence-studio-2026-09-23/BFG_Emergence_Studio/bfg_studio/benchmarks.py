from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Callable, Any
import csv
import json
import time

from .types import NumericalPolicy
from .core import canonical_reclosure
from .seeds import make_random_seed_state, make_commuting_control_state
from .alife import (
    SelfOrganizationParameters,
    simulate_self_organization,
    organization_metrics,
)
from .population import PopulationParameters, simulate_population
from .evolution import EvolutionParameters, simulate_evolution
from .environment import standard_shift_program, simulate_environmental_evolution
from .learning import LearningParameters, compare_memory_learning
from .selfmodel import SelfModelParameters, compare_self_model
from .perspective import PerspectiveParameters, compare_perspective
from .identity import IdentityParameters, compare_identity
from .session import ProvenanceManifest, save_experiment_ledger


@dataclass
class BenchmarkResult:
    name: str
    passed: bool
    metrics: dict[str, Any]
    criteria: dict[str, Any]
    elapsed_seconds: float
    error: str | None = None


@dataclass
class BenchmarkSuiteReport:
    results: list[BenchmarkResult]
    source_fingerprint: str

    @property
    def passed(self) -> bool:
        return all(r.passed for r in self.results)

    def summary(self) -> dict[str, Any]:
        return {
            "suite_passed": self.passed,
            "benchmarks": len(self.results),
            "passed": sum(int(r.passed) for r in self.results),
            "failed": sum(int(not r.passed) for r in self.results),
            "source_fingerprint": self.source_fingerprint,
            "results": [asdict(r) for r in self.results],
        }


def _run_case(name: str, fn: Callable[[], tuple[bool, dict, dict]]) -> BenchmarkResult:
    start = time.perf_counter()
    try:
        passed, metrics, criteria = fn()
        error = None
    except Exception as exc:
        passed = False
        metrics = {}
        criteria = {}
        error = f"{type(exc).__name__}: {exc}"
    return BenchmarkResult(
        name=name,
        passed=bool(passed),
        metrics=metrics,
        criteria=criteria,
        elapsed_seconds=float(time.perf_counter()-start),
        error=error,
    )


def _canonical_core_case():
    policy=NumericalPolicy()
    noncomm=make_random_seed_state(dim=6,persistent_rank=4,seed=17)
    comm=make_commuting_control_state(dim=6,persistent_rank=4,seed=17)
    a=canonical_reclosure(noncomm,policy)
    b=canonical_reclosure(comm,policy)

    metrics={
        "noncommuting_success":a.success,
        "noncommuting_novelty":bool(a.spectral_novelty),
        "noncommuting_spectral_mismatch":a.spectral_mismatch,
        "commuting_success":b.success,
        "commuting_novelty":bool(b.spectral_novelty),
        "commuting_spectral_mismatch":b.spectral_mismatch,
        "neutral_partition_residual":max(
            float(a.diagnostics.get("neutral_partition_residual",1.0)),
            float(b.diagnostics.get("neutral_partition_residual",1.0)),
        ),
        "reciprocal_balance_residual":max(
            float(a.diagnostics.get("reciprocal_balance_residual",1.0)),
            float(b.diagnostics.get("reciprocal_balance_residual",1.0)),
        ),
    }
    criteria={
        "noncommuting_step_success":True,
        "noncommuting_novelty":True,
        "commuting_spectral_mismatch_max":1e-7,
        "neutral_partition_residual_max":1e-8,
        "reciprocal_balance_residual_max":1e-8,
    }
    passed=(
        a.success
        and bool(a.spectral_novelty)
        and b.success
        and float(b.spectral_mismatch or 1.0) < 1e-7
        and metrics["neutral_partition_residual"] < 1e-8
        and metrics["reciprocal_balance_residual"] < 1e-8
    )
    return passed,metrics,criteria


def _self_organization_case():
    p=SelfOrganizationParameters(node_count=24,persistent_rank=6)
    run=simulate_self_organization(seed=1341550191,steps=18,params=p)
    successful=sum(int(s.success) for s in run.steps)
    novel=sum(int(bool(s.spectral_novelty)) for s in run.steps)
    final=organization_metrics(run.states[-1],p)
    metrics={
        "attempted_steps":len(run.steps),
        "successful_reclosures":successful,
        "novel_reclosures":novel,
        "final_maintenance":final["maintenance_score"],
        "final_viable_fraction":final["viable_fraction"],
        "terminal":run.states[-1].terminal,
    }
    criteria={
        "successful_reclosures_min":16,
        "novel_reclosures_min":12,
        "final_maintenance_min":0.20,
    }
    passed=(
        successful>=16
        and novel>=12
        and final["maintenance_score"]>=0.20
    )
    return passed,metrics,criteria


def _population_case():
    org=SelfOrganizationParameters(node_count=24,persistent_rank=6)
    pop=PopulationParameters(
        min_unit_nodes=4,
        max_unit_nodes=40,
        max_population=12,
        node_birth_threshold=1.10,
        max_node_births_per_step=0,
    )
    run=simulate_population(
        seed=1341550191,generations=22,
        org_params=org,pop_params=pop
    )
    summary=run.summary()
    metrics=dict(summary)
    criteria={
        "fission_events_min":1,
        "max_population_min":2,
        "successful_reclosures_min":16,
    }
    passed=(
        summary["fission_events"]>=1
        and summary["max_population"]>=2
        and summary["successful_reclosures"]>=16
    )
    return passed,metrics,criteria


def _evolution_case():
    org=SelfOrganizationParameters(node_count=24,persistent_rank=6)
    pop=PopulationParameters(
        min_unit_nodes=4,
        max_unit_nodes=40,
        max_population=16,
        node_birth_threshold=1.05,
        max_node_births_per_step=0,
    )
    evo=EvolutionParameters(
        mutation_rate=1.0,
        mutation_sigma=0.03,
        carrying_capacity=8,
        max_candidate_population=16,
        minimum_reproductive_age=5,
    )
    run=simulate_evolution(
        seed=1341550191,generations=24,
        base_org=org,base_pop=pop,evo=evo
    )
    summary=run.summary()
    metrics=dict(summary)
    criteria={
        "unit_birth_events_min":3,
        "mutation_events_min":1,
        "max_lineage_depth_min":1,
        "successful_reclosures_min":18,
    }
    passed=(
        summary["unit_birth_events"]>=3
        and summary["mutation_events"]>=1
        and summary["max_lineage_depth"]>=1
        and summary["successful_reclosures"]>=18
    )
    return passed,metrics,criteria


def _environment_case():
    org=SelfOrganizationParameters(node_count=20,persistent_rank=5)
    pop=PopulationParameters(
        min_unit_nodes=4,max_unit_nodes=32,max_population=24,
        node_birth_threshold=0.95,
    )
    evo=EvolutionParameters(
        mutation_rate=0.8,mutation_sigma=0.05,
        carrying_capacity=10,max_candidate_population=20,
        minimum_reproductive_age=3,
    )
    run=simulate_environmental_evolution(
        seed=11,generations=16,
        program=standard_shift_program(shift_generation=7),
        base_org=org,base_pop=pop,evo=evo,
        founder_count=10,founder_sigma=0.14,
    )
    summary=run.summary()
    selection_rounds=[
        e for e in run.events if e["event"]=="selection_round"
    ]
    positive_selection_gain=max(
        [float(e["match_gain"]) for e in selection_rounds]+[-1.0]
    )
    metrics={
        **summary,
        "selection_rounds":len(selection_rounds),
        "max_selection_match_gain":positive_selection_gain,
    }
    criteria={
        "environment_shifts_min":1,
        "selection_rounds_min":1,
        "positive_match_gain_required":True,
    }
    passed=(
        summary["environment_shifts"]>=1
        and len(selection_rounds)>=1
        and positive_selection_gain>0
    )
    return passed,metrics,criteria


def _learning_case():
    learn=LearningParameters(
        witness_min_gap=4,max_memory_slots=8
    )
    comp=compare_memory_learning(
        seed=1341550191,generations=44,learn=learn
    )
    s=comp["summary"]
    metrics=dict(s)
    criteria={
        "witness_recoveries_min":1,
        "memory_slots_final_min":1,
        "mean_reward_gain_min":0.0,
    }
    passed=(
        s["witness_recoveries"]>=1
        and s["memory_slots_final"]>=1
        and s["mean_reward_gain_memory_vs_control"]>0
    )
    return passed,metrics,criteria


def _self_model_case():
    params=SelfModelParameters(
        min_observations=12,
        candidate_count=5,
        candidate_sigma=0.035,
        recurrent_rho_max=1.04,
    )
    comp=compare_self_model(
        seed=1341550191,generations=64,self_params=params
    )
    s=comp["summary"]
    metrics=dict(s)
    criteria={
        "closure_passes_min":20,
        "action_interventions_min":1,
        "final_self_reference_reachable":True,
        "prediction_vs_persistence_ratio_max":1.10,
    }
    pred=s["mean_prediction_error"]
    base=s["mean_persistence_baseline_error"]
    ratio=(pred/base) if pred is not None and base not in (None,0) else 999.0
    metrics["prediction_to_persistence_error_ratio"]=ratio
    passed=(
        s["self_model_closure_passes"]>=20
        and s["self_model_action_interventions"]>=1
        and bool(s["final_self_reference_reachable"])
        and ratio<=1.10
    )
    return passed,metrics,criteria


def _perspective_case():
    params=PerspectiveParameters(standpoint_action_weight=0.05)
    comp=compare_perspective(
        seed=1341550191,generations=64,
        perspective_params=params
    )
    s=comp["summary"]
    metrics=dict(s)
    criteria={
        "perspective_closure_fraction_min":0.50,
        "diversity_retention_ratio_min":0.90,
        "standpoint_distance_reduction_min":0.02,
        "mean_standpoint_persistence_min":0.90,
    }
    passed=(
        s["perspective_closure_fraction"]>=0.50
        and s["diversity_retention_ratio"]>=0.90
        and s["standpoint_distance_reduction"]>=0.02
        and s["mean_standpoint_persistence"]>=0.90
    )
    return passed,metrics,criteria


def _identity_case():
    params=IdentityParameters(
        recurrent_alpha=0.965,
        epsilon_identity=0.0015,
        max_identity_distance=0.14,
        export_component_threshold=0.16,
        minimum_self_index_similarity=0.80,
    )
    comp=compare_identity(
        seed=1341550191,generations=64,
        identity_params=params
    )
    s=comp["summary"]
    metrics=dict(s)
    criteria={
        "identity_closure_passes_min":55,
        "identity_closure_failures_max":2,
        "minimum_self_index_similarity_min":0.80,
        "mean_transverse_adaptation_min":0.01,
        "continuity_smoothing_gain_min":0.0,
    }
    passed=(
        s["identity_closure_passes"]>=55
        and s["identity_closure_failures"]<=2
        and s["minimum_self_index_similarity"]>=0.80
        and s["mean_transverse_adaptation"]>=0.01
        and s["continuity_smoothing_gain"]>0
    )
    return passed,metrics,criteria


BENCHMARK_CASES: list[tuple[str,Callable]] = [
    ("canonical_core", _canonical_core_case),
    ("self_organization", _self_organization_case),
    ("population_fission", _population_case),
    ("evolution", _evolution_case),
    ("changing_environment", _environment_case),
    ("learning_memory", _learning_case),
    ("self_model", _self_model_case),
    ("perspective", _perspective_case),
    ("identity", _identity_case),
]


def run_benchmark_suite(
    selected: list[str] | None = None,
) -> BenchmarkSuiteReport:
    manifest=ProvenanceManifest.build(
        experiment="bfg_reference_benchmark_suite",
        seed=None,
        parameters={
            "selected":selected or [name for name,_ in BENCHMARK_CASES]
        },
    )
    allowed=set(selected) if selected else None
    results=[]
    for name,fn in BENCHMARK_CASES:
        if allowed is not None and name not in allowed:
            continue
        results.append(_run_case(name,fn))
    return BenchmarkSuiteReport(
        results=results,
        source_fingerprint=manifest.source_fingerprint,
    )


def write_benchmark_report(
    report: BenchmarkSuiteReport,
    outdir: str | Path,
    stem: str = "benchmark_suite",
) -> dict[str,str]:
    outdir=Path(outdir)
    outdir.mkdir(parents=True,exist_ok=True)

    json_path=outdir/f"{stem}.json"
    json_path.write_text(
        json.dumps(report.summary(),indent=2,default=str),
        encoding="utf-8",
    )

    csv_path=outdir/f"{stem}.csv"
    rows=[]
    for r in report.results:
        rows.append({
            "name":r.name,
            "passed":r.passed,
            "elapsed_seconds":r.elapsed_seconds,
            "error":r.error or "",
            "metrics":json.dumps(r.metrics,sort_keys=True,default=str),
            "criteria":json.dumps(r.criteria,sort_keys=True,default=str),
        })
    if rows:
        with csv_path.open("w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0].keys()))
            w.writeheader(); w.writerows(rows)

    md_path=outdir/f"{stem}.md"
    lines=[
        "# BFG Emergence Studio — Reference Benchmark Suite",
        "",
        f"Overall: **{'PASS' if report.passed else 'FAIL'}**",
        "",
        "| Benchmark | Result | Seconds |",
        "|---|---:|---:|",
    ]
    for r in report.results:
        lines.append(
            f"| {r.name} | {'PASS' if r.passed else 'FAIL'} | {r.elapsed_seconds:.3f} |"
        )
    lines += [
        "",
        f"Source fingerprint: `{report.source_fingerprint}`",
        "",
        "Each benchmark uses frozen reference seeds and declared criteria. "
        "Passing the suite validates software behavior under these tests; it is "
        "not by itself empirical validation of BFG in a natural domain.",
    ]
    md_path.write_text("\n".join(lines)+"\n",encoding="utf-8")

    ledger=save_experiment_ledger(
        outdir,
        experiment="bfg_reference_benchmark_suite",
        seed=None,
        parameters={"benchmarks":[r.name for r in report.results]},
        summary=report.summary(),
        name=f"{stem}_provenance",
    )

    return {
        "json":str(json_path),
        "csv":str(csv_path),
        "markdown":str(md_path),
        **{f"provenance_{k}":v for k,v in ledger.items()},
    }
