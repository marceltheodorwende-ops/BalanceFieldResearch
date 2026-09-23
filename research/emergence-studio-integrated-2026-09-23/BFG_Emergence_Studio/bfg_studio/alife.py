from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import csv
import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse.csgraph import connected_components

from .carrier import CarrierAdapter
from .types import BFGState, CoreStep, NumericalPolicy, RunRecord
from .linalg import hermitize, psd_project
from .simulate import simulate


@dataclass(frozen=True)
class SelfOrganizationParameters:
    node_count: int = 24
    persistent_rank: int = 6
    neighbor_scale: float = 0.32
    edge_threshold: float = 0.16
    resource_blend: float = 0.28
    topology_blend: float = 0.20
    export_cost: float = 0.10
    basal_recovery: float = 0.035
    load_scale: float = 0.42
    stress_scale: float = 0.18
    formation_drive: float = 1.45
    formation_offset: float = 0.20
    contraction: float = 0.76
    phase_scale: float = 0.40
    cluster_threshold: float = 0.22
    viability_threshold: float = 0.20

    def validate(self):
        if self.node_count < 4:
            raise ValueError("node_count must be >= 4")
        if not (2 <= self.persistent_rank <= self.node_count):
            raise ValueError("persistent_rank must satisfy 2 <= rank <= node_count")
        for name in ("resource_blend", "topology_blend", "export_cost", "basal_recovery",
                     "load_scale", "stress_scale", "formation_drive", "contraction"):
            value = getattr(self, name)
            if value < 0:
                raise ValueError(f"{name} must be nonnegative")
        if not (0 <= self.contraction < 1):
            raise ValueError("contraction must lie in [0,1)")


def _distance_kernel(positions: np.ndarray, scale: float) -> np.ndarray:
    diff = positions[:, None, :] - positions[None, :, :]
    dist2 = np.sum(diff * diff, axis=2)
    scale2 = max(scale * scale, 1e-12)
    K = np.exp(-dist2 / (2.0 * scale2))
    np.fill_diagonal(K, 0.0)
    return K


def _normalize01(x: np.ndarray, eps: float = 1e-12) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    lo, hi = float(np.min(x)), float(np.max(x))
    if hi - lo <= eps:
        return np.full_like(x, 0.5)
    return (x - lo) / (hi - lo)


def _weighted_laplacian(A: np.ndarray) -> np.ndarray:
    A = np.asarray(A, dtype=float)
    A = 0.5 * (A + A.T)
    A[A < 0] = 0
    np.fill_diagonal(A, 0.0)
    return np.diag(np.sum(A, axis=1)) - A


def _formation_operator(A: np.ndarray, resource: np.ndarray,
                        formation_drive: float, formation_offset: float) -> np.ndarray:
    L = _weighted_laplacian(A)
    n = A.shape[0]
    # Positive graph stiffness plus one collective resource-supported destabilizing mode.
    # The rank-one subtraction can create at most one negative mode, preserving the
    # strict BFG determinate-formation requirement rather than weakening its gate.
    scale = max(float(np.linalg.norm(L, 2)), 1e-12)
    Ln = L / scale
    r = np.clip(np.asarray(resource, dtype=float), 0.0, 1.0)
    u = r / max(float(np.linalg.norm(r)), 1e-12)
    K = Ln + formation_offset * np.eye(n) - formation_drive * np.outer(u, u)
    return hermitize(K.astype(complex))


def _neutral_load(A: np.ndarray, resource: np.ndarray,
                  load_scale: float, stress_scale: float) -> np.ndarray:
    L = _weighted_laplacian(A)
    n = A.shape[0]
    scale = max(float(np.linalg.norm(L, 2)), 1e-12)
    Ln = L / scale
    # Keep neutral geometry spectrally aligned with the same graph operator that
    # defines the persistent modes. Global resource stress changes the scalar load
    # but does not rotate the persistent eigenspaces. This places the carrier on
    # the exact [P,Y]=0 support stratum rather than creating an ambiguous doubled support.
    r = np.clip(np.asarray(resource, dtype=float), 0.0, 1.0)
    stress = float(np.mean((1.0-r)**2))
    Y = load_scale * (Ln @ Ln) + stress_scale * stress * np.eye(n)
    return psd_project(Y, floor=0.0).astype(complex)


