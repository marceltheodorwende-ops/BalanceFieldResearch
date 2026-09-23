from bfg_studio import (
    TransferDomainSummary,
    transformation_corridor_overlap,
    run_master_runtime_transfer_audit,
)

def _summary(cid,q10,q90,median):
    metrics={
        "alpha":{
            "mean":median,
            "std":0.0,
            "q10":q10,
            "q25":median,
            "median":median,
            "q75":median,
            "q90":q90,
            "min":q10,
            "max":q90,
        }
    }
    return TransferDomainSummary(
        carrier_id=cid,
        scope="test",
        states=1,
        processed=1,
        exceptions=0,
        first_step_successes=1,
        first_step_terminals=0,
        first_step_success_fraction=1.0,
        maximum_successful_depth=1,
        median_successful_depth=1.0,
        q10_successful_depth=1.0,
        q90_successful_depth=1.0,
        terminal_reason_counts={},
        transformation_metrics=metrics,
        maximum_unitarity_residual=0.0,
        maximum_gram_rebuild_residual=0.0,
    )

def test_transformation_corridor_overlap():
    summaries=[
        _summary("a",0.1,0.5,0.3),
        _summary("b",0.2,0.6,0.4),
        _summary("c",0.15,0.45,0.25),
    ]
    out=transformation_corridor_overlap(summaries,"alpha")
    assert out["shared"]
    assert abs(out["lower"]-0.2)<1e-12
    assert abs(out["upper"]-0.45)<1e-12
    assert out["overlap_ratio"]>0

def test_master_transfer_smoke_uses_only_ready_development_sources():
    result=run_master_runtime_transfer_audit(
        recursive_horizon=2,
        limit_per_carrier=2,
    )
    assert result["audit_passed"]
    assert result["heldout_metrics_evaluated"] is False
    assert result["states_total"]==6
    assert result["states_processed"]==6
    assert result["exceptions"]==0
    assert set(result["portfolio_status"])=={
        "annual-sunspots",
        "mauna-loa-co2",
        "enso-pacific-sst",
    }
    for status in result["portfolio_status"].values():
        assert status["status"]=="READY_FOR_VALIDATION"
        assert status["heldout_metrics_evaluated"] is False
