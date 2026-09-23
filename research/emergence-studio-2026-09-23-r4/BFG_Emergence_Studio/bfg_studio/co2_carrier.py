from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any
import csv
import hashlib
import json
import math

import numpy as np
import pandas as pd

from .types import BFGState, CoreStep, NumericalPolicy
from .core import canonical_reclosure, neutral_pair
from .carrier_sdk import CarrierSchema, ValidatedCarrierAdapter, write_carrier_schema
from .real_validation import HeldoutValidationPlan, plan_fingerprint
from .session import save_experiment_ledger
from .portfolio import ValidationPortfolio, BlindHeldoutGuard


DEFAULT_DATA=(
    Path(__file__).resolve().parent.parent
    / "data"
    / "mauna_loa_co2_weekly_1958_2001.csv"
)

BFG_FEATURE_CANDIDATES=(
    "neutral_retention",
    "formation_rayleigh",
    "crossfed_gain",
    "omega_keep",
    "lambda_up",
    "spectral_mismatch",
)

NULL_FEATURE_CANDIDATES=(
    "diff_volatility",
    "level_volatility",
    "absolute_slope",
    "range",
    "recent_level",
    "curvature",
)

PREFLIGHT_FOLDS=(
    ("1975-12-01","1976-01-01","1980-12-01"),
    ("1980-12-01","1981-01-01","1985-12-01"),
    ("1985-12-01","1986-01-01","1990-12-01"),
)


@dataclass(frozen=True)
class CO2CarrierConfig:
    lag:int
    calibration_end:str
    heldout_start:str
    heldout_end:str
    mean:float
    std:float
    graph_sigma:float
    temporal_scale:float
    neutral_load_scale:float
    stress_scale:float
    formation_drive:float
    formation_offset:float
    persistent_rank:int
    contraction:float
    phase_scale:float

    bfg_feature_name:str
    bfg_feature_mean:float
    bfg_feature_std:float
    bfg_intercept:float
    bfg_slope:float

    null_feature_name:str
    null_feature_mean:float
    null_feature_std:float
    null_intercept:float
    null_slope:float

    dataset_sha256:str

    def to_jsonable(self):
        return asdict(self)


def _sha256(path:str|Path)->str:
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""):
            h.update(chunk)
    return h.hexdigest()


def load_weekly_co2(path:str|Path=DEFAULT_DATA)->pd.Series:
    df=pd.read_csv(path,parse_dates=["date"])
    s=df.set_index("date")["co2"].astype(float)
    if s.index.min()!=pd.Timestamp("1958-03-29"):
        raise ValueError("unexpected CO2 snapshot start")
    if s.index.max()!=pd.Timestamp("2001-12-29"):
        raise ValueError("unexpected CO2 snapshot end")
    return s


def _monthly_for_split(s:pd.Series,start=None,end=None)->pd.Series:
    x=s.copy()
    if start is not None:
        x=x.loc[pd.Timestamp(start):]
    if end is not None:
        x=x.loc[:pd.Timestamp(end)]
    monthly=x.resample("MS").mean()
    monthly=monthly.interpolate("time",limit_direction="both")
    if monthly.isna().any():
        raise ValueError("monthly CO2 transform left missing values")
    return monthly.astype(float)


def load_monthly_calibration(
    path:str|Path=DEFAULT_DATA,
    calibration_end:str="1990-12-31",
)->pd.Series:
    return _monthly_for_split(load_weekly_co2(path),end=calibration_end)


def load_monthly_heldout(
    path:str|Path=DEFAULT_DATA,
    heldout_start:str="1991-01-01",
)->pd.Series:
    return _monthly_for_split(load_weekly_co2(path),start=heldout_start)


def _graph_sigma(values:np.ndarray,mean:float,std:float,lag:int)->float:
    zall=(np.asarray(values,dtype=float)-mean)/std
    diffs=[]
    for t in range(lag,len(zall)+1):
        w=zall[t-lag:t]
        d=np.abs(w[:,None]-w[None,:])
        tri=d[np.triu_indices(lag,1)]
        diffs.extend(tri[tri>1e-12].tolist())
    return float(max(np.median(diffs),0.10)) if diffs else 1.0


def _window_graph(z:np.ndarray,sigma:float,temporal_scale:float):
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


def _resource(z:np.ndarray)->np.ndarray:
    return 1.0/(1.0+np.exp(-np.clip(z,-8.0,8.0)))


