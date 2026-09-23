import numpy as np
from bfg_studio import NumericalPolicy, BFGState, neutral_pair, graph_metric, make_commuting_control_state, canonical_reclosure

def test_neutral_partition():
    Y=np.diag([0.0,0.5,2.0]).astype(complex)
    C,B=neutral_pair(Y)
    assert np.linalg.norm(C+B-np.eye(3)) < 1e-12
    assert np.min(np.linalg.eigvalsh(C)) > 0
    assert np.min(np.linalg.eigvalsh(B)) >= -1e-12

def test_graph_metric_positive():
    Y=np.diag([0.0,1.0,3.0]).astype(complex)
    assert np.min(np.linalg.eigvalsh(graph_metric(Y))) > 0

def test_commuting_control_inherits_first_step_spectrum():
    state=make_commuting_control_state(dim=5,persistent_rank=3,seed=12)
    step=canonical_reclosure(state,NumericalPolicy())
    assert step.K_inherited is not None
    assert step.K_successor is not None
    assert step.diagnostics["schur_stratum_compatible"]
    assert step.spectral_mismatch < 1e-7

def test_reciprocal_balance():
    state=make_commuting_control_state(dim=5,persistent_rank=3,seed=13)
    step=canonical_reclosure(state,NumericalPolicy())
    assert step.diagnostics["reciprocal_balance_residual"] < 1e-10


def test_core_rejects_growing_recursive_operator():
    state=BFGState(
        D=np.array([1.0,1.0],complex)/np.sqrt(2.0),
        K=np.diag([-2.0,1.0]).astype(complex),
        Y=np.eye(2,dtype=complex),
        R_C=np.diag([1.0,2.0]).astype(complex),
    )
    step=canonical_reclosure(state,NumericalPolicy())
    assert not step.success
    assert "power-boundedness" in step.terminal_reason
    assert step.diagnostics["recursive_admission"]["unstable_count"]==1

def test_core_rejects_defective_unit_circle_jordan_operator():
    state=BFGState(
        D=np.array([1.0,0.0],complex),
        K=np.diag([-2.0,1.0]).astype(complex),
        Y=np.eye(2,dtype=complex),
        R_C=np.array([[1.0,1.0],[0.0,1.0]],complex),
    )
    step=canonical_reclosure(state,NumericalPolicy())
    assert not step.success
    assert "power-boundedness" in step.terminal_reason
    assert not step.diagnostics["recursive_admission"]["semisimple_peripheral"]
