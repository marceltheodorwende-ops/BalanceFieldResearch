from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any
import csv
import hashlib
import json

import numpy as np
from scipy.linalg import expm

from .types import BFGState, CoreStep, NumericalPolicy
from .carrier_sdk import (
    CarrierSchema,
    ValidatedCarrierAdapter,
    write_carrier_schema,
)


DEFAULT_DATA = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "zachary_karate_club_weighted_edges.csv"
)


@dataclass(frozen=True)
class KarateNetworkConfig:
    diffusion_time: float = 1.0
    neutral_load_scale: float = 0.42
    stress_scale: float = 0.18
    formation_drive: float = 1.45
    formation_offset: float = 0.20
    persistent_rank: int = 4
    contraction: float = 0.76
    phase_scale: float = 0.40
    dataset_sha256: str = ""

    def to_jsonable(self) -> dict[str,Any]:
        return asdict(self)


def _sha256(path:str|Path)->str:
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""):
            h.update(chunk)
    return h.hexdigest()


def load_weighted_karate_graph(
    path:str|Path=DEFAULT_DATA,
) -> np.ndarray:
    path=Path(path)
    rows=[]
    max_node=-1
    with path.open("r",encoding="utf-8") as f:
        reader=csv.DictReader(f)
        for row in reader:
            u=int(row["source"])
            v=int(row["target"])
            w=float(row["weight"])
            if w<=0 or not np.isfinite(w):
                raise ValueError("edge weights must be positive finite")
            rows.append((u,v,w))
            max_node=max(max_node,u,v)
    n=max_node+1
    if n!=34:
        raise ValueError("unexpected Zachary karate node count")
    A=np.zeros((n,n),dtype=float)
    for u,v,w in rows:
        if u==v:
            raise ValueError("unexpected self-loop")
        A[u,v]+=w
        A[v,u]+=w
    if int(np.count_nonzero(np.triu(A,1)))!=78:
        raise ValueError("unexpected Zachary karate edge count")
    return A


def graph_operators(
    adjacency:np.ndarray,
) -> tuple[np.ndarray,np.ndarray]:
    A=np.asarray(adjacency,dtype=float)
    if A.ndim!=2 or A.shape[0]!=A.shape[1]:
        raise ValueError("adjacency must be square")
    if np.linalg.norm(A-A.T,2)>1e-12:
        raise ValueError("adjacency must be symmetric")
    if np.min(A)<0:
        raise ValueError("adjacency weights must be nonnegative")
    strength=A.sum(axis=1)
    L=np.diag(strength)-A
    scale=max(float(np.linalg.norm(L,2)),1e-12)
    return L,L/scale


def node_probe_measurements(
    adjacency:np.ndarray,
) -> tuple[dict[str,Any],...]:
    n=adjacency.shape[0]
    strength=adjacency.sum(axis=1)
    return tuple(
        {
            "focal_node":int(i),
            "weighted_degree":float(strength[i]),
        }
        for i in range(n)
    )


