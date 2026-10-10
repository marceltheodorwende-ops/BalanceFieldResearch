# P70 — A declared sensor-memory extension and its identification boundary

## Statement, source and types

P69 rejects its direct rounding-only instrument/ODE conjunction. Here we ask
whether a physically justified memory bridge can be obtained or selected from
the available canonical model and passive channels. We construct one exact
conditional interface and prove which parts remain unidentified. This does not
replace P69's tests by new fitted uncertainty, or claim that PS-3220 uses this
response. Dependencies P65/P68/P69. Sole source Dynamic Order,8Oct2026,144pages,
SHA2561ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba.
Part I22(87)/23(88)–(91),73.1 and II89(161)–(162) impose fiber closure, calibrated
positive clock and exact flow endpoint equality. Part I62–64/Appendix A give
regular quotient differential prerequisites, not sensor dynamics. II83(121)–(123)
requires types/units and unitary invariance. None of these axioms specifies a
manufacturer transfer function or a measured calibration.

Assume an already declared smooth rank-two factor z=(q,v), q'=v,
v'=f(q,v), vector field F=(v,f), in physical time t supplied by an additional
clock. At this stage q is an ideal *output trajectory coordinate*, not an
independently selected true mechanical angle. For the P68 example
f=-kappa sin q-Gamma cos(q/2)v, kappa>0,Gamma>0. Its mechanics and arcsine
readout are imposed, not newly derived here. Radians dimensionless; v has s^-1,
f s^-2. Introduce a positive constant response time theta in seconds, and ideal
raw sensor outputs x,y of units rad,rad/s. Declare the instrument equations

 theta x'=Q-x, theta y'=W-y, Q'=W.                     (1)

Q,W are candidate latent physical coordinates. This is an added measurement
model, not a hidden change to the autonomous canonical update. Initial sensor
states/history, gains, biases, delays and uncertainty must also be specified.
Assume C2 F where second derivatives are used, and restrict all identities to
regular domains; C1 suffices for the basic pushforward.

## Memory state, closure and observation ranks

If the plant (Q,W) has a known smooth vector field (W,a(Q,W)), (1) has four
states (Q,W,x,y) with output (x,y). Projection to (x,y) alone is not autonomous:
two states with the same x,y but different Q have different x'=(Q-x)/theta.
For sufficiently small common positive time steps their output endpoints
likewise differ. Thus the factor criterion (161) fails on the unrestricted
four-state extension. Extra memory cannot be silently discarded as a gauge.

For KNOWN theta, the ideal first output jet (x,y,x',y') recovers
Q=x+theta x',W=y+theta y'. Its Jacobian w.r.t. (Q,W,x,y) has determinant
1/theta^2 and rank4. This is local ideal differential observability, not four
independent channels, a noiseless finite-difference certificate or identification
of unknown theta. Differentiating rounded data can amplify errors as 1/dt.

Define the compatibility defect r=x'-y. Differentiating (1) gives
theta r'=-r, hence r(t)=r(0)exp(-t/theta). In particular r(0)=0 implies x'=y
for all times of existence. Independent inconsistent memory initialization has
a transient; it must NOT be mistaken for a force or forgotten at a crop boundary.
An identical time-invariant linear response to Q and W on a compatible history
commutes with differentiation and preserves x'=y. The exponential kernel is
one example. Distinct filters/gains/channel delays generally do not preserve it.
With gains a,b, offsets d,e and correctly aligned common response, the relation
is x'=(a/b)(y-e), with nonzero a,b; independent scale/time calibration is needed.
Changing device time s=t/c adds the unknown factor c. Consequently fitting a
common response cannot automatically explain a kinematic violation. Nor can
P69's curvature/energy bounds be reused unchanged on differently filtered
latent angles: their premises and initial envelopes must be derived anew.

For a fixed identical plant input, differences between two instrument states
decay exactly exp(-t/theta) in any fixed product norm. With forcing difference
delta Q, delta x(t)=exp(-t/theta)delta x(0)+
 integral_0^t exp(-(t-s)/theta)delta Q(s) ds/theta;
