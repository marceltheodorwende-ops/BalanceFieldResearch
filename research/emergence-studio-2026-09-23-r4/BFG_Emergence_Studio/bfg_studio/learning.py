from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
import csv
import json
import math
import numpy as np
import matplotlib.pyplot as plt

from .types import BFGState, NumericalPolicy
from .core import canonical_reclosure
from .alife import (
    SelfOrganizationParameters,
    SelfOrganizingNetworkCarrier,
    make_self_organizing_seed,
    organization_metrics,
)
from .population import PopulationParameters
from .evolution import (
    TRAIT_BOUNDS,
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
    standard_shift_program,
)


PLASTIC_TRAITS = (
    "formation_drive",
    "neighbor_scale",
    "resource_blend",
    "topology_blend",
    "export_cost",
)


@dataclass(frozen=True)
class LearningParameters:
    exploration_sigma: float = 0.035
    recalled_exploration_factor: float = 0.12
    retrieval_blend: float = 0.92
    reward_baseline_rate: float = 0.12
    policy_accept_margin: float = 0.002
    max_policy_step: float = 0.11
    max_policy_offset: float = 0.28
    memory_decay: float = 0.994
    memory_similarity_threshold: float = 0.84
    memory_merge_threshold: float = 0.96
    memory_update_rate: float = 0.38
    max_memory_slots: int = 8
    witness_min_gap: int = 4

    def validate(self):
        if self.exploration_sigma < 0:
            raise ValueError("exploration_sigma must be nonnegative")
        if not (0 <= self.recalled_exploration_factor <= 1):
            raise ValueError("recalled_exploration_factor must lie in [0,1]")
        if not (0 <= self.retrieval_blend <= 1):
            raise ValueError("retrieval_blend must lie in [0,1]")
        if not (0 < self.reward_baseline_rate <= 1):
            raise ValueError("reward_baseline_rate must lie in (0,1]")
        if self.max_policy_step <= 0:
            raise ValueError("max_policy_step must be positive")
        if self.max_policy_offset <= 0:
            raise ValueError("max_policy_offset must be positive")
        if not (0 < self.memory_decay <= 1):
            raise ValueError("memory_decay must lie in (0,1]")
        if not (0 <= self.memory_similarity_threshold <= 1):
            raise ValueError("memory_similarity_threshold must lie in [0,1]")
        if not (0 <= self.memory_merge_threshold <= 1):
            raise ValueError("memory_merge_threshold must lie in [0,1]")
        if self.max_memory_slots < 1:
            raise ValueError("max_memory_slots must be positive")
        if self.witness_min_gap < 1:
            raise ValueError("witness_min_gap must be positive")


@dataclass
class MemorySlot:
    slot_id: str
    cue: np.ndarray
    policy: dict[str, float]
    reward: float
    strength: float
    created_generation: int
    last_update_generation: int
    last_retrieved_generation: int | None = None
    retrieval_count: int = 0


@dataclass
class MemoryState:
    slots: list[MemorySlot] = field(default_factory=list)
    reward_baseline: float = 0.0
    witness_recoveries: int = 0
    witness_failures: int = 0
    exported_slots: int = 0


@dataclass
class LearningUnit:
    state: BFGState
    genotype: dict[str, float]
    policy: dict[str, float]
    memory: MemoryState
    age: int = 0
    last_reward: float = 0.0


@dataclass
class LearningRun:
    initial_seed: int
    frames: list[dict]
    events: list[dict]
    final_unit: LearningUnit
    core_steps: int
    successful_reclosures: int
    memory_enabled: bool

    def summary(self) -> dict:
        retrievals = sum(e["event"] == "memory_retrieval" for e in self.events)
        recoveries = sum(e["event"] == "witness_recovery" for e in self.events)
        encodings = sum(e["event"] == "memory_encode" for e in self.events)
        policy_changes = sum(e["event"] == "policy_update" for e in self.events)
        final = self.frames[-1] if self.frames else {}
        return {
            "initial_seed": self.initial_seed,
            "frames": len(self.frames),
            "memory_enabled": self.memory_enabled,
            "memory_slots_final": len(self.final_unit.memory.slots),
            "memory_encodings": encodings,
            "memory_retrievals": retrievals,
            "witness_recoveries": recoveries,
            "witness_failures": self.final_unit.memory.witness_failures,
            "memory_exports": self.final_unit.memory.exported_slots,
            "policy_updates": policy_changes,
            "core_steps": self.core_steps,
            "successful_reclosures": self.successful_reclosures,
            "final_reward": final.get("reward", 0.0),
            "final_environment_match": final.get("environment_match", 0.0),
            "final_maintenance": final.get("maintenance", 0.0),
        }


