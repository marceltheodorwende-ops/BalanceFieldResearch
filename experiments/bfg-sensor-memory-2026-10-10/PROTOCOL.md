# P70 — Sensor memory, observable closure and independent calibration

Active step, dependencies P65/P68/P69. Investigate an explicitly EXTRA common
first-order sensor response with response time theta>0 seconds. Do not infer
theta or manufacturer behavior from a fitted pendulum. Completion: derive the
extended state, observation/jet ranks, exact nonlinear force transformation and
canonical return/tangent compatibility; give passive nonidentifiability and
independent reference calibration construction; search whole active source;
run independent synthetic algebra/ODE/tangent/adverse-conditioning controls;
archive limitations and verify publication plus register/both ledgers.

Primary metadata evidence remains the pinned dataset README/process/schema
audited in P65, commit cbf82673641ecd65e902ad5c38a048387649a2a0. Fresh README
read must match blob baf8f1eb4760df7c08820d3431b2fb44e4d3ad99. No new measurements,
raw data, holdout, dataset archive, regression, development variant selection or
empirical workflow. P69 scores and 35 countercertificates remain unchanged.
Source metadata does not certify this response model, its initialization,
channel gains, independent time alignment or error budgets.

Sole math source Dynamic Order 8Oct2026, 144 pages, SHA256
1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba.
Use Part I22–23/62–64/73.1, II83–90 and Appendix A. Instrument memory is a
declared observation extension, not a new canonical BFG input or seed lift.

Predeclared controls: symbolic identities for memory compatibility, jet rank,
nonlinear acceleration/determinant, harmonic commutation and calibration
inverse; harmonic exact exponential vs augmented independent DOP853 for three
response times (.02,.1,.5 s) on 2 s; nonlinear conjugate-vs-augmented ODE for
three states using theta=.03,.12,.25, kappa=4,Gamma=.15 on 1 s; central-difference
return Jacobian vs variational conjugate Jacobian and state-dependent duration
including F DT. Synthetic parameters are ONLY control choices, no physical
calibration. Absolute endpoint tolerance2e-8, tangent2e-6, symbolic exact zero.
Check common-memory inconsistent initialization decay and explicit rank loss
at q=pi,w=0,theta=1/sqrt(kappa) when Gamma=0. Record adverse conditioning.

Stability notion: fixed true input, positive known theta, differences in sensor
memory decay exp(-t/theta); this is not joint plant or full BFG stability.
Robust inverse on a convex chart with ||DF||<=L and theta L<1 has gain bound
1/(1-theta L); no bound outside this domain. Calibration errors are bounded
complex transfer errors with real part at least r>0, imaginary magnitude <=B
and independently known nonzero angular frequency. Examine low real-part and
theta-to-zero differentiation sensitivity. No actual sensor uncertainty is
claimed. If genuine preparation/response/event calibration absent, close only
this interface investigation with a proved identification boundary and leave
physics open. No new package until publication and both ledgers verified.
