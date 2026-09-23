from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
import copy
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
from .population import (
    PopulationParameters,
    _dimension_update,
    _viable_components,
    _substate,
    _rebuild_state,
)
from .evolution import (
    EvolutionParameters,
    EvolutionUnit,
    TRAIT_BOUNDS,
    default_traits,
    mutate_traits,
    traits_to_org,
    traits_to_pop,
    _fitness,
    _rebuild_with_traits,
)


@dataclass(frozen=True)
class EnvironmentState:
    name: str
    resource_supply: float = 0.80
    disturbance: float = 0.02
    carrying_capacity: int = 8
    preferred_traits: dict[str, float] = field(default_factory=dict)
    match_weight: float = 0.38
    perturbation_fraction: float = 0.25

    def validate(self):
        if not (0.0 <= self.resource_supply <= 1.5):
            raise ValueError("resource_supply must be in [0,1.5]")
        if not (0.0 <= self.disturbance <= 1.0):
            raise ValueError("disturbance must be in [0,1]")
        if self.carrying_capacity < 1:
            raise ValueError("carrying_capacity must be positive")
        if not (0.0 <= self.match_weight <= 1.0):
            raise ValueError("match_weight must lie in [0,1]")
        for key, value in self.preferred_traits.items():
            if key not in TRAIT_BOUNDS:
                raise ValueError(f"unknown preferred trait: {key}")
            lo, hi = TRAIT_BOUNDS[key]
            if not (lo <= value <= hi):
                raise ValueError(f"preferred {key}={value} outside [{lo},{hi}]")


@dataclass(frozen=True)
class EnvironmentProgram:
    phases: tuple[tuple[int, EnvironmentState], ...]

    def __post_init__(self):
        if not self.phases:
            raise ValueError("at least one environment phase is required")
        starts = [int(s) for s, _ in self.phases]
        if starts[0] != 0:
            raise ValueError("first environment phase must start at generation 0")
        if starts != sorted(starts) or len(set(starts)) != len(starts):
            raise ValueError("phase starts must be unique and sorted")
        for _, env in self.phases:
            env.validate()

    def at(self, generation: int) -> EnvironmentState:
        chosen = self.phases[0][1]
        for start, env in self.phases:
            if generation >= start:
                chosen = env
            else:
                break
        return chosen

    @property
    def shift_generations(self) -> list[int]:
        return [int(s) for s, _ in self.phases[1:]]


@dataclass
class EnvironmentalEvolutionRun:
    initial_seed: int
    frames: list[dict]
    environment_history: list[dict]
    trait_history: list[dict]
    events: list[dict]
    final_units: dict[str, EvolutionUnit]
    core_steps: int
    successful_reclosures: int
    novel_reclosures: int
    shift_generations: list[int]

    def summary(self) -> dict:
        selections = sum(e["event"] == "selection_death" for e in self.events)
        shifts = sum(e["event"] == "environment_shift" for e in self.events)
        fissions = sum(e["event"] == "fission" for e in self.events)
        mutations = sum(e["event"] == "mutation" for e in self.events)
        max_pop = max((f["population_size"] for f in self.frames), default=0)

        before_after = []
        for sg in self.shift_generations:
            before = next((f for f in self.frames if f["generation"] == max(0, sg-1)), None)
            after = next((f for f in self.frames if f["generation"] == sg), None)
            final = self.frames[-1] if self.frames else None
            selection = next(
                (
                    e for e in self.events
                    if e["event"] == "selection_round" and e["generation"] == sg
                ),
                None,
            )
            if before and after and final:
                baseline_new = (
                    selection["mean_match_before_selection"] if selection
                    else after["mean_environment_match"]
                )
                post_new = (
                    selection["mean_match_after_selection"] if selection
                    else after["mean_environment_match"]
                )
                before_after.append({
                    "shift_generation": sg,
                    "pre_shift_old_environment_match": before["mean_environment_match"],
                    "new_environment_match_before_selection": baseline_new,
                    "new_environment_match_after_selection": post_new,
                    "immediate_selection_match_gain": post_new-baseline_new,
                    "final_new_environment_match": final["mean_environment_match"],
                    "net_adaptation_from_new_environment_baseline":
                        final["mean_environment_match"]-baseline_new,
                    "pre_shift_mean_maintenance": before["mean_maintenance"],
                    "immediate_post_shift_mean_maintenance": after["mean_maintenance"],
                    "final_mean_maintenance": final["mean_maintenance"],
                })

        return {
            "initial_seed": self.initial_seed,
            "frames": len(self.frames),
            "final_population": len(self.final_units),
            "max_population": max_pop,
            "environment_shifts": shifts,
            "selection_deaths": selections,
            "fission_events": fissions,
            "mutation_events": mutations,
            "core_steps": self.core_steps,
            "successful_reclosures": self.successful_reclosures,
            "spectrally_novel_reclosures": self.novel_reclosures,
            "shift_response": before_after,
        }