def normalize_trait(key: str, value: float) -> float:
    lo, hi = TRAIT_BOUNDS[key]
    return float((value-lo)/(hi-lo))


def denormalize_trait(key: str, value: float) -> float:
    lo, hi = TRAIT_BOUNDS[key]
    return float(lo + np.clip(value, 0.0, 1.0)*(hi-lo))


def environment_cue(env: EnvironmentState) -> np.ndarray:
    # The learner senses environmental conditions, not the hidden preferred-trait vector.
    capacity = min(float(env.carrying_capacity)/16.0, 1.0)
    return np.array([
        np.clip(env.resource_supply/1.5, 0.0, 1.0),
        np.clip(env.disturbance, 0.0, 1.0),
        capacity,
    ], dtype=float)


def cue_similarity(a: np.ndarray, b: np.ndarray) -> float:
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    # RBF similarity is stable even for low-dimensional positive cue vectors.
    d2 = float(np.sum((a-b)**2))
    return float(np.exp(-d2/(2*0.18**2)))


def zero_policy() -> dict[str, float]:
    return {k: 0.0 for k in PLASTIC_TRAITS}


def effective_traits(
    genotype: dict[str, float],
    policy: dict[str, float],
    params: LearningParameters,
) -> dict[str, float]:
    out = dict(genotype)
    for key in PLASTIC_TRAITS:
        g = normalize_trait(key, genotype[key])
        p = float(np.clip(policy.get(key, 0.0), -params.max_policy_offset, params.max_policy_offset))
        out[key] = denormalize_trait(key, np.clip(g+p, 0.0, 1.0))
    return out


def _policy_vector(policy: dict[str, float]) -> np.ndarray:
    return np.array([float(policy.get(k, 0.0)) for k in PLASTIC_TRAITS], dtype=float)


def _vector_policy(v: np.ndarray) -> dict[str, float]:
    return {k: float(v[i]) for i, k in enumerate(PLASTIC_TRAITS)}


def _bounded_policy_move(
    current: dict[str, float],
    target: dict[str, float],
    max_step: float,
    max_offset: float,
) -> tuple[dict[str, float], float]:
    c = _policy_vector(current)
    t = _policy_vector(target)
    delta = t-c
    norm = float(np.linalg.norm(delta))
    if norm > max_step:
        delta *= max_step/max(norm, 1e-12)
    out = np.clip(c+delta, -max_offset, max_offset)
    actual = float(np.linalg.norm(out-c))
    return _vector_policy(out), actual


def retrieve_memory(
    memory: MemoryState,
    cue: np.ndarray,
    generation: int,
    params: LearningParameters,
) -> tuple[MemorySlot | None, float]:
    if not memory.slots:
        return None, 0.0
    sims = [cue_similarity(cue, slot.cue) for slot in memory.slots]
    idx = int(np.argmax(sims))
    best = memory.slots[idx]
    sim = float(sims[idx])
    if sim < params.memory_similarity_threshold:
        return None, sim
    best.retrieval_count += 1
    best.last_retrieved_generation = generation
    return best, sim


def _decay_and_compress_memory(
    memory: MemoryState,
    params: LearningParameters,
) -> list[str]:
    exported = []
    for slot in memory.slots:
        slot.strength *= params.memory_decay

    # Merge highly similar contextual memories, retaining the higher-reward policy.
    merged = []
    used = set()
    for i, a in enumerate(memory.slots):
        if i in used:
            continue
        best = a
        for j in range(i+1, len(memory.slots)):
            if j in used:
                continue
            b = memory.slots[j]
            if cue_similarity(a.cue, b.cue) >= params.memory_merge_threshold:
                used.add(j)
                if b.reward > best.reward:
                    best = b
        merged.append(best)
    memory.slots = merged

    # Forget weak / surplus slots first. This is the explicit memory export channel.
    if len(memory.slots) > params.max_memory_slots:
        ordered = sorted(
            memory.slots,
            key=lambda s: (s.strength, s.reward, s.last_update_generation),
            reverse=True,
        )
        keep = ordered[:params.max_memory_slots]
        remove = ordered[params.max_memory_slots:]
        exported.extend([s.slot_id for s in remove])
        memory.slots = keep
        memory.exported_slots += len(remove)
    return exported


