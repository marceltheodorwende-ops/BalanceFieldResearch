import argparse, json
from pathlib import Path
from .types import NumericalPolicy
from .carrier import ReferenceGramCarrier
from .seeds import make_random_seed_state, make_commuting_control_state
from .simulate import simulate
from .search import inverse_design
from .report import write_run_report
from .population import PopulationParameters, simulate_population, write_population_report
from .evolution import EvolutionParameters, simulate_evolution, write_evolution_report
from .environment import standard_shift_program, seasonal_program, simulate_environmental_evolution, write_environmental_report
from .learning import LearningParameters, simulate_learning, compare_memory_learning, write_learning_report, write_learning_comparison
from .selfmodel import SelfModelParameters, compare_self_model, write_self_model_report, write_self_model_comparison
from .perspective import PerspectiveParameters, compare_perspective, write_perspective_report, write_perspective_comparison
from .identity import IdentityParameters, compare_identity, write_identity_report, write_identity_comparison
from .alife import (
    SelfOrganizationParameters,
    simulate_self_organization,
    write_self_organization_report,
    organization_metrics,
    search_self_organization,
)

from .benchmarks import run_benchmark_suite, write_benchmark_report
from .robustness import run_robustness_suite, write_robustness_report
from .batch import run_seed_sweep, write_seed_sweep
from .hardening import run_hardening
from .session import ProvenanceManifest, save_bfg_checkpoint, load_bfg_checkpoint

from .sunspot_carrier import prepare_sunspot_validation, validate_sunspot_heldout

from .co2_carrier import prepare_co2_validation, validate_co2_heldout

from .portfolio import ValidationPortfolio, BlindHeldoutGuard, write_portfolio_report, CONFIRMATION_ACK

from .sunspot_validation import prepare_sunspot_validation_current, validate_sunspot_future

from .enso_carrier import prepare_enso_validation, validate_enso_future

from .cross_domain import run_cross_domain_invariants, write_cross_domain_report

from .stability import run_master_stability_audit, write_stability_audit

from .math_audit import run_integrated_math_audit, write_integrated_math_audit

from .finite_closure import run_reduced_runtime

from .runtime_transfer import run_master_runtime_transfer_audit, write_master_runtime_transfer_report

from .formation_dynamics import run_formation_termination_analysis, write_formation_termination_report

from .small_load import run_small_load_contraction_audit, write_small_load_contraction_report

from .network_carrier import prepare_karate_carrier
from .network_audit import run_karate_network_audit, write_karate_network_report

from .formation_eligibility import run_formation_eligibility_audit, write_formation_eligibility_report

from .formation_robustness import run_formation_robustness_audit, write_formation_robustness_report

from .parent_formation import run_parent_formation_radius_audit, write_parent_formation_radius_report

from .stratum_geometry import run_stratum_transition_audit, write_stratum_transition_report

def show(step):
    print(f"generation={step.generation} success={step.success} novelty={step.spectral_novelty}")
    print(f"  persistent_rank={step.diagnostics.get('persistent_rank')} support_rank={step.diagnostics.get('support_rank')}")
    print(f"  spectral_mismatch={step.spectral_mismatch} commutator_norm={step.commutator_norm}")
    print(f"  lambda_min={step.formation_eigenvalue} gap={step.formation_gap}")
    print(f"  crossfed_gain={step.diagnostics.get('crossfed_gain')}")
    if step.terminal_reason:
        print(f"  terminal_reason={step.terminal_reason}")

def common(sp):
    sp.add_argument("--dim",type=int,default=5)
    sp.add_argument("--rank",type=int,default=3)
    sp.add_argument("--steps",type=int,default=10)
    sp.add_argument("--seed",type=int,default=7)
    sp.add_argument("--out",type=str,default="outputs")

def demo(args, control=False):
    policy=NumericalPolicy()
    maker=make_commuting_control_state if control else make_random_seed_state
    state=maker(args.dim,args.rank,args.seed)

    if args.runtime=="finite":
        run=simulate(
            state,
            carrier=None,
            steps=args.steps,
            policy=policy,
            runtime="finite",
            tau=args.tau,
        )
        print(json.dumps(run.summary(),indent=2,default=str))
        return

    carrier=ReferenceGramCarrier()
    run=simulate(
        state,
        carrier,
        args.steps,
        policy,
        runtime="carrier",
    )
    for s in run.steps:
        show(s)
    print(json.dumps(run.summary(),indent=2))
    print(json.dumps(
        write_run_report(
            run,args.out,"control" if control else "demo"
        ),
        indent=2,
    ))

def search(args):
    hits=inverse_design(args.trials,args.dim,args.rank,args.steps,ReferenceGramCarrier(),
                        NumericalPolicy(),args.seed,args.top)
    Path(args.out).mkdir(parents=True,exist_ok=True)
    payload=[]
    for i,h in enumerate(hits,1):
        print(f"#{i} score={h.score:.6f} seed={h.seed} summary={h.run.summary()}")
        payload.append({"rank":i,"score":h.score,"seed":h.seed,"summary":h.run.summary()})
        if i==1:
            write_run_report(h.run,args.out,"best_search")
    Path(args.out,"search_hits.json").write_text(json.dumps(payload,indent=2),encoding="utf-8")

