# Known-reference trajectory monitor

The new residual monitor compares sensor readings with a known healthy
reference trajectory. It flags some changes the previous diffusion-consistency
monitor misses. This is a standard model-based detector using additional
information, not a demonstration of BFG superiority.

## Observation cost and use

Run `python -m bfg_lab.reference` to generate all 288 catalogue cases, per-step
residual diagnostics and summaries in `results/reference.json`.

API: `assess_reference(r, initial, samples, sensors, initial_error=0., sensor_error=0.)`.
Supply the original reference operator, a full-network initial calibration,
equally spaced sample rows starting at time zero, and unique node indices.
Future measurements may be supplied by extending the prefix; earlier diagnostics
do not change. The monitor never receives fault type, changed topology or fault time.

`reference_inconsistent` means an observed sample is outside the stated error
budget. `no_observed_conflict` is not a health certificate. Neither status
identifies a failed edge or distinguishes forcing from parameter error.

Reference graph, weights and sampling interval are assumed exact. Initial
componentwise calibration error is bounded by e0; later reading error by e.
Starting at delta=e0*1, propagate delta_next=|R| delta and x_next=R x.
For sensor i, compare |observed_i-x_i| with delta_i+e+1e-10.
For an exact nonnegative stochastic heat operator, uniform calibration error
does not grow. The absolute numerical allowance is fixed, not fitted.

## Paired catalogue results

Same histories, seed, noise and sensors as the earlier catalogue; additional
full initial calibration uses the initial noisy data row. The detector has more
information, so this is not an equal-information superiority comparison.
See the [protocol](REFERENCE_PROTOCOL.md).

| Event | Detected with 2 sensors | With 4 | With all 8 |
| --- | ---: | ---: | ---: |
| Remove edge | 15/24 | 20/24 | 21/24 |
| External input | 18/24 | 24/24 | 24/24 |
| Eightfold speedup | 22/24 | 23/24 | 23/24 |

Normal diffusion: 0 false alarms in 24 cases at each coverage. No pre-event
alarms occurred. For detected edge removals, median delay was zero samples at
each coverage, but maximum delay was 13, 11 and 11 samples respectively. Misses
are censored at step 20 and excluded from delay statistics, not counted as fast
detections. Three edge removals remain missed even with full coverage.

The earlier full-coverage monitor detected 0/24 edge removals. The improvement
comes from reference information, not a new conservation or BFG principle.
Two or four ongoing sensors now produce useful alarms, but still require an
initial full-network calibration; this is not operation with only two sensors
available at every time.

## Self-check and limitations

A uniform initial state stays uniform after removing an edge. With no forcing,
even perfect full observations cannot distinguish those reference trajectories.
This negative case is explicitly tested. Active probing or another measurement
would be required to distinguish such systems.

The catalogue uses correctly specified topology and bounded noise. Wrong
reference weights, initial calibration bias outside the bound, missing sensors,
clock errors and model mismatch can cause alarms in a healthy network. These
are not tested reliability guarantees. No field detection rate is claimed.

Verification includes analytic two-node trajectories, calibration and reading
errors at their bounds, sensor identity validation, uniform-state invisibility,
causality of prefix diagnostics and full catalogue accounting. Existing modules
and original papers are unchanged. Reusing the previous synthetic catalogue is
an exploratory comparison, not an independent held-out test.

Fresh verification: all 52 tests in the publication set passed, exit 0. The
CLI completed all 288 cases; case identifiers and pre-event hashes match the
previous catalogue for every run. The initial focused suite failed on the absent
reference module before implementation. The separate pre-existing local
observation module is preserved outside this publication set.