class KarateInteractionCarrier(ValidatedCarrierAdapter):
    """
    Real relational carrier based on Zachary's weighted karate-club interaction
    graph.

    The mapping does not use the later club/fission labels. Each measurement is
    a node-centered graph probe over the same observed weighted interaction
    network.

    No predictive held-out claim is attached to this carrier yet; it enters the
    master as an exploratory real relational carrier.
    """

    def __init__(
        self,
        config:KarateNetworkConfig|None=None,
        *,
        data_path:str|Path=DEFAULT_DATA,
    ):
        data_path=Path(data_path)
        sha=_sha256(data_path)
        if config is None:
            config=KarateNetworkConfig(dataset_sha256=sha)
        elif config.dataset_sha256 and config.dataset_sha256!=sha:
            raise ValueError("network snapshot hash does not match frozen config")
        elif not config.dataset_sha256:
            config=KarateNetworkConfig(
                **{
                    **config.to_jsonable(),
                    "dataset_sha256":sha,
                }
            )
        self.config=config
        self.data_path=data_path
        self.adjacency=load_weighted_karate_graph(data_path)
        self.L,self.Ln=graph_operators(self.adjacency)

        schema=CarrierSchema(
            name="Zachary Karate Weighted Interaction BFG Carrier",
            domain="real social interaction network / weighted undirected graph",
            description=(
                "Node-centered heat-diffusion probes on the fixed weighted "
                "Zachary karate-club interaction graph; club labels are not used."
            ),
            measurement_mapping={
                "D": (
                    "normalized heat-diffusion state exp(-t L_n) e_i from the "
                    "focal observed node"
                ),
                "K": (
                    "normalized observed graph Laplacian plus fixed offset minus "
                    "one diffusion-supported formation mode"
                ),
                "Y": (
                    "PSD squared normalized observed graph Laplacian plus scalar "
                    "probe-complement stress"
                ),
                "R_C": (
                    "observed graph-Laplacian eigenbasis with low persistent "
                    "unit-modulus modes and contractive complement"
                ),
            },
            invariant_parameters={
                **config.to_jsonable(),
                "probe_family":"all 34 observed nodes, one heat-diffusion probe each",
                "club_labels_used":False,
                "parameter_policy":(
                    "same graph-aligned load/formation/recursion coefficients "
                    "already used by the real time-series carriers; no target fit"
                ),
            },
            empirical_units={
                "edge_weight":"interaction-context count",
                "node":"club member index",
            },
        )
        super().__init__(schema)

    def measurements(self) -> tuple[dict[str,Any],...]:
        return node_probe_measurements(self.adjacency)

    def _resource(
        self,
        focal_node:int,
    ) -> np.ndarray:
        n=self.adjacency.shape[0]
        if not 0<=int(focal_node)<n:
            raise ValueError("focal node out of range")
        e=np.zeros(n,dtype=float)
        e[int(focal_node)]=1.0
        h=expm(-self.config.diffusion_time*self.Ln)@e
        h=np.maximum(np.real(h),0.0)
        norm=float(np.linalg.norm(h))
        if norm<=1e-15:
            raise ValueError("heat probe vanished")
        return h/norm

    def _neutral_load(self,r:np.ndarray) -> np.ndarray:
        stress=float(np.mean((1.0-r)**2))
        Y=(
            self.config.neutral_load_scale*(self.Ln@self.Ln)
            +self.config.stress_scale*stress*np.eye(len(r))
        )
        Y=0.5*(Y+Y.T)
        vals,vecs=np.linalg.eigh(Y)
        vals=np.maximum(vals,0.0)
        return (vecs*vals)@vecs.T

    def _formation_operator(self,r:np.ndarray) -> np.ndarray:
        u=r/max(float(np.linalg.norm(r)),1e-15)
        K=(
            self.Ln
            +self.config.formation_offset*np.eye(len(r))
            -self.config.formation_drive*np.outer(u,u)
        )
        return 0.5*(K+K.T)

    def _recursive_operator(self) -> np.ndarray:
        vals,vecs=np.linalg.eigh(0.5*(self.L+self.L.T))
        order=np.argsort(vals)
        vals=vals[order]
        vecs=vecs[:,order]
        r=min(
            max(2,int(self.config.persistent_rank)),
            len(vals),
        )
        denom=max(float(vals[-1]),1e-12)
        phase=np.exp(
            1j*self.config.phase_scale*vals[:r]/denom
        )
        spec=np.concatenate([
            phase,
            np.full(
                len(vals)-r,
                self.config.contraction,
                dtype=complex,
            ),
        ])
        return (
            vecs.astype(complex)
            @np.diag(spec)
            @vecs.T.astype(complex)
        )

    def map_measurement_to_state(
        self,
        measurement:Any,
        *,
        generation:int=0,
    ) -> BFGState:
        self.assert_no_retuning()
        focal=int(measurement["focal_node"])
        r=self._resource(focal)
        D=r.astype(complex)
        Y=self._neutral_load(r).astype(complex)
        K=self._formation_operator(r).astype(complex)
        R=self._recursive_operator()

        return BFGState(
            D=D,
            K=K,
            Y=Y,
            R_C=R,
            generation=int(generation),
            name=f"karate_node_{focal}",
            metadata={
                "domain":"zachary_karate_interaction_network",
                "focal_node":focal,
                "weighted_degree":float(
                    self.adjacency[focal].sum()
                ),
                "mapping_fingerprint":self.mapping_fingerprint,
                "club_label_used":False,
            },
        )

    def advance(
        self,
        previous:BFGState,
        step:CoreStep,
        policy:NumericalPolicy,
    ) -> BFGState:
        # Static interaction carrier: no separate empirical next-time state.
        return previous


def prepare_karate_carrier(
    outdir:str|Path,
    *,
    data_path:str|Path=DEFAULT_DATA,
) -> dict[str,str]:
    outdir=Path(outdir)
    outdir.mkdir(parents=True,exist_ok=True)
    carrier=KarateInteractionCarrier(data_path=data_path)

    schema_path=write_carrier_schema(
        carrier.schema,
        outdir/"karate_carrier_schema.json",
    )
    config_path=outdir/"karate_frozen_config.json"
    config_path.write_text(
        json.dumps(
            {
                "status":"EXPLORATORY",
                "heldout_metrics_evaluated":False,
                "config":carrier.config.to_jsonable(),
                "mapping_fingerprint":carrier.mapping_fingerprint,
                "measurements":len(carrier.measurements()),
                "club_labels_used":False,
                "confirmatory_plan_defined":False,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    return {
        "schema":str(schema_path),
        "config":str(config_path),
    }