def alife(args):
    params=SelfOrganizationParameters(
        node_count=args.nodes,
        persistent_rank=args.rank,
        neighbor_scale=args.neighbor_scale,
        formation_drive=args.formation_drive,
    )
    run=simulate_self_organization(seed=args.seed,steps=args.steps,params=params)
    for s in run.steps:
        show(s)
    metrics=[organization_metrics(s,params) for s in run.states]
    print(json.dumps({"run":run.summary(),"final_organization":metrics[-1]},indent=2))
    out=Path(args.out)
    write_run_report(run,out,"self_organization_core")
    print(json.dumps(write_self_organization_report(run,out,"self_organization"),indent=2))

def alife_search(args):
    params=SelfOrganizationParameters(
        node_count=args.nodes,
        persistent_rank=args.rank,
        neighbor_scale=args.neighbor_scale,
        formation_drive=args.formation_drive,
    )
    hits=search_self_organization(
        trials=args.trials,steps=args.steps,params=params,seed=args.seed,top_k=args.top
    )
    out=Path(args.out)
    out.mkdir(parents=True,exist_ok=True)
    payload=[]
    for i,(score,seed,run) in enumerate(hits,1):
        final=organization_metrics(run.states[-1],params)
        record={"rank":i,"score":score,"seed":seed,"summary":run.summary(),
                "final_organization":final}
        payload.append(record)
        print(json.dumps(record,indent=2))
        if i==1:
            write_run_report(run,out,"best_self_organization_core")
            write_self_organization_report(run,out,"best_self_organization")
    (out/"self_organization_search_hits.json").write_text(json.dumps(payload,indent=2),encoding="utf-8")


def population(args):
    org=SelfOrganizationParameters(
        node_count=args.nodes,
        persistent_rank=args.rank,
        neighbor_scale=args.neighbor_scale,
        formation_drive=args.formation_drive,
    )
    pop=PopulationParameters(
        min_unit_nodes=args.min_unit_nodes,
        max_unit_nodes=args.max_unit_nodes,
        max_population=args.max_population,
        node_birth_threshold=args.node_birth_threshold,
    )
    run=simulate_population(
        seed=args.seed,
        generations=args.generations,
        org_params=org,
        pop_params=pop,
    )
    print(json.dumps(run.summary(),indent=2))
    print(json.dumps(write_population_report(run,args.out,"population"),indent=2))
    for e in run.events:
        if e["event"] in ("fission","unit_death"):
            print(json.dumps(e,indent=2))



def evolution(args):
    org=SelfOrganizationParameters(
        node_count=args.nodes,
        persistent_rank=args.rank,
        neighbor_scale=args.neighbor_scale,
        formation_drive=args.formation_drive,
    )
    pop=PopulationParameters(
        min_unit_nodes=args.min_unit_nodes,
        max_unit_nodes=args.max_unit_nodes,
        max_population=max(args.carrying_capacity*2,args.carrying_capacity),
        node_birth_threshold=args.node_birth_threshold,
    )
    evo=EvolutionParameters(
        mutation_rate=args.mutation_rate,
        mutation_sigma=args.mutation_sigma,
        carrying_capacity=args.carrying_capacity,
        max_candidate_population=max(args.carrying_capacity*2,args.carrying_capacity+2),
        minimum_reproductive_age=args.minimum_reproductive_age,
        selection_pressure=args.selection_pressure,
    )
    run=simulate_evolution(
        seed=args.seed,
        generations=args.generations,
        base_org=org,
        base_pop=pop,
        evo=evo,
    )
    print(json.dumps(run.summary(),indent=2))
    print(json.dumps(write_evolution_report(run,args.out,"evolution"),indent=2))
    for e in run.events:
        if e["event"] in ("fission","mutation","selection_death"):
            print(json.dumps(e,indent=2))



def environment(args):
    org=SelfOrganizationParameters(
        node_count=args.nodes,
        persistent_rank=args.rank,
        neighbor_scale=args.neighbor_scale,
        formation_drive=args.formation_drive,
    )
    pop=PopulationParameters(
        min_unit_nodes=args.min_unit_nodes,
        max_unit_nodes=args.max_unit_nodes,
        max_population=max(args.founders*2,args.carrying_capacity*2),
        node_birth_threshold=args.node_birth_threshold,
    )
    evo=EvolutionParameters(
        mutation_rate=args.mutation_rate,
        mutation_sigma=args.mutation_sigma,
        carrying_capacity=args.carrying_capacity,
        max_candidate_population=max(args.founders*2,args.carrying_capacity*2),
        minimum_reproductive_age=args.minimum_reproductive_age,
        selection_pressure=1.0,
    )
    if args.program=="seasonal":
        program=seasonal_program(period=args.period,generations=args.generations)
    else:
        program=standard_shift_program(shift_generation=args.shift_generation)
    run=simulate_environmental_evolution(
        seed=args.seed,
        generations=args.generations,
        program=program,
        base_org=org,
        base_pop=pop,
        evo=evo,
        founder_count=args.founders,
        founder_sigma=args.founder_sigma,
    )
    print(json.dumps(run.summary(),indent=2))
    print(json.dumps(write_environmental_report(run,args.out,"environment"),indent=2))
    for e in run.events:
        if e["event"] in ("environment_shift","selection_round"):
            print(json.dumps(e,indent=2))



def learning(args):
    learn=LearningParameters(
        exploration_sigma=args.exploration_sigma,
        retrieval_blend=args.retrieval_blend,
        max_memory_slots=args.max_memory_slots,
        witness_min_gap=args.witness_min_gap,
    )
    comparison=compare_memory_learning(
        seed=args.seed,
        generations=args.generations,
        learn=learn,
    )
    enabled=comparison["memory_enabled"]
    disabled=comparison["memory_disabled"]
    print(json.dumps({
        "memory_enabled":enabled.summary(),
        "memory_disabled":disabled.summary(),
        "comparison":comparison["summary"],
    },indent=2))
    out=Path(args.out)
    write_learning_report(enabled,out,"learning_memory")
    write_learning_report(disabled,out,"learning_control")
    print(json.dumps(write_learning_comparison(comparison,out,"learning_comparison"),indent=2))
    for e in enabled.events:
        if e["event"] in ("witness_recovery","memory_export","policy_update"):
            print(json.dumps(e,indent=2))



