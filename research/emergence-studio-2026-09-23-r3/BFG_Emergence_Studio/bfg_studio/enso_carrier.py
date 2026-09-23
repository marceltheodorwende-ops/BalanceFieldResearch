from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any
import csv
import hashlib
import json

import numpy as np
import pandas as pd

from .types import BFGState, CoreStep, NumericalPolicy
from .core import canonical_reclosure, neutral_pair
from .carrier_sdk import CarrierSchema, ValidatedCarrierAdapter, write_carrier_schema
from .real_validation import HeldoutValidationPlan, plan_fingerprint
from .session import save_experiment_ledger
from .portfolio import ValidationPortfolio, BlindHeldoutGuard


DEFAULT_DATA = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "enso_pacific_sst_monthly_1950_2010.csv"
)

MONTHS = (
    "JAN","FEB","MAR","APR","MAY","JUN",
    "JUL","AUG","SEP","OCT","NOV","DEC",
)

BFG_FEATURE_CANDIDATES = (
    "neutral_retention",
    "formation_rayleigh",
    "crossfed_gain",
    "omega_keep",
    "lambda_up",
    "spectral_mismatch",
)

NULL_FEATURE_CANDIDATES = (
    "diff_volatility",
    "level_volatility",
    "absolute_slope",
    "range",
    "recent_level",
    "curvature",
)

PREFLIGHT_FOLDS = (
    ("1970-12-01","1971-01-01","1983-12-01"),
    ("1983-12-01","1984-01-01","1996-12-01"),
    ("1996-12-01","1997-01-01","2010-12-01"),
)

FUTURE_HELDOUT_START = "2011-01-01"
FUTURE_HELDOUT_END = "2025-12-01"


@dataclass(frozen=True)
class ENSOCarrierConfig:
    lag: int
    development_start: str
    development_end: str
    heldout_start: str
    heldout_end: str

    month_climatology: tuple[float, ...]
    anomaly_mean: float
    anomaly_std: float

    graph_sigma: float
    temporal_scale: float
    neutral_load_scale: float
    stress_scale: float
    formation_drive: float
    formation_offset: float
    persistent_rank: int
    contraction: float
    phase_scale: float

    bfg_feature_name: str
    bfg_feature_mean: float
    bfg_feature_std: float
    bfg_intercept: float
    bfg_slope: float

    null_feature_name: str
    null_feature_mean: float
    null_feature_std: float
    null_intercept: float
    null_slope: float

    development_dataset_sha256: str

    def to_jsonable(self) -> dict[str, Any]:
        return asdict(self)


def _sha256(path: str | Path) -> str:
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""):
            h.update(chunk)
    return h.hexdigest()


def load_enso_monthly(
    path: str | Path = DEFAULT_DATA,
) -> pd.Series:
    df=pd.read_csv(path)
    dates=[]
    values=[]
    for _,row in df.iterrows():
        year=int(row["YEAR"])
        for month_idx,name in enumerate(MONTHS,1):
            dates.append(pd.Timestamp(year=year,month=month_idx,day=1))
            values.append(float(row[name]))
    s=pd.Series(values,index=pd.DatetimeIndex(dates),name="sst")
    if len(s)!=61*12:
        raise ValueError("unexpected ENSO monthly snapshot length")
    if s.index.min()!=pd.Timestamp("1950-01-01"):
        raise ValueError("unexpected ENSO snapshot start")
    if s.index.max()!=pd.Timestamp("2010-12-01"):
        raise ValueError("unexpected ENSO snapshot end")
    return s.astype(float)


def _month_climatology(series: pd.Series) -> tuple[float, ...]:
    values=[]
    for month in range(1,13):
        v=series[series.index.month==month]
        if len(v)==0:
            raise ValueError("missing month in climatology")
        values.append(float(v.mean()))
    return tuple(values)


def _anomaly_series(
    series: pd.Series,
    climatology: tuple[float, ...],
) -> pd.Series:
    vals=[
        float(value)-float(climatology[date.month-1])
        for date,value in series.items()
    ]
    return pd.Series(vals,index=series.index,name="anomaly")


