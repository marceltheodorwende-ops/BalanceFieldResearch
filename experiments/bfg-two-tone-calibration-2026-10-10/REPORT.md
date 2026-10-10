# P71 — Two-reference calibration result, 10 October 2026

This completes P70's next mathematical calibration-design dependency within an
explicit first-order/gain/delay family. It does not complete physical calibration
of the actual pendulum apparatus or BFG force selection.

Two distinct known SI reference frequencies uniquely identify nonnegative
response time and positive gain from their magnitude ratio under this response
family. Delay is determined modulo rational-frequency aliases. An irrational
ratio removes exact aliases but has distant arbitrarily close phase alternatives
under finite error. A declared bounded delay domain yields an explicit robust
inverse. Error intervals retain zero response time, infeasible ratios and
infinite upper bounds rather than forcing a convenient positive estimate.

The response family itself is not established by two tones: a stable causal
rival with an extra sixth-order branch matches DC and both tones exactly and
predicts a different third-tone response. Its extra branch has finite state;
an exact pure delay still requires history. Thus primary apparatus evidence and
independent model checks are essential, not optional extra fit parameters.

Known channel response/gain/delay supplies explicit ideal latent angle,
velocity and acceleration reconstruction. This is mathematically connected to
the nonlinear factor, including conditional delayed projection and complete
clock-gradient tangent. It does not make rounded data differentiable, create
a BFG event label, supply inertia/energy, or select sine over nonlinear rivals.
An unrestricted small high-frequency output error can produce arbitrarily large
reconstructed force error. Bounded bandwidth/history and a real uncertainty
budget are necessary before development force analysis.

Actual checks completed:

- Eight exact symbolic identities passed; four independent delayed-input
  reference cases (including zero and10s response) recovered parameters with
  maximum error1.069e-8 under frozen2e-7 tolerance. These cases are synthetic.
- 300 bounded amplitude perturbations retained the true response time in the
  derived uncertainty outer interval. Tested widths up to .13592s in the10s
  case; explicit separate cases retain infinite upper bound and theta=0.
  These are feasible outer bounds, not complete feasibility or confidence levels.
- Independent70-digit inversion error <=2.30e-68; 300 bounded-delay sensitivity
  checks passed. Near-equal frequencies increase d(theta²)/dR from .05326 to
  2796.22. The long-delay irrational near-alias has separation87084.948s and
  corrected-phase difference about .000160277; this is a synthetic ambiguity,
  not measured latency.
- Stable rival DC/two-tone discrepancy0, third-tone discrepancy .00387470.
  Nonlinear delayed-output force reconstruction vs independent true-velocity
  central differences: max2.030e-10 under2e-5 tolerance.
- Independent nonlinear delayed-factor endpoint error1.50e-15, tangent error
  2.34e-11; omitting F DC gives error .05162. Its synthetic state-dependent
  duration checks the general formula, not a measured/canonical BFG event.
- Unrestricted differentiation counterexample retained: output error about1e-5
  can yield a second-derivative force term9230.86 in the synthetic chosen units.
  It proves the missing smoothness/bandwidth obligation, not a device defect.

Both scripts exited successfully, protocol unchanged (SHA256
72cad34cab07f9777f03343ed0e1c7f02ffcbb261389b417ef7e19b3487c0c44).
Reproduce locally with `python check.py` then `python verify.py`; no dataset,
network or physical measurement required. py_compile passed. Symbolic and
synthetic tests check the derivation/implementation; they do not certify actual
instrument behavior. No failed empirical variant was discarded or repaired.

Active PDF hash was freshly checked. Whole-paper accompanying mathematical
search, exact references, other-level mapping, assumptions and all proof scopes
are in DERIVATION.md. Fresh four pinned dataset metadata blobs match P65/P70;
the inspected README/processor/schema does not supply the proposed independent
two-tone calibration records or complete response/delay/history/error model.
No source processor was executed; no raw/development/holdout CSVs were opened.
No empirical fit, workflow, automation, main merge or original-paper change.

Next necessary open dependency: justify a bounded instrument complexity,
history, delay and uncertainty family from primary apparatus evidence; specify
independent calibration/preparation observations and an out-of-family reference
check before any new development fit. P69's failures and prior results remain
unchanged. Physical angle/force selection, SI canonical-event clock,
inertia/energy scale, shared preparation and real interventions remain OPEN.
Full-persistence replication transfers the same interface and adds no independent
measurements or physical fractality.