def _state_vector(z:np.ndarray,r:np.ndarray)->np.ndarray:
    local=np.asarray(z,dtype=float)+1j*np.gradient(np.asarray(z,dtype=float))
    phase=np.angle(local+1e-15)
    D=np.asarray(r,dtype=float)*np.exp(1j*phase)
    return D/max(float(np.linalg.norm(D)),1e-12)


def _neutral_load(
    Ln:np.ndarray,r:np.ndarray,load_scale:float,stress_scale:float
)->np.ndarray:
    stress=float(np.mean((1.0-r)**2))
    Y=load_scale*(Ln@Ln)+stress_scale*stress*np.eye(len(r))
    vals,vecs=np.linalg.eigh(0.5*(Y+Y.T))
    vals=np.maximum(vals,0.0)
    return (vecs*vals)@vecs.T


def _formation_operator(
    Ln:np.ndarray,r:np.ndarray,drive:float,offset:float
)->np.ndarray:
    u=r/max(float(np.linalg.norm(r)),1e-12)
    K=Ln+offset*np.eye(len(r))-drive*np.outer(u,u)
    return 0.5*(K+K.T)


def _recursive_operator(
    L:np.ndarray,persistent_rank:int,contraction:float,phase_scale:float
)->np.ndarray:
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


def _ordinary_feature(name:str,z:np.ndarray)->float:
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
    actual:np.ndarray,
    seasonal:np.ndarray,
    drift:np.ndarray,
    feature:np.ndarray,
):
    feature=np.asarray(feature,dtype=float)
    fm=float(np.mean(feature))
    fs=float(np.std(feature))
    if fs<=1e-12:
        fs=1.0
    q=(feature-fm)/fs
    d=np.asarray(drift)-np.asarray(seasonal)
    X=np.column_stack([d,q*d])
    beta=np.linalg.lstsq(
        X,
        np.asarray(actual)-np.asarray(seasonal),
        rcond=None,
    )[0]
    pred=np.asarray(seasonal)+X@beta
    return float(beta[0]),float(beta[1]),fm,fs,pred


def _rmse(y,p):
    return float(np.sqrt(np.mean((np.asarray(y)-np.asarray(p))**2)))


class CO2BFGCarrier(ValidatedCarrierAdapter):
    def __init__(self,config:CO2CarrierConfig):
        self.config=config
        schema=CarrierSchema(
            name="Mauna Loa Monthly CO2 BFG Carrier",
            domain="atmospheric CO2 / monthly Mauna Loa measurements",
            description=(
                "24-month causal recurrence-graph carrier with graph-aligned "
                "formation, neutral load, and recursive persistence."
            ),
            measurement_mapping={
                "D":"standardized monthly delay state with resource/phase embedding",
                "K":"graph-aligned formation operator with one rank-one negative mode",
                "Y":"PSD squared graph geometry plus scalar stress",
                "R_C":"graph eigenbasis with persistent low modes and contractive complement",
            },
            invariant_parameters={
                **config.to_jsonable(),
                "forecast_endpoints":[
                    "seasonal persistence y[t-12]",
                    "seasonal drift y[t-12] + y[t-1]-y[t-13]",
                ],
                "adaptive_family":"two coefficients: intercept + standardized feature slope",
                "matched_null":"same coefficient count and same forecast endpoints",
            },
            empirical_units={
                "date":"calendar month",
                "co2":"parts per million",
            },
        )
        super().__init__(schema)

    def _z(self,window_values):
        x=np.asarray(window_values,dtype=float)
        if len(x)!=self.config.lag:
            raise ValueError("window length mismatch")
        return (x-self.config.mean)/self.config.std

    def map_measurement_to_state(self,measurement:Any,*,generation:int=0):
        z=self._z(measurement["window_values"])
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
            D=D,K=K.astype(complex),Y=Y.astype(complex),R_C=R,
            generation=generation,
            name=f"co2_{measurement['target_date']}",
            metadata={
                "domain":"mauna_loa_monthly_co2",
                "target_date":measurement["target_date"],
                "mapping_fingerprint":self.mapping_fingerprint,
            },
        )

    def advance(self,previous:BFGState,step:CoreStep,policy:NumericalPolicy):
        return previous

    def feature_bundle(self,measurement:dict[str,Any])->tuple[dict,dict,bool]:
        z=self._z(measurement["window_values"])
        state=self.map_measurement_to_state(measurement)
        step=canonical_reclosure(state,NumericalPolicy())
        C,_=neutral_pair(state.Y)
        denom=max(float(np.real(np.vdot(state.D,state.D))),1e-12)
        bfg={
            "neutral_retention":
                float(np.real(np.vdot(state.D,C@state.D))/denom),
            "formation_rayleigh":
                float(np.real(np.vdot(state.D,state.K@state.D))/denom),
            "crossfed_gain":
                float(step.diagnostics.get("crossfed_gain",np.nan)),
            "omega_keep":float(step.omega_keep) if step.omega_keep is not None else np.nan,
            "lambda_up":float(step.lambda_up) if step.lambda_up is not None else np.nan,
            "spectral_mismatch":
                float(step.spectral_mismatch) if step.spectral_mismatch is not None else np.nan,
        }
        null={name:_ordinary_feature(name,z) for name in NULL_FEATURE_CANDIDATES}
        return bfg,null,bool(step.success)

    def forecast(self,measurement:dict[str,Any])->dict[str,float]:
        bfg,null,_=self.feature_bundle(measurement)
        seasonal=float(measurement["seasonal_endpoint"])
        drift=float(measurement["drift_endpoint"])

        bf=bfg[self.config.bfg_feature_name]
        bq=(bf-self.config.bfg_feature_mean)/max(self.config.bfg_feature_std,1e-12)
        bw=self.config.bfg_intercept+self.config.bfg_slope*bq
        bfg_pred=seasonal+bw*(drift-seasonal)

        nf=null[self.config.null_feature_name]
        nq=(nf-self.config.null_feature_mean)/max(self.config.null_feature_std,1e-12)
        nw=self.config.null_intercept+self.config.null_slope*nq
        null_pred=seasonal+nw*(drift-seasonal)

        return {
            "seasonal":seasonal,
            "drift":drift,
            "bfg_feature":float(bf),
            "bfg_weight":float(bw),
            "bfg":float(bfg_pred),
            "null_feature":float(nf),
            "null_weight":float(nw),
            "matched_null":float(null_pred),
        }


