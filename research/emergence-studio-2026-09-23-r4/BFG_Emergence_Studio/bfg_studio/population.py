from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
import csv
import json
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse.csgraph import connected_components

from .types import BFGState, NumericalPolicy
from .core import canonical_reclosure
from .alife import (
    SelfOrganizationParameters,
    SelfOrganizingNetworkCarrier,
    make_self_organizing_seed,
    organization_metrics,
    _formation_operator,
    _neutral_load,
    _recursive_operator,
)


@dataclass(frozen=True)
class PopulationParameters:
    min_unit_nodes: int = 4
    max_unit_nodes: int = 40
    fission_threshold: float = 0.22
    fission_min_resource: float = 0.30
    max_children_per_fission: int = 3
    max_population: int = 32

    # Dimension-changing carrier dynamics.
    node_death_threshold: float = 0.035
    node_birth_threshold: float = 0.88
    max_node_births_per_step: int = 1
    birth_resource_fraction: float = 0.28
    birth_position_jitter: float = 0.025
    birth_phase_jitter: float = 0.08

    def validate(self):
        if self.min_unit_nodes < 2:
            raise ValueError("min_unit_nodes must be >= 2")
        if self.max_unit_nodes < self.min_unit_nodes:
            raise ValueError("max_unit_nodes must be >= min_unit_nodes")
        if self.max_population < 1:
            raise ValueError("max_population must be >= 1")
        if self.max_children_per_fission < 2:
            raise ValueError("max_children_per_fission must be >= 2")
        if not (0 <= self.birth_resource_fraction < 0.5):
            raise ValueError("birth_resource_fraction must be in [0, 0.5)")


@dataclass
class PopulationUnit:
    unit_id: str
    state: BFGState
    parent_id: str | None = None
    birth_generation: int = 0
    age: int = 0
    alive: bool = True
    death_reason: str | None = None


@dataclass
class PopulationRun:
    initial_seed: int
    frames: list[dict]
    events: list[dict]
    final_units: dict[str, PopulationUnit]
    core_steps: int = 0
    successful_reclosures: int = 0
    novel_reclosures: int = 0

    def summary(self) -> dict:
        fissions = sum(e["event"] == "fission" for e in self.events)
        births = sum(e["event"] == "node_birth" for e in self.events)
        losses = sum(e["event"] == "node_loss" for e in self.events)
        deaths = sum(e["event"] == "unit_death" for e in self.events)
        max_pop = max((f["population_size"] for f in self.frames), default=0)
        max_nodes = max((f["total_nodes"] for f in self.frames), default=0)
        return {
            "initial_seed": self.initial_seed,
            "frames": len(self.frames),
            "final_population": len(self.final_units),
            "max_population": max_pop,
            "max_total_nodes": max_nodes,
            "fission_events": fissions,
            "node_birth_events": births,
            "node_loss_events": losses,
            "unit_deaths": deaths,
            "core_steps": self.core_steps,
            "successful_reclosures": self.successful_reclosures,
            "spectrally_novel_reclosures": self.novel_reclosures,
        }


def _rebuild_state(
    template: BFGState,
    positions: np.ndarray,
    adjacency: np.ndarray,
    resource: np.ndarray,
    D: np.ndarray | None,
    org_params: SelfOrganizationParameters,
    name: str,
) -> BFGState:
    n = len(resource)
    if n < 2:
        raise ValueError("a population unit needs at least two nodes")

    adjacency = np.asarray(adjacency, dtype=float)
    adjacency = np.clip(0.5*(adjacency + adjacency.T), 0.0, 1.0)
    np.fill_diagonal(adjacency, 0.0)
    resource = np.clip(np.asarray(resource, dtype=float), 0.0, 1.0)
    positions = np.asarray(positions, dtype=float)

    K = _formation_operator(
        adjacency, resource, org_params.formation_drive, org_params.formation_offset
    )
    Y = _neutral_load(
        adjacency, resource, org_params.load_scale, org_params.stress_scale
    )
    R_C = _recursive_operator(
        adjacency,
        min(org_params.persistent_rank, n),
        org_params.contraction,
        org_params.phase_scale,
    )

    if D is None or len(D) != n:
        D = resource.astype(complex)
    D = np.asarray(D, dtype=complex)
    norm = float(np.linalg.norm(D))
    if norm <= 1e-12:
        D = np.ones(n, dtype=complex) / math.sqrt(n)
    else:
        D = D / norm

    metadata = {
        **template.metadata,
        "positions": positions,
        "adjacency": adjacency,
        "resource": resource,
        "carrier": "PopulationSelfOrganizationCarrier",
        "params": org_params.__dict__.copy(),
        "carrier_scope": "population/fission research model; not an empirical biological law",
    }

    return BFGState(
        D=D, K=K, Y=Y, R_C=R_C,
        generation=template.generation,
        name=name,
        metadata=metadata,
        terminal=False,
        terminal_reason=None,
    )


