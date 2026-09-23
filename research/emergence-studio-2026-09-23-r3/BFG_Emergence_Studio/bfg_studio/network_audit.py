from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
from typing import Any
import csv
import json
import tempfile

import numpy as np
import matplotlib.pyplot as plt

from .carrier_sdk import validate_state_contract
from .finite_closure import (
    bfg_state_to_reduced,
    reduced_closure_step,
)
from .network_carrier import (
    KarateInteractionCarrier,
    KarateNetworkConfig,
    DEFAULT_DATA,
    prepare_karate_carrier,
)
from .runtime_transfer import transfer_one_state
from .small_load import one_step_small_load_certificate
from .session import source_tree_fingerprint


TRANSFORM_METRICS=(
    "alpha",
    "formation_depth_normalized",
    "formation_gap_normalized",
    "neutral_load_density_ratio",
    "k_rms_ratio",
)

FORMATION_METRICS=(
    "depth_over_spectral_norm",
    "depth_over_rms_norm",
    "depth_over_gap",
    "depth_over_mean_abs_eigenvalue",
)


def _qstats(values:list[float]) -> dict[str,float|None]:
    x=np.asarray([v for v in values if np.isfinite(v)],dtype=float)
    if x.size==0:
        return {
            "q10":None,"median":None,"q90":None,
            "min":None,"max":None,
        }
    q=np.quantile(x,[.10,.50,.90])
    return {
        "q10":float(q[0]),
        "median":float(q[1]),
        "q90":float(q[2]),
        "min":float(np.min(x)),
        "max":float(np.max(x)),
    }


def _formation_coordinates(state,step) -> dict[str,float]:
    K=np.asarray(state.K,dtype=complex)
    vals=np.linalg.eigvalsh(0.5*(K+K.conj().T)).real
    depth=-float(step.formation_eigenvalue)
    gap=float(step.formation_gap)
    spectral=max(float(np.max(np.abs(vals))),1e-300)
    rms=max(float(np.sqrt(np.mean(vals*vals))),1e-300)
    mean_abs=max(float(np.mean(np.abs(vals))),1e-300)
    return {
        "depth_over_spectral_norm":depth/spectral,
        "depth_over_rms_norm":depth/rms,
        "depth_over_gap":(
            depth/gap if np.isfinite(gap) and gap>0 else float("nan")
        ),
        "depth_over_mean_abs_eigenvalue":depth/mean_abs,
    }


def _intersection(
    intervals:list[tuple[float,float]],
) -> tuple[bool,float|None,float|None]:
    if not intervals:
        return False,None,None
    lo=max(x[0] for x in intervals)
    hi=min(x[1] for x in intervals)
    return bool(lo<=hi), (float(lo) if lo<=hi else None), (
        float(hi) if lo<=hi else None
    )


