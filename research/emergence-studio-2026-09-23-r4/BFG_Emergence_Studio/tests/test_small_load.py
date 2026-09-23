import numpy as np

from bfg_studio import (
    scalar_nonterminal_seed,
    reduced_closure_step,
    explicit_small_load_bound,
    termination_depth_bound,
    one_step_small_load_certificate,
    run_small_load_contraction_audit,
)

def test_explicit_small_load_bound_covers_scalar_successor():
    state=scalar_nonterminal_seed(1e-3)
    successor,step=reduced_closure_step(state)
    assert step.success
    bound=explicit_small_load_bound(
        state,
        lambda_keep=step.lambda_keep,
    )
    assert np.linalg.norm(successor.Y,2) <= bound.successor_y_bound + 1e-15

def test_termination_depth_bound_matches_recursive_upper_bound():
    y0=0.01
    C=2.5
    eps=1e-9
    n=termination_depth_bound(y0,C,eps)
    q=C*y0
    upper=(q**(2**n))/C
    assert upper<=eps
    if n>0:
        previous=(q**(2**(n-1)))/C
        assert previous>eps

def test_one_step_certificate_reports_quadratic_ratio():
    state=scalar_nonterminal_seed(1e-3)
    successor,step=reduced_closure_step(state)
    cert=one_step_small_load_certificate(
        state,
        successor,
        step,
        carrier_id="scalar",
        state_index=0,
        depth=1,
    )
    assert cert.theorem_applicable
    assert cert.bound_satisfied
    assert cert.actual_quadratic_ratio is not None
    assert cert.actual_quadratic_ratio>0

def test_small_load_audit_smoke_uses_no_heldout():
    result=run_small_load_contraction_audit(
        recursive_horizon=2,
        limit_per_carrier=2,
    )
    assert result["heldout_metrics_evaluated"] is False
    assert result["certificates"]>=6
    assert result["bound_passed"]==result["certificates"]
    assert result["bound_pass_fraction"]==1.0
