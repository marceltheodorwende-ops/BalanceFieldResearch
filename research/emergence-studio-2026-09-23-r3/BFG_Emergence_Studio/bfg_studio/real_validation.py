from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Callable
import hashlib
import json
import numpy as np

from .carrier_sdk import ValidatedCarrierAdapter, no_retuning_comparison
from .types import NumericalPolicy
from .core import canonical_reclosure
from .session import ProvenanceManifest, save_experiment_ledger


@dataclass(frozen=True)
class HeldoutValidationPlan:
    domain: str
    dataset_name: str
    target_statement: str
    calibration_indices: tuple[int,...]
    heldout_indices: tuple[int,...]
    null_model_name: str
    primary_metric: str
    success_criterion: str
    mapping_fingerprint: str

    def validate(self):
        if not self.domain.strip():
            raise ValueError("domain must be declared")
        if not self.dataset_name.strip():
            raise ValueError("dataset_name must be declared")
        if not self.target_statement.strip():
            raise ValueError("target_statement must be prospective")
        cal=set(self.calibration_indices)
        test=set(self.heldout_indices)
        if not cal:
            raise ValueError("calibration split must be nonempty")
        if not test:
            raise ValueError("held-out split must be nonempty")
        if cal & test:
            raise ValueError("calibration and held-out indices must be disjoint")
        if len(self.mapping_fingerprint)!=64:
            raise ValueError("mapping fingerprint must be SHA-256 hex")


def plan_fingerprint(plan:HeldoutValidationPlan)->str:
    plan.validate()
    payload=json.dumps(
        asdict(plan),sort_keys=True,separators=(",",":")
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def run_heldout_carrier_validation(
    adapter:ValidatedCarrierAdapter,
    measurements:list[Any],
    plan:HeldoutValidationPlan,
    null_metric_fn:Callable[[list[Any],tuple[int,...]],float],
    bfg_metric_fn:Callable[[list[dict],tuple[int,...]],float],
    policy:NumericalPolicy|None=None,
)->dict[str,Any]:
    """
    Execute a predeclared no-retuning held-out carrier validation.

    The caller owns the domain-specific metric definitions. This function enforces
    split separation and frozen carrier mapping; it does not choose a favorable
    metric after seeing held-out outcomes.
    """
    policy=policy or NumericalPolicy()
    plan.validate()
    adapter.assert_no_retuning()
    if adapter.mapping_fingerprint != plan.mapping_fingerprint:
        raise ValueError(
            "validation plan fingerprint does not match the carrier mapping"
        )

    audit=no_retuning_comparison(
        adapter,measurements,policy=policy
    )
    states=[]
    for i,m in enumerate(measurements):
        state,report=adapter.validate_measurement_state(
            m,generation=i,policy=policy
        )
        step=canonical_reclosure(state,policy)
        states.append({
            "index":i,
            "mapping_valid":report.valid,
            "reclosure_success":step.success,
            "spectral_novelty":step.spectral_novelty,
            "spectral_mismatch":step.spectral_mismatch,
            "formation_eigenvalue":step.formation_eigenvalue,
            "formation_gap":step.formation_gap,
            "terminal_reason":step.terminal_reason,
            "diagnostics":step.diagnostics,
        })
        adapter.assert_no_retuning()

    # Metrics are computed only after the split and mapping were frozen.
    bfg_cal=float(bfg_metric_fn(states,plan.calibration_indices))
    bfg_test=float(bfg_metric_fn(states,plan.heldout_indices))
    null_cal=float(null_metric_fn(measurements,plan.calibration_indices))
    null_test=float(null_metric_fn(measurements,plan.heldout_indices))

    return {
        "plan":asdict(plan),
        "plan_fingerprint":plan_fingerprint(plan),
        "mapping_fingerprint":adapter.mapping_fingerprint,
        "mapping_audit":audit,
        "states":states,
        "metrics":{
            "bfg_calibration":bfg_cal,
            "bfg_heldout":bfg_test,
            "null_calibration":null_cal,
            "null_heldout":null_test,
        },
        "interpretation_guard":{
            "natural_realization_established":False,
            "note":(
                "A single held-out benchmark can support or fail the declared "
                "target statement but does not by itself establish universal "
                "natural realization."
            ),
        },
    }


def write_heldout_validation(
    result:dict[str,Any],
    outdir:str|Path,
    stem:str="real_domain_validation",
)->dict[str,str]:
    outdir=Path(outdir)
    outdir.mkdir(parents=True,exist_ok=True)
    result_path=outdir/f"{stem}.json"
    result_path.write_text(
        json.dumps(result,indent=2,default=str),
        encoding="utf-8"
    )
    plan=result["plan"]
    ledger=save_experiment_ledger(
        outdir,
        experiment="heldout_real_domain_carrier_validation",
        seed=None,
        parameters={
            "domain":plan["domain"],
            "dataset_name":plan["dataset_name"],
            "mapping_fingerprint":result["mapping_fingerprint"],
            "plan_fingerprint":result["plan_fingerprint"],
        },
        summary={
            "metrics":result["metrics"],
            "interpretation_guard":result["interpretation_guard"],
        },
        name=f"{stem}_provenance",
    )
    return {
        "result":str(result_path),
        **{f"provenance_{k}":v for k,v in ledger.items()},
    }
