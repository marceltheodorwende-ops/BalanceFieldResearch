from bfg_studio import (
    SelfOrganizationParameters,
    PopulationParameters,
    simulate_population,
)

def test_population_simulation_runs():
    org=SelfOrganizationParameters(node_count=18,persistent_rank=5)
    pop=PopulationParameters(
        min_unit_nodes=4,
        max_unit_nodes=28,
        max_population=8,
        node_birth_threshold=0.96,
    )
    run=simulate_population(seed=11,generations=4,org_params=org,pop_params=pop)
    assert len(run.frames) >= 2
    assert run.core_steps >= 1
    assert run.frames[0]["population_size"] == 1

def test_population_tracks_dimension_events():
    org=SelfOrganizationParameters(node_count=18,persistent_rank=5)
    pop=PopulationParameters(
        min_unit_nodes=4,
        max_unit_nodes=24,
        max_population=8,
        node_birth_threshold=0.70,
        max_node_births_per_step=1,
    )
    run=simulate_population(seed=7,generations=5,org_params=org,pop_params=pop)
    assert any(e["event"] in ("node_birth","node_loss","fission","unit_death")
               for e in run.events)

def test_reference_seed_can_create_independent_children():
    org=SelfOrganizationParameters(node_count=24,persistent_rank=6)
    pop=PopulationParameters(
        min_unit_nodes=4,
        max_unit_nodes=40,
        max_population=8,
        node_birth_threshold=1.10,  # disable birth to preserve known structural split
        max_node_births_per_step=0,
    )
    run=simulate_population(seed=1341550191,generations=22,org_params=org,pop_params=pop)
    fissions=[e for e in run.events if e["event"]=="fission"]
    assert len(fissions) >= 1
    assert max(f["population_size"] for f in run.frames) >= 2