def _dimension_update(
    state: BFGState,
    org_params: SelfOrganizationParameters,
    pop_params: PopulationParameters,
    rng: np.random.Generator,
    unit_id: str,
) -> tuple[BFGState, list[dict]]:
    """
    Carrier-specific node birth / loss.

    Resource is approximately conserved during birth by splitting a high-resource
    parent node. Node loss removes very low-resource nodes, but never below the
    minimum viable unit size.
    """
    events = []
    positions = np.asarray(state.metadata["positions"], dtype=float).copy()
    A = np.asarray(state.metadata["adjacency"], dtype=float).copy()
    resource = np.asarray(state.metadata["resource"], dtype=float).copy()
    D = np.asarray(state.D, dtype=complex).copy()

    # Loss: only low-resource nodes, never below min_unit_nodes.
    candidates = np.where(resource < pop_params.node_death_threshold)[0].tolist()
    removable = max(0, len(resource) - pop_params.min_unit_nodes)
    if candidates and removable > 0:
        candidates = sorted(candidates, key=lambda i: resource[i])[:removable]
        keep = np.ones(len(resource), dtype=bool)
        keep[candidates] = False
        lost_resource = float(np.sum(resource[~keep]))
        positions = positions[keep]
        A = A[np.ix_(keep, keep)]
        resource = resource[keep]
        D = D[keep]
        events.append({
            "event": "node_loss",
            "unit_id": unit_id,
            "generation": state.generation,
            "count": len(candidates),
            "resource_removed": lost_resource,
        })

    # Birth: duplicate at most a small number of high-resource nodes.
    available = pop_params.max_unit_nodes - len(resource)
    if available > 0 and pop_params.max_node_births_per_step > 0:
        high = np.where(resource >= pop_params.node_birth_threshold)[0]
        if high.size:
            order = high[np.argsort(resource[high])[::-1]]
            births = min(available, pop_params.max_node_births_per_step, len(order))
            for parent in order[:births]:
                parent = int(parent)
                frac = pop_params.birth_resource_fraction
                child_resource = float(resource[parent] * frac)
                resource[parent] *= (1.0-frac)

                angle = rng.uniform(0.0, 2*np.pi)
                offset = pop_params.birth_position_jitter * np.array([np.cos(angle), np.sin(angle)])
                new_pos = np.clip(positions[parent] + offset, 0.0, 1.0)

                old_n = len(resource)
                positions = np.vstack([positions, new_pos])
                resource = np.concatenate([resource, [child_resource]])

                # Inherit parent's relation profile with a small attenuation;
                # make a strong parent-child relation.
                A2 = np.zeros((old_n+1, old_n+1), dtype=float)
                A2[:old_n, :old_n] = A
                inherited = 0.88 * A[parent, :]
                A2[old_n, :old_n] = inherited
                A2[:old_n, old_n] = inherited
                A2[parent, old_n] = A2[old_n, parent] = max(0.72, float(np.max(A[parent])) if old_n > 1 else 0.72)
                np.fill_diagonal(A2, 0.0)
                A = A2

                parent_phase = np.angle(D[parent]) if len(D) > parent else 0.0
                child_phase = parent_phase + rng.normal(0.0, pop_params.birth_phase_jitter)
                D = np.concatenate([D, [child_resource*np.exp(1j*child_phase)]])

                events.append({
                    "event": "node_birth",
                    "unit_id": unit_id,
                    "generation": state.generation,
                    "parent_node": parent,
                    "new_node": old_n,
                    "resource_allocated": child_resource,
                })

    rebuilt = _rebuild_state(
        state, positions, A, resource, D, org_params,
        name=f"{state.name}_dimension_updated"
    )
    return rebuilt, events


def _viable_components(
    state: BFGState,
    pop_params: PopulationParameters,
) -> list[np.ndarray]:
    A = np.asarray(state.metadata["adjacency"], dtype=float)
    resource = np.asarray(state.metadata["resource"], dtype=float)
    graph = (A >= pop_params.fission_threshold).astype(int)
    np.fill_diagonal(graph, 0)
    count, labels = connected_components(graph, directed=False, connection="weak")
    comps = []
    for k in range(count):
        idx = np.where(labels == k)[0]
        if len(idx) < pop_params.min_unit_nodes:
            continue
        if float(np.mean(resource[idx])) < pop_params.fission_min_resource:
            continue
        comps.append(idx)
    comps.sort(key=lambda idx: (len(idx), float(np.sum(resource[idx]))), reverse=True)
    return comps[:pop_params.max_children_per_fission]