def update_memory(
    memory: MemoryState,
    cue: np.ndarray,
    policy: dict[str, float],
    reward: float,
    generation: int,
    params: LearningParameters,
    slot_counter: int,
) -> tuple[list[dict], int]:
    events = []
    if memory.reward_baseline == 0.0:
        memory.reward_baseline = float(reward)
    else:
        memory.reward_baseline = (
            (1.0-params.reward_baseline_rate)*memory.reward_baseline
            + params.reward_baseline_rate*float(reward)
        )

    # Find context match independently of retrieval threshold, so encoding can
    # refine an existing nearby trace.
    match = None
    sim = 0.0
    if memory.slots:
        sims = [cue_similarity(cue, slot.cue) for slot in memory.slots]
        idx = int(np.argmax(sims))
        sim = float(sims[idx])
        if sim >= params.memory_similarity_threshold:
            match = memory.slots[idx]

    if match is None:
        slot = MemorySlot(
            slot_id=f"M{slot_counter}",
            cue=np.asarray(cue, dtype=float).copy(),
            policy=dict(policy),
            reward=float(reward),
            strength=1.0,
            created_generation=generation,
            last_update_generation=generation,
        )
        memory.slots.append(slot)
        slot_counter += 1
        events.append({
            "event": "memory_encode",
            "generation": generation,
            "slot_id": slot.slot_id,
            "reward": float(reward),
            "context_similarity": sim,
        })
    else:
        # Incorporate change only when outcome improves, avoiding unstable overwrite.
        if reward > match.reward + params.policy_accept_margin:
            p_old = _policy_vector(match.policy)
            p_new = _policy_vector(policy)
            p = (1.0-params.memory_update_rate)*p_old + params.memory_update_rate*p_new
            match.policy = _vector_policy(p)
            match.reward = float(reward)
            match.cue = (
                (1.0-params.memory_update_rate)*match.cue
                + params.memory_update_rate*np.asarray(cue, dtype=float)
            )
            match.last_update_generation = generation
            match.strength = min(1.5, match.strength + 0.12)
            events.append({
                "event": "memory_consolidate",
                "generation": generation,
                "slot_id": match.slot_id,
                "reward": float(reward),
            })

    exported = _decay_and_compress_memory(memory, params)
    for slot_id in exported:
        events.append({
            "event": "memory_export",
            "generation": generation,
            "slot_id": slot_id,
            "mode": "compression_abstraction_forgetting",
        })
    return events, slot_counter



def _evaluate_policy_once(
    state: BFGState,
    genotype: dict[str, float],
    candidate_policy: dict[str, float],
    env: EnvironmentState,
    base_org: SelfOrganizationParameters,
    evo: EvolutionParameters,
    learn: LearningParameters,
    numerical_policy: NumericalPolicy,
    forcing_seed: int,
    generation: int,
):
    """
    Evaluate one candidate policy from the same pre-transition state.

    Candidate comparisons use the same forcing seed, so environmental edge damage
    is matched across the two policy probes. Only one selected transition is
    committed to the lifecycle.
    """
    traits = effective_traits(genotype, candidate_policy, learn)
    org = traits_to_org(base_org, traits, state.dim)
    rng = np.random.default_rng(forcing_seed)
    forced, forcing = apply_environment(state, env, org, rng)
    forced.generation = generation
    carrier = SelfOrganizingNetworkCarrier(org)
    step = canonical_reclosure(forced, numerical_policy)
    if not step.success:
        return {
            "success": False,
            "reward": float("-inf"),
            "traits": traits,
            "org": org,
            "forcing": forcing,
            "step": step,
            "state": None,
            "intrinsic": float("-inf"),
            "match": 0.0,
            "maintenance": 0.0,
        }

    evolved = carrier.advance(forced, step, numerical_policy)
    evolved.generation = generation + 1
    if evolved.terminal:
        return {
            "success": False,
            "reward": float("-inf"),
            "traits": traits,
            "org": org,
            "forcing": forcing,
            "step": step,
            "state": evolved,
            "intrinsic": float("-inf"),
            "match": 0.0,
            "maintenance": 0.0,
        }

    eval_unit = EvolutionUnit(
        unit_id="L0",
        state=evolved,
        traits=traits,
        age=generation,
        last_novelty=float(step.spectral_mismatch or 0.0),
    )
    reward, intrinsic, match = environmental_fitness(
        eval_unit, org, evo, env
    )
    maintenance = organization_metrics(evolved, org)["maintenance_score"]
    return {
        "success": True,
        "reward": float(reward),
        "traits": traits,
        "org": org,
        "forcing": forcing,
        "step": step,
        "state": evolved,
        "intrinsic": float(intrinsic),
        "match": float(match),
        "maintenance": float(maintenance),
    }


