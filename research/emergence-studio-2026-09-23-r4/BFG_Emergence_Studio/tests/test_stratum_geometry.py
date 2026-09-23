import numpy as np

from bfg_studio import (
    NumericalPolicy,
    persistent_runtime_rank_certificate,
    active_runtime_rank_certificate,
    certify_runtime_stratum_radius,
    structured_parent_perturbation_control,
    scalar_nonterminal_seed,
    run_stratum_transition_audit,
)

def test_persistent_runtime_rank_margin_is_positive_for_normal_contraction():
    policy=NumericalPolicy()
    R=np.diag([1.0,0.5]).astype(complex)
    cert=persistent_runtime_rank_certificate(R,policy)
    assert cert.rank==1
    assert cert.runtime_consistency
    assert cert.certified_operator_radius>0

    r=cert.certified_operator_radius
    inside=np.diag([1.0-0.5*r,0.5]).astype(complex)
    outside=np.diag([1.0-1.1*r,0.5]).astype(complex)

    assert persistent_runtime_rank_certificate(
        inside,policy
    ).rank==1
    assert persistent_runtime_rank_certificate(
        outside,policy
    ).rank==0

def test_active_runtime_rank_margin_controls_latent_activation():
    policy=NumericalPolicy()
    A=np.diag([0.2,0.0]).astype(complex)
    cert=active_runtime_rank_certificate(A,policy)
    assert cert.rank==1
    assert cert.certified_operator_radius>0

    r=cert.certified_operator_radius
    inside=A.copy()
    inside[1,1]=0.5*r
    outside=A.copy()
    outside[1,1]=1.2*r

    assert active_runtime_rank_certificate(
        inside,policy
    ).rank==1
    assert active_runtime_rank_certificate(
        outside,policy
    ).rank==2

def test_runtime_stratum_parent_radius_is_stricter_than_conditional_radius():
    state=scalar_nonterminal_seed(0.2)
    cert=certify_runtime_stratum_radius(state)
    assert cert.runtime_stratum_parent_radius>0
    assert (
        cert.runtime_stratum_parent_radius
        < cert.conditional_parent_radius
    )
    assert cert.limiting_surface in {
        "persistent_runtime_rank",
        "active_runtime_rank",
        "formation_status",
    }

def test_structured_control_inside_strict_runtime_radius_preserves_status():
    state=scalar_nonterminal_seed(0.2)
    runtime=certify_runtime_stratum_radius(state)

    class RadiusProxy:
        parent_radius=runtime.conditional_parent_radius

    control=structured_parent_perturbation_control(
        state,
        RadiusProxy(),
        factor=0.5,
        radius_override=runtime.runtime_stratum_parent_radius,
    )
    assert control["within_certificate"]
    assert control["same_active_rank"]
    assert control["status_preserved"]

def test_stratum_smoke_audit_has_four_surface_families_and_expected_ranks():
    result=run_stratum_transition_audit(
        limit_per_timeseries_carrier=2,
        include_full_network=True,
    )
    assert result["heldout_metrics_evaluated"] is False
    assert result["states_total"]==40
    assert set(result["surfaces"])=={
        "formation_sign",
        "formation_simplicity",
        "persistent_runtime_rank",
        "active_runtime_rank",
    }
    assert result["active_upward_bottleneck_states"]==40
    assert result["persistent_loss_bottleneck_states"]==40
    for domain in result["domains"]:
        assert domain["persistent_ranks"]==[4]
        assert domain["active_ranks"]==[4]