def _graph_sigma(
    anomalies: np.ndarray,
    mean: float,
    std: float,
    lag: int,
) -> float:
    zall=(np.asarray(anomalies,dtype=float)-mean)/std
    diffs=[]
    for t in range(lag,len(zall)+1):
        w=zall[t-lag:t]
        d=np.abs(w[:,None]-w[None,:])
        tri=d[np.triu_indices(lag,1)]
        diffs.extend(tri[tri>1e-12].tolist())
    return float(max(np.median(diffs),0.10)) if diffs else 1.0


def _window_graph(
    z: np.ndarray,
    sigma: float,
    temporal_scale: float,
):
    z=np.asarray(z,dtype=float)
    n=len(z)
    idx=np.arange(n,dtype=float)
    dz=z[:,None]-z[None,:]
    dt=idx[:,None]-idx[None,:]
    A=np.exp(
        -(dz*dz)/(2*sigma*sigma)
        -(dt*dt)/(2*temporal_scale*temporal_scale)
    )
    np.fill_diagonal(A,0.0)
    A=0.5*(A+A.T)
    L=np.diag(A.sum(axis=1))-A
    scale=max(float(np.linalg.norm(L,2)),1e-12)
    return A,L,L/scale


def _resource(z: np.ndarray) -> np.ndarray:
    return 1.0/(1.0+np.exp(-np.clip(np.asarray(z,dtype=float),-8.0,8.0)))


def _state_vector(z: np.ndarray,r: np.ndarray) -> np.ndarray:
    z=np.asarray(z,dtype=float)
    local=z+1j*np.gradient(z)
    phase=np.angle(local+1e-15)
    D=np.asarray(r,dtype=float)*np.exp(1j*phase)
    return D/max(float(np.linalg.norm(D)),1e-12)


def _neutral_load(
    Ln: np.ndarray,
    r: np.ndarray,
    load_scale: float,
    stress_scale: float,
) -> np.ndarray:
    stress=float(np.mean((1.0-r)**2))
    Y=load_scale*(Ln@Ln)+stress_scale*stress*np.eye(len(r))
    vals,vecs=np.linalg.eigh(0.5*(Y+Y.T))
    vals=np.maximum(vals,0.0)
    return (vecs*vals)@vecs.T


def _formation_operator(
    Ln: np.ndarray,
    r: np.ndarray,
    drive: float,
    offset: float,
) -> np.ndarray:
    u=r/max(float(np.linalg.norm(r)),1e-12)
    K=Ln+offset*np.eye(len(r))-drive*np.outer(u,u)
    return 0.5*(K+K.T)


def _recursive_operator(
    L: np.ndarray,
    persistent_rank: int,
    contraction: float,
    phase_scale: float,
) -> np.ndarray:
    vals,vecs=np.linalg.eigh(0.5*(L+L.T))
    order=np.argsort(vals)
    vals=vals[order]
    vecs=vecs[:,order]
    r=min(max(2,int(persistent_rank)),len(vals))
    denom=max(float(vals[-1]),1e-12)
    phase=np.exp(1j*phase_scale*vals[:r]/denom)
    spec=np.concatenate([
        phase,
        np.full(len(vals)-r,contraction,dtype=complex),
    ])
    return vecs.astype(complex)@np.diag(spec)@vecs.T.astype(complex)


def _ordinary_feature(name: str,z: np.ndarray) -> float:
    z=np.asarray(z,dtype=float)
    if name=="diff_volatility":
        return float(np.std(np.diff(z)))
    if name=="level_volatility":
        return float(np.std(z))
    if name=="absolute_slope":
        return float(abs(np.polyfit(np.arange(len(z)),z,1)[0]))
    if name=="range":
        return float(np.ptp(z))
    if name=="recent_level":
        return float(z[-1])
    if name=="curvature":
        return float(abs(z[-1]-2*z[-2]+z[-3]))
    raise ValueError(f"unknown ordinary feature: {name}")