thus the input sup-norm gain is at most1. The analogous velocity identity has
the same bound. This is sensor-memory stability only, not full BFG/plant
contraction or certified prediction robustness. theta=0 is a distinct algebraic
direct-output limit; dividing by theta in the four-state observability statement
is then invalid.

## Exact nonlinear alternative with two observable evolving directions

For a compatible observed trajectory z=(x,y)=(q,v) satisfying F, define

 T_theta(z)=z+theta F(z)=(q+theta v,v+theta f(q,v)).     (2)

Let Z=(Q,W)=T_theta(z). Then (1) is satisfied exactly with x=q,y=v, and
Q'=v+theta f=W. Its full acceleration is

 W'=A_theta(z)=f+theta(f_q v+f_v f).                   (3)

On an invertible chart the candidate plant is the closed nonlinear field
G_theta=(W,A_theta composed with T_theta^-1). This constructs an actual
conditional output/plant/memory realization without reassigning device ticks
to canonical events. It is a coordinate/observation alternative, not a selected
physical law. Its rank determinant is

 D_theta=det DT_theta=1+theta f_v-theta^2 f_q.          (4)

For P68 this becomes
1-theta Gamma cos(q/2)+theta^2 kappa cos q
 -(theta^2 Gamma/2)sin(q/2)v, and

 A_theta=-kappa sin q-Gamma cos(q/2)v
 +theta[-kappa cos q v+(Gamma/2)sin(q/2)v^2
         +Gamma kappa cos(q/2)sin q+Gamma^2 cos(q/2)^2 v]. (5)