def _permutation_equivariance_audit(
    carrier:KarateInteractionCarrier,
) -> dict[str,Any]:
    A=carrier.adjacency
    n=A.shape[0]
    rng=np.random.default_rng(20260923)
    perm=rng.permutation(n)

    P=np.zeros((n,n),dtype=float)
    for old,new in enumerate(perm):
        P[new,old]=1.0
    Ap=P@A@P.T

    with tempfile.TemporaryDirectory() as td:
        path=Path(td)/"permuted_edges.csv"
        with path.open("w",newline="",encoding="utf-8") as f:
            w=csv.writer(f)
            w.writerow(["source","target","weight"])
            for i in range(n):
                for j in range(i+1,n):
                    if Ap[i,j]>0:
                        w.writerow([i,j,float(Ap[i,j])])

        pc=KarateInteractionCarrier(
            config=KarateNetworkConfig(
                diffusion_time=carrier.config.diffusion_time,
                neutral_load_scale=carrier.config.neutral_load_scale,
                stress_scale=carrier.config.stress_scale,
                formation_drive=carrier.config.formation_drive,
                formation_offset=carrier.config.formation_offset,
                persistent_rank=carrier.config.persistent_rank,
                contraction=carrier.config.contraction,
                phase_scale=carrier.config.phase_scale,
                dataset_sha256="",
            ),
            data_path=path,
        )

        maxima={
            "D":0.0,
            "K":0.0,
            "Y":0.0,
            "R_C":0.0,
        }
        for old in range(n):
            new=int(perm[old])
            s=carrier.map_measurement_to_state(
                {"focal_node":old,"weighted_degree":float(A[old].sum())},
                generation=old,
            )
            sp=pc.map_measurement_to_state(
                {"focal_node":new,"weighted_degree":float(Ap[new].sum())},
                generation=old,
            )
            maxima["D"]=max(
                maxima["D"],
                float(np.linalg.norm(sp.D-P@s.D)),
            )
            for attr in ("K","Y","R_C"):
                lhs=getattr(sp,attr)
                rhs=P@getattr(s,attr)@P.T
                maxima[attr]=max(
                    maxima[attr],
                    float(np.linalg.norm(lhs-rhs,2)),
                )

    return {
        "permutation_seed":20260923,
        "maximum_residuals":maxima,
        "equivariant":bool(max(maxima.values())<=1e-10),
    }