def _fit_correction(
    actual: np.ndarray,
    persistence: np.ndarray,
    feature: np.ndarray,
):
    """
    Equal-complexity adaptive mean-reversion/persistence mixture.

    Endpoint A is climatological zero anomaly.
    Endpoint B is previous-month anomaly persistence.
    """
    feature=np.asarray(feature,dtype=float)
    fm=float(np.mean(feature))
    fs=float(np.std(feature))
    if fs<=1e-12:
        fs=1.0
    q=(feature-fm)/fs
    p=np.asarray(persistence,dtype=float)
    X=np.column_stack([p,q*p])
    beta=np.linalg.lstsq(
        X,
        np.asarray(actual,dtype=float),
        rcond=None,
    )[0]
    pred=X@beta
    return float(beta[0]),float(beta[1]),fm,fs,pred


def _rmse(y,p) -> float:
    return float(np.sqrt(np.mean((np.asarray(y)-np.asarray(p))**2)))


def _mae(y,p) -> float:
    return float(np.mean(np.abs(np.asarray(y)-np.asarray(p))))


class ENSOBFGCarrier(ValidatedCarrierAdapter):
    def __init__(self,config:ENSOCarrierConfig):
        self.config=config
        schema=CarrierSchema(
            name="ENSO Pacific SST BFG Carrier",
            domain="Pacific sea-surface-temperature anomaly / ENSO-like dynamics",
            description=(
                "24-month causal anomaly-window recurrence graph. K, Y and R_C "
                "share one graph geometry; forecast adapts between climatological "
                "mean reversion and anomaly persistence."
            ),
            measurement_mapping={
                "D":"standardized monthly SST-anomaly resource/phase state",
                "K":"graph-aligned formation operator with one resource-supported negative mode",
                "Y":"PSD squared recurrence-graph geometry plus scalar stress",
                "R_C":"same graph eigenbasis with persistent low modes and contractive complement",
            },
            invariant_parameters={
                **config.to_jsonable(),
                "forecast_endpoints":[
                    "zero climatological anomaly",
                    "previous-month anomaly persistence",
                ],
                "adaptive_family":"two coefficients: intercept + standardized feature slope",
                "matched_null":"same coefficient count and same forecast endpoints",
                "climatology_rule":"month-of-year means estimated from development data only",
            },
            empirical_units={
                "date":"calendar month",
                "sst":"degrees Celsius",
                "anomaly":"degrees Celsius relative to development climatology",
            },
        )
        super().__init__(schema)

    def _z(self,window_anomalies):
        x=np.asarray(window_anomalies,dtype=float)
        if len(x)!=self.config.lag:
            raise ValueError("ENSO window length mismatch")
        return (x-self.config.anomaly_mean)/self.config.anomaly_std

    def map_measurement_to_state(
        self,
        measurement:Any,
        *,
        generation:int=0,
    )->BFGState:
        self.assert_no_retuning()
        z=self._z(measurement["window_anomalies"])
        _,L,Ln=_window_graph(
            z,self.config.graph_sigma,self.config.temporal_scale
        )
        r=_resource(z)
        D=_state_vector(z,r)
        Y=_neutral_load(
            Ln,r,self.config.neutral_load_scale,self.config.stress_scale
        )
        K=_formation_operator(
            Ln,r,self.config.formation_drive,self.config.formation_offset
        )
        R=_recursive_operator(
            L,self.config.persistent_rank,
            self.config.contraction,self.config.phase_scale
        )
        return BFGState(
            D=D,
            K=K.astype(complex),
            Y=Y.astype(complex),
            R_C=R,
            generation=generation,
            name=f"enso_{measurement['target_date']}",
            metadata={
                "domain":"enso_pacific_sst",
                "target_date":measurement["target_date"],
                "mapping_fingerprint":self.mapping_fingerprint,
            },
        )

    def advance(self,previous:BFGState,step:CoreStep,policy:NumericalPolicy):
        return previous

    def feature_bundle(
        self,
        measurement:dict[str,Any],
        policy:NumericalPolicy|None=None,
    ):
        policy=policy or NumericalPolicy()
        z=self._z(measurement["window_anomalies"])
        state=self.map_measurement_to_state(measurement)
        step=canonical_reclosure(state,policy)
        C,_=neutral_pair(state.Y)
        denom=max(float(np.real(np.vdot(state.D,state.D))),1e-12)

        bfg={
            "neutral_retention":
                float(np.real(np.vdot(state.D,C@state.D))/denom),
            "formation_rayleigh":
                float(np.real(np.vdot(state.D,state.K@state.D))/denom),
            "crossfed_gain":
                float(step.diagnostics.get("crossfed_gain",np.nan)),
            "omega_keep":
                float(step.omega_keep) if step.omega_keep is not None else np.nan,
            "lambda_up":
                float(step.lambda_up) if step.lambda_up is not None else np.nan,
            "spectral_mismatch":
                float(step.spectral_mismatch)
                if step.spectral_mismatch is not None else np.nan,
        }
        ordinary={
            name:_ordinary_feature(name,z)
            for name in NULL_FEATURE_CANDIDATES
        }
        return bfg,ordinary,bool(step.success),step

    def forecast(self,measurement:dict[str,Any])->dict[str,float]:
        bfg,ordinary,_,_=self.feature_bundle(measurement)
        persistence=float(measurement["previous_anomaly"])

        bf=bfg[self.config.bfg_feature_name]
        bq=(bf-self.config.bfg_feature_mean)/max(
            self.config.bfg_feature_std,1e-12
        )
        bw=self.config.bfg_intercept+self.config.bfg_slope*bq
        bfg_anomaly=bw*persistence

        nf=ordinary[self.config.null_feature_name]
        nq=(nf-self.config.null_feature_mean)/max(
            self.config.null_feature_std,1e-12
        )
        nw=self.config.null_intercept+self.config.null_slope*nq
        null_anomaly=nw*persistence

        month=int(str(measurement["target_date"])[5:7])
        clim=float(self.config.month_climatology[month-1])

        return {
            "previous_anomaly":persistence,
            "bfg_feature":float(bf),
            "bfg_weight":float(bw),
            "bfg_anomaly":float(bfg_anomaly),
            "matched_null_feature":float(nf),
            "matched_null_weight":float(nw),
            "matched_null_anomaly":float(null_anomaly),
            "climatology":clim,
            "bfg_sst":float(clim+bfg_anomaly),
            "matched_null_sst":float(clim+null_anomaly),
        }


