from bfg_studio import (
    SelfOrganizationParameters,
    PopulationParameters,
    EvolutionParameters,
    standard_shift_program,
    simulate_environmental_evolution,
    write_environmental_report,
)

org = SelfOrganizationParameters(node_count=24, persistent_rank=6)
pop = PopulationParameters(
    min_unit_nodes=4,
    max_unit_nodes=42,
    max_population=64,
    node_birth_threshold=0.90,
)
evo = EvolutionParameters(
    mutation_rate=0.85,
    mutation_sigma=0.055,
    carrying_capacity=12,
    max_candidate_population=24,
    minimum_reproductive_age=4,
)

run = simulate_environmental_evolution(
    seed=1341550191,
    generations=60,
    program=standard_shift_program(shift_generation=24),
    base_org=org,
    base_pop=pop,
    evo=evo,
    founder_count=12,
    founder_sigma=0.18,
)
print(run.summary())
print(write_environmental_report(run, "outputs/environment_demo"))
