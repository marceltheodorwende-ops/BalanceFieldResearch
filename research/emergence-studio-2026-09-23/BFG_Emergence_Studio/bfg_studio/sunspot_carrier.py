from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any
import csv
import hashlib
import json
import math

import numpy as np

from .types import BFGState, CoreStep, NumericalPolicy
from .core import canonical_reclosure, neutral_pair
from .carrier_sdk import (
    CarrierSchema,
    ValidatedCarrierAdapter,
    write_carrier_schema,
)
from .real_validation import HeldoutValidationPlan, plan_fingerprint
from .session import ProvenanceManifest, save_experiment_ledger


DEFAULT_DATA = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "sunspots_annual_1700_2008.csv"
)


@dataclass(frozen=True)
class SunspotCarrierConfig:
    lag: int
    calibration_start_year: int
    calibration_end_year: int
    heldout_start_year: int
    heldout_end_year: int
    mean: float
    std: float

    graph_sigma: float
    temporal_scale: float
    neutral_load_scale: float
    stress_scale: float
    formation_drive: float
    formation_offset: float
    persistent_rank: int
    contraction: float
    phase_scale: float

    ar_ridge: float
    ar_intercept: float
    ar_coefficients: tuple[float, ...]

    neutral_feature_mean: float
    neutral_feature_std: float
    bfg_correction_intercept: float
    bfg_correction_slope: float

    null_feature_name: str
    null_feature_mean: float
    null_feature_std: float
    null_correction_intercept: float
    null_correction_slope: float

    static_blend_alpha: float
    dataset_sha256: str

    def to_jsonable(self):
        return asdict(self)


def _sha256(path: str | Path) -> str:
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""):
            h.update(chunk)
    return h.hexdigest()


def load_sunspots(
    path: str | Path = DEFAULT_DATA,
) -> tuple[np.ndarray,np.ndarray]:
    years=[]
    values=[]
    with Path(path).open(newline="",encoding="utf-8") as f:
        for row in csv.DictReader(f):
            years.append(int(row["YEAR"]))
            values.append(float(row["SUNACTIVITY"]))
    years=np.asarray(years,dtype=int)
    values=np.asarray(values,dtype=float)
    if len(years)!=309 or years[0]!=1700 or years[-1]!=2008:
        raise ValueError("unexpected bundled sunspot snapshot")
    return years,values


def build_window_measurements(
    years: np.ndarray,
    values: np.ndarray,
    lag: int = 12,
) -> list[dict[str,Any]]:
    measurements=[]
    for target_idx in range(lag,len(values)):
        measurements.append({
            "target_index":int(target_idx),
            "target_year":int(years[target_idx]),
            "window_years":
                years[target_idx-lag:target_idx].astype(int).tolist(),
            "window_values":
                values[target_idx-lag:target_idx].astype(float).tolist(),
        })
    return measurements


def _fit_ridge_ar(
    calibration_values: np.ndarray,
    lag: int,
    ridge: float,
    mean: float,
    std: float,
) -> tuple[float,np.ndarray]:
    z=(np.asarray(calibration_values,dtype=float)-mean)/std
    X=[]
    y=[]
    for t in range(lag,len(z)):
        X.append(z[t-lag:t])
        y.append(z[t])
    X=np.asarray(X,dtype=float)
    y=np.asarray(y,dtype=float)
    X1=np.column_stack([np.ones(len(X)),X])
    penalty=np.eye(X1.shape[1])
    penalty[0,0]=0.0
    beta=np.linalg.solve(
        X1.T@X1 + ridge*penalty,
        X1.T@y,
    )
    return float(beta[0]),np.asarray(beta[1:],dtype=float)


def _graph_sigma_from_calibration(
    calibration_values: np.ndarray,
    mean: float,
    std: float,
    lag: int,
) -> float:
    z=(np.asarray(calibration_values,dtype=float)-mean)/std
    diffs=[]
    for t in range(lag,len(z)+1):
        w=z[t-lag:t]
        d=np.abs(w[:,None]-w[None,:])
        tri=d[np.triu_indices(lag,1)]
        diffs.extend(tri[tri>1e-12].tolist())
    return float(max(np.median(diffs),0.10)) if diffs else 1.0


def _window_graph(
    z: np.ndarray,
    graph_sigma: float,
    temporal_scale: float,
) -> tuple[np.ndarray,np.ndarray,np.ndarray]:
    z=np.asarray(z,dtype=float)
    n=len(z)
    idx=np.arange(n,dtype=float)
    dz=z[:,None]-z[None,:]
    dt=idx[:,None]-idx[None,:]
    A=np.exp(
        -(dz*dz)/(2*graph_sigma*graph_sigma)
        -(dt*dt)/(2*temporal_scale*temporal_scale)
    )
    np.fill_diagonal(A,0.0)
    A=0.5*(A+A.T)
    L=np.diag(np.sum(A,axis=1))-A
    scale=max(float(np.linalg.norm(L,2)),1e-12)
    Ln=L/scale
    return A,L,Ln