def simulate_learning(
    seed: int = 1341550191,
    generations: int = 60,
    program: EnvironmentProgram | None = None,
    base_org: SelfOrganizationParameters | None = None,
    base_pop: PopulationParameters | None = None,
    evo: EvolutionParameters | None = None,
    learn: LearningParameters | None = None,
    memory_enabled: bool = True,
    policy: NumericalPolicy | None = None,
) -> LearningRun:
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
    learn = learn or LearningParameters()
    policy = policy or NumericalPolicy()
    learn.validate()

    if program is None:
        # Repeated contexts create a prospective memory test:
        # the same cue disappears and later returns after separated recursive cycles.
        rich = EnvironmentState(
            name="learning_rich",
            resource_supply=0.94,
            disturbance=0.02,
            carrying_capacity=8,
            match_weight=0.58,
            preferred_traits={
                "formation_drive": 1.26,
                "neighbor_scale": 0.41,
                "resource_blend": 0.19,
                "topology_blend": 0.12,
                "export_cost": 0.13,
            },
        )
        poor = EnvironmentState(
            name="learning_poor",
            resource_supply=0.50,
            disturbance=0.17,
            carrying_capacity=5,
            match_weight=0.58,
            preferred_traits={
                "formation_drive": 1.72,
                "neighbor_scale": 0.22,
                "resource_blend": 0.47,
                "topology_blend": 0.35,
                "export_cost": 0.04,
            },
        )
        program = EnvironmentProgram(phases=(
            (0, rich), (10, poor), (20, rich), (30, poor), (40, rich), (50, poor)
        ))

    rng = np.random.default_rng(seed + 41813)
    state = make_self_organizing_seed(seed=seed, params=base_org)
    genotype = default_traits(base_org, base_pop)
    unit = LearningUnit(
        state=state,
        genotype=genotype,
        policy=zero_policy(),
        memory=MemoryState(),
        age=0,
    )
    events = []
    frames = []
    core_steps = successful = 0
    slot_counter = 0
    last_env_name = None
    context_last_seen: dict[str, int] = {}

    for generation in range(int(generations)+1):
        env = program.at(generation)
        cue = environment_cue(env)
        prior_context_generation = context_last_seen.get(env.name)
        context_gap = (
            generation - prior_context_generation
            if prior_context_generation is not None
            else None
        )
        is_environment_shift = last_env_name is not None and env.name != last_env_name
        if is_environment_shift:
            events.append({
                "event": "environment_shift",
                "generation": generation,
                "from": last_env_name,
                "to": env.name,
            })
        last_env_name = env.name

        retrieved = None
        similarity = 0.0
        retrieval_age = None
        if memory_enabled:
            retrieved, similarity = retrieve_memory(
                unit.memory, cue, generation, learn
            )
            if retrieved is not None:
                retrieval_age = generation - retrieved.last_update_generation
                events.append({
                    "event": "memory_retrieval",
                    "generation": generation,
                    "slot_id": retrieved.slot_id,
                    "similarity": similarity,
                    "trace_age": retrieval_age,
                    "stored_reward": retrieved.reward,
                })
                if (
                    is_environment_shift
                    and context_gap is not None
                    and context_gap >= learn.witness_min_gap
                ):
                    unit.memory.witness_recoveries += 1
                    events.append({
                        "event": "witness_recovery",
                        "generation": generation,
                        "slot_id": retrieved.slot_id,
                        "trace_age": retrieval_age,
                        "context_gap": context_gap,
                        "similarity": similarity,
                    })

        if (
            memory_enabled
            and is_environment_shift
            and context_gap is not None
            and context_gap >= learn.witness_min_gap
            and retrieved is None
        ):
            unit.memory.witness_failures += 1
            events.append({
                "event": "witness_failure",
                "generation": generation,
                "environment": env.name,
                "context_gap": context_gap,
                "best_similarity": similarity,
            })

        # Stabilized baseline policy for this context.
        if memory_enabled and retrieved is not None:
            base_policy, recall_step = _bounded_policy_move(
                unit.policy,
                retrieved.policy,
                learn.max_policy_step,
                learn.max_policy_offset,
            )
        elif memory_enabled:
            base_policy = dict(unit.policy)
            recall_step = 0.0
        else:
            base_policy = zero_policy()
            recall_step = 0.0

        # One bounded exploratory alternative. The no-memory control does not
        # retain or optimize actions; it represents fixed-transition behavior.
        explore_policy = dict(base_policy)
        exploration_scale = learn.exploration_sigma
        if retrieved is not None:
            exploration_scale *= learn.recalled_exploration_factor
        eps = rng.normal(0.0, exploration_scale, size=len(PLASTIC_TRAITS))
        for i, key in enumerate(PLASTIC_TRAITS):
            explore_policy[key] = float(np.clip(
                explore_policy[key] + eps[i],
                -learn.max_policy_offset,
                learn.max_policy_offset,
            ))
        explore_policy, explore_step = _bounded_policy_move(
            base_policy,
            explore_policy,
            learn.max_policy_step,
            learn.max_policy_offset,
        )

        forcing_seed = int(seed + 100003*generation + 7919)
        base_eval = _evaluate_policy_once(
            unit.state, unit.genotype, base_policy, env,
            base_org, evo, learn, policy, forcing_seed, generation
        )

        if memory_enabled:
            explore_eval = _evaluate_policy_once(
                unit.state, unit.genotype, explore_policy, env,
                base_org, evo, learn, policy, forcing_seed, generation
            )
            probe_count = 2
            if explore_eval["success"] and (
                not base_eval["success"]
                or explore_eval["reward"] > base_eval["reward"] + learn.policy_accept_margin
            ):
                chosen_policy = explore_policy
                chosen = explore_eval
                chosen_label = "explore"
            else:
                chosen_policy = base_policy
                chosen = base_eval
                chosen_label = "recall_or_current"
        else:
            chosen_policy = zero_policy()
            chosen = base_eval
            chosen_label = "fixed_control"
            probe_count = 1

        if not chosen["success"]:
            events.append({
                "event": "learning_terminal",
                "generation": generation,
                "reason": chosen["step"].terminal_reason or "formation_failure",
            })
            break

        core_steps += 1
        successful += 1
        step = chosen["step"]
        evolved = chosen["state"]
        reward = chosen["reward"]
        intrinsic = chosen["intrinsic"]
        match = chosen["match"]
        maintenance = chosen["maintenance"]
        forcing = chosen["forcing"]

        old_policy = dict(unit.policy)
        if memory_enabled:
            unit.policy, policy_change = _bounded_policy_move(
                unit.policy,
                chosen_policy,
                learn.max_policy_step,
                learn.max_policy_offset,
            )
        else:
            unit.policy = zero_policy()
            policy_change = 0.0

        if policy_change > 1e-12:
            events.append({
                "event": "policy_update",
                "generation": generation,
                "change_norm": policy_change,
                "reward": reward,
                "source": chosen_label,
            })

        if memory_enabled:
            mem_events, slot_counter = update_memory(
                unit.memory, cue, chosen_policy, reward,
                generation, learn, slot_counter
            )
            events.extend(mem_events)
        else:
            if unit.memory.reward_baseline == 0:
                unit.memory.reward_baseline = reward
            else:
                unit.memory.reward_baseline = (
                    (1.0-learn.reward_baseline_rate)*unit.memory.reward_baseline
                    + learn.reward_baseline_rate*reward
                )

        policy_norm = float(np.linalg.norm(_policy_vector(unit.policy)))
        frames.append({
            "generation": generation,
            "environment": env.name,
            "reward": float(reward),
            "intrinsic_fitness": float(intrinsic),
            "environment_match": float(match),
            "maintenance": float(maintenance),
            "memory_slots": len(unit.memory.slots),
            "memory_retrieved": bool(retrieved is not None),
            "retrieval_similarity": float(similarity),
            "retrieval_age": retrieval_age if retrieval_age is not None else -1,
            "witness_recoveries_total": unit.memory.witness_recoveries,
            "reward_baseline": float(unit.memory.reward_baseline),
            "policy_norm": policy_norm,
            "policy_change_norm": float(policy_change),
            "recall_step_norm": float(recall_step),
            "exploration_step_norm": float(explore_step),
            "chosen_probe": chosen_label,
            "probe_count": probe_count,
            "base_probe_reward": float(base_eval["reward"]) if base_eval["success"] else None,
            "explore_probe_reward": (
                float(explore_eval["reward"])
                if memory_enabled and explore_eval["success"]
                else None
            ),
            "spectral_novelty": bool(step.spectral_novelty),
            "spectral_mismatch": float(step.spectral_mismatch or 0.0),
            "mean_resource_after_forcing": forcing["mean_resource_after"],
        })
        for key in PLASTIC_TRAITS:
            frames[-1][f"policy_{key}"] = float(unit.policy[key])
            frames[-1][f"effective_{key}"] = float(chosen["traits"][key])

        context_last_seen[env.name] = generation
        unit.state = evolved
        unit.age += 1
        unit.last_reward = reward

    return LearningRun(
        initial_seed=seed,
        frames=frames,
        events=events,
        final_unit=unit,
        core_steps=core_steps,
        successful_reclosures=successful,
        memory_enabled=memory_enabled,
    )