def _measurements(
    series:pd.Series,
    climatology:tuple[float,...],
    lag:int,
):
    anomalies=_anomaly_series(series,climatology)
    out=[]
    for t in range(lag,len(series)):
        out.append({
            "target_index":t,
            "target_date":str(series.index[t].date()),
            "window_dates":[str(d.date()) for d in series.index[t-lag:t]],
            "window_anomalies":
                anomalies.iloc[t-lag:t].astype(float).tolist(),
            "actual_sst":float(series.iloc[t]),
            "actual_anomaly":float(anomalies.iloc[t]),
            "previous_anomaly":float(anomalies.iloc[t-1]),
        })
    return out


def _base_parameters(
    train:pd.Series,
    lag:int,
    dataset_hash:str,
)->dict[str,Any]:
    climatology=_month_climatology(train)
    anomalies=_anomaly_series(train,climatology)
    mean=float(anomalies.mean())
    std=float(anomalies.std(ddof=0))
    if std<=0:
        raise ValueError("degenerate ENSO anomaly variance")
    sigma=_graph_sigma(anomalies.values,mean,std,lag)
    return {
        "lag":lag,
        "development_start":str(train.index.min().date()),
        "development_end":str(train.index.max().date()),
        "heldout_start":FUTURE_HELDOUT_START,
        "heldout_end":FUTURE_HELDOUT_END,
        "month_climatology":tuple(float(x) for x in climatology),
        "anomaly_mean":mean,
        "anomaly_std":std,
        "graph_sigma":sigma,
        "temporal_scale":6.0,
        "neutral_load_scale":0.42,
        "stress_scale":0.18,
        "formation_drive":1.45,
        "formation_offset":0.20,
        "persistent_rank":4,
        "contraction":0.76,
        "phase_scale":0.40,
        "development_dataset_sha256":dataset_hash,
    }


def _temporary_config(base:dict[str,Any])->ENSOCarrierConfig:
    return ENSOCarrierConfig(
        **base,
        bfg_feature_name=BFG_FEATURE_CANDIDATES[0],
        bfg_feature_mean=0.0,bfg_feature_std=1.0,
        bfg_intercept=0.0,bfg_slope=0.0,
        null_feature_name=NULL_FEATURE_CANDIDATES[0],
        null_feature_mean=0.0,null_feature_std=1.0,
        null_intercept=0.0,null_slope=0.0,
    )


