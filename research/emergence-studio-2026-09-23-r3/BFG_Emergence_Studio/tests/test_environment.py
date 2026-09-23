import numpy as np
from bfg_studio import (
    SelfOrganizationParameters,
    PopulationParameters,
    EvolutionParameters,
    standard_shift_program,
    trait_match,
    make_self_organizing_seed,
    apply_environment,
    simulate_environmental_evolution,
)

def test_environment_program_switches():
    p=standard_shift_program(shift_generation=9)
    assert p.at(0).name=="resource_rich_connected"
    assert p.at(8).name=="resource_rich_connected"
    assert p.at(9).name=="resource_poor_fragmenting"
    assert p.shift_generations==[9]

def test_environment_forcing_preserves_state_shapes_and_bounds():
    org=SelfOrganizationParameters(node_count=16,persistent_rank=4)
    s=make_self_organizing_seed(seed=3,params=org)
    env=standard_shift_program(5).at(5)
    forced,diag=apply_environment(s,env,org,np.random.default_rng(2))
    assert forced.D.shape==s.D.shape
    assert forced.K.shape==s.K.shape
    assert forced.Y.shape==s.Y.shape
    assert np.min(forced.metadata["resource"]) >= 0
    assert np.max(forced.metadata["resource"]) <= 1
    assert np.min(np.linalg.eigvalsh(forced.Y)) >= -1e-9
    assert diag["environment"]==env.name

def test_trait_match_prefers_target():
    env=standard_shift_program(5).at(5)
    exact=dict(env.preferred_traits)
    far={}
    from bfg_studio.evolution import TRAIT_BOUNDS
    for k,target in env.preferred_traits.items():
        lo,hi=TRAIT_BOUNDS[k]
        far[k]=lo if abs(target-lo)>abs(target-hi) else hi
    assert trait_match(exact,env) > trait_match(far,env)

def test_environmental_evolution_records_shift_and_selection():
    org=SelfOrganizationParameters(node_count=18,persistent_rank=5)
    pop=PopulationParameters(min_unit_nodes=4,max_unit_nodes=28,max_population=20,node_birth_threshold=0.95)
    evo=EvolutionParameters(carrying_capacity=10,max_candidate_population=20,minimum_reproductive_age=3)
    program=standard_shift_program(shift_generation=4)
    run=simulate_environmental_evolution(
        seed=11,generations=7,program=program,
        base_org=org,base_pop=pop,evo=evo,
        founder_count=10,founder_sigma=0.14,
    )
    assert any(e["event"]=="environment_shift" for e in run.events)
    assert any(e["event"]=="selection_round" for e in run.events)
    assert run.frames[4]["environment"]=="resource_poor_fragmenting"
    assert run.core_steps >= 1
