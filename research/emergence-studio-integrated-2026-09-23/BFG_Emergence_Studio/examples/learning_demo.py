from bfg_studio import (
    LearningParameters,
    compare_memory_learning,
    write_learning_report,
    write_learning_comparison,
)

learn = LearningParameters(
    exploration_sigma=0.035,
    retrieval_blend=0.92,
    max_memory_slots=8,
    witness_min_gap=4,
)

comparison = compare_memory_learning(
    seed=1341550191,
    generations=60,
    learn=learn,
)

memory_run = comparison["memory_enabled"]
control_run = comparison["memory_disabled"]

print(memory_run.summary())
print(control_run.summary())
print(comparison["summary"])

write_learning_report(memory_run, "outputs/learning_demo", "memory")
write_learning_report(control_run, "outputs/learning_demo", "control")
write_learning_comparison(
    comparison,
    "outputs/learning_demo",
    "comparison",
)