def _select_features(
    carrier:ENSOBFGCarrier,
    measurements:list[dict[str,Any]],
):
    bundles=[]
    for m in measurements:
        bfg,null,success,_=carrier.feature_bundle(m)
        bundles.append((bfg,null,success))

    actual=np.asarray([m["actual_anomaly"] for m in measurements])
    persistence=np.asarray([m["previous_anomaly"] for m in measurements])

    def select(names,idx):
        best=None
        rows=[]
        for name in names:
            feature=np.asarray(
                [b[idx][name] for b in bundles],
                dtype=float,
            )
            if not np.all(np.isfinite(feature)):
                continue
            b0,b1,fm,fs,pred=_fit_correction(
                actual,persistence,feature
            )
            row={
                "feature":name,
                "rmse":_rmse(actual,pred),
                "mae":_mae(actual,pred),
                "intercept":b0,
                "slope":b1,
                "feature_mean":fm,
                "feature_std":fs,
            }
            rows.append(row)
            if best is None or row["rmse"]<best["rmse"]:
                best=row
        if best is None:
            raise RuntimeError("no finite ENSO feature candidate")
        return best,rows

    bfg_best,bfg_rows=select(BFG_FEATURE_CANDIDATES,0)
    null_best,null_rows=select(NULL_FEATURE_CANDIDATES,1)
    reclosure=float(np.mean([b[2] for b in bundles]))
    return bfg_best,null_best,bfg_rows,null_rows,reclosure


def _fixed_config(
    base:dict[str,Any],
    bfg_best:dict[str,Any],
    null_best:dict[str,Any],
)->ENSOCarrierConfig:
    return ENSOCarrierConfig(
        **base,
        bfg_feature_name=bfg_best["feature"],
        bfg_feature_mean=bfg_best["feature_mean"],
        bfg_feature_std=bfg_best["feature_std"],
        bfg_intercept=bfg_best["intercept"],
        bfg_slope=bfg_best["slope"],
        null_feature_name=null_best["feature"],
        null_feature_mean=null_best["feature_mean"],
        null_feature_std=null_best["feature_std"],
        null_intercept=null_best["intercept"],
        null_slope=null_best["slope"],
    )


def _evaluate_fixed(
    carrier:ENSOBFGCarrier,
    measurements:list[dict[str,Any]],
):
    rows=[]
    successful=0
    novel=0
    for i,m in enumerate(measurements):
        f=carrier.forecast(m)
        state,report=carrier.validate_measurement_state(m,generation=i)
        step=canonical_reclosure(state,NumericalPolicy())
        successful+=int(step.success)
        novel+=int(bool(step.spectral_novelty)) if step.success else 0
        rows.append({
            "target_date":m["target_date"],
            "actual_sst":m["actual_sst"],
            "actual_anomaly":m["actual_anomaly"],
            **f,
            "mapping_valid":report.valid,
            "reclosure_success":step.success,
            "spectral_novelty":step.spectral_novelty,
        })

    actual=np.asarray([r["actual_anomaly"] for r in rows])
    bfg=np.asarray([r["bfg_anomaly"] for r in rows])
    null=np.asarray([r["matched_null_anomaly"] for r in rows])
    return {
        "bfg_rmse":_rmse(actual,bfg),
        "null_rmse":_rmse(actual,null),
        "relative_improvement":1.0-_rmse(actual,bfg)/_rmse(actual,null),
        "reclosure_fraction":successful/max(len(rows),1),
        "novelty_fraction_among_successful":novel/max(successful,1),
        "rows":rows,
    }


