# P71 — Identifiable two-tone instrument family and its physical limits

## Statement and sources

P70 left an unknown response-time/gain/delay and preparation interface. Here
construct a reference calibration for a restricted response family, resolve
its identification/robustness limits, and derive the reconstruction needed by
the nonlinear force/canonical-factor problem. This is one necessary interface
investigation, not a fitted new pendulum. The actual calibration remains absent.

Sole source Dynamic Order,8Oct2026,144pages,SHA256
1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba.
PartI22–23(87)–(91),73.1; II83(121)–(123),89(161)–(162) require typed
quotient-invariant observables, independent clocks/preparation, factor fibers
and exact flow endpoint equality. PartI62–64/AppendixA supply regular matrix
tangents, not a device response. Instrument equations below are explicitly
ADDITIONAL assumptions, not canonical inputs or internal physics derivations.
This continues P65/P68/P70, retaining P69's countercertificates unchanged.

Assume an independently known real reference Q_ref(t)=Q0+
Re(A1 exp(i omega1 t)+A2 exp(i omega2 t)), A1,A2!=0,
0<omega1<omega2, with SI seconds, phases, amplitudes and units independently
calibrated. On a settled record postulate one linear channel

 theta x'(t)+x(t)=a Q_ref(t-Delta)+d,                  (1)
 H_j=X_j/A_j=a exp(-i omega_j Delta)/(1+i omega_j theta).

a>0 dimensionless, theta>=0 and Delta>=0 seconds, d angular units. theta=0
is an algebraic direct-response limit with delay, not a four-state ODE divided
by zero. Transient history, estimator error, reference error and nonlinearity
must be bounded separately. A nominal sample grid supplies none of these.
The gain sign restriction is essential to the phase convention. Repeat this
design for the velocity channel using known W_ref=Q_ref', with nonzero tone
amplitudes i omega_j A_j, its OWN gain/offset/response/delay. Equality or channel
alignment is a testable extra restriction, not obtained by renaming variables.

## Global response/gain identification inside the fixed family

Let m_j=|H_j|>0, R=m1^2/m2^2, u=theta^2, A=omega1^2,B=omega2^2.
Then R=(1+B u)/(1+A u). Since
 dR/du=(B-A)/(1+A u)^2>0,
the map is strictly increasing from1 to B/A (not attained for finite theta).
Consequently

 u=(R-1)/(B-A R), theta=sqrt(u),
 a=m1 sqrt(1+A u), d=x_DC-a Q0.                       (2)

For 1<=R<B/A these are unique and satisfy both magnitudes. R<1 or R>=B/A
is inconsistent with finite positive gain in this exact family, not evidence
against all sensors or BFG. omega1=omega2 carries no ratio information;
zero reference/transfer amplitude invalidates division. Large theta drives
R near B/A; d u/dR=(B-A)/(B-A R)^2 diverges. At theta=0, square root is not
Lipschitz in u: a small ratio excess creates order sqrt(error) response time.
Hence exact identification does not establish robust positivity of theta.
Gain and DC offset need reference mean and its uncertainty; DC alone gives
no response-time or delay calibration. If SI timebase is free, rescaling time
rescales theta/Delta/frequencies; no seconds-per-canonical-event follows.

## Delay uniqueness, aliases and finite-error instability

After (2), corrected phases are
 U_j=(H_j/|H_j|)(1+i omega_j theta)/sqrt(1+omega_j^2 theta^2)
     =exp(-i omega_j Delta).                          (3)
Two admissible delays differ by h iff omega1 h and omega2 h both belong to
2pi Z. If omega1=m Omega,omega2=n Omega with coprime positive integers m,n,
the aliases are h=2pi k/Omega: proof uses n*k1=m*k2 and coprimality.
If their ratio is irrational, only h=0 is an EXACT common alias.
This exact irrational statement is not uniform robustness on an unbounded
delay domain. Dirichlet approximation gives unbounded integers q,p with
|q omega2/omega1-p| tending to0. Taking h=2pi q/omega1 makes U1 unchanged
and changes U2 by at most2pi|q omega2/omega1-p|, tending to0 despite h tending
to infinity. Arbitrarily close measured phases can therefore correspond to
arbitrarily remote delays. Independent bounded latency/history restrictions
are necessary for a quantitative instrument claim.

