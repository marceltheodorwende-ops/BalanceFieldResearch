from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import csv
import json
import math
import numpy as np
import matplotlib.pyplot as plt

from .types import BFGState, NumericalPolicy
from .core import canonical_reclosure
from .alife import SelfOrganizationParameters, SelfOrganizingNetworkCarrier, organization_metrics
from .population import (
    PopulationParameters,
    _dimension_update,
    _viable_components,
    _substate,
    _rebuild_state,
)
from .alife import make_self_organizing_seed


TRAIT_BOUNDS = {
    "formation_drive": (1.05, 1.90),
    "neighbor_scale": (0.20, 0.46),
    "resource_blend": (0.12, 0.50),
    "topology_blend": (0.08, 0.38),
    "export_cost": (0.03, 0.18),
    "node_birth_threshold": (0.62, 1.05),
    "fission_threshold": (0.16, 0.30),
}


@dataclass(frozen=True)
class EvolutionParameters:
    mutation_rate: float = 0.75
    mutation_sigma: float = 0.055
    carrying_capacity: int = 12
    selection_pressure: float = 1.0
    max_candidate_population: int = 24
    minimum_reproductive_age: int = 5
    age_bonus_scale: float = 0.08
    novelty_bonus_scale: float = 0.06

    def validate(self):
        if not (0 <= self.mutation_rate <= 1):
            raise ValueError("mutation_rate must lie in [0,1]")
        if self.mutation_sigma < 0:
            raise ValueError("mutation_sigma must be nonnegative")
        if self.carrying_capacity < 1:
            raise ValueError("carrying_capacity must be positive")
        if self.max_candidate_population < self.carrying_capacity:
            raise ValueError("max_candidate_population must be >= carrying_capacity")
        if self.minimum_reproductive_age < 0:
            raise ValueError("minimum_reproductive_age must be nonnegative")


@dataclass
class EvolutionUnit:
    unit_id: str
    state: BFGState
    traits: dict[str, float]
    parent_id: str | None = None
    birth_generation: int = 0
    age: int = 0
    lineage_depth: int = 0
    last_novelty: float = 0.0
    cumulative_offspring: int = 0


@dataclass
class EvolutionRun:
    initial_seed: int
    frames: list[dict]
    events: list[dict]
    final_units: dict[str, EvolutionUnit]
    trait_history: list[dict]
    core_steps: int
    successful_reclosures: int
    novel_reclosures: int

    def summary(self) -> dict:
        births = sum(e["event"] == "unit_birth" for e in self.events)
        fissions = sum(e["event"] == "fission" for e in self.events)
        mutations = sum(e["event"] == "mutation" for e in self.events)
        selections = sum(e["event"] == "selection_death" for e in self.events)
        intrinsic_deaths = sum(e["event"] == "unit_death" for e in self.events)
        max_population = max((f["population_size"] for f in self.frames), default=0)
        max_depth = max((u.lineage_depth for u in self.final_units.values()), default=0)
        return {
            "initial_seed": self.initial_seed,
            "frames": len(self.frames),
            "final_population": len(self.final_units),
            "max_population": max_population,
            "max_lineage_depth": max_depth,
            "unit_birth_events": births,
            "fission_events": fissions,
            "mutation_events": mutations,
            "selection_deaths": selections,
            "intrinsic_deaths": intrinsic_deaths,
            "core_steps": self.core_steps,
            "successful_reclosures": self.successful_reclosures,
            "spectrally_novel_reclosures": self.novel_reclosures,
        }


def default_traits(
    org: SelfOrganizationParameters,
    pop: PopulationParameters,
) -> dict[str, float]:
    return {
        "formation_drive": float(org.formation_drive),
        "neighbor_scale": float(org.neighbor_scale),
        "resource_blend": float(org.resource_blend),
        "topology_blend": float(org.topology_blend),
        "export_cost": float(org.export_cost),
        "node_birth_threshold": float(pop.node_birth_threshold),
        "fission_threshold": float(pop.fission_threshold),
    }


