import numpy as np

from bfg_studio import (
    packet_formation_eligibility,
    run_formation_eligibility_audit,
)

def test_generalized_criterion_matches_direct_active_compression():
    K=np.array([
        [-2.0,0.25,0.0],
        [0.25,0.8,0.1],
        [0.0,0.1,1.4],
    ],dtype=complex)
    A=np.array([
        [1.0,0.1,0.0],
        [0.0,0.8,0.2],
        [0.0,0.0,0.5],
        [0.4,0.0,0.0],
        [0.0,0.3,0.0],
        [0.0,0.0,0.2],
    ],dtype=complex)

    cert=packet_formation_eligibility(K,A)
    assert cert.active_rank==3
    assert cert.generalized_match_residual is not None
    assert cert.generalized_match_residual<1e-10
    assert abs(
        cert.exact_lowest_eigenvalue
        -cert.generalized_lowest_eigenvalue
    )<1e-10

def test_negative_parent_ground_witness_is_sufficient_for_active_negativity():
    K=np.diag([-2.0,0.5]).astype(complex)
    A=np.array([
        [1.0,0.0],
        [0.0,0.5],
        [0.2,0.0],
        [0.0,0.25],
    ],dtype=complex)

    cert=packet_formation_eligibility(K,A)
    assert cert.ground_witness_negative is True
    assert cert.exact_negative is True
    assert cert.eligible

def test_relational_13_21_split_is_transport_not_parent_negativity():
    result=run_formation_eligibility_audit(
        limit_per_timeseries_carrier=2,
        include_full_network=True,
    )
    assert result["heldout_metrics_evaluated"] is False
    assert result["maximum_generalized_match_residual"]<1e-10

    network=next(
        d for d in result["domains"]
        if d["carrier_id"]=="zachary-karate-network"
    )
    assert network["gate_reached"]==34
    assert network["formation_successes"]==13
    assert network["parent_negative_ground_modes"]==34
    assert network["exact_generalized_criterion_matches"]=="34/34"
    assert network["ground_witness_sign_matches"]=="34/34"
    assert network["minimum_formation_gap"]>0.08

    explanation=result["network_explanation"]
    assert explanation["all_parent_K_have_negative_ground_mode"]
    assert explanation["simplicity_condition_passes_for_all_34"]
    assert explanation["ground_witness_sign_matches_formation_34_of_34"]
