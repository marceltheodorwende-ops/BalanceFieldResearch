from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from typing import Any
import csv
import json
import os
import numpy as np

from .types import NumericalPolicy, BFGState
from .core import (
    neutral_pair,
    graph_metric,
    reciprocal_order,
    polar_partial_isometry,
    canonical_reclosure,
)
from .seeds import make_random_seed_state, make_commuting_control_state
from .alife import SelfOrganizationParameters, simulate_self_organization
from .session import ProvenanceManifest, save_experiment_ledger


@dataclass
class RobustnessReport:
    passed: bool
    randomized_trials: int
    randomized_failures: int
    commuting_controls: int
    commuting_failures: int
    noncommuting_controls: int
    noncommuting_success_fraction: float
    noncommuting_novelty_fraction: float
    tolerance_classification_stable: bool
    carrier_perturbation_survival_fraction: float
    diagnostics: dict[str,Any]
    source_fingerprint: str

    def summary(self) -> dict[str,Any]:
        return asdict(self)


def _random_psd(seed: int, dim: int) -> np.ndarray:
    rng=np.random.default_rng(seed)
    A=rng.normal(size=(dim,dim))+1j*rng.normal(size=(dim,dim))
    return (A.conj().T@A)/dim


def _property_trial(args):
    seed,dim=args
    rng=np.random.default_rng(seed)
    Y=_random_psd(seed,dim)
    C,B=neutral_pair(Y)
    G=graph_metric(Y)
    I=np.eye(dim,dtype=complex)

    partition=float(np.linalg.norm(C+B-I,ord="fro"))
    cmin=float(np.min(np.linalg.eigvalsh(0.5*(C+C.conj().T)).real))
    bmin=float(np.min(np.linalg.eigvalsh(0.5*(B+B.conj().T)).real))
    gmin=float(np.min(np.linalg.eigvalsh(0.5*(G+G.conj().T)).real))
    cmax=float(np.max(np.linalg.eigvalsh(0.5*(C+C.conj().T)).real))
    bmax=float(np.max(np.linalg.eigvalsh(0.5*(B+B.conj().T)).real))

    l1=float(rng.uniform(1e-3,10.0))
    l2=float(rng.uniform(1e-3,10.0))
    w1,w2=reciprocal_order(l1,l2,NumericalPolicy())
    balance=abs(w1*l1-w2*l2)

    A=rng.normal(size=(2*dim,dim))+1j*rng.normal(size=(2*dim,dim))
    J,V,_=polar_partial_isometry(A,NumericalPolicy())
    if V.shape[1]:
        initial=V@V.conj().T
        polar_residual=float(np.linalg.norm(J.conj().T@J-initial,ord="fro"))
    else:
        polar_residual=0.0

    passed=(
        partition<1e-8
        and cmin>=-1e-9
        and bmin>=-1e-9
        and cmax<=1+1e-8
        and bmax<=1+1e-8
        and gmin>0
        and balance<1e-9
        and polar_residual<1e-7
    )
    return {
        "seed":seed,
        "dim":dim,
        "passed":passed,
        "partition_residual":partition,
        "C_min":cmin,
        "B_min":bmin,
        "C_max":cmax,
        "B_max":bmax,
        "G_min":gmin,
        "reciprocal_balance":balance,
        "polar_support_residual":polar_residual,
    }


def _commuting_trial(seed: int):
    state=make_commuting_control_state(dim=6,persistent_rank=4,seed=seed)
    step=canonical_reclosure(state,NumericalPolicy())
    mismatch=float(step.spectral_mismatch or 0.0)
    passed=(
        step.success
        and mismatch<1e-7
        and not bool(step.spectral_novelty)
    )
    return {
        "seed":seed,
        "passed":passed,
        "success":step.success,
        "spectral_mismatch":mismatch,
        "novelty":bool(step.spectral_novelty),
    }


def _noncommuting_trial(seed: int):
    state=make_random_seed_state(dim=6,persistent_rank=4,seed=seed)
    step=canonical_reclosure(state,NumericalPolicy())
    return {
        "seed":seed,
        "success":bool(step.success),
        "novelty":bool(step.spectral_novelty) if step.success else False,
        "spectral_mismatch":(
            float(step.spectral_mismatch)
            if step.spectral_mismatch is not None else None
        ),
        "terminal_reason":step.terminal_reason,
    }


def _tolerance_policy(scale: float) -> NumericalPolicy:
    base=NumericalPolicy()
    return NumericalPolicy(
        atol=base.atol*scale,
        rtol=base.rtol*scale,
        peripheral_tol=base.peripheral_tol*scale,
        rank_tol=base.rank_tol*scale,
        simple_gap_tol=base.simple_gap_tol*scale,
        psd_tol=base.psd_tol*scale,
        novelty_tol=base.novelty_tol*scale,
    )


