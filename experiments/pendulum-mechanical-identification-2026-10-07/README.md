# Development-only mechanical identification checkpoint

Status: local analysis completed; remote reproduction must be checked.
Destination: experiment/real-pendulum-decay-2026-10-07. No main changes.

15 real attempt-1 recordings; attempts 2 and 3 remain sealed.
Primary source: EnzeXu/Damped_Pendulum_Dataset at
cbf82673641ecd65e902ad5c38a048387649a2a0.
See the preceding development audit's source_manifest.json and Apache license.
These are strong mechanical rivals and calibration diagnostics, not BFG success.

## Model and identifiability

Assume theta_dot=w and
w_dot=-a*sin(theta)-b*w-c*abs(w)*w-d*sign(w),
with nonnegative coefficients.
Mechanically a=mg*ell/I, b=b_torque/I, c=c_torque/I, d=tau_c/I.
Multiplying m,I,b_torque,c_torque,tau_c by a common positive factor leaves
all angle/velocity trajectories unchanged. Therefore those trajectories alone
cannot determine absolute mass, inertia, torque or energy. Conditional effective
ratios can be fitted. They are not identified BFG operators.

Compare gravity-only, gravity+viscous, gravity+quadratic, gravity+dry friction
and all terms together. Fit by nonnegative least squares on trapezoidal
integral balances over nonoverlapping 0.1-second blocks in 0<=t<30.
Column normalization prevents scale disparities in fitting.
Integral fitting avoids directly differentiating rounded angular velocity.
This uses observations inside training blocks only.

Evaluate on 30<=t<60 within those same development recordings.
This internal temporal split is exploratory, not the untouched confirmation set.
Forecast theta and w with RK4 from the measured block-start state only,
without future measured features; compare predicted endpoint velocity.
20 integration substeps per 0.1 second; 40 substeps provide a sensitivity check.

Score per recording RMSE(w_pred-w_next) divided by persistence's RMSE of
the velocity increment. Average 15 recording ratios equally.
A value below one improves on velocity persistence. Denominator varies by
recording; this is not the ratio of pooled errors or a confidence interval.

| Rival | Mean relative increment RMSE |
|---|---:|
| Velocity persistence | 1.000000 |
| Gravity only | 0.255719 |
| Viscous | 0.255082 |
| Quadratic | 0.253407 |
| Dry friction | 0.255719 |
| Mixed | 0.253407 |

Quadratic and mixed perform equally: mixed fitting selected only the
quadratic drag term alongside gravity. Dry-friction coefficients were zero
for every recording in these fits. This does not prove absence of dry
friction; weak identification, annotation/measurement effects and the chosen
fitting objective must be considered.
Most short-horizon predictive improvement is already explained by gravity.
The small differences between damping rivals are not established superiority.

Scaled design condition number reaches 38.57 for the mixed model.
Maximum 20-vs-40-substep velocity difference: 5.2631e-8 rad/s.
Four controls passed: free motion, analytic viscous velocity decay, exact
coefficient recovery and constant-velocity integral calculation.
Synthetic inputs are implementation controls only.

## Limits and next work

No independent physical inertia/drag calibration, sensor-error estimate,
causal intervention claim, new holdout test or BFG-derived force law is claimed.
The assumed theta_dot=w and torque balance need measurement-model checks;
these fits can be biased by sensor offset, rounding and correlated noise.
The internal validation has the same apparatus and recording as training.
All labels, clock and assumptions remain additional physical hypotheses.
Coefficient ratios and residual structure, not good scores alone, constrain
a future carrier/projection construction.

Next package: inspect sensor/apparatus primary metadata, offset and measurement
consistency; audit sensitivity to fitting window and integration horizon;
seek shared cross-condition constraints without tuning the reserved holdout.
Keep publication on this branch with a research-ledger checkpoint every package.

## Reproduce

Python 3.12, NumPy 2.3.5, SciPy 1.17.0.

    python -m unittest -v test_identify.py
    python identify.py ../bfg-realization-development-2026-10-07/data results

First obtain only development source files using the preceding audit's
fetch_development.py, whose filename allowlist and Git blob checks are pinned.
Derived predictions are published compressed in results/predictions.csv.gz.
Models, provenance, summary and code checksums accompany them.