def _resource_from_window(z: np.ndarray) -> np.ndarray:
    z=np.asarray(z,dtype=float)
    # Fixed monotone map; no held-out calibration.
    return 1.0/(1.0+np.exp(-np.clip(z,-8.0,8.0)))


def _state_vector(
    z: np.ndarray,
    resource: np.ndarray,
) -> np.ndarray:
    z=np.asarray(z,dtype=float)
    resource=np.asarray(resource,dtype=float)
    local=z+1j*np.gradient(z)
    phase=np.angle(local+1e-15)
    D=resource*np.exp(1j*phase)
    norm=float(np.linalg.norm(D))
    if norm<=1e-12:
        D=np.ones(len(z),dtype=complex)/math.sqrt(len(z))
    else:
        D=D/norm
    return D


def _neutral_load_aligned(
    Ln: np.ndarray,
    resource: np.ndarray,
    load_scale: float,
    stress_scale: float,
) -> np.ndarray:
    stress=float(np.mean((1.0-np.asarray(resource,dtype=float))**2))
    Y=load_scale*(Ln@Ln)+stress_scale*stress*np.eye(Ln.shape[0])
    Y=0.5*(Y+Y.T)
    vals,vecs=np.linalg.eigh(Y)
    vals=np.maximum(vals,0.0)
    return (vecs*vals)@vecs.T


def _formation_operator_aligned(
    Ln: np.ndarray,
    resource: np.ndarray,
    formation_drive: float,
    formation_offset: float,
) -> np.ndarray:
    r=np.asarray(resource,dtype=float)
    u=r/max(float(np.linalg.norm(r)),1e-12)
    K=(
        Ln
        + formation_offset*np.eye(Ln.shape[0])
        - formation_drive*np.outer(u,u)
    )
    return 0.5*(K+K.T)


def _recursive_operator_aligned(
    L: np.ndarray,
    persistent_rank: int,
    contraction: float,
    phase_scale: float,
) -> np.ndarray:
    vals,vecs=np.linalg.eigh(0.5*(L+L.T))
    order=np.argsort(vals)
    vals=vals[order]
    vecs=vecs[:,order]
    n=len(vals)
    r=min(max(2,int(persistent_rank)),n)
    denom=max(float(vals[-1]),1e-12)
    phase=np.exp(1j*phase_scale*vals[:r]/denom)
    residual=np.full(n-r,contraction,dtype=complex)
    spec=np.concatenate([phase,residual])
    return (
        vecs.astype(complex)
        @ np.diag(spec)
        @ vecs.T.astype(complex)
    )


def _ordinary_feature(
    name: str,
    z: np.ndarray,
) -> float:
    z=np.asarray(z,dtype=float)
    if name=="diff_volatility":
        return float(np.std(np.diff(z)))
    if name=="level_volatility":
        return float(np.std(z))
    if name=="absolute_slope":
        return float(abs(np.polyfit(np.arange(len(z)),z,1)[0]))
    if name=="range":
        return float(np.max(z)-np.min(z))
    if name=="recent_level":
        return float(z[-1])
    if name=="curvature":
        return float(abs(z[-1]-2*z[-2]+z[-3]))
    raise ValueError(f"unknown ordinary feature: {name}")


ORDINARY_NULL_FEATURES=(
    "diff_volatility",
    "level_volatility",
    "absolute_slope",
    "range",
    "recent_level",
    "curvature",
)


def _fit_adaptive_correction(
    actual: np.ndarray,
    ar: np.ndarray,
    persistence: np.ndarray,
    feature: np.ndarray,
) -> tuple[float,float,float,float,np.ndarray]:
    feature=np.asarray(feature,dtype=float)
    fmean=float(np.mean(feature))
    fstd=float(np.std(feature))
    if fstd<=1e-12:
        q=np.zeros_like(feature)
        fstd=1.0
    else:
        q=(feature-fmean)/fstd

    d=np.asarray(persistence,dtype=float)-np.asarray(ar,dtype=float)
    X=np.column_stack([d,q*d])
    target=np.asarray(actual,dtype=float)-np.asarray(ar,dtype=float)
    beta=np.linalg.lstsq(X,target,rcond=None)[0]
    pred=np.asarray(ar,dtype=float)+X@beta
    return (
        float(beta[0]),
        float(beta[1]),
        fmean,
        fstd,
        pred,
    )


