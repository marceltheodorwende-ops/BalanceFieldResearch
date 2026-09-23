import numpy as np
from bfg_studio import (
    LearningParameters,
    MemoryState,
    EnvironmentState,
    environment_cue,
    cue_similarity,
    simulate_learning,
    compare_memory_learning,
)

def test_environment_cue_and_similarity():
    e=EnvironmentState(name="x",resource_supply=0.8,disturbance=0.1,carrying_capacity=6)
    c=environment_cue(e)
    assert c.shape==(3,)
    assert cue_similarity(c,c) > 0.999999

def test_learning_run_records_memory():
    learn=LearningParameters(witness_min_gap=3,max_memory_slots=6)
    run=simulate_learning(seed=11,generations=24,learn=learn,memory_enabled=True)
    assert len(run.frames) >= 10
    assert run.core_steps >= 1
    assert len(run.final_unit.memory.slots) >= 1
    assert any(e["event"]=="memory_encode" for e in run.events)

def test_recurring_context_recovers_witness():
    learn=LearningParameters(witness_min_gap=4,max_memory_slots=8)
    run=simulate_learning(seed=1341550191,generations=44,learn=learn,memory_enabled=True)
    recoveries=[e for e in run.events if e["event"]=="witness_recovery"]
    assert len(recoveries) >= 1
    assert max(e["trace_age"] for e in recoveries) >= 4

def test_memory_disabled_control_has_no_slots():
    run=simulate_learning(seed=9,generations=12,memory_enabled=False)
    assert len(run.final_unit.memory.slots)==0

def test_comparison_executes():
    comp=compare_memory_learning(seed=5,generations=20)
    assert comp["summary"]["compared_steps"] >= 10


def test_policy_updates_are_bounded():
    learn=LearningParameters(max_policy_step=0.08,witness_min_gap=4)
    run=simulate_learning(seed=21,generations=24,learn=learn,memory_enabled=True)
    changes=[f["policy_change_norm"] for f in run.frames]
    assert max(changes) <= learn.max_policy_step + 1e-10

def test_memory_export_bounds_slot_count():
    from bfg_studio.learning import update_memory, zero_policy
    learn=LearningParameters(
        max_memory_slots=2,
        memory_similarity_threshold=0.99,
        memory_merge_threshold=0.999,
    )
    mem=MemoryState()
    counter=0
    cues=[
        np.array([0.0,0.0,0.0]),
        np.array([1.0,0.0,0.0]),
        np.array([0.0,1.0,0.0]),
    ]
    for g,cue in enumerate(cues):
        _,counter=update_memory(mem,cue,zero_policy(),0.5+0.1*g,g,learn,counter)
    assert len(mem.slots) <= 2
    assert mem.exported_slots >= 1

def test_reference_memory_improves_mean_reward():
    comp=compare_memory_learning(seed=1341550191,generations=60)
    assert comp["summary"]["mean_reward_gain_memory_vs_control"] > 0
    assert comp["summary"]["witness_recoveries"] >= 1
