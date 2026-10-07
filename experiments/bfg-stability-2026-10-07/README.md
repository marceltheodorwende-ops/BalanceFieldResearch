# Robustness of the better nonlinear realizations

Question: are nominally good real-data forecasts insensitive to small declared disturbances? Result: no absolute robustness. Both the exact sine-flow BFG representation and its analytic phase approximation are strongly sensitive to hypothetical clock calibration changes over6.4s. No model is changed or refitted in this package.

PROTOCOL.md fixes scenarios and reporting rules before evaluation. STABILITY_PROOF.md proves conditional downward-equilibrium asymptotic stability, supplies a finite-horizon log-norm bound, and exhibits upright instability. The physical generator is additionally supplied; none of these claims derives pendulum forces from BFG alone.

15 real attempt-1 recordings, source EnzeXu/Damped_Pendulum_Dataset cbf82673641ecd65e902ad5c38a048387649a2a0, Xu et al., TMLR2026 https://openreview.net/forum?id=xvQYvYEGhj. Source downloader verifies pinned development files only. Calibration uses already published viscous fits on seconds0–30. Evaluation starts every0.1s in seconds30–60, horizons0.1,1.6,6.4s. No exclusions, refit or holdout access; reserved attempts2/3 remain sealed. All perturbations are deterministic sensitivity controls on real-data forecasts, not new measurements or confidence intervals.

11 scenarios per model/horizon: nominal and plus/minus initial angle0.002070796rad (illustrative half0.18-degree encoder division plus CSV rounding), initial velocity0.0005rad/s (rounding only), gravity coefficient1%, damping coefficient1%, clock duration1%. These are one-factor tests, not a certified joint error box. Scores are equal-record means of RMSE divided by target RMS; windows overlap and no significance claim is made. At6.4s each scenario has3540 forecast pairs.

| Sine-flow scenario at6.4s | Angle error | Velocity error |
|---|---:|---:|
|Nominal|0.088291|0.128745|
|Initial angle plus|0.089585|0.129471|
|Gravity coefficient plus1%|0.205493|0.221684|
|Damping coefficient plus1%|0.088661|0.128967|
|Clock duration plus1%|0.351789|0.360452|

Worst scenario among those tested is clock plus1% for both metrics and both models. The phase observable gives0.351338/0.360201 there versus nominal0.088297/0.128974: it inherits the same clock sensitivity. This is not evidence that the actual dataset clock is wrong by1%. It shows that simply replacing the readout or adding nonlinear terms cannot remove phase accumulation from uncertain physical time/frequency. Current timestamp metadata do not independently calibrate a1% uncertainty interval.

Basin certificate: all4500 nominal start states have low enough energy and lie in the downward well;4200 additionally have fitted b>0 and satisfy the asymptotic-attraction theorem. Recording len5_cond1_1.csv has fitted b=0 for300 states: the energy-well stability argument still applies but convergence is not certified. Do not label these states unstable or remove them. Certificate assumes the fitted generator is correct; it is not empirical validation of true parameters or forecast accuracy.

## Stabilization direction justified by this result

Keep the published exact nonlinear flow and phase observable as comparators. Prioritize independent clock/frequency calibration and explicit horizon-dependent error budgets, not extra force terms. The declared stress identifies a failure mode, not a fix or a universal guarantee. Updating the physical clock by fitting these validation errors would be new exploratory calibration and must be documented; it cannot be called independent stabilization. Any future restricted horizon or error threshold must be fixed before confirmation and cannot hide current failures. Absolute global stability is mathematically refuted by the upright equilibrium counterexample.

## Verification and reproduction

Two new controls independently verify the log-norm bound and upright eigenvalue. Re-run the prior three force-family integrator controls and four phase-observable controls as dependency verification. Numerical sine stepping is<=0.005s; the prior DOP853 and matrix-exponential6.4s controls verify that scale. Published SHA256SUMS covers package files, including all990 per-record/model/scenario/horizon rows and source/calibration hashes. Protocol is exploratory, not a confirmatory preregistration.

    python -m unittest -v test_stability.py
    python stress.py ../bfg-realization-development-2026-10-07/data ../pendulum-mechanical-identification-2026-10-07/results/models.csv results

Use numpy2.3.5/scipy1.17.0. A single bounded GitHub reproduction runs source verification, nine controls and stress analysis with max45minutes. Remaining measurement accuracy, joint disturbance coverage, genuine coupling selection and untouched confirmation are explicit limitations.