def mutate_traits(
    traits: dict[str, float],
    rng: np.random.Generator,
    evo: EvolutionParameters,
) -> tuple[dict[str, float], list[dict]]:
    child = dict(traits)
    changes = []
    for key, (lo, hi) in TRAIT_BOUNDS.items():
        if rng.random() > evo.mutation_rate:
            continue
        span = hi - lo
        before = float(child[key])
        after = float(np.clip(before + rng.normal(0.0, evo.mutation_sigma * span), lo, hi))
        child[key] = after
        if abs(after-before) > 1e-12:
            changes.append({
                "trait": key,
                "before": before,
                "after": after,
                "delta": after-before,
            })
    return child, changes


def traits_to_org(
    base: SelfOrganizationParameters,
    traits: dict[str, float],
    node_count: int,
) -> SelfOrganizationParameters:
    return SelfOrganizationParameters(
        node_count=int(node_count),
        persistent_rank=min(base.persistent_rank, int(node_count)),
        neighbor_scale=float(traits["neighbor_scale"]),
        edge_threshold=base.edge_threshold,
        resource_blend=float(traits["resource_blend"]),
        topology_blend=float(traits["topology_blend"]),
        export_cost=float(traits["export_cost"]),
        basal_recovery=base.basal_recovery,
        load_scale=base.load_scale,
        stress_scale=base.stress_scale,
        formation_drive=float(traits["formation_drive"]),
        formation_offset=base.formation_offset,
        contraction=base.contraction,
        phase_scale=base.phase_scale,
        cluster_threshold=base.cluster_threshold,
        viability_threshold=base.viability_threshold,
    )


def traits_to_pop(
    base: PopulationParameters,
    traits: dict[str, float],
) -> PopulationParameters:
    return PopulationParameters(
        min_unit_nodes=base.min_unit_nodes,
        max_unit_nodes=base.max_unit_nodes,
        fission_threshold=float(traits["fission_threshold"]),
        fission_min_resource=base.fission_min_resource,
        max_children_per_fission=base.max_children_per_fission,
        max_population=base.max_population,
        node_death_threshold=base.node_death_threshold,
        node_birth_threshold=float(traits["node_birth_threshold"]),
        max_node_births_per_step=base.max_node_births_per_step,
        birth_resource_fraction=base.birth_resource_fraction,
        birth_position_jitter=base.birth_position_jitter,
        birth_phase_jitter=base.birth_phase_jitter,
    )


def _fitness(
    unit: EvolutionUnit,
    org: SelfOrganizationParameters,
    evo: EvolutionParameters,
) -> float:
    m = organization_metrics(unit.state, org)
    maintenance = float(m["maintenance_score"])
    viable = float(m["viable_fraction"])
    entropy = float(m["resource_entropy"])
    connectivity = float(np.tanh(max(0.0, m["algebraic_connectivity"])))
    age_term = evo.age_bonus_scale * min(unit.age / 12.0, 1.0)
    novelty_term = evo.novelty_bonus_scale * math.tanh(max(0.0, unit.last_novelty) * 100.0)

    # Compact viability/organization score. This is a carrier-level selection
    # observable, not a universal BFG theorem.
    return float(
        0.50*maintenance
        + 0.18*viable
        + 0.15*entropy
        + 0.09*connectivity
        + age_term
        + novelty_term
    )


def _rebuild_with_traits(
    state: BFGState,
    org: SelfOrganizationParameters,
    name: str,
) -> BFGState:
    return _rebuild_state(
        state,
        np.asarray(state.metadata["positions"], dtype=float),
        np.asarray(state.metadata["adjacency"], dtype=float),
        np.asarray(state.metadata["resource"], dtype=float),
        np.asarray(state.D, dtype=complex),
        org,
        name=name,
    )


