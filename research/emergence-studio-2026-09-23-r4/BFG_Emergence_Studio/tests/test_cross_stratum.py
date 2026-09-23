import numpy as np

from bfg_studio import (
    NumericalPolicy,
    active_runtime_support_projector,
    persistent_runtime_support_projector,
    canonical_projector_transport,
    canonical_emergent_seed,
    continue_witness_across_strata,
    continue_witness_chain,
    run_cross_stratum_audit,
)

def test_active_rank_increase_preserves_inherited_witness_without_inventing_new_amplitude():
    policy=NumericalPolicy()
    tau=max(policy.rank_tol,policy.rtol)
    A0=np.diag([1.0,0.5*tau]).astype(complex)
    A1=np.diag([1.0,2.0*tau]).astype(complex)
    Q0,_=active_runtime_support_projector(A0,policy)
    Q1,_=active_runtime_support_projector(A1,policy)
    rho=Q0.copy()

    c=continue_witness_across_strata(Q0,Q1,rho,policy=policy)
    assert not c.terminal
    assert c.certificate.transition_kind=="rank_increase"
    assert c.certificate.source_rank==1
    assert c.certificate.target_rank==2
    assert c.certificate.emergent_rank==1
    assert abs(c.retained_witness_mass-1.0)<1e-12
    assert c.emergent_seed is None
    assert abs(np.trace(c.emergent_projector@c.transported_witness))<1e-12

def test_rank_decrease_with_zero_witness_overlap_commits_to_bottom():
    Q0=np.eye(2,dtype=complex)
    Q1=np.diag([1.0,0.0]).astype(complex)
    rho=np.diag([0.0,1.0]).astype(complex)
    c=continue_witness_across_strata(Q0,Q1,rho)
    assert c.terminal
    assert c.transported_witness is None
    assert c.retained_witness_mass==0.0
    assert c.lost_witness_mass==1.0

def test_same_rank_rotation_uses_canonical_polar_transport():
    theta=0.37
    u0=np.array([[1.0],[0.0]],dtype=complex)
    u1=np.array([[np.cos(theta)],[np.sin(theta)]],dtype=complex)
    Q0=u0@u0.conj().T
    Q1=u1@u1.conj().T
    T,Si,Sf,E,L,cert=canonical_projector_transport(Q0,Q1)
    assert cert.transition_kind=="same_rank_transport"
    assert cert.emergent_rank==0
    assert cert.lost_rank==0
    assert np.linalg.norm(T@Q0-T,2)<1e-12
    assert np.linalg.norm(Q1@T-T,2)<1e-12

    c=continue_witness_across_strata(Q0,Q1,Q0)
    assert not c.terminal
    assert np.linalg.norm(c.transported_witness-Q1,2)<1e-12

def test_emergent_no_choice_rule_rejects_degenerate_ground_and_accepts_unique_ground():
    Q0=np.diag([1.0,0.0,0.0]).astype(complex)
    Q1=np.eye(3,dtype=complex)
    rho=Q0.copy()

    bad=continue_witness_across_strata(
        Q0,Q1,rho,
        formation_operator=np.diag([0.5,-1.0,-1.0]).astype(complex),
        require_emergent_seed=True,
    )
    assert bad.terminal
    assert bad.emergent_seed is None

    good=continue_witness_across_strata(
        Q0,Q1,rho,
        formation_operator=np.diag([0.5,-2.0,1.0]).astype(complex),
        require_emergent_seed=True,
    )
    assert not good.terminal
    assert good.emergent_seed is not None
    assert abs(np.trace(good.emergent_seed).real-2.0)<1e-12

def test_persistent_runtime_support_crossing_is_basis_free():
    policy=NumericalPolicy()
    tau=1.0-policy.peripheral_tol
    R0=np.diag([1.0,tau-0.25*policy.peripheral_tol]).astype(complex)
    R1=np.diag([1.0,tau+0.25*policy.peripheral_tol]).astype(complex)
    Q0,c0=persistent_runtime_support_projector(R0,policy)
    Q1,c1=persistent_runtime_support_projector(R1,policy)
    assert c0["rank"]==1
    assert c1["rank"]==2

    c=continue_witness_across_strata(Q0,Q1,Q0,policy=policy)
    assert not c.terminal
    assert c.certificate.transition_kind=="rank_increase"


def test_cross_stratum_chain_is_nonamplifying():
    q0=np.diag([1.0,0.0,0.0]).astype(complex)
    q1=np.diag([1.0,1.0,0.0]).astype(complex)
    theta=0.23
    U=np.eye(3,dtype=complex)
    U[:2,:2]=np.array([
        [np.cos(theta),-np.sin(theta)],
        [np.sin(theta),np.cos(theta)],
    ])
    q2=U@q1@U.conj().T
    q3=U@q0@U.conj().T
    result=continue_witness_chain([q0,q1,q2,q3],q0)
    assert not result["terminal"]
    assert result["transport_product_norm"]<=1.0+1e-10
    assert result["cumulative_retained_mass"]<=1.0+1e-10
    for step in result["steps"]:
        assert step["transport_norm"]<=1.0+1e-10
        assert step["product_norm"]<=1.0+1e-10
        assert step["mass_after"]<=step["mass_before"]+1e-10

def test_cross_stratum_smoke_audit_is_closed_and_does_not_claim_real_crossing():
    result=run_cross_stratum_audit(
        limit_per_timeseries_carrier=2,
        include_full_network=True,
    )
    assert result["heldout_metrics_evaluated"] is False
    assert result["real_states_total"]==40
    assert result["real_identity_continuity_passed"]==40
    assert result["real_observed_rank_crossings"]==0
    assert result["synthetic_crossing_cases"]>=7
    assert result["synthetic_crossing_passed"]
    assert result["unitary_equivariance_passed"]
    assert result["identity_continuity_passed"]
    assert result["cross_stratum_chain_stability_passed"]
    assert result["interpretation_guard"]["real_cross_stratum_event_observed"] is False