def tolerance_sensitivity(
    seeds: list[int] | None = None,
    scales: tuple[float,...] = (0.1,1.0,10.0),
) -> dict[str,Any]:
    seeds=seeds or [3,7,11,17,23,31]
    rows=[]
    stable=True
    for seed in seeds:
        signatures=[]
        for scale in scales:
            state=make_random_seed_state(dim=6,persistent_rank=4,seed=seed)
            step=canonical_reclosure(state,_tolerance_policy(scale))
            sig=(
                bool(step.success),
                bool(step.spectral_novelty) if step.spectral_novelty is not None else None,
                step.diagnostics.get("persistent_rank"),
                step.diagnostics.get("support_rank"),
            )
            signatures.append(sig)
            rows.append({
                "seed":seed,
                "scale":scale,
                "success":sig[0],
                "novelty":sig[1],
                "persistent_rank":sig[2],
                "support_rank":sig[3],
                "formation_eigenvalue":step.formation_eigenvalue,
            })
        if any(sig!=signatures[0] for sig in signatures[1:]):
            stable=False
    return {"stable":stable,"rows":rows}


def carrier_parameter_sensitivity(
    seed: int = 1341550191,
    perturbations: tuple[float,...] = (-0.05,-0.025,0.0,0.025,0.05),
    steps: int = 12,
) -> dict[str,Any]:
    rows=[]
    survived=0
    total=0
    for df in perturbations:
        for dn in perturbations:
            base=SelfOrganizationParameters()
            p=SelfOrganizationParameters(
                node_count=24,
                persistent_rank=6,
                neighbor_scale=base.neighbor_scale*(1.0+dn),
                edge_threshold=base.edge_threshold,
                resource_blend=base.resource_blend,
                topology_blend=base.topology_blend,
                export_cost=base.export_cost,
                basal_recovery=base.basal_recovery,
                load_scale=base.load_scale,
                stress_scale=base.stress_scale,
                formation_drive=base.formation_drive*(1.0+df),
                formation_offset=base.formation_offset,
                contraction=base.contraction,
                phase_scale=base.phase_scale,
                cluster_threshold=base.cluster_threshold,
                viability_threshold=base.viability_threshold,
            )
            run=simulate_self_organization(
                seed=seed,steps=steps,params=p
            )
            success=sum(int(s.success) for s in run.steps)
            ok=success>=max(1,steps-2)
            survived+=int(ok)
            total+=1
            rows.append({
                "formation_drive_relative_change":df,
                "neighbor_scale_relative_change":dn,
                "successful_reclosures":success,
                "attempted_steps":len(run.steps),
                "survived":ok,
            })
    return {
        "survival_fraction":survived/max(total,1),
        "rows":rows,
    }


def invalid_input_guard() -> dict[str,Any]:
    n=4
    D=np.ones(n,dtype=complex)/2
    K=np.diag([-1.0,0.5,1.0,2.0]).astype(complex)
    Y=np.diag([1.0,0.5,-0.25,2.0]).astype(complex)
    R=np.eye(n,dtype=complex)
    state=BFGState(D=D,K=K,Y=Y,R_C=R,name="invalid_negative_Y")
    step=canonical_reclosure(state,NumericalPolicy())
    return {
        "rejected":not step.success,
        "terminal_reason":step.terminal_reason,
    }