def _recursive_operator(A: np.ndarray, persistent_rank: int,
                        contraction: float, phase_scale: float) -> np.ndarray:
    L = _weighted_laplacian(A)
    vals, vecs = np.linalg.eigh(L)
    order = np.argsort(vals)
    vals = vals[order]
    vecs = vecs[:, order]
    n = len(vals)
    r = min(max(2, persistent_rank), n)
    # Lowest graph modes are the slowly varying persistent organization modes.
    phase = np.exp(1j * phase_scale * vals[:r] / max(float(vals[-1]), 1e-12))
    residual = np.full(n-r, contraction, dtype=complex)
    spec = np.concatenate([phase, residual])
    return vecs.astype(complex) @ np.diag(spec) @ vecs.T.astype(complex)


def make_self_organizing_seed(
    seed: int = 7,
    params: SelfOrganizationParameters | None = None,
) -> BFGState:
    params = params or SelfOrganizationParameters()
    params.validate()
    rng = np.random.default_rng(seed)
    n = params.node_count

    positions = rng.uniform(0.0, 1.0, size=(n, 2))
    geom = _distance_kernel(positions, params.neighbor_scale)
    # Mild random heterogeneity prevents exact symmetry locks.
    hetero = rng.uniform(0.75, 1.25, size=(n, n))
    hetero = 0.5 * (hetero + hetero.T)
    A = geom * hetero
    A[A < params.edge_threshold] = 0.0
    np.fill_diagonal(A, 0.0)
    if np.max(A) > 0:
        A /= np.max(A)

    # Seed one broad resource-rich region plus low background.
    center = rng.uniform(0.25, 0.75, size=2)
    d2 = np.sum((positions-center)**2, axis=1)
    resource = 0.18 + 0.72*np.exp(-d2/(2*0.22**2))
    resource += rng.normal(0, 0.025, size=n)
    resource = np.clip(resource, 0.04, 1.0)

    phase = rng.uniform(-np.pi, np.pi, size=n)
    D = resource * np.exp(1j*phase)
    D /= max(float(np.linalg.norm(D)), 1e-12)

    K = _formation_operator(A, resource, params.formation_drive, params.formation_offset)
    Y = _neutral_load(A, resource, params.load_scale, params.stress_scale)
    R_C = _recursive_operator(A, params.persistent_rank, params.contraction, params.phase_scale)

    return BFGState(
        D=D, K=K, Y=Y, R_C=R_C, generation=0,
        name="self_organization_seed",
        metadata={
            "carrier": "SelfOrganizingNetworkCarrier",
            "seed": seed,
            "positions": positions,
            "adjacency": A,
            "resource": resource,
            "params": params.__dict__.copy(),
            "carrier_scope": "research model; not an empirical biological law",
        },
    )


