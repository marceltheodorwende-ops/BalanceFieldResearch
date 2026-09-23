import numpy as np

from bfg_studio import (
    scalar_nonterminal_seed,
    certify_parent_formation_radius,
    parent_formation_bound,
    structured_parent_perturbation_control,
)
from bfg_studio.network_carrier import KarateInteractionCarrier
from bfg_studio.finite_closure import bfg_state_to_reduced

def test_no_unrestricted_active_rank_radius_in_ambient_matrix_space():
    eps=1e-12
    A=np.diag([1.0,0.0])
    Ap=np.diag([1.0,eps])
    assert np.linalg.norm(Ap-A,2)==eps
    assert np.linalg.matrix_rank(A)==1
    assert np.linalg.matrix_rank(Ap)==2

def test_no_unrestricted_persistent_radius_for_exact_unit_circle_sector():
    eps=1e-12
    R=np.diag([1.0,0.5]).astype(complex)
    Rp=np.diag([1.0-eps,0.5]).astype(complex)
    assert np.linalg.norm(Rp-R,2)<=eps*(1+1e-6)
    base=sum(abs(abs(z)-1.0)<1e-15 for z in np.linalg.eigvals(R))
    pert=sum(abs(abs(z)-1.0)<1e-15 for z in np.linalg.eigvals(Rp))
    assert base==1
    assert pert==0

def test_scalar_parent_radius_is_positive_and_bound_is_valid():
    state=scalar_nonterminal_seed(0.2)
    cert=certify_parent_formation_radius(state)
    assert cert.parent_radius>0
    bound=parent_formation_bound(state,0.5*cert.parent_radius)
    assert bound.valid
    assert bound.active_formation_bound<bound.active_margin

def test_structured_relational_control_stays_inside_certified_stratum():
    carrier=KarateInteractionCarrier()
    bfg=carrier.map_measurement_to_state(
        carrier.measurements()[0],
        generation=0,
    )
    state=bfg_state_to_reduced(bfg)
    cert=certify_parent_formation_radius(state)
    ctl=structured_parent_perturbation_control(
        state,cert,factor=0.5
    )
    assert ctl["within_certificate"]
    assert ctl["same_active_rank"]
    assert ctl["status_preserved"]
    assert ctl["active_bound_verified"]
    assert ctl["bound_valid"]