def _rmse(y: np.ndarray,p: np.ndarray) -> float:
    return float(np.sqrt(np.mean((np.asarray(y)-np.asarray(p))**2)))


def _mae(y: np.ndarray,p: np.ndarray) -> float:
    return float(np.mean(np.abs(np.asarray(y)-np.asarray(p))))


class SunspotBFGCarrier(ValidatedCarrierAdapter):
    """
    Frozen annual-sunspot external carrier.

    K, Y and R_C are built from one recurrence graph. This keeps the persistent
    recursive sector and neutral geometry on the controlled [P,Y]=0 stratum.
    """

    def __init__(self,config:SunspotCarrierConfig):
        self.config=config
        schema=CarrierSchema(
            name="Annual Sunspot BFG Carrier",
            domain="solar activity / annual sunspot count",
            description=(
                "12-year causal delay window mapped to a recurrence graph. "
                "Formation, neutral geometry, and recursive persistence are "
                "constructed from the same graph operator."
            ),
            measurement_mapping={
                "D":(
                    "sigmoid-calibrated activity resource with phase from "
                    "standardized level + i*local temporal gradient"
                ),
                "K":(
                    "normalized recurrence-graph Laplacian plus fixed offset "
                    "minus one resource-supported rank-one formation mode"
                ),
                "Y":(
                    "fixed-scale squared normalized graph Laplacian plus scalar "
                    "resource-stress load; PSD and graph-aligned"
                ),
                "R_C":(
                    "same graph eigenbasis: lowest fixed-rank modes have unit "
                    "modulus phase; complement is contractive"
                ),
            },
            invariant_parameters={
                **config.to_jsonable(),
                "forecast_rule":(
                    "AR12 plus a two-coefficient adaptive correction along "
                    "(persistence-AR12); BFG feature is standardized neutral "
                    "retention <D,C_N D>/<D,D>"
                ),
                "matched_null_rule":(
                    "same two-coefficient correction family, but driven by the "
                    "calibration-selected ordinary window statistic"
                ),
                "neutral_pair":"C_N=(I+Y)^-1; B_N=I-C_N",
            },
            empirical_units={
                "YEAR":"calendar year",
                "SUNACTIVITY":"annual sunspot count",
            },
        )
        super().__init__(schema)

    def _standardized_window(self,measurement:dict[str,Any])->np.ndarray:
        values=np.asarray(measurement["window_values"],dtype=float)
        if len(values)!=self.config.lag:
            raise ValueError("window length does not match frozen lag")
        return (values-self.config.mean)/self.config.std

    def map_measurement_to_state(
        self,
        measurement:Any,
        *,
        generation:int=0,
    )->BFGState:
        self.assert_no_retuning()
        z=self._standardized_window(measurement)
        _,L,Ln=_window_graph(
            z,self.config.graph_sigma,self.config.temporal_scale
        )
        resource=_resource_from_window(z)
        D=_state_vector(z,resource)
        Y=_neutral_load_aligned(
            Ln,resource,
            self.config.neutral_load_scale,
            self.config.stress_scale,
        )
        K=_formation_operator_aligned(
            Ln,resource,
            self.config.formation_drive,
            self.config.formation_offset,
        )
        R=_recursive_operator_aligned(
            L,
            self.config.persistent_rank,
            self.config.contraction,
            self.config.phase_scale,
        )
        return BFGState(
            D=D,
            K=K.astype(complex),
            Y=Y.astype(complex),
            R_C=R,
            generation=int(generation),
            name=f"sunspots_{measurement['target_year']}",
            metadata={
                "domain":"annual_sunspots",
                "target_year":int(measurement["target_year"]),
                "window_years":list(measurement["window_years"]),
                "mapping_fingerprint":self.mapping_fingerprint,
            },
        )

    def advance(
        self,
        previous:BFGState,
        step:CoreStep,
        policy:NumericalPolicy,
    )->BFGState:
        # The next empirical year is externally observed, never generated.
        return previous

    def neutral_retention(self,measurement:dict[str,Any])->float:
        state=self.map_measurement_to_state(measurement)
        C,_=neutral_pair(state.Y)
        denom=max(float(np.real(np.vdot(state.D,state.D))),1e-12)
        c=float(np.real(np.vdot(state.D,C@state.D))/denom)
        return float(np.clip(c,0.0,1.0))

    def component_forecasts(
        self,
        measurement:dict[str,Any],
    )->dict[str,float]:
        z=self._standardized_window(measurement)
        persistence=float(measurement["window_values"][-1])
        ar_z=(
            self.config.ar_intercept
            + float(np.dot(
                np.asarray(self.config.ar_coefficients,dtype=float),
                z,
            ))
        )
        ar=self.config.mean+self.config.std*ar_z

        c=self.neutral_retention(measurement)
        cq=(
            (c-self.config.neutral_feature_mean)
            / max(self.config.neutral_feature_std,1e-12)
        )
        bfg_weight=(
            self.config.bfg_correction_intercept
            + self.config.bfg_correction_slope*cq
        )
        bfg=ar+bfg_weight*(persistence-ar)

        ordinary=_ordinary_feature(self.config.null_feature_name,z)
        nq=(
            (ordinary-self.config.null_feature_mean)
            / max(self.config.null_feature_std,1e-12)
        )
        null_weight=(
            self.config.null_correction_intercept
            + self.config.null_correction_slope*nq
        )
        matched_null=ar+null_weight*(persistence-ar)

        static=(
            self.config.static_blend_alpha*persistence
            +(1.0-self.config.static_blend_alpha)*ar
        )
        return {
            "persistence":float(persistence),
            "ar12":float(ar),
            "neutral_retention":float(c),
            "bfg_correction_weight":float(bfg_weight),
            "bfg":float(bfg),
            "null_feature_value":float(ordinary),
            "null_correction_weight":float(null_weight),
            "matched_null":float(matched_null),
            "static_blend":float(static),
        }


