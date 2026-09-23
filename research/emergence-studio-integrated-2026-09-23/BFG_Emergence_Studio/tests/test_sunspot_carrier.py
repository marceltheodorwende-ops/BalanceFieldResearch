import json
import numpy as np
import pytest

from bfg_studio import (
    load_sunspots,
    build_window_measurements,
    prepare_sunspot_validation_current,
    AnnualSunspotValidationCarrier,
    SunspotValidationConfig,
    validate_state_contract,
    validate_sunspot_future,
)

def test_bundled_sunspot_snapshot():
    years,values=load_sunspots()
    assert len(years)==309
    assert years[0]==1700 and years[-1]==2008
    assert np.all(values>=0)

def test_window_measurements_are_causal():
    years,values=load_sunspots()
    ms=build_window_measurements(years,values,lag=12)
    assert ms[0]["target_year"]==1712
    assert max(ms[0]["window_years"])==1711
    assert max(ms[-1]["window_years"])==2007
    assert ms[-1]["target_year"]==2008

def test_refresh_uses_all_opened_history_as_development(tmp_path):
    result=prepare_sunspot_validation_current(tmp_path)
    frozen=json.loads((tmp_path/"sunspot_frozen_model.json").read_text())
    plan=json.loads((tmp_path/"sunspot_validation_plan.json").read_text())
    assert frozen["heldout_metrics_evaluated"] is False
    assert plan["development_years"]==[1700,2008]
    assert plan["heldout_years"]==[2009,2025]
    assert plan["heldout_data_bundled"] is False
    assert len(result["mapping_fingerprint"])==64

def test_refreshed_sunspot_state_contract(tmp_path):
    prepare_sunspot_validation_current(tmp_path)
    frozen=json.loads((tmp_path/"sunspot_frozen_model.json").read_text())
    cfg=dict(frozen["config"])
    cfg["ar_coefficients"]=tuple(cfg["ar_coefficients"])
    carrier=AnnualSunspotValidationCarrier(SunspotValidationConfig(**cfg))
    years,values=load_sunspots()
    m=build_window_measurements(years,values,lag=12)[-1]
    state=carrier.map_measurement_to_state(m)
    report=validate_state_contract(state)
    assert report.valid

def test_refreshed_sunspot_preflight_does_not_open_future_targets(tmp_path):
    result=prepare_sunspot_validation_current(tmp_path)
    assert result["heldout_metrics_evaluated"] is False
    assert not (tmp_path/"sunspot_future_heldout_result.json").exists()

def test_future_confirmation_requires_external_data_and_permit(tmp_path):
    prepare_sunspot_validation_current(tmp_path)
    with pytest.raises((RuntimeError, FileNotFoundError)):
        validate_sunspot_future(
            tmp_path,
            future_data_path=tmp_path/"future.csv",
            permit_path=tmp_path/"permit.json",
        )


def test_refreshed_sunspot_reference_preflight_is_ready(tmp_path):
    result=prepare_sunspot_validation_current(tmp_path)
    pre=result["preflight"]
    assert result["status"]=="READY_FOR_VALIDATION"
    assert pre["fold_wins"]==3
    assert pre["mean_relative_improvement"]>0
    assert pre["worst_relative_improvement"]>0
    assert pre["minimum_eval_reclosure_fraction"]==1.0