def standard_shift_program(shift_generation: int = 30) -> EnvironmentProgram:
    calm = EnvironmentState(
        name="resource_rich_connected",
        resource_supply=0.92,
        disturbance=0.015,
        carrying_capacity=8,
        match_weight=0.38,
        preferred_traits={
            "formation_drive": 1.34,
            "neighbor_scale": 0.38,
            "resource_blend": 0.22,
            "topology_blend": 0.14,
            "export_cost": 0.12,
            "node_birth_threshold": 0.92,
            "fission_threshold": 0.235,
        },
    )
    stressed = EnvironmentState(
        name="resource_poor_fragmenting",
        resource_supply=0.48,
        disturbance=0.20,
        carrying_capacity=4,
        match_weight=0.52,
        preferred_traits={
            "formation_drive": 1.63,
            "neighbor_scale": 0.25,
            "resource_blend": 0.43,
            "topology_blend": 0.31,
            "export_cost": 0.055,
            "node_birth_threshold": 0.72,
            "fission_threshold": 0.185,
        },
    )
    return EnvironmentProgram(phases=((0, calm), (int(shift_generation), stressed)))


def seasonal_program(period: int = 24, generations: int = 96) -> EnvironmentProgram:
    """
    Piecewise seasonal approximation with alternating rich/calm and poor/disturbed
    phases. It is intentionally discrete so environmental transitions are auditable.
    """
    if period < 4:
        raise ValueError("period must be >= 4")
    half = period // 2
    rich = EnvironmentState(
        name="season_rich",
        resource_supply=0.95,
        disturbance=0.02,
        carrying_capacity=8,
        match_weight=0.35,
        preferred_traits={
            "neighbor_scale": 0.37,
            "resource_blend": 0.23,
            "topology_blend": 0.15,
            "export_cost": 0.115,
        },
    )
    poor = EnvironmentState(
        name="season_poor",
        resource_supply=0.52,
        disturbance=0.16,
        carrying_capacity=5,
        match_weight=0.46,
        preferred_traits={
            "neighbor_scale": 0.26,
            "resource_blend": 0.40,
            "topology_blend": 0.29,
            "export_cost": 0.065,
        },
    )
    phases = []
    g = 0
    toggle = False
    while g <= generations:
        phases.append((g, poor if toggle else rich))
        toggle = not toggle
        g += half
    return EnvironmentProgram(phases=tuple(phases))


def trait_match(traits: dict[str, float], env: EnvironmentState) -> float:
    if not env.preferred_traits:
        return 1.0
    errors = []
    for key, target in env.preferred_traits.items():
        lo, hi = TRAIT_BOUNDS[key]
        span = max(hi-lo, 1e-12)
        # 0.25 of the allowed trait span is one environmental mismatch scale.
        z = abs(float(traits[key])-float(target)) / (0.25*span)
        errors.append(z*z)
    mse = float(np.mean(errors))
    return float(np.exp(-0.5*mse))


