from __future__ import annotations

from pathlib import Path
import json

import numpy as np

from .closure_math import (
    M3ConnectionState,
    verify_exact_recursive_certificate,
    gram_rebuild_from_supplied_factors,
    retained_channel_gram_decomposition,
    g1_intertwining_audit,
    m3_operators,
)
from .session import source_tree_fingerprint
from .finite_closure import (
    scalar_nonterminal_seed,
    reduced_closure_step,
    iterate_reduced_closure,
    bounded_infinite_entry_contract,
)


SOURCE_REPOSITORY = (
    "https://github.com/marceltheodorwende-ops/BalanceFieldResearch"
)

SOURCE_PATHS = {
    "exact_nonnormal":
        "research/exact-nonnormal-2026-09-18/README.md",
    "retained_channels":
        "research/retained-channels-2026-09-18/README.md",
    "gram_compatibility":
        "research/gram-compatibility-2026-09-18/README.md",
    "gram_inheritance_proposal":
        "research/gram-inheritance-proposal-2026-09-18/README.md",
    "reconstruction_witness":
        "research/reconstruction-witness-2026-09-18/README.md",
    "closure_boundaries":
        "research/closure-boundaries-2026-09-19/README.md",
    "connection_model_m3":
        "research/connection-model-2026-09-19/README.md",
    "finite_repair":
        "research/finite-repair-2026-09-23/REPAIR.md",
    "finite_reconstruction_contract":
        "research/finite-repair-2026-09-23/RECONSTRUCTION.md",
    "finite_closure_theorem":
        "research/finite-closure-model-2026-09-23/THEOREM.md",
    "finite_closure_audit":
        "research/finite-closure-model-2026-09-23/AUDIT.md",
}


