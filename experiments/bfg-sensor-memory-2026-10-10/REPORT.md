# P70 — Result and reproduction, 10 October 2026

This package closes one sensor-memory/interface investigation after P69.
It supplies an exact conditional nonlinear extension, a structural passive
identification counterexample, and concrete independently referenced calibration
formulas. It does NOT supply a measured PS-3220 response or a selected physical
force. The parent instrument/preparation/event-clock problem remains open.

## Newly proved result

For the declared first-order response theta x'=Q-x,theta y'=W-y,Q'=W,
the four-state output projection is generally not a closed factor. Known-theta
ideal output jets have rank4; compatible initialization preserves x'=y, and
incompatible history creates exactly the exp(-t/theta) defect transient.
Therefore common filtering is neither a general cure for P69's kinematic
countercertificates nor automatically a two-state physical realization.

For an already declared rank-two field F=(v,f), T_theta=z+theta F yields an
exact candidate plant/measurement pair where det DT=1+theta f_v-theta^2 f_q.
The complete acceleration, nonlinear inverse, exact canonical endpoint and
clock-gradient tangent term are derived. The P68 sine/cos-half law changes
under this transformation; a fixed-law nonpreservation counterexample is proved.
Pullback Lyapunov energy survives on the conjugate chart, not as an independently
calibrated energy of the actual apparatus. Singular charts and limited inverse
sensitivity domains are explicit.

A known harmonic plant admits the same entire continuous passive output for
EVERY positive response time, with different true initial preparations. This
counterexample does not rely on finite sampling/noise and does not assert
universal nonidentifiability of all restricted nonlinear apparatus models.
An independently known nonstationary true initial angle breaks this particular
ambiguity by theta=(Q0-q0)/v0; equilibrium cannot do so. An independent timed,
phase-known harmonic reference identifies response time, gain and offset for
the stipulated delay-free first-order channel. Unknown delay restores one-tone
ambiguity; commensurate tones retain delay aliases. Explicit error bounds and
ill-conditioning are included. No synthetic reference is called a real measurement.

## Actual independent controls

- Eleven symbolic identities passed. Initial control compared unsimplified
  symbolic matrices by syntactic equality and failed. It was corrected to
  entrywise algebraic simplification; the original failed control is documented
  here. No theorem, physical model, frozen protocol or threshold was changed.
- Three harmonic exact-exponential vs augmented DOP853 controls: maximum
  observed-state error1.80e-12, true-state error2.90e-12. Inconsistent-memory
  defect control max2.37e-9 under predeclared2e-8 tolerance.
- Three nonlinear augmented-vs-base flow controls: endpoint max5.73e-12;
  independent central-difference return tangent max2.04e-10 under2e-6.
  Omitting F DC produces errors .04952,.06854,.18562. The synthetic duration
  used here checks the general identity; it is NOT a measured/canonical
  event interval and does not numerically replace P68's actual canonical clock.
- Independent prescribed-reference ODE and harmonic coefficient extraction at
  three frequencies recover response/gain/offset to <=3.60e-14.
  Compatible-history convolution quadrature discrepancy4.45e-16;
  independent four-state jet determinant discrepancy1.29e-9.
- Independent known-preparation inverse controls recover response time to
  <=1.12e-16; equilibrium is explicitly uninformative.
- 300 bounded complex perturbations satisfy the derived sensitivity bounds.
  Negative robustness retained: with Re H about1e-6, an absolute transfer
  perturbation bounded2.50e-7 gives response-time error up to3.183s in the
  synthetic10s case. Near a singular conservative chart, condition number
  grows from1243 to12,499,993. These are controls, not uncertainty of the device.

Both scripts completed successfully. Python3.12.14, NumPy2.3.5, SciPy1.17.0,
SymPy1.14.0. py_compile passed. Protocol SHA256 remains
b298843fa9952c7c6543b6d31e48048bca7dafc3392f5724eacb45170f153c00.
Reproduce: `python check.py`, then `python verify.py` in this directory.
They use no dataset/network, and overwrite only their local control JSONs.
Synthetic code controls cannot verify physical preparation, sensor response,
SI uncertainty or manufacturer behavior.

## Source and unfinished physics

Active paper SHA256 freshly verified. Full-paper accompanying search and exact
section/equation references are in DERIVATION.md. Fresh pinned dataset README,
processor, schema and length metadata blobs match P65 evidence; metadata read
alone does not execute the unrestricted all-files processor. Fresh workflow
inspection found zero active runs; no empirical experiment or workflow started.
No pendulum recordings, reserved holdout or EEG subjects were opened this step.

P69's positive/negative development results and 35 family-wide countercertificates
remain unchanged. A filter correction must have its own independently justified
law/history/uncertainty; P69's latent-state curvature envelope cannot be reused
by relabeling filtered channels. No new physical calibration is claimed.

Next necessary dependency: independent preparation/reference/response evidence,
or a physically justified finite-dimensional instrument family and explicit
identifiable calibration/preparation design, including channel alignment and
bounded uncertainty. A fitted response time alone cannot satisfy this obligation.
Physical angle/force selection, seconds per canonical event, inertia/energy
scale, common preparation and actual interventions remain OPEN. Full-persistence
tensor replication transfers the same factor/interface and supplies no new
measurement; no physical fractality or automatic emergence is claimed.
