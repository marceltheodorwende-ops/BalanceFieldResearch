# Conditional physical explanation of pendulum damping and its BFG representation

Status: physical mechanism derived under explicit additional mechanical
assumptions; representation in the scalar BFG extension is exact for the
exponential envelope model. Derivation of those physical assumptions from
BFG alone is not established. No held-out observations were accessed.

## Physical state, energy and dissipation

Assume a rigid pendulum with moment of inertia I about the pivot, total mass m,
center-of-mass distance ell, angular displacement theta and angular velocity w.
Under gravity and passive viscous, quadratic and dry-friction torques,

    I * theta_ddot + m*g*ell*sin(theta)
       + b*w + c*abs(w)*w + tau_c*sign(w) = 0.

Here b,c,tau_c are nonnegative empirical mechanical coefficients.
This torque law is an additional physical model, not a consequence presently
proved from the BFG finite-state axioms. Its mechanical energy is

    E = I*w^2/2 + m*g*ell*(1-cos(theta)).

Multiplication of the motion equation by w gives the exact power balance
away from the dry-friction discontinuity,

    E_dot = -b*w^2 - c*abs(w)^3 - tau_c*abs(w) <= 0.

Thus energy decreases because resistive torque does negative mechanical work;
it transfers mechanical energy to the environment. A closed system including
that environment may conserve total energy; the pendulum subsystem is open.
This explains the physical mechanism with a force law and an energy balance.
It does not require measured energy to equal the BFG internal Gram load.

The earlier potential energy per mass g*L*(1-cos(theta)) additionally assumes
ell=L and negligible kinetic energy at an extremum. A point-mass pendulum
would have I=m*L^2, but a rotor/rod/baffle can change inertia. Those identifications
require apparatus calibration and are not guaranteed by the dataset labels.

## When the exponential model follows

For small angles, viscous damping dominant and weak damping,

    theta_ddot + (b/I)*theta_dot + omega_0^2*theta = 0,
    omega_0^2 = m*g*ell/I.

The underdamped solution has amplitude envelope exp(-b*t/(2I)).
The period-averaged mechanical energy, to the weak-damping approximation,
is proportional to amplitude squared:

    E_bar(t) = E_bar(0)*exp(-kappa*t), kappa=b/I.

Instantaneous mechanical energy is not exactly that exponential: its derivative
is -b*w^2 and oscillates in phase. The exponential is an averaged/envelope
description. Comparable extrema follow it approximately in the linear weakly
damped regime. No exact exponential fit to all rounded peaks is asserted.

For a nearly harmonic cycle, average w^2=E/I. Also
average abs(w)^3=(4/(3*pi))*(2E/I)^(3/2) and
average abs(w)=(2/pi)*sqrt(2E/I). Therefore the approximate energy envelope
for mixed friction is

    E_bar_dot = -(b/I)*E_bar
                - (4*c/(3*pi))*(2E_bar/I)^(3/2)
                - (2*tau_c/pi)*sqrt(2E_bar/I).

Exponential damping is a special regime, not a universal friction law.
This wider mechanism predicts amplitude-dependent losses when quadratic drag
or dry friction matters. It provides strong physical rivals for development.

## Baffle intervention: what can be predicted conditionally

For a small object moving at speed v through air in a quadratic-drag regime,
assume F_drag=(rho_air*C_D*A/2)*abs(v)*v.
For a baffle concentrated at radius r with v=r*w, the corresponding torque is

    tau_drag = -(rho_air*C_D*A*r^3/2)*abs(w)*w,

so c=(rho_air*C_D*A*r^3/2). An extended baffle requires a spatial integral.
Adding a baffle may also change I, the center of mass and other drag terms.

Conditional intervention prediction: at fixed I and otherwise matched state,
increasing c increases dissipative power c*abs(w)^3, particularly at high speed.
A larger paper baffle cannot automatically be reduced to a larger constant
viscous kappa: its geometry, drag regime and inertia changes matter.

The source metadata provides length and damping-condition labels, but the
materials inspected do not provide calibrated I, m, ell, baffle areas/radii,
air properties, drag coefficients and full sensor uncertainty. These cannot
be silently invented. Development fitting can estimate effective coefficients,
but that is not an independent first-principles BFG prediction.

## Exact connection to the scalar BFG representation

For the canonical scalar branch f and its coordinate phi,
phi(f(y))=phi(y)^2. Define H_p(y)=C*(-log(phi(y)))^(-p).
The continuous extension

    T_t(y)=phi^{-1}(phi(y)^(exp(kappa*t/p)))

obeys H_p(T_t(y))=exp(-kappa*t)*H_p(y).
Consequently it represents the viscous energy envelope exactly when that
physical envelope approximation applies. Setting kappa=b/I supplies a
conditional connection to the mechanical torque model above.

This is a physical explanation plus a BFG representation under declared
coupling assumptions. It is not yet a proof that the mechanical torque law,
energy observable, physical units or rate follow from the BFG axioms.

## Why the unrestricted derivation is currently underdetermined

For any positive C,p,kappa the same internal scalar f permits this representation.
The dimensionless map does not select an energy unit, a time unit or b/I.
At a fixed canonical event, H_p retention is 2^(-p), so varying p changes the
assigned physical damping without changing f. Changing the assigned seconds
per event changes kappa without changing f.

These freedoms are an explicit nonuniqueness example: the internal scalar
structure alone does not determine a unique physical damping law or coefficient.
An independent coupling/calibration principle is required. Choosing parameters
to reproduce measured damping establishes a representation, not a new mechanism.

## Current disposition

The conditional physical mechanism and exact representation are now specified.
The missing unconditional BFG derivation is explicitly isolated:
derive or independently justify the observable/coupling, physical clock and
intervention coefficients. Do not claim this requirement has been solved.

Next development work should estimate competing viscous/quadratic/dry-friction
models on attempt-1 angle/velocity data, audit identifiability and measurement
errors, and look for independently supported calibration constraints.
A future confirmation must freeze these assumptions and compare against the
same mechanical models, rather than count their coordinate encoding as a win.

Sources: paper commit 76d9e87b4275ec41b3dcd84434e2ee3791a8d076,
docs/MODEL.md and docs/CLAIM_STATUS.md; primary measurement dataset
https://github.com/EnzeXu/Damped_Pendulum_Dataset at
cbf82673641ecd65e902ad5c38a048387649a2a0.
The mechanical assumptions above are stated explicitly; no new source is
claimed to prove their emergence from BFG.
