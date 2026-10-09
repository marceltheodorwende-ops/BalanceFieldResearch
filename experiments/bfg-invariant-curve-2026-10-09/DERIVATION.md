# P62 — Positive nonanalytic invariant curves and exact 2D event closure

## Claim, assumptions, and completion rule
Construct a positive C1 invariant curve t=T(x) inside the exact P60/P61
amplitude surface; prove complete nonlinear invariance, seam regularity,
endpoint behavior and an interior rank-two event factor. Independently check
the algebra and the fundamental-segment construction, publish these controls
and verify the register and both ledgers. This closes this discrete-curve
dependency, not the physical pendulum, continuous generator or force law.

Sole source: Dynamic Order, 8 October 2026, 144 pages, SHA256
1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba.
Source locations: Part I 62–64 (complete regular differential chain),
83 (121)–(123) (types and quotient), 84 (124)–(140) (all event gates),
85 (141)–(143) (full-persistence geometry), 88.3 (157) (viability),
89 (161)–(162) (factor and clock), 90 (163)–(164) (conditional tensor lift).
Dependencies: P53/P54 quotient formulas, P57 forward gates, P59 jets,
P60 exact surface and P61 C1,1 regularity. All are retained.

Retain the explicitly additional, fixed commutator preparation
D=eta*i[Y,J], eta!=0, J=K/kappa, P=I, formation=fI, f>0;
the geometry anisotropy is perpendicular to J and a non-scalar inherited
witness supplies relative phase phi. No mechanical motion is inserted.
The preparation is a hypothesis, not the autonomous kernel. All coordinates
t,x,q,z,phi are dimensionless. No seconds, inertia, energy or force calibration.

Write Z=Z*(t,x) for P60's exact surface. Put q=sqrt(x)Z, x=4eta²s²,
a(t,x)=A(t,q), X(t,x)=x*g(t,q). Here A and g are the canonical quotient
functions, not freely chosen vector fields. The exact surface satisfies
F(t,x,Z)=Z(a,X), with F=z B(t,q)sqrt(1/g+x).
P61 gives Z=1+O(t), bounded Z_t and Z_x=O(t), locally C1,1.

## Uniform local inequalities and invariant tangent cone
The rational g is even in q and g(t,0)=1. It therefore has the exact
factorization g(t,q)=1-q² H(t,q²), where H is analytic near (0,0)
and H(0,0)=1. Consequently

 X=x-x² Z² H(t,x Z²).                                      (1)

P61 and the analytic A give uniformly, after shrinking a closed rectangle,

 a=2(1+x)t²+O(t³), a_t=4(1+x)t+O(t²), a_x=2t²+O(t³),
 X_t=O(x²), X_x=1-2x+O(tx+x²).                            (2)

The t-derivative remainder in a is controlled using bounded Z_t; the
x-derivative uses Z_x=O(t). Thus these statements do not differentiate
an uncontrolled asymptotic expansion. Choose finite C>=1, c_+>=c_->0,
and restrict 0<t<=epsilon, 0<x<=delta so

 0<a<=Ct²<t, 0<a_t<=Ct, 0<a_x<=Ct²,
 |X_t|<=Cx², X_x>=3/4, c_-x²<=x-X<=c_+x²,
 Cdelta²<=1/4, 2C(epsilon+epsilon²)<=1/2.                 (3)

Such constants and radii exist by (1)–(2); choose Cepsilon<1/2,
c_+delta<1/2 as well, and retain every P57/P60/P61 domain restriction.
These are mathematically specified bounds, not numerically certified sample
radii or measurement calibrations. They ensure X>0 and forward invariance.

For a graph with slope 0<=m<=1, its image has denominator
X_x+X_t m>=1/2 and slope

 m_new=(a_x+a_t m)/(X_x+X_t m).                            (4)

Hence 0<m_new<=2Ct²+2Ct m<=1/2. The cone [0,1] is forward
invariant, and the x-coordinate along every such graph is strictly
increasing. This is a cone for tangent transport, not a full-state
Lyapunov stability claim. It avoids assuming that a local diffeomorphism
is onto the rectangle or that arbitrary curves remain graphs.

