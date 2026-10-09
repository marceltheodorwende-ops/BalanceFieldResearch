# P63 — Exact continuous interpolation and force nonidentifiability

## Active claim and completion criteria
Starting with ONE fixed P62 invariant curve and its actual nonlinear canonical
return, construct an autonomous two-dimensional continuous interpolation whose
unit-time map is exactly that return. Prove regularity, nonlinear closure,
domain and tangent identities. Determine whether the event and even a fixed
constant event duration identify the interpolating angular velocity/acceleration.
Finish with counterexamples, independent controls, publication and verified
register/ledgers. This package does not assert a physical pendulum law.

Sole source: Dynamic Order, 8 October 2026, 144 pages, SHA256
1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba.
Sources: Part I 22–23 (87)–(91), 62–64 (full regular differential chain),
83 (121)–(123), 84 (124)–(140), 85 (141)–(143), 86 (144)–(150),
87 (152), 88.3 (157)–(158), 88.4 (159), 89 (161)–(162), 90 (163)–(164).
Dependencies P53/P54, P57, P60/P61 and completed P62.

Keep their explicitly additional commutator preparation, transverse matrix
family and inherited non-scalar witness. The continuous path is a newly
declared interpolation of that family, NOT an extra canonical event stage or
the paper's autonomous core generator. It uses no external mechanical solution.
All coordinates and interpolation time lambda are dimensionless. Seconds
remain uncalibrated. No measurements, holdout, interventions or model fitting.

Fix P62's exact T(x), and put

 U(x,phi)=(P(x),phi+theta(x)),
 P(x)=X(T(x),x), theta(x)=sigma atan(sqrt(x)), sigma=sign(eta).

Here 0<P<x on (0,x0], P'>=1/2, x_n=P^n(x0)->0; phi is a quotient
relative phase on S1, or a locally lifted real coordinate. These are the
actual return functions, not a guessed scalar damping map.

## Required local regularity
P62 gives global C1 up to its zero coordinate endpoint. More locally, away
from zero, its T is C1,1: each finite propagated segment is C1,1 because
P61's surface map is C1,1, its graph projection has derivative >=1/2,
and a C1,1 local inverse with nonzero derivative is C1,1. On each compact
subinterval of (0,x0], only finitely many seams occur. The first derivatives
match at each seam; their finitely many Lipschitz bounds give a Lipschitz
bound across the seam by splitting the difference there. Thus T and P are
locally C1,1 on the positive interval. No endpoint C2 conclusion is used.

## An exact Abel coordinate, with no fixed-point contradiction
Write x1=P(x0), p0=P'(x0)>0 and Delta=x0-x1. Choose a positive smooth
density w on [x1,x0] with w(x0)=1 and w(x1)=1/p0; a linear interpolation
of these positive numbers suffices. Let I=integral_x1^x0 w(y)dy and

 N0(x)=integral_x^x0 w(y)dy/I.

Then N0(x0)=0,N0(x1)=1,N0'<0, and
N0'(x1)*p0=N0'(x0). On I_n=[x_{n+1},x_n], define uniquely

 N(P^n r)=n+N0(r), r in [x1,x0].                         (1)

P^n maps this seed interval bijectively onto I_n; its derivative is
positive. Shared endpoint values and derivatives agree by the displayed
seed condition and the chain rule. Consequently N is locally C1,1,
N'<0, maps (0,x0] onto [0,infinity), and obeys EXACTLY

 N(P(x))=N(x)+1, N'(P(x))*P'(x)=N'(x).                   (2)

It diverges at x=0, which is excluded and canonically terminal. Thus this
construction does not claim a continuous Abel coordinate at a fixed point,
nor reuse the invalid scalar-input clock. No global inverse bounds at zero.

## Exact phase cocycle, including seam derivatives
Choose a smooth Hermite seed b0 on [x1,x0] with

 b0(x0)=0, b0(x1)=theta(x0), b0'(x0)=0,
 b0'(x1)=theta'(x0)/p0.

A cubic always realizes these four data; monotonicity of b0 is not needed.
Define on I_n

 b(P^n r)=b0(r)+sum_{j=0}^{n-1} theta(P^j r).            (3)

The values match at the seams. Differentiate the identity between neighboring
segments. At the first seam the required identity is
b0'(x1)*p0=b0'(x0)+theta'(x0), precisely the selected endpoint data.
At later seams the chain rule transports that identity, including every
theta' term in the sum. Thus b is locally C1,1 and

 b(P(x))-b(x)=theta(x),
 b'(P(x))*P'(x)=b'(x)+theta'(x).                         (4)