One useful explicit extra prior is 0<=Delta<=D<=pi/omega1. It removes even
the first-tone alias. For any two candidates inside this interval,
|U1(Delta)-U1(Delta')|=2 sin(omega1|Delta-Delta'|/2)
 >=2omega1|Delta-Delta'|/pi.
Thus |Delta-Delta'|<=pi|U1-U1'|/(2omega1). Recover a consistent delay from
the principal phase in [-omega1 D,0]; if phase falls outside this range under
uncertainty, intersect feasible phase sets rather than silently unwrap to the
desired answer. The second phase tests the same delay. This prior is proposed
design information, not a measured bound on the dataset apparatus.

For pairwise complex transfer discrepancy |H-H'|<=E and |H|,|H'|>=m>0,
normalization gives |H/|H|-H'/|H'||<=2E/m. The derivative of the phase
correction in theta has magnitude omega/(1+omega^2 theta^2)<=omega.
Hence |U-U'|<=2E/m+omega|theta-theta'|, yielding a conditional delay bound
with the preceding inequality. For two candidates within the SAME measurement
error epsilon, use E<=2epsilon, not epsilon. Uncertainty in frequency/reference
phase/time adds its own terms; (3) does not calibrate an unknown SI reference.

## Exact set-membership amplitude uncertainty

Given measured amplitudes hat m_j and complex-transfer errors <=epsilon_j
with hat m_j>epsilon_j, every possible true response has

 R_lo=(hat m1-epsilon1)^2/(hat m2+epsilon2)^2,
 R_hi=(hat m1+epsilon1)^2/(hat m2-epsilon2)^2.           (4)

Intersect [R_lo,R_hi] with [1,B/A). If empty, this fixed family is infeasible
under the specified errors. Apply increasing (2) to endpoints. If R_hi>=B/A
and the intersection is nonempty, theta has NO finite upper bound from this
test. A prior theta_max may intersect it but is an extra prior. If the interval
contains1, theta=0 cannot be excluded. Endpoint B/A is strictly inadmissible;
a lower bound at or above it leaves the set empty. This interval contains every
feasible theta; it need not be sufficient for a jointly feasible common gain,
phase and delay. Those must be intersected too, rather than labeling an outer
bound a complete confidence interval. No noise distribution or confidence
coverage is invented. Within finite response bounds, (2)'s derivative and the
square-root inequality |sqrt(u)-sqrt(u')|<=sqrt(|u-u'|) give explicit sensitivity.
Gain/offset intervals propagate via (2); unresolved response uncertainty can
make them unbounded as well. Robustness here is calibration inversion only.

## A stable causal rival: two tones do not establish the response law

Fix b>0, a known time unit t0>0, and a nonzero dimensionless eta. To any
first-order/delayed transfer H0(s) add the proper real rational transfer

 P(s)=(eta/t0) s(s^2+omega1^2)(s^2+omega2^2)/(s+b)^6.  (5)

s,b,omega have s^-1 units; the prefactor eta/t0 supplies s^-1, so P is
dimensionless. All six poles are at-b, numerator degree5: P is a stable
causal finite-dimensional added LTI branch. H0+P remains stable and causal;
it is finite-dimensional only if H0 has no exact pure delay. Its impulse response need
not be positive. That stronger physical restriction was not supplied. P(0)=0
and P(i omega1)=P(i omega2)=0. Thus H0+P has the exact same DC and two-tone
observations for any eta. It differs at a third omega3>0 distinct from both:
|P(i omega3)|=(|eta|/t0)omega3|omega1^2-omega3^2|
              |omega2^2-omega3^2|/(b^2+omega3^2)^3>0.
This is a strong explicit rival and a distinguishable prediction, not a new
empirical fit. Finitely many added tones still permit a corresponding higher
degree zero polynomial with stable denominator. Identifying a finite response
family therefore requires independently justified complexity/order restrictions
and reserved calibration checks; no finite spectral fit establishes arbitrary
unknown instrument behavior. Unknown pure delay requires a history space for
general inputs: it is not an exact ordinary four-state realization.

## Nonlinear force/state reconstruction and canonical interface

