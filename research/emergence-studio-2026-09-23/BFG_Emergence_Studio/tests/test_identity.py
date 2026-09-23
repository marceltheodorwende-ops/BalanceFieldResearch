import numpy as np
from bfg_studio import (
    IdentityParameters,
    make_identity_state,
    identity_step,
    simulate_identity,
    compare_identity,
)

def test_identity_corridor_accepts_bounded_change():
    params=IdentityParameters(
        epsilon_identity=0.001,
        max_identity_distance=0.20,
        export_component_threshold=1.0,
    )
    initial=np.array([0.6,0.5,0.7,0.6,0.3,0.5,0.7],dtype=float)
    present=initial+np.array([0.02,-0.01,0.01,0.0,0.01,0.02,-0.01])
    state=make_identity_state(initial)
    state,diag,_=identity_step(state,present,params,generation=1)
    assert diag["closure"]
    assert params.epsilon_identity < diag["raw_distance"] < params.max_identity_distance

def test_identity_detects_fragmentation():
    params=IdentityParameters(
        epsilon_identity=0.001,
        max_identity_distance=0.10,
        export_component_threshold=1.0,
    )
    initial=np.full(7,0.2)
    present=np.full(7,1.0)
    state=make_identity_state(initial)
    state,diag,_=identity_step(state,present,params,generation=1)
    assert not diag["closure"]
    assert diag["failure"]=="fragmentation"
    assert state.fragmentation_failures >= 1

def test_identity_detects_rigidity():
    params=IdentityParameters(
        epsilon_identity=0.01,
        max_identity_distance=0.20,
        export_component_threshold=1.0,
    )
    initial=np.full(7,0.5)
    present=initial+1e-5
    state=make_identity_state(initial)
    state,diag,_=identity_step(state,present,params,generation=1)
    assert not diag["closure"]
    assert diag["failure"]=="rigidity"
    assert state.rigidity_failures >= 1

def test_identity_detects_recursive_instability():
    params=IdentityParameters(
        recurrent_alpha=0.99,
        recurrent_rho_max=0.98,
        epsilon_identity=0.001,
        max_identity_distance=0.20,
        export_component_threshold=1.0,
    )
    initial=np.full(7,0.5)
    present=initial+0.02
    state=make_identity_state(initial)
    state,diag,_=identity_step(state,present,params,generation=1)
    assert not diag["closure"]
    assert diag["failure"]=="recursive_instability"
    assert state.instability_failures >= 1

def test_identity_export_removes_obsolete_historical_component():
    params=IdentityParameters(
        epsilon_identity=0.001,
        max_identity_distance=0.30,
        export_component_threshold=0.10,
    )
    initial=np.array([0.5,0.5,0.5,0.5,0.5,0.5,0.5])
    present=np.array([0.5,0.5,0.5,0.5,0.5,0.5,0.65])
    state=make_identity_state(initial)
    state,diag,events=identity_step(state,present,params,generation=1)
    assert 6 in diag["exported"]
    assert any(e["event"]=="identity_export" for e in events)
    assert state.exports >= 1

def test_reference_identity_closure_emerges():
    run=simulate_identity(seed=1341550191,generations=64)
    assert run.perspective_run.successful_reclosures >= 60
    assert run.final_identity.closure_passes >= 50
    assert any(f["identity_closure"] for f in run.frames[1:])

def test_identity_ablation_never_claims_closure():
    comp=compare_identity(seed=1341550191,generations=48)
    control=comp["ablated_control"]
    assert not any(f["identity_closure"] for f in control.frames)

def test_identity_preserves_index_while_allowing_change():
    comp=compare_identity(seed=1341550191,generations=96)
    s=comp["identity"].summary()
    assert s["minimum_self_index_similarity"] > 0.80
    assert s["mean_transverse_adaptation"] > 0.01
    assert comp["summary"]["continuity_smoothing_gain"] > 0