def _frame(
    generation: int,
    units: dict[str, EvolutionUnit],
    base_org: SelfOrganizationParameters,
    evo: EvolutionParameters,
) -> tuple[dict, dict]:
    if not units:
        empty = {
            "generation": generation,
            "population_size": 0,
            "total_nodes": 0,
            "mean_fitness": 0.0,
            "mean_age": 0.0,
            "mean_lineage_depth": 0.0,
        }
        return empty, {"generation": generation}

    fitness = []
    sizes = []
    ages = []
    depths = []
    trait_matrix = {k: [] for k in TRAIT_BOUNDS}
    for u in units.values():
        org = traits_to_org(base_org, u.traits, u.state.dim)
        fitness.append(_fitness(u, org, evo))
        sizes.append(u.state.dim)
        ages.append(u.age)
        depths.append(u.lineage_depth)
        for k in trait_matrix:
            trait_matrix[k].append(float(u.traits[k]))

    frame = {
        "generation": generation,
        "population_size": len(units),
        "total_nodes": int(sum(sizes)),
        "mean_unit_nodes": float(np.mean(sizes)),
        "mean_fitness": float(np.mean(fitness)),
        "max_fitness": float(np.max(fitness)),
        "mean_age": float(np.mean(ages)),
        "mean_lineage_depth": float(np.mean(depths)),
        "max_lineage_depth": int(max(depths)),
    }
    traits = {"generation": generation}
    for k, vals in trait_matrix.items():
        traits[f"{k}_mean"] = float(np.mean(vals))
        traits[f"{k}_std"] = float(np.std(vals))
    return frame, traits