def self_model(args):
    params=SelfModelParameters(
        min_observations=args.min_observations,
        candidate_count=args.candidates,
        candidate_sigma=args.candidate_sigma,
        recurrent_rho_max=args.rho_max,
    )
    comparison=compare_self_model(
        seed=args.seed,
        generations=args.generations,
        self_params=params,
    )
    enabled=comparison["self_model"]
    control=comparison["ablated_control"]
    print(json.dumps({
        "self_model":enabled.summary(),
        "ablated_control":control.summary(),
        "comparison":comparison["summary"],
    },indent=2))
    out=Path(args.out)
    write_self_model_report(enabled,out,"self_model")
    write_self_model_report(control,out,"self_model_control")
    print(json.dumps(
        write_self_model_comparison(comparison,out,"self_model_comparison"),
        indent=2
    ))
    for e in enabled.events:
        if e["event"] in ("self_model_action","self_prediction"):
            if e["generation"] % 8 == 0:
                print(json.dumps(e,indent=2))



def perspective(args):
    params=PerspectiveParameters(
        recurrent_alpha=args.alpha,
        epsilon_multiplicity_unity=args.epsilon,
        max_multiplicity_unity=args.max_distance,
        export_residual_threshold=args.export_threshold,
        standpoint_action_weight=args.action_weight,
    )
    comparison=compare_perspective(
        seed=args.seed,
        generations=args.generations,
        perspective_params=params,
    )
    enabled=comparison["perspective"]
    control=comparison["ablated_control"]
    print(json.dumps({
        "perspective":enabled.summary(),
        "ablated_control":control.summary(),
        "comparison":comparison["summary"],
    },indent=2))
    out=Path(args.out)
    write_perspective_report(enabled,out,"perspective")
    write_perspective_report(control,out,"perspective_control")
    print(json.dumps(
        write_perspective_comparison(comparison,out,"perspective_comparison"),
        indent=2
    ))
    for e in enabled.events:
        if e["event"] in ("perspective_action","perspective_export"):
            if e.get("generation",0) % 8 == 0:
                print(json.dumps(e,indent=2))



def identity(args):
    params=IdentityParameters(
        recurrent_alpha=args.alpha,
        epsilon_identity=args.epsilon,
        max_identity_distance=args.max_distance,
        export_component_threshold=args.export_threshold,
        minimum_self_index_similarity=args.min_index_similarity,
    )
    comparison=compare_identity(
        seed=args.seed,
        generations=args.generations,
        identity_params=params,
    )
    enabled=comparison["identity"]
    control=comparison["ablated_control"]
    print(json.dumps({
        "identity":enabled.summary(),
        "ablated_control":control.summary(),
        "comparison":comparison["summary"],
    },indent=2))
    out=Path(args.out)
    write_identity_report(enabled,out,"identity")
    write_identity_report(control,out,"identity_control")
    print(json.dumps(
        write_identity_comparison(comparison,out,"identity_comparison"),
        indent=2
    ))
    for e in enabled.events:
        if e["event"] in ("identity_export","identity_failure"):
            print(json.dumps(e,indent=2))



def benchmark(args):
    selected=args.only if args.only else None
    report=run_benchmark_suite(selected=selected)
    print(json.dumps(report.summary(),indent=2,default=str))
    print(json.dumps(write_benchmark_report(report,args.out),indent=2))

def robustness(args):
    report=run_robustness_suite(
        randomized_trials=args.trials,
        commuting_controls=args.commuting,
        noncommuting_controls=args.noncommuting,
        seed=args.seed,
        workers=args.workers,
    )
    compact={
        k:v for k,v in report.summary().items()
        if k!="diagnostics"
    }
    print(json.dumps(compact,indent=2,default=str))
    print(json.dumps(write_robustness_report(report,args.out),indent=2))

def sweep(args):
    seeds=list(range(args.seed,args.seed+args.runs))
    run=run_seed_sweep(
        seeds=seeds,
        mode=args.mode,
        horizon=args.horizon,
        workers=args.workers,
    )
    print(json.dumps({
        "mode":run.mode,
        "runs":len(run.items),
        "workers":run.workers,
        "source_fingerprint":run.source_fingerprint,
    },indent=2))
    print(json.dumps(write_seed_sweep(run,args.out),indent=2))

def checkpoint(args):
    state=make_random_seed_state(
        dim=args.dim,persistent_rank=args.rank,seed=args.seed
    )
    run=simulate(
        state,ReferenceGramCarrier(),steps=args.pre_steps,
        policy=NumericalPolicy()
    )
    saved=run.states[-1]
    manifest=ProvenanceManifest.build(
        experiment="cli_checkpoint",
        seed=args.seed,
        parameters={
            "dim":args.dim,
            "rank":args.rank,
            "pre_steps":args.pre_steps,
            "post_steps":args.post_steps,
        },
    )
    files=save_bfg_checkpoint(
        saved,args.out,name="state",manifest=manifest,
        extra={"pre_summary":run.summary()}
    )
    loaded,loaded_manifest,extra=load_bfg_checkpoint(
        args.out,name="state"
    )
    resumed=simulate(
        loaded,ReferenceGramCarrier(),steps=args.post_steps,
        policy=NumericalPolicy()
    )
    print(json.dumps({
        "checkpoint_generation":loaded.generation,
        "resume_steps":len(resumed.steps),
        "final_generation":resumed.states[-1].generation,
        "files":files,
        "source_fingerprint":loaded_manifest["source_fingerprint"],
    },indent=2))

