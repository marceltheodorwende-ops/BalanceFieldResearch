from bfg_studio import (
    scalar_neutral_load_map,
    FORMATION_NORMALIZATIONS,
    run_formation_termination_analysis,
)

def test_scalar_neutral_load_map_has_quadratic_small_load_asymptotic():
    y=1e-6
    y_next=scalar_neutral_load_map(y)
    ratio=y_next/(2*y*y)
    assert abs(ratio-1.0)<5e-6

def test_formation_normalization_candidates_are_fixed_and_complete():
    assert FORMATION_NORMALIZATIONS==(
        "depth_over_spectral_norm",
        "depth_over_rms_norm",
        "depth_over_gap",
        "depth_over_mean_abs_eigenvalue",
    )

def test_formation_analysis_smoke_uses_only_allowed_real_states():
    result=run_formation_termination_analysis(
        horizon=3,
        limit_per_carrier=2,
    )
    assert result["heldout_metrics_evaluated"] is False
    assert result["states_total"]==6
    assert result["first_step_successes"]==6
    assert len(result["formation_normalization_corridors"])==4
    assert result["pooled_y_decay_pairs"]>=6
    assert result["interpretation_guard"]["normalization_selected_posthoc"] is False
