from bfg_studio import NumericalPolicy, ReferenceGramCarrier, make_random_seed_state, simulate
from bfg_studio.report import write_run_report
state=make_random_seed_state(dim=6,persistent_rank=4,seed=17)
run=simulate(state,ReferenceGramCarrier(),steps=12,policy=NumericalPolicy())
print(run.summary())
print(write_run_report(run,"outputs","emergence_example"))