def compare_memory_learning(
    seed: int = 1341550191,
    generations: int = 60,
    program: EnvironmentProgram | None = None,
    **kwargs,
) -> dict:
    enabled = simulate_learning(
        seed=seed, generations=generations, program=program,
        memory_enabled=True, **kwargs
    )
    disabled = simulate_learning(
        seed=seed, generations=generations, program=program,
        memory_enabled=False, **kwargs
    )

    n = min(len(enabled.frames), len(disabled.frames))
    reward_gain = np.array([
        enabled.frames[i]["reward"] - disabled.frames[i]["reward"]
        for i in range(n)
    ], dtype=float)
    recurrence_gens = [
        e["generation"] for e in enabled.events
        if e["event"] == "witness_recovery"
    ]
    recovery_indices = [
        i for i in range(n)
        if enabled.frames[i]["generation"] in set(recurrence_gens)
    ]
    mean_recovery_gain = (
        float(np.mean(reward_gain[recovery_indices]))
        if recovery_indices else 0.0
    )
    post_recall = [
        i for i in range(n)
        if enabled.frames[i]["memory_retrieved"]
        and enabled.frames[i]["retrieval_age"] >= kwargs.get(
            "learn", LearningParameters()
        ).witness_min_gap
    ]
    mean_post_recall_gain = (
        float(np.mean(reward_gain[post_recall])) if post_recall else 0.0
    )
    return {
        "memory_enabled": enabled,
        "memory_disabled": disabled,
        "summary": {
            "compared_steps": n,
            "mean_reward_gain_memory_vs_control": float(np.mean(reward_gain)) if n else 0.0,
            "mean_reward_gain_at_witness_recovery": mean_recovery_gain,
            "mean_post_recall_reward_gain": mean_post_recall_gain,
            "witness_recoveries": enabled.final_unit.memory.witness_recoveries,
            "memory_slots_final": len(enabled.final_unit.memory.slots),
            "recurrence_generations": recurrence_gens,
        }
    }