def _preflight_fold(
    full_series:pd.Series,
    dataset_hash:str,
    lag:int,
    train_end:str,
    eval_start:str,
    eval_end:str,
):
    train=full_series.loc[:pd.Timestamp(train_end)]
    base=_base_parameters(train,lag,dataset_hash)
    temp=ENSOBFGCarrier(_temporary_config(base))

    train_measurements=_measurements(
        train,base["month_climatology"],lag
    )
    bfg_best,null_best,_,_,train_reclosure=_select_features(
        temp,train_measurements
    )
    config=_fixed_config(base,bfg_best,null_best)
    carrier=ENSOBFGCarrier(config)

    # Evaluation anomalies use only the training climatology frozen above.
    through_eval=full_series.loc[:pd.Timestamp(eval_end)]
    all_m=_measurements(
        through_eval,config.month_climatology,lag
    )
    evaluation=[
        m for m in all_m
        if pd.Timestamp(eval_start)
        <=pd.Timestamp(m["target_date"])
        <=pd.Timestamp(eval_end)
    ]
    ev=_evaluate_fixed(carrier,evaluation)

    return {
        "train_end":train_end,
        "eval_start":eval_start,
        "eval_end":eval_end,
        "bfg_feature":bfg_best["feature"],
        "null_feature":null_best["feature"],
        "train_reclosure_fraction":train_reclosure,
        "bfg_rmse":ev["bfg_rmse"],
        "null_rmse":ev["null_rmse"],
        "relative_improvement":ev["relative_improvement"],
        "eval_reclosure_fraction":ev["reclosure_fraction"],
        "eval_novelty_fraction_among_successful":
            ev["novelty_fraction_among_successful"],
    }