def _calibration_endpoints(
    measurements:list[dict[str,Any]],
    values:np.ndarray,
    mean:float,
    std:float,
    ar_intercept:float,
    ar_coefficients:np.ndarray,
)->tuple[np.ndarray,np.ndarray,np.ndarray,list[np.ndarray]]:
    actual=[]
    persistence=[]
    ar=[]
    z_windows=[]
    for m in measurements:
        z=(
            np.asarray(m["window_values"],dtype=float)-mean
        )/std
        actual.append(float(values[int(m["target_index"])]))
        persistence.append(float(m["window_values"][-1]))
        ar_z=ar_intercept+float(np.dot(ar_coefficients,z))
        ar.append(mean+std*ar_z)
        z_windows.append(z)
    return (
        np.asarray(actual,dtype=float),
        np.asarray(persistence,dtype=float),
        np.asarray(ar,dtype=float),
        z_windows,
    )


def prepare_sunspot_validation(
    outdir:str|Path,
    data_path:str|Path=DEFAULT_DATA,
    lag:int=12,
    calibration_end_year:int=1899,
    heldout_start_year:int=1900,
)->dict[str,Any]:
    """
    Calibration-only freeze.

    No held-out target value enters model selection, coefficient fitting, or
    threshold selection in this function.
    """
    outdir=Path(outdir)
    outdir.mkdir(parents=True,exist_ok=True)

    years,values=load_sunspots(data_path)
    dataset_hash=_sha256(data_path)
    if heldout_start_year!=calibration_end_year+1:
        raise ValueError("held-out period must directly follow calibration")

    cal_values=values[years<=calibration_end_year]
    mean=float(np.mean(cal_values))
    std=float(np.std(cal_values))
    if std<=0:
        raise ValueError("degenerate calibration variance")

    # Domain / implementation choices fixed before held-out evaluation.
    ar_ridge=1.0
    temporal_scale=4.0
    stress_scale=0.18
    formation_drive=1.45
    formation_offset=0.20
    persistent_rank=4
    contraction=0.76
    phase_scale=0.40

    ar_intercept,ar_coeff=_fit_ridge_ar(
        cal_values,lag,ar_ridge,mean,std
    )
    graph_sigma=_graph_sigma_from_calibration(
        cal_values,mean,std,lag
    )

    measurements=build_window_measurements(years,values,lag)
    calibration_measurements=[
        m for m in measurements
        if int(m["target_year"])<=calibration_end_year
    ]
    actual,persistence,ar,z_windows=_calibration_endpoints(
        calibration_measurements,
        values,mean,std,ar_intercept,ar_coeff
    )

    # Static one-parameter blend comparator.
    delta=persistence-ar
    denom=float(np.dot(delta,delta))
    static_alpha=(
        float(np.clip(
            np.dot(delta,actual-ar)/denom,0.0,1.0
        ))
        if denom>1e-12 else 0.5
    )
    static_pred=ar+static_alpha*delta

    # Fair ordinary-feature matched null: the family is frozen in source. It may
    # select the best calibration feature but receives the same two regression
    # coefficients as the BFG correction.
    null_candidates=[]
    for feature_name in ORDINARY_NULL_FEATURES:
        feature=np.array([
            _ordinary_feature(feature_name,z)
            for z in z_windows
        ],dtype=float)
        b0,b1,fmean,fstd,pred=_fit_adaptive_correction(
            actual,ar,persistence,feature
        )
        null_candidates.append({
            "feature_name":feature_name,
            "rmse":_rmse(actual,pred),
            "mae":_mae(actual,pred),
            "intercept":b0,
            "slope":b1,
            "feature_mean":fmean,
            "feature_std":fstd,
        })
    null_best=min(null_candidates,key=lambda r:r["rmse"])

    # BFG-only calibration choice: neutral load scale. For each candidate we fit
    # the same two correction coefficients used by the matched null.
    load_grid=(0.01,0.025,0.05,0.10,0.25,0.50,1.0,2.0,4.0,8.0)
    bfg_candidates=[]
    for scale in load_grid:
        neutral=[]
        # Temporary config values for state mapping; correction coefficients below
        # do not affect the neutral state itself.
        cfg=SunspotCarrierConfig(
            lag=lag,
            calibration_start_year=int(years[0]),
            calibration_end_year=calibration_end_year,
            heldout_start_year=heldout_start_year,
            heldout_end_year=int(years[-1]),
            mean=mean,std=std,
            graph_sigma=graph_sigma,
            temporal_scale=temporal_scale,
            neutral_load_scale=float(scale),
            stress_scale=stress_scale,
            formation_drive=formation_drive,
            formation_offset=formation_offset,
            persistent_rank=persistent_rank,
            contraction=contraction,
            phase_scale=phase_scale,
            ar_ridge=ar_ridge,
            ar_intercept=ar_intercept,
            ar_coefficients=tuple(float(x) for x in ar_coeff),
            neutral_feature_mean=0.0,
            neutral_feature_std=1.0,
            bfg_correction_intercept=0.0,
            bfg_correction_slope=0.0,
            null_feature_name=null_best["feature_name"],
            null_feature_mean=null_best["feature_mean"],
            null_feature_std=null_best["feature_std"],
            null_correction_intercept=null_best["intercept"],
            null_correction_slope=null_best["slope"],
            static_blend_alpha=static_alpha,
            dataset_sha256=dataset_hash,
        )
        carrier=SunspotBFGCarrier(cfg)
        neutral=np.array([
            carrier.neutral_retention(m)
            for m in calibration_measurements
        ],dtype=float)
        b0,b1,cmean,cstd,pred=_fit_adaptive_correction(
            actual,ar,persistence,neutral
        )
        bfg_candidates.append({
            "neutral_load_scale":float(scale),
            "rmse":_rmse(actual,pred),
            "mae":_mae(actual,pred),
            "intercept":b0,
            "slope":b1,
            "feature_mean":cmean,
            "feature_std":cstd,
        })
    bfg_best=min(bfg_candidates,key=lambda r:r["rmse"])

    config=SunspotCarrierConfig(
        lag=lag,
        calibration_start_year=int(years[0]),
        calibration_end_year=calibration_end_year,
        heldout_start_year=heldout_start_year,
        heldout_end_year=int(years[-1]),
        mean=mean,std=std,
        graph_sigma=graph_sigma,
        temporal_scale=temporal_scale,
        neutral_load_scale=bfg_best["neutral_load_scale"],
        stress_scale=stress_scale,
        formation_drive=formation_drive,
        formation_offset=formation_offset,
        persistent_rank=persistent_rank,
        contraction=contraction,
        phase_scale=phase_scale,
        ar_ridge=ar_ridge,
        ar_intercept=ar_intercept,
        ar_coefficients=tuple(float(x) for x in ar_coeff),
        neutral_feature_mean=bfg_best["feature_mean"],
        neutral_feature_std=bfg_best["feature_std"],
        bfg_correction_intercept=bfg_best["intercept"],
        bfg_correction_slope=bfg_best["slope"],
        null_feature_name=null_best["feature_name"],
        null_feature_mean=null_best["feature_mean"],
        null_feature_std=null_best["feature_std"],
        null_correction_intercept=null_best["intercept"],
        null_correction_slope=null_best["slope"],
        static_blend_alpha=static_alpha,
        dataset_sha256=dataset_hash,
    )
    carrier=SunspotBFGCarrier(config)

    # Calibration-only reclosure audit and rows.
    policy=NumericalPolicy()
    cal_rows=[]
    cal_success=0
    cal_novel=0
    for i,m in enumerate(calibration_measurements):
        f=carrier.component_forecasts(m)
        state,report=carrier.validate_measurement_state(
            m,generation=i,policy=policy
        )
        step=canonical_reclosure(state,policy)
        cal_success+=int(step.success)
        cal_novel+=int(bool(step.spectral_novelty)) if step.success else 0
        cal_rows.append({
            "measurement_index":i,
            "year":int(m["target_year"]),
            "actual":float(values[int(m["target_index"])]),
            **f,
            "mapping_valid":report.valid,
            "reclosure_success":step.success,
            "spectral_novelty":step.spectral_novelty,
            "spectral_mismatch":step.spectral_mismatch,
            "formation_eigenvalue":step.formation_eigenvalue,
            "formation_gap":step.formation_gap,
        })

    cal_actual=np.array([r["actual"] for r in cal_rows])
    calibration_metrics={}
    for name in [
        "bfg","matched_null","static_blend","ar12","persistence"
    ]:
        pred=np.array([r[name] for r in cal_rows],dtype=float)
        calibration_metrics[name]={
            "rmse":_rmse(cal_actual,pred),
            "mae":_mae(cal_actual,pred),
        }

    cal_indices=tuple(
        i for i,m in enumerate(measurements)
        if int(m["target_year"])<=calibration_end_year
    )
    held_indices=tuple(
        i for i,m in enumerate(measurements)
        if int(m["target_year"])>=heldout_start_year
    )

    plan=HeldoutValidationPlan(
        domain="solar activity / annual sunspot count",
        dataset_name="Statsmodels yearly sunspots 1700-2008 snapshot",
        target_statement=(
            "With one frozen 12-year recurrence-graph BFG carrier, the "
            "state-dependent neutral-retention correction will achieve held-out "
            "1900-2008 one-step RMSE at least 1% below an equal-coefficient "
            "calibration-selected ordinary-feature adaptive null, while at least "
            "90% of held-out mapped states pass canonical BFG reclosure."
        ),
        calibration_indices=cal_indices,
        heldout_indices=held_indices,
        null_model_name=(
            "best calibration-selected ordinary one-feature adaptive correction "
            "from six frozen window-statistic candidates"
        ),
        primary_metric="held-out one-step-ahead RMSE",
        success_criterion=(
            "BFG_RMSE <= 0.99 * matched_null_RMSE AND "
            "heldout_reclosure_success_fraction >= 0.90"
        ),
        mapping_fingerprint=carrier.mapping_fingerprint,
    )
    plan.validate()

    # Freeze all artifacts now, before held-out evaluation.
    write_carrier_schema(
        carrier.schema,outdir/"sunspot_carrier_schema.json"
    )
    plan_payload=asdict(plan)
    plan_payload["plan_fingerprint"]=plan_fingerprint(plan)
    plan_payload["calibration_years"]=[
        int(years[0]),calibration_end_year
    ]
    plan_payload["heldout_years"]=[
        heldout_start_year,int(years[-1])
    ]
    (outdir/"sunspot_validation_plan.json").write_text(
        json.dumps(plan_payload,indent=2),encoding="utf-8"
    )

    frozen={
        "config":config.to_jsonable(),
        "mapping_fingerprint":carrier.mapping_fingerprint,
        "plan_fingerprint":plan_fingerprint(plan),
        "dataset_sha256":dataset_hash,
        "calibration_metrics":calibration_metrics,
        "calibration_reclosure_success_fraction":
            cal_success/max(len(calibration_measurements),1),
        "calibration_novelty_fraction_among_successful":
            cal_novel/max(cal_success,1),
        "bfg_neutral_scale_candidates":bfg_candidates,
        "ordinary_null_candidates":null_candidates,
        "heldout_metrics_evaluated":False,
        "calibration_design_note":(
            "This freeze supersedes a rejected calibration-only prototype whose "
            "R_C lacked a persistent sector and whose direct neutral blend did "
            "not beat the calibration null. No held-out metric was evaluated "
            "before this freeze."
        ),
    }
    (outdir/"sunspot_frozen_model.json").write_text(
        json.dumps(frozen,indent=2),encoding="utf-8"
    )

    with (outdir/"sunspot_calibration_forecasts.csv").open(
        "w",newline="",encoding="utf-8"
    ) as f:
        w=csv.DictWriter(f,fieldnames=list(cal_rows[0].keys()))
        w.writeheader();w.writerows(cal_rows)

    (outdir/"SUNSPOT_CALIBRATION_DESIGN_LOG.md").write_text(
        "\n".join([
            "# Sunspot carrier calibration design log",
            "",
            "Held-out years 1900-2008 were not used for coefficient fitting, "
            "feature selection, neutral-load selection, or success-threshold selection.",
            "",
            "An earlier calibration-only prototype was rejected before held-out "
            "evaluation because it had no bounded non-decay persistent sector / "
            "formation-admissible reclosure and its direct BFG blend was inferior "
            "to the calibration null.",
            "",
            "The frozen carrier uses graph-aligned K, Y and R_C so the persistent "
            "sector and neutral geometry share one recurrence-graph basis.",
            "",
            "The BFG correction and matched ordinary-feature null both fit two "
            "linear correction coefficients on calibration. The BFG load scale "
            "is chosen from a declared calibration grid; the matched null chooses "
            "its ordinary feature from six frozen candidates.",
            "",
            f"Frozen mapping fingerprint: `{carrier.mapping_fingerprint}`",
            f"Frozen plan fingerprint: `{plan_fingerprint(plan)}`",
        ])+"\n",
        encoding="utf-8",
    )

    save_experiment_ledger(
        outdir,
        experiment="sunspot_carrier_calibration_freeze",
        seed=None,
        parameters={
            "lag":lag,
            "calibration_years":[int(years[0]),calibration_end_year],
            "heldout_years":[heldout_start_year,int(years[-1])],
            "mapping_fingerprint":carrier.mapping_fingerprint,
            "plan_fingerprint":plan_fingerprint(plan),
            "dataset_sha256":dataset_hash,
        },
        summary=frozen,
        frames=cal_rows,
        name="sunspot_calibration_freeze",
    )

    return {
        "mapping_fingerprint":carrier.mapping_fingerprint,
        "plan_fingerprint":plan_fingerprint(plan),
        "calibration_metrics":calibration_metrics,
        "calibration_reclosure_success_fraction":
            cal_success/max(len(calibration_measurements),1),
        "calibration_novelty_fraction_among_successful":
            cal_novel/max(cal_success,1),
        "neutral_load_scale":config.neutral_load_scale,
        "matched_null_feature":config.null_feature_name,
        "files":{
            "schema":str(outdir/"sunspot_carrier_schema.json"),
            "plan":str(outdir/"sunspot_validation_plan.json"),
            "frozen_model":str(outdir/"sunspot_frozen_model.json"),
            "calibration_forecasts":
                str(outdir/"sunspot_calibration_forecasts.csv"),
            "design_log":
                str(outdir/"SUNSPOT_CALIBRATION_DESIGN_LOG.md"),
        },
    }


