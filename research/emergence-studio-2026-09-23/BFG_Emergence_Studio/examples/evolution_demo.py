from bfg_studio import (
    SelfOrganizationParameters,
    PopulationParameters,
    EvolutionParameters,
    simulate_evolution,
    write_evolution_report,
)

org = SelfOrganizationParameters(node_count=24, persistent_rank=6)
pop = PopulationParameters(
    min_unit_nodes=4,
    max_unit_nodes=40,
    max_population=8,
    node_birth_threshold=1.05,
    max_node_births_per_step=0,
)
evo = EvolutionParameters(
    mutation_rate=1.0,
    mutation_sigma=0.05,
    carrying_capacity=1,
    max_candidate_population=3,
    minimum_reproductive_age=3,
)

run = simulate_evolution(
    seed=1341550191,
    generations=32,
    base_org=org,
    base_pop=pop,
    evo=evo,
)
print(run.summary())
print(write_evolution_report(run, "outputs/evolution_demo"))
