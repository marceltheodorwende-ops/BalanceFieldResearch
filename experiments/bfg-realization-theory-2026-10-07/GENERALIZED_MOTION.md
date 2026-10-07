# Extending the movement representation beyond underdamping

## Constructive result and scope

The movement representation can be generalized to every passive linear
oscillator theta_ddot+b*theta_dot+a*theta=0 with a,b>=0:
undamped, underdamped, critical, overdamped, and free motion.
The physical rest state can also be represented without zero formation loads.
These restrictions of the first coordinate choice are removed mathematically.
Physical force/clock calibration is still an added assumption, not eliminated.

## Positive preparation including rest

Fix positive angular and angular-velocity reference scales theta_star,w_star.
For initial physical state let x=theta/theta_star and q=w/w_star.
Choose scalar

    F=1+x^2+q^2, K=atan2(-q,x), W=P=1, Y=0.25.

F>=1 ensures strictly positive formation even when theta=w=0.
Decode r=sqrt(F-1), theta0=theta_star*r*cos(K),
w0=-w_star*r*sin(K).
At rest r=0 and K can be chosen zero; no nonterminal zero-load gate is required.
Formation here is a shifted dimensionless encoding, not physical energy.

The actual canonical scalar update preserves F,K and advances the exact
geometry-derived clock N(Y) by one. No alteration of its ambient update is made.

## General readout and exact compatibility

Let M=[[0,1],[-a,-b]], and declare step duration dt.
Define the physical projection

    Pi(F,K,Y)=exp(M*dt*N(Y))*[theta0,w0]^T.

Then, using N(f(Y))=N(Y)+1,

    Pi(U(Xi))=exp(M*dt)*Pi(Xi).

This proves closed physical evolution for this specific declared projection:
states with the same projected physical vector have the same projected successor,
provided a,b,dt and reference scales are fixed. It is stronger than reconstructing
an initial state. Matrix exponentiation remains regular at critical damping,
so no division by a vanishing damped frequency is needed.

This is a calibrated semiconjugacy/representation. M is supplied by the
mechanical hypothesis and calibration; it is not an independently predicted
BFG generator. Using the solution operator in the readout cannot be presented
as an emergence proof of that same physical law.

## Verification

generalized_motion.py checks 110 actual ambient BFG states across five regimes,
including rest, and compares projected successors to linear state transitions.
Largest residual 2.4424906541753444e-15.
Separate analytic critical-damping and free-motion controls pass.
The original movement package's six controls and 4,485 real development
transitions were remotely reproduced in successful Action37688045722.
These generalization controls are synthetic mathematical checks, not additional
empirical evidence for overdamped or critical physical apparatus.

Reproduce from the theory directory with pinned NumPy/SciPy:

    PYTHONPATH=../bfg-pendulum-motion-2026-10-07:../real-eeg-covariance-2026-10-07 python generalized_motion.py

For long trajectories use the published stable log-coordinate clock.
Uncertainty in a,b and the clock can still amplify trajectory errors; extending
the analytic domain does not remove parameter uncertainty.

## Further extensions and independent tests

For a different well-posed autonomous physical flow Phi_t, the same scalar clock
can formally support a readout Phi_{dt*N(Y)}(decoded initial state).
That explains the breadth of possible mathematical representations. The physical
flow is then being supplied to the readout. A discriminating BFG explanation
requires independently justified restrictions on that freedom and intervention
predictions that do not simply restate a rival.

Continue to develop such restrictions using the allowed development observations.
Retain failed variants; preserve all 30 reserved recordings.
Physical calibration, independent prediction and observability constraints remain
scientific obligations, not errors cured by renaming them.
