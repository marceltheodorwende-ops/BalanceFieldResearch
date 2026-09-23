import numpy as np
from bfg_studio import (
    SelfModelParameters,
    SelfOrganizationParameters,
    make_self_organizing_seed,
    MemoryState,
    organism_readout,
    world_readout,
    self_closure_readout,
    self_world_distance,
    EnvironmentState,
    simulate_self_model,
    compare_self_model,
)
from bfg_studio.learning import zero_policy

def test_self_readouts_preserve_separate_world_and_organism_blocks():
    org=SelfOrganizationParameters(node_count=16,persistent_rank=4)
    state=make_self_organizing_seed(seed=3,params=org)
    o=organism_readout(state,zero_policy(),MemoryState(),org)
    env=EnvironmentState(name="e",resource_supply=0.8,disturbance=0.1,carrying_capacity=6)
    w=world_readout(env)
    s=self_closure_readout(w,o)
    assert w.shape==(3,)
    assert o.shape==(7,)
    assert s.shape==(13,)
    assert np.allclose(s[:3],w)
    assert np.allclose(s[3:10],o)
    assert self_world_distance(w,o) >= 0

def test_self_model_predictor_is_bounded():
    params=SelfModelParameters(recurrent_rho_max=1.02,min_observations=4)
    run=simulate_self_model(seed=11,generations=20,self_params=params)
    assert run.successful_reclosures >= 10
    assert run.self_model.predictor.recurrent_rho() <= 1.0200001

def test_self_reference_reachability_emerges():
    params=SelfModelParameters(min_observations=5)
    run=simulate_self_model(seed=1341550191,generations=36,self_params=params)
    assert any(f["self_reference_reachable"] for f in run.frames[8:])
    assert any(f["self_model_closure"] for f in run.frames[8:])

def test_self_model_makes_action_interventions():
    run=simulate_self_model(seed=1341550191,generations=36)
    assert run.self_model.action_interventions >= 1

def test_self_model_prediction_becomes_competitive_after_learning():
    comp=compare_self_model(seed=1341550191,generations=80)
    summary=comp["summary"]
    assert summary["prediction_beats_persistence_fraction"] > 0.45
    assert summary["mean_prediction_error"] <= 1.05*summary["mean_persistence_baseline_error"]
    assert summary["mean_reward_gain"] > 0


def test_ablated_control_never_claims_self_reference_closure():
    run=simulate_self_model(
        seed=1341550191,
        generations=36,
        self_model_enabled=False,
    )
    assert not any(f["self_reference_reachable"] for f in run.frames)
    assert not any(f["self_model_closure"] for f in run.frames)

def test_world_self_corridor_is_noncollapsed_in_reference_run():
    run=simulate_self_model(seed=1341550191,generations=36)
    distances=[f["world_self_distance"] for f in run.frames]
    assert min(distances) > 0
    assert all(f["world_self_corridor"] for f in run.frames)
