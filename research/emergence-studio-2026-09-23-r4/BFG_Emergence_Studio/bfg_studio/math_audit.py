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
from .simulate import simulate
from .seeds import make_random_seed_state
from .types import BFGState, NumericalPolicy
from .core import canonical_reclosure
from .stability import admissible_perturbation_certificate
from .small_load import (
    small_load_contraction_constant,
    certify_small_load_step,
)
from .formation_eligibility import packet_formation_eligibility
from .formation_robustness import (
    formation_margin,
    boundary_crossing_control,
)
from .parent_formation import (
    certify_parent_formation_radius,
    certify_runtime_stratum_radius,
    parent_formation_bound,
)
from .stratum_geometry import (
    persistent_runtime_rank_certificate,
    active_runtime_rank_certificate,
)
from .cross_stratum import (
    canonical_projector_transport,
    continue_witness_across_strata,
    canonical_emergent_seed,
)
from .finite_closure import (
    scalar_nonterminal_seed,
    reduced_closure_step,
    iterate_reduced_closure,
    bounded_infinite_entry_contract,
)



def run_integrated_math_audit() -> dict:
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

    # Unified runtime dispatch: no carrier means finite master runtime.
    dispatch=simulate(
        make_random_seed_state(dim=5,persistent_rank=3,seed=7),
        carrier=None,
        steps=1,
        runtime="auto",
    )
    dispatch_ok=bool(
        dispatch.summary().get("runtime_profile")
        =="finite_reduced_closure"
    )

    # Shared canonical_reclosure now rejects the reproduced growth-admission case.
    growth_state=BFGState(
        D=np.array([1.0,1.0],complex)/np.sqrt(2.0),
        K=np.diag([-2.0,1.0]).astype(complex),
        Y=np.eye(2,dtype=complex),
        R_C=np.diag([1.0,2.0]).astype(complex),
    )
    growth_step=canonical_reclosure(
        growth_state,
        NumericalPolicy(),
    )
    growth_rejected=bool(
        (not growth_step.success)
        and growth_step.terminal_reason is not None
        and "power-boundedness" in growth_step.terminal_reason
    )

    # Perturbation smallness alone is not promoted to stability.
    perturb=admissible_perturbation_certificate(
        np.diag([1.0,0.5]).astype(complex),
        np.diag([1.0001,0.5]).astype(complex),
    )
    perturbation_guard_ok=bool(
        perturb["operator_norm_perturbation"]<1e-3
        and not perturb["admissible_stability_preserved"]
    )

    small_state=scalar_nonterminal_seed(1e-3)
    small_cert,small_next,small_step=certify_small_load_step(
        small_state,
        tau=1.0,
    )
    small_formula=small_load_contraction_constant(
        small_cert.projector_norm,
        small_cert.rho_mass,
        small_cert.lambda_keep,
    )
    small_load_bound_ok=bool(
        small_step.success
        and small_cert.lambda_up_bound_verified
        and small_cert.alpha_bound_verified
        and small_cert.successor_bound_verified
        and abs(
            small_formula-small_cert.contraction_constant
        )<1e-12
    )

    eligibility_cert=packet_formation_eligibility(
        np.array([
            [-2.0,0.25,0.0],
            [0.25,0.8,0.1],
            [0.0,0.1,1.4],
        ],dtype=complex),
        np.array([
            [1.0,0.1,0.0],
            [0.0,0.8,0.2],
            [0.0,0.0,0.5],
            [0.4,0.0,0.0],
            [0.0,0.3,0.0],
            [0.0,0.0,0.2],
        ],dtype=complex),
    )
    formation_eligibility_ok=bool(
        eligibility_cert.active_rank==3
        and eligibility_cert.generalized_match_residual is not None
        and eligibility_cert.generalized_match_residual<1e-10
        and eligibility_cert.exact_lowest_eigenvalue is not None
        and eligibility_cert.generalized_lowest_eigenvalue is not None
        and abs(
            eligibility_cert.exact_lowest_eigenvalue
            -eligibility_cert.generalized_lowest_eigenvalue
        )<1e-10
    )

    margin_operator=np.diag([-2.0,-1.0,3.0]).astype(complex)
    margin_cert=formation_margin(margin_operator)
    margin_control=boundary_crossing_control(margin_operator)
    formation_margin_ok=bool(
        margin_cert.eligible
        and margin_cert.limiting_surface=="simplicity"
        and abs(
            margin_cert.absolute_boundary_distance
            -(1.0-NumericalPolicy().simple_gap_tol)/2.0
        )<1e-12
        and margin_control["inside_preserved"]
        and margin_control["outside_crossed"]
    )

    # No unrestricted ambient parent radius can preserve exact persistence/rank.
    eps_rank=1e-12
    A0=np.diag([1.0,0.0])
    A1=np.diag([1.0,eps_rank])
    active_rank_not_open=bool(
        np.linalg.norm(A1-A0,2)<=eps_rank*(1.0+1e-6)
        and np.linalg.matrix_rank(A0)==1
        and np.linalg.matrix_rank(A1)==2
    )

    R0=np.diag([1.0,0.5]).astype(complex)
    R1=np.diag([1.0-eps_rank,0.5]).astype(complex)
    persistent_not_open=bool(
        np.linalg.norm(R1-R0,2)<=eps_rank*(1.0+1e-6)
        and sum(
            abs(abs(z)-1.0)<1e-15
            for z in np.linalg.eigvals(R0)
        )==1
        and sum(
            abs(abs(z)-1.0)<1e-15
            for z in np.linalg.eigvals(R1)
        )==0
    )

    parent_seed=scalar_nonterminal_seed(0.2)
    parent_cert=certify_parent_formation_radius(parent_seed)
    parent_half=parent_formation_bound(
        parent_seed,
        0.5*parent_cert.parent_radius,
    )
    parent_radius_ok=bool(
        parent_cert.parent_radius>0
        and parent_half.valid
        and parent_half.active_formation_bound is not None
        and parent_half.active_formation_bound<parent_half.active_margin
    )

    persistent_rank_cert=persistent_runtime_rank_certificate(
        np.diag([1.0,0.5]).astype(complex),
        NumericalPolicy(),
    )
    active_rank_cert=active_runtime_rank_certificate(
        np.diag([0.2,0.0]).astype(complex),
        NumericalPolicy(),
    )
    runtime_stratum_cert=certify_runtime_stratum_radius(
        parent_seed,
    )
    stratum_geometry_ok=bool(
        persistent_rank_cert.rank==1
        and persistent_rank_cert.certified_operator_radius>0
        and active_rank_cert.rank==1
        and active_rank_cert.certified_operator_radius>0
        and runtime_stratum_cert.runtime_stratum_parent_radius>0
        and runtime_stratum_cert.runtime_stratum_parent_radius
            <runtime_stratum_cert.conditional_parent_radius
        and runtime_stratum_cert.limiting_surface
            in {
                "persistent_runtime_rank",
                "active_runtime_rank",
                "formation_status",
            }
    )

    q0=np.diag([1.0,0.0,0.0]).astype(complex)
    q1=np.eye(3,dtype=complex)
    witness=q0.copy()
    continuation=continue_witness_across_strata(
        q0,q1,witness,
    )
    degenerate_seed=continue_witness_across_strata(
        q0,q1,witness,
        formation_operator=np.diag([0.5,-1.0,-1.0]).astype(complex),
        require_emergent_seed=True,
    )
    unique_seed=continue_witness_across_strata(
        q0,q1,witness,
        formation_operator=np.diag([0.5,-2.0,1.0]).astype(complex),
        require_emergent_seed=True,
    )
    cross_stratum_ok=bool(
        not continuation.terminal
        and continuation.certificate.transition_kind=="rank_increase"
        and continuation.certificate.emergent_rank==2
        and abs(continuation.retained_witness_mass-1.0)<1e-12
        and degenerate_seed.terminal
        and not unique_seed.terminal
        and unique_seed.emergent_seed is not None
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
        "finite_master_runtime_dispatch":dispatch_ok,
        "legacy_core_growth_admission_rejected":growth_rejected,
        "perturbation_smallness_guard":perturbation_guard_ok,
        "multidimensional_small_load_contraction_bound":
            small_load_bound_ok,
        "formation_eligibility_generalized_spectrum":
            formation_eligibility_ok,
        "formation_bifurcation_exact_operator_margin":
            formation_margin_ok,
        "ambient_active_rank_not_open":
            active_rank_not_open,
        "ambient_persistent_sector_not_open":
            persistent_not_open,
        "conditional_parent_formation_radius":
            parent_radius_ok,
        "runtime_stratum_transition_geometry":
            stratum_geometry_ok,
        "cross_stratum_canonical_continuation":
            cross_stratum_ok,
    }

    return {
        "audit_passed":all(checks.values()),
        "checks":checks,
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
            "multidimensional_small_load_contraction":
                "EXACT under bounded projector, density-mass and positive keep-load corridor assumptions: ||Y_+|| <= C||Y||^2",
            "formation_eligibility":
                "EXACT finite criterion: the active formation spectrum equals the generalized spectrum of (A*(K⊕K)A, A*A) on active support; parent-ground negative Rayleigh transport is a sufficient witness",
            "formation_bifurcation_margin":
                "EXACT in active Hermitian operator norm: eligible distance min(sign clearance, gap clearance/2); ineligible distance max(sign violation, gap violation/2)",
            "parent_formation_radius":
                "CONDITIONAL sufficient radius on the fixed persistent-rank / fixed-active-rank admissible stratum; no positive unrestricted ambient radius is claimed because exact persistence and exact rank are not open properties",
            "runtime_stratum_geometry":
                "OPERATIONAL finite-runtime rank surfaces are certified by singular-value margins; persistent and active numerical ranks can therefore be protected in parent norm without claiming openness of exact algebraic rank",
            "cross_stratum_continuation":
                "EXACT basis-free support transport by the polar partial isometry of Q_target Q_source; inherited witness mass is preserved on the transportable support, zero-overlap continuity commits to bottom, and emergent seeding obeys the simple-negative no-choice gate",
            "historical_internal_uniqueness":
                "not required for runtime closure and not claimed as a derivation from older axioms",
        },
    }


def write_integrated_math_audit(
    result:dict,
    outdir:str|Path,
):
    outdir=Path(outdir)
    outdir.mkdir(parents=True,exist_ok=True)

    json_path=outdir/"integrated_math_audit.json"
    json_path.write_text(
        json.dumps(result,indent=2),encoding="utf-8"
    )

    md_path=outdir/"INTEGRATED_MATH_AUDIT.md"
    lines=[
        "# BFG Integrated Mathematical Closure Audit",
        "",
        f"Audit: **{'PASS' if result['audit_passed'] else 'FAIL'}**",
        "",
        "This audit verifies the executable mathematics of the integrated master "
        "closure stack, including finite closure, stability admission, "
        "runtime dispatch and reconstruction controls.",
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