def environmental_fitness(
    unit: EvolutionUnit,
    org: SelfOrganizationParameters,
    evo: EvolutionParameters,
    env: EnvironmentState,
) -> tuple[float, float, float]:
    intrinsic = _fitness(unit, org, evo)
    match = trait_match(unit.traits, env)
    score = (1.0-env.match_weight)*intrinsic + env.match_weight*match
    return float(score), float(intrinsic), float(match)


def apply_environment(
    state: BFGState,
    env: EnvironmentState,
    org: SelfOrganizationParameters,
    rng: np.random.Generator,
) -> tuple[BFGState, dict]:
    """
    Apply environmental forcing before the next BFG reclosure.

    Resource supply acts continuously. Disturbance affects a symmetric random
    fraction of existing edges and a position-dependent resource exposure field.
    The forced carrier is then rebuilt through the same K/Y/R_C constructors.
    """
    positions = np.asarray(state.metadata["positions"], dtype=float)
    A = np.asarray(state.metadata["adjacency"], dtype=float).copy()
    resource = np.asarray(state.metadata["resource"], dtype=float).copy()
    D = np.asarray(state.D, dtype=complex).copy()
    n = len(resource)

    # Resource forcing: rich environments replenish; poor environments drain.
    supply = float(env.resource_supply)
    if supply >= 1.0:
        resource = resource + 0.10*(supply-1.0)*(1.0-resource)
    else:
        resource = resource * (0.82 + 0.18*supply)

    # Spatially structured exposure means the same environmental shock does not
    # affect every node identically.
    phase = 2*np.pi*(positions[:,0] + 0.37*positions[:,1])
    exposure = 0.5 + 0.5*np.sin(phase)
    resource *= (1.0 - 0.22*env.disturbance*exposure)
    resource = np.clip(resource, 0.0, 1.0)

    # Symmetric edge disturbance.
    damaged_edges = 0
    if env.disturbance > 0 and n > 1:
        upper = rng.random((n,n))
        upper = np.triu(upper, 1)
        damage = upper < (env.disturbance*env.perturbation_fraction)
        damage = np.triu(damage, 1)
        damage = damage | damage.T
        existing = A > 0
        mask = damage & existing
        damaged_edges = int(np.count_nonzero(np.triu(mask,1)))
        A[mask] *= (1.0 - 0.65*env.disturbance)
        A = np.clip(0.5*(A+A.T), 0.0, 1.0)
        np.fill_diagonal(A, 0.0)

    # Preserve phases while changing amplitudes with the forced resource field.
    phase_D = np.angle(D + 1e-15)
    D_forced = resource*np.exp(1j*phase_D)

    forced = _rebuild_state(
        state, positions, A, resource, D_forced, org,
        name=f"{state.name}_env_{env.name}"
    )
    forced.generation = state.generation
    return forced, {
        "environment": env.name,
        "resource_supply": supply,
        "disturbance": float(env.disturbance),
        "mean_resource_before": float(np.mean(state.metadata["resource"])),
        "mean_resource_after": float(np.mean(resource)),
        "damaged_edges": damaged_edges,
    }