All sums are finite at any positive point. No convergent infinite phase sum
or regular boundary phase is assumed.

## Autonomous continuous interpolation on the same two coordinates
The C1 change of coordinates (u,psi)=(N(x),phi-b(x)) has nonzero
Jacobian N'(x). It conjugates U to (u,psi)->(u+1,psi). Pull back the
translation (u,psi)->(u+lambda,psi). For lambda>=0 set

 x_lambda=N^-1(N(x)+lambda),
 phi_lambda=phi+b(x_lambda)-b(x).                       (5)

This is a forward-complete C1 semigroup; local negative times exist when
N(x)+lambda>=0. Semigroup composition follows by canceling the two b
increments. Its unit-time map is EXACTLY U for ALL positive states, by
(2)–(4), not just at orbital endpoints. It solves the autonomous ODE

 dx/dlambda=v(x)=1/N'(x)<0,
 dphi/dlambda=omega(x)=b'(x)/N'(x).                     (6)

Both coefficients are locally Lipschitz on the positive domain, since N'
and b' are locally Lipschitz and N' is locally bounded away from zero.
Solutions are unique; (5) supplies them directly. The flow is C1 in its
initial state even though a globally C1 vector field has not been proved.
In particular, second derivatives and acceleration are initially only
almost-everywhere statements; no C2 field or endpoint extension is claimed.

The exact tangent for finite lambda is

 [[N'(x)/N'(x_lambda),0],
  [b'(x_lambda)*N'(x)/N'(x_lambda)-b'(x),1]].             (7)

At lambda=1, (2) and (4) reduce it to
[[P',0],[theta',1]], exactly P62's canonical two-dimensional tangent.
Its determinant is positive at every finite positive state. Individual
continuous phase derivatives can vanish or change sign; the event phase
increment is nonzero. No continuous monotone-phase hypothesis is inferred.

Reconstruct the complete quotient state along (5) using P62's t=T(x),
q=sqrt(x)Z*(T(x),x), s=sqrt(x)/(2|eta|), r=tq/sqrt(1+x), and the
phase/witness family. All intermediate states remain in that admitted
positive family. At lambda=1 the reconstructed endpoint is the canonical
prepared event, including witnesses. Intermediate points are the declared
interpolation; canonical discrete rules impose no evolution between events.

## Fixed-clock counterexample: accelerations still differ
Keep the SAME T, P, theta, N, event duration and measured endpoint phase.
For any smooth nonconstant one-periodic h define

 b_h(x)=b(x)+h(N(x)).

Equation (4)'s difference remains theta because h(N+1)=h(N).
Construction (5) with b_h therefore gives another autonomous locally
Lipschitz flow on the same admitted family, with the SAME unit-time event
and tangent at EVERY state. In the original observed phi coordinate,

 omega_h(x)=omega(x)+h'(N(x)).                           (8)

It is a different BETWEEN-EVENT prediction, not an SVD gauge change or a
mere relabeling of the observed phase. Along each solution N(x_lambda)
=N(x)+lambda. Wherever the base acceleration exists, differentiation gives

 alpha_h(x)=alpha(x)+h''(N(x)), alpha=v*omega' a.e.       (9)

For h(u)=epsilon sin(2pi u), the velocity difference is
2pi epsilon cos(2pi N), and the acceleration difference is
-4pi² epsilon sin(2pi N). These are explicitly nonzero while all canonical
event observations and the chosen constant event duration remain identical.
The difference itself is smooth in lambda even if base acceleration exists
only a.e. Thus even fixing the event clock cannot identify an instantaneous
angular acceleration/force from this event law alone. This counterexample
is scoped to this declared return family and endpoint information; it does
not rule out selection by additional measurements or another BFG mechanism.

If phi were independently identified with a mechanical angle and a moment
of inertia J_phys were independently supplied, the additionally assumed
law torque=J_phys*d²phi/dtau² would produce different torques for these
flows. Neither that mechanical identification nor J_phys follows here.
There is no derived sine law, potential, friction or energy. This is a
concrete force nonidentifiability result, not an embedded rival pendulum.

The Abel coordinate itself is also nonunique: for any increasing smooth
f with f(u+1)=f(u)+1, N_f=f(N) is another Abel coordinate. For example
f(u)=u+epsilon sin(2pi u), |2pi epsilon|<1, yields
v_f=v/[1+2pi epsilon cos(2pi N)] and still the same unit-time U after
using the same b. The radial interpolation is consequently not selected
either. This freedom is independent of P62's preparation-curve freedom.