Nonzero D gives two locally recoverable evolving directions from fixed bridge
states by the inverse function theorem. A pair of printed channels does not
establish that condition or identify theta. At q=v=0,
D=1-theta Gamma+theta^2 kappa>0 when Gamma^2<4kappa, all theta>=0.
This local result does not imply global inversion. At Gamma=0,q=pi,v=0,
theta=1/sqrt(kappa), D=0: explicit singular counterexample outside the principal
low-energy chart. On any convex patch with ||DF||<=L in a FIXED dimensionally
scaled norm and theta L<1, the mean-value Lipschitz estimate gives
||T_theta(z)-T_theta(z')||>=(1-theta L)||z-z'||. Hence injectivity and inverse
gain <=1/(1-theta L) on its image. State-to-state rank is not an uncertainty
certificate unless L,theta and instrument errors are independently justified.

The *same* P68 sine/cos-half law is not preserved by the sensor coordinate
change. On q=0 and varying v, (5) is linear in v, whereas substituting
Q=theta v,W=(1-theta Gamma)v into that same law gives
-kappa sin(theta v)-Gamma(1-theta Gamma)v cos(theta v/2).
Its third v-derivative at0 is
kappa theta^3+3Gamma(1-theta Gamma)theta^2/4>0 for
theta>0,0<theta Gamma<1. Thus it cannot agree with (5) on a neighborhood.
This proves nonpreservation of this fixed force/damping law, not exclusion of
other parameters or all instrument bridges. A general common convolution
also does not commute with nonlinear sine: equal-weight inputs q±d yield
mean sin = sin(q)cos(d), different from sin(mean q) when sin(q)!=0,cos(d)!=1.

## Canonical event, tangent, domains and energy

Retain P68's prepared canonical factor Pi, exact return R and state-dependent
positive event duration C(z): R(z)=flow_F^{C(z)}(z), Pi U=R Pi.
Set Pi_theta=T_theta Pi, C_theta=C composed with T_theta^-1. On a chart
containing the entire between-event trajectory, declare
R_theta=T_theta R T_theta^-1. Then
Pi_theta U=R_theta Pi_theta=flow_Gtheta^{C_theta}(Pi_theta).
This is exact conjugacy, retains terminal-fiber rules and gauge invariance
inherited from Pi, and changes neither U nor the prepared canonical policy.
The tangent on base directions is

 DR_theta(T_theta z)=DT_theta(Rz) DR(z) DT_theta(z)^-1,
 DR(z)=D_z flow_F^C(z)+F(Rz) DC(z).                    (6)

The F DC term remains essential; introducing sensor memory does not remove
the clock-gradient correction. All compact trajectory/chart/rank assumptions
are additional to the paper's regular operator gaps. Inherited C has the same
positive bounds along conjugate paths, so a prior no-Zeno lower bound persists;
no measured seconds or canonical-event detector is supplied by (6).

P68 conditional E(z)=v^2/2+kappa(1-cos q), E'=-Gamma cos(q/2)v^2 on its
principal energy chart. Define E_theta(Z)=E(T_theta^-1 Z); chain rule gives
the same dissipation on the conjugate domain. This is a pullback Lyapunov
function, generally not W^2/2+kappa(1-cos Q). Multiplying by a physical inertia
still needs a calibrated extra bridge. No apparatus energy conservation follows
from formation stock or from changing observed coordinates.

## Passive response time is nonidentifiable: exact full-trajectory example

Let observed z'=Jz, J=[[0,1],[-kappa,-gamma]], gamma^2<4kappa, with an
arbitrary nonzero initial z0. For EVERY theta>0 let S_theta=I+theta J.
det S=1-theta gamma+theta^2 kappa>0, and S commutes with J. True candidate
Z_theta=S_theta exp(tJ)z0 obeys the SAME specified harmonic force
Q'=W,W'=-kappa Q-gamma W. Take instrument initial x,y=z0. Then
theta z'=Z_theta-z, so every theta gives exactly the SAME angle and velocity
outputs at ALL times, not just finite samples. True initial preparation differs.
No noise, unknown mechanical coefficients or interpolation freedom is needed.
Thus ideal passive outputs plus a known linear plant cannot generally identify
common theta without independently restricted preparation/reference. The P66
harmonic factor transfers this example to its conditional canonical return.
Its externally installed harmonic physics remains category(c); this is not a
claim that the nonlinear P68 sine model is unidentifiable for every fully fixed
preparation. Nonlinear known force with constrained preparation may identify a
restricted filter; it must be separately proved and checked, not guaranteed.

A minimal extra *preparation reference* breaks this specific ambiguity:
if the independently known true initial angle Q0 and ideal observed q0,v0
satisfy v0!=0, (2) forces theta=(Q0-q0)/v0. If v0=0 but known f0!=0,
an independently known true W0 instead gives theta=(W0-v0)/f0.
Both equations must agree when both are available, and inferred theta must
respect the declared positive domain. At F(z0)=0 they identify no response
time. The first ratio has error bound
|delta theta| <= (eps_Qtrue+eps_q)/vmin+N eps_v/vmin^2
on a same-sign convex velocity interval |v|>=vmin>0 and initial numerator
|Q0-q0|<=N. This follows by differentiating the ratio; it requires independent
reference/response error budgets, not a timestamp or a noncausal peak flag.
This construction is a concrete next measurable dependency; none of its
reference values is invented for the actual pendulum data.

## A concrete independent reference calibration, and its limits

Assume independently measured true angle reference
Q_ref(t)=Q0+Re(A exp(i omega t)), known omega>0,known nonzero complex A and
known phase/seconds, after sensor transients, with no unknown channel delay.
Postulate a first-order channel with positive gain a and offset d:
theta x'+x=a Q_ref+d. Its measured complex transfer is
H=X/A=a/(1+i omega theta); x_DC=a Q0+d. If Re H=xh>0 then

 theta=-Im H/(omega Re H), a=|H|^2/Re H,
 d=x_DC-a Q0.                                        (7)

These exact formulas uniquely identify this restricted channel. A velocity
channel requires its own known W_ref=Q_ref' and positive gain/offset calibration;
equality of fitted response times/alignment is testable, not assumed by notation.
A second independently known nonzero frequency tests the SAME a,theta and
transfer law; disagreement invalidates the first-order model. This is a
prospective reference procedure, not measured calibration or a request to
contact anyone. Dataset README supplies no such reference/preparation record.

Unknown additional delay Delta changes H to a exp(-i omega Delta)/(1+i omega
theta). At ONE tone, for any candidate theta>=0 choose
a=|H|sqrt(1+omega^2 theta^2) and a delay modulo2pi/omega to match its phase.
Thus one tone no longer identifies theta,a,Delta; independent delay restriction
or sufficiently specified multi-frequency experiment is necessary. Even exact
two-tone measurements have delay aliases if frequencies are commensurate.
DC-only (omega=0) cannot identify theta. At theta=0 the same inverse formula
works with real H if direct response is explicitly admitted, but positive
theta cannot be confirmed at finite uncertainty. With no independently fixed
SI reference frequency, only the corresponding frequency-time product is
calibrated, not seconds per BFG event. Device transfer calibration alone still
does not supply a canonical state, Pi, preparation or event label.

For a convex complex-transfer uncertainty rectangle Re H>=r>0,|Im H|<=B,
and independently exact omega, differentiating (7) and integrating on the
segment gives the reproducible bounds
|delta theta| <= B|delta Re H|/(omega r^2)+|delta Im H|/(omega r),
|delta a| <= (1+B^2/r^2)|delta Re H|+2B|delta Im H|/r.   (8)
Frequency uncertainty requires its own term: on omega>=omega_min>0,
|partial theta/partial omega|<=B/(r omega_min^2).
Small r/low omega cause adverse conditioning; uncertainty cannot be replaced
by printed digits. Likewise unknown initial memory transient contributes
exp(-t/theta) times its unknown initial size, requiring a prior bound and
settling rule. No unmeasured errors are set to zero to rescue P69.

## Whole-source/other-level search and actual status

The accompanying whole-paper search included spectral/gauge/polar/SVD chain,
cross-load balance86(144)–(145), formation/loss/seed86(146)–(147), spectral
diversity86(148)–(149), historical witness86(150), finite seed capacity87(152),
autonomous scalar88(153)–(154), driven88(155)–(156), viability/transverse
88(157)–(158), independent mediator88(159), factors/clocks89 and typed lifts90.
They supply canonical/domain/accounting constraints, not instrument histories
or independently calibrated physical reference records. Frozen scalar
contraction16/27 is not a bound on this endogenous sensor/plant map; driven
input d is a different declared extension, and the old Abel clock cannot be
assigned to its fixed point. No scalar no-go is a universal BFG limitation.

Alternative compatible level: on full persistence lift L_m of90(163)–(164),
put Pi_theta,m(L_m Xi)=T_theta Pi(Xi), keeping the SAME two instrument memory
states, not m independent experiments. Then lifted return/clock is exactly
R_theta,C_theta and (6) on base directions. Kernel formation stock and witness
normalization remain preserved, ambient/persistent ranks multiply by m, while
sensor-state projection still lacks closure unless memory/jet is supplied.
Seed replication may terminate T_seeddeg; no sensor dynamics is called a seed.
Taking a Cartesian product with the four-state instrument equations is an
explicit measurement extension with external initialization; it is not the
paper's tensor law. Neither transition manufactures independent measurements,
reduces error by replica labels, or proves physical fractality.

PROVED under assumptions: extended/jet ranks, defect decay, exact nonlinear
rank-two conjugate closure, return/tangent/energy transfer, harmonic passive
nonidentifiability, and restricted reference inverse/error bounds.
ADDITIONAL HYPOTHESES: actual response law, response time, gain/delay/errors,
true physical angle/force/preparation and event clock. The pinned metadata
does not supply their independent calibration. No actual response time or
force law is newly identified. Next necessary dependency: independently
restricted preparation/response/reference evidence OR a separately justified
finite-dimensional response family with an explicit identifiable multi-channel
calibration/preparation design; establish rank and uncertainty before any new
development fit. Physical force selection, SI event durations, inertia, energy
scale and causal interventions remain OPEN; P69 failure is preserved.