def _measurements_from_monthly(monthly:pd.Series,lag:int)->list[dict[str,Any]]:
    y=monthly.values.astype(float)
    dates=monthly.index
    out=[]
    for t in range(lag,len(y)):
        # lag>=24, so all seasonal endpoints are causal.
        out.append({
            "target_index":int(t),
            "target_date":str(dates[t].date()),
            "window_dates":[str(d.date()) for d in dates[t-lag:t]],
            "window_values":y[t-lag:t].tolist(),
            "actual":float(y[t]),
            "seasonal_endpoint":float(y[t-12]),
            "drift_endpoint":float(y[t-12]+(y[t-1]-y[t-13])),
        })
    return out


def _select_models(
    measurements:list[dict[str,Any]],
    mean:float,std:float,sigma:float,
    base_config:dict,
):
    tmp_cfg=CO2CarrierConfig(
        **base_config,
        mean=mean,std=std,graph_sigma=sigma,
        bfg_feature_name=BFG_FEATURE_CANDIDATES[0],
        bfg_feature_mean=0.0,bfg_feature_std=1.0,
        bfg_intercept=0.0,bfg_slope=0.0,
        null_feature_name=NULL_FEATURE_CANDIDATES[0],
        null_feature_mean=0.0,null_feature_std=1.0,
        null_intercept=0.0,null_slope=0.0,
    )
    carrier=CO2BFGCarrier(tmp_cfg)
    bundles=[]
    for m in measurements:
        b,n,ok=carrier.feature_bundle(m)
        bundles.append((b,n,ok))

    actual=np.array([m["actual"] for m in measurements])
    seasonal=np.array([m["seasonal_endpoint"] for m in measurements])
    drift=np.array([m["drift_endpoint"] for m in measurements])

    def select(names,idx):
        best=None
        all_rows=[]
        for name in names:
            feat=np.array([x[idx][name] for x in bundles],dtype=float)
            b0,b1,fm,fs,pred=_fit_correction(
                actual,seasonal,drift,feat
            )
            rm=_rmse(actual,pred)
            row={
                "feature":name,"rmse":rm,
                "intercept":b0,"slope":b1,
                "feature_mean":fm,"feature_std":fs,
            }
            all_rows.append(row)
            if best is None or rm<best["rmse"]:
                best=row
        return best,all_rows

    bfg_best,bfg_rows=select(BFG_FEATURE_CANDIDATES,0)
    null_best,null_rows=select(NULL_FEATURE_CANDIDATES,1)
    reclosure=float(np.mean([x[2] for x in bundles]))
    return bfg_best,null_best,bfg_rows,null_rows,reclosure