def simulate_evolution(
    seed: int = 1341550191,
    generations: int = 90,
    base_org: SelfOrganizationParameters | None = None,
    base_pop: PopulationParameters | None = None,
    evo: EvolutionParameters | None = None,
    policy: NumericalPolicy | None = None,
) -> EvolutionRun:
    base_org = base_org or SelfOrganizationParameters()
    base_pop = base_pop or PopulationParameters(
        min_unit_nodes=4,
        max_unit_nodes=42,
        max_population=64,
        node_birth_threshold=0.82,
    )
    evo = evo or EvolutionParameters()
    policy = policy or NumericalPolicy()

    base_org.validate()
    base_pop.validate()
    evo.validate()

    rng = np.random.default_rng(seed + 19073)
    initial = make_self_organizing_seed(seed=seed, params=base_org)
    root_traits = default_traits(base_org, base_pop)

    units: dict[str, EvolutionUnit] = {
        "E0": EvolutionUnit(
            unit_id="E0",
            state=initial,
            traits=root_traits,
            parent_id=None,
            birth_generation=0,
            age=0,
            lineage_depth=0,
        )
    }
    next_id = 1
    events = [{
        "event": "unit_birth",
        "unit_id": "E0",
        "parent_id": None,
        "generation": 0,
        "lineage_depth": 0,
        "traits": root_traits,
        "reason": "initial_seed",
    }]
    frame0, traits0 = _frame(0, units, base_org, evo)
    frames = [frame0]
    trait_history = [traits0]
    core_steps = successful = novel = 0

    for generation in range(1, int(generations)+1):
        if not units:
            f, t = _frame(generation, units, base_org, evo)
            frames.append(f)
            trait_history.append(t)
            break

        candidates: dict[str, EvolutionUnit] = {}

        for unit_id, unit in list(units.items()):
            org = traits_to_org(base_org, unit.traits, unit.state.dim)
            pop = traits_to_pop(base_pop, unit.traits)
            carrier = SelfOrganizingNetworkCarrier(org)

            step = canonical_reclosure(unit.state, policy)
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
                    "age": unit.age,
                    "lineage_depth": unit.lineage_depth,
                })
                continue

            evolved = carrier.advance(unit.state, step, policy)
            evolved.generation = generation
            if evolved.terminal:
                events.append({
                    "event": "unit_death",
                    "unit_id": unit_id,
                    "generation": generation,
                    "reason": evolved.terminal_reason or "carrier_failure",
                    "age": unit.age,
                    "lineage_depth": unit.lineage_depth,
                })
                continue

            evolved, dim_events = _dimension_update(
                evolved, org, pop, rng, unit_id
            )
            evolved.generation = generation
            for e in dim_events:
                events.append(e)

            if evolved.dim < pop.min_unit_nodes:
                events.append({
                    "event": "unit_death",
                    "unit_id": unit_id,
                    "generation": generation,
                    "reason": "below_minimum_unit_size",
                    "age": unit.age,
                    "lineage_depth": unit.lineage_depth,
                })
                continue

            components = _viable_components(evolved, pop)
            can_reproduce = unit.age + 1 >= evo.minimum_reproductive_age
            projected = len(candidates) + len(components)

            if (
                can_reproduce
                and len(components) >= 2
                and projected <= evo.max_candidate_population
            ):
                child_ids = []
                child_sizes = []
                for idx in components:
                    cid = f"E{next_id}"
                    next_id += 1

                    child_traits, changes = mutate_traits(unit.traits, rng, evo)

                    # First inherit the structural subset, then rebuild K,Y,R_C
                    # under the child's inherited/mutated carrier traits.
                    parent_child = _substate(
                        evolved, idx, org, child_name=f"{cid}_raw_g{generation}"
                    )
                    child_org = traits_to_org(base_org, child_traits, parent_child.dim)
                    child_state = _rebuild_with_traits(
                        parent_child, child_org, name=f"{cid}_g{generation}"
                    )
                    child_state.generation = generation

                    child = EvolutionUnit(
                        unit_id=cid,
                        state=child_state,
                        traits=child_traits,
                        parent_id=unit_id,
                        birth_generation=generation,
                        age=0,
                        lineage_depth=unit.lineage_depth+1,
                        last_novelty=float(step.spectral_mismatch or 0.0),
                    )
                    candidates[cid] = child
                    child_ids.append(cid)
                    child_sizes.append(child_state.dim)

                    events.append({
                        "event": "unit_birth",
                        "unit_id": cid,
                        "parent_id": unit_id,
                        "generation": generation,
                        "lineage_depth": child.lineage_depth,
                        "node_count": child_state.dim,
                        "traits": child_traits,
                        "reason": "fission_child",
                    })
                    if changes:
                        events.append({
                            "event": "mutation",
                            "unit_id": cid,
                            "parent_id": unit_id,
                            "generation": generation,
                            "changes": changes,
                        })

                events.append({
                    "event": "fission",
                    "unit_id": unit_id,
                    "generation": generation,
                    "children": child_ids,
                    "child_sizes": child_sizes,
                    "lineage_depth": unit.lineage_depth,
                })
                continue

            # Identity persists when no fission occurs.
            candidates[unit_id] = EvolutionUnit(
                unit_id=unit_id,
                state=evolved,
                traits=dict(unit.traits),
                parent_id=unit.parent_id,
                birth_generation=unit.birth_generation,
                age=unit.age+1,
                lineage_depth=unit.lineage_depth,
                last_novelty=float(step.spectral_mismatch or 0.0),
                cumulative_offspring=unit.cumulative_offspring,
            )

        # Differential survival under finite carrying capacity.
        if len(candidates) > evo.carrying_capacity:
            ranked = []
            for uid, u in candidates.items():
                org = traits_to_org(base_org, u.traits, u.state.dim)
                ranked.append((_fitness(u, org, evo), uid, u))
            ranked.sort(key=lambda x: x[0], reverse=True)

            # selection_pressure=1 -> strict top-K. Lower pressure mixes a small
            # stochastic component without allowing low-fitness domination.
            if evo.selection_pressure < 1.0:
                fitness = np.array([r[0] for r in ranked], dtype=float)
                floor = np.min(fitness)
                weights = np.maximum(fitness-floor+1e-9, 1e-9)
                alpha = max(0.0, min(1.0, evo.selection_pressure))
                weights = alpha*weights + (1-alpha)*np.ones_like(weights)
                choose = rng.choice(
                    len(ranked),
                    size=evo.carrying_capacity,
                    replace=False,
                    p=weights/np.sum(weights),
                )
                keep = {ranked[int(i)][1] for i in choose}
            else:
                keep = {uid for _, uid, _ in ranked[:evo.carrying_capacity]}

            for score, uid, u in ranked:
                if uid not in keep:
                    events.append({
                        "event": "selection_death",
                        "unit_id": uid,
                        "generation": generation,
                        "fitness": score,
                        "age": u.age,
                        "lineage_depth": u.lineage_depth,
                        "traits": u.traits,
                    })
            candidates = {uid: u for uid, u in candidates.items() if uid in keep}

        units = candidates
        f, t = _frame(generation, units, base_org, evo)
        frames.append(f)
        trait_history.append(t)

    return EvolutionRun(
        initial_seed=seed,
        frames=frames,
        events=events,
        final_units=units,
        trait_history=trait_history,
        core_steps=core_steps,
        successful_reclosures=successful,
        novel_reclosures=novel,
    )