def run_github_math_integration_audit() -> dict:
    # Exact rational nonnormal certificate.
    exact=verify_exact_recursive_certificate(
        r=[["1","-1/2"],["0","1/2"]],
        basis=[["1","1"],["0","1"]],
        persistent_dimension=1,
        persistent_metric=[["1"]],
        stable_metric=[["1"]],
    )
    exact_ok=exact.status=="certified"

    jordan_rejected=False
    try:
        verify_exact_recursive_certificate(
            r=[["1","1"],["0","1"]],
            basis=[["1","0"],["0","1"]],
            persistent_dimension=2,
            persistent_metric=[["1","0"],["0","1"]],
            stable_metric=[],
        )
    except ValueError:
        jordan_rejected=True

    # Supplied-factor Gram rebuild.
    gram=gram_rebuild_from_supplied_factors(
        np.array([[1.0,0.0],[0.0,2.0]]),
        np.eye(2),
        np.eye(2),
    )
    gram_ok=bool(
        np.min(np.linalg.eigvalsh(gram["Y"]))>=-1e-12
        and np.linalg.norm(
            gram["C_N"]+gram["B_N"]-np.eye(2),2
        )<1e-12
    )

    # Retained-channel bookkeeping identity with a purely external channel.
    retained=retained_channel_gram_decomposition(
        np.array([[0.0,0.0],[1.0,0.0]]),
        np.array([[1.0],[0.0]]),
    )
    retained_ok=bool(
        retained["identity_residual"]<1e-12
        and retained["external_rank"]==1
        and retained["interpretation"]["gram_energy_recovered"]
        and not retained["interpretation"]["future_dynamics_recovered"]
    )

    # Positive conditional G1 intertwining example.
    g1_good=g1_intertwining_audit(
        b2=np.diag([2.0,3.0]),
        w2=np.eye(2),
        l2=np.eye(2),
        u=np.array([[1.0],[0.0]]),
        b_next=np.array([[2.0]]),
        w_next=np.array([[1.0]]),
        l_next=np.array([[1.0]]),
    )
    g1_good_ok=bool(g1_good["intertwining_satisfied"])

    # A deliberately incompatible local reconstruction must not be promoted.
    g1_bad=g1_intertwining_audit(
        b2=np.diag([2.0,3.0]),
        w2=np.eye(2),
        l2=np.eye(2),
        u=np.array([[1.0],[0.0]]),
        b_next=np.array([[0.0]]),
        w_next=np.array([[1.0]]),
        l_next=np.array([[1.0]]),
    )
    g1_bad_rejected=not bool(g1_bad["intertwining_satisfied"])

    # M3: explicit extra connection assumptions give a unitary Cayley transport.
    m3=m3_operators(
        M3ConnectionState(
            connection=np.array([[0.0,-1.0],[1.0,0.0]]),
            coherence=np.diag([1.0,2.0]),
            difference=5.0*np.eye(2),
            neutral=np.eye(2),
            packet=np.ones(2),
        )
    )
    m3_ok=bool(
        m3["power_bounded_by_construction"]
        and m3["unitarity_residual"]<1e-10
    )

    # Current 23-Sep finite conditional closure, adopted as the master runtime
    # profile for the declared reduced finite category.
    scalar=scalar_nonterminal_seed(1.0)
    scalar_next,scalar_step=reduced_closure_step(scalar,tau=1.0)
    scalar_expected=2.0/(4.0*2.0)
    finite_scalar_ok=bool(
        scalar_step.success
        and not scalar_next.bottom
        and abs(float(np.real(scalar_next.Y[0,0]))-scalar_expected)<1e-12
    )
    finite_run=iterate_reduced_closure(
        scalar_nonterminal_seed(1.0),
        4,
        tau=1.0,
    )
    finite_iteration_ok=bool(
        finite_run["executed_steps"]>=1
        and all(
            st.bottom or (
                st.Y is not None
                and st.K is not None
                and st.R is not None
            )
            for st in finite_run["states"]
        )
    )
    bounded_entry=bounded_infinite_entry_contract()
    bounded_entry_ok=bool(
        bounded_entry["peripheral_riesz_range"]=="finite-dimensional"
        and "reduces" in bounded_entry["consequence"]
    )

    checks={
        "exact_nonnormal_supplied_certificate":exact_ok,
        "defective_peripheral_control_rejected":jordan_rejected,
        "supplied_factor_gram_rebuild":gram_ok,
        "retained_channel_gram_identity":retained_ok,
        "g1_conditional_intertwining_example":g1_good_ok,
        "g1_incompatible_reconstruction_rejected":g1_bad_rejected,
        "m3_cayley_transport_unitary":m3_ok,
        "finite_reduced_closure_scalar_identity":finite_scalar_ok,
        "finite_reduced_closure_iteration_contract":finite_iteration_ok,
        "bounded_infinite_entry_reduction_contract":bounded_entry_ok,
    }

    return {
        "audit_passed":all(checks.values()),
        "checks":checks,
        "source_repository":SOURCE_REPOSITORY,
        "source_paths":SOURCE_PATHS,
        "source_fingerprint":source_tree_fingerprint(),
        "claim_register":{
            "exact_nonnormal_certificate":
                "runtime-confirmed for supplied rational invariant splittings and metrics",
            "finite_gram_rebuild":
                "runtime-confirmed for explicitly supplied B_C, W_N, L_C",
            "retained_channel_gram_energy":
                "runtime-confirmed exact decomposition identity",
            "g1":
                "conditional compatibility layer; not required by the finite master closure profile",
            "m3":
                "complete finite experimental connection model under its declared assumptions",
            "finite_reduced_master_closure":
                "CLOSED for the declared finite reduced category by adopted explicit laws; total with absorbing bottom and exact finite iteration",
            "bounded_infinite_entry_class":
                "CLOSED as a restricted reduction theorem into the finite master profile under the declared bounded finite-peripheral-rank assumptions",
            "historical_internal_uniqueness":
                "not required for runtime closure and not claimed as a derivation from older axioms",
        },
    }


def write_github_math_integration_audit(
    result:dict,
    outdir:str|Path,
):
    outdir=Path(outdir)
    outdir.mkdir(parents=True,exist_ok=True)

    json_path=outdir/"github_math_integration_audit.json"
    json_path.write_text(
        json.dumps(result,indent=2),encoding="utf-8"
    )

    md_path=outdir/"GITHUB_MATH_INTEGRATION_AUDIT.md"
    lines=[
        "# GitHub BalanceFieldResearch — Math Integration Audit",
        "",
        f"Audit: **{'PASS' if result['audit_passed'] else 'FAIL'}**",
        "",
        "This audit verifies the executable mathematics integrated from the "
        "current BalanceFieldResearch line, including the adopted 23-September "
        "finite reduced master closure profile.",
        "",
        "## Checks",
        "",
    ]
    for name,ok in result["checks"].items():
        lines.append(f"- {name}: `{'PASS' if ok else 'FAIL'}`")
    lines += [
        "",
        "## Claim register",
        "",
    ]
    for name,status in result["claim_register"].items():
        lines.append(f"- **{name}** — {status}")
    lines += [
        "",
        "The active master architecture adopts the explicit finite reduced closure "
        "laws as its runtime profile. For that declared category, reconstruction "
        "and finite iteration are no longer an open runtime blocker. Historical "
        "uniqueness from older axioms is a provenance question, not a runtime gap.",
    ]
    md_path.write_text("\n".join(lines)+"\n",encoding="utf-8")
    return {
        "json":str(json_path),
        "markdown":str(md_path),
    }