def _evaluate_fixed_models(
    measurements:list[dict[str,Any]],
    config:CO2CarrierConfig,
):
    carrier=CO2BFGCarrier(config)
    rows=[]
    successes=0
    for m in measurements:
        f=carrier.forecast(m)
        state,report=carrier.validate_measurement_state(m)
        step=canonical_reclosure(state,NumericalPolicy())
        successes+=int(step.success)
        rows.append({
            "target_date":m["target_date"],
            "actual":m["actual"],
            **f,
            "mapping_valid":report.valid,
            "reclosure_success":step.success,
        })
    y=np.array([r["actual"] for r in rows])
    b=np.array([r["bfg"] for r in rows])
    n=np.array([r["matched_null"] for r in rows])
    return {
        "bfg_rmse":_rmse(y,b),
        "null_rmse":_rmse(y,n),
        "relative_improvement":1.0-_rmse(y,b)/_rmse(y,n),
        "reclosure_fraction":successes/max(len(rows),1),
        "rows":rows,
    }


def _fold_preflight(
    monthly:pd.Series,
    train_end:str,
    eval_start:str,
    eval_end:str,
    lag:int,
    base_config:dict,
):
    train=monthly.loc[:pd.Timestamp(train_end)]
    mean=float(train.mean())
    std=float(train.std(ddof=0))
    sigma=_graph_sigma(train.values,mean,std,lag)

    all_m=_measurements_from_monthly(monthly,lag)
    train_m=[
        m for m in all_m
        if pd.Timestamp(m["target_date"])<=pd.Timestamp(train_end)
    ]
    eval_m=[
        m for m in all_m
        if pd.Timestamp(eval_start)<=pd.Timestamp(m["target_date"])<=pd.Timestamp(eval_end)
    ]

    bfg_best,null_best,_,_,train_reclosure=_select_models(
        train_m,mean,std,sigma,base_config
    )
    cfg=CO2CarrierConfig(
        **base_config,
        mean=mean,std=std,graph_sigma=sigma,
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
    ev=_evaluate_fixed_models(eval_m,cfg)
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
    }