def hardening(args):
    summary=run_hardening(
        args.out,
        randomized_trials=args.trials,
        seed=args.seed,
        workers=args.workers,
    )
    print(json.dumps(summary,indent=2,default=str))



def sunspot_prepare(args):
    result=prepare_sunspot_validation_current(
        args.out,
        lag=args.lag,
    )
    print(json.dumps(result,indent=2,default=str))

def sunspot_validate(args):
    result=validate_sunspot_future(
        args.prepared,
        future_data_path=args.data,
        permit_path=args.permit,
    )
    print(json.dumps(result,indent=2,default=str))



def co2_prepare(args):
    result=prepare_co2_validation(
        args.out,
        lag=args.lag,
        calibration_end=args.calibration_end,
        heldout_start=args.heldout_start,
    )
    print(json.dumps(result,indent=2,default=str))

def co2_validate(args):
    result=validate_co2_heldout(args.prepared,permit_path=args.permit)
    print(json.dumps(result,indent=2,default=str))



def portfolio_status(args):
    portfolio=ValidationPortfolio()
    audit=portfolio.audit()
    files=write_portfolio_report(portfolio,args.out)
    print(json.dumps({
        "audit":audit,
        "files":files,
    },indent=2,default=str))

def portfolio_seal(args):
    portfolio=ValidationPortfolio()
    guard=BlindHeldoutGuard(portfolio)
    seal=guard.build_seal(args.id)
    print(json.dumps(seal,indent=2,default=str))

def portfolio_permit(args):
    portfolio=ValidationPortfolio()
    guard=BlindHeldoutGuard(portfolio)
    path=guard.issue_confirmation_permit(
        args.id,args.ack
    )
    print(json.dumps({
        "carrier_id":args.id,
        "permit":str(path),
        "warning":"Creating a permit does not open held-out data; using it does.",
    },indent=2))



def enso_prepare(args):
    result=prepare_enso_validation(
        args.out,
        lag=args.lag,
    )
    print(json.dumps(result,indent=2,default=str))

def enso_validate(args):
    result=validate_enso_future(
        args.prepared,
        future_data_path=args.data,
        permit_path=args.permit,
    )
    print(json.dumps(result,indent=2,default=str))



def cross_domain(args):
    result=run_cross_domain_invariants()
    files=write_cross_domain_report(result,args.out)
    compact={
        "status":result["status"],
        "heldout_metrics_evaluated":result["heldout_metrics_evaluated"],
        "all_development_reclosures_successful":
            result["all_development_reclosures_successful"],
        "all_successful_reclosures_novel":
            result["all_successful_reclosures_novel"],
        "shared_corridors":result["shared_corridors"],
        "files":files,
    }
    print(json.dumps(compact,indent=2,default=str))



def stability_audit(args):
    result=run_master_stability_audit(
        horizon=args.horizon,
    )
    files=write_stability_audit(result,args.out)
    compact={
        "audit_passed":result["audit_passed"],
        "theorem_scope":result["theorem_scope"],
        "development_carrier_operators":
            result["development_carrier_operators"],
        "development_carrier_criterion_passed":
            result["development_carrier_criterion_passed"],
        "controls_passed":result["controls_passed"],
        "synthetic_core_passed":result["synthetic_core_passed"],
        "families":result["families"],
        "files":files,
    }
    print(json.dumps(compact,indent=2,default=str))



def integrated_math_audit(args):
    result=run_integrated_math_audit()
    files=write_integrated_math_audit(result,args.out)
    print(json.dumps({
        "audit_passed":result["audit_passed"],
        "checks":result["checks"],
        "claim_register":result["claim_register"],
        "files":files,
    },indent=2,default=str))



def transfer_audit(args):
    result=run_master_runtime_transfer_audit(
        recursive_horizon=args.horizon,
        tau=args.tau,
        limit_per_carrier=args.limit,
    )
    files=write_master_runtime_transfer_report(
        result,
        args.out,
    )
    compact={
        "audit_passed":result["audit_passed"],
        "heldout_metrics_evaluated":
            result["heldout_metrics_evaluated"],
        "states_total":result["states_total"],
        "states_processed":result["states_processed"],
        "exceptions":result["exceptions"],
        "first_step_success_fraction":
            result["first_step_success_fraction"],
        "carriers":result["carriers"],
        "shared_transformation_corridors":
            result["shared_transformation_corridors"],
        "files":files,
    }
    print(json.dumps(compact,indent=2,default=str))



def formation_analysis(args):
    result=run_formation_termination_analysis(
        horizon=args.horizon,
        tau=args.tau,
        limit_per_carrier=args.limit,
    )
    files=write_formation_termination_report(
        result,
        args.out,
    )
    compact={
        "heldout_metrics_evaluated":
            result["heldout_metrics_evaluated"],
        "states_total":result["states_total"],
        "first_step_success_fraction":
            result["first_step_success_fraction"],
        "shared_formation_normalizations":
            result["shared_formation_normalizations"],
        "formation_normalization_corridors":
            result["formation_normalization_corridors"],
        "pooled_loglog_y_decay_exponent":
            result["pooled_loglog_y_decay_exponent"],
        "terminal_reason_counts":
            result["terminal_reason_counts"],
        "domains":result["domains"],
        "files":files,
    }
    print(json.dumps(compact,indent=2,default=str))



