# Clock-only error budgets and independent-calibration obstruction

## Conditional certified bound

For the supplied sine pendulum generator theta'=w,w'=-a sin(theta)-b w, assume a>0,b>=0 and forward physical time. Normalized energy E=w²/2+a(1-cos(theta)) satisfies E'=-b w²<=0. Therefore for a trajectory starting at(theta0,w0), speed obeys |w(t)|<=sqrt(2E0). Also sin²(theta)<=2(1-cos(theta)), hence |sin(theta(t))|<=min(1,sqrt(2E0/a)). Set

    S=sqrt(2E0)
    Q=a*min(1,sqrt(2E0/a))+b*S.

Then |w'|<=Q. If the same trajectory is read at h and h(1+delta), with |delta|<=epsilon<=1, both times are forward. Integrating over their time difference gives

    |theta(h(1+delta))-theta(h)| <= S*epsilon*h
    |w(h(1+delta))-w(h)| <= Q*epsilon*h.

This is an exact analytic clock-only bound for this additionally supplied mechanical model, including rotation and b=0. It is not a new BFG force derivation. For a batch, take RMS of the per-input bounds. By the triangle inequality, target RMSE with a clock perturbation is at most nominal target RMSE plus this model-to-model bound. Initial state, parameters and model error are held fixed; this is not a joint uncertainty guarantee. Numerical evaluations require solver-error allowance.

## Real-data derived budgets

Only15 real attempt-1 recordings from EnzeXu/Damped_Pendulum_Dataset, commit cbf82673641ecd65e902ad5c38a048387649a2a0, Xu et al. TMLR2026 https://openreview.net/forum?id=xvQYvYEGhj. Existing fitted sine/viscous coefficients on seconds0-30; starts every0.1s in seconds30-60. All15 included, no new data downloaded, no reserved attempts accessed. These are derived analytic budgets on real states, not new forecasting experiments or independent confirmation.

Before calculation, the declared diagnostic budgets are an additional angle normalized RMSE<=0.05 per recording, and separately a maximum added angle error<=0.01rad per input. They are illustrative engineering allowances, not retrospectively selected success criteria for confirmation. Target RMS from development data is only a diagnostic normalization; deployment or confirmation must fix its scale in advance. The code computes conservative sufficient tolerances without changing or refitting the predictor.

| Horizon | Common clock tolerance for extra angle NRMSE<=0.05 | Common tolerance for maximum extra angle<=0.01rad |
|---|---:|---:|
|0.1s|5.569%|2.435%|
|1.6s|0.3354%|0.1522%|
|6.4s|0.07255%|0.03804%|

Each common tolerance is the minimum across all15 recordings, not an average masking a weak record. At1% clock perturbation, equal-record mean normalized angle bound is0.501 at6.4s. This is a bound on additional model discrepancy, not the prior observed total forecast error0.352. It is conservative and need not be attained. No assertion is made that the true instrument clock has1% uncertainty or satisfies these tolerances.

## Why timestamp spacing alone cannot calibrate seconds independently

Let physical time t=c*tau, c>0, and observed angular velocity u=dtheta/dtau=c*w. Then the same trajectory in recorded time obeys

    d²theta/dtau² + (c*b)*dtheta/dtau + (c²*a)*sin(theta)=0.

Thus angle and velocity derived using the same recorded clock identify effective a_obs=c²*a,b_obs=c*b; they do not separately identify c,a,b. Uniform0.01 spacing in CSV proves a recorded-time grid, not traceable physical clock accuracy. If velocity were independently calibrated in physical seconds it could break this ambiguity, but independence must be established from primary instrument/processing documentation, not assumed. This is a conditional identifiability obstruction for the currently shared timing calibration, not a universal BFG impossibility theorem.

The BFG event clock N(Y) supplies event ordering. An independent seconds-per-event coupling still needs evidence. Rescaling its declared step together with mechanical coefficients does not create independent physical information.

## Verified controls and next action

Three controls passed: both state bounds against independent adaptive DOP853 for rest, libration, near-upright and rotational cases with/without damping; exact time-rescaling equivalence; invalid backward-time uncertainty rejected. Synthetic inputs are mathematics/code controls only. Bound derivation is the proof; tests corroborate implementation.

Use numpy2.3.5/scipy1.17.0:

    python -m unittest -v test_budget.py
    python budget.py ../bfg-realization-development-2026-10-07/data ../pendulum-mechanical-identification-2026-10-07/results/models.csv results

SHA256SUMS covers published code and derived per-record budgets. Summary preserves source/calibration hashes. No new empirical GitHub workflow is launched for this short analytic checkpoint; previous stress reproduction37692412238 remains verified.

Next: seek primary-source clock accuracy and independently justified frequency calibration; set an explicit operational horizon/error allowance before confirmatory evaluation. These bounds provide a defensible requirement, not a completed independent calibration or guaranteed improved measured predictions. Preserve long-horizon failures, closed holdout and strong mechanical rivals.