def run_karate_network_audit(
    project_root:str|Path|None=None,
    *,
    recursive_horizon:int=4,
) -> dict[str,Any]:
    root=(
        Path(project_root)
        if project_root is not None
        else Path(__file__).resolve().parent.parent
    )
    carrier=KarateInteractionCarrier()
    measurements=carrier.measurements()

    states=[]
    state_reports=[]
    for i,m in enumerate(measurements):
        s=carrier.map_measurement_to_state(m,generation=i)
        rep=validate_state_contract(s)
        states.append(s)
        state_reports.append({
            "focal_node":i,
            "valid":rep.valid,
            "checks":rep.checks,
        })

    transfer=[
        transfer_one_state(
            s,
            carrier_id="zachary-karate-network",
            index=i,
            recursive_horizon=recursive_horizon,
        )
        for i,s in enumerate(states)
    ]

    first_success=[
        r for r in transfer if r["first_step_success"]
    ]
    first_failure=[
        r for r in transfer if not r["first_step_success"]
    ]

    transform_stats={
        metric:_qstats([
            r[metric] for r in first_success
        ])
        for metric in TRANSFORM_METRICS
    }

    formation_values=defaultdict(list)
    small_load_rows=[]
    for i,s in enumerate(states):
        current=bfg_state_to_reduced(s)
        for depth in range(1,recursive_horizon+1):
            nxt,step=reduced_closure_step(current)
            if depth==1 and step.success:
                coords=_formation_coordinates(current,step)
                for k,v in coords.items():
                    formation_values[k].append(float(v))

            cert=one_step_small_load_certificate(
                current,nxt,step,
                carrier_id="zachary-karate-network",
                state_index=i,
                depth=depth,
            )
            if cert.theorem_applicable:
                small_load_rows.append(cert.to_dict())

            if step.success:
                current=nxt
            else:
                break

    formation_stats={
        metric:_qstats(formation_values[metric])
        for metric in FORMATION_METRICS
    }

    three_transfer=json.loads(
        (root/"outputs/runtime_transfer/master_runtime_transfer_audit.json")
        .read_text(encoding="utf-8")
    )
    three_formation=json.loads(
        (root/"outputs/formation_dynamics/formation_termination_analysis.json")
        .read_text(encoding="utf-8")
    )

    four_transform=[]
    for metric in TRANSFORM_METRICS:
        intervals=[]
        for domain in three_transfer["carriers"]:
            q=domain["transformation_metrics"][metric]
            intervals.append((float(q["q10"]),float(q["q90"])))
        nq=transform_stats[metric]
        if nq["q10"] is not None:
            intervals.append((float(nq["q10"]),float(nq["q90"])))
        shared,lo,hi=_intersection(intervals)
        four_transform.append({
            "metric":metric,
            "shared_four_domain":shared,
            "lower":lo,
            "upper":hi,
        })

    four_formation=[]
    for metric in FORMATION_METRICS:
        intervals=[]
        for domain in three_formation["domains"]:
            q=domain["first_step_normalizations"][metric]
            intervals.append((float(q["q10"]),float(q["q90"])))
        nq=formation_stats[metric]
        if nq["q10"] is not None:
            intervals.append((float(nq["q10"]),float(nq["q90"])))
        shared,lo,hi=_intersection(intervals)
        four_formation.append({
            "metric":metric,
            "shared_four_domain":shared,
            "lower":lo,
            "upper":hi,
        })

    terminal_reasons=Counter(
        r["terminal_reason_within_horizon"]
        for r in transfer
        if r["terminal_reason_within_horizon"]
    )
    failure_reasons=Counter(
        r["first_step_reason"]
        for r in first_failure
        if r["first_step_reason"]
    )

    small_pass=sum(
        int(r["bound_satisfied"] is True)
        for r in small_load_rows
    )
    local_by_depth={}
    for depth in range(1,recursive_horizon+1):
        rows=[r for r in small_load_rows if r["depth"]==depth]
        local=[
            r for r in rows
            if r["local_small_load_parameter"] is not None
            and r["local_small_load_parameter"]<1
        ]
        local_by_depth[str(depth)]={
            "certificates":len(rows),
            "bound_passed":sum(
                int(r["bound_satisfied"] is True)
                for r in rows
            ),
            "local_fraction":len(local)/max(len(rows),1),
            "local_parameter":_qstats([
                r["local_small_load_parameter"]
                for r in rows
                if r["local_small_load_parameter"] is not None
            ]),
        }

    equivariance=_permutation_equivariance_audit(carrier)

    return {
        "status":"EXPLORATORY_REAL_RELATIONAL_CARRIER",
        "source_fingerprint":source_tree_fingerprint(),
        "heldout_metrics_evaluated":False,
        "confirmatory_plan_defined":False,
        "carrier_id":"zachary-karate-network",
        "mapping_fingerprint":carrier.mapping_fingerprint,
        "dataset_sha256":carrier.config.dataset_sha256,
        "nodes":34,
        "edges":78,
        "measurements":len(measurements),
        "club_labels_used":False,
        "state_contract_valid":sum(int(x["valid"]) for x in state_reports),
        "first_step_successes":len(first_success),
        "first_step_success_fraction":len(first_success)/len(states),
        "first_step_failure_reasons":dict(sorted(failure_reasons.items())),
        "terminal_reasons_within_horizon":dict(sorted(terminal_reasons.items())),
        "successful_depth_distribution":dict(sorted(Counter(
            int(r["successful_depth"]) for r in transfer
        ).items())),
        "transform_metrics":transform_stats,
        "formation_metrics":formation_stats,
        "four_domain_transform_corridors":four_transform,
        "four_domain_formation_corridors":four_formation,
        "small_load":{
            "certificates":len(small_load_rows),
            "bound_passed":small_pass,
            "all_bounds_verified":bool(
                len(small_load_rows)>0
                and small_pass==len(small_load_rows)
            ),
            "by_depth":local_by_depth,
        },
        "permutation_equivariance":equivariance,
        "transfer_records":transfer,
        "state_reports":state_reports,
        "interpretation_guard":{
            "ready_for_validation":False,
            "empirical_confirmation":False,
            "network_universality_established":False,
            "note":(
                "This carrier is a structurally different real interaction graph. "
                "It is exploratory because no independent confirmatory target/split "
                "has yet been defined. Failure of time-series corridors to extend "
                "to the network is retained as a domain-structure result."
            ),
        },
    }


