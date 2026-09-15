# Detection catalogue V1, 2026-09-15

Fixed before execution; synthetic diagnostic evaluation, not external registration.
Monitor thresholds and logic remain unchanged.

Eight nodes; path and cycle; edge weights 0.5 and 1; dt=0.2; initial impulse
at node zero and seeded positive random state normalized to sum one. Seed
20260916. Horizon 20. At sample 7: no change, remove edge (3,4), add 0.5 to
node 7, or multiply all edge weights by 8. Uniform independent scalar noise
in [-e,e], e=0,0.001,0.01, supplied to the monitor as the true error bound.
Reuse each noise matrix across the four scenarios for paired pre-event data.

Coverage: nodes [0,1], [0,1,4,5], all eight. This gives 96 underlying noisy
histories and 288 monitor runs. Evaluate every prefix ending at steps 1..20;
no future sample enters an earlier assessment. All runs assert the fixed-heat
assumption so that violations, not missing declarations, control abstention.

Report by scenario and sensor count: runs, first alarms before step 7, alarms
from step 7, no alarm by horizon, and coverage abstentions. For faulty cases,
delay=first alarm step minus 7, only if no earlier alarm existed. A pre-event
alarm is not credited as detection. Baseline alarms at any time are false alarms.
Partial-coverage abstentions are reported separately, never as successful
detections, healthy outcomes or ordinary full-coverage misses. No threshold
tuning or exclusion of difficult cases after inspecting outcomes.

Expected structural limitation: this version always abstains at partial coverage.
Thus two versus four sensors cannot improve global detection without a new
method. Fault-detection percentages here are descriptive for this constructed
catalogue and bounded-noise assumption, not field reliability estimates.
