# Exploratory BFG realization dossier, version 1

## Status and evidence boundary

Development-only feasibility audit, not a confirmatory realization.
The existing architecture is evaluated without replacing its ambient analysis.
Paper source: 76d9e87b4275ec41b3dcd84434e2ee3791a8d076,
especially docs/MODEL.md and docs/CLAIM_STATUS.md.
The scalar energy preparation is an additional hypothesis. It is not derived
by identifying a physical energy with an internal load merely because both
are positive. A fully BFG-derived physical realization is currently unresolved.

## Typed construction that a realization must provide

Let X be physical states, D be measured records, S be admissible complete
BFG states modulo simultaneous unitary transformations, and U:S->S plus
named terminals the canonical update. A measurement model M:X->D, preparation
R:D->S, physical projection Pi:S->X, clock tau and intervention instruments
I_u must be declared. The intended compatibility is
Pi(U(xi))=Phi_u^tau(xi)(Pi(xi)), with a correctly specified physical evolution
Phi_u and input u. This formula is an obligation, not a proved fact.

For a discrete autonomous projected model, closure demands that any two xi
with Pi(xi1)=Pi(xi2) have the same projected successor. Otherwise hidden BFG
variables must be observed, identified or carried as uncertainty. A single
energy value generally does not identify K,F,W,Y,P. Normalized witnesses
also cannot recover original witness mass or directed transport history.

Required deliverables: calibration and uncertainty for R and Pi; a typed
clock; identifiable states or equivalence classes; specified terminals;
closure or explicitly nonclosed latent dynamics; intervention transformations;
and testable rival-discriminating predictions. Each step needs a derivation
or a separately declared physical assumption with evidence.

## Current concrete diagnostic

Input: annotated alternating pendulum extrema, angle theta and length L.
Potential energy per mass E=gL(1-cos(theta)); g=9.799 m/s^2.
This assumes negligible velocity at the chosen extrema; measured velocities
are retained for checking kinetic/potential ratios.
Scalar preparation on H=C:
P=1, W=1, Y=E/s, F=E, K=-s, with s>0.
These are admissible choices, not identifiable physical determinations.
The output readout is E_hat=sY_plus. One internal update is assigned to
one consecutive extremum interval. Every measured input resets the preparation.

From the canonical scalar computation, for 0<y<1,
Y_plus=f(y)=2y^2/((1+y)^2(1+y^2)).
Selected carrier is full; C=1/(1+y), B=y/(1+y);
Lambda_C=F/(1+y), Lambda_B=F*y^2/(1+y).
Therefore alpha=y^2/(1+y^2), beta=1/(1+y^2), and
A_dagger*A=(alpha+beta*y^2)/(1+y)^2=f(y).
No complement seed is needed in this one-dimensional nonterminal case.
The formula, positivity and contraction are derived internally.
The assignments to physical energy and event time are additional hypotheses.

Crucial reset distinction: scalar R4 inherits F, whereas Y changes. Thus
F=sY need not hold at the successor. Reinitializing from every physical
measurement is a one-step preparation experiment, not proof that the complete
BFG state follows this physical trajectory. Iterating an energy-only reset
would require a further mechanism, or a demonstrated closed projection.

## Structural feasibility and stress obligations

1. Units: Y dimensionless; E and s both J/kg. Unit changes with s transformed
   consistently preserve predictions, but changing s at fixed measurements
   changes the map. Calibration cannot be selected on holdout.
2. Carrier: scalar U(1) changes have no effect. This vacuous scalar invariance
   does not demonstrate matrix-carrier robustness or identify a carrier.
3. Gates: y>=1 loses the entire scalar selection; y=0 has zero loads.
   Coverage and terminals must accompany any error on valid predictions.
4. Small amplitudes: f'(0)=0. A regular C1 closed energy bridge to a physical
   transition with derivative a in (0,1) is impossible: differentiating
   h(f(y))=g(h(y)) yields 0=a*h'(0). Assumptions and escape routes are
   documented in the preceding MATHEMATICAL_ASSESSMENT.md.
5. Information: unsigned energy erases phase/sign and trajectory history.
   A carrier for full motion must encode enough information, or restrict
   the target to a demonstrably closed event sequence.
6. Timing: annotated extrema use future samples, including plateau resolution.
   This is a retrospective event diagnostic. A prospective predictor needs
   a causal event detector with delay declared and tested.
7. Noise: cleaned angles are rounded to 0.001 rad. Low-amplitude derivatives
   at exactly zero cannot be identified; quantization, sensor offset and
   extrema-selection error need sensitivity checks before any final bridge.
8. Clock freedom: choosing state-dependent duration to fit any observed decay
   can make a bridge unfalsifiable. Freeze independently calibrated clock
   and prohibit retrospective target-derived timing.

## Intervention logic and identifiable contrasts

The upstream experiment varied pendulum length and paper-baffle damping.
These controlled settings can support exploratory condition contrasts.
Randomization, run order and exclusion of confounding are not established by
the metadata read here; they do not by themselves identify causal effects.

For a BFG intervention claim, define u->I_u acting on K,F,W,Y,P or on
preparation, with independent calibration and predicted changes before
measurement. In the present scalar model damping condition is absent and
the formula depends only on normalized energy. At matched E/s it predicts
the same next energy ratio across damping conditions. This is a falsifiable
hypothesis, not a derived baffle intervention. No justification currently
maps baffle size into a particular BFG operator.

Physical rival: damping changes dissipation; a development-fitted energy
decay factor per length/condition is included. Further rivals before
confirmation should include angle/velocity state-space dynamics with viscous,
quadratic and dry-friction components, plus measurement uncertainty. Passive
prediction performance cannot establish the claimed intervention mechanism.

## Development design and immutable holdout boundary

Primary source EnzeXu/Damped_Pendulum_Dataset, commit
cbf82673641ecd65e902ad5c38a048387649a2a0, Apache-2.0.
Xu et al., TMLR 2026, https://openreview.net/forum?id=xvQYvYEGhj.
Only len{1..5}_cond{1..3}_1.csv was downloaded: 15 attempt-1 recordings.
Attempt 2 and 3 files (30) remain unopened. No repository clone or bulk
archive of source data is used. fetch_development.py has an explicit
filename allowlist, blob verification and a pinned source manifest.

Use upstream extrema annotations. Consecutive extrema must have finite
measurements, positive elapsed time, opposite angle signs and both angles
at least 0.01 rad. No interpolation across rejected pairs.
s=1.1*maximum eligible development peak energy.
Loss: per-record relative L2 error, then equally average 15 records.
Rivals: persistence, and per-record E_next=aE least squares constrained
0<=a<=1. The latter is scored on its fitting data. These descriptive
in-sample errors are not estimates of generalization or confidence intervals.
Stress s by factors 0.1,0.5,1,2,10; report coverage as well as valid error.
No best scale is promoted into a confirmed hypothesis.
No success rule or confirmatory claim applies to these exploratory results.

## Gate to confirmation

Not passed. The carrier map, physical projection/closure, trajectory
preparation and intervention mapping remain open. The simple scalar
linear-energy hypothesis fails the development feasibility check.
A useful next deliverable is an identifiability and closure analysis for a
carrier retaining angle and angular velocity, without inventing a formula
for its BFG operators. Candidate mappings may be explored only on attempt 1.

A revised map must document derivation versus extra assumptions, causal
measurement availability, robustness, terminals and intervention predictions.
Only then freeze all structures, code, rivals and a decision rule in a
new protocol before opening untouched data. If requirements remain unsatisfied,
publish the open requirement rather than conducting a misleading confirmation.