## Exact fundamental segment
Fix any sufficiently small x0>0. Choose t0>0 sufficiently small relative
to x0², within the rectangle. Let (t1,x1)=(a(t0,x0),X(t0,x0)) and
set D0=(t0-t1)/(x0-x1)>0. Since x0 is fixed, D0 tends to zero
as t0 tends to zero; demand D0<=1/2. Set m0=D0 and

 m1=(a_x(t0,x0)+a_t(t0,x0)D0)/(X_x(t0,x0)+X_t(t0,x0)D0).

This is the image slope required at the lower endpoint, not an independent
choice. From (3), D0>=t0/(2c_+x0²), so
m1/D0<=2Ct0+4Cc_+t0 x0². Shrink t0 so 0<m1<=D0.
Put u=m1/D0, v=(x-x1)/(x0-x1), and define the seed graph on [x1,x0]:

 T0(x)=t1+(t0-t1)[(u-1)v³+2(1-u)v²+u v].                (5)

It has the required endpoint values and slopes T0'(x1)=m1,
T0'(x0)=m0. Its derivative divided by D0 is
u+(1-u)(4v-3v²), which lies in [u,4/3] for 0<=v<=1.
Thus T0 is positive, increasing, and its slope is <=2/3.
The image tangent at the upper endpoint agrees EXACTLY with the seed
tangent at the lower endpoint. No approximate jet substitutes for invariance.

## Propagation, gluing and endpoint proof
Let p_n=(t_n,x_n)=U_surface^n(p0). Define the nth graph segment
C_n=U_surface^n(C0), over I_n=[x_{n+1},x_n]. The invariant cone,
strict positive x derivative, and ordered endpoints prove inductively that
each image is a single C1 graph over exactly that interval. Its t maximum
is t_n and minimum t_{n+1}. Distinct interiors of I_n do not overlap.
At every shared endpoint the derivative matches: the initial tangent
match is transported by the same derivative DU_surface^n. Equivalently,
the chain rule applied to (4) sends both endpoint slopes to the same slope.
Thus their union defines a C1 graph T on (0,x0]. By construction

 T(X(T(x),x))=a(T(x),x),                                 (6)

on EVERY point, including seams. This is exact nonlinear invariance of
the exact surface; no finite-depth numerical graph is asserted to be exact.

The scalar x decrement in (3) gives x_n decreasing to zero, since a
positive limiting x would give a nonzero decrement. Moreover

 c_- <= 1/x_{n+1}-1/x_n <= 2c_+.

The upper bound uses x_{n+1}>=x_n(1-c_+delta)>=x_n/2.
Therefore x_n is bounded above and below by constants times 1/(n+1).
For rho=Ct0<1, induction gives t_n<=C^-1 rho^(2^n).
For every p>0 and x in I_n, T(x)<=t_n and x>=x_{n+1}; hence
T(x)/x^p ->0. Values are flatter than every positive power.

If M_n is the maximum slope on C_n, (4) gives
M_{n+1}<=2Ct_n M_n+2Ct_n². As M_n<=1, M_n->0.
Extend T(0)=0. The value bound with p=1 gives T'(0)=0;
the slope bound proves derivative continuity there. Thus T is C1 on
[0,x0], positive for x>0, with values flat to every order. It cannot
be real analytic at zero: analyticity and all-power value flatness force
every Taylor coefficient to vanish and the function to be locally zero.
We do NOT claim C2 or C-infinity at zero from these estimates.

## Exact two-dimensional factor and tangent
Reconstruct the quotient state from (x,phi) using
t=T(x), q=sqrt(x)Z(T(x),x), s=sqrt(x)/(2|eta|),
r=tq/sqrt(1+x), and the declared inherited witness/formation family.
The phase is a relative quotient observable, not an SVD frame phase.
Canonical evolution preserves the curve by (6), the surface by P60,
and the witness family by P53/P54. Therefore the restricted full return is

 (x,phi) -> (P(x),phi+sigma atan(sqrt(x))),
 P(x)=X(T(x),x), sigma=sign(eta).                         (7)

