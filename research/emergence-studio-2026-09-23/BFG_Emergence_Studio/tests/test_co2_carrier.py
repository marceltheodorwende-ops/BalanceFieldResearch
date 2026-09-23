from pathlib import Path
import json
import pandas as pd

from bfg_studio import (
    load_weekly_co2,
    load_monthly_calibration,
    prepare_co2_validation,
)

def test_bundled_co2_snapshot():
    s=load_weekly_co2()
    assert len(s)==2284
    assert s.index.min()==pd.Timestamp("1958-03-29")
    assert s.index.max()==pd.Timestamp("2001-12-29")

def test_calibration_transform_stops_before_heldout():
    s=load_monthly_calibration(calibration_end="1990-12-31")
    assert s.index.max()==pd.Timestamp("1990-12-01")
    assert not s.isna().any()

def test_co2_preflight_seals_heldout(tmp_path):
    result=prepare_co2_validation(tmp_path)
    frozen=json.loads((tmp_path/"co2_frozen_model.json").read_text())
    preflight=json.loads((tmp_path/"co2_preflight.json").read_text())
    assert frozen["heldout_metrics_evaluated"] is False
    assert preflight["heldout_metrics_evaluated"] is False
    assert "heldout_result" not in frozen
    assert result["status"] in ("READY_FOR_VALIDATION","NOT_YET_VALIDATED")

def test_readiness_token_exists_only_when_ready(tmp_path):
    result=prepare_co2_validation(tmp_path)
    token=tmp_path/"CO2_READINESS_TOKEN.json"
    assert token.exists() == bool(result["readiness"])


def test_co2_confirmatory_path_requires_portfolio_permit(tmp_path):
    import pytest
    from bfg_studio import validate_co2_heldout
    prepare_co2_validation(tmp_path)
    with pytest.raises(RuntimeError,match="portfolio confirmation permit"):
        validate_co2_heldout(tmp_path)
