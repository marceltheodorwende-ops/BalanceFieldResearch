# P66 — Restricted geometric observation: exact force closure and its limit

## Statement fixed before controls
Investigate the next P65 dependency, a restricted observation/preparation family,
by deriving its exact force-class compatibility before any empirical fit.
Claim: on an open two-dimensional regular patch of the selected P62/P63
nonlinear canonical-return realization, a single geometric phase harmonic
cannot obey the full damped sine pendulum law with nonzero restoring coefficient.
Derive necessary and sufficient harmonic-force conditions, rank, error bounds,
and the precise interface required of an alternative nonlinear observable.
Completion: proof and boundary/counterexample audit; independent symbolic and
synthetic controls; publication and exact register/both-ledger verification.
This closes this restricted-family investigation, not physical pendulum closure.

Sole source: The Balance Field Equation: Dynamic Order and Recursive Structure
Formation,8October2026,144pages,SHA256
1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba.
Dependencies: P60–P63 exact selected family and interpolation; P65 instrument
and observation audit. No new empirical model, recording or fit in this package. A local control initially
used the opposite orientation sign for the observation determinant; the direct
symbolic check rejected it. The sign was corrected before publication, and
all controls were rerun. Rank conclusions are unaffected; this failed control
is retained in this note.

## Source search and model boundaries
Part I22–23(87)–(91),73.1 and Part II89(161)–(162) require actual factor
closure, terminal consistency and independently calibrated time. Part I62–64
and Part II84–85(124)–(143) supply regular differential/quotient rules; they
do not identify angle, seconds or inertia. P62's invariant curve is an exact
chosen nonlinear return family after the explicitly additional commutator
preparation; P63 selects a compatible between-event interpolation. These
choices remain hypotheses rather than unique physical preparation rules.

The companion search covered the complete text including matrix updates,
gauge, differential chain, loads, formation-loss-seed(146)–(147), spectral
entropy/diversity(148)–(149), historical witness(150), finite seed capacity(152),
autonomous scalar(153)–(154), driven scalar(155)–(156), viability/transverse
certificates(157)–(158), independent continuous mediator(159), factors/clocks,
and typed lift(163)–(164). The load and stock identities do not specify a
mechanical potential or SI energy. Spectral/historical readouts can constrain
preparation only through an additional instrument identification. The declared
scalar input changes the return and clock equation; it is not inserted into
P63 here. A separate continuous mediator is not this generator. Full-persistence
lift is compatible but preserves the obstruction through normalized base
readouts; seed replication can terminate and cannot bypass it. These limits
select a nonlinear observable as the next necessary dependency, rather than
new uncalibrated inputs, scalar impossibility claims, or arbitrary hierarchy.

## Explicit assumptions and types
Fix an interior rectangle I x J of the P63 carrier, with x>0, nonterminal
canonical states and fixed preparation/interpolation. In event-time lambda,
L=v(x) partial_x + omega(x) partial_phi, v<0, v,omega C1. Extra regularity
is not inferred from P63's general locally Lipschitz conclusion. Assume a
constant c>0 seconds/event, tau=c lambda, requiring independent calibration.
Fix Q=q0+A(x)cos(phi+psi(x)), A>0 C2, psi C2, q0 constant.
This geometrically motivated relative-phase readout is an EXTRA observation
hypothesis, not a physical angle measured by the paper. q0,A,phi,psi,x are
dimensionless (radians); V= LQ/c has s^-1 units and R=L²Q/c² has s^-2 units.
Define theta=phi+psi(x), Omega=omega+v psi'; Omega is C1.
Changing coordinates to (x,theta) has determinant one and changes L to
v partial_x + Omega partial_theta. No canonical update is changed.

## Exact chain rule and two observable directions
Put B=v A', C=A Omega. Then
 V=(B cos(theta)-C sin(theta))/c,
 R=(D cos(theta)-E sin(theta))/c²,
 D=v² A''+v v' A'-A Omega²,
 E=2v A' Omega+v A Omega'.                                      (1)
The two physical-channel directions have determinant
 det D(Q,V)=[(A B'-A' B)sin(theta)cos(theta)
             -A' C cos²(theta)-A C' sin²(theta)]/c.             (2)
The coordinate shear leaves this determinant unchanged. Nonzero determinant
allows local inversion of G=(Q,V) and exact local normal form
 Qdot=V, Vdot=R(G^-1(Q,V)). It establishes neither global inversion nor a
