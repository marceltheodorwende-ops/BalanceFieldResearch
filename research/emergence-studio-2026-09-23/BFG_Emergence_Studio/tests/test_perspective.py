import numpy as np
from bfg_studio import (
    PerspectiveParameters,
    PerspectiveState,
    SelfOrganizationParameters,
    make_self_organizing_seed,
    MemoryState,
    EnvironmentState,
    organism_readout,
    world_readout,
    build_self_representations,
    perspective_step,
    simulate_perspective,
    compare_perspective,
)
from bfg_studio.learning import zero_policy

def test_multiple_self_representations_remain_distinct():
    org=SelfOrganizationParameters(node_count=16,persistent_rank=4)
    state=make_self_organizing_seed(seed=3,params=org)
    o=organism_readout(state,zero_policy(),MemoryState(),org)
    env=EnvironmentState(name="e",resource_supply=0.8,disturbance=0.1,carrying_capacity=6)
    w=world_readout(env)
    names,reps=build_self_representations(
        o,zero_policy(),MemoryState(),None,0.0,o,w
    )
    assert len(names) >= 5
    assert reps.shape[1] == 7
    assert np.mean(np.std(reps,axis=0)) > 0

def test_perspective_step_is_bounded_and_not_simple_sum():
    params=PerspectiveParameters()
    reps=np.array([
        [0.8,0.3,0.7,0.8,0.2,0.4,0.6],
        [0.6,0.7,0.5,0.7,0.3,0.5,0.8],
        [0.5,0.6,0.6,0.7,0.2,0.8,0.6],
        [0.7,0.5,0.7,0.8,0.2,0.5,0.7],
        [0.6,0.4,0.6,0.7,0.3,0.6,0.7],
    ])
    state=PerspectiveState(standpoint=np.mean(reps,axis=0))
    state,diag,_=perspective_step(
        state,[f"s{i}" for i in range(len(reps))],reps,params
    )
    assert np.all(np.isfinite(state.standpoint))
    assert np.max(state.standpoint) <= 1.5
    assert not np.allclose(state.standpoint,np.sum(reps,axis=0))

def test_perspective_export_removes_extreme_outlier():
    params=PerspectiveParameters(export_residual_threshold=0.35)
    core=np.array([
        [0.7,0.5,0.7,0.7,0.3,0.5,0.7],
        [0.68,0.52,0.69,0.72,0.28,0.52,0.68],
        [0.72,0.49,0.71,0.69,0.31,0.48,0.72],
        [0.69,0.51,0.68,0.71,0.29,0.50,0.70],
    ])
    outlier=np.array([[1.5,0,1.5,0,1.5,0,1.5]])
    reps=np.vstack([core,outlier])
    state=PerspectiveState(standpoint=np.mean(core,axis=0))
    state,diag,events=perspective_step(
        state,["a","b","c","d","outlier"],reps,params
    )
    assert "outlier" in diag["exported"]
    assert any(e["event"]=="perspective_export" for e in events)

def test_reference_perspective_closure_emerges():
    run=simulate_perspective(seed=1341550191,generations=40)
    assert any(f["perspective_closure"] for f in run.frames)
    assert run.successful_reclosures >= 30

def test_perspective_ablation_never_claims_closure():
    run=simulate_perspective(
        seed=1341550191,generations=30,perspective_enabled=False
    )
    assert not any(f["perspective_closure"] for f in run.frames)

def test_reference_perspective_standpoint_persists():
    comp=compare_perspective(seed=1341550191,generations=64)
    s=comp["perspective"].summary()
    assert s["mean_standpoint_persistence"] > 0.9
    assert comp["summary"]["perspective_closure_fraction"] > 0.5


def test_perspective_detects_fragmentation():
    params=PerspectiveParameters(
        max_multiplicity_unity=0.20,
        export_residual_threshold=2.0,
    )
    reps=np.array([
        [0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1],
        [0,1,0,1,0,1,0],
        [1,0,1,0,1,0,1],
        [0.9,0.1,0.9,0.1,0.9,0.1,0.9],
    ],dtype=float)
    state=PerspectiveState(standpoint=np.full(7,0.5))
    state,diag,_=perspective_step(
        state,[f"s{i}" for i in range(5)],reps,params
    )
    assert not diag["closure"]
    assert diag["failure"]=="fragmentation"
    assert state.fragmentation_failures >= 1

def test_perspective_detects_over_unification():
    params=PerspectiveParameters(
        epsilon_multiplicity_unity=0.08,
        max_multiplicity_unity=0.62,
    )
    reps=np.tile(np.array([[0.6,0.6,0.6,0.6,0.6,0.6,0.6]]),(5,1))
    state=PerspectiveState(standpoint=np.full(7,0.6))
    state,diag,_=perspective_step(
        state,[f"s{i}" for i in range(5)],reps,params
    )
    assert not diag["closure"]
    assert diag["failure"]=="over_unification"
    assert state.over_unification_failures >= 1

def test_perspective_detects_representational_collapse():
    params=PerspectiveParameters(minimum_active_representations=4)
    reps=np.array([
        [0.7]*7,
        [0.6]*7,
        [0.0]*7,
        [0.0]*7,
        [0.0]*7,
    ],dtype=float)
    state=PerspectiveState(standpoint=np.full(7,0.6))
    state,diag,_=perspective_step(
        state,[f"s{i}" for i in range(5)],reps,params
    )
    assert not diag["closure"]
    assert diag["failure"]=="representational_collapse"
    assert state.collapse_failures >= 1

def test_perspective_detects_recursive_instability():
    params=PerspectiveParameters(
        recurrent_alpha=0.99,
        recursive_rho_max=0.98,
        export_residual_threshold=2.0,
    )
    reps=np.array([
        [0.7,0.5,0.7,0.7,0.3,0.5,0.7],
        [0.6,0.6,0.6,0.6,0.4,0.6,0.6],
        [0.8,0.4,0.7,0.8,0.2,0.5,0.7],
        [0.65,0.55,0.65,0.7,0.3,0.55,0.65],
        [0.75,0.45,0.72,0.75,0.25,0.52,0.69],
    ])
    state=PerspectiveState(standpoint=np.full(7,0.6))
    state,diag,_=perspective_step(
        state,[f"s{i}" for i in range(5)],reps,params
    )
    assert not diag["closure"]
    assert diag["failure"]=="recursive_instability"
    assert state.instability_failures >= 1