def prepare_co2_validation(
    outdir:str|Path,
    data_path:str|Path=DEFAULT_DATA,
    lag:int=24,
    calibration_end:str="1990-12-31",
    heldout_start:str="1991-01-01",
):
    """
    Calibration + rolling-preflight only.

    Held-out 1991-2001 target metrics are never evaluated here.
    """
    outdir=Path(outdir)
    outdir.mkdir(parents=True,exist_ok=True)
    dataset_hash=_sha256(data_path)

    calibration=load_monthly_calibration(data_path,calibration_end)
    mean=float(calibration.mean())
    std=float(calibration.std(ddof=0))
    sigma=_graph_sigma(calibration.values,mean,std,lag)

    base_config={
        "lag":lag,
        "calibration_end":calibration_end,
        "heldout_start":heldout_start,
        "heldout_end":"2001-12-01",
        "temporal_scale":6.0,
        "neutral_load_scale":0.42,
        "stress_scale":0.18,
        "formation_drive":1.45,
        "formation_offset":0.20,
        "persistent_rank":4,
        "contraction":0.76,
        "phase_scale":0.40,
        "dataset_sha256":dataset_hash,
    }

    fold_rows=[
        _fold_preflight(
            calibration,*fold,lag,base_config
        )
        for fold in PREFLIGHT_FOLDS
    ]
    wins=sum(r["relative_improvement"]>0 for r in fold_rows)
    mean_improvement=float(np.mean([
        r["relative_improvement"] for r in fold_rows
    ]))
    worst_improvement=float(np.min([
        r["relative_improvement"] for r in fold_rows
    ]))
    min_reclosure=float(np.min([
        r["eval_reclosure_fraction"] for r in fold_rows
    ]))

    # Readiness gate is prospective for the later held-out test. It is deliberately
    # moderate: repeated directionality, positive average gain, no catastrophic
    # fold, and stable reclosure.
    readiness=bool(
        wins>=2
        and mean_improvement>0
        and worst_improvement>=-0.02
        and min_reclosure>=0.95
    )

    full_m=_measurements_from_monthly(calibration,lag)
    bfg_best,null_best,bfg_candidates,null_candidates,full_reclosure=_select_models(
        full_m,mean,std,sigma,base_config
    )
    config=CO2CarrierConfig(
        **base_config,
        mean=mean,std=std,graph_sigma=sigma,
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
    carrier=CO2BFGCarrier(config)
    full_eval=_evaluate_fixed_models(full_m,config)

    # The held-out plan is frozen now, but no held-out metric is computed.
    # Indices refer to the future concatenated monthly measurement list.
    full_weekly=load_weekly_co2(data_path)
    # Build only the future monthly calendar here. Held-out target values are not
    # transformed, interpolated, scored, or fitted during preflight.
    heldout_end_month=full_weekly.index.max().to_period("M").to_timestamp()
    heldout_calendar=pd.date_range(
        pd.Timestamp(heldout_start),
        heldout_end_month,
        freq="MS",
    )
    combined_index=calibration.index.append(heldout_calendar)
    measurement_dates=combined_index[lag:]
    cal_indices=tuple(
        i for i,d in enumerate(measurement_dates)
        if d<=pd.Timestamp(calibration_end)
    )
    held_indices=tuple(
        i for i,d in enumerate(measurement_dates)
        if d>=pd.Timestamp(heldout_start)
    )

    plan=HeldoutValidationPlan(
        domain="atmospheric CO2 / monthly Mauna Loa measurements",
        dataset_name="Statsmodels weekly Mauna Loa CO2 snapshot, monthly transformed",
        target_statement=(
            "With one frozen 24-month graph-aligned BFG carrier, the adaptive "
            "BFG feature correction will achieve lower one-step held-out RMSE "
            "than the equal-coefficient matched ordinary-feature correction, "
            "with at least 95% canonical BFG reclosure success."
        ),
        calibration_indices=cal_indices,
        heldout_indices=held_indices,
        null_model_name=(
            "equal-coefficient adaptive correction using the best calibration-"
            "selected feature from six frozen ordinary window statistics"
        ),
        primary_metric="held-out one-step-ahead monthly RMSE",
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
        "folds":fold_rows,
        "fold_wins":wins,
        "folds_total":len(fold_rows),
        "mean_relative_improvement":mean_improvement,
        "worst_relative_improvement":worst_improvement,
        "minimum_eval_reclosure_fraction":min_reclosure,
        "full_calibration":{
            "bfg_feature":bfg_best["feature"],
            "null_feature":null_best["feature"],
            "bfg_rmse":full_eval["bfg_rmse"],
            "null_rmse":full_eval["null_rmse"],
            "relative_improvement":full_eval["relative_improvement"],
            "reclosure_fraction":full_eval["reclosure_fraction"],
        },
        "readiness_rule":{
            "fold_wins_min":2,
            "mean_relative_improvement_gt":0.0,
            "worst_fold_relative_improvement_min":-0.02,
            "minimum_reclosure_fraction":0.95,
        },
        "heldout_metrics_evaluated":False,
    }

    write_carrier_schema(carrier.schema,outdir/"co2_carrier_schema.json")
    plan_payload=asdict(plan)
    plan_payload["plan_fingerprint"]=plan_fingerprint(plan)
    (outdir/"co2_validation_plan.json").write_text(
        json.dumps(plan_payload,indent=2),encoding="utf-8"
    )
    frozen={
        "config":config.to_jsonable(),
        "mapping_fingerprint":carrier.mapping_fingerprint,
        "plan_fingerprint":plan_fingerprint(plan),
        "dataset_sha256":dataset_hash,
        "bfg_candidates":bfg_candidates,
        "null_candidates":null_candidates,
        "preflight":preflight,
        "heldout_metrics_evaluated":False,
    }
    (outdir/"co2_frozen_model.json").write_text(
        json.dumps(frozen,indent=2),encoding="utf-8"
    )
    (outdir/"co2_preflight.json").write_text(
        json.dumps(preflight,indent=2),encoding="utf-8"
    )

    if readiness:
        token_payload={
            "mapping_fingerprint":carrier.mapping_fingerprint,
            "plan_fingerprint":plan_fingerprint(plan),
            "preflight_sha256":_sha256(outdir/"co2_preflight.json"),
        }
        token_text=json.dumps(token_payload,sort_keys=True,separators=(",",":"))
        token_payload["readiness_token"]=hashlib.sha256(
            token_text.encode("utf-8")
        ).hexdigest()
        (outdir/"CO2_READINESS_TOKEN.json").write_text(
            json.dumps(token_payload,indent=2),encoding="utf-8"
        )

    save_experiment_ledger(
        outdir,
        experiment="co2_validation_preflight",
        seed=None,
        parameters={
            "mapping_fingerprint":carrier.mapping_fingerprint,
            "plan_fingerprint":plan_fingerprint(plan),
            "lag":lag,
            "calibration_end":calibration_end,
            "heldout_start":heldout_start,
        },
        summary=preflight,
        frames=fold_rows,
        name="co2_preflight",
    )

    return {
        "status":preflight["status"],
        "readiness":readiness,
        "mapping_fingerprint":carrier.mapping_fingerprint,
        "plan_fingerprint":plan_fingerprint(plan),
        "preflight":preflight,
        "heldout_metrics_evaluated":False,
    }


def validate_co2_heldout(
    prepared_dir:str|Path,
    data_path:str|Path=DEFAULT_DATA,
    permit_path:str|Path|None=None,
):
    """
    Confirmatory evaluation. Refuses to run without a valid readiness token.

    This function is intentionally separate from `prepare_co2_validation`.
    """
    prepared_dir=Path(prepared_dir)

    # A readiness token is necessary but no longer sufficient. Confirmatory
    # opening additionally requires a one-time portfolio permit bound to the
    # frozen mapping, plan, artifacts, and current source tree.
    if permit_path is None:
        raise RuntimeError(
            "held-out CO2 validation is sealed: a portfolio confirmation permit "
            "is required"
        )
    portfolio=ValidationPortfolio()
    guard=BlindHeldoutGuard(portfolio)
    guard.validate_confirmation_permit("mauna-loa-co2",permit_path)

    token_path=prepared_dir/"CO2_READINESS_TOKEN.json"
    if not token_path.exists():
        raise RuntimeError(
            "held-out CO2 validation is sealed: no readiness token exists"
        )

    frozen=json.loads(
        (prepared_dir/"co2_frozen_model.json").read_text(encoding="utf-8")
    )
    preflight=json.loads(
        (prepared_dir/"co2_preflight.json").read_text(encoding="utf-8")
    )
    token=json.loads(token_path.read_text(encoding="utf-8"))
    if not preflight.get("readiness"):
        raise RuntimeError("held-out CO2 validation is sealed: preflight not ready")
    if token["preflight_sha256"]!=_sha256(prepared_dir/"co2_preflight.json"):
        raise RuntimeError("readiness token invalid: preflight artifact changed")

    cfg=dict(frozen["config"])
    config=CO2CarrierConfig(**cfg)
    carrier=CO2BFGCarrier(config)
    if carrier.mapping_fingerprint!=frozen["mapping_fingerprint"]:
        raise RuntimeError("carrier fingerprint mismatch")

    calibration=load_monthly_calibration(data_path,config.calibration_end)

    # From this line onward the confirmatory block is considered opened.
    permit_audit=guard.consume_confirmation_permit(
        "mauna-loa-co2",permit_path
    )
    heldout=load_monthly_heldout(data_path,config.heldout_start)
    combined=pd.concat([calibration,heldout])
    measurements=_measurements_from_monthly(combined,config.lag)
    held=[
        m for m in measurements
        if pd.Timestamp(m["target_date"])>=pd.Timestamp(config.heldout_start)
    ]
    ev=_evaluate_fixed_models(held,config)
    result={
        "passed":bool(
            ev["bfg_rmse"]<ev["null_rmse"]
            and ev["reclosure_fraction"]>=0.95
        ),
        "bfg_rmse":ev["bfg_rmse"],
        "matched_null_rmse":ev["null_rmse"],
        "relative_improvement":ev["relative_improvement"],
        "heldout_reclosure_success_fraction":ev["reclosure_fraction"],
        "mapping_fingerprint":carrier.mapping_fingerprint,
        "plan_fingerprint":frozen["plan_fingerprint"],
        "heldout_metrics_evaluated":True,
        "retuning_after_heldout":False,
        "confirmation_permit":permit_audit,
    }
    result_path=prepared_dir/"co2_heldout_result.json"
    result_path.write_text(
        json.dumps(result,indent=2),encoding="utf-8"
    )

    try:
        result_rel=str(result_path.relative_to(portfolio.project_root))
    except ValueError:
        result_rel=str(result_path)
    portfolio.record_confirmatory_result(
        "mauna-loa-co2",
        passed=bool(result["passed"]),
        result_artifact=result_rel,
        metrics={
            "bfg_rmse":result["bfg_rmse"],
            "matched_null_rmse":result["matched_null_rmse"],
            "relative_improvement":result["relative_improvement"],
            "heldout_reclosure_success_fraction":
                result["heldout_reclosure_success_fraction"],
        },
    )
    return result
