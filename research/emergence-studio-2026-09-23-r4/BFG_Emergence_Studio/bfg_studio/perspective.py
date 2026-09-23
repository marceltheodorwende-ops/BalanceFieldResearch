from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
import csv
import json
import math
import numpy as np
import matplotlib.pyplot as plt

from .types import BFGState, NumericalPolicy
from .alife import SelfOrganizationParameters, organization_metrics
from .population import PopulationParameters
from .evolution import EvolutionParameters, default_traits, traits_to_org
from .environment import EnvironmentState, EnvironmentProgram
from .learning import (
    LearningParameters,
    MemoryState,
    PLASTIC_TRAITS,
    zero_policy,
    effective_traits,
    environment_cue,
    retrieve_memory,
    update_memory,
    _bounded_policy_move,
    _policy_vector,
    _evaluate_policy_once,
)
from .selfmodel import (
    SelfModelParameters,
    make_self_model,
    organism_readout,
    world_readout,
    update_world_model,
    predict_world,
    self_predictor_input,
    contextual_self_prediction,
    update_contextual_self_transition,
    self_reference_metrics,
    _candidate_policies,
    _predicted_candidate_score,
)


PERSPECTIVE_FEATURE_NAMES = (
    "resource_position",
    "stability_position",
    "maintenance_position",
    "retention_position",
    "export_position",
    "agency_position",
    "continuity_position",
)


@dataclass(frozen=True)
class PerspectiveParameters:
    recurrent_alpha: float = 0.985
    epsilon_multiplicity_unity: float = 0.035
    max_multiplicity_unity: float = 0.62
    export_residual_threshold: float = 0.46
    minimum_representation_norm: float = 0.04
    minimum_active_representations: int = 4
    consensus_temperature: float = 0.22
    standpoint_action_weight: float = 0.05
    minimum_standpoint_persistence: float = 0.70
    recursive_rho_max: float = 1.02

    def validate(self):
        if not (0.90 <= self.recurrent_alpha < 1.0):
            raise ValueError("recurrent_alpha must be in [0.90,1)")
        if self.epsilon_multiplicity_unity <= 0:
            raise ValueError("epsilon_multiplicity_unity must be positive")
        if self.max_multiplicity_unity <= self.epsilon_multiplicity_unity:
            raise ValueError("max corridor bound must exceed epsilon")
        if self.export_residual_threshold <= 0:
            raise ValueError("export_residual_threshold must be positive")
        if self.minimum_active_representations < 3:
            raise ValueError("at least three active self-representations are required")
        if self.consensus_temperature <= 0:
            raise ValueError("consensus_temperature must be positive")
        if not (0 <= self.standpoint_action_weight <= 1):
            raise ValueError("standpoint_action_weight must lie in [0,1]")
        if not (0 < self.minimum_standpoint_persistence <= 1):
            raise ValueError("minimum_standpoint_persistence must lie in (0,1]")
        if self.recursive_rho_max <= 0:
            raise ValueError("recursive_rho_max must be positive")


@dataclass
class PerspectiveState:
    standpoint: np.ndarray
    previous_standpoint: np.ndarray | None = None
    age: int = 0
    exports: int = 0
    closure_passes: int = 0
    closure_failures: int = 0
    fragmentation_failures: int = 0
    collapse_failures: int = 0
    over_unification_failures: int = 0
    instability_failures: int = 0