def small_load_audit(args):
    result=run_small_load_contraction_audit(
        horizon=args.horizon,
        tau=args.tau,
        limit_per_carrier=args.limit,
    )
    files=write_small_load_contraction_report(
        result,
        args.out,
    )
    compact={
        "heldout_metrics_evaluated":
            result["heldout_metrics_evaluated"],
        "successful_transitions":
            result["successful_transitions"],
        "all_theorem_bounds_verified":
            result["all_theorem_bounds_verified"],
        "domain_summaries":
            result["domain_summaries"],
        "depth_summaries":
            result["depth_summaries"],
        "observed_corridor_envelope":
            result["observed_corridor_envelope"],
        "files":files,
    }
    print(json.dumps(compact,indent=2,default=str))



def network_prepare(args):
    files=prepare_karate_carrier(args.out)
    print(json.dumps(files,indent=2,default=str))

def network_audit(args):
    result=run_karate_network_audit(
        recursive_horizon=args.horizon,
    )
    files=write_karate_network_report(result,args.out)
    compact={
        "status":result["status"],
        "heldout_metrics_evaluated":
            result["heldout_metrics_evaluated"],
        "state_contract_valid":
            result["state_contract_valid"],
        "measurements":result["measurements"],
        "first_step_successes":
            result["first_step_successes"],
        "first_step_success_fraction":
            result["first_step_success_fraction"],
        "first_step_failure_reasons":
            result["first_step_failure_reasons"],
        "small_load":result["small_load"],
        "permutation_equivariance":
            result["permutation_equivariance"],
        "four_domain_transform_corridors":
            result["four_domain_transform_corridors"],
        "four_domain_formation_corridors":
            result["four_domain_formation_corridors"],
        "files":files,
    }
    print(json.dumps(compact,indent=2,default=str))



def formation_eligibility_audit(args):
    result=run_formation_eligibility_audit(
        limit_per_timeseries_carrier=args.limit,
        include_full_network=True,
    )
    files=write_formation_eligibility_report(
        result,
        args.out,
    )
    compact={
        "heldout_metrics_evaluated":
            result["heldout_metrics_evaluated"],
        "states_total":result["states_total"],
        "maximum_generalized_match_residual":
            result["maximum_generalized_match_residual"],
        "domains":result["domains"],
        "network_explanation":
            result["network_explanation"],
        "files":files,
    }
    print(json.dumps(compact,indent=2,default=str))



def formation_robustness_audit(args):
    result=run_formation_robustness_audit(
        limit_per_timeseries_carrier=args.limit,
        include_full_network=True,
    )
    files=write_formation_robustness_report(
        result,
        args.out,
    )
    compact={
        "heldout_metrics_evaluated":
            result["heldout_metrics_evaluated"],
        "states_total":result["states_total"],
        "gate_states":result["gate_states"],
        "boundary_controls":result["boundary_controls"],
        "inside_preserved":result["inside_preserved"],
        "outside_crossed":result["outside_crossed"],
        "domains":result["domains"],
        "network_bifurcation":
            result["network_bifurcation"],
        "files":files,
    }
    print(json.dumps(compact,indent=2,default=str))



def parent_formation_audit(args):
    result=run_parent_formation_radius_audit(
        limit_per_timeseries_carrier=args.limit,
        include_full_network=True,
    )
    files=write_parent_formation_radius_report(
        result,
        args.out,
    )
    compact={
        "heldout_metrics_evaluated":
            result["heldout_metrics_evaluated"],
        "states_total":result["states_total"],
        "certified_states":result["certified_states"],
        "structured_controls":result["structured_controls"],
        "structured_status_preserved":
            result["structured_status_preserved"],
        "structured_active_bound_verified":
            result["structured_active_bound_verified"],
        "runtime_controls":result["runtime_controls"],
        "runtime_status_preserved":
            result["runtime_status_preserved"],
        "runtime_same_active_rank":
            result["runtime_same_active_rank"],
        "runtime_limiting_surface_counts":
            result["runtime_limiting_surface_counts"],
        "domains":result["domains"],
        "network":result["network"],
        "files":files,
    }
    print(json.dumps(compact,indent=2,default=str))



def stratum_transition_audit(args):
    result=run_stratum_transition_audit(
        limit_per_timeseries_carrier=args.limit,
        include_full_network=True,
    )
    files=write_stratum_transition_report(
        result,
        args.out,
    )
    compact={
        "heldout_metrics_evaluated":
            result["heldout_metrics_evaluated"],
        "states_total":result["states_total"],
        "active_upward_bottleneck_states":
            result["active_upward_bottleneck_states"],
        "persistent_loss_bottleneck_states":
            result["persistent_loss_bottleneck_states"],
        "domains":result["domains"],
        "files":files,
    }
    print(json.dumps(compact,indent=2,default=str))


