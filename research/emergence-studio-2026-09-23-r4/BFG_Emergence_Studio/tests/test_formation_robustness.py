import numpy as np

from bfg_studio import (
    formation_margin,
    formation_margin_from_spectrum,
    boundary_crossing_control,
    run_formation_robustness_audit,
)

def test_exact_margin_for_eligible_sign_limited_operator():
    K=np.diag([-0.2,1.0]).astype(complex)
    cert=formation_margin(K)
    assert cert.eligible
    assert cert.limiting_surface=="sign"
    assert abs(cert.signed_margin-(0.2-1e-10))<1e-12

    control=boundary_crossing_control(K)
    assert control["inside_preserved"]
    assert control["outside_crossed"]

def test_exact_margin_for_eligible_gap_limited_operator():
    K=np.diag([-2.0,-1.0,3.0]).astype(complex)
    cert=formation_margin(K)
    assert cert.eligible
    assert cert.limiting_surface=="simplicity"
    expected=(1.0-1e-8)/2.0
    assert abs(cert.signed_margin-expected)<1e-12

    control=boundary_crossing_control(K)
    assert control["inside_preserved"]
    assert control["outside_crossed"]

def test_ineligible_distance_to_eligibility_is_signed_negative():
    cert=formation_margin_from_spectrum(
        0.125,
        0.5,
    )
    assert not cert.eligible
    assert cert.limiting_surface=="sign"
    assert cert.signed_margin<0
    assert abs(
        cert.absolute_boundary_distance-(0.125+1e-10)
    )<1e-12

def test_full_network_and_smoke_timeseries_boundary_controls():
    result=run_formation_robustness_audit(
        limit_per_timeseries_carrier=2,
        include_full_network=True,
    )
    assert result["heldout_metrics_evaluated"] is False
    assert result["boundary_controls"]==40
    assert result["inside_preserved"]==40
    assert result["outside_crossed"]==40

    network=result["network_bifurcation"]
    assert network["eligible_count"]==13
    assert network["terminal_count"]==21
    assert network["nearest_eligible_margin"]>0
    assert network["nearest_terminal_margin"]<0
