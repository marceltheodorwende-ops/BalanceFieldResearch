# P68 — Position clock, sine restoring force and exact event compatibility

## One active obligation, assumptions and completion rule
Resolve P67's next clock dependency on the SAME selected P62/P63 canonical
return and P66 harmonic factor. Classify a monotone point observable together
with a positive position-dependent time change. Construct a rank-two full sine
restoring factor, or establish the precise obstruction; retain damping, energy,
event durations and their tangent term. Completion requires general derivation,
domains/counterexamples, independent controls, publication and byte-verified
register plus both ledgers. This is mathematical interface work, not a fit.

Sole source: Dynamic Order,8October2026,144pages,SHA256
1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba,
freshly verified. PartI22–23(87)–(91),62–64,73.1; PartII83(121)–(123),
84–85(124)–(143),86(144)–(150),87(152),88(153)–(159),89(161)–(162),
90(163)–(164),AppendixA. P62/P63 preparation/interpolation selections and P66
readout are extra hypotheses. Nothing here changes the canonical matrix update.

Accompanying full-paper search covers the ambient nonlinear differential chain,
gauge quotient, loads/stocks/spectral diversity/witness, finite seed capacity,
autonomous/driven scalar, mediator/viability/transverse, factors/clocks and lifts.
The clock/factor provisions explicitly allow state durations but require independent
calibration and endpoint equality; positivity alone excludes neither Zeno nor a
wrong generator. Stock/load balances are not SI energy. Input d introduces a
different model and breaks the old Abel equation; it is not silently added here.
Full-persistence replication preserves this base construction, not independent
clock evidence. No tensor hierarchy is needed; no physical fractality asserted.

Fix u=N(x), theta=phi+nu N(x)-b(x), Lu=1,Ltheta=nu as in P66.
With a>0,delta>0,nu!=0,c>0 define old model time s=c*u along each trajectory,
q=a exp(-delta*u)cos(theta),
p=a exp(-delta*u)[-delta*cos(theta)-nu*sin(theta)]/c.
Then dq/ds=p, dp/ds=-k0*q-g0*p, k0=(delta^2+nu^2)/c^2,
g0=2delta/c; hence k0>g0^2/4 and the inherited readout has rank two at
every finite nonterminal u. Its event matrix is M=exp(c*A0),
A0=[[0,1],[-k0,-g0]]. These choices install harmonic mechanics in a readout,
category(c); s and c were not independently identified as measured SI time.
The origin is an excluded limiting point of the inherited carrier, though the
factor vector field below has a regular extension there.

## Classification of the additional position clock
On an interval J choose h C2 with h' nonzero and r C1 positive. Declare
 Q=h(q), d tau/ds=r(q), W=dQ/dtau=h'(q)*p/r(q).            (1)
Both h and r are additional observable/clock hypotheses. Put B=h'/r. The
map H=(h,B*p) has det DH=h'^2/r>0, inverse q=h^-1(Q),p=W/B.
Using d/dtau=(1/r)d/ds gives the FULL factor
 Q'=W,
 W'=[h''/h'^2-r'/(r*h')]W^2-(g0/r)W-k0*q*h'/r^2.        (2)
Primes on Q,W denote tau derivatives; h,r derivatives are with respect to q.
The quadratic coefficient vanishes on an open rank-two state patch iff
(log|h'|-log r)'=0, equivalently r=C*h', where C is a nonzero constant
with C*h'>0. Then W=p/C and
 W'=-(g0/r)W-k0*q/(C^2*h').                              (3)
For constant target damping gp and g0>0 the velocity coefficient requires
r=g0/gp constant (gp=0 is impossible), hence h' constant. The restoring
force is then affine in Q and cannot equal kp*sin Q for kp>0 on an open
interval, by two derivatives. Thus even a positive position clock plus any
monotone point map cannot produce BOTH constant damping and a pure sine
acceleration from this damped harmonic factor. Constant torque does not remove
the second-derivative contradiction. This scoped obstruction does not cover
velocity-dependent clocks/observables, other carriers or declared force inputs.
For g0=0 this damping argument fails, but delta=0 loses inherited rank; that
algebraic exception is not a regular two-dimensional P66 realization.

