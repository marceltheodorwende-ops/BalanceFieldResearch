# Reference error and known excitation: sensitivity results

The 144-case [fixed protocol](REFERENCE_STRESS_PROTOCOL.md) is complete.
Reproduce with `python -m bfg_lab.reference_stress`; full rows and the protocol
hash are saved to `results/reference_stress.json`. Existing detector code and
thresholds were not changed. Impulses are simulated only.

## Known initial impulse resolves some invisible failures

With exact weights and unbiased calibration (declared error 0.001), the four
uniform-state cut cases yield no alarm. Adding the known initial impulse makes
all four cut cases alarm; the corresponding four intact cases still have no
alarm. Median first alarm for these cuts is sample 6. The cuts exist before
sample 0, so this is elapsed observation time, not a later event delay.

This is four constructed graph/weight cases, not a reliable 100% field detection
rate. The input amplitude is 0.5 in the synthetic state units. No claim is made
that the same excitation is feasible or safe on a physical application.

## Reference mismatch produces alarms without a physical fault

With unbiased calibration and a known impulse, +/-10% reference weight error
causes alarms in all eight intact cases (four at each scale). Median first alarm
is sample 1. The detector correctly reports inconsistency with its supplied
reference, but treating this as a connection-failure diagnosis would be wrong.
Alarms in faulty cases with the same wrong reference cannot be credited as
unambiguous fault detection because their intact counterparts already alarm.

Without excitation the uniform state does not reveal either weight mismatch
or a missing edge. Absence of an alarm there is not evidence for correct weights.

## Calibration uncertainty creates a sensitivity tradeoff

At exact reference weights, add +0.02 calibration bias at node zero:

| Declared initial error | Intact excited cases alarming | Cut excited cases alarming |
| --- | ---: | ---: |
| Honest bound 0.021 | 0/4 | 1/4 |
| Understated bound 0.001 | 4/4 | 4/4 |

The understated budget triggers at sample 0: those alarms reveal inconsistent
calibration and readings, not evidence that a connection has failed. Under the
honest budget, three cuts are missed by the 20-sample horizon. A wider allowance
is not a free improvement; it hides smaller deviations as well.

The honest budget applies uniformly to all nodes although the injected bias
affects one. It is conservative. Component-specific calibration bounds could
be investigated separately, but were not tuned in this evaluation.

## Engineering implication

The monitor is currently a reference-consistency checker. Before using its
alarms as fault indicators, represent plausible graph/parameter uncertainty and
separate calibration conflicts from later dynamical discrepancies. Increasing
the alarm threshold alone does not establish robust fault discrimination.

The experiment is synthetic and small. Only a common +/-10% weight scaling,
one bias location, one impulse and two topologies were examined. Nonuniform
weight errors, optimized probing, practical measurement constraints and real
data remain untested. This work does not establish new BFG predictions.

Verification: 53 tests in the publication set passed. The new check covers
catalogue size, outcome accounting, valid-reference controls, unexcited invisible
cuts and identical paired measurements across reference/calibration alternatives.
The focused test initially failed on the absent module. CLI and final tests
completed with exit 0. The separate pre-existing local observation module is
preserved outside this publication set.
