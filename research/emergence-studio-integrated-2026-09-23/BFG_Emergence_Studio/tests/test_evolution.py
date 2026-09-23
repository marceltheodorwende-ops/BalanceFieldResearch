import numpy as np
from bfg_studio import (
    SelfOrganizationParameters,
    PopulationParameters,
    EvolutionParameters,
    default_traits,
    mutate_traits,
    simulate_evolution,
)

def test_mutation_respects_bounds():
    org=SelfOrganizationParameters(node_count=16,persistent_rank=4)
    pop=PopulationParameters()
    traits=default_traits(org,pop)
    evo=EvolutionParameters(mutation_rate=1.0,mutation_sigma=0.2)
    rng=np.random.default_rng(4)
    child,changes=mutate_traits(traits,rng,evo)
    from bfg_studio.evolution import TRAIT_BOUNDS
    assert changes
    for k,(lo,hi) in TRAIT_BOUNDS.items():
        assert lo <= child[k] <= hi

def test_evolution_simulation_executes():
    org=SelfOrganizationParameters(node_count=20,persistent_rank=5)
    pop=PopulationParameters(
        min_unit_nodes=4,max_unit_nodes=30,max_population=12,
        node_birth_threshold=0.95,
    )
    evo=EvolutionParameters(
        carrying_capacity=6,
        max_candidate_population=12,
        minimum_reproductive_age=3,
    )
    run=simulate_evolution(seed=11,generations=6,base_org=org,base_pop=pop,evo=evo)
    assert len(run.frames) >= 2
    assert run.core_steps >= 1
    assert run.frames[0]["population_size"] == 1

def test_reference_lineage_produces_heritable_children():
    org=SelfOrganizationParameters(node_count=24,persistent_rank=6)
    pop=PopulationParameters(
        min_unit_nodes=4,max_unit_nodes=40,max_population=16,
        node_birth_threshold=1.05,max_node_births_per_step=0,
    )
    evo=EvolutionParameters(
        mutation_rate=1.0,
        mutation_sigma=0.03,
        carrying_capacity=8,
        max_candidate_population=16,
        minimum_reproductive_age=5,
    )
    run=simulate_evolution(
        seed=1341550191,generations=24,
        base_org=org,base_pop=pop,evo=evo,
    )
    births=[e for e in run.events if e["event"]=="unit_birth" and e.get("parent_id") is not None]
    mutations=[e for e in run.events if e["event"]=="mutation"]
    assert len(births) >= 2
    assert len(mutations) >= 1
    assert max(f["max_lineage_depth"] for f in run.frames) >= 1