class SelfOrganizingNetworkCarrier(CarrierAdapter):
    """
    Reference self-organization carrier.

    Carrier-specific rules:
    - BFG formation amplitude redistributes local resource.
    - exported load acts as a maintenance cost.
    - recurrent co-activity reinforces geometrically admissible edges.
    - topology rebuild changes the next K, Y, and R_C.

    These rules are deliberately labeled carrier-specific. The generic BFG
    reclosure equations remain in bfg_studio.core.
    """

    def __init__(self, params: SelfOrganizationParameters | None = None):
        self.params = params or SelfOrganizationParameters()
        self.params.validate()

    def advance(self, previous: BFGState, step: CoreStep,
                policy: NumericalPolicy) -> BFGState:
        if not step.success or step.support_basis is None or step.formation_vector is None:
            return BFGState(
                D=previous.D.copy(), K=previous.K.copy(), Y=previous.Y.copy(),
                R_C=previous.R_C.copy(), generation=previous.generation+1,
                name=f"{previous.name}_terminal",
                metadata=dict(previous.metadata),
                terminal=True,
                terminal_reason=step.terminal_reason or "BFG reclosure failed",
            )

        p = self.params
        positions = np.asarray(previous.metadata["positions"], dtype=float)
        A_prev = np.asarray(previous.metadata["adjacency"], dtype=float)
        r_prev = np.asarray(previous.metadata["resource"], dtype=float)

        V = step.support_basis
        formed = V @ step.formation_vector
        if np.real(np.vdot(previous.D, formed)) < 0:
            formed = -formed

        activity = np.abs(formed)**2
        activity /= max(float(np.max(activity)), 1e-12)

        exported = np.abs(step.D_out)**2 if step.D_out is not None else np.zeros_like(activity)
        exported /= max(float(np.max(exported)), 1e-12)

        # Resource update: formation-supported activity receives resource,
        # export dissipates it, and a small basal recovery prevents trivial freeze.
        target_resource = np.clip(0.10 + 0.90*activity, 0.0, 1.0)
        resource = (
            (1.0-p.resource_blend)*r_prev
            + p.resource_blend*target_resource
            - p.export_cost*exported
            + p.basal_recovery*(1.0-r_prev)
        )
        resource = np.clip(resource, 0.0, 1.0)

        # Relational rebuild: co-active nodes strengthen nearby admissible relations.
        geom = _distance_kernel(positions, p.neighbor_scale)
        coactivity = np.sqrt(np.outer(activity, activity))
        target_A = geom * (0.20 + 0.80*coactivity)
        target_A *= np.sqrt(np.outer(resource, resource))
        if np.max(target_A) > 0:
            target_A /= np.max(target_A)

        A = (1.0-p.topology_blend)*A_prev + p.topology_blend*target_A
        A[A < 0.25*p.edge_threshold] = 0.0
        A = np.clip(0.5*(A+A.T), 0.0, 1.0)
        np.fill_diagonal(A, 0.0)

        # The new state is reconstructed from the evolved carrier geometry.
        K = _formation_operator(A, resource, p.formation_drive, p.formation_offset)
        Y = _neutral_load(A, resource, p.load_scale, p.stress_scale)
        R_C = _recursive_operator(A, p.persistent_rank, p.contraction, p.phase_scale)

        phase = np.angle(formed + 1e-15)
        D = resource * (0.25 + 0.75*activity) * np.exp(1j*phase)
        D /= max(float(np.linalg.norm(D)), 1e-12)

        return BFGState(
            D=D, K=K, Y=Y, R_C=R_C,
            generation=previous.generation+1,
            name=f"self_organization_g{previous.generation+1}",
            metadata={
                **previous.metadata,
                "adjacency": A,
                "resource": resource,
                "activity": activity,
                "exported": exported,
                "carrier": "SelfOrganizingNetworkCarrier",
            },
        )


def organization_metrics(state: BFGState,
                         params: SelfOrganizationParameters | None = None) -> dict:
    params = params or SelfOrganizationParameters(**state.metadata.get("params", {}))
    A = np.asarray(state.metadata["adjacency"], dtype=float)
    r = np.asarray(state.metadata["resource"], dtype=float)
    n = len(r)

    active = (A >= params.cluster_threshold).astype(int)
    np.fill_diagonal(active, 0)
    n_components, labels = connected_components(active, directed=False, connection="weak")
    sizes = np.bincount(labels, minlength=n_components)
    largest = int(np.max(sizes)) if sizes.size else 0

    viable = r >= params.viability_threshold
    viable_fraction = float(np.mean(viable))
    edge_density = float(np.count_nonzero(np.triu(active, 1)) / max(n*(n-1)/2, 1))
    mean_resource = float(np.mean(r))
    resource_std = float(np.std(r))

    # Shannon effective participation of resource, normalized to [0,1].
    probs = r / max(float(np.sum(r)), 1e-12)
    entropy = -float(np.sum(probs*np.log(probs+1e-15))) / np.log(n)

    L = _weighted_laplacian(A)
    lvals = np.sort(np.linalg.eigvalsh(L).real)
    algebraic_connectivity = float(lvals[1]) if len(lvals) > 1 else 0.0

    large_clusters = int(np.sum(sizes >= max(2, int(np.ceil(0.18*n)))))
    multi_cluster_state = bool(large_clusters >= 2 and viable_fraction >= 0.55)

    maintenance = float(
        np.clip(mean_resource, 0, 1)
        * np.clip(entropy, 0, 1)
        * (0.5 + 0.5*viable_fraction)
    )

    return {
        "generation": int(state.generation),
        "component_count": int(n_components),
        "largest_component_fraction": largest/n,
        "large_cluster_count": large_clusters,
        "multi_cluster_state": multi_cluster_state,
        "division_like_candidate": multi_cluster_state,
        "mean_resource": mean_resource,
        "resource_std": resource_std,
        "resource_entropy": entropy,
        "viable_fraction": viable_fraction,
        "edge_density": edge_density,
        "algebraic_connectivity": algebraic_connectivity,
        "maintenance_score": maintenance,
        "terminal": bool(state.terminal),
    }


