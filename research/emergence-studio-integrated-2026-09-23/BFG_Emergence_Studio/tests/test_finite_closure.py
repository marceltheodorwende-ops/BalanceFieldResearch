import numpy as np
import pytest

from bfg_studio import (
    ReducedClosureState,
    reduced_closure_step,
    iterate_reduced_closure,
    scalar_nonterminal_seed,
    bounded_infinite_entry_contract,
)

def test_scalar_nonterminal_update_matches_analytic_formula():
    y=1.0
    state=scalar_nonterminal_seed(y)
    nxt,step=reduced_closure_step(state,tau=1.0)
    assert step.success
    assert not nxt.bottom
    expected=2*y*y/((1+y)**2*(1+y*y))
    assert np.allclose(nxt.K,[[-1.0]],atol=1e-12)
    assert np.allclose(nxt.rho,[[1.0]],atol=1e-12)
    assert np.allclose(nxt.Y,[[expected]],atol=1e-12)
    assert np.allclose(nxt.R,[[np.exp(-1j)]],atol=1e-12)

def test_scalar_exact_model_iterates_multiple_steps_until_numerical_resolution():
    state=scalar_nonterminal_seed(1.0)
    run=iterate_reduced_closure(state,4,tau=1.0)
    assert run["executed_steps"]>=1
    for st in run["states"]:
        if not st.bottom:
            assert st.Y.shape==(1,1)
            assert np.real(st.Y[0,0])>0

def test_bottom_is_absorbing():
    state=ReducedClosureState(bottom=True,generation=7,reason="terminal")
    nxt,step=reduced_closure_step(state)
    assert nxt is state
    assert step.terminal
    assert not step.success

def test_growing_recursive_input_is_rejected():
    state=ReducedClosureState(
        rho=np.array([[1.0]],complex),
        K=np.array([[-1.0]],complex),
        Y=np.array([[1.0]],complex),
        R=np.array([[1.01]],complex),
    )
    with pytest.raises(ValueError,match="power-boundedness"):
        reduced_closure_step(state)

def test_unit_circle_jordan_input_is_rejected():
    state=ReducedClosureState(
        rho=np.array([[1.0,0.0],[0.0,0.0]],complex),
        K=np.diag([-1.0,1.0]).astype(complex),
        Y=np.eye(2,dtype=complex),
        R=np.array([[1.0,1.0],[0.0,1.0]],complex),
    )
    with pytest.raises(ValueError,match="power-boundedness"):
        reduced_closure_step(state)

def test_failed_formation_gate_maps_to_bottom():
    state=ReducedClosureState(
        rho=np.array([[1.0]],complex),
        K=np.array([[1.0]],complex),
        Y=np.array([[1.0]],complex),
        R=np.array([[1.0]],complex),
    )
    nxt,step=reduced_closure_step(state)
    assert nxt.bottom
    assert step.terminal
    assert "formation gate failed" in step.reason

def test_successor_recursion_is_unitary_and_gram_rebuild_exact():
    state=scalar_nonterminal_seed(1.0)
    nxt,step=reduced_closure_step(state)
    eye=np.eye(nxt.dim)
    assert np.linalg.norm(nxt.R.conj().T@nxt.R-eye)<1e-10
    assert step.diagnostics["gram_rebuild_residual"]<1e-12

def test_bounded_infinite_entry_contract_reduces_to_finite_runtime():
    contract=bounded_infinite_entry_contract()
    assert contract["peripheral_riesz_range"]=="finite-dimensional"
    assert "reduces" in contract["consequence"]