def _environment_frame(
    generation: int,
    units: dict[str, EvolutionUnit],
    base_org: SelfOrganizationParameters,
    evo: EvolutionParameters,
    env: EnvironmentState,
) -> tuple[dict, dict]:
    if not units:
        return (
            {
                "generation": generation,
                "population_size": 0,
                "total_nodes": 0,
                "mean_environment_fitness": 0.0,
                "mean_intrinsic_fitness": 0.0,
                "mean_environment_match": 0.0,
                "mean_maintenance": 0.0,
                "environment": env.name,
            },
            {"generation": generation, "environment": env.name},
        )

    scores = []
    intrinsic = []
    matches = []
    maintenance = []
    nodes = []
    trait_values = {k: [] for k in TRAIT_BOUNDS}
    for u in units.values():
        org = traits_to_org(base_org, u.traits, u.state.dim)
        s, i, m = environmental_fitness(u, org, evo, env)
        scores.append(s)
        intrinsic.append(i)
        matches.append(m)
        maintenance.append(organization_metrics(u.state, org)["maintenance_score"])
        nodes.append(u.state.dim)
        for key in TRAIT_BOUNDS:
            trait_values[key].append(float(u.traits[key]))

    frame = {
        "generation": generation,
        "population_size": len(units),
        "total_nodes": int(sum(nodes)),
        "mean_unit_nodes": float(np.mean(nodes)),
        "mean_environment_fitness": float(np.mean(scores)),
        "max_environment_fitness": float(np.max(scores)),
        "mean_intrinsic_fitness": float(np.mean(intrinsic)),
        "mean_environment_match": float(np.mean(matches)),
        "mean_maintenance": float(np.mean(maintenance)),
        "environment": env.name,
        "resource_supply": float(env.resource_supply),
        "disturbance": float(env.disturbance),
        "carrying_capacity": int(env.carrying_capacity),
    }
    traits = {"generation": generation, "environment": env.name}
    for key, vals in trait_values.items():
        traits[f"{key}_mean"] = float(np.mean(vals))
        traits[f"{key}_std"] = float(np.std(vals))
        if key in env.preferred_traits:
            traits[f"{key}_target"] = float(env.preferred_traits[key])
    return frame, traits