def main():
    p=argparse.ArgumentParser(prog="bfg-studio",description="BFG Emergence Studio")
    sub=p.add_subparsers(dest="cmd",required=True)

    d=sub.add_parser("demo",help="generic BFG emergence demo; finite master runtime by default")
    common(d)
    d.add_argument("--runtime",choices=["finite","legacy"],default="finite")
    d.add_argument("--tau",type=float,default=1.0)
    d.set_defaults(func=lambda a:demo(a,False))

    c=sub.add_parser("control",help="commuting BFG control; finite master runtime by default")
    common(c)
    c.add_argument("--runtime",choices=["finite","legacy"],default="finite")
    c.add_argument("--tau",type=float,default=1.0)
    c.set_defaults(func=lambda a:demo(a,True))

    s=sub.add_parser("search",help="generic inverse search for novel seeds")
    common(s); s.add_argument("--trials",type=int,default=100); s.add_argument("--top",type=int,default=5)
    s.set_defaults(func=search)

    a=sub.add_parser("alife",help="self-organization / artificial-life carrier experiment")
    a.add_argument("--nodes",type=int,default=24)
    a.add_argument("--rank",type=int,default=6)
    a.add_argument("--steps",type=int,default=20)
    a.add_argument("--seed",type=int,default=7)
    a.add_argument("--neighbor-scale",type=float,default=0.32)
    a.add_argument("--formation-drive",type=float,default=1.45)
    a.add_argument("--out",type=str,default="outputs/alife")
    a.set_defaults(func=alife)

    q=sub.add_parser("alife-search",help="search self-organizing carrier seeds")
    q.add_argument("--nodes",type=int,default=24)
    q.add_argument("--rank",type=int,default=6)
    q.add_argument("--steps",type=int,default=16)
    q.add_argument("--seed",type=int,default=1)
    q.add_argument("--neighbor-scale",type=float,default=0.32)
    q.add_argument("--formation-drive",type=float,default=1.45)
    q.add_argument("--trials",type=int,default=50)
    q.add_argument("--top",type=int,default=5)
    q.add_argument("--out",type=str,default="outputs/alife_search")
    q.set_defaults(func=alife_search)

    r=sub.add_parser("population",help="independent-unit population and fission experiment")
    r.add_argument("--nodes",type=int,default=24)
    r.add_argument("--rank",type=int,default=6)
    r.add_argument("--generations",type=int,default=36)
    r.add_argument("--seed",type=int,default=1341550191)
    r.add_argument("--neighbor-scale",type=float,default=0.32)
    r.add_argument("--formation-drive",type=float,default=1.45)
    r.add_argument("--min-unit-nodes",type=int,default=4)
    r.add_argument("--max-unit-nodes",type=int,default=40)
    r.add_argument("--max-population",type=int,default=32)
    r.add_argument("--node-birth-threshold",type=float,default=0.88)
    r.add_argument("--out",type=str,default="outputs/population")
    r.set_defaults(func=population)

    v=sub.add_parser("evolution",help="heritable variation and selection across independent BFG units")
    v.add_argument("--nodes",type=int,default=24)
    v.add_argument("--rank",type=int,default=6)
    v.add_argument("--generations",type=int,default=90)
    v.add_argument("--seed",type=int,default=1341550191)
    v.add_argument("--neighbor-scale",type=float,default=0.32)
    v.add_argument("--formation-drive",type=float,default=1.45)
    v.add_argument("--min-unit-nodes",type=int,default=4)
    v.add_argument("--max-unit-nodes",type=int,default=42)
    v.add_argument("--node-birth-threshold",type=float,default=0.82)
    v.add_argument("--mutation-rate",type=float,default=0.75)
    v.add_argument("--mutation-sigma",type=float,default=0.055)
    v.add_argument("--carrying-capacity",type=int,default=12)
    v.add_argument("--minimum-reproductive-age",type=int,default=5)
    v.add_argument("--selection-pressure",type=float,default=1.0)
    v.add_argument("--out",type=str,default="outputs/evolution")
    v.set_defaults(func=evolution)

    w=sub.add_parser("environment",help="evolution under a changing environment")
    w.add_argument("--program",choices=["shift","seasonal"],default="shift")
    w.add_argument("--nodes",type=int,default=24)
    w.add_argument("--rank",type=int,default=6)
    w.add_argument("--generations",type=int,default=72)
    w.add_argument("--seed",type=int,default=1341550191)
    w.add_argument("--founders",type=int,default=12)
    w.add_argument("--founder-sigma",type=float,default=0.16)
    w.add_argument("--shift-generation",type=int,default=30)
    w.add_argument("--period",type=int,default=24)
    w.add_argument("--neighbor-scale",type=float,default=0.32)
    w.add_argument("--formation-drive",type=float,default=1.45)
    w.add_argument("--min-unit-nodes",type=int,default=4)
    w.add_argument("--max-unit-nodes",type=int,default=42)
    w.add_argument("--node-birth-threshold",type=float,default=0.84)
    w.add_argument("--mutation-rate",type=float,default=0.85)
    w.add_argument("--mutation-sigma",type=float,default=0.055)
    w.add_argument("--carrying-capacity",type=int,default=12)
    w.add_argument("--minimum-reproductive-age",type=int,default=4)
    w.add_argument("--out",type=str,default="outputs/environment")
    w.set_defaults(func=environment)

    l=sub.add_parser("learning",help="within-lifetime learning and memory experiment")
    l.add_argument("--generations",type=int,default=60)
    l.add_argument("--seed",type=int,default=1341550191)
    l.add_argument("--exploration-sigma",type=float,default=0.035)
    l.add_argument("--retrieval-blend",type=float,default=0.72)
    l.add_argument("--max-memory-slots",type=int,default=8)
    l.add_argument("--witness-min-gap",type=int,default=4)
    l.add_argument("--out",type=str,default="outputs/learning")
    l.set_defaults(func=learning)

    sm=sub.add_parser("self-model",help="BFG self-model closure and self-prediction experiment")
    sm.add_argument("--generations",type=int,default=80)
    sm.add_argument("--seed",type=int,default=1341550191)
    sm.add_argument("--min-observations",type=int,default=12)
    sm.add_argument("--candidates",type=int,default=5)
    sm.add_argument("--candidate-sigma",type=float,default=0.035)
    sm.add_argument("--rho-max",type=float,default=1.04)
    sm.add_argument("--out",type=str,default="outputs/self_model")
    sm.set_defaults(func=self_model)

    pp=sub.add_parser("perspective",help="BFG perspective closure and unified standpoint experiment")
    pp.add_argument("--generations",type=int,default=96)
    pp.add_argument("--seed",type=int,default=1341550191)
    pp.add_argument("--alpha",type=float,default=0.985)
    pp.add_argument("--epsilon",type=float,default=0.035)
    pp.add_argument("--max-distance",type=float,default=0.62)
    pp.add_argument("--export-threshold",type=float,default=0.46)
    pp.add_argument("--action-weight",type=float,default=0.05)
    pp.add_argument("--out",type=str,default="outputs/perspective")
    pp.set_defaults(func=perspective)

    ident=sub.add_parser("identity",help="BFG Level-30 temporal Identity Closure experiment")
    ident.add_argument("--generations",type=int,default=120)
    ident.add_argument("--seed",type=int,default=1341550191)
    ident.add_argument("--alpha",type=float,default=0.965)
    ident.add_argument("--epsilon",type=float,default=0.0015)
    ident.add_argument("--max-distance",type=float,default=0.14)
    ident.add_argument("--export-threshold",type=float,default=0.16)
    ident.add_argument("--min-index-similarity",type=float,default=0.80)
    ident.add_argument("--out",type=str,default="outputs/identity")
    ident.set_defaults(func=identity)

    bm=sub.add_parser("benchmark",help="run the frozen cross-layer reference benchmark suite")
    bm.add_argument("--only",nargs="*",default=None)
    bm.add_argument("--out",type=str,default="outputs/benchmarks")
    bm.set_defaults(func=benchmark)

    rb=sub.add_parser("robustness",help="randomized algebraic and numerical robustness suite")
    rb.add_argument("--trials",type=int,default=200)
    rb.add_argument("--commuting",type=int,default=40)
    rb.add_argument("--noncommuting",type=int,default=40)
    rb.add_argument("--seed",type=int,default=20260923)
    rb.add_argument("--workers",type=int,default=None)
    rb.add_argument("--out",type=str,default="outputs/robustness")
    rb.set_defaults(func=robustness)

    sw=sub.add_parser("sweep",help="parallel seed sweep for alife, population, or evolution")
    sw.add_argument("--mode",choices=["alife","population","evolution"],default="alife")
    sw.add_argument("--runs",type=int,default=20)
    sw.add_argument("--seed",type=int,default=1)
    sw.add_argument("--horizon",type=int,default=20)
    sw.add_argument("--workers",type=int,default=None)
    sw.add_argument("--out",type=str,default="outputs/sweep")
    sw.set_defaults(func=sweep)

    cp=sub.add_parser("checkpoint",help="save, verify, load, and resume a BFG state")
    cp.add_argument("--dim",type=int,default=6)
    cp.add_argument("--rank",type=int,default=4)
    cp.add_argument("--seed",type=int,default=17)
    cp.add_argument("--pre-steps",type=int,default=2)
    cp.add_argument("--post-steps",type=int,default=2)
    cp.add_argument("--out",type=str,default="outputs/checkpoint")
    cp.set_defaults(func=checkpoint)

    hd=sub.add_parser("hardening",help="run benchmark + robustness + checkpoint audit")
    hd.add_argument("--trials",type=int,default=200)
    hd.add_argument("--seed",type=int,default=20260923)
    hd.add_argument("--workers",type=int,default=None)
    hd.add_argument("--out",type=str,default="outputs/hardening")
    hd.set_defaults(func=hardening)

    sp=sub.add_parser("sunspot-prepare",help="rebuild annual sunspots under the readiness-first portfolio using 1700-2008 as development data")
    sp.add_argument("--lag",type=int,default=12)
    sp.add_argument("--out",type=str,default="outputs/real_sunspots")
    sp.set_defaults(func=sunspot_prepare)

    sv=sub.add_parser("sunspot-validate",help="open the prospective 2009-2025 sunspot confirmation using external future data and a one-time permit")
    sv.add_argument("--prepared",type=str,default="outputs/real_sunspots")
    sv.add_argument("--data",type=str,required=True,help="CSV with YEAR,SUNACTIVITY for every year 2009-2025")
    sv.add_argument("--permit",type=str,required=True)
    sv.set_defaults(func=sunspot_validate)

    cp2=sub.add_parser("co2-prepare",help="run calibration/rolling preflight and freeze a sealed Mauna Loa CO2 validation plan")
    cp2.add_argument("--lag",type=int,default=24)
    cp2.add_argument("--calibration-end",type=str,default="1990-12-31")
    cp2.add_argument("--heldout-start",type=str,default="1991-01-01")
    cp2.add_argument("--out",type=str,default="outputs/real_co2")
    cp2.set_defaults(func=co2_prepare)

    cv2=sub.add_parser("co2-validate",help="open the frozen CO2 held-out evaluation using a one-time portfolio permit")
    cv2.add_argument("--prepared",type=str,default="outputs/real_co2")
    cv2.add_argument("--permit",type=str,required=True)
    cv2.set_defaults(func=co2_validate)

    ep=sub.add_parser("enso-prepare",help="build the development-only ENSO/Pacific-SST readiness preflight")
    ep.add_argument("--lag",type=int,default=24)
    ep.add_argument("--out",type=str,default="outputs/real_enso")
    ep.set_defaults(func=enso_prepare)

    ev=sub.add_parser("enso-validate",help="open the prospective 2011-2025 ENSO confirmation using external future data and a one-time permit")
    ev.add_argument("--prepared",type=str,default="outputs/real_enso")
    ev.add_argument("--data",type=str,required=True,help="CSV with date,sst for every month 2011-01 through 2025-12")
    ev.add_argument("--permit",type=str,required=True)
    ev.set_defaults(func=enso_validate)

    pf=sub.add_parser("portfolio",help="audit and report the empirical validation portfolio without opening held-out data")
    pf.add_argument("--out",type=str,default="validation")
    pf.set_defaults(func=portfolio_status)

    ps=sub.add_parser("portfolio-seal",help="cryptographically seal one READY carrier against mapping/plan/source drift")
    ps.add_argument("--id",type=str,required=True)
    ps.set_defaults(func=portfolio_seal)

    pp=sub.add_parser("portfolio-permit",help="issue a one-time confirmatory held-out opening permit for a sealed READY carrier")
    pp.add_argument("--id",type=str,required=True)
    pp.add_argument("--ack",type=str,required=True,help=f'exact acknowledgement: {CONFIRMATION_ACK}')
    pp.set_defaults(func=portfolio_permit)

    cd=sub.add_parser("cross-domain",help="compare development-only BFG invariant coordinates across all READY real carriers")
    cd.add_argument("--out",type=str,default="outputs/cross_domain")
    cd.set_defaults(func=cross_domain)

    sta=sub.add_parser("stability-audit",help="audit finite-dimensional BFG recursive power-boundedness theorem hypotheses")
    sta.add_argument("--horizon",type=int,default=64)
    sta.add_argument("--out",type=str,default="outputs/stability")
    sta.set_defaults(func=stability_audit)

    sma=sub.add_parser("math-audit",help="audit the integrated BFG mathematical closure layer")
    sma.add_argument("--out",type=str,default="outputs/math_audit")
    sma.set_defaults(func=integrated_math_audit)

    ta=sub.add_parser("transfer-audit",help="transport all allowed real-domain development/calibration states through the common finite master runtime")
    ta.add_argument("--horizon",type=int,default=4)
    ta.add_argument("--tau",type=float,default=1.0)
    ta.add_argument("--limit",type=int,default=None,help="optional per-carrier smoke-test limit")
    ta.add_argument("--out",type=str,default="outputs/runtime_transfer")
    ta.set_defaults(func=transfer_audit)

    fa=sub.add_parser("formation-analysis",help="analyze formation normalization, neutral-load decay and the recursive terminal surface")
    fa.add_argument("--horizon",type=int,default=6)
    fa.add_argument("--tau",type=float,default=1.0)
    fa.add_argument("--limit",type=int,default=None,help="optional per-carrier smoke-test limit")
    fa.add_argument("--out",type=str,default="outputs/formation_dynamics")
    fa.set_defaults(func=formation_analysis)

    sl=sub.add_parser("small-load-audit",help="verify the multidimensional quadratic successor-load theorem on allowed real-domain states")
    sl.add_argument("--horizon",type=int,default=4)
    sl.add_argument("--tau",type=float,default=1.0)
    sl.add_argument("--limit",type=int,default=None,help="optional per-carrier smoke-test limit")
    sl.add_argument("--out",type=str,default="outputs/small_load")
    sl.set_defaults(func=small_load_audit)

    np4=sub.add_parser("network-prepare",help="prepare the exploratory real weighted interaction-network carrier")
    np4.add_argument("--out",type=str,default="outputs/real_network")
    np4.set_defaults(func=network_prepare)

    na4=sub.add_parser("network-audit",help="audit the exploratory real relational carrier and four-domain extension")
    na4.add_argument("--horizon",type=int,default=4)
    na4.add_argument("--out",type=str,default="outputs/real_network")
    na4.set_defaults(func=network_audit)

    fe=sub.add_parser("formation-eligibility",help="audit the exact generalized-eigenvalue formation criterion and parent-ground witness")
    fe.add_argument("--limit",type=int,default=None,help="optional per-time-series-carrier smoke-test limit; network remains complete")
    fe.add_argument("--out",type=str,default="outputs/formation_eligibility")
    fe.set_defaults(func=formation_eligibility_audit)

    fr=sub.add_parser("formation-robustness",help="audit exact active-operator formation margins and bifurcation surfaces")
    fr.add_argument("--limit",type=int,default=None,help="optional per-time-series-carrier smoke-test limit; network remains complete")
    fr.add_argument("--out",type=str,default="outputs/formation_robustness")
    fr.set_defaults(func=formation_robustness_audit)

    pf=sub.add_parser("parent-formation",help="audit the conditional parent-state formation radius on the fixed admissible rank stratum")
    pf.add_argument("--limit",type=int,default=None,help="optional per-time-series-carrier smoke-test limit; network remains complete")
    pf.add_argument("--out",type=str,default="outputs/parent_formation")
    pf.set_defaults(func=parent_formation_audit)

    sg=sub.add_parser("stratum-audit",help="audit formation, persistent-rank and active-rank bifurcation surfaces")
    sg.add_argument("--limit",type=int,default=None,help="optional per-time-series-carrier smoke-test limit; network remains complete")
    sg.add_argument("--out",type=str,default="outputs/stratum_geometry")
    sg.set_defaults(func=stratum_transition_audit)


    args=p.parse_args()
    args.func(args)

if __name__=="__main__":
    main()