def _substate(
    parent: BFGState,
    idx: np.ndarray,
    org_params: SelfOrganizationParameters,
    child_name: str,
) -> BFGState:
    idx = np.asarray(idx, dtype=int)
    positions = np.asarray(parent.metadata["positions"])[idx]
    A = np.asarray(parent.metadata["adjacency"])[np.ix_(idx, idx)]
    resource = np.asarray(parent.metadata["resource"])[idx]
    D = np.asarray(parent.D)[idx]
    child = _rebuild_state(parent, positions, A, resource, D, org_params, child_name)
    child.metadata["source_node_indices"] = idx.tolist()
    return child


def _frame(generation: int, units: dict[str, PopulationUnit],
           org_params: SelfOrganizationParameters) -> dict:
    if not units:
        return {
            "generation": generation,
            "population_size": 0,
            "total_nodes": 0,
            "mean_unit_nodes": 0.0,
            "mean_resource": 0.0,
            "mean_maintenance": 0.0,
            "mean_unit_age": 0.0,
        }
    ms = [organization_metrics(u.state, org_params) for u in units.values()]
    sizes = [u.state.dim for u in units.values()]
    return {
        "generation": generation,
        "population_size": len(units),
        "total_nodes": int(sum(sizes)),
        "mean_unit_nodes": float(np.mean(sizes)),
        "min_unit_nodes": int(min(sizes)),
        "max_unit_nodes": int(max(sizes)),
        "mean_resource": float(np.mean([m["mean_resource"] for m in ms])),
        "mean_maintenance": float(np.mean([m["maintenance_score"] for m in ms])),
        "mean_unit_age": float(np.mean([u.age for u in units.values()])),
    }


def simulate_population(
    seed: int = 1341550191,
    generations: int = 36,
    org_params: SelfOrganizationParameters | None = None,
    pop_params: PopulationParameters | None = None,
    policy: NumericalPolicy | None = None,
) -> PopulationRun:
    org_params = org_params or SelfOrganizationParameters()
    pop_params = pop_params or PopulationParameters()
    policy = policy or NumericalPolicy()
    org_params.validate()
    pop_params.validate()

    rng = np.random.default_rng(seed + 9321)
    carrier = SelfOrganizingNetworkCarrier(org_params)

    initial = make_self_organizing_seed(seed=seed, params=org_params)
    units: dict[str, PopulationUnit] = {
        "U0": PopulationUnit(
            unit_id="U0", state=initial, parent_id=None,
            birth_generation=0, age=0, alive=True
        )
    }
    next_id = 1
    events = [{
        "event": "unit_birth",
        "unit_id": "U0",
        "parent_id": None,
        "generation": 0,
        "node_count": initial.dim,
        "reason": "initial_seed",
    }]
    frames = [_frame(0, units, org_params)]
    core_steps = successful = novel = 0

    for generation in range(1, int(generations)+1):
        if not units:
            frames.append(_frame(generation, units, org_params))
            break

        next_units: dict[str, PopulationUnit] = {}

        for unit_id, unit in list(units.items()):
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
                    "node_count": unit.state.dim,
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
                    "node_count": unit.state.dim,
                })
                continue

            evolved, dim_events = _dimension_update(
                evolved, org_params, pop_params, rng, unit_id
            )
            evolved.generation = generation
            events.extend(dim_events)

            if evolved.dim < pop_params.min_unit_nodes:
                events.append({
                    "event": "unit_death",
                    "unit_id": unit_id,
                    "generation": generation,
                    "reason": "below_minimum_unit_size",
                    "age": unit.age,
                    "node_count": evolved.dim,
                })
                continue

            components = _viable_components(evolved, pop_params)

            # Fission only if at least two independently viable components exist
            # and the population cap can accommodate them.
            can_fission = (
                len(components) >= 2
                and len(next_units) + len(components) <= pop_params.max_population
            )

            if can_fission:
                child_ids = []
                child_sizes = []
                retained_nodes = 0
                for idx in components:
                    cid = f"U{next_id}"
                    next_id += 1
                    child_state = _substate(
                        evolved, idx, org_params,
                        child_name=f"{cid}_g{generation}"
                    )
                    child_state.generation = generation
                    child = PopulationUnit(
                        unit_id=cid,
                        state=child_state,
                        parent_id=unit_id,
                        birth_generation=generation,
                        age=0,
                        alive=True,
                    )
                    next_units[cid] = child
                    child_ids.append(cid)
                    child_sizes.append(child_state.dim)
                    retained_nodes += child_state.dim
                    events.append({
                        "event": "unit_birth",
                        "unit_id": cid,
                        "parent_id": unit_id,
                        "generation": generation,
                        "node_count": child_state.dim,
                        "reason": "fission_child",
                    })

                discarded = evolved.dim - retained_nodes
                events.append({
                    "event": "fission",
                    "unit_id": unit_id,
                    "generation": generation,
                    "children": child_ids,
                    "child_sizes": child_sizes,
                    "parent_nodes_before_fission": evolved.dim,
                    "unassigned_fragment_nodes": discarded,
                    "age": unit.age + 1,
                })
                if discarded > 0:
                    events.append({
                        "event": "node_loss",
                        "unit_id": unit_id,
                        "generation": generation,
                        "count": discarded,
                        "resource_removed": None,
                        "reason": "nonviable_fission_fragments",
                    })
                continue

            # No fission: the same unit identity persists.
            next_units[unit_id] = PopulationUnit(
                unit_id=unit_id,
                state=evolved,
                parent_id=unit.parent_id,
                birth_generation=unit.birth_generation,
                age=unit.age+1,
                alive=True,
            )

        units = next_units
        frames.append(_frame(generation, units, org_params))

        # Hard population cap: keep the best-maintained units, terminate the rest.
        if len(units) > pop_params.max_population:
            ranked = sorted(
                units.items(),
                key=lambda kv: organization_metrics(kv[1].state, org_params)["maintenance_score"],
                reverse=True,
            )
            keep_ids = {uid for uid, _ in ranked[:pop_params.max_population]}
            for uid in list(units):
                if uid not in keep_ids:
                    u = units.pop(uid)
                    events.append({
                        "event": "unit_death",
                        "unit_id": uid,
                        "generation": generation,
                        "reason": "population_cap",
                        "age": u.age,
                        "node_count": u.state.dim,
                    })

    return PopulationRun(
        initial_seed=seed,
        frames=frames,
        events=events,
        final_units=units,
        core_steps=core_steps,
        successful_reclosures=successful,
        novel_reclosures=novel,
    )


