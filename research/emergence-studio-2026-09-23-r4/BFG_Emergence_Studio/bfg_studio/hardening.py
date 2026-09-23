from __future__ import annotations

from pathlib import Path
import json

from .benchmarks import run_benchmark_suite, write_benchmark_report
from .robustness import run_robustness_suite, write_robustness_report
from .seeds import make_random_seed_state
from .carrier import ReferenceGramCarrier
from .simulate import simulate
from .stability import run_master_stability_audit, write_stability_audit
from .math_audit import run_integrated_math_audit, write_integrated_math_audit
from .runtime_transfer import (
    run_master_runtime_transfer_audit,
    write_master_runtime_transfer_report,
)
from .formation_dynamics import (
    run_formation_termination_analysis,
    scalar_neutral_load_map,
)
from .small_load import run_small_load_contraction_audit
from .network_audit import run_karate_network_audit, write_karate_network_report
from .formation_eligibility import (
    run_formation_eligibility_audit,
    write_formation_eligibility_report,
)
from .formation_robustness import (
    run_formation_robustness_audit,
    write_formation_robustness_report,
)
from .parent_formation import (
    run_parent_formation_radius_audit,
    write_parent_formation_radius_report,
)
from .stratum_geometry import (
    run_stratum_transition_audit,
    write_stratum_transition_report,
)
from .cross_stratum import (
    run_cross_stratum_audit,
    write_cross_stratum_report,
)
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

    math_audit=run_integrated_math_audit()
    math_audit_files=write_integrated_math_audit(
        math_audit,outdir/"math_audit"
    )

    transfer=run_master_runtime_transfer_audit(
        recursive_horizon=4,
        tau=1.0,
    )
    transfer_files=write_master_runtime_transfer_report(
        transfer,
        outdir/"runtime_transfer",
    )

    formation_smoke=run_formation_termination_analysis(
        horizon=4,
        tau=1.0,
        limit_per_carrier=4,
        compute_tolerance_sensitivity=False,
    )
    scalar_probe_y=1e-6
    scalar_probe_ratio=(
        scalar_neutral_load_map(scalar_probe_y)
        /(2.0*scalar_probe_y*scalar_probe_y)
    )
    formation_smoke_pass=bool(
        formation_smoke["heldout_metrics_evaluated"] is False
        and formation_smoke["states_total"]==12
        and formation_smoke["first_step_success_fraction"]==1.0
        and formation_smoke["pooled_loglog_y_decay_exponent"] is not None
        and abs(scalar_probe_ratio-1.0)<5e-6
    )

    small_load_smoke=run_small_load_contraction_audit(
        horizon=3,
        tau=1.0,
        limit_per_carrier=4,
    )
    small_load_smoke_pass=bool(
        small_load_smoke["heldout_metrics_evaluated"] is False
        and small_load_smoke["successful_transitions"]>=12
        and small_load_smoke["all_theorem_bounds_verified"]
    )

    network=run_karate_network_audit(
        recursive_horizon=4,
    )
    network_files=write_karate_network_report(
        network,
        outdir/"real_network",
    )
    network_pass=bool(
        network["heldout_metrics_evaluated"] is False
        and network["state_contract_valid"]==34
        and network["permutation_equivariance"]["equivariant"]
        and network["small_load"]["all_bounds_verified"]
    )

    eligibility=run_formation_eligibility_audit(
        limit_per_timeseries_carrier=4,
        include_full_network=True,
    )
    eligibility_files=write_formation_eligibility_report(
        eligibility,
        outdir/"formation_eligibility",
    )
    eligibility_pass=bool(
        eligibility["heldout_metrics_evaluated"] is False
        and eligibility["maximum_generalized_match_residual"]<=1e-10
        and eligibility["network_explanation"][
            "all_parent_K_have_negative_ground_mode"
        ]
        and eligibility["network_explanation"][
            "simplicity_condition_passes_for_all_34"
        ]
        and eligibility["network_explanation"][
            "ground_witness_sign_matches_formation_34_of_34"
        ]
        and all(
            d["exact_generalized_criterion_matches"]
            ==f"{d['gate_reached']}/{d['gate_reached']}"
            for d in eligibility["domains"]
        )
    )

    formation_robustness=run_formation_robustness_audit(
        limit_per_timeseries_carrier=4,
        include_full_network=True,
    )
    formation_robustness_files=write_formation_robustness_report(
        formation_robustness,
        outdir/"formation_robustness",
    )
    formation_robustness_pass=bool(
        formation_robustness["heldout_metrics_evaluated"] is False
        and formation_robustness["gate_states"]>0
        and formation_robustness["inside_preserved"]
            ==formation_robustness["boundary_controls"]
        and formation_robustness["outside_crossed"]
            ==formation_robustness["boundary_controls"]
    )

    parent_formation=run_parent_formation_radius_audit(
        limit_per_timeseries_carrier=2,
        include_full_network=True,
    )
    parent_formation_files=write_parent_formation_radius_report(
        parent_formation,
        outdir/"parent_formation",
    )
    parent_formation_pass=bool(
        parent_formation["heldout_metrics_evaluated"] is False
        and parent_formation["states_total"]==40
        and parent_formation["certified_states"]==40
        and parent_formation["structured_status_preserved"]
            ==parent_formation["structured_controls"]
        and parent_formation["structured_active_bound_verified"]
            ==parent_formation["structured_controls"]
        and parent_formation["structured_same_active_rank"]
            ==parent_formation["structured_controls"]
        and parent_formation["runtime_status_preserved"]
            ==parent_formation["runtime_controls"]
        and parent_formation["runtime_same_active_rank"]
            ==parent_formation["runtime_controls"]
        and parent_formation["runtime_limiting_surface_counts"][
            "active_runtime_rank"
        ]==40
    )

    stratum_geometry=run_stratum_transition_audit(
        limit_per_timeseries_carrier=2,
        include_full_network=True,
    )
    stratum_geometry_files=write_stratum_transition_report(
        stratum_geometry,
        outdir/"stratum_geometry",
    )
    stratum_geometry_pass=bool(
        stratum_geometry["heldout_metrics_evaluated"] is False
        and stratum_geometry["states_total"]==40
        and stratum_geometry["active_upward_bottleneck_states"]==40
        and stratum_geometry["persistent_loss_bottleneck_states"]==40
        and all(
            d["persistent_ranks"]==[4]
            and d["active_ranks"]==[4]
            for d in stratum_geometry["domains"]
        )
    )

    cross_stratum=run_cross_stratum_audit(
        limit_per_timeseries_carrier=2,
        include_full_network=True,
    )
    cross_stratum_files=write_cross_stratum_report(
        cross_stratum,
        outdir/"cross_stratum",
    )
    cross_stratum_pass=bool(
        cross_stratum["heldout_metrics_evaluated"] is False
        and cross_stratum["real_states_total"]==40
        and cross_stratum["real_identity_continuity_passed"]==40
        and cross_stratum["synthetic_crossing_cases"]>=7
        and cross_stratum["synthetic_crossing_passed"]
        and cross_stratum["unitary_equivariance_passed"]
        and cross_stratum["identity_continuity_passed"]
        and cross_stratum["cross_stratum_chain_stability_passed"]
        and cross_stratum["real_observed_rank_crossings"]==0
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
            and math_audit["audit_passed"]
            and transfer["audit_passed"]
            and formation_smoke_pass
            and small_load_smoke_pass
            and network_pass
            and eligibility_pass
            and formation_robustness_pass
            and parent_formation_pass
            and stratum_geometry_pass
            and cross_stratum_pass
            and checkpoint_pass
        ),
        "benchmark_passed":benchmark.passed,
        "robustness_passed":robustness.passed,
        "recursive_stability_audit_passed":stability["audit_passed"],
        "integrated_math_audit_passed":math_audit["audit_passed"],
        "master_runtime_transfer_audit_passed":transfer["audit_passed"],
        "master_runtime_first_step_success_fraction":
            transfer["first_step_success_fraction"],
        "formation_dynamics_smoke_passed":formation_smoke_pass,
        "formation_dynamics_smoke_pooled_exponent":
            formation_smoke["pooled_loglog_y_decay_exponent"],
        "formation_scalar_quadratic_probe_ratio":
            scalar_probe_ratio,
        "small_load_contraction_smoke_passed":
            small_load_smoke_pass,
        "small_load_contraction_smoke_transitions":
            small_load_smoke["successful_transitions"],
        "relational_network_audit_passed":network_pass,
        "relational_network_first_step_success_fraction":
            network["first_step_success_fraction"],
        "relational_network_small_load_bounds":
            f"{network['small_load']['bound_passed']}/{network['small_load']['certificates']}",
        "formation_eligibility_audit_passed":eligibility_pass,
        "formation_eligibility_max_generalized_residual":
            eligibility["maximum_generalized_match_residual"],
        "formation_robustness_audit_passed":
            formation_robustness_pass,
        "formation_robustness_boundary_controls":
            formation_robustness["boundary_controls"],
        "parent_formation_radius_audit_passed":
            parent_formation_pass,
        "parent_formation_radius_smoke_states":
            parent_formation["states_total"],
        "parent_formation_radius_smoke_certified":
            parent_formation["certified_states"],
        "parent_runtime_stratum_controls":
            parent_formation["runtime_controls"],
        "parent_runtime_stratum_status_preserved":
            parent_formation["runtime_status_preserved"],
        "stratum_transition_audit_passed":
            stratum_geometry_pass,
        "stratum_transition_smoke_states":
            stratum_geometry["states_total"],
        "cross_stratum_continuation_audit_passed":
            cross_stratum_pass,
        "cross_stratum_smoke_real_states":
            cross_stratum["real_states_total"],
        "cross_stratum_synthetic_cases":
            cross_stratum["synthetic_crossing_cases"],
        "checkpoint_roundtrip_passed":checkpoint_pass,
        "benchmark_count":len(benchmark.results),
        "randomized_trials":robustness.randomized_trials,
        "source_fingerprint":benchmark.source_fingerprint,
        "checkpoint_loaded_generation":loaded.generation,
        "checkpoint_post_steps":len(post.steps),
        "benchmark_files":benchmark_files,
        "robustness_files":robustness_files,
        "stability_files":stability_files,
        "math_audit_files":math_audit_files,
        "runtime_transfer_files":transfer_files,
        "network_files":network_files,
        "formation_eligibility_files":eligibility_files,
        "formation_robustness_files":formation_robustness_files,
        "parent_formation_files":parent_formation_files,
        "stratum_geometry_files":stratum_geometry_files,
        "cross_stratum_files":cross_stratum_files,
        "checkpoint_files":checkpoint_files,
    }
    summary_path=outdir/"hardening_summary.json"
    summary_path.write_text(
        json.dumps(summary,indent=2,default=str),
        encoding="utf-8"
    )
    return summary