@dataclass
class PerspectiveRun:
    initial_seed: int
    frames: list[dict]
    events: list[dict]
    final_state: BFGState
    final_policy: dict[str, float]
    memory: MemoryState
    perspective: PerspectiveState
    perspective_enabled: bool
    core_steps: int
    successful_reclosures: int

    def summary(self) -> dict:
        persistence = [
            f["standpoint_persistence"]
            for f in self.frames
            if f["standpoint_persistence"] is not None
        ]
        distances = [
            f["multiplicity_unity_distance"]
            for f in self.frames
            if f["multiplicity_unity_distance"] is not None
        ]
        diversity = [
            f["representation_diversity"]
            for f in self.frames
            if f["representation_diversity"] is not None
        ]
        perspective_actions = sum(
            f["action_source"] == "perspective"
            for f in self.frames
        )
        interventions = sum(
            f["action_source"] == "perspective"
            and int(f["chosen_candidate_index"]) != 0
            for f in self.frames
        )
        return {
            "initial_seed": self.initial_seed,
            "perspective_enabled": self.perspective_enabled,
            "frames": len(self.frames),
            "core_steps": self.core_steps,
            "successful_reclosures": self.successful_reclosures,
            "perspective_closure_passes": self.perspective.closure_passes,
            "perspective_closure_failures": self.perspective.closure_failures,
            "representation_exports": self.perspective.exports,
            "fragmentation_failures": self.perspective.fragmentation_failures,
            "representational_collapse_failures": self.perspective.collapse_failures,
            "over_unification_failures": self.perspective.over_unification_failures,
            "recursive_instability_failures": self.perspective.instability_failures,
            "mean_standpoint_persistence": (
                float(np.mean(persistence)) if persistence else None
            ),
            "mean_multiplicity_unity_distance": (
                float(np.mean(distances)) if distances else None
            ),
            "mean_representation_diversity": (
                float(np.mean(diversity)) if diversity else None
            ),
            "perspective_action_decisions": int(perspective_actions),
            "perspective_action_interventions": int(interventions),
            "final_perspective_rho": (
                self.frames[-1]["perspective_rho"] if self.frames else None
            ),
            "final_here_norm": (
                float(np.linalg.norm(self.perspective.standpoint))
                if self.frames else 0.0
            ),
        }


def _safe01(x: float) -> float:
    return float(np.clip(x, 0.0, 1.0))


def _policy_projection(policy: dict[str, float]) -> np.ndarray:
    """
    Fixed declared projection from bounded plastic action coordinates into the
    common seven-dimensional self-representation carrier.
    """
    p = _policy_vector(policy)
    if len(p) < 5:
        p = np.pad(p, (0, 5-len(p)))
    # Map signed plastic deviations to [0,1]-like coordinates.
    q = 0.5 + 1.6*np.clip(p[:5], -0.28, 0.28)
    q = np.clip(q, 0.0, 1.0)
    return np.array([
        q[1],                         # neighbor geometry -> resource position proxy
        1.0-q[4],                     # low export cost -> stability
        0.5*(q[0]+q[2]),              # formation/resource blend -> maintenance
        q[0],                         # formation drive -> retention
        q[4],                         # export orientation
        0.5*(q[2]+q[3]),              # plastic agency
        0.5*(q[0]+q[3]),              # continuity of action organization
    ], dtype=float)


def build_self_representations(
    organism: np.ndarray,
    policy: dict[str, float],
    memory: MemoryState,
    retrieved,
    retrieval_similarity: float,
    predicted_next_organism: np.ndarray,
    world: np.ndarray,
) -> tuple[list[str], np.ndarray]:
    """
    Operational Level-29 multiplicity.

    Each row is a distinct current self-representation embedded into the same
    seven-dimensional standpoint carrier. They remain separately inspectable.
    """
    o = np.asarray(organism, dtype=float)
    pred = np.asarray(predicted_next_organism, dtype=float)
    world = np.asarray(world, dtype=float)

    body = np.clip(o, 0.0, 1.5)

    action = _policy_projection(policy)

    if retrieved is not None:
        memory_policy = _policy_projection(retrieved.policy)
        memory_rep = np.array([
            _safe01(retrieved.reward),
            _safe01(retrieved.strength/1.5),
            _safe01(0.55*retrieved.reward + 0.45*retrieval_similarity),
            _safe01(memory_policy[3]),
            _safe01(memory_policy[4]),
            _safe01(memory_policy[5]),
            _safe01(0.5 + 0.5*retrieval_similarity),
        ])
    else:
        memory_rep = np.array([
            o[0], 0.0, 0.5*o[2], o[3], o[4], 0.0,
            _safe01(len(memory.slots)/8.0),
        ], dtype=float)

    predictive = np.clip(pred, 0.0, 1.5)

    # World-relative self: the organism represented from its situated relation to
    # the current external carrier, not world state alone.
    world_relative = np.array([
        _safe01(0.5*o[0] + 0.5*world[0]),
        _safe01(0.5*(1.0-o[4]) + 0.5*(1.0-world[1])),
        _safe01(0.6*o[2] + 0.4*world[2]),
        _safe01(o[3]),
        _safe01(0.5*o[4] + 0.5*world[1]),
        _safe01(0.5*action[5] + 0.5*(1.0-world[1])),
        _safe01(0.5*o[6] + 0.5*world[2]),
    ], dtype=float)

    names = [
        "body_self",
        "memory_self",
        "action_self",
        "predictive_self",
        "world_relative_self",
    ]
    reps = np.vstack([body, memory_rep, action, predictive, world_relative])
    return names, reps


