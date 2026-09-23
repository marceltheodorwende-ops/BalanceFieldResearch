import json
import pandas as pd
import pytest

from bfg_studio import (
    load_enso_monthly,
    prepare_enso_validation,
    ENSOBFGCarrier,
    ENSOCarrierConfig,
    validate_state_contract,
    validate_enso_future,
)

@pytest.fixture(scope="module")
def prepared_enso(tmp_path_factory):
    path=tmp_path_factory.mktemp("enso_prepared")
    result=prepare_enso_validation(path)
    return path,result

def test_bundled_enso_snapshot():
    s=load_enso_monthly()
    assert len(s)==61*12
    assert s.index.min()==pd.Timestamp("1950-01-01")
    assert s.index.max()==pd.Timestamp("2010-12-01")
    assert s.notna().all()

def test_enso_preflight_keeps_future_unopened(prepared_enso):
    path,result=prepared_enso
    frozen=json.loads((path/"enso_frozen_model.json").read_text())
    plan=json.loads((path/"enso_validation_plan.json").read_text())
    assert frozen["heldout_metrics_evaluated"] is False
    assert plan["heldout_data_bundled"] is False
    assert plan["development_period"]==["1950-01-01","2010-12-01"]
    assert plan["heldout_period"]==["2011-01-01","2025-12-01"]
    assert not (path/"enso_future_heldout_result.json").exists()
    assert result["heldout_metrics_evaluated"] is False

def test_enso_reference_preflight_is_ready(prepared_enso):
    _,result=prepared_enso
    pre=result["preflight"]
    assert result["status"]=="READY_FOR_VALIDATION"
    assert pre["fold_wins"]>=2
    assert pre["mean_relative_improvement"]>0
    assert pre["worst_relative_improvement"]>=-0.02
    assert pre["minimum_eval_reclosure_fraction"]>=0.95

def test_frozen_enso_state_contract(prepared_enso):
    path,_=prepared_enso
    frozen=json.loads((path/"enso_frozen_model.json").read_text())
    cfg=dict(frozen["config"])
    cfg["month_climatology"]=tuple(cfg["month_climatology"])
    carrier=ENSOBFGCarrier(ENSOCarrierConfig(**cfg))
    s=load_enso_monthly()
    climatology=cfg["month_climatology"]
    anomalies=pd.Series(
        [float(v)-float(climatology[d.month-1]) for d,v in s.items()],
        index=s.index,
    )
    lag=cfg["lag"]
    m={
        "target_date":str(s.index[lag].date()),
        "window_anomalies":anomalies.iloc[:lag].tolist(),
        "previous_anomaly":float(anomalies.iloc[lag-1]),
    }
    state=carrier.map_measurement_to_state(m)
    assert validate_state_contract(state).valid

def test_enso_confirmation_requires_external_data_and_permit(prepared_enso,tmp_path):
    path,_=prepared_enso
    with pytest.raises((RuntimeError,FileNotFoundError)):
        validate_enso_future(
            path,
            future_data_path=tmp_path/"future.csv",
            permit_path=tmp_path/"permit.json",
        )
