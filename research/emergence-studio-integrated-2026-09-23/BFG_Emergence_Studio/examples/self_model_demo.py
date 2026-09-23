from bfg_studio import (
    SelfModelParameters,
    compare_self_model,
    write_self_model_report,
    write_self_model_comparison,
)

params = SelfModelParameters(
    min_observations=12,
    candidate_count=5,
    candidate_sigma=0.035,
    recurrent_rho_max=1.04,
)

comparison = compare_self_model(
    seed=1341550191,
    generations=80,
    self_params=params,
)

run = comparison["self_model"]
control = comparison["ablated_control"]

print(run.summary())
print(control.summary())
print(comparison["summary"])

write_self_model_report(run, "outputs/self_model_demo", "self_model")
write_self_model_report(control, "outputs/self_model_demo", "control")
write_self_model_comparison(
    comparison,
    "outputs/self_model_demo",
    "comparison",
)
