# Shared calibration and hierarchical BFG clock

Exploratory real-data checkpoint, 15 attempt-1 recordings. No confirmation.
This package constrains the calibrated movement representation rather than
claiming its mechanical coefficients emerge from BFG.

## A shared physically motivated frequency hypothesis

Assume an identical point bob at distance L, plus constant pivot inertia I0.
Then I=m*L^2+I0 and the gravity coefficient is

    a(L)=m*g*L/I = g*L/(L^2+lambda), lambda=I0/m.

This derives a cross-length relation conditional on that apparatus hypothesis.
The dataset does not independently establish identical bob mass, COM or I0.
A point-mass model is lambda=0. Absolute I0 and m remain unidentifiable
from their ratio alone.

Fit lambda on development seconds0–30 with nonnegative per-record viscous
rates, using the previously declared integral balances. Minimize the equally
weighted mean record-normalized training residual over lambda in [0,0.02] m^2,
checking both endpoints. Do not fit on temporal validation or reserved files.
Evaluate the BFG motion readout on seconds30–60 with fixed 0.1-second horizon.
The original unconstrained frequency fit is a comparator.
All parameters, alternatives and comparisons are exploratory.

## Result

One shared lambda=0.0022888769594424643 m^2 replaces 15 free gravity coefficients.
Condition-specific alternatives give 0.001985,0.002346,0.002528 m^2.
Neither is an independently measured pivot inertia.

| Calibration | Effective fitted coefficients | Angle error / persistence | Velocity error / persistence |
|---|---:|---:|---:|
| Point mass | 15 | 0.082917 | 0.257336 |
| Shared inertia ratio | 16 | 0.082510 | 0.255771 |
| Condition-specific inertia ratios | 18 | 0.082518 | 0.255834 |
| Free frequency per recording | 30 | 0.082509 | 0.255849 |

Counts include 15 viscous rates and respectively0,1,3 or15 frequency quantities;
fixed g and readout scales are additional supplied constants.
The shared relation nearly preserves the developmental scores with fewer
fitted coefficients. Small numerical differences are not evidence of statistical
superiority. Same-apparatus temporal validation does not confirm the hypothesis.

Three controls cover point-mass scaling, independent rotor torque calculation
and recovery of a known shared ratio. Synthetic cases are controls only.

## Relation to BFG time

BFG supplies the internal event identity N(f(Y))=N(Y)+1.
Measured seconds and g,L constrain a physical readout; the relation above
does not derive a unit of seconds from the dimensionless internal recursion.
Changing the assigned seconds/event and adjusting physical generator parameters
can preserve the internal event predictions. Independent clock calibration
remains necessary. This is an explicit conditional constraint, not a unique
BFG derivation of gravity.

## Hierarchy / fractal hypothesis requested by the owner

A precise first construction is a dyadic hierarchy of the scalar canonical map:

    U_j = U^(2^j), j=0,1,2,...
    U_(j+1) = U_j composed with U_j,
    N(U_j(Y)) = N(Y)+2^j.

In the scalar phi coordinate,
phi(U_j(Y))=phi(Y)^(2^(2^j)).
A coarse level spans 2^j calibrated fine events. All levels commute because
they are powers of the same autonomous transition. This is exact temporal
self-similarity and consistency, not evidence of a fractal physical object
or a noninteger fractal dimension.

For the calibrated oscillator projection, every level obeys
Pi(U_j(Xi))=exp(M*dt*2^j)*Pi(Xi).
Thus hierarchical BFG representations can describe the same physical flow
at multiple event scales without changing parameters at each level.
Longer-horizon development predictions should test this constraint.

Do not treat separate matrix blocks as independent canonical BFG systems
without checking global formation-dependent weights, carrier changes and
couplings. A matrix hierarchy is a further construction.
Actual fractal physical claims require a specified scale law, domain,
measured evidence and comparisons against ordinary multiscale dynamics.

## Reproduce and next step

    PYTHONPATH=../pendulum-mechanical-identification-2026-10-07:../bfg-pendulum-motion-2026-10-07 python -m unittest -v test_shared.py
    python shared_calibration.py ../bfg-realization-development-2026-10-07/data ../pendulum-mechanical-identification-2026-10-07/results/models.csv results

Pinned NumPy2.3.5/SciPy1.17.0, primary dataset commit
cbf82673641ecd65e902ad5c38a048387649a2a0.
Next: evaluate one fixed hierarchical realization across longer dyadic
horizons with measurement uncertainty, preserve failures, and develop matrix
coupling constraints. Reserved attempts2/3 remain sealed.


Owner clarification: fractal methods are optional and should be used only when
physically or mathematically justified. No empirical fractal model is adopted
for the pendulum here. The dyadic result is ordinary temporal consistency; it
does not establish noninteger scaling or warrant extra fitted fractal parameters.