def simulate_environmental_evolution(
    seed: int = 1341550191,
    generations: int = 72,
    program: EnvironmentProgram | None = None,
    base_org: SelfOrganizationParameters | None = None,
    base_pop: PopulationParameters | None = None,
    evo: EvolutionParameters | None = None,
    founder_count: int = 12,
    founder_sigma: float = 0.16,
    policy: NumericalPolicy | None = None,
) -> EnvironmentalEvolutionRun:
    program = program or standard_shift_program(shift_generation=30)
    base_org = base_org or SelfOrganizationParameters(node_count=24, persistent_rank=6)
    base_pop = base_pop or PopulationParameters(
        min_unit_nodes=4,
        max_unit_nodes=42,
        max_population=64,
        node_birth_threshold=0.84,
    )
    evo = evo or EvolutionParameters(
        mutation_rate=0.85,
        mutation_sigma=0.055,
        carrying_capacity=12,
        max_candidate_population=24,
        minimum_reproductive_age=4,
    )
    policy = policy or NumericalPolicy()

    base_org.validate()
    base_pop.validate()
    evo.validate()
    if founder_count < 1:
        raise ValueError("founder_count must be positive")

    rng = np.random.default_rng(seed + 27191)
    initial = make_self_organizing_seed(seed=seed, params=base_org)
    root_traits = default_traits(base_org, base_pop)

    # Standing variation: founders share one structural ancestry but receive
    # bounded heritable variation before environmental filtering begins.
    units: dict[str, EvolutionUnit] = {}
    events = []
    for i in range(founder_count):
        uid = f"A{i}"
        traits = dict(root_traits)
        changes = []
        if i > 0:
            for key, (lo, hi) in TRAIT_BOUNDS.items():
                before = traits[key]
                after = float(np.clip(
                    before + rng.normal(0.0, founder_sigma*(hi-lo)), lo, hi
                ))
                traits[key] = after
                if abs(after-before) > 1e-12:
                    changes.append({
                        "trait": key, "before": before, "after": after,
                        "delta": after-before,
                    })

        org = traits_to_org(base_org, traits, initial.dim)
        st = copy.deepcopy(initial)
        st = _rebuild_with_traits(st, org, name=f"{uid}_g0")
        st.generation = 0
        units[uid] = EvolutionUnit(
            unit_id=uid, state=st, traits=traits,
            parent_id=None, birth_generation=0, age=0, lineage_depth=0
        )
        events.append({
            "event": "unit_birth", "unit_id": uid, "parent_id": None,
            "generation": 0, "reason": "founder_variation",
            "traits": traits,
        })
        if changes:
            events.append({
                "event": "standing_variation", "unit_id": uid,
                "generation": 0, "changes": changes,
            })

    next_id = founder_count
    env0 = program.at(0)
    frame0, trait0 = _environment_frame(0, units, base_org, evo, env0)
    frames = [frame0]
    trait_history = [trait0]
    env_history = [{
        "generation": 0,
        "name": env0.name,
        "resource_supply": env0.resource_supply,
        "disturbance": env0.disturbance,
        "carrying_capacity": env0.carrying_capacity,
        "preferred_traits": env0.preferred_traits,
    }]
    core_steps = successful = novel = 0
    last_env_name = env0.name

    for generation in range(1, int(generations)+1):
        env = program.at(generation)
        if env.name != last_env_name:
            events.append({
                "event": "environment_shift",
                "generation": generation,
                "from": last_env_name,
                "to": env.name,
                "resource_supply": env.resource_supply,
                "disturbance": env.disturbance,
                "carrying_capacity": env.carrying_capacity,
                "preferred_traits": env.preferred_traits,
            })
            last_env_name = env.name

        env_history.append({
            "generation": generation,
            "name": env.name,
            "resource_supply": env.resource_supply,
            "disturbance": env.disturbance,
            "carrying_capacity": env.carrying_capacity,
            "preferred_traits": env.preferred_traits,
        })

        if not units:
            frame, traits = _environment_frame(generation, units, base_org, evo, env)
            frames.append(frame)
            trait_history.append(traits)
            break

        candidates: dict[str, EvolutionUnit] = {}

        for unit_id, unit in list(units.items()):
            org = traits_to_org(base_org, unit.traits, unit.state.dim)
            pop = traits_to_pop(base_pop, unit.traits)

            forced, forcing = apply_environment(unit.state, env, org, rng)
            forced.generation = generation-1
            if env.disturbance > 0.08:
                events.append({
                    "event": "environmental_forcing",
                    "unit_id": unit_id,
                    "generation": generation,
                    **forcing,
                })

            carrier = SelfOrganizingNetworkCarrier(org)
            step = canonical_reclosure(forced, policy)
            core_steps += 1
            if step.success:
                successful += 1
            if step.spectral_novelty:
                novel += 1

            if not step.success:
                events.append({
                    "event": "unit_death",
                    "unit_id": unit_id,
                    "generation": generation,
                    "reason": step.terminal_reason or "formation_failure",
                    "environment": env.name,
                    "age": unit.age,
                })
                continue

            evolved = carrier.advance(forced, step, policy)
            evolved.generation = generation
            if evolved.terminal:
                events.append({
                    "event": "unit_death", "unit_id": unit_id,
                    "generation": generation,
                    "reason": evolved.terminal_reason or "carrier_failure",
                    "environment": env.name,
                })
                continue

            evolved, dim_events = _dimension_update(
                evolved, org, pop, rng, unit_id
            )
            evolved.generation = generation
            events.extend(dim_events)

            components = _viable_components(evolved, pop)
            can_reproduce = unit.age + 1 >= evo.minimum_reproductive_age
            projected = len(candidates) + len(components)

            if (
                can_reproduce and len(components) >= 2
                and projected <= evo.max_candidate_population
            ):
                child_ids = []
                for idx in components:
                    cid = f"A{next_id}"
                    next_id += 1
                    child_traits, changes = mutate_traits(unit.traits, rng, evo)
                    raw = _substate(
                        evolved, idx, org, child_name=f"{cid}_raw_g{generation}"
                    )
                    child_org = traits_to_org(base_org, child_traits, raw.dim)
                    child_state = _rebuild_with_traits(
                        raw, child_org, name=f"{cid}_g{generation}"
                    )
                    child_state.generation = generation
                    candidates[cid] = EvolutionUnit(
                        unit_id=cid, state=child_state, traits=child_traits,
                        parent_id=unit_id, birth_generation=generation,
                        age=0, lineage_depth=unit.lineage_depth+1,
                        last_novelty=float(step.spectral_mismatch or 0.0),
                    )
                    child_ids.append(cid)
                    events.append({
                        "event": "unit_birth", "unit_id": cid,
                        "parent_id": unit_id, "generation": generation,
                        "reason": "fission_child", "traits": child_traits,
                        "environment": env.name,
                    })
                    if changes:
                        events.append({
                            "event": "mutation", "unit_id": cid,
                            "parent_id": unit_id, "generation": generation,
                            "changes": changes, "environment": env.name,
                        })

                events.append({
                    "event": "fission", "unit_id": unit_id,
                    "generation": generation, "children": child_ids,
                    "environment": env.name,
                })
                continue

            candidates[unit_id] = EvolutionUnit(
                unit_id=unit_id, state=evolved, traits=dict(unit.traits),
                parent_id=unit.parent_id, birth_generation=unit.birth_generation,
                age=unit.age+1, lineage_depth=unit.lineage_depth,
                last_novelty=float(step.spectral_mismatch or 0.0),
                cumulative_offspring=unit.cumulative_offspring,
            )

        # Environmental carrying capacity creates differential survival.
        capacity = min(env.carrying_capacity, evo.carrying_capacity)
        if len(candidates) > capacity:
            ranked = []
            for uid, u in candidates.items():
                org = traits_to_org(base_org, u.traits, u.state.dim)
                score, intrinsic, match = environmental_fitness(u, org, evo, env)
                ranked.append((score, intrinsic, match, uid, u))
            ranked.sort(key=lambda x: x[0], reverse=True)

            # Record pre-selection mean match so adaptation can distinguish
            # environmental response from the selection step itself.
            pre_match = float(np.mean([r[2] for r in ranked]))
            keep = {uid for _, _, _, uid, _ in ranked[:capacity]}
            post_match = float(np.mean([r[2] for r in ranked if r[3] in keep]))

            events.append({
                "event": "selection_round",
                "generation": generation,
                "environment": env.name,
                "candidate_count": len(ranked),
                "survivor_count": capacity,
                "mean_match_before_selection": pre_match,
                "mean_match_after_selection": post_match,
                "match_gain": post_match-pre_match,
            })

            for score, intrinsic, match, uid, u in ranked:
                if uid not in keep:
                    events.append({
                        "event": "selection_death",
                        "unit_id": uid,
                        "generation": generation,
                        "environment": env.name,
                        "environmental_fitness": score,
                        "intrinsic_fitness": intrinsic,
                        "environment_match": match,
                        "traits": u.traits,
                    })
            candidates = {uid: u for uid, u in candidates.items() if uid in keep}

        units = candidates
        frame, traits = _environment_frame(generation, units, base_org, evo, env)
        frames.append(frame)
        trait_history.append(traits)

    return EnvironmentalEvolutionRun(
        initial_seed=seed,
        frames=frames,
        environment_history=env_history,
        trait_history=trait_history,
        events=events,
        final_units=units,
        core_steps=core_steps,
        successful_reclosures=successful,
        novel_reclosures=novel,
        shift_generations=program.shift_generations,
    )


