# Fault catalogue results, 2026-09-15

The unchanged monitor was evaluated on 288 runs under the fixed
[protocol](DETECTION_PROTOCOL.md). Each run consumes prefixes only, one sample
at a time. Run `python -m bfg_lab.detection` to regenerate all status histories,
first alarm reasons, paired prefix hashes, summary and protocol hash in
`results/detection.json`. No thresholds were tuned after observing results.

## Full observation (eight sensors)

| Scenario | Runs | Alarms | No alarm through step 20 |
| --- | ---: | ---: | ---: |
| Normal diffusion | 24 | 0 | 24 |
| Remove an edge | 24 | 0 | 24 |
| External input +0.5 | 24 | 24 | 0 |
| Eightfold coupling speedup | 24 | 20 | 4 |

There were no pre-event alarms. All detected events alarmed at sample 7,
the first affected sample: median and maximum delay zero sampling intervals.
This does not mean zero real-time latency or guaranteed detection of smaller
inputs. Four speedup cases and every edge removal were missed by the horizon.
The healthy full-observation baseline had 0 false alarms in 24 constructed cases.

These are paired simulations with only two topologies, two weights, two initial
states and three noise amplitudes. They are not independent field trials, so no
general reliability estimate or confidence interval is claimed. Noise is bounded
uniform noise with the correct bound supplied to the monitor. Unknown bounds,
drift, wrong sensor identities and gross outliers are not covered.

## Partial observation

All 192 runs with two or four sensors abstained from a global judgement. This
is the monitor's explicit coverage rule, not an empirical discovery that four
sensors can never work. Neither coverage level can detect a global fault with
this implementation. Abstentions are not credited as correct healthy decisions
or included as ordinary full-coverage detection misses.

## Interpretation and next engineering decision

This prototype can check some violations of the fixed diffusion assumption.
It is unsuitable as a general connection-failure detector: all 24 tested edge
removals went undetected even with full coverage. A passing consistency check
must never be displayed as a network health certificate.

A connection monitor needs extra information, such as a specified reference
topology and predicted sensor trajectories, or active probing. That would be
a new method with a new observation and calibration budget, requiring its own
test protocol. The current evaluation supplies evidence for choosing that scope;
it does not establish BFG predictive superiority.

## Verification

All 46 tests in the publication set passed. The new catalogue test verifies all
288 runs, exact outcome accounting, delay arithmetic, all coverage abstentions,
and identical pre-event data/statuses across paired scenarios. The initial
focused run failed because the catalogue module was absent. Both execution and
tests completed with exit 0. The separate pre-existing local observation module
is preserved and is outside this publication set.

JSON field `detected` is a generic first alarm at or after sample 7; for the
normal scenario any such alarm would count as a false alarm, not a detection.
`no_alarm` means only no alarm by the finite horizon, never proven health.