def run_robustness_suite(
    randomized_trials: int = 200,
    commuting_controls: int = 40,
    noncommuting_controls: int = 40,
    seed: int = 20260923,
    workers: int | None = None,
) -> RobustnessReport:
    workers=workers or min(8,max(1,os.cpu_count() or 1))
    rng=np.random.default_rng(seed)

    property_args=[
        (int(rng.integers(0,2**31-1)),int(rng.integers(2,10)))
        for _ in range(int(randomized_trials))
    ]
    with ThreadPoolExecutor(max_workers=workers) as ex:
        property_rows=list(ex.map(_property_trial,property_args))

    commuting_seeds=[
        int(rng.integers(0,2**31-1))
        for _ in range(int(commuting_controls))
    ]
    with ThreadPoolExecutor(max_workers=workers) as ex:
        commuting_rows=list(ex.map(_commuting_trial,commuting_seeds))

    noncomm_seeds=[
        int(rng.integers(0,2**31-1))
        for _ in range(int(noncommuting_controls))
    ]
    with ThreadPoolExecutor(max_workers=workers) as ex:
        noncomm_rows=list(ex.map(_noncommuting_trial,noncomm_seeds))

    tolerance=tolerance_sensitivity()
    carrier=carrier_parameter_sensitivity()
    invalid=invalid_input_guard()

    property_failures=sum(int(not r["passed"]) for r in property_rows)
    commuting_failures=sum(int(not r["passed"]) for r in commuting_rows)
    noncomm_success=sum(int(r["success"]) for r in noncomm_rows)
    noncomm_novel=sum(int(r["novelty"]) for r in noncomm_rows)
    success_fraction=noncomm_success/max(len(noncomm_rows),1)
    novelty_fraction=noncomm_novel/max(noncomm_success,1)

    passed=(
        property_failures==0
        and commuting_failures==0
        and success_fraction>=0.70
        and novelty_fraction>=0.80
        and tolerance["stable"]
        and carrier["survival_fraction"]>=0.70
        and invalid["rejected"]
    )

    manifest=ProvenanceManifest.build(
        experiment="bfg_robustness_suite",
        seed=seed,
        parameters={
            "randomized_trials":randomized_trials,
            "commuting_controls":commuting_controls,
            "noncommuting_controls":noncommuting_controls,
            "workers":workers,
        },
    )

    return RobustnessReport(
        passed=bool(passed),
        randomized_trials=len(property_rows),
        randomized_failures=property_failures,
        commuting_controls=len(commuting_rows),
        commuting_failures=commuting_failures,
        noncommuting_controls=len(noncomm_rows),
        noncommuting_success_fraction=float(success_fraction),
        noncommuting_novelty_fraction=float(novelty_fraction),
        tolerance_classification_stable=bool(tolerance["stable"]),
        carrier_perturbation_survival_fraction=float(
            carrier["survival_fraction"]
        ),
        diagnostics={
            "invalid_input_guard":invalid,
            "property_trials":property_rows,
            "commuting_rows":commuting_rows,
            "noncommuting_rows":noncomm_rows,
            "tolerance_sensitivity":tolerance,
            "carrier_parameter_sensitivity":carrier,
        },
        source_fingerprint=manifest.source_fingerprint,
    )


def write_robustness_report(
    report: RobustnessReport,
    outdir: str | Path,
    stem: str = "robustness",
) -> dict[str,str]:
    outdir=Path(outdir)
    outdir.mkdir(parents=True,exist_ok=True)

    summary=report.summary()
    json_path=outdir/f"{stem}.json"
    json_path.write_text(
        json.dumps(summary,indent=2,default=str),
        encoding="utf-8",
    )

    tol_path=outdir/f"{stem}_tolerance.csv"
    tol_rows=report.diagnostics["tolerance_sensitivity"]["rows"]
    if tol_rows:
        with tol_path.open("w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(f,fieldnames=list(tol_rows[0].keys()))
            w.writeheader(); w.writerows(tol_rows)

    carrier_path=outdir/f"{stem}_carrier_sensitivity.csv"
    carrier_rows=report.diagnostics[
        "carrier_parameter_sensitivity"
    ]["rows"]
    if carrier_rows:
        with carrier_path.open("w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(f,fieldnames=list(carrier_rows[0].keys()))
            w.writeheader(); w.writerows(carrier_rows)

    md_path=outdir/f"{stem}.md"
    md_path.write_text(
        "\n".join([
            "# BFG Emergence Studio — Robustness Suite",
            "",
            f"Overall: **{'PASS' if report.passed else 'FAIL'}**",
            "",
            f"- randomized algebraic property trials: {report.randomized_trials}",
            f"- randomized property failures: {report.randomized_failures}",
            f"- commuting controls: {report.commuting_controls}",
            f"- commuting-control failures: {report.commuting_failures}",
            f"- noncommuting success fraction: {report.noncommuting_success_fraction:.4f}",
            f"- novelty fraction among successful noncommuting trials: {report.noncommuting_novelty_fraction:.4f}",
            f"- numerical tolerance classification stable: {report.tolerance_classification_stable}",
            f"- carrier ±5% perturbation survival fraction: {report.carrier_perturbation_survival_fraction:.4f}",
            "",
            "Numerical-tolerance sweeps alter implementation precision only; "
            "they are not additional BFG generator parameters.",
            "",
            f"Source fingerprint: `{report.source_fingerprint}`",
        ])+"\n",
        encoding="utf-8",
    )

    ledger=save_experiment_ledger(
        outdir,
        experiment="bfg_robustness_suite",
        seed=None,
        parameters={
            "randomized_trials":report.randomized_trials,
            "commuting_controls":report.commuting_controls,
            "noncommuting_controls":report.noncommuting_controls,
        },
        summary={
            k:v for k,v in summary.items()
            if k!="diagnostics"
        },
        name=f"{stem}_provenance",
    )

    return {
        "json":str(json_path),
        "markdown":str(md_path),
        "tolerance_csv":str(tol_path),
        "carrier_sensitivity_csv":str(carrier_path),
        **{f"provenance_{k}":v for k,v in ledger.items()},
    }
