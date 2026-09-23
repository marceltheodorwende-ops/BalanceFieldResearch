from bfg_studio import (
    SelfOrganizationParameters,
    PopulationParameters,
    simulate_population,
    write_population_report,
)

org = SelfOrganizationParameters(node_count=24, persistent_rank=6)
pop = PopulationParameters(
    min_unit_nodes=4,
    max_unit_nodes=40,
    max_population=12,
    node_birth_threshold=1.10,  # isolate structural fission in this demo
    max_node_births_per_step=0,
)
run = simulate_population(
    seed=1341550191,
    generations=28,
    org_params=org,
    pop_params=pop,
)
print(run.summary())
print(write_population_report(run, "outputs/population_demo"))