def _load_frozen_config(path:str|Path)->SunspotCarrierConfig:
    payload=json.loads(Path(path).read_text(encoding="utf-8"))
    cfg=dict(payload["config"])
    cfg["ar_coefficients"]=tuple(cfg["ar_coefficients"])
    return SunspotCarrierConfig(**cfg)


def validate_sunspot_heldout(
    prepared_dir:str|Path,
    data_path:str|Path=DEFAULT_DATA,
    policy:NumericalPolicy|None=None,
)->dict[str,Any]:
    """
    Evaluate the already-frozen carrier. No fitting or model selection occurs here.
    """
    prepared_dir=Path(prepared_dir)
    policy=policy or NumericalPolicy()

    frozen=json.loads(
        (prepared_dir/"sunspot_frozen_model.json").read_text(encoding="utf-8")
    )
    if frozen.get("heldout_metrics_evaluated") is not False:
        raise ValueError("expected a calibration-only frozen model artifact")

    config=_load_frozen_config(
        prepared_dir/"sunspot_frozen_model.json"
    )
    if _sha256(data_path)!=config.dataset_sha256:
        raise ValueError("dataset hash mismatch")

    carrier=SunspotBFGCarrier(config)
    if carrier.mapping_fingerprint!=frozen["mapping_fingerprint"]:
        raise ValueError("reconstructed carrier fingerprint mismatch")

    plan_payload=json.loads(
        (prepared_dir/"sunspot_validation_plan.json").read_text(encoding="utf-8")
    )
    plan=HeldoutValidationPlan(
        domain=plan_payload["domain"],
        dataset_name=plan_payload["dataset_name"],
        target_statement=plan_payload["target_statement"],
        calibration_indices=tuple(plan_payload["calibration_indices"]),
        heldout_indices=tuple(plan_payload["heldout_indices"]),
        null_model_name=plan_payload["null_model_name"],
        primary_metric=plan_payload["primary_metric"],
        success_criterion=plan_payload["success_criterion"],
        mapping_fingerprint=plan_payload["mapping_fingerprint"],
    )
    plan.validate()
    if plan_fingerprint(plan)!=frozen["plan_fingerprint"]:
        raise ValueError("validation plan fingerprint mismatch")
    if plan.mapping_fingerprint!=carrier.mapping_fingerprint:
        raise ValueError("plan/carrier mapping fingerprint mismatch")

    years,values=load_sunspots(data_path)
    measurements=build_window_measurements(years,values,config.lag)
    held_set=set(plan.heldout_indices)
    cal_set=set(plan.calibration_indices)

    rows=[]
    heldout_success=0
    heldout_novel=0
    for i,m in enumerate(measurements):
        carrier.assert_no_retuning()
        f=carrier.component_forecasts(m)
        state,report=carrier.validate_measurement_state(
            m,generation=i,policy=policy
        )
        step=canonical_reclosure(state,policy)
        split=(
            "calibration" if i in cal_set
            else "heldout" if i in held_set
            else "unused"
        )
        if split=="heldout":
            heldout_success+=int(step.success)
            heldout_novel+=int(bool(step.spectral_novelty)) if step.success else 0
        rows.append({
            "measurement_index":i,
            "year":int(m["target_year"]),
            "split":split,
            "actual":float(values[int(m["target_index"])]),
            **f,
            "mapping_valid":report.valid,
            "reclosure_success":step.success,
            "spectral_novelty":step.spectral_novelty,
            "spectral_mismatch":step.spectral_mismatch,
            "formation_eigenvalue":step.formation_eigenvalue,
            "formation_gap":step.formation_gap,
            "terminal_reason":step.terminal_reason,
        })
        carrier.assert_no_retuning()

    held=[r for r in rows if r["split"]=="heldout"]
    y=np.array([r["actual"] for r in held],dtype=float)

    metrics={}
    for name in [
        "bfg","matched_null","static_blend","ar12","persistence"
    ]:
        pred=np.array([r[name] for r in held],dtype=float)
        metrics[name]={
            "rmse":_rmse(y,pred),
            "mae":_mae(y,pred),
            "correlation":float(np.corrcoef(y,pred)[0,1]),
        }

    reclosure_fraction=heldout_success/max(len(held),1)
    novelty_fraction=heldout_novel/max(heldout_success,1)
    improvement=(
        1.0-metrics["bfg"]["rmse"]/metrics["matched_null"]["rmse"]
    )
    passed=bool(
        metrics["bfg"]["rmse"]
        <=0.99*metrics["matched_null"]["rmse"]
        and reclosure_fraction>=0.90
    )

    result={
        "passed":passed,
        "target_statement":plan.target_statement,
        "success_criterion":plan.success_criterion,
        "mapping_fingerprint":carrier.mapping_fingerprint,
        "plan_fingerprint":plan_fingerprint(plan),
        "dataset_sha256":config.dataset_sha256,
        "calibration_years":[
            config.calibration_start_year,
            config.calibration_end_year,
        ],
        "heldout_years":[
            config.heldout_start_year,
            config.heldout_end_year,
        ],
        "heldout_observations":len(held),
        "heldout_metrics":metrics,
        "heldout_reclosure_success_fraction":reclosure_fraction,
        "heldout_novelty_fraction_among_successful":novelty_fraction,
        "rmse_improvement_vs_matched_null":improvement,
        "frozen_parameters":{
            "lag":config.lag,
            "ar_ridge":config.ar_ridge,
            "neutral_load_scale":config.neutral_load_scale,
            "matched_null_feature":config.null_feature_name,
            "persistent_rank":config.persistent_rank,
            "contraction":config.contraction,
            "phase_scale":config.phase_scale,
            "formation_drive":config.formation_drive,
            "formation_offset":config.formation_offset,
        },
        "interpretation_guard":{
            "empirical_domain_result":True,
            "universal_BFG_validation":False,
            "note":(
                "This is one frozen held-out benchmark of one external carrier. "
                "Passing supports only the declared annual-sunspot statement. "
                "Failing rejects that statement; held-out retuning is not allowed."
            ),
        },
    }

    (prepared_dir/"sunspot_heldout_result.json").write_text(
        json.dumps(result,indent=2),encoding="utf-8"
    )
    with (prepared_dir/"sunspot_all_forecasts.csv").open(
        "w",newline="",encoding="utf-8"
    ) as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys()))
        w.writeheader();w.writerows(rows)

    # Mark frozen artifact as evaluated only after result is committed.
    evaluated=dict(frozen)
    evaluated["heldout_metrics_evaluated"]=True
    evaluated["heldout_result_file"]="sunspot_heldout_result.json"
    (prepared_dir/"sunspot_frozen_model_evaluated.json").write_text(
        json.dumps(evaluated,indent=2),encoding="utf-8"
    )

    save_experiment_ledger(
        prepared_dir,
        experiment="sunspot_heldout_validation",
        seed=None,
        parameters={
            "mapping_fingerprint":carrier.mapping_fingerprint,
            "plan_fingerprint":plan_fingerprint(plan),
            "heldout_years":[
                config.heldout_start_year,
                config.heldout_end_year,
            ],
        },
        summary=result,
        frames=held,
        name="sunspot_heldout_validation",
    )
    return result
