# Physical calibration and intervention closure audit

## Outcome

The mathematical representation can be completed as a candidate, but its
physical derivation is not established by the paper or current measurements.
The new observable is not yet a justified physical realization. This audit
closes the feasibility assessment of a fixed constant-retention candidate;
it does not claim to close the missing BFG-to-physics derivation.

## Constant observable: development feasibility

The construction H_p(f(y))=2^(-p)H_p(y) predicts a single retention factor
q=2^(-p) for every event if p is fixed. The scale C cancels from retention.
Thus one physically fixed energy calibration cannot reproduce arbitrary
condition- or state-dependent losses merely by choosing initial y.

We used all 1,364 previously published development pairs, no new observations
and no held-out files. Assuming only cleaned angle rounding of +/-0.0005 rad,
the admissible retention interval for measured absolute angles a,b is

    [ sin((b-epsilon)/2)^2 / sin((a+epsilon)/2)^2,
      sin((b+epsilon)/2)^2 / sin((a-epsilon)/2)^2 ].

The length and g cancel. For a,b>epsilon and a,b+epsilon<pi, potential energy
is monotone in absolute angle, giving these exact rounding bounds.
The global lower bound is 1.5158909135935055; global upper bound is
0.6176081126281858. Their intersection is empty.
Both conflicting witnesses occur in len3_cond2_1.csv, at input times
58.27 s and 54.97 s. Thus even a per-condition constant q does not exactly
match that recording under a rounding-only error model.
Some apparent energy increases exceed rounding alone; they may reflect sensor
offset, extrema processing, other measurement effects or unmodelled dynamics.
They are not established physical energy creation or a refutation of passive
damping. A complete sensor/annotation uncertainty model is missing.

Median measured retention across all pairs by damping condition:
air only 1.0000; small baffle 0.97724; large baffle 0.96190.
These pooled descriptive medians mix lengths and states. They are not matched
causal estimates or independent validation of an intervention map.

calibration_audit.py reproduces the interval audit using only the existing
derived development-pair file. Three controls verify zero-width calibration,
interval enclosure and invalid-angle rejection. No confidence intervals or
confirmatory decision are claimed.

## Exact continuous interpolation and intervention candidate

Let phi be the increasing scalar coordinate established in
NONLINEAR_OBSERVABLE.md, with phi(f(y))=phi(y)^2 and 0<phi(y)<1.
Let p>0 be fixed and introduce a nonnegative physical rate kappa(u).
For physical duration t>=0 define

    T_t^u(y)=phi^{-1}(phi(y)^{exp(kappa(u)*t/p)}).

For nonnegative t and rate, the powered coordinate stays within the range of
phi, so the inverse is defined. Direct substitution gives

    H_p(T_t^u(y))=exp(-kappa(u)*t)*H_p(y).

For fixed u, T_s^u composed with T_t^u equals T_{s+t}^u.
The original scalar BFG map is the particular time
t=p*log(2)/kappa(u), when kappa(u)>0.
At kappa=0 the interpolation is the identity.
A piecewise-constant intervention schedule composes these maps; accumulated
decay depends on the integral of kappa over physical time.

This is a mathematically consistent scalar flow and an explicit candidate
intervention parameterization. It is an extension/interpolation of the
canonical discrete model, not a physical clock or instrument supplied by
the original paper. General event durations do not equal one canonical step.
It also does not identify the complete carrier state or matrix interventions.

## What would physically justify this candidate

Required, not yet supplied:
1. Independently calibrated preparation and observable H_p, including why
   the inverse-log dependence represents measured energy. Parameters cannot
   be chosen solely to encode the target decay curve.
2. A physical relation from length, baffle geometry, medium and apparatus
   into kappa(u), justified independently of the evaluation targets.
3. An independently calibrated physical clock relating canonical events to
   seconds; event detection delay and annotations must be modelled.
4. A sensor and extrema uncertainty model adequate for apparent increases,
   with observables and state information consistently specified.
5. Closure/identifiability of the relevant BFG states, or explicit uncertainty
   over latent states. Angle and velocity do not uniquely determine all
   K,F,W,Y,P components without an additional construction.
6. An intervention contrast or constraint distinguishing this realization
   from the ordinary decay rival.

Fitting kappa to measured damping simply reproduces the physical rival in
new coordinates. It does not show physical damping emerges from BFG.
If all parameters and readouts can change freely by condition, empirical
universality becomes an unfalsifiable representation claim.

## Disposition and next authorized work

Do not open the reserved 30 recordings or call this a confirmatory realization.
Preserve both failed scalar energy mappings and the constructive interpolation.
Next developmental tasks: derive independently motivated calibration
constraints; audit richer angle/velocity carriers and their closure; examine
sensor metadata and uncertainty using primary sources; develop discriminating
intervention predictions. If no such constraints can be established, publish
the remaining requirement rather than assert that physical derivation is done.