physical preparation/calibration rule. A constant A and constant Omega gives
rank<=1; amplitude decay can instead give rank2 even at turning points.

## Full sine-force obstruction, including local patches
Suppose R=-kappa sin(Q)-gamma V holds on a nonempty open carrier patch,
with kappa!=0 and any constants gamma,c. Choose a fixed interior x with an
open theta interval. After bringing terms together, the left side is a first
harmonic: a cos(theta)+b sin(theta). The right side is a nonzero multiple
of sin(q0+A cos(theta)). Both sides are real analytic functions of theta,
so interval equality implies equality for all real theta. Comparing theta
and -theta eliminates b. Thus sin(q0+A z)=p z for all z in[-1,1]. Taking two
z derivatives gives -A² sin(q0+A z)=0 throughout(-1,1), impossible for A>0.
The same argument allows an added constant torque (affine rather than linear
right-side function in z). It does not rely on Omega!=0 or observation rank;
it therefore also rules out purported rank-degenerate escapes on open sets.

This is a genuine full nonlinear closure obstruction for the declared
single-harmonic observation, including state-dependent radial phase shifts.
It is not a no-go theorem for other BFG carriers, arbitrary nonlinear q(x,phi),
state-dependent clocks or additional physical couplings. Equality along one
trajectory or finitely many sample nodes does not imply open-set closure.
A=0, kappa=0, a single point, or the small-angle LIMIT escapes an assumption;
none establishes a regular finite-amplitude sine-law realization.

## What linear forces this family can actually support
For a centered harmonic rival R=-kappa(Q-q0)-gamma V, equality on an open
phase interval is equivalent, pointwise in x, to the two identities
 D=-kappa c² A-gamma c v A',
 E=-gamma c A Omega.                                           (3)
Necessity follows from independence of sine/cosine; sufficiency follows by
substitution in(1). No division by Omega is needed, so its zeros are covered.
Where Omega!=0 the second identity is
 v(2 A'/A+Omega'/Omega)=-gamma c.
If u=N(x), Lu=1, this says d_u log(A² |Omega|)=-gamma c, hence
 A² |Omega|=constant exp(-gamma c u) on each connected nonzero-Omega interval.