def simulate_self_organization(
    seed: int = 7,
    steps: int = 20,
    params: SelfOrganizationParameters | None = None,
    policy: NumericalPolicy | None = None,
) -> RunRecord:
    params = params or SelfOrganizationParameters()
    initial = make_self_organizing_seed(seed=seed, params=params)
    return simulate(initial, SelfOrganizingNetworkCarrier(params), steps=steps,
                    policy=policy or NumericalPolicy())



def _cluster_sets(state: BFGState,
                  params: SelfOrganizationParameters | None = None) -> list[set[int]]:
    params = params or SelfOrganizationParameters(**state.metadata.get("params", {}))
    A = np.asarray(state.metadata["adjacency"], dtype=float)
    active = (A >= params.cluster_threshold).astype(int)
    np.fill_diagonal(active, 0)
    n_components, labels = connected_components(active, directed=False, connection="weak")
    return [set(np.where(labels == k)[0].tolist()) for k in range(n_components)]


def cluster_lineage_events(
    run: RunRecord,
    params: SelfOrganizationParameters | None = None,
    minimum_cluster_size: int | None = None,
    overlap_threshold: float = 0.15,
) -> list[dict]:
    """
    Track component ancestry by node overlap.

    A `split_like` event means one sufficiently large predecessor component has
    substantial overlap with two or more sufficiently large successor components.
    The node set is fixed, so this is structural fission, not biological reproduction.
    """
    if not run.states:
        return []
    params = params or SelfOrganizationParameters(**run.states[0].metadata.get("params", {}))
    n = run.states[0].dim
    minimum_cluster_size = minimum_cluster_size or max(2, int(np.ceil(0.18*n)))
    events = []

    for prev, nxt in zip(run.states[:-1], run.states[1:]):
        prev_clusters = [c for c in _cluster_sets(prev, params) if len(c) >= minimum_cluster_size]
        next_clusters = [c for c in _cluster_sets(nxt, params) if len(c) >= minimum_cluster_size]

        for pi, pc in enumerate(prev_clusters):
            descendants = []
            for ni, nc in enumerate(next_clusters):
                inter = len(pc & nc)
                if inter == 0:
                    continue
                # predecessor-overlap fraction: how much of the old cluster survives in this child
                pfrac = inter / max(len(pc), 1)
                # Jaccard is reported for interpretability but does not alone define ancestry.
                jaccard = inter / max(len(pc | nc), 1)
                if pfrac >= overlap_threshold or jaccard >= overlap_threshold:
                    descendants.append({
                        "next_cluster": ni,
                        "next_size": len(nc),
                        "predecessor_overlap": pfrac,
                        "jaccard": jaccard,
                    })
            if descendants:
                events.append({
                    "from_generation": prev.generation,
                    "to_generation": nxt.generation,
                    "previous_cluster": pi,
                    "previous_size": len(pc),
                    "descendants": descendants,
                    "event": "split_like" if len(descendants) >= 2 else "continuation",
                })
    return events