def prepare_enso_validation(
    outdir:str|Path,
    data_path:str|Path=DEFAULT_DATA,
    lag:int=24,
):
    """
    Development-only readiness preparation.

    The bundled 1950-2010 NOAA/Statsmodels series is entirely development data.
    Prospective monthly continuation 2011-2025 is not bundled or scored here.
    """
    outdir=Path(outdir)
    outdir.mkdir(parents=True,exist_ok=True)

    series=load_enso_monthly(data_path)
    dataset_hash=_sha256(data_path)

    folds=[
        _preflight_fold(
            series,dataset_hash,lag,*fold
        )
        for fold in PREFLIGHT_FOLDS
    ]
    wins=sum(f["relative_improvement"]>0 for f in folds)
    mean_improvement=float(np.mean([
        f["relative_improvement"] for f in folds
    ]))
    worst_improvement=float(np.min([
        f["relative_improvement"] for f in folds
    ]))
    min_reclosure=float(np.min([
        f["eval_reclosure_fraction"] for f in folds
    ]))

    readiness=bool(
        wins>=2
        and mean_improvement>0
        and worst_improvement>=-0.02
        and min_reclosure>=0.95
    )

    base=_base_parameters(series,lag,dataset_hash)
    temp=ENSOBFGCarrier(_temporary_config(base))
    development_measurements=_measurements(
        series,base["month_climatology"],lag
    )
    bfg_best,null_best,bfg_candidates,null_candidates,_=_select_features(
        temp,development_measurements
    )
    config=_fixed_config(base,bfg_best,null_best)
    carrier=ENSOBFGCarrier(config)
    full=_evaluate_fixed(carrier,development_measurements)

    # Future indices are prospective placeholders only.
    development_indices=tuple(range(len(development_measurements)))
    heldout_months=15*12
    heldout_indices=tuple(
        range(
            len(development_measurements),
            len(development_measurements)+heldout_months,
        )
    )
    plan=HeldoutValidationPlan(
        domain="Pacific SST anomaly / ENSO-like dynamics",
        dataset_name=(
            "NOAA Pacific monthly SST 1950-2010 development snapshot; "
            "prospective monthly continuation 2011-2025"
        ),
        target_statement=(
            "With one frozen 24-month graph-aligned ENSO carrier, the BFG-feature "
            "adaptive mean-reversion/persistence correction will achieve lower "
            "2011-2025 monthly anomaly RMSE than an equal-coefficient matched "
            "ordinary-feature correction, while at least 95% of mapped future "
            "states pass canonical BFG reclosure."
        ),
        calibration_indices=development_indices,
        heldout_indices=heldout_indices,
        null_model_name=(
            "equal-coefficient adaptive correction using the best development-"
            "selected feature from six frozen ordinary anomaly-window statistics"
        ),
        primary_metric="prospective monthly SST-anomaly one-step RMSE",
        success_criterion=(
            "BFG_RMSE < matched_null_RMSE AND "
            "heldout_reclosure_success_fraction >= 0.95"
        ),
        mapping_fingerprint=carrier.mapping_fingerprint,
    )
    plan.validate()

    preflight={
        "readiness":readiness,
        "status":"READY_FOR_VALIDATION" if readiness else "NOT_YET_VALIDATED",
        "folds":folds,
        "fold_wins":wins,
        "folds_total":len(folds),
        "mean_relative_improvement":mean_improvement,
        "worst_relative_improvement":worst_improvement,
        "minimum_eval_reclosure_fraction":min_reclosure,
        "readiness_rule":{
            "fold_wins_min":2,
            "mean_relative_improvement_gt":0.0,
            "worst_fold_relative_improvement_min":-0.02,
            "minimum_reclosure_fraction":0.95,
        },
        "full_development":{
            "period":[
                str(series.index.min().date()),
                str(series.index.max().date()),
            ],
            "bfg_feature":bfg_best["feature"],
            "null_feature":null_best["feature"],
            "bfg_rmse":full["bfg_rmse"],
            "null_rmse":full["null_rmse"],
            "relative_improvement":full["relative_improvement"],
            "reclosure_fraction":full["reclosure_fraction"],
            "novelty_fraction_among_successful":
                full["novelty_fraction_among_successful"],
        },
        "heldout_period":[FUTURE_HELDOUT_START,FUTURE_HELDOUT_END],
        "heldout_metrics_evaluated":False,
    }

    write_carrier_schema(
        carrier.schema,outdir/"enso_carrier_schema.json"
    )
    plan_payload=asdict(plan)
    plan_payload["plan_fingerprint"]=plan_fingerprint(plan)
    plan_payload["development_period"]=[
        str(series.index.min().date()),
        str(series.index.max().date()),
    ]
    plan_payload["heldout_period"]=[
        FUTURE_HELDOUT_START,FUTURE_HELDOUT_END
    ]
    plan_payload["heldout_data_bundled"]=False
    (outdir/"enso_validation_plan.json").write_text(
        json.dumps(plan_payload,indent=2),encoding="utf-8"
    )

    frozen={
        "config":config.to_jsonable(),
        "mapping_fingerprint":carrier.mapping_fingerprint,
        "plan_fingerprint":plan_fingerprint(plan),
        "development_dataset_sha256":dataset_hash,
        "bfg_candidates":bfg_candidates,
        "null_candidates":null_candidates,
        "preflight":preflight,
        "heldout_metrics_evaluated":False,
    }
    (outdir/"enso_frozen_model.json").write_text(
        json.dumps(frozen,indent=2),encoding="utf-8"
    )
    (outdir/"enso_preflight.json").write_text(
        json.dumps(preflight,indent=2),encoding="utf-8"
    )

    if readiness:
        token_payload={
            "mapping_fingerprint":carrier.mapping_fingerprint,
            "plan_fingerprint":plan_fingerprint(plan),
            "preflight_sha256":_sha256(outdir/"enso_preflight.json"),
            "future_heldout_period":[
                FUTURE_HELDOUT_START,FUTURE_HELDOUT_END
            ],
        }
        canonical=json.dumps(
            token_payload,sort_keys=True,separators=(",",":")
        ).encode("utf-8")
        token_payload["readiness_token"]=hashlib.sha256(
            canonical
        ).hexdigest()
        (outdir/"ENSO_READINESS_TOKEN.json").write_text(
            json.dumps(token_payload,indent=2),encoding="utf-8"
        )

    save_experiment_ledger(
        outdir,
        experiment="enso_validation_preflight",
        seed=None,
        parameters={
            "mapping_fingerprint":carrier.mapping_fingerprint,
            "plan_fingerprint":plan_fingerprint(plan),
            "lag":lag,
            "development_period":preflight["full_development"]["period"],
            "heldout_period":preflight["heldout_period"],
        },
        summary=preflight,
        frames=folds,
        name="enso_preflight",
    )

    return {
        "status":preflight["status"],
        "readiness":readiness,
        "mapping_fingerprint":carrier.mapping_fingerprint,
        "plan_fingerprint":plan_fingerprint(plan),
        "preflight":preflight,
        "heldout_metrics_evaluated":False,
    }