def write_evolution_report(
    run: EvolutionRun,
    outdir: str | Path,
    stem: str = "evolution",
) -> dict[str, str]:
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    frames_csv = outdir / f"{stem}_frames.csv"
    with frames_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(run.frames[0].keys()))
        w.writeheader()
        w.writerows(run.frames)

    traits_csv = outdir / f"{stem}_traits.csv"
    trait_fields = sorted({k for row in run.trait_history for k in row.keys()})
    with traits_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=trait_fields)
        w.writeheader()
        w.writerows(run.trait_history)

    events_json = outdir / f"{stem}_events.json"
    events_json.write_text(json.dumps(run.events, indent=2), encoding="utf-8")

    summary_json = outdir / f"{stem}_summary.json"
    summary_json.write_text(json.dumps(run.summary(), indent=2), encoding="utf-8")

    # Population / fitness trajectory.
    g = np.array([f["generation"] for f in run.frames])
    pop = np.array([f["population_size"] for f in run.frames])
    fit = np.array([f["mean_fitness"] for f in run.frames])
    depth = np.array([f["max_lineage_depth"] for f in run.frames])

    population_plot = outdir / f"{stem}_population.png"
    fig, ax1 = plt.subplots(figsize=(7.8, 4.8))
    ax1.plot(g, pop, marker="o", label="population")
    ax1.plot(g, depth, marker="s", label="max lineage depth")
    ax1.set_xlabel("Generation")
    ax1.set_ylabel("Count / depth")
    ax2 = ax1.twinx()
    ax2.plot(g, fit, linestyle="--", marker="^", label="mean fitness")
    ax2.set_ylabel("Carrier selection score")
    lines = ax1.get_lines() + ax2.get_lines()
    ax1.legend(lines, [x.get_label() for x in lines], loc="best")
    ax1.set_title("BFG evolutionary population trajectory")
    fig.tight_layout()
    fig.savefig(population_plot, dpi=165)
    plt.close(fig)

    # Trait means over time.
    trait_plot = outdir / f"{stem}_traits.png"
    plt.figure(figsize=(8.2, 5.2))
    for key in TRAIT_BOUNDS:
        vals = np.array([
            row.get(f"{key}_mean", np.nan)
            for row in run.trait_history
        ], dtype=float)
        lo, hi = TRAIT_BOUNDS[key]
        normalized = (vals-lo)/(hi-lo)
        plt.plot(g[:len(normalized)], normalized, label=key)
    plt.xlabel("Generation")
    plt.ylabel("Normalized mean heritable trait")
    plt.title("Heritable carrier-trait dynamics")
    plt.legend(fontsize=7, ncol=2)
    plt.tight_layout()
    plt.savefig(trait_plot, dpi=165)
    plt.close()

    # Lineage plot.
    births = [e for e in run.events if e["event"] == "unit_birth"]
    coords = {}
    by_depth = {}
    for e in births:
        by_depth.setdefault(int(e["lineage_depth"]), []).append(e)

    lineage_plot = outdir / f"{stem}_lineage.png"
    plt.figure(figsize=(8.5, 5.5))
    # Stable vertical order by birth time within depth.
    for depth, entries in sorted(by_depth.items()):
        entries = sorted(entries, key=lambda e: (e["generation"], e["unit_id"]))
        for j, e in enumerate(entries):
            x = e["generation"]
            y = depth + 0.06*j
            coords[e["unit_id"]] = (x, y)
            plt.scatter([x], [y], s=50)
    for e in births:
        par = e.get("parent_id")
        uid = e["unit_id"]
        if par is not None and par in coords and uid in coords:
            x0,y0 = coords[par]
            x1,y1 = coords[uid]
            plt.plot([x0,x1],[y0,y1], linewidth=0.9)
    plt.xlabel("Birth generation")
    plt.ylabel("Lineage depth")
    plt.title("BFG inherited-unit lineage")
    plt.tight_layout()
    plt.savefig(lineage_plot, dpi=165)
    plt.close()

    return {
        "frames_csv": str(frames_csv),
        "traits_csv": str(traits_csv),
        "events_json": str(events_json),
        "summary_json": str(summary_json),
        "population_plot": str(population_plot),
        "trait_plot": str(trait_plot),
        "lineage_plot": str(lineage_plot),
    }
