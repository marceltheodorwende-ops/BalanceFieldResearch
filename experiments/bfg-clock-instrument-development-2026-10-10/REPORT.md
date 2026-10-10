# P69 — Direct sensor bridge fails its narrow certificate; force choice remains open

Completed investigation, not physical BFG confirmation. The protocol was fixed
before this new pass over the fifteen permitted attempt-1 records, all previously
used development data. Exactly one local finite experiment; no new GitHub
empirical workflow. The 30 reserved files were not downloaded or opened.

## New checked result and its exact reach
The combined hypothesis identifies sensor angle/velocity directly with Q,W,
uses exact reported sample times, assumes total errors are only printed rounding
(.0005 rad and .0005 rad/s), and imposes the P68 cosine-damping sine equation
with shared kappa(L)=9.799 L/(L^2+lambda),lambda in[0,.02] and Gamma0<2sqrt(kappa).
Thirty-five of1,785 half-second kinematic windows violate the conservative bound
even for the ENTIRE parameter family, in10/15 records. Every window has the
required common energy corridor. Thus fitting another allowed lambda/rate
cannot rescue this narrow direct sensor bridge. This refutes the combined
hypothesis, not the sine force separately, not actual sensor accuracy, and not
all BFG carriers/observables/clocks/couplings. Missing sensor response, filtering,
timing, gain/offset or uncertainty need independent justification; none is
invented as the proven cause. Five records with no violations do not establish
their calibration or full nonlinear closure.

All35 countercertificates were independently recomputed at60 decimal digits
from the printed samples; minimum excess over the bound1.33198e-5 rad.
Double independent calculations over all1,785 windows differ by<=1.56e-15.
Maximum residual/bound ratio1.34324. Evidence family_kinematic.csv and the
35-row family_violations.csv,verification.json plus the proof in DERIVATION.md.
At their particular fitted parameters the clock/viscous/mixed models have
500/500/497 violating windows, preserved in kinematic.csv. These fitted-model
counts are distinct from the stronger parameter-family exclusion.

One clock_cos fit (len1_cond3_1) has Gamma0=0. That is a legitimate numerical
boundary optimum retained in the archive, but corresponds to inherited delta=0
and loses P66 carrier rank. It cannot be reported as a regular P68 realization.
The old zero-rate and bad developmental results are not deleted or regularized
away with an invented positive floor.

## Developmental force comparison and longer fixed-parameter horizons
Shared lambda fits: clock_cos0.0030507277604,viscous0.0030510608450,
mixed_drag0.0030259571448 m^2. These are mechanically assumed inertia ratios,
not measured inertias and not internal BFG parameters. Their first30s normalized
weak losses are0.00434571,0.00434873,0.00424839. Temporal weak losses are
0.00277164,0.00277208,0.00274246. Small differences do not select the clock
law. The normalized clock/viscous damping designs have condition331.59–2467.75;
relative column differences0.250%–1.461%. The finite-amplitude terms are weakly
distinguishable here; no independently calibrated uncertainty exists.

For a single autonomous trajectory starting at30s, the29.99s cumulative metrics
(medians across records, not scores from rolling state-reset prediction) are:

| Model | Fitted coefficients | Angle RMSE/persistence | Velocity RMSE/persistence | Angle/velocity wins vs viscous |
|---|---:|---:|---:|---:|
| P68 clock_cos |16|0.12033|0.13500|7/15,7/15|
| Nonlinear viscous sine |16|0.11903|0.13676|reference|
| Nonlinear mixed drag sine |31|0.12444|0.11190|9/15,9/15|

Individual long-horizon angle RMSE ranges0.00536–0.18808 rad for clock_cos,
0.00533–0.18435 for viscous,0.00966–0.18997 for mixed_drag; velocity ranges
0.04741–0.90422,0.04734–0.92730,0.06803–0.90398 rad/s. Per-record/horizon
scores and prediction nodes are published, including horizons .1,.5,1,2,5,10,20.
No uniform or absolute prediction-stability guarantee follows. Mixed drag adds
15 coefficients and wins some comparisons; no single average proves superiority.
The clock law does not win across records/channels. Forecasts are diagnostic
since the stated instrument identification failed; they are not force or clock
calibration certificates. All are reused exploratory development comparisons.

This differs from the older rolling .1s shared-calibration task; its historical
lambda0.0022888769594 and scores remain unchanged and are not compared as if
the protocol were the same. No observations from the reserved attempts were used.

## Independent controls, perturbation limits and correction preserved
Three independent synthetic DOP853/RK4/weak-identity controls,three constrained
least-squares face controls,an adversarial rounding/trapezoid bound and an invisible
weak residual passed. The energy identity was also symbolically checked.
All45 real forecast paths have energy corridors; step refinement .005→.0025
gives max discrepancies5.13e-7 rad and3.13e-6 rad/s, within frozen1e-5/1e-4.
No integration repair needed. Independent DOP853 forecasts for the fixed first
record across all3 models differ by<=3.08e-8 rad and1.75e-7 rad/s.
This verifies numerical calculations, not real physical prediction uncertainty.

Coarsening the calibration quadrature from .01 to .02 at the same fitted lambda
changes normalized loss by about0.5%; max gamma change0.008992 s^-1,beta change
0.000952. These perturbations and near-collinear designs are retained, not
hidden by picking one favorable mean. Profile ranges within1% loss are sampled
development sensitivity diagnostics, not confidence intervals or exact intervals.

Review corrected an overbroad draft reading of extra_angle_allowance: the number
is an additive budget deficit at a FIXED energy/curvature envelope. It is not a
minimum physical device uncertainty when that initial uncertainty itself changes
the envelope. The original broader draft claim is withdrawn here; the derived
rounding-only exclusion, protocol, fits, forecasts and decision rules are unchanged.
No after-result model term, time transform or threshold was fitted to rescue P68.

## Status and next necessary dependency
Completed: conditional proof, direct-channel countercertificates, shared
development fit/rivals, long-horizon and numerical checks, archived failures.
Physical bridge status: FAILED in the stated direct,rounding-only clock-family
form; no physically calibrated BFG representation established. General physical
force law,angle/SI event clock,inertia,preparation,shared parameter selection and
interventions remain OPEN. A tensor lift preserves the same test on pullback;
replication is not new instrument evidence and does not resolve the failure.

Next necessary solvable dependency is an independently justified bounded sensor
response/time-alignment/uncertainty model and preparation/event correspondence.
Derive its rank and parameter identifiability before reusing development data;
preserve this failure and strong rivals. Do not open a holdout, silently redefine
sensor time or declare a different physical question solved.

## Reproduction and provenance
Python3.12.14,NumPy2.3.5,SciPy1.17.0,SymPy1.14.0 and mpmath for60-digit controls.
Run with the already authorized fifteen pinned attempt-1 files only:

```sh
python check.py
python analysis.py ../bfg-instrument-audit-2026-10-09/data ../bfg-instrument-audit-2026-10-09/source_manifest.json
python verify.py ../bfg-instrument-audit-2026-10-09/data
```

Code refuses mixed CSV directories before opening measurements and verifies
source blobs/SHA256; verify.py also rechecks the unchanged protocol hash.
Data provenance is in results.json, source commit
cbf82673641ecd65e902ad5c38a048387649a2a0. Original dataset is Apache2.0;
source attribution/license remain in the P65 provenance package. Only derived
results/predictions/certificates are published here; no raw measurements copied.
No external contact,paid service,new automation,main merge or original-paper edit.
