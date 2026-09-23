from bfg_studio import (
    run_benchmark_suite,
    run_robustness_suite,
    run_seed_sweep,
)

def test_canonical_reference_benchmark_passes():
    report=run_benchmark_suite(selected=["canonical_core"])
    assert report.passed
    assert len(report.results)==1

def test_small_robustness_suite_passes():
    report=run_robustness_suite(
        randomized_trials=20,
        commuting_controls=8,
        noncommuting_controls=8,
        seed=1234,
        workers=2,
    )
    assert report.randomized_failures==0
    assert report.commuting_failures==0
    assert report.tolerance_classification_stable
    assert report.diagnostics["invalid_input_guard"]["rejected"]

def test_parallel_seed_sweep_executes():
    sweep=run_seed_sweep(
        seeds=[3,5,7],
        mode="alife",
        horizon=4,
        workers=2,
    )
    assert len(sweep.items)==3
    assert all(item.mode=="alife" for item in sweep.items)
