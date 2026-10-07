# Frozen protocol: real damped-pendulum energy transitions

Status: protocol prepared before measurement CSV contents or holdout were
opened. No empirical result yet. Implementation must pass code controls
before evaluating the holdout. Date: 2026-10-07.

## Question and additional hypotheses

Does the paper's scalar map predict the energy at the next pendulum extremum
better than physical decay models? This tests an added bridge, not an existing
physical prediction of the paper. Hypotheses: y=E/s, one BFG update equals one
transition between consecutive absolute-angle extrema, and the scalar branch
f(y)=2y^2/((1+y)^2(1+y^2)) describes this transition. Each measured input resets
y; predicted physical energy is s*f(E/s). Domain: 0<y<1. Neither the bridge nor
the event clock is supplied by the paper.

The conditional derivative theorem in the preceding EEG mathematical
assessment motivates this diagnostic. It does not assert that these
measurements obey purely viscous damping.

## Primary source and immutable data

Enze Xu, Damped_Pendulum_Dataset:
https://github.com/EnzeXu/Damped_Pendulum_Dataset
Source commit cbf82673641ecd65e902ad5c38a048387649a2a0.
Xu et al., Identifying Invariant Physical Dynamics Across Multiple
Environments, TMLR (2026), https://openreview.net/forum?id=xvQYvYEGhj.
Retain upstream Apache-2.0 license and attribution when distributing data.

45 actual sensor recordings: five lengths, three damping conditions and
three attempts. PASCO rotary sensor; cleaned_data/len{1..5}_cond{1..3}_{1..3}.csv.
Use pinned cleaned files, existing is_peak annotations, without recomputing
peaks. Record upstream Git blob hashes; verify downloaded bytes using the
Git blob SHA1 construction and additionally publish SHA256. Keep raw source
bytes locally/Actions artifact if license verified; publish derived pairs and
provenance. Do not read measurement CSVs until this protocol is committed.

## Split and preparation

Attempt 1 of each of 15 length/condition cells is development (15 recordings).
Attempts 2 and 3 are untouched holdout (30 recordings). This tests repeated
measurements of the same apparatus/conditions, not unseen apparatus.

Lengths: 0.236,0.330,0.426,0.518,0.607 m. Use g=9.799 m/s^2.
At annotated extrema define E=g*L*(1-cos(theta)), potential energy per unit
mass in J/kg. This assumes the angular extremum approximates zero velocity;
publish measured angular_velocity there as a diagnostic. No energy inference
from uncalibrated brightness or synthetic trajectories.

Take consecutive annotated extrema within a recording. Eligible pairs have
finite times, angles and velocities, strictly positive dt, alternating angle
signs, and both absolute angles >=0.01 radians (ten cleaned rounding units).
Do not bridge rejected pairs. Minimum five eligible pairs per recording;
otherwise exclude that recording with its reason. Preserve all eligible
pairs including nonmonotone energy. Report interval and peak velocity
diagnostics, excluded counts and any schema failures.

Set s=1.1*maximum development input/target peak energy over eligible pairs.
No holdout refitting. Outside BFG domain, report terminal/invalid coverage
explicitly. Primary paired comparison uses the intersection of predictions;
also report every-model coverage and a sensitivity that assigns BFG invalid
predictions the persistence prediction. Do not claim predictive success if
BFG coverage is below 95%.

## Frozen comparators

Persistence: E_next=E.
Per-cell exponential physical decay: E_next=E*exp(-k*dt), k>=0. Fit k using
development only by bounded scalar minimization of squared energy error over
[0,100] s^-1, include endpoints and choose the minimum; no holdout tuning.
Per-cell affine energy transition: E_next=max(0,a*E+b), fit unconstrained
ordinary least squares on development pairs with intercept.
Same development split, preparation and eligible comparisons for all models.
No model selected using held-out performance.

## Outcomes and uncertainty

For each recording compute relative L2 error:
sqrt(sum(pred-target)^2 / sum(target^2)).
Average the two held-out attempt scores within each cell; average over cells.
Paired differences are BFG minus comparator (negative is better).
Use 10,000 bootstrap draws of the 15 cells, random seed 20261007, percentile
95% intervals. Shared apparatus makes these descriptive conditional intervals,
not population-level independent experimental replications. Report actual
sample counts and cells lost to exclusions.

Primary success requires BFG coverage >=95% and the upper paired 95% interval
below zero against all three comparators. Intervals are exploratory, unadjusted.
Secondary analysis: same loss and coverage on pairs whose two angles are
<=0.2 radians and >=0.01 radians; require five pairs per recording.
Report E_next/E and dt descriptive distributions in that subset to connect
the mathematical restriction to finite observed amplitudes. Do not infer an
exact asymptotic derivative from finite rounded measurements.

## Reproducibility and limits

Publish implementation, meaningful parser/model controls, environment,
provenance and checksums, exclusions, development parameters, pair and
record/cell tables, plots, summary and positive or negative report.
Synthetic cases are code controls only. Runtime limit 45 minutes; at most
one empirical experiment active. No merge into main or paper edits.

Measurement rounding, annotation processing, potential-only peak energy,
nonviscous friction, event sampling and repeated-condition holdout constrain
interpretation. Failure rejects only the specified scalar linear energy
bridge on this dataset. Revised bridges require newly independent data.
Scientific changes after reading holdout must be labeled post-hoc and cannot
be presented as this protocol's confirmation.
