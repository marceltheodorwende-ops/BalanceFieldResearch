import numpy as np

from bfg_studio import (
    recursive_stability_certificate,
    admissible_perturbation_certificate,
    feedback_margin_certificate,
    neutral_resolvent_certificate,
    jordan_counterexample,
)

def test_semisimple_unit_circle_plus_stable_complement_passes():
    A=np.diag([1.0,np.exp(0.4j),0.8,0.55]).astype(complex)
    cert=recursive_stability_certificate(A,horizon=32)
    assert cert.spectral_criterion_satisfied
    assert cert.unstable_count==0
    assert cert.semisimple_peripheral
    assert abs(cert.stable_gap-0.2)<1e-12

def test_unit_circle_jordan_block_is_rejected_even_with_rho_one():
    A=jordan_counterexample(2)
    cert=recursive_stability_certificate(A,horizon=32)
    assert abs(cert.spectral_radius-1.0)<1e-12
    assert not cert.semisimple_peripheral
    assert not cert.spectral_criterion_satisfied
    assert cert.finite_horizon_peak_norm>10.0

def test_supercritical_operator_is_rejected():
    A=np.diag([1.0,1.01]).astype(complex)
    cert=recursive_stability_certificate(A,horizon=16)
    assert cert.unstable_count==1
    assert cert.spectral_radius>1.0
    assert not cert.spectral_criterion_satisfied

def test_feedback_margin_is_separate_admissibility_gate():
    ok=feedback_margin_certificate(0.8,0.1)
    bad=feedback_margin_certificate(0.96,0.05)
    assert ok["admissible"]
    assert not bad["admissible"]

def test_neutral_resolvent_bounds_for_psd_load():
    Y=np.diag([0.0,0.25,2.0]).astype(complex)
    cert=neutral_resolvent_certificate(Y)
    assert cert["Y_psd"]
    assert cert["neutral_bounds_satisfied"]
    assert cert["partition_residual"]<1e-12

def test_neutral_resolvent_rejects_non_psd_load():
    Y=np.diag([0.1,-0.2,1.0]).astype(complex)
    cert=neutral_resolvent_certificate(Y)
    assert not cert["Y_psd"]
    assert not cert["neutral_bounds_satisfied"]


def test_small_outward_perturbation_is_not_assumed_stable():
    base=np.diag([1.0,0.5]).astype(complex)
    pert=np.diag([1.0001,0.5]).astype(complex)
    cert=admissible_perturbation_certificate(base,pert)
    assert cert["operator_norm_perturbation"]<1e-3
    assert not cert["admissible_stability_preserved"]
    assert cert["smallness_alone_sufficient"] is False

def test_tangential_unit_circle_perturbation_preserves_admissibility():
    base=np.diag([1.0,0.5]).astype(complex)
    pert=np.diag([np.exp(1e-4j),0.5]).astype(complex)
    cert=admissible_perturbation_certificate(base,pert)
    assert cert["admissible_stability_preserved"]