def write_learning_report(
    run: LearningRun,
    outdir: str | Path,
    stem: str = "learning",
) -> dict[str, str]:
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    frames_csv = outdir / f"{stem}_frames.csv"
    if run.frames:
        with frames_csv.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(run.frames[0].keys()))
            w.writeheader()
            w.writerows(run.frames)

    events_json = outdir / f"{stem}_events.json"
    events_json.write_text(json.dumps(run.events, indent=2), encoding="utf-8")
    summary_json = outdir / f"{stem}_summary.json"
    summary_json.write_text(json.dumps(run.summary(), indent=2), encoding="utf-8")

    memory_json = outdir / f"{stem}_memory.json"
    memory_payload = [{
        "slot_id": s.slot_id,
        "cue": s.cue.tolist(),
        "policy": s.policy,
        "reward": s.reward,
        "strength": s.strength,
        "created_generation": s.created_generation,
        "last_update_generation": s.last_update_generation,
        "last_retrieved_generation": s.last_retrieved_generation,
        "retrieval_count": s.retrieval_count,
    } for s in run.final_unit.memory.slots]
    memory_json.write_text(json.dumps(memory_payload, indent=2), encoding="utf-8")

    if run.frames:
        g = np.array([f["generation"] for f in run.frames])
        reward = np.array([f["reward"] for f in run.frames])
        match = np.array([f["environment_match"] for f in run.frames])
        slots = np.array([f["memory_slots"] for f in run.frames])
        policy_norm = np.array([f["policy_norm"] for f in run.frames])

        trajectory = outdir / f"{stem}_trajectory.png"
        fig, ax1 = plt.subplots(figsize=(8.1, 4.8))
        ax1.plot(g, reward, label="reward")
        ax1.plot(g, match, label="environment match")
        ax1.set_xlabel("Generation")
        ax1.set_ylabel("Performance")
        ax2 = ax1.twinx()
        ax2.plot(g, policy_norm, linestyle="--", label="policy norm")
        ax2.plot(g, slots/ max(1, np.max(slots)), linestyle=":", label="memory slots (norm)")
        ax2.set_ylabel("Plasticity / memory")
        lines = ax1.get_lines() + ax2.get_lines()
        ax1.legend(lines, [ln.get_label() for ln in lines], loc="best", fontsize=8)
        ax1.set_title("BFG within-lifetime learning and memory")
        fig.tight_layout()
        fig.savefig(trajectory, dpi=165)
        plt.close(fig)
    else:
        trajectory = None

    return {
        "frames_csv": str(frames_csv),
        "events_json": str(events_json),
        "summary_json": str(summary_json),
        "memory_json": str(memory_json),
        "trajectory_plot": str(trajectory) if trajectory else "",
    }