def write_population_report(
    run: PopulationRun,
    outdir: str | Path,
    stem: str = "population",
) -> dict[str, str]:
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    frames_csv = outdir / f"{stem}_frames.csv"
    with frames_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(run.frames[0].keys()))
        w.writeheader()
        w.writerows(run.frames)

    events_json = outdir / f"{stem}_events.json"
    events_json.write_text(json.dumps(run.events, indent=2), encoding="utf-8")

    summary_json = outdir / f"{stem}_summary.json"
    summary_json.write_text(json.dumps(run.summary(), indent=2), encoding="utf-8")

    # Population trajectory.
    g = np.array([f["generation"] for f in run.frames])
    pop = np.array([f["population_size"] for f in run.frames])
    nodes = np.array([f["total_nodes"] for f in run.frames])
    maintenance = np.array([f["mean_maintenance"] for f in run.frames])

    trajectory = outdir / f"{stem}_trajectory.png"
    fig, ax1 = plt.subplots(figsize=(7.6, 4.7))
    ax1.plot(g, pop, marker="o", label="independent units")
    ax1.plot(g, nodes, marker="s", label="total nodes")
    ax1.set_xlabel("Generation")
    ax1.set_ylabel("Count")
    ax2 = ax1.twinx()
    ax2.plot(g, maintenance, marker="^", linestyle="--", label="mean maintenance")
    ax2.set_ylabel("Maintenance")
    lines = ax1.get_lines() + ax2.get_lines()
    ax1.legend(lines, [ln.get_label() for ln in lines], loc="best")
    ax1.set_title("BFG population / dimension dynamics")
    fig.tight_layout()
    fig.savefig(trajectory, dpi=165)
    plt.close(fig)

    # Lineage tree from unit-birth/fission events.
    births = [e for e in run.events if e["event"] == "unit_birth"]
    birth_gen = {e["unit_id"]: e["generation"] for e in births}
    parent = {e["unit_id"]: e.get("parent_id") for e in births}
    all_ids = list(birth_gen)
    layers = {}
    for uid in all_ids:
        gen = birth_gen[uid]
        layers.setdefault(gen, []).append(uid)

    lineage = outdir / f"{stem}_lineage.png"
    plt.figure(figsize=(8.2, 5.2))
    coords = {}
    for gen in sorted(layers):
        ids = layers[gen]
        for j, uid in enumerate(ids):
            y = j - (len(ids)-1)/2
            coords[uid] = (gen, y)
            plt.scatter([gen], [y], s=80)
            plt.text(gen+0.15, y, uid, fontsize=8, va="center")
    for uid, par in parent.items():
        if par is not None and uid in coords and par in coords:
            x0,y0 = coords[par]
            x1,y1 = coords[uid]
            plt.plot([x0,x1],[y0,y1], linewidth=1.1)
    plt.xlabel("Birth generation")
    plt.ylabel("Lineage branch")
    plt.title("Independent BFG unit lineage")
    plt.tight_layout()
    plt.savefig(lineage, dpi=165)
    plt.close()

    return {
        "frames_csv": str(frames_csv),
        "events_json": str(events_json),
        "summary_json": str(summary_json),
        "trajectory_plot": str(trajectory),
        "lineage_plot": str(lineage),
    }