For calibrated channel constants and sufficiently smooth outputs, (1) gives
 Q(t)=[x(t+Delta)-d+theta x'(t+Delta)]/a.              (6)
For a separately calibrated velocity channel y with b_gain>0,e,theta_v,Delta_v,
 W(t)=[y(t+Delta_v)-e+theta_v y'(t+Delta_v)]/b_gain.
Then Q'=W is a cross-channel compatibility test, and independently
 W'=[y'(t+Delta_v)+theta_v y''(t+Delta_v)]/b_gain.
These are exact ideal reconstructions under the stipulated response law, not
a differentiation algorithm for rounded data. Force-in-acceleration units can
be tested against the P68 sine/cos-half candidate and strong viscous/mixed
rivals on a physically specified domain only AFTER calibrated error bounds.
Neither (2) nor (6) derives sine, inertia, gravitational coupling or an SI energy
scale from BFG; inertia times acceleration needs its own physical premise.

For known times/gains and sample/output derivative error bounds eps_x,eps_x',
the reconstruction error is <=(eps_x+theta eps_x')/a. Parameter uncertainty
adds terms; delay uncertainty <=eps_Delta adds <=sup|W| eps_Delta for Q and
<=sup|W'| eps_Delta for W only under separately proved trajectory envelopes.
These errors cannot be bounded by rounding alone or silently borrowed from
P69's direct latent-state energy bound. Inverse filtering differentiates and
is not bounded in unrestricted continuous-output sup norm: arbitrarily small
high-frequency output perturbations have large derivative/force errors.
Thus independent bandwidth/smoothness and uncertainty are necessary before
finite-sample force analysis. Calibrating the device does not prove BFG state
rank or preparation. With known theta>0 the ideal memory jet in P70 remains
rank4, while (6) exposes two latent state coordinates if the chosen BFG factor
itself has rank2. Instrument delay does not create an extra canonical direction.

For a chosen regular BFG factor Pi into nonlinear F and independently calibrated
event duration C, retain Pi U=R Pi, R(z)=flow_F^{C(z)}z and tangent
DR=D_z flow_F^C+F(Rz)DC. No calibrated sensor sample is called a BFG event.
If a delayed latent-state projection is desired and a backward flow on the
entire required domain is independently justified, set J=flow_F^{-Delta},
Pi_Delta=J Pi, R_Delta=J R J^-1,C_Delta=C composed with J^-1.
Then R_Delta(z)=flow_F^{C_Delta(z)}z and
DR_Delta=D J(R J^-1 z) DR(J^-1 z) D J^-1(z).
Thus nonlinear closure and the essential clock-gradient term survive under
this specific invertible flow chart. Without backward-domain/history and
physical selection this construction is unavailable; delays and filters may
not simply be discarded to force (161). Positivity/terminal fiber and no-Zeno
clock bounds are inherited only within the verified conjugate domain.

## Whole-source/other-level search and proof status

Search covered ambient/gauge/differential chain83–85/62–64/AppendixA, weighted
loads86(144)–(145), formation/loss/seed86(146)–(147), entropy/diversity86(148)–(149),
historical witness86(150), finite seed87(152), autonomous/driven scalar88(153)–(156),
viability/transverse88(157)–(158), separate mediator88(159), factors/clocks89 and
typed transition90(163)–(164). These constrain canonical evolution/accounting
but supply neither reference tones, response law nor calibrated delay/gain.
Constant d and16/27 scalar contraction are a declared input model; fixed-point
event counting requires a new clock and is not this instrument response.

For full-persistence tensor L_m, use the normalized base Pi_m(L_m Xi)=Pi(Xi)
and the SAME calibrated instrument constants/history. The return/clock and
reconstruction pull back unchanged; rank2 is retained on base directions,
ambient/persistent ranks multiply, formation stock and witness normalization
are preserved. No m independent reference measurements or noise averaging
results. Seed replication may terminate T_seeddeg. An apparatus with distinct
filters at different levels needs a separate typed measurement/state/history
extension, not automatic application of (164). No fractality is asserted.

PROVED under the fixed assumptions: global magnitude inverse, exact delay
alias classification, unbounded-delay instability, bounded-domain sensitivity,
uncertainty outer intervals, stable causal rival, nonlinear reconstruction and
conditional canonical conjugacy. EXTRA PHYSICAL HYPOTHESES: first-order order,
positive gain, stationary history, independent SI reference/phase, bounded
delay/errors, actual mechanical angle/preparation. Inspected P65/P70 source
metadata does not supply these reference records. Actual physical calibration,
force selection, SI canonical-event clock, inertia/energy, shared preparation
and interventions remain OPEN. Next necessary dependency: justify a bounded
instrument complexity/history/delay/uncertainty family from primary apparatus
evidence and specify independent calibration/preparation observations including
an out-of-family reference check before further development fitting.