It satisfies the source (161) fiber criterion; no hidden amplitude remains
on this selected family. Here 0<P(x)<x and the phase increment is nonzero:
both observable directions evolve. The exact tangent, in (x,phi) order, is

 [[X_x+X_t T',0],[sigma/(2sqrt(x)(1+x)),1]].               (8)

Its determinant is >=1/2 on the chosen positive domain. This is a regular
two-dimensional DISCRETE local diffeomorphism. Its phase derivative
diverges toward x=0, and zero is still a canonical load terminal with
undefined phase/axis. No regular extension of the physical event across
that endpoint is claimed. The constructed curve derivative also obeys
T'(P)P'=a_x+a_t T', exactly the P61 tangent equation.

## Nonuniqueness, force, units and conditioning
The curve is not selected uniquely by the kernel. On the seed interval
add a sufficiently small nonzero smooth bump supported away from its
endpoints. Because T0' has positive minimum and maximum <1, its slope
remains in [0,1], its endpoint values and jets remain identical, and it
stays positive. Propagation gives a DIFFERENT exact C1 invariant curve
with the same orbital seams. There are infinitely many such choices.
Thus this construction supplies a carrier but not an independent physical
preparation/selection rule. It does not prove that no other BFG candidate
can select a force.

Neither (7) nor its tangent determines a continuous generator or sine
torque. Source (162) requires independently calibrated event durations
and exact flow matching. For any proposed continuous realization, replacing
seconds tau by c*tau changes velocity by c^-1 and acceleration by c^-2
without changing any canonical event or dimensionless observable here.
Energy scale and inertia likewise require additional measured bridges;
formation balance (147) is not a mechanical energy equation. Even before
clock nonuniqueness, the bump construction is a concrete internal freedom
in the physical carrier. The force-law selection claim remains OPEN.

Stability investigated here is forward graph/cone preservation and seam
regularity on (3), with bounded seed-slope perturbations as above. It is not
uniform robustness of physical predictions or a Lyapunov theorem for the
full state. The embedding becomes ill-conditioned as t tends to zero:
geometry anisotropy r tends to zero super-exponentially, erasing phase
under finite measurement resolution. The x phase derivative in (8) is
unbounded. No experiment or improved development score is reported.

## Accompanying whole-source audit and verification
Search of the complete active source supports this one dependency:
83–85 fixes types, gates and quotient; Part I 62–64 supplies all endogenous
tangent terms; 86's load/formation/entropy/witness balances do not impose
a unique curve or torque; 87 prohibits undeclared persistent seed growth;
88.1's scalar damping does not settle the matrix problem; 88.2 is a different
declared input; 88.3 supplies the viability distinction; 88.4 mediator ODEs
cannot be substituted as canonical generators; 89 requires independent
continuous-flow/clock closure. On 90's admitted full-persistence tensor
family (164), replication of this reconstruction and preparation preserves
the event and rank-two factor in normalized base coordinates. It does not
justify arbitrary nonreplicated inputs, seed degeneracy, spatial fractality
or a hierarchy inferred from time aggregation. No lift is needed here.

Frozen controls: symbolic g factorization and leading terms; exact Hermite
endpoint/tangent algebra and monotonic derivative bound; finite positive
quotient orbit and tangent-cone/seam controls using the archived P59
second jet ONLY as a numerical approximation. Independent matrix events
verify quotient amplitudes and phase at sample states. Numerical samples
are synthetic code controls, not exact-surface/radius certificates or data.
The general theorem is (1)–(8), not sample convergence.

Observed controls: 16 symbolic checks passed; all three 80-digit seed
tangent seams matched, all 303 sampled cone slopes satisfied the frozen
bounds, and all three ten-event approximate orbits retained positive
decreasing amplitudes. Three independent complete Ambient events agreed
with quotient amplitudes and phase to <=1.07e-14 (tolerance 1e-10).
These checks do not calibrate the exact local radius. The first control
invocation was stopped after roughly 90 seconds without a result because
global symbolic cancellation of substituted rational jets caused excessive
expansion. Retaining the identical factored expressions removed that
computational bottleneck; the completed run passed. No model, tolerance,
data, or hypothesis was changed, and no empirical failure was discarded.

PROVED under declared preparation and local domain restrictions: positive
nonanalytic C1 invariant curves, exact full nonlinear 2D event closure,
regular interior tangent, and nonuniqueness of the selected family.
OPEN next dependency: continuous flow matching and an independently
justified physical selection/clock rule, then force, energy and interventions.
Holdout remains closed; no real-data claim. Publication and verified ledger
entries are required before this package is called complete.
