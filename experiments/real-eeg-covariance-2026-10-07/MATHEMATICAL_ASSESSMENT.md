# Mathematical assessment after the real EEG experiment

Paper source: 76d9e87b4275ec41b3dcd84434e2ee3791a8d076.
EEG protocol: 37f31b1b8aae878418fe2510a55b7896bb114579.
Results: d1e4a2d8bb02de4ea2cbc97c7fd6d590d23c40b9.
This assessment is post-holdout analysis, not a change to the frozen experiment.

## Independent spectral reduction

For the tested preparation P=I, F=sY and W=F/tr(F), let y_i be the
eigenvalues of Y and J={i:0<=y_i<1}. On nonterminal inputs define

    C = s sum_J y_i/(1+y_i)
    B = s sum_J y_i^3/(1+y_i)
    alpha = B/(C+B), beta = C/(C+B).

The next physical covariance has eigenvalues

    s (alpha + beta y_i^2)/(1+y_i)^2, i in J,

and zero in discarded directions. This follows by simultaneously diagonalizing
F and Y, applying the paper's selected subspace and the R4 update. It is an
independent oracle for this particular commuting preparation, not a formula
for arbitrary BFG states.

A separate calculation from the published window covariances reproduced every
one of the 3,685 held-out relative Frobenius losses: largest absolute residual
7.105427357601002e-15. Subject aggregation and the seeded paired bootstrap
were also independently reproduced. Eleven artifact files matched their
published SHA256 entries. These checks strengthen implementation confidence,
not the empirical predictive claim.

## A structural limitation of this EEG bridge

With fixed development scale s, multiplying a positive definite covariance by
r selects precisely the eigenvalues r lambda_i(F)<s. Thus large-power
directions can be discarded. For r>=s/min_i lambda_i(F), every direction is
discarded and the preparation is terminal. This bridge is consequently not
globally equivariant under arbitrary physical covariance rescaling with s
fixed. Rescaling the development data and refitting s is a different operation.
This observation motivates explicit bridge tests; it does not refute the
paper's abstract matrix construction.

## A conditional theorem for a physical follow-up

The scalar branch studied in the paper is

    f(y) = 2 y^2 / ((1+y)^2 (1+y^2)).

It extends smoothly to zero with f(0)=0 and f'(0)=0, since
f(y)=2y^2+O(y^3). Suppose a physical energy transition extends smoothly to
zero with g(0)=0 and g'(0)=a, where 0<a<1. Suppose further that a regular C1
observable/coordinate bridge h satisfies h(0)=0, 0<|h'(0)|<infinity and
h(f(y))=g(h(y)) near zero. Differentiating at zero gives

    h'(0) f'(0) = g'(0) h'(0),
    0 = a h'(0),

a contradiction. Such a regular closed scalar bridge cannot exist under
these assumptions. Linear viscous damping sampled at a fixed finite time,
or asymptotically fixed peak interval, supplies a candidate physical
transition with a nonzero derivative.

Scope: this is a conditional mathematical restriction, not evidence that
a measured apparatus actually follows that transition. Singular bridges,
state-dependent clocks, additional state variables, other preparations and
nonviscous damping are outside the theorem. Finite noisy measurements cannot
establish a derivative at exactly zero.

Next empirical question: compare an explicitly hypothetical linear energy
bridge to the scalar update on independent real damped-pendulum recordings,
with development-fitted physical decay baselines and a frozen holdout.
No old EEG holdout will be used to validate a revised predictive hypothesis.