def representation_coherence(rep: np.ndarray) -> float:
    rep = np.asarray(rep, dtype=float)
    return float(np.linalg.norm(rep)/math.sqrt(max(len(rep), 1)))


def multiplicity_unity_distance(
    representations: np.ndarray,
    standpoint: np.ndarray,
) -> float:
    R = np.asarray(representations, dtype=float)
    z = np.asarray(standpoint, dtype=float)
    residuals = np.linalg.norm(R-z[None,:], axis=1)/math.sqrt(R.shape[1])
    return float(np.sqrt(np.mean(residuals**2)))


def _robust_neutral_center(
    representations: np.ndarray,
    previous: np.ndarray,
    params: PerspectiveParameters,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Neutral mediation is not arithmetic summation.

    Representation weights are determined endogenously by pairwise compatibility
    and continuity with the prior standpoint. The resulting center is then
    nonlinearly bounded.
    """
    R = np.asarray(representations, dtype=float)
    prev = np.asarray(previous, dtype=float)

    diffs = R[:,None,:]-R[None,:,:]
    pair = np.linalg.norm(diffs, axis=2)/math.sqrt(R.shape[1])
    compatibility = np.exp(
        -np.mean(pair, axis=1)/params.consensus_temperature
    )
    continuity = np.exp(
        -np.linalg.norm(R-prev[None,:],axis=1)
        /(math.sqrt(R.shape[1])*params.consensus_temperature)
    )
    weights = np.sqrt(np.maximum(compatibility*continuity, 1e-12))
    weights /= np.sum(weights)

    raw = np.sum(weights[:,None]*R, axis=0)
    mediator = np.tanh(
        raw + 0.20*(raw-prev)
    )
    # Re-map tanh output from roughly [-1,1] into the positive standpoint carrier.
    center = 0.5*(mediator+1.0)
    center = np.clip(center, 0.0, 1.5)

    residuals = np.linalg.norm(R-center[None,:],axis=1)/math.sqrt(R.shape[1])
    return center, weights, residuals


def perspective_step(
    state: PerspectiveState,
    names: list[str],
    representations: np.ndarray,
    params: PerspectiveParameters,
) -> tuple[PerspectiveState, dict, list[dict]]:
    params.validate()
    R = np.asarray(representations, dtype=float)
    events = []

    coherence = np.array([representation_coherence(r) for r in R])
    active_mask = coherence >= params.minimum_representation_norm
    active_names = [n for n,m in zip(names,active_mask) if m]
    active = R[active_mask]

    if len(active) < params.minimum_active_representations:
        state.collapse_failures += 1
        state.closure_failures += 1
        return state, {
            "closure": False,
            "failure": "representational_collapse",
            "active_representations": len(active),
            "distance": None,
            "standpoint_persistence": None,
            "rho": params.recurrent_alpha,
            "standpoint": state.standpoint.copy(),
            "weights": [],
            "residuals": [],
            "exported": [],
        }, events

    candidate, weights, residuals = _robust_neutral_center(
        active, state.standpoint, params
    )

    exported = []
    keep = residuals <= params.export_residual_threshold
    if np.sum(keep) >= params.minimum_active_representations and not np.all(keep):
        for n,r in zip(active_names,residuals):
            if r > params.export_residual_threshold:
                exported.append(n)
                events.append({
                    "event": "perspective_export",
                    "representation": n,
                    "residual": float(r),
                    "mode": "non_integrable_self_relation",
                })
        state.exports += len(exported)
        active = active[keep]
        active_names = [n for n,k in zip(active_names,keep) if k]
        candidate, weights, residuals = _robust_neutral_center(
            active, state.standpoint, params
        )

    prev = state.standpoint.copy()
    alpha = params.recurrent_alpha
    standpoint = alpha*prev + (1.0-alpha)*candidate
    standpoint = np.clip(standpoint, 0.0, 1.5)

    distance = multiplicity_unity_distance(active, standpoint)
    diversity = float(
        np.mean(np.std(active,axis=0))
    )
    persistence = float(
        np.exp(-np.linalg.norm(standpoint-prev)/math.sqrt(len(standpoint)))
    )

    fragmentation = distance >= params.max_multiplicity_unity
    over_unification = distance <= params.epsilon_multiplicity_unity
    collapse = len(active) < params.minimum_active_representations
    rho = alpha
    instability = rho > params.recursive_rho_max
    coherent = float(np.linalg.norm(standpoint)) > 0
    persistent = persistence >= params.minimum_standpoint_persistence

    closure = bool(
        not fragmentation
        and not over_unification
        and not collapse
        and not instability
        and coherent
        and persistent
    )

    if fragmentation:
        state.fragmentation_failures += 1
    if over_unification:
        state.over_unification_failures += 1
    if collapse:
        state.collapse_failures += 1
    if instability:
        state.instability_failures += 1

    if closure:
        state.closure_passes += 1
    else:
        state.closure_failures += 1

    state.previous_standpoint = prev
    state.standpoint = standpoint
    state.age += 1

    return state, {
        "closure": closure,
        "failure": (
            "fragmentation" if fragmentation else
            "over_unification" if over_unification else
            "representational_collapse" if collapse else
            "recursive_instability" if instability else
            None
        ),
        "active_representations": len(active),
        "distance": distance,
        "diversity": diversity,
        "standpoint_persistence": persistence,
        "rho": rho,
        "standpoint": standpoint.copy(),
        "weights": weights.tolist(),
        "residuals": residuals.tolist(),
        "exported": exported,
    }, events


def standpoint_alignment(
    predicted_next_organism: np.ndarray,
    standpoint: np.ndarray,
) -> float:
    pred = np.clip(np.asarray(predicted_next_organism,dtype=float),0.0,1.5)
    z = np.asarray(standpoint,dtype=float)
    d = np.linalg.norm(pred-z)/math.sqrt(len(z))
    return float(np.exp(-d/0.32))


def simulate_perspective(
    seed: int = 1341550191,
    generations: int = 96,
    program: EnvironmentProgram | None = None,
    base_org: SelfOrganizationParameters | None = None,
    base_pop: PopulationParameters | None = None,
    evo: EvolutionParameters | None = None,
    learn: LearningParameters | None = None,
    self_params: SelfModelParameters | None = None,
    perspective_params: PerspectiveParameters | None = None,
    perspective_enabled: bool = True,
    numerical_policy: NumericalPolicy | None = None,
) -> PerspectiveRun:
    base_org = base_org or SelfOrganizationParameters(node_count=24,persistent_rank=6)
    base_pop = base_pop or PopulationParameters(
        min_unit_nodes=4,max_unit_nodes=42,max_population=8,
        node_birth_threshold=1.05,max_node_births_per_step=0,
    )
    evo = evo or EvolutionParameters(
        mutation_rate=0.0,mutation_sigma=0.0,
        carrying_capacity=1,max_candidate_population=1,
        minimum_reproductive_age=10_000,
    )
    learn = learn or LearningParameters(
        exploration_sigma=0.03,retrieval_blend=0.92,
        max_memory_slots=8,witness_min_gap=4,
    )
    self_params = self_params or SelfModelParameters()
    perspective_params = perspective_params or PerspectiveParameters()
    numerical_policy = numerical_policy or NumericalPolicy()
    perspective_params.validate()

    if program is None:
        a=EnvironmentState(
            name="perspective_A",resource_supply=0.93,disturbance=0.03,
            carrying_capacity=8,match_weight=0.50,
            preferred_traits={
                "formation_drive":1.30,"neighbor_scale":0.39,
                "resource_blend":0.22,"topology_blend":0.14,
                "export_cost":0.12,
            },
        )
        b=EnvironmentState(
            name="perspective_B",resource_supply=0.65,disturbance=0.10,
            carrying_capacity=6,match_weight=0.50,
            preferred_traits={
                "formation_drive":1.52,"neighbor_scale":0.30,
                "resource_blend":0.35,"topology_blend":0.24,
                "export_cost":0.075,
            },
        )
        c=EnvironmentState(
            name="perspective_C",resource_supply=0.48,disturbance=0.18,
            carrying_capacity=5,match_weight=0.50,
            preferred_traits={
                "formation_drive":1.68,"neighbor_scale":0.23,
                "resource_blend":0.45,"topology_blend":0.32,
                "export_cost":0.045,
            },
        )
        program=EnvironmentProgram(phases=(
            (0,a),(8,b),(16,c),(24,a),(32,b),(40,c),
            (48,a),(56,b),(64,c),(72,a),(80,b),(88,c)
        ))

    rng=np.random.default_rng(seed+71933)
    from .alife import make_self_organizing_seed
    state=make_self_organizing_seed(seed=seed,params=base_org)
    genotype=default_traits(base_org,base_pop)
    policy_state=zero_policy()
    memory=MemoryState()
    slot_counter=0
    self_model=make_self_model(self_params)

    initial_org=traits_to_org(base_org,genotype,state.dim)
    initial_o=organism_readout(state,policy_state,memory,initial_org)
    perspective=PerspectiveState(standpoint=np.clip(initial_o,0.0,1.5))

    events=[]
    frames=[]
    core_steps=successful=0

    for generation in range(int(generations)+1):
        env=program.at(generation)
        world=world_readout(env)
        update_world_model(self_model,env.name,world)
        predicted_world=predict_world(self_model,env.name,world)

        traits=effective_traits(genotype,policy_state,learn)
        org=traits_to_org(base_org,traits,state.dim)
        organism=organism_readout(state,policy_state,memory,org)

        retrieved,similarity=retrieve_memory(
            memory,environment_cue(env),generation,learn
        )
        if retrieved is not None:
            recalled,_=_bounded_policy_move(
                policy_state,retrieved.policy,
                learn.max_policy_step,learn.max_policy_offset
            )
        else:
            recalled=dict(policy_state)

        x_current=self_predictor_input(
            world,predicted_world,organism,recalled
        )
        if self_model.predictor.observations >= self_params.min_observations:
            predicted_self=contextual_self_prediction(
                self_model,env.name,x_current,organism
            )[:7]
        else:
            predicted_self=organism.copy()

        rep_names,reps=build_self_representations(
            organism,recalled,memory,retrieved,similarity,
            predicted_self,world
        )

        if perspective_enabled:
            perspective,pdiag,pevents=perspective_step(
                perspective,rep_names,reps,perspective_params
            )
            for e in pevents:
                events.append({"generation":generation,**e})
        else:
            # Ablation keeps a passive previous standpoint but cannot close it.
            pdiag={
                "closure":False,"failure":"perspective_ablated",
                "active_representations":len(reps),
                "distance":multiplicity_unity_distance(
                    reps,perspective.standpoint
                ),
                "diversity":float(np.mean(np.std(reps,axis=0))),
                "standpoint_persistence":1.0,
                "rho":perspective_params.recurrent_alpha,
                "standpoint":perspective.standpoint.copy(),
                "weights":[],"residuals":[],"exported":[],
            }

        candidates=_candidate_policies(
            recalled,rng,learn,self_params
        )
        model_ready=self_model.predictor.observations >= self_params.min_observations

        scores=[]
        predicted_vectors=[]
        if model_ready:
            for cand in candidates:
                x=self_predictor_input(
                    world,predicted_world,organism,cand
                )
                pred=contextual_self_prediction(
                    self_model,env.name,x,organism
                )
                predicted_vectors.append(pred)
                base_score=_predicted_candidate_score(
                    pred,organism,self_params
                )
                if perspective_enabled and pdiag["closure"]:
                    align=standpoint_alignment(
                        pred[:7],perspective.standpoint
                    )
                    score=(
                        (1.0-perspective_params.standpoint_action_weight)*base_score
                        + perspective_params.standpoint_action_weight*align
                    )
                else:
                    score=base_score
                scores.append(score)
            chosen_index=int(np.argmax(scores))
            chosen_policy=candidates[chosen_index]
            action_source=(
                "perspective" if perspective_enabled and pdiag["closure"]
                else "self_model"
            )
        else:
            chosen_index=1 if (len(candidates)>1 and generation%3==0) else 0
            chosen_policy=candidates[chosen_index]
            action_source="model_free"

        forcing_seed=int(seed+211019*generation+13007)
        chosen=_evaluate_policy_once(
            state,genotype,chosen_policy,env,
            base_org,evo,learn,numerical_policy,
            forcing_seed,generation
        )
        if not chosen["success"]:
            events.append({
                "event":"perspective_terminal",
                "generation":generation,
                "reason":chosen["step"].terminal_reason or "formation_failure",
            })
            break

        core_steps+=1
        successful+=1
        evolved=chosen["state"]
        reward=chosen["reward"]
        next_org=organism_readout(
            evolved,chosen_policy,memory,chosen["org"]
        )

        x_chosen=self_predictor_input(
            world,predicted_world,organism,chosen_policy
        )
        update_contextual_self_transition(
            self_model,env.name,organism,next_org,reward
        )
        self_model.predictor.update(
            x_chosen,np.concatenate([next_org,[reward]])
        )

        # Action closes back into later self state.
        if chosen_index!=0 and action_source=="perspective":
            events.append({
                "event":"perspective_action",
                "generation":generation,
                "chosen_index":chosen_index,
                "score":scores[chosen_index] if scores else None,
            })

        policy_state,policy_change=_bounded_policy_move(
            policy_state,chosen_policy,
            learn.max_policy_step,learn.max_policy_offset
        )
        mem_events,slot_counter=update_memory(
            memory,environment_cue(env),chosen_policy,reward,
            generation,learn,slot_counter
        )
        events.extend({"generation":generation,**e} for e in mem_events)

        self_oo,self_po,self_reachable=self_reference_metrics(
            self_model,self_params
        )

        frame = {
            "generation":generation,
            "environment":env.name,
            "reward":float(reward),
            "maintenance":float(chosen["maintenance"]),
            "environment_match":float(chosen["match"]),
            "active_self_representations":pdiag["active_representations"],
            "multiplicity_unity_distance":pdiag["distance"],
            "representation_diversity":pdiag.get("diversity"),
            "standpoint_persistence":pdiag["standpoint_persistence"],
            "perspective_rho":pdiag["rho"],
            "perspective_closure":bool(pdiag["closure"]),
            "perspective_failure":pdiag["failure"],
            "perspective_exports_this_step":len(pdiag["exported"]),
            "perspective_exports_total":perspective.exports,
            "here_norm":float(np.linalg.norm(perspective.standpoint)),
            "action_source":action_source,
            "chosen_candidate_index":chosen_index,
            "policy_change_norm":float(policy_change),
            "self_reference_reachable":bool(self_reachable),
            "self_recurrent_coupling":float(self_oo),
            "policy_to_self_coupling":float(self_po),
        }
        for i, value in enumerate(perspective.standpoint):
            frame[f"standpoint_{i}"] = float(value)
        frames.append(frame)

        state=evolved

    return PerspectiveRun(
        initial_seed=seed,
        frames=frames,
        events=events,
        final_state=state,
        final_policy=policy_state,
        memory=memory,
        perspective=perspective,
        perspective_enabled=perspective_enabled,
        core_steps=core_steps,
        successful_reclosures=successful,
    )


def compare_perspective(
    seed: int = 1341550191,
    generations: int = 96,
    **kwargs,
) -> dict:
    enabled=simulate_perspective(
        seed=seed,generations=generations,
        perspective_enabled=True,**kwargs
    )
    disabled=simulate_perspective(
        seed=seed,generations=generations,
        perspective_enabled=False,**kwargs
    )
    n=min(len(enabled.frames),len(disabled.frames))
    reward_gain=np.array([
        enabled.frames[i]["reward"]-disabled.frames[i]["reward"]
        for i in range(n)
    ],dtype=float)

    closure_fraction=(
        float(np.mean([f["perspective_closure"] for f in enabled.frames]))
        if enabled.frames else 0.0
    )
    enabled_distance=np.array([
        f["multiplicity_unity_distance"]
        for f in enabled.frames
        if f["multiplicity_unity_distance"] is not None
    ],dtype=float)
    disabled_distance=np.array([
        f["multiplicity_unity_distance"]
        for f in disabled.frames
        if f["multiplicity_unity_distance"] is not None
    ],dtype=float)
    enabled_diversity=np.array([
        f["representation_diversity"]
        for f in enabled.frames
        if f["representation_diversity"] is not None
    ],dtype=float)
    disabled_diversity=np.array([
        f["representation_diversity"]
        for f in disabled.frames
        if f["representation_diversity"] is not None
    ],dtype=float)
    mean_enabled_distance=float(np.mean(enabled_distance)) if enabled_distance.size else None
    mean_disabled_distance=float(np.mean(disabled_distance)) if disabled_distance.size else None
    mean_enabled_diversity=float(np.mean(enabled_diversity)) if enabled_diversity.size else None
    mean_disabled_diversity=float(np.mean(disabled_diversity)) if disabled_diversity.size else None
    return {
        "perspective":enabled,
        "ablated_control":disabled,
        "summary":{
            "compared_steps":n,
            "mean_reward_gain":float(np.mean(reward_gain)) if n else 0.0,
            "perspective_closure_fraction":closure_fraction,
            "perspective_exports":enabled.perspective.exports,
            "mean_standpoint_persistence":enabled.summary()[
                "mean_standpoint_persistence"
            ],
            "mean_multiplicity_unity_distance":mean_enabled_distance,
            "ablated_mean_multiplicity_unity_distance":mean_disabled_distance,
            "standpoint_distance_reduction":(
                mean_disabled_distance-mean_enabled_distance
                if mean_enabled_distance is not None and mean_disabled_distance is not None
                else None
            ),
            "mean_representation_diversity":mean_enabled_diversity,
            "ablated_mean_representation_diversity":mean_disabled_diversity,
            "diversity_retention_ratio":(
                mean_enabled_diversity/mean_disabled_diversity
                if mean_enabled_diversity is not None
                and mean_disabled_diversity not in (None,0.0)
                else None
            ),
            "perspective_action_decisions":enabled.summary()[
                "perspective_action_decisions"
            ],
            "perspective_action_interventions":enabled.summary()[
                "perspective_action_interventions"
            ],
            "final_here_norm":enabled.summary()["final_here_norm"],
        },
    }


def write_perspective_report(
    run: PerspectiveRun,
    outdir: str | Path,
    stem: str = "perspective",
) -> dict[str,str]:
    outdir=Path(outdir)
    outdir.mkdir(parents=True,exist_ok=True)

    csv_path=outdir/f"{stem}_frames.csv"
    if run.frames:
        fields=list(run.frames[0].keys())
        with csv_path.open("w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(f,fieldnames=fields)
            w.writeheader(); w.writerows(run.frames)

    events_path=outdir/f"{stem}_events.json"
    events_path.write_text(json.dumps(run.events,indent=2),encoding="utf-8")
    summary_path=outdir/f"{stem}_summary.json"
    summary_path.write_text(json.dumps(run.summary(),indent=2),encoding="utf-8")

    standpoint_path=outdir/f"{stem}_standpoint.csv"
    np.savetxt(
        standpoint_path,
        run.perspective.standpoint[None,:],
        delimiter=",",
        header=",".join(PERSPECTIVE_FEATURE_NAMES),
        comments="",
    )

    plot_path=outdir/f"{stem}_closure.png"
    if run.frames:
        g=np.array([f["generation"] for f in run.frames])
        d=np.array([
            np.nan if f["multiplicity_unity_distance"] is None
            else f["multiplicity_unity_distance"]
            for f in run.frames
        ])
        persistence=np.array([
            np.nan if f["standpoint_persistence"] is None
            else f["standpoint_persistence"]
            for f in run.frames
        ])
        reward=np.array([f["reward"] for f in run.frames])

        fig,ax1=plt.subplots(figsize=(8.4,4.9))
        ax1.plot(g,d,label="multiplicity/unity distance")
        ax1.plot(g,persistence,label="standpoint persistence")
        ax1.set_xlabel("Generation")
        ax1.set_ylabel("Perspective geometry")
        ax2=ax1.twinx()
        ax2.plot(g,reward,linestyle="--",label="reward")
        ax2.set_ylabel("Outcome")
        lines=ax1.get_lines()+ax2.get_lines()
        ax1.legend(lines,[ln.get_label() for ln in lines],loc="best",fontsize=8)
        ax1.set_title("BFG perspective closure")
        fig.tight_layout()
        fig.savefig(plot_path,dpi=165)
        plt.close(fig)
    else:
        plot_path=Path("")

    return {
        "frames_csv":str(csv_path),
        "events_json":str(events_path),
        "summary_json":str(summary_path),
        "standpoint_csv":str(standpoint_path),
        "closure_plot":str(plot_path),
    }


def write_perspective_comparison(
    comparison: dict,
    outdir: str | Path,
    stem: str = "perspective_comparison",
) -> dict[str,str]:
    outdir=Path(outdir)
    outdir.mkdir(parents=True,exist_ok=True)
    a=comparison["perspective"]
    b=comparison["ablated_control"]
    n=min(len(a.frames),len(b.frames))
    rows=[]
    for i in range(n):
        rows.append({
            "generation":a.frames[i]["generation"],
            "environment":a.frames[i]["environment"],
            "reward_perspective":a.frames[i]["reward"],
            "reward_control":b.frames[i]["reward"],
            "reward_gain":a.frames[i]["reward"]-b.frames[i]["reward"],
            "perspective_closure":a.frames[i]["perspective_closure"],
            "multiplicity_unity_distance":a.frames[i]["multiplicity_unity_distance"],
            "standpoint_persistence":a.frames[i]["standpoint_persistence"],
            "action_source":a.frames[i]["action_source"],
        })
    csv_path=outdir/f"{stem}.csv"
    if rows:
        with csv_path.open("w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0].keys()))
            w.writeheader(); w.writerows(rows)
    summary_path=outdir/f"{stem}_summary.json"
    summary_path.write_text(
        json.dumps(comparison["summary"],indent=2),encoding="utf-8"
    )
    return {
        "comparison_csv":str(csv_path),
        "comparison_summary":str(summary_path),
    }