def write_learning_comparison(
    comparison: dict,
    outdir: str | Path,
    stem: str = "learning_comparison",
) -> dict[str, str]:
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    enabled = comparison["memory_enabled"]
    disabled = comparison["memory_disabled"]
    n = min(len(enabled.frames), len(disabled.frames))

    rows = []
    for i in range(n):
        a = enabled.frames[i]
        b = disabled.frames[i]
        rows.append({
            "generation": a["generation"],
            "environment": a["environment"],
            "reward_memory": a["reward"],
            "reward_control": b["reward"],
            "reward_gain": a["reward"]-b["reward"],
            "match_memory": a["environment_match"],
            "match_control": b["environment_match"],
            "memory_retrieved": a["memory_retrieved"],
            "retrieval_age": a["retrieval_age"],
            "witness_recoveries_total": a["witness_recoveries_total"],
        })

    csv_path = outdir / f"{stem}.csv"
    if rows:
        with csv_path.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)

    summary_path = outdir / f"{stem}_summary.json"
    summary_path.write_text(
        json.dumps(comparison["summary"], indent=2), encoding="utf-8"
    )

    plot_path = outdir / f"{stem}.png"
    if rows:
        g = np.array([r["generation"] for r in rows])
        a = np.array([r["reward_memory"] for r in rows])
        b = np.array([r["reward_control"] for r in rows])
        plt.figure(figsize=(8.0, 4.7))
        plt.plot(g, a, label="memory + learning")
        plt.plot(g, b, label="memory-disabled control")
        for r in rows:
            if r["memory_retrieved"] and r["retrieval_age"] >= 4:
                plt.scatter([r["generation"]], [r["reward_memory"]], s=22)
        plt.xlabel("Generation")
        plt.ylabel("Environmental reward")
        plt.title("Recall-enabled learning vs memory-disabled control")
        plt.legend()
        plt.tight_layout()
        plt.savefig(plot_path, dpi=165)
        plt.close()
    else:
        plot_path = Path("")

    return {
        "comparison_csv": str(csv_path),
        "comparison_summary": str(summary_path),
        "comparison_plot": str(plot_path),
    }
