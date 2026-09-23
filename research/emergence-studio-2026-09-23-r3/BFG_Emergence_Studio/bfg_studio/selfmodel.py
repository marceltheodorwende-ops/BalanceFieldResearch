from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
import csv
import json
import math
import numpy as np
import matplotlib.pyplot as plt

from .types import BFGState, NumericalPolicy
from .core import canonical_reclosure, neutral_pair, graph_metric
from .alife import (
    SelfOrganizationParameters,
    SelfOrganizingNetworkCarrier,
    make_self_organizing_seed,
    organization_metrics,
)
from .population import PopulationParameters
from .evolution import (
    EvolutionParameters,
    EvolutionUnit,
    default_traits,
    traits_to_org,
)
from .environment import (
    EnvironmentState,
    EnvironmentProgram,
    apply_environment,
    environmental_fitness,
)
from .learning import (
    LearningParameters,
    MemoryState,
    LearningUnit,
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


SELF_FEATURE_NAMES = (
    "mean_resource",
    "resource_dispersion",
    "maintenance",
    "retained_fraction",
    "export_fraction",
    "policy_norm",
    "memory_load",
)


@dataclass(frozen=True)
class SelfModelParameters:
    ridge: float = 0.001
    min_observations: int = 12
    recurrent_rho_max: float = 1.04
    prediction_clip: float = 1.5
    candidate_count: int = 5
    candidate_sigma: float = 0.035
    prediction_weight: float = 0.60
    model_action_blend: float = 0.80
    world_self_epsilon: float = 0.055
    world_self_limit: float = 1.55
    self_reference_min_coupling: float = 0.015
    mediator_min_coupling: float = 0.010
    world_coherence_min: float = 0.050
    organism_coherence_min: float = 0.050

    def validate(self):
        if self.ridge <= 0:
            raise ValueError("ridge must be positive")
        if self.min_observations < 2:
            raise ValueError("min_observations must be >= 2")
        if not (0.90 <= self.recurrent_rho_max <= 1.25):
            raise ValueError("recurrent_rho_max outside intended bounded-critical range")
        if self.candidate_count < 2:
            raise ValueError("candidate_count must be >= 2")
        if self.candidate_sigma < 0:
            raise ValueError("candidate_sigma must be nonnegative")
        if not (0 <= self.prediction_weight <= 1):
            raise ValueError("prediction_weight must lie in [0,1]")
        if not (0 <= self.model_action_blend <= 1):
            raise ValueError("model_action_blend must lie in [0,1]")


@dataclass
class OnlineSelfPredictor:
    input_dim: int
    output_dim: int
    ridge: float
    recurrent_input_slice: tuple[int, int]
    recurrent_output_slice: tuple[int, int]
    rho_max: float
    xtx: np.ndarray = field(init=False)
    xty: np.ndarray = field(init=False)
    weights: np.ndarray = field(init=False)
    observations: int = 0

    def __post_init__(self):
        self.xtx = self.ridge*np.eye(self.input_dim, dtype=float)
        self.xty = np.zeros((self.input_dim, self.output_dim), dtype=float)
        self.weights = np.zeros((self.input_dim, self.output_dim), dtype=float)

    def update(self, x: np.ndarray, y: np.ndarray):
        x = np.asarray(x, dtype=float)
        y = np.asarray(y, dtype=float)
        self.xtx += np.outer(x, x)
        self.xty += np.outer(x, y)
        self.observations += 1
        self.weights = np.linalg.solve(self.xtx, self.xty)
        self._clip_recurrent_block()

    def _clip_recurrent_block(self):
        i0, i1 = self.recurrent_input_slice
        o0, o1 = self.recurrent_output_slice
        block = self.weights[i0:i1, o0:o1].T
        if block.shape[0] != block.shape[1] or block.size == 0:
            return
        eig = np.linalg.eigvals(block)
        rho = float(np.max(np.abs(eig))) if eig.size else 0.0
        if rho > self.rho_max:
            self.weights[i0:i1, o0:o1] *= self.rho_max/max(rho, 1e-12)

    def predict(self, x: np.ndarray) -> np.ndarray:
        return np.asarray(x, dtype=float) @ self.weights

    def recurrent_rho(self) -> float:
        i0, i1 = self.recurrent_input_slice
        o0, o1 = self.recurrent_output_slice
        block = self.weights[i0:i1, o0:o1].T
        if block.shape[0] != block.shape[1] or block.size == 0:
            return 0.0
        eig = np.linalg.eigvals(block)
        return float(np.max(np.abs(eig))) if eig.size else 0.0

    def organism_recurrent_coupling(self) -> float:
        i0, i1 = self.recurrent_input_slice
        o0, o1 = self.recurrent_output_slice
        return float(np.linalg.norm(self.weights[i0:i1, o0:o1], ord="fro"))


@dataclass
class SelfModelState:
    predictor: OnlineSelfPredictor
    world_transition_sum: dict[str, np.ndarray] = field(default_factory=dict)
    world_transition_count: dict[str, int] = field(default_factory=dict)
    organism_delta_sum: dict[str, np.ndarray] = field(default_factory=dict)
    organism_delta_count: dict[str, int] = field(default_factory=dict)
    reward_sum: dict[str, float] = field(default_factory=dict)
    reward_count: dict[str, int] = field(default_factory=dict)
    last_world_name: str | None = None
    last_world_cue: np.ndarray | None = None
    prediction_errors: list[float] = field(default_factory=list)
    baseline_errors: list[float] = field(default_factory=list)
    self_readout_errors: list[float] = field(default_factory=list)
    action_interventions: int = 0
    closure_passes: int = 0
    closure_failures: int = 0
    excess_exports: int = 0


@dataclass
class SelfModelRun:
    initial_seed: int
    frames: list[dict]
    events: list[dict]
    final_state: BFGState
    final_policy: dict[str, float]
    memory: MemoryState
    self_model: SelfModelState
    self_model_enabled: bool
    core_steps: int
    successful_reclosures: int

    def summary(self) -> dict:
        prospective = [
            f["prediction_error"]
            for f in self.frames
            if f["prediction_error"] is not None
        ]
        baseline = [
            f["persistence_baseline_error"]
            for f in self.frames
            if f["persistence_baseline_error"] is not None
        ]
        actions = sum(bool(f["self_model_action_used"]) for f in self.frames)
        interventions = sum(
            bool(f["self_model_action_intervention"]) for f in self.frames
        )
        closure = sum(bool(f["self_model_closure"]) for f in self.frames)
        corridor_fraction = (
            float(np.mean([f["world_self_corridor"] for f in self.frames]))
            if self.frames else 0.0
        )
        reachable_fraction = (
            float(np.mean([f["self_reference_reachable"] for f in self.frames]))
            if self.frames else 0.0
        )
        return {
            "initial_seed": self.initial_seed,
            "self_model_enabled": self.self_model_enabled,
            "frames": len(self.frames),
            "core_steps": self.core_steps,
            "successful_reclosures": self.successful_reclosures,
            "predictor_observations": self.self_model.predictor.observations,
            "mean_self_prediction_error": (
                float(np.mean(prospective)) if prospective else None
            ),
            "mean_persistence_baseline_error": (
                float(np.mean(baseline)) if baseline else None
            ),
            "self_model_action_decisions": actions,
            "self_model_action_interventions": interventions,
            "self_model_closure_passes": closure,
            "world_self_corridor_pass_fraction": corridor_fraction,
            "self_reference_reachable_fraction": reachable_fraction,
            "self_model_closure_failures": self.self_model.closure_failures,
            "self_model_excess_exports": self.self_model.excess_exports,
            "final_recurrent_rho": self.self_model.predictor.recurrent_rho(),
        }


def organism_readout(
    state: BFGState,
    policy: dict[str, float],
    memory: MemoryState,
    org: SelfOrganizationParameters,
) -> np.ndarray:
    metrics = organization_metrics(state, org)
    resource = np.asarray(state.metadata["resource"], dtype=float)
    C, B = neutral_pair(np.asarray(state.Y, dtype=complex))
    D = np.asarray(state.D, dtype=complex)
    denom = max(float(np.real(np.vdot(D, D))), 1e-12)
    retained = float(np.real(np.vdot(D, C @ D))/denom)
    exported = float(np.real(np.vdot(D, B @ D))/denom)
    policy_norm = float(np.linalg.norm(_policy_vector(policy)))
    memory_load = float(len(memory.slots)/8.0)
    return np.array([
        float(np.mean(resource)),
        float(np.std(resource)),
        float(metrics["maintenance_score"]),
        np.clip(retained, 0.0, 1.5),
        np.clip(exported, 0.0, 1.5),
        np.clip(policy_norm, 0.0, 1.5),
        np.clip(memory_load, 0.0, 1.5),
    ], dtype=float)


def world_readout(env: EnvironmentState) -> np.ndarray:
    return environment_cue(env)


def self_world_distance(world: np.ndarray, organism: np.ndarray) -> float:
    # Compare a fixed world embedding with a fixed organism embedding.
    # Separate coordinates are retained; only the distance readout is shared.
    w = np.asarray(world, dtype=float)
    o = np.array([
        organism[0],              # resource-related self condition
        1.0-organism[4],          # retained-vs-export orientation
        organism[2],              # maintenance
    ], dtype=float)
    return float(np.linalg.norm(w-o))


def self_closure_readout(world: np.ndarray, organism: np.ndarray) -> np.ndarray:
    """
    Carrier realization of Self = Cl_NSelf(W, Os).

    W and Os remain explicit disjoint coordinate blocks. The mediator block is a
    bounded cross-relation, not an overwrite of either pole.
    """
    w = np.asarray(world, dtype=float)
    o = np.asarray(organism, dtype=float)
    o3 = np.array([o[0], 1.0-o[4], o[2]], dtype=float)
    mediator = np.tanh(w*o3 + 0.5*(w-o3))
    return np.concatenate([w, o, mediator])


def update_world_model(
    model: SelfModelState,
    current_name: str,
    current_cue: np.ndarray,
):
    if model.last_world_name is not None and model.last_world_cue is not None:
        key = model.last_world_name
        model.world_transition_sum[key] = (
            model.world_transition_sum.get(key, np.zeros_like(current_cue))
            + current_cue
        )
        model.world_transition_count[key] = (
            model.world_transition_count.get(key, 0) + 1
        )
    model.last_world_name = current_name
    model.last_world_cue = np.asarray(current_cue, dtype=float).copy()


def predict_world(model: SelfModelState, current_name: str, current_cue: np.ndarray) -> np.ndarray:
    count = model.world_transition_count.get(current_name, 0)
    if count <= 0:
        return np.asarray(current_cue, dtype=float).copy()
    return model.world_transition_sum[current_name]/count


def self_predictor_input(
    world: np.ndarray,
    predicted_world: np.ndarray,
    organism: np.ndarray,
    policy: dict[str, float],
) -> np.ndarray:
    return np.concatenate([
        np.asarray(world, dtype=float),
        np.asarray(predicted_world, dtype=float),
        np.asarray(organism, dtype=float),
        _policy_vector(policy),
        np.ones(1, dtype=float),
    ])


def predictor_layout():
    # [world(3), predicted_world(3), organism(7), policy(5), bias(1)]
    world = (0, 3)
    predicted_world = (3, 6)
    organism = (6, 13)
    policy = (13, 18)
    bias = (18, 19)
    # output [next_organism(7), reward(1)]
    next_organism = (0, 7)
    reward = (7, 8)
    return {
        "world": world,
        "predicted_world": predicted_world,
        "organism": organism,
        "policy": policy,
        "bias": bias,
        "next_organism": next_organism,
        "reward": reward,
    }


def make_self_model(params: SelfModelParameters) -> SelfModelState:
    layout = predictor_layout()
    pred = OnlineSelfPredictor(
        input_dim=19,
        output_dim=8,
        ridge=params.ridge,
        recurrent_input_slice=layout["organism"],
        recurrent_output_slice=layout["next_organism"],
        rho_max=params.recurrent_rho_max,
    )
    return SelfModelState(predictor=pred)


def self_reference_metrics(
    model: SelfModelState,
    params: SelfModelParameters,
) -> tuple[float, float, bool]:
    layout = predictor_layout()
    W = model.predictor.weights
    oo = model.predictor.organism_recurrent_coupling()
    p0, p1 = layout["policy"]
    o0, o1 = layout["next_organism"]
    policy_to_self = float(np.linalg.norm(W[p0:p1, o0:o1], ord="fro"))
    reachable = (
        model.predictor.observations >= params.min_observations
        and oo >= params.self_reference_min_coupling
        and policy_to_self >= params.mediator_min_coupling
        and model.action_interventions > 0
    )
    return oo, policy_to_self, bool(reachable)


def contextual_self_prediction(
    model: SelfModelState,
    env_name: str,
    x: np.ndarray,
    organism: np.ndarray,
) -> np.ndarray:
    """
    Blend the general linear self-predictor with an environment-indexed recursive
    transition witness. The contextual term predicts the organism's own change
    when the same world regime recurs; the linear term retains action dependence.
    """
    linear = model.predictor.predict(x)
    count = model.organism_delta_count.get(env_name, 0)
    if count <= 0:
        return linear

    mean_delta = model.organism_delta_sum[env_name] / count
    context_next = np.asarray(organism, dtype=float) + mean_delta
    reward_count = model.reward_count.get(env_name, 0)
    context_reward = (
        model.reward_sum.get(env_name, 0.0)/reward_count
        if reward_count > 0 else float(linear[7])
    )

    # As repeated context evidence accumulates, trust contextual self-transition
    # more strongly while retaining enough linear contribution for action effects.
    context_weight = min(0.82, 0.38 + 0.08*count)
    out = np.empty_like(linear)
    out[:7] = (
        context_weight*context_next
        + (1.0-context_weight)*linear[:7]
    )
    out[7] = (
        0.55*context_reward
        + 0.45*linear[7]
    )
    return out


def update_contextual_self_transition(
    model: SelfModelState,
    env_name: str,
    organism: np.ndarray,
    next_organism: np.ndarray,
    reward: float,
):
    delta = np.asarray(next_organism, dtype=float) - np.asarray(organism, dtype=float)
    model.organism_delta_sum[env_name] = (
        model.organism_delta_sum.get(env_name, np.zeros_like(delta)) + delta
    )
    model.organism_delta_count[env_name] = (
        model.organism_delta_count.get(env_name, 0) + 1
    )
    model.reward_sum[env_name] = model.reward_sum.get(env_name, 0.0) + float(reward)
    model.reward_count[env_name] = model.reward_count.get(env_name, 0) + 1


def _candidate_policies(
    current: dict[str, float],
    rng: np.random.Generator,
    learn: LearningParameters,
    params: SelfModelParameters,
) -> list[dict[str, float]]:
    out = [dict(current)]
    for _ in range(params.candidate_count-1):
        v = dict(current)
        eps = rng.normal(0.0, params.candidate_sigma, size=len(PLASTIC_TRAITS))
        for i, key in enumerate(PLASTIC_TRAITS):
            v[key] = float(np.clip(
                v[key] + eps[i],
                -learn.max_policy_offset,
                learn.max_policy_offset,
            ))
        v, _ = _bounded_policy_move(
            current, v, learn.max_policy_step, learn.max_policy_offset
        )
        out.append(v)
    return out


def _predicted_candidate_score(
    predicted: np.ndarray,
    current_org: np.ndarray,
    params: SelfModelParameters,
) -> float:
    next_org = np.clip(predicted[:7], -params.prediction_clip, params.prediction_clip)
    pred_reward = float(np.clip(predicted[7], -0.5, 1.5))
    predicted_maintenance = float(np.clip(next_org[2], 0.0, 1.0))
    predicted_retention = float(np.clip(next_org[3], 0.0, 1.0))
    predicted_export = float(np.clip(next_org[4], 0.0, 1.0))
    stability = 1.0 - min(1.0, abs(predicted_export-current_org[4]))
    structural = (
        0.48*pred_reward
        + 0.28*predicted_maintenance
        + 0.14*predicted_retention
        + 0.10*stability
    )
    return float(structural)


def simulate_self_model(
    seed: int = 1341550191,
    generations: int = 80,
    program: EnvironmentProgram | None = None,
    base_org: SelfOrganizationParameters | None = None,
    base_pop: PopulationParameters | None = None,
    evo: EvolutionParameters | None = None,
    learn: LearningParameters | None = None,
    self_params: SelfModelParameters | None = None,
    self_model_enabled: bool = True,
    numerical_policy: NumericalPolicy | None = None,
) -> SelfModelRun:
    base_org = base_org or SelfOrganizationParameters(node_count=24, persistent_rank=6)
    base_pop = base_pop or PopulationParameters(
        min_unit_nodes=4,
        max_unit_nodes=42,
        max_population=8,
        node_birth_threshold=1.05,
        max_node_births_per_step=0,
    )
    evo = evo or EvolutionParameters(
        mutation_rate=0.0,
        mutation_sigma=0.0,
        carrying_capacity=1,
        max_candidate_population=1,
        minimum_reproductive_age=10_000,
    )
    learn = learn or LearningParameters(
        exploration_sigma=0.03,
        retrieval_blend=0.92,
        max_memory_slots=8,
        witness_min_gap=4,
    )
    self_params = self_params or SelfModelParameters()
    numerical_policy = numerical_policy or NumericalPolicy()
    self_params.validate()

    if program is None:
        # Three contexts force the model to represent world dynamics separately
        # from its own internal condition.
        a = EnvironmentState(
            name="self_world_A",
            resource_supply=0.94,
            disturbance=0.025,
            carrying_capacity=8,
            match_weight=0.52,
            preferred_traits={
                "formation_drive": 1.28,
                "neighbor_scale": 0.39,
                "resource_blend": 0.21,
                "topology_blend": 0.14,
                "export_cost": 0.12,
            },
        )
        b = EnvironmentState(
            name="self_world_B",
            resource_supply=0.62,
            disturbance=0.11,
            carrying_capacity=6,
            match_weight=0.52,
            preferred_traits={
                "formation_drive": 1.54,
                "neighbor_scale": 0.29,
                "resource_blend": 0.36,
                "topology_blend": 0.25,
                "export_cost": 0.075,
            },
        )
        c = EnvironmentState(
            name="self_world_C",
            resource_supply=0.47,
            disturbance=0.19,
            carrying_capacity=5,
            match_weight=0.52,
            preferred_traits={
                "formation_drive": 1.70,
                "neighbor_scale": 0.23,
                "resource_blend": 0.46,
                "topology_blend": 0.33,
                "export_cost": 0.045,
            },
        )
        program = EnvironmentProgram(phases=(
            (0, a), (8, b), (16, c), (24, a), (32, b),
            (40, c), (48, a), (56, b), (64, c), (72, a)
        ))

    rng = np.random.default_rng(seed + 58217)
    state = make_self_organizing_seed(seed=seed, params=base_org)
    genotype = default_traits(base_org, base_pop)
    policy_state = zero_policy()
    memory = MemoryState()
    slot_counter = 0
    model = make_self_model(self_params)
    events = []
    frames = []
    core_steps = successful = 0
    previous_learning_sample = None

    for generation in range(int(generations)+1):
        env = program.at(generation)
        world = world_readout(env)
        update_world_model(model, env.name, world)
        predicted_world = predict_world(model, env.name, world)

        current_traits = effective_traits(genotype, policy_state, learn)
        current_org = traits_to_org(base_org, current_traits, state.dim)
        organism = organism_readout(state, policy_state, memory, current_org)
        closure = self_closure_readout(world, organism)
        distance = self_world_distance(world, organism)

        # Memory supplies contextual policy continuity but is not itself the self model.
        retrieved, similarity = retrieve_memory(
            memory, environment_cue(env), generation, learn
        )
        if retrieved is not None:
            recalled, _ = _bounded_policy_move(
                policy_state, retrieved.policy,
                learn.max_policy_step, learn.max_policy_offset
            )
        else:
            recalled = dict(policy_state)

        candidates = _candidate_policies(
            recalled, rng, learn, self_params
        )

        model_ready = (
            self_model_enabled
            and model.predictor.observations >= self_params.min_observations
        )
        predicted_scores = []
        predicted_vectors = []
        if model_ready:
            for cand in candidates:
                x = self_predictor_input(
                    world, predicted_world, organism, cand
                )
                pred = contextual_self_prediction(
                    model, env.name, x, organism
                )
                predicted_vectors.append(pred)
                predicted_scores.append(
                    _predicted_candidate_score(pred, organism, self_params)
                )
            model_index = int(np.argmax(predicted_scores))
        else:
            model_index = 0
            predicted_vectors = [None]*len(candidates)
            predicted_scores = [float("nan")]*len(candidates)

        # Causal action selection: exactly one candidate transition is committed.
        # Before the self-model has enough observations, and in the ablated
        # control, the system follows a deterministic model-free exploration
        # schedule. This keeps random candidate generation matched across runs and
        # avoids an oracle that evaluates unchosen futures.
        if not self_model_enabled:
            candidates = candidates[:2]

        recent_model_competent = False
        if model.prediction_errors and model.baseline_errors:
            window = min(8, len(model.prediction_errors), len(model.baseline_errors))
            pm = float(np.mean(model.prediction_errors[-window:]))
            bm = float(np.mean(model.baseline_errors[-window:]))
            recent_model_competent = pm <= 1.20*max(bm, 1e-12)

        if self_model_enabled and model_ready and recent_model_competent:
            chosen_index = model_index
            source = "self_model"
        else:
            # One exploratory action every third generation; otherwise use the
            # current/recalled lower-closure policy.
            chosen_index = 1 if (len(candidates) > 1 and generation % 3 == 0) else 0
            source = "model_free"

        forcing_seed = int(seed + 177013*generation + 10103)
        chosen_policy = candidates[chosen_index]
        chosen = _evaluate_policy_once(
            state, genotype, chosen_policy, env,
            base_org, evo, learn, numerical_policy,
            forcing_seed, generation
        )

        if self_model_enabled and source == "self_model":
            model.action_interventions += int(chosen_index != 0)
            events.append({
                "event": "self_model_action",
                "generation": generation,
                "candidate_count": len(candidates),
                "chosen_index": chosen_index,
                "predicted_score": predicted_scores[chosen_index],
                "recent_model_competent": recent_model_competent,
            })

        if not chosen["success"]:
            events.append({
                "event": "self_model_terminal",
                "generation": generation,
                "reason": chosen["step"].terminal_reason or "formation_failure",
            })
            break

        core_steps += 1
        successful += 1
        evolved = chosen["state"]
        reward = chosen["reward"]
        next_org = organism_readout(
            evolved, chosen_policy, memory, chosen["org"]
        )

        # Evaluate the prediction made before committing this action.
        x_chosen = self_predictor_input(
            world, predicted_world, organism, chosen_policy
        )
        prediction_error = None
        baseline_error = None
        exported_excess_norm = 0.0
        if model.predictor.observations >= self_params.min_observations:
            pred = contextual_self_prediction(
                model, env.name, x_chosen, organism
            )
            clipped_pred = np.clip(
                pred[:7],
                -self_params.prediction_clip,
                self_params.prediction_clip,
            )
            exported_excess_norm = float(np.linalg.norm(pred[:7]-clipped_pred))
            if exported_excess_norm > 1e-12:
                model.excess_exports += 1
                events.append({
                    "event": "self_model_export",
                    "generation": generation,
                    "excess_norm": exported_excess_norm,
                    "mode": "non_integrable_self_description",
                })
            # The Self-Model prediction benchmark concerns the organism's own
            # future persistent state. Reward prediction is used for action choice
            # but is not allowed to inflate or deflate this self-state benchmark.
            prediction_error = float(
                np.linalg.norm(pred[:7]-next_org)/math.sqrt(len(next_org))
            )
            baseline_error = float(
                np.linalg.norm(organism-next_org)/math.sqrt(len(next_org))
            )
            model.prediction_errors.append(prediction_error)
            model.baseline_errors.append(baseline_error)

        # Online causal update: current world+self+action -> next self+outcome.
        # The environment-indexed transition witness and the general linear map
        # are both updated only after the committed transition is observed.
        update_contextual_self_transition(
            model, env.name, organism, next_org, reward
        )
        target = np.concatenate([next_org, [reward]])
        model.predictor.update(x_chosen, target)

        oo_coupling, policy_coupling, reachable = self_reference_metrics(
            model, self_params
        )
        rho = model.predictor.recurrent_rho()
        mediator_strength = float(
            np.linalg.norm(closure[-3:])
        )
        world_coherent = bool(
            np.linalg.norm(world) >= self_params.world_coherence_min
        )
        organism_coherent = bool(
            np.linalg.norm(organism) >= self_params.organism_coherence_min
        )
        corridor_ok = (
            self_params.world_self_epsilon < distance < self_params.world_self_limit
        )
        bounded = rho <= self_params.recurrent_rho_max + 1e-10
        self_closure = bool(
            model.predictor.observations >= self_params.min_observations
            and world_coherent
            and organism_coherent
            and reachable
            and corridor_ok
            and bounded
            and mediator_strength >= self_params.mediator_min_coupling
        )
        if self_closure:
            model.closure_passes += 1
        elif model.predictor.observations >= self_params.min_observations:
            model.closure_failures += 1

        # Learning and memory remain retained lower closures.
        policy_state, policy_change = _bounded_policy_move(
            policy_state, chosen_policy,
            learn.max_policy_step, learn.max_policy_offset
        )
        mem_events, slot_counter = update_memory(
            memory, environment_cue(env), chosen_policy, reward,
            generation, learn, slot_counter
        )
        events.extend(mem_events)

        if prediction_error is not None:
            events.append({
                "event": "self_prediction",
                "generation": generation,
                "prediction_error": prediction_error,
                "persistence_baseline_error": baseline_error,
                "recurrent_rho": rho,
                "self_reference_reachable": reachable,
            })

        frames.append({
            "generation": generation,
            "environment": env.name,
            "reward": float(reward),
            "maintenance": float(chosen["maintenance"]),
            "environment_match": float(chosen["match"]),
            "world_coherent": world_coherent,
            "organism_coherent": organism_coherent,
            "world_self_distance": distance,
            "world_self_corridor": corridor_ok,
            "self_mediator_strength": mediator_strength,
            "self_reference_reachable": reachable,
            "organism_recurrent_coupling": oo_coupling,
            "policy_to_self_coupling": policy_coupling,
            "recurrent_rho": rho,
            "self_model_closure": self_closure,
            "self_model_action_used": bool(
                self_model_enabled and source == "self_model"
            ),
            "self_model_action_intervention": bool(
                self_model_enabled and source == "self_model" and chosen_index != 0
            ),
            "action_source": source,
            "chosen_candidate_index": chosen_index,
            "candidate_count": len(candidates),
            "prediction_error": prediction_error,
            "persistence_baseline_error": baseline_error,
            "policy_change_norm": float(policy_change),
            "memory_slots": len(memory.slots),
            "mean_resource": float(next_org[0]),
            "retained_fraction": float(next_org[3]),
            "export_fraction": float(next_org[4]),
            "self_model_excess_export_norm": exported_excess_norm,
            "self_model_excess_exports_total": model.excess_exports,
        })

        state = evolved

    return SelfModelRun(
        initial_seed=seed,
        frames=frames,
        events=events,
        final_state=state,
        final_policy=policy_state,
        memory=memory,
        self_model=model,
        self_model_enabled=self_model_enabled,
        core_steps=core_steps,
        successful_reclosures=successful,
    )


def compare_self_model(
    seed: int = 1341550191,
    generations: int = 80,
    **kwargs,
) -> dict:
    enabled = simulate_self_model(
        seed=seed, generations=generations,
        self_model_enabled=True, **kwargs
    )
    disabled = simulate_self_model(
        seed=seed, generations=generations,
        self_model_enabled=False, **kwargs
    )
    n = min(len(enabled.frames), len(disabled.frames))
    reward_gain = np.array([
        enabled.frames[i]["reward"] - disabled.frames[i]["reward"]
        for i in range(n)
    ], dtype=float)

    ep = [
        f["prediction_error"] for f in enabled.frames
        if f["prediction_error"] is not None
    ]
    eb = [
        f["persistence_baseline_error"] for f in enabled.frames
        if f["persistence_baseline_error"] is not None
    ]
    model_better_fraction = 0.0
    if ep and eb:
        m = min(len(ep), len(eb))
        model_better_fraction = float(np.mean(
            np.array(ep[:m]) < np.array(eb[:m])
        ))

    return {
        "self_model": enabled,
        "ablated_control": disabled,
        "summary": {
            "compared_steps": n,
            "mean_reward_gain": float(np.mean(reward_gain)) if n else 0.0,
            "self_model_action_interventions":
                enabled.self_model.action_interventions,
            "self_model_closure_passes":
                enabled.self_model.closure_passes,
            "mean_prediction_error":
                float(np.mean(ep)) if ep else None,
            "mean_persistence_baseline_error":
                float(np.mean(eb)) if eb else None,
            "prediction_beats_persistence_fraction":
                model_better_fraction,
            "final_self_reference_reachable": (
                enabled.frames[-1]["self_reference_reachable"]
                if enabled.frames else False
            ),
        },
    }


def write_self_model_report(
    run: SelfModelRun,
    outdir: str | Path,
    stem: str = "self_model",
) -> dict[str, str]:
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    csv_path = outdir / f"{stem}_frames.csv"
    if run.frames:
        fields = list(run.frames[0].keys())
        with csv_path.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(run.frames)

    events_path = outdir / f"{stem}_events.json"
    events_path.write_text(json.dumps(run.events, indent=2), encoding="utf-8")
    summary_path = outdir / f"{stem}_summary.json"
    summary_path.write_text(json.dumps(run.summary(), indent=2), encoding="utf-8")

    weights_path = outdir / f"{stem}_predictor_weights.csv"
    np.savetxt(weights_path, run.self_model.predictor.weights, delimiter=",")

    plot_path = outdir / f"{stem}_closure.png"
    if run.frames:
        g = np.array([f["generation"] for f in run.frames])
        pred = np.array([
            np.nan if f["prediction_error"] is None else f["prediction_error"]
            for f in run.frames
        ])
        base = np.array([
            np.nan if f["persistence_baseline_error"] is None
            else f["persistence_baseline_error"]
            for f in run.frames
        ])
        dist = np.array([f["world_self_distance"] for f in run.frames])
        rho = np.array([f["recurrent_rho"] for f in run.frames])

        fig, ax1 = plt.subplots(figsize=(8.3, 5.0))
        ax1.plot(g, pred, label="self-model prediction error")
        ax1.plot(g, base, label="persistence baseline error", linestyle="--")
        ax1.set_xlabel("Generation")
        ax1.set_ylabel("Prediction error")
        ax2 = ax1.twinx()
        ax2.plot(g, dist, label="world/self distance", linestyle=":")
        ax2.plot(g, rho, label="self recurrent rho", linestyle="-.")
        ax2.set_ylabel("Closure geometry")
        lines = ax1.get_lines()+ax2.get_lines()
        ax1.legend(lines,[ln.get_label() for ln in lines],loc="best",fontsize=8)
        ax1.set_title("BFG self-model closure diagnostics")
        fig.tight_layout()
        fig.savefig(plot_path,dpi=165)
        plt.close(fig)
    else:
        plot_path = Path("")

    return {
        "frames_csv": str(csv_path),
        "events_json": str(events_path),
        "summary_json": str(summary_path),
        "predictor_weights_csv": str(weights_path),
        "closure_plot": str(plot_path),
    }


def write_self_model_comparison(
    comparison: dict,
    outdir: str | Path,
    stem: str = "self_model_comparison",
) -> dict[str, str]:
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    a = comparison["self_model"]
    b = comparison["ablated_control"]
    n = min(len(a.frames),len(b.frames))
    rows = []
    for i in range(n):
        rows.append({
            "generation": a.frames[i]["generation"],
            "environment": a.frames[i]["environment"],
            "reward_self_model": a.frames[i]["reward"],
            "reward_control": b.frames[i]["reward"],
            "reward_gain": a.frames[i]["reward"]-b.frames[i]["reward"],
            "prediction_error": a.frames[i]["prediction_error"],
            "persistence_baseline_error": a.frames[i]["persistence_baseline_error"],
            "self_reference_reachable": a.frames[i]["self_reference_reachable"],
            "self_model_closure": a.frames[i]["self_model_closure"],
            "self_model_action_intervention":
                a.frames[i]["self_model_action_intervention"],
        })
    csv_path = outdir/f"{stem}.csv"
    if rows:
        with csv_path.open("w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0].keys()))
            w.writeheader(); w.writerows(rows)
    summary_path = outdir/f"{stem}_summary.json"
    summary_path.write_text(
        json.dumps(comparison["summary"],indent=2),encoding="utf-8"
    )
    return {
        "comparison_csv": str(csv_path),
        "comparison_summary": str(summary_path),
    }