def load_future_enso_monthly(
    path:str|Path,
    start:str=FUTURE_HELDOUT_START,
    end:str=FUTURE_HELDOUT_END,
)->pd.Series:
    """
    Expected CSV columns: date,sst for every month in the prospective block.
    """
    df=pd.read_csv(path,parse_dates=["date"])
    if "sst" not in df.columns:
        raise ValueError("future ENSO file must contain date,sst")
    s=df.set_index("date")["sst"].astype(float).sort_index()
    expected=pd.date_range(pd.Timestamp(start),pd.Timestamp(end),freq="MS")
    if not s.index.equals(expected):
        raise ValueError(
            "future ENSO file must contain every prospective month exactly once"
        )
    return s


def validate_enso_future(
    prepared_dir:str|Path,
    future_data_path:str|Path,
    permit_path:str|Path,
    development_data_path:str|Path=DEFAULT_DATA,
):
    prepared_dir=Path(prepared_dir)
    frozen=json.loads(
        (prepared_dir/"enso_frozen_model.json").read_text(encoding="utf-8")
    )
    if frozen.get("heldout_metrics_evaluated") is not False:
        raise RuntimeError("ENSO prospective plan already evaluated")

    portfolio=ValidationPortfolio()
    guard=BlindHeldoutGuard(portfolio)
    guard.validate_confirmation_permit("enso-pacific-sst",permit_path)

    cfg=dict(frozen["config"])
    cfg["month_climatology"]=tuple(cfg["month_climatology"])
    config=ENSOCarrierConfig(**cfg)
    carrier=ENSOBFGCarrier(config)
    if carrier.mapping_fingerprint!=frozen["mapping_fingerprint"]:
        raise RuntimeError("ENSO mapping fingerprint mismatch")
    if _sha256(development_data_path)!=config.development_dataset_sha256:
        raise RuntimeError("ENSO development snapshot changed")

    development=load_enso_monthly(development_data_path)

    # Confirmation is spent before future targets are loaded.
    permit_audit=guard.consume_confirmation_permit(
        "enso-pacific-sst",permit_path
    )
    future=load_future_enso_monthly(future_data_path)
    combined=pd.concat([development,future])

    measurements=_measurements(
        combined,config.month_climatology,config.lag
    )
    held=[
        m for m in measurements
        if pd.Timestamp(config.heldout_start)
        <=pd.Timestamp(m["target_date"])
        <=pd.Timestamp(config.heldout_end)
    ]
    ev=_evaluate_fixed(carrier,held)
    passed=bool(
        ev["bfg_rmse"]<ev["null_rmse"]
        and ev["reclosure_fraction"]>=0.95
    )
    result={
        "passed":passed,
        "heldout_period":[config.heldout_start,config.heldout_end],
        "heldout_observations":len(held),
        "future_dataset_sha256":_sha256(future_data_path),
        "bfg_rmse":ev["bfg_rmse"],
        "matched_null_rmse":ev["null_rmse"],
        "relative_improvement":ev["relative_improvement"],
        "heldout_reclosure_success_fraction":ev["reclosure_fraction"],
        "heldout_novelty_fraction_among_successful":
            ev["novelty_fraction_among_successful"],
        "mapping_fingerprint":carrier.mapping_fingerprint,
        "plan_fingerprint":frozen["plan_fingerprint"],
        "confirmation_permit":permit_audit,
        "retuning_after_heldout":False,
    }
    result_path=prepared_dir/"enso_future_heldout_result.json"
    result_path.write_text(
        json.dumps(result,indent=2),encoding="utf-8"
    )

    try:
        result_rel=str(result_path.relative_to(portfolio.project_root))
    except ValueError:
        result_rel=str(result_path)
    portfolio.record_confirmatory_result(
        "enso-pacific-sst",
        passed=passed,
        result_artifact=result_rel,
        metrics={
            "bfg_rmse":ev["bfg_rmse"],
            "matched_null_rmse":ev["null_rmse"],
            "relative_improvement":ev["relative_improvement"],
            "heldout_reclosure_success_fraction":
                ev["reclosure_fraction"],
        },
    )
    return result