def write_environmental_report(
    run: EnvironmentalEvolutionRun,
    outdir: str | Path,
    stem: str = "environmental_evolution",
) -> dict[str, str]:
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    frame_fields = sorted({k for row in run.frames for k in row.keys()})
    frames_csv = outdir / f"{stem}_frames.csv"
    with frames_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=frame_fields)
        w.writeheader()
        w.writerows(run.frames)

    trait_fields = sorted({k for row in run.trait_history for k in row.keys()})
    traits_csv = outdir / f"{stem}_traits.csv"
    with traits_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=trait_fields)
        w.writeheader()
        w.writerows(run.trait_history)

    events_json = outdir / f"{stem}_events.json"
    events_json.write_text(json.dumps(run.events, indent=2), encoding="utf-8")
    environment_json = outdir / f"{stem}_environment.json"
    environment_json.write_text(
        json.dumps(run.environment_history, indent=2), encoding="utf-8"
    )
    summary_json = outdir / f"{stem}_summary.json"
    summary_json.write_text(
        json.dumps(run.summary(), indent=2), encoding="utf-8"
    )

    g = np.array([f["generation"] for f in run.frames], dtype=float)
    pop = np.array([f["population_size"] for f in run.frames], dtype=float)
    match = np.array([f["mean_environment_match"] for f in run.frames], dtype=float)
    maintenance = np.array([f["mean_maintenance"] for f in run.frames], dtype=float)
    disturbance = np.array([f["disturbance"] for f in run.frames], dtype=float)

    adaptation_plot = outdir / f"{stem}_adaptation.png"
    fig, ax1 = plt.subplots(figsize=(8.2, 4.9))
    ax1.plot(g, match, label="mean environment match", marker="o", markersize=2.8)
    ax1.plot(g, maintenance, label="mean maintenance", marker="s", markersize=2.5)
    ax1.set_xlabel("Generation")
    ax1.set_ylabel("Adaptation / maintenance")
    ax2 = ax1.twinx()
    ax2.plot(g, disturbance, linestyle="--", label="environment disturbance")
    ax2.set_ylabel("Disturbance")
    for sg in run.shift_generations:
        ax1.axvline(sg, linestyle=":", linewidth=1.0)
    lines = ax1.get_lines() + ax2.get_lines()
    ax1.legend(lines, [ln.get_label() for ln in lines], loc="best", fontsize=8)
    ax1.set_title("BFG environmental response and adaptation")
    fig.tight_layout()
    fig.savefig(adaptation_plot, dpi=165)
    plt.close(fig)

    population_plot = outdir / f"{stem}_population.png"
    plt.figure(figsize=(7.8, 4.6))
    plt.plot(g, pop, marker="o", markersize=3)
    for sg in run.shift_generations:
        plt.axvline(sg, linestyle=":", linewidth=1.0)
    plt.xlabel("Generation")
    plt.ylabel("Independent units")
    plt.title("Population under changing environment")
    plt.tight_layout()
    plt.savefig(population_plot, dpi=165)
    plt.close()

    # Trait-to-target trajectories, normalized by trait range.
    trait_plot = outdir / f"{stem}_trait_tracking.png"
    plt.figure(figsize=(8.5, 5.2))
    keys = ["neighbor_scale", "resource_blend", "topology_blend", "export_cost"]
    for key in keys:
        lo, hi = TRAIT_BOUNDS[key]
        vals = np.array([
            row.get(f"{key}_mean", np.nan) for row in run.trait_history
        ], dtype=float)
        target = np.array([
            next(
                (
                    row.get(f"{key}_target", np.nan)
                    for row in [run.trait_history[i]]
                ),
                np.nan,
            )
            for i in range(len(run.trait_history))
        ], dtype=float)
        plt.plot(g, (vals-lo)/(hi-lo), label=f"{key}: population")
        plt.plot(g, (target-lo)/(hi-lo), linestyle="--", alpha=0.6,
                 label=f"{key}: environment")
    plt.xlabel("Generation")
    plt.ylabel("Normalized trait / environmental target")
    plt.title("Heritable trait tracking under environmental change")
    plt.legend(fontsize=7, ncol=2)
    plt.tight_layout()
    plt.savefig(trait_plot, dpi=165)
    plt.close()

    return {
        "frames_csv": str(frames_csv),
        "traits_csv": str(traits_csv),
        "events_json": str(events_json),
        "environment_json": str(environment_json),
        "summary_json": str(summary_json),
        "adaptation_plot": str(adaptation_plot),
        "population_plot": str(population_plot),
        "trait_tracking_plot": str(trait_plot),
    }