def write_karate_network_report(
    result:dict[str,Any],
    outdir:str|Path,
) -> dict[str,str]:
    outdir=Path(outdir)
    outdir.mkdir(parents=True,exist_ok=True)

    json_path=outdir/"karate_network_audit.json"
    json_path.write_text(
        json.dumps(result,indent=2),
        encoding="utf-8",
    )

    csv_path=outdir/"karate_transfer_records.csv"
    rows=result["transfer_records"]
    if rows:
        fields=sorted({k for r in rows for k in r})
        with csv_path.open("w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(f,fieldnames=fields,extrasaction="ignore")
            w.writeheader()
            w.writerows(rows)

    md_path=outdir/"KARATE_NETWORK_AUDIT.md"
    lines=[
        "# BFG Real Relational Carrier Audit",
        "",
        "Carrier: **Zachary weighted karate-club interaction network**",
        "",
        "Status: **EXPLORATORY**",
        "",
        "No club/fission label is used by the BFG mapping.",
        "",
        f"State contract: `{result['state_contract_valid']}/{result['measurements']}`",
        "",
        f"First-step formation/master success: "
        f"`{result['first_step_successes']}/{result['measurements']}` "
        f"(`{100*result['first_step_success_fraction']:.3f}%`)",
        "",
        "## First-step failures",
        "",
    ]
    for reason,count in result["first_step_failure_reasons"].items():
        lines.append(f"- `{reason}`: {count}")

    lines += [
        "",
        "## Small-load theorem",
        "",
        f"Successful recursive certificates: "
        f"`{result['small_load']['certificates']}`",
        "",
        f"Explicit quadratic bounds satisfied: "
        f"`{result['small_load']['bound_passed']}/"
        f"{result['small_load']['certificates']}`",
        "",
        "## Permutation equivariance",
        "",
        f"Equivariant: `{result['permutation_equivariance']['equivariant']}`",
        "",
    ]
    for k,v in result["permutation_equivariance"]["maximum_residuals"].items():
        lines.append(f"- {k}: `{v:.3e}`")

    lines += [
        "",
        "## Four-domain transformation-corridor check",
        "",
        "| Metric | Shared across Sunspots + CO2 + ENSO + network |",
        "|---|---:|",
    ]
    for row in result["four_domain_transform_corridors"]:
        lines.append(
            f"| {row['metric']} | {row['shared_four_domain']} |"
        )

    lines += [
        "",
        "## Four-domain formation-normalization check",
        "",
        "| Metric | Shared across all four domains |",
        "|---|---:|",
    ]
    for row in result["four_domain_formation_corridors"]:
        lines.append(
            f"| {row['metric']} | {row['shared_four_domain']} |"
        )

    lines += [
        "",
        "## Interpretation",
        "",
        "The carrier deliberately tests relational structure rather than another "
        "time-series recurrence graph.",
        "",
        "The existing three-domain transformation corridors are not promoted to "
        "universal invariants if they fail to include this network carrier.",
        "",
        "The small-load theorem is evaluated separately because it is a mathematical "
        "master-runtime statement rather than an empirical corridor claim.",
        "",
        "This carrier is not moved to READY_FOR_VALIDATION until an independent "
        "confirmatory network target and sealed split are specified prospectively.",
    ]
    md_path.write_text("\n".join(lines)+"\n",encoding="utf-8")

    # Plot: first-step success/failure.
    plot_path=outdir/"karate_network_transfer_summary.png"
    fig,ax=plt.subplots(figsize=(6.4,4.6))
    ax.bar(
        ["formation success","formation-gate terminal"],
        [
            result["first_step_successes"],
            result["measurements"]-result["first_step_successes"],
        ],
    )
    ax.set_ylabel("node-centered probes")
    ax.set_title("Relational carrier: first master-transfer gate")
    fig.tight_layout()
    fig.savefig(plot_path,dpi=170)
    plt.close(fig)

    return {
        "json":str(json_path),
        "csv":str(csv_path),
        "markdown":str(md_path),
        "plot":str(plot_path),
    }
