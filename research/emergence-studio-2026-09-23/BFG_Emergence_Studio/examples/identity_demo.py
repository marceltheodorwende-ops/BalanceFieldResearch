from bfg_studio import (
    IdentityParameters,
    compare_identity,
    write_identity_report,
    write_identity_comparison,
)

params = IdentityParameters(
    recurrent_alpha=0.965,
    epsilon_identity=0.0015,
    max_identity_distance=0.14,
    export_component_threshold=0.16,
    minimum_self_index_similarity=0.80,
)

comparison = compare_identity(
    seed=1341550191,
    generations=120,
    identity_params=params,
)

run = comparison["identity"]
control = comparison["ablated_control"]

print(run.summary())
print(control.summary())
print(comparison["summary"])

write_identity_report(run, "outputs/identity_demo", "identity")
write_identity_report(control, "outputs/identity_demo", "control")
write_identity_comparison(
    comparison,
    "outputs/identity_demo",
    "comparison",
)