def write_self_organization_report(
    run: RunRecord,
    outdir: str | Path,
    stem: str = "self_organization",
) -> dict[str, str]:
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    rows = [organization_metrics(s) for s in run.states]

    csv_path = outdir / f"{stem}_organization.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    json_path = outdir / f"{stem}_organization.json"
    json_path.write_text(json.dumps(rows, indent=2), encoding="utf-8")

    lineage = cluster_lineage_events(run)
    lineage_path = outdir / f"{stem}_lineage.json"
    lineage_path.write_text(json.dumps(lineage, indent=2), encoding="utf-8")

    g = np.array([r["generation"] for r in rows])
    maintenance = np.array([r["maintenance_score"] for r in rows])
    largest = np.array([r["largest_component_fraction"] for r in rows])
    clusters = np.array([r["large_cluster_count"] for r in rows])

    metric_plot = outdir / f"{stem}_organization.png"
    plt.figure(figsize=(7.4, 4.5))
    plt.plot(g, maintenance, marker="o", label="maintenance score")
    plt.plot(g, largest, marker="s", label="largest cluster fraction")
    plt.plot(g, clusters / max(1, np.max(clusters)), marker="^",
             label="large clusters (normalized)")
    plt.xlabel("Generation")
    plt.ylabel("Normalized organization measure")
    plt.title("BFG self-organization trajectory")
    plt.legend()
    plt.tight_layout()
    plt.savefig(metric_plot, dpi=160)
    plt.close()

    # Initial/final carrier geometry.
    network_plot = outdir / f"{stem}_network_final.png"
    state = run.states[-1]
    positions = np.asarray(state.metadata["positions"])
    A = np.asarray(state.metadata["adjacency"])
    resource = np.asarray(state.metadata["resource"])
    plt.figure(figsize=(6.2, 5.4))
    for i in range(len(resource)):
        for j in range(i+1, len(resource)):
            if A[i, j] >= 0.18:
                plt.plot([positions[i,0], positions[j,0]],
                         [positions[i,1], positions[j,1]],
                         linewidth=0.4 + 2.0*A[i,j],
                         alpha=0.18 + 0.65*A[i,j])
    sizes = 40 + 260*resource
    plt.scatter(positions[:,0], positions[:,1], s=sizes)
    plt.title(f"Self-organized carrier at generation {state.generation}")
    plt.xlabel("carrier x")
    plt.ylabel("carrier y")
    plt.tight_layout()
    plt.savefig(network_plot, dpi=160)
    plt.close()

    return {
        "organization_csv": str(csv_path),
        "organization_json": str(json_path),
        "lineage_json": str(lineage_path),
        "organization_plot": str(metric_plot),
        "final_network_plot": str(network_plot),
    }


def self_organization_score(run: RunRecord) -> float:
    metrics = [organization_metrics(s) for s in run.states]
    if not metrics:
        return -1e9
    longevity = len(run.steps)
    mean_maintenance = float(np.mean([m["maintenance_score"] for m in metrics]))
    max_clusters = max(m["large_cluster_count"] for m in metrics)
    lineage = cluster_lineage_events(run)
    split_count = sum(int(e["event"] == "split_like") for e in lineage)
    split_bonus = 4.0 * min(split_count, 2)
    novelty = sum(int(bool(s.spectral_novelty)) for s in run.steps
                  if s.spectral_novelty is not None)
    terminal_penalty = 1.5 if run.states[-1].terminal else 0.0
    return float(
        1.5*longevity + 4.0*mean_maintenance + 0.8*novelty
        + 0.6*max_clusters + split_bonus - terminal_penalty
    )


def search_self_organization(
    trials: int = 50,
    steps: int = 16,
    params: SelfOrganizationParameters | None = None,
    seed: int = 1,
    top_k: int = 5,
):
    params = params or SelfOrganizationParameters()
    rng = np.random.default_rng(seed)
    hits = []
    for _ in range(int(trials)):
        s = int(rng.integers(0, 2**31-1))
        run = simulate_self_organization(s, steps, params)
        hits.append((self_organization_score(run), s, run))
    hits.sort(key=lambda x: x[0], reverse=True)
    return hits[:int(top_k)]
