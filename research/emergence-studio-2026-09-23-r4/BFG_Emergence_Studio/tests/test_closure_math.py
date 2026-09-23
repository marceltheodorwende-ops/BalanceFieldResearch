import numpy as np
import pytest

from bfg_studio import (
    M3ConnectionState,
    verify_exact_recursive_certificate,
    gram_rebuild_from_supplied_factors,
    retained_channel_gram_decomposition,
    g1_inherited_load,
    g1_intertwining_audit,
    m3_operators,
)

def test_exact_rational_nonnormal_certificate():
    cert=verify_exact_recursive_certificate(
        r=[["1","-1/2"],["0","1/2"]],
        basis=[["1","1"],["0","1"]],
        persistent_dimension=1,
        persistent_metric=[["1"]],
        stable_metric=[["1"]],
    )
    assert cert.status=="certified"
    assert cert.persistent_dimension==1
    assert cert.stable_dimension==1

def test_exact_certificate_rejects_float_entries():
    with pytest.raises(ValueError):
        verify_exact_recursive_certificate(
            r=[[1.0,0.0],[0.0,0.5]],
            basis=[["1","0"],["0","1"]],
            persistent_dimension=1,
            persistent_metric=[["1"]],
            stable_metric=[["1"]],
        )

def test_exact_certificate_rejects_defective_unit_circle_block():
    with pytest.raises(ValueError):
        verify_exact_recursive_certificate(
            r=[["1","1"],["0","1"]],
            basis=[["1","0"],["0","1"]],
            persistent_dimension=2,
            persistent_metric=[["1","0"],["0","1"]],
            stable_metric=[],
        )

def test_supplied_factor_gram_rebuild():
    g=gram_rebuild_from_supplied_factors(
        np.diag([1.0,2.0]),
        np.eye(2),
        np.eye(2),
    )
    assert np.all(np.linalg.eigvalsh(g["Y"])>=-1e-12)
    assert np.linalg.norm(g["C_N"]+g["B_N"]-np.eye(2))<1e-12

def test_retained_channel_identity_captures_external_gram_energy():
    r=retained_channel_gram_decomposition(
        np.array([[0.0,0.0],[1.0,0.0]]),
        np.array([[1.0],[0.0]]),
    )
    assert r["identity_residual"]<1e-12
    assert r["external_rank"]==1
    assert r["interpretation"]["gram_energy_recovered"]
    assert not r["interpretation"]["future_dynamics_recovered"]

def test_g1_is_conditional_on_intertwining():
    good=g1_intertwining_audit(
        b2=np.diag([2.0,3.0]),
        w2=np.eye(2),
        l2=np.eye(2),
        u=np.array([[1.0],[0.0]]),
        b_next=np.array([[2.0]]),
        w_next=np.array([[1.0]]),
        l_next=np.array([[1.0]]),
    )
    assert good["intertwining_satisfied"]

    bad=g1_intertwining_audit(
        b2=np.diag([2.0,3.0]),
        w2=np.eye(2),
        l2=np.eye(2),
        u=np.array([[1.0],[0.0]]),
        b_next=np.array([[0.0]]),
        w_next=np.array([[1.0]]),
        l_next=np.array([[1.0]]),
    )
    assert not bad["intertwining_satisfied"]

def test_g1_inherited_load_is_basis_covariant_shape():
    y=np.diag([1.0,2.0])
    u=np.array([[1.0],[0.0],[0.0],[1.0]])/np.sqrt(2.0)
    yn=g1_inherited_load(y,u)
    assert yn.shape==(1,1)
    assert np.linalg.eigvalsh(yn)[0]>=0

def test_m3_cayley_transport_is_unitary_for_skew_hermitian_connection():
    op=m3_operators(
        M3ConnectionState(
            connection=np.array([[0.0,-1.0],[1.0,0.0]]),
            coherence=np.diag([1.0,2.0]),
            difference=5*np.eye(2),
            neutral=np.eye(2),
            packet=np.ones(2),
        )
    )
    assert op["power_bounded_by_construction"]
    assert op["unitarity_residual"]<1e-10