## Units, positive clocks, robustness and bounds
A constant duration c>0, assigned seconds ONLY by independent calibration,
would give lambda=tau/c, generator (v,omega)/c, angular acceleration
alpha/c², and event clock c. Infinite event continuation then has total
time infinity. No value of c or physical calibration is invented.
Both flows (8) use the same c and retain the force ambiguity. A merely
positive state clock need not avoid finite total time; the source requires
the separate sum-of-durations condition. No claim about arbitrary clocks.

Here robustness means local sensitivity and interpolation perturbations
on a specified compact interval away from the terminal. For a time segment
whose trajectory remains there, assume |N'|>=m>0, |N'|<=M and |b'|<=B.
(7) gives |d x_lambda/dx|<=M/m and absolute off-diagonal <=B(M/m+1).
For a periodic perturbation with ||h||_infinity<=e, ||h'||<=e1,
||h''||<=e2, phase paths differ by <=2e, velocities by <=e1 and
accelerations by <=e2 (divide by c,c² in seconds). All event discrepancies
are EXACTLY zero. These are local sensitivity bounds, not full-state
Lyapunov or empirical prediction stability. No uniform boundary conditioning
or force accuracy follows; high-frequency periodic choices can keep phase
perturbations small while making acceleration differences large.

## Full-source and other-level audit
Part I 22–23 and 89 explicitly distinguish factor closure, a clock and a
continuous generator: (1)–(7) construct the previously missing flow matching.
Part I 62–64 demands all endogenous tangent and witness terms; P62 and (7)
retain them at events rather than changing the kernel. 83–85 provides the
admitted quotient reconstruction and terminal rules. 86's cross-load and
formation balances remain equal for the counterexample endpoints; constant
formation on this full-persistence family is not mechanical energy.
Spectral diversity and witness identities do not choose h or c. 87 offers
no infinite undeclared seed resource. 88.1's scalar limit, 88.2's positive
input fixed point and 88.3's viability distinctions neither obstruct the
positive no-fixed-point interval nor select its generator. 88.4's mediator
ODE is explicitly not a kernel generator and is not substituted here.

For the admitted full-persistence lift L_m of 90 (163), define the lifted
path by L_m composed with the reconstructed (5). By (164) its unit-time
endpoint is the lifted canonical event; normalized base readouts recover
the same x,phi and tangent. Formation stock and witness normalization
persist; ranks multiply by m, with no seed complement. The same h and c
freedoms survive the return to base coordinates. Replicated SVD degeneracy
is handled by the quotient, not invalid separated-gap component formulas.
This explicitly transfers the continuous bridge and its limit to another
compatible carrier. It supplies no independent selection, arbitrary input,
seed lift or physical fractality. No higher-dimensional suspension is needed.

## Independent controls and status
Frozen checks in check.py: symbolic derivative/cocycle cancellation and
periodic-force differences; endpoint derivative matching for general positive
p0; numerical seam and unit-time tangent controls on the independently
solvable nonlinear test P_ref=x/(1+x), theta=atan(sqrt(x)); direct autonomous
ODE integration versus the conjugacy solution; different h flows with equal
unit-time maps and different intermediate angles. The reference is ONLY a
synthetic test of this general construction, NOT P62's exact P, a calibrated
BFG surrogate, or a real measurement. The theorem uses the exact P62 P.

Observed controls: eight symbolic identities and three seed endpoint checks
passed, as did five finite-offset seam checks and five independent starting
states. Ten independently integrated ODE trajectories (two interpolations
per state) matched the canonical reference endpoints to <=1.06e-9 against
the frozen 1e-7 acceptance threshold. Direct unit-time errors were <=2.23e-15;
finite-difference tangent discrepancy <=1.36e-8. Acceleration-difference
checks agreed to <=2.56e-9; differing intermediate phases reached 0.05181
dimensionless radians while unit-time maps agreed. Seam finite offsets are
not exact seam proofs; the endpoint algebra and chain rule above provide
that proof. No numerical P62 radius, physical force or calibration is inferred.

PROVED: exact locally C1 autonomous forward interpolation on the fixed P62
family, full event/flow matching and tangent; fixed-clock nonidentifiability
of intermediate angular velocity and a.e. acceleration; compatible lifted
endpoint and local sensitivity bounds. ADDITIONAL: interpolation seeds,
continuous path and any physical clock. OPEN: independently justified physical
selection/measurement rule, sufficiently smooth mechanical observable and
calibration, then force/energy/inertia/interventions. Holdout remains closed.