This is a conditional restriction, not a value of gamma or a calibration of c.
The first identity is a second compatibility condition and cannot be discarded.
Under Omega!=0, (1) can also be written R=k(x)(Q-q0)+ell(x)V, with
 ell=E/(A Omega c),
 k=[D-E v A'/(A Omega)]/(A c²).
State-dependent k and ell yield an autonomous local force only after G inverse;
they are not constant linear parameters just because a good mean fit exists.

A positive mathematical control exists: in coordinates u with Lu=1, choose
A=a exp(-delta u), Omega=nu!=0, delta>=0. Then gamma=2delta/c,
kappa=(delta²+nu²)/c² satisfies(3), and det D_u,theta(Q,V)=delta A² nu/c.
It is rank2 for delta>0, rank1 for delta=0. On the actual selected P63
flow a declared radial phase shift psi=nu N-b gives Ltheta=nu, while
A=a exp(-delta N). Thus it gives an EXACT conditional harmonic factor, including
the canonical event endpoints, rather than changing the canonical phase law.
The original phi increment remains sign(eta)atan(sqrt(x)); only the chosen
observable phase theta advances by nu. In u,theta the event is
(u,theta)->(u+1,theta+nu). Hence Q,V undergo exactly the time-c damped
harmonic factor. Its explicit event matrix on (Q,V), taking q0=0, is
 exp(-delta) [[cos(nu)+delta sin(nu)/nu, c sin(nu)/nu],
 [-(delta²+nu²)sin(nu)/(c nu), cos(nu)-delta sin(nu)/nu]].
For q0!=0 use Q-q0. Differentiating the exact factor identity gives
 DG(U state) DU = M DG(state), hence the factor tangent dynamics is also exact
on regular charts. M=exp(c [[0,1],[-kappa,-gamma]]). This checks the full return,
not just a frequency fit. N,b are C1 from P63; along-flow derivatives for this factor
are smooth by the exact flow identities even where carrier second derivatives
are unavailable. Ordinary formulas(1) apply on the additional smooth patches.
The transformation (x,phi)->(u,theta) has determinant N'!=0; multiplying by
that determinant preserves rank2 in carrier coordinates for delta>0,nu!=0.
This construction deliberately installs freely chosen delta,nu and a in a
readout: it is a calibrated harmonic representation, category(c), NOT an
internal force derivation or physical selection. It preserves P65's finite
calibration ambiguity. With psi=0, constant omega would instead conflict with
the actual varying canonical phase increment; these cases must not be confused.
A clock rescaling c->r c rescales gamma->gamma/r,kappa->kappa/r² for the
same dimensionless factor. No observations in this package determine r.

## Robustness and energy under stated assumptions
Before numerical controls, define the tested structural stability as persistence
of exact open-set closure under admissible C1 v,Omega and C2 A perturbations
that retain A>0 and constant c. The sine obstruction persists throughout that
entire class; numerical error or tiny amplitude cannot make it an exact law.
This is structural incompatibility, not a trajectory-stability theorem.
If harmonic conditions(3) hold with kappa>0,gamma>=0, the EXTRA inertia scale
I>0 defines Ephys=I[V²/2+kappa(Q-q0)²/2], with derivative -I gamma V².
This supplies Lyapunov nonincrease for the hypothetical harmonic factor;
I and joule calibration remain unidentified. It is not the formation stock.
For a harmonic approximation to a sine rival at |Q|<=a, |sin Q-Q|<=|Q|³/6,
so restoring acceleration error<=|kappa|a³/6. This pointwise bound is not a
long-horizon prediction guarantee; accumulated phase error and instrument
uncertainty remain unresolved. No empirical robustness claim is made.
Scaled observation uncertainty requires a positive singular-value margin and
validated errors as P65 explains; three printed decimals are not that evidence.

## Required alternative nonlinear observation interface
For q(x,phi) C2 and v,omega C1, the next prospective candidate must satisfy
 L²q=v² q_xx+v v' q_x+2v omega q_xphi+v omega' q_phi+omega² q_phiphi,
 L²q+gamma c Lq+kappa c² sin(q)=0,
 det D(q,Lq/c)!=0,                                            (4)
with a physically justified preparation and fixed shared parameters, calibrated
c, instrument model and exact event relation G(U state)=flow_c(G(state)).
Equation(4) is a necessary and, locally with rank and unique smooth factor flow,
sufficient mechanical-factor interface. It is a PDE that imposes the sine law
as a constitutive hypothesis; solving it alone is not an internal derivation
or independent selection of that law. If R only continuous, additional local
uniqueness regularity for a general factor must be checked; the specific sine
vector field itself is smooth. Terminals and chart boundaries remain separate.
A nonharmonic q or phase-dependent dynamics/clock is a mathematically justified
way to escape this obstruction, but requires a new explicit candidate, not a
free test-dependent correction. This package does not claim to solve that PDE.

For a compatible full-persistence tensor lift L_m, define q_m(L_m state)=q(state)
and keep normalized invariants, c and V. The base pullback of (4) is unchanged;
rank in the two base directions and the sine obstruction are unchanged. Lift
copies add labels, not independent measured directions, clock information or
physical fractality. Gauge invariance follows from the inherited quotient
coordinates; independent absolute basis angles would violate that assumption.

## Controls and proof status
check.py independently differentiates the generic observation and generator,
checks determinant, elimination formula, both linear conditions, positive
control and energy, and proves the sine residual cannot be first harmonic by
the derivative of (partial_theta²+1)sin(Acos theta) at theta=pi/2: A³!=0.
That diagnostic is supplementary to the general q0 proof above. Two independent matrix-exponential controls check the exact event factor
against its explicit Q,V return matrix. Numerical
quadrature compares the third harmonic with -2 J3(A), and verifies the cubic
small-angle bound for three declared synthetic amplitudes. No real measurements
or holdout are touched, no fits or new workflows are launched.
Status: PROVED under assumptions, single-harmonic full-sine closure impossible;
PROVED conditional linear compatibility/rank/error/energy formulas; physical
preparation, seconds, nonlinear observation and sine-law selection remain OPEN.
Next necessary solvable dependency: construct a nonharmonic quotient observable
for the fixed return, with preparation/shared-parameter selection and exact
factor interface, or prove its scoped obstruction before fitting development
measurements against strong nonlinear mechanical rivals. Preserve P65's
instrument blockade and every earlier positive/negative empirical result.
