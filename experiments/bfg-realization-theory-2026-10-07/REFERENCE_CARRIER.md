# Reference-instrument carrier: constructive preparation candidate

Status: mathematical encoding and observables constructed and verified;
physical transition and intervention closure not established. Development only.

## Information loss in a bare Gram encoding

For x=(theta/theta_star,w/w_star), x*x^T is positive semidefinite but
identifies x and -x. It cannot recover signed angle and velocity.
An energy-only carrier similarly erases phase. A full-motion forecast
requires more information or an explicitly restricted target.

## Anchored construction

Choose calibrated positive reference scales theta_star,w_star.
Put v=(1,theta/theta_star,w/w_star) and F=v*v^T.
Define J=diag(1,0,0),
A=(|0><1|+|1><0|)/2, B=(|0><2|+|2><0|)/2.
Then F is positive semidefinite, and

    theta = theta_star * tr(A F)/tr(J F),
    w = w_star * tr(B F)/tr(J F).

For this preparation tr(JF)=1, so reconstruction is exact.
The reference component resolves the sign ambiguity of the bare two-vector
Gram matrix. All these statements are algebraic, not sensor accuracy claims.

Under joint unitary coordinate changes of F,J,A,B, the trace ratios are
unchanged. The instruments are essential: transforming F alone while holding
the numerical instruments fixed changes the measurement.
The BFG quotient does not independently supply oriented sensor instruments.

One admissible exploratory state proposal is
P=I, W=F/tr(F), Y=gamma*F/tr(F), K=-I, with fixed 0<gamma<1.
The load is selected and the formation is positive semidefinite.
These operator assignments are additional hypotheses; units, preparation
scale and physical meaning are not derived merely by their admissibility.

## What this solves

A precise preparation and observable candidate preserves signed angle and
velocity and respects joint unitary coordinate covariance.
reference_carrier.py verifies 200 random preparations, positivity and jointly
rotated readouts, to floating-point precision. Synthetic values are controls.

## Transition obligation

It remains necessary to propagate instruments into the successor carrier
with a declared rule and prove/test closure of the physical readout under
the actual ambient BFG update. No assertion is made that this candidate
already obeys the mechanical pendulum ODE or preserves its energy law.
Observer instruments, carrier changes, named terminals and measurement
uncertainty must be part of that test. Fitting a mechanical ODE outside this
carrier would not establish BFG-derived transition dynamics.

Next development package: implement the full ambient update for this fixed
candidate and inspect observable closure, physical one-step dynamics and
failure modes against the existing strong mechanical rivals. Keep all
confirmation observations sealed and retain any negative result.