## Constructive escape: sine acceleration with variable damping
Keep g0>0, choose kp>0,C>0 and impose centered h(0)=0,h'>0 plus the sine
restoring requirement k0*q/(C^2*h')=kp*sin h. Integration yields
 cos h(q)=1-k0*q^2/(2*C^2*kp).
On the principal monotone branch this fixes
 alpha=sqrt(k0/kp)/(2*C), h(q)=2*asin(alpha*q),
 r(q)=C*h'=r0/sqrt(1-alpha^2*q^2), r0=sqrt(k0/kp).        (4)
This is conditional uniqueness inside the chosen centered/oriented branch,
not physical selection: the target kp and centering are imposed. Noncentered
branches on intervals avoiding zero have different integration constants;
identity h with constant r is an admissible harmonic rival. C<0 with h'<0
gives the reversed orientation version. Therefore compatibility alone is not
a unique physical angle or clock criterion.

For |alpha*q|<1, -pi<Q<pi, H(q,p)=(2asin(alpha*q),p/C),
inverse q=sin(Q/2)/alpha,p=C*W. The exact nonlinear law is
 Q'=W,
 W'=-kp*sin Q-Gamma(Q)*W,
 Gamma(Q)=g0*sqrt(kp/k0)*cos(Q/2)>0.                     (5)
The quadratic inertial term is gone and the restoring acceleration is exactly
sinusoidal. Damping is position dependent; replacing Gamma by a constant
changes the equation. Its ratio Gamma(0)/sqrt(kp)=g0/sqrt(k0)<2 is an inherited
conditional underdamping restriction, not a BFG physical parameter prediction.
This construction solves the stated mathematical clock interface; it does not
derive a physical pendulum law internally. The sine was expressly required in
selecting h,r, on top of embedded harmonic mechanics. Category(c) representation
and category(b) proposed physical clock/instrument identification remain distinct.

## Exact event duration and tangent — no silent fixed-time substitution
Let Phi_s(z)=exp(s*A0)z for z=(q,p). Define the quotient-invariant duration
 T(z)=integral_0^c r([Phi_s(z)]_q) ds,                   (6)
on trajectories within the chart, and F=(W,-kp*sin Q-Gamma(Q)W).
Time change of the already constructed flow gives
 H(Mz)=flow_F^{T(z)}(H(z)).                              (7)
Thus the discrete event factor is still H M H^-1, not flow_F at a constant
time. Because H is injective, T factors through H and is constant on the
inherited projection fibers on this selected family. No statement is made for
all ambient BFG states. A continuous clock is an accumulated path variable
tau(s)=tau(0)+integral r ds; it is not claimed to be a function of q alone.
It neither asserts nor needs N(f(y+d))=N(y)+1 at a driven fixed point.

With J_F the fixed-duration flow Jacobian, differentiation gives
 DH(Mz) M = J_F(T(z),H(z)) DH(z)+F(H(Mz)) DT(z),
 DT(z)=integral_0^c r'(q(s))*[exp(s*A0)]_{first row} ds.  (8)
The final rank-one term is essential when the event duration varies. Equivalently
in (Q,W) coordinates the derivative of the event is
 DH(Mz)M DH(z)^-1=J_F+F(H(Mz))*DT(z)*DH(z)^-1.
Ignoring DT compares two different maps and gives a false tangent mismatch.
For (5), DF=[[0,1],[-kp*cos Q+(Gamma(0)/2)sin(Q/2)W,-Gamma(Q)]].
The exact identities inherit P62/P63 actual canonical endpoint and differential;
controls independently integrate the new flow and duration, rather than equate
an arbitrary clock to a mechanical endpoint by notation.

## Units, energy, admissibility and declared robustness range
q,Q dimensionless; p inverse old model seconds, W inverse new model seconds.
r and C dimensionless ratios when s,tau are both in a seconds unit; k0,kp have
inverse-time-squared units in their respective clocks, g0,Gamma inverse time.
An actual equality to SI device timestamps remains uncalibrated. Choose extra
I>0 in kg*m^2 and define
 E=I*[W^2/2+kp*(1-cos Q)]=I*(p^2+k0*q^2)/(2*C^2),
 dE/dtau=-I*Gamma(Q)*W^2<=0.                             (9)
This is constant inertia and the full sine potential, obtained conditionally
through the selected clock; I does not come from formation stock. With a
hypothetical impulse Delta W at fixed Q, p+=p+C*Delta W and
Delta E=I*(W*Delta W+Delta W^2/2). This is a typed factor interface, not a
constructed canonical actuator or evidence of an actual intervention.

Before numerical controls define dynamical stability as factor energy
nonincrease and forward chart invariance. Put e0=(p0^2+k0*q0^2)/2 and assume
2*alpha^2*e0/k0<=rho^2<1. Then energy decay ensures |alpha*q(s)|<=rho;
 d=1-rho^2, r0<=r(q)<=rmax=r0/sqrt(d),
 c*r0<=T(z)<=c*rmax.                                    (10)
All future event sums diverge; there is no Zeno accumulation on this corridor.
For any finite old horizon, the new horizon is finite and comparable. In the
extended factor origin, asymptotic stability follows from harmonic decay and
these clock bounds. More explicitly omega0=sqrt(k0-g0^2/4)>0 gives
 ||exp(s*A0)||<=B exp(-g0*s/2),
 B=1+||A0+(g0/2)Id||/omega0 in a declared scaled state norm;
 s>=tau/rmax and H Lipschitz on the corridor transfer exponential decay to
(Q,W), with a norm-dependent prefactor. This does not prove full ambient BFG
contraction, uniform rank at the limiting origin or gate/gap reserve.

For observation/clock conditioning freeze |alpha*q|<=rho, bounded p and fixed
parameters. |h'|<=2alpha/sqrt(d), |r'|<=r0*alpha*rho/d^(3/2),
 |Delta Q|<=2alpha/sqrt(d)|Delta q|,
 |Delta W|=|Delta p|/C,
 ||DT||<=[r0*alpha*rho/d^(3/2)]integral_0^c ||row_1(exp(s*A0))||ds.
Finite disturbances require both connecting states and intervening trajectories
inside the same energy corridor. Bounds worsen as rho->1 or omega0->0;
at |alpha*q|=1 the clock and DH diverge and this chart is invalid. The restoring
vector field extends differently beyond |Q|=pi (Gamma changes sign), but that
extension is not this monotone clock construction. Numerical stability here is
agreement of independent DOP853/quadrature/exact exponential calculations at
frozen tolerances, not a universal integration guarantee. Prediction robustness
on real records has not been tested; synthetic controls are not measurements.

## Distinguishable predictions and independent physical selection still required
If an independently identified preparation fixes A (old harmonic amplitude),
g0=0 algebraic limit has s-period 2pi/sqrt(k0); time transformation yields
tau-period 4*K(alpha*A)/sqrt(kp), K the complete elliptic integral. Equivalently
the constructed conservative sine pendulum is amplitude dependent. This
illustration is not a delta=0 rank-two BFG realization or measured frequency.
For actual g0>0 use (5),(6), not a constant-amplitude period formula.
With measured Q,W and independent time one can distinguish Gamma(Q) from
constant damping through energy decay/acceleration away from zero, subject to
instrument error and common preparation; near zero they agree to first order.
There are no genuine canonical-event timestamps in P65's inspected recordings.
Changing the time label of existing sensor data cannot supply those timestamps.
P65's identification blockade therefore remains. No new empirical fit is
justified by this representation; old shared-calibration results remain intact.

Necessary next dependency: independently restricted angle/clock/preparation
selection with observable event identification, or a compatible state/velocity
bridge with explicit physical selection. Do not claim success for constant
damping by dropping Gamma(Q), the event-clock tangent or calibration obligation.

An explicit force rival demonstrates remaining nonidentifiability without
altering the canonical return. Choose an EXTRA even single-well potential V(Q)
with V(0)=0,V''(0)=kappa>0 and V'(Q) of the sign of Q. Locally the monotone
inverse coordinate q(Q)=(C/sqrt(k0))*sign(Q)*sqrt(2V(Q)) is smooth at zero
for a smooth even potential with a positive quadratic term. Its inverse h and
r=C*h' give W'=-V'(Q)-(g0/r)W, since differentiation of
V(h(q))=k0*q^2/(2*C^2) gives V'(h)*h'=k0*q/C^2.
For V=kappa*Q^2/2+lambda*Q^4/4,lambda>=0, the explicit inverse
q(Q)=(C/sqrt(k0))*Q*sqrt(kappa+lambda*Q^2/2) has strictly positive
derivative and yields a linear-plus-cubic force rather than sine. Both clocks
are quotient compatible on compact energy charts. Thus full nonlinear closure
and positive clocks do not select sine over this nonlinear rival. Independent
physical time/observable/preparation evidence is the next necessary discriminator.

The new carrier observation determinant is h'/C times the inherited
delta*a^2*exp(-2delta*u)*nu/c, and nonzero at finite u. Under the new clock,
the inherited envelope R=a*exp(-delta*u) and phase obey
dR/dtau=-delta*R/(c*r(q)), dtheta/dtau=nu/(c*r(q)). Their state-dependent
rates explain amplitude/phase distortion without changing the canonical event.
Numerical initial pairs below are nonzero; choose a above their reconstructed
envelope sqrt(q^2+((p+g0*q/2)/sqrt(k0-g0^2/4))^2), so they lie in an
open inherited factor image at u>0. No new physical preparation is inferred.

## Proof and verification status
General formulas, scoped obstruction, centered sine construction, rank, exact
event/clock tangent, conditional energy and corridor/no-Zeno bounds PROVED
under declared assumptions. Explicit full sine acceleration is a representation,
not internal physical force derivation. Constant-damping target REFUTED within
this position-clock/point-map subclass. Independent symbolic and numerical
controls in check.py/controls.json verify calculations only. Physical angle,
SI clock, I,shared preparation/parameters,real interventions and force selection
remain OPEN; no holdout/measurements/data download or new empirical workflow.
