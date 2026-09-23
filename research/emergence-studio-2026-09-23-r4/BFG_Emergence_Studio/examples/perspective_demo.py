from bfg_studio import (
    PerspectiveParameters,
    compare_perspective,
    write_perspective_report,
    write_perspective_comparison,
)

params = PerspectiveParameters(
    recurrent_alpha=0.985,
    epsilon_multiplicity_unity=0.035,
    max_multiplicity_unity=0.62,
    export_residual_threshold=0.46,
    standpoint_action_weight=0.05,
)

comparison = compare_perspective(
    seed=1341550191,
    generations=96,
    perspective_params=params,
)

run = comparison["perspective"]
control = comparison["ablated_control"]

print(run.summary())
print(control.summary())
print(comparison["summary"])

write_perspective_report(run, "outputs/perspective_demo", "perspective")
write_perspective_report(control, "outputs/perspective_demo", "control")
write_perspective_comparison(
    comparison,
    "outputs/perspective_demo",
    "comparison",
)
