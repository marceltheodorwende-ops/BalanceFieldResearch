# P60 — Exact local invariant amplitude surface by a weighted pullback

## One active dependency and precise status
P59 left the exact amplitude surface open after two polynomial jets failed exact
invariance. We construct that surface locally for the SAME fixed commutator
preparation, prove convergence and a remainder certificate. This closes this
surface-existence dependency only. The positive nonanalytic curve t=T(s), its
regular two-dimensional return/generator and physical force/clock remain OPEN.
The result is a Lipschitz surface with a uniform two-jet asymptotic expansion;
it is not a claim of a globally smooth manifold or a physical pendulum.

## Source, preparation and types
Sole active source: Dynamic Order, 8 October 2026, 144 pages, SHA256
1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba.
Sections83(121)–(123),84(124)–(138),85(141)–(143) supply the canonical
matrix event and quotient. PartI62–64 supplies interior differentials;
88.3(157) distinguishes viability from a static gate;89(161)–(162) demands
exact factor/clock closure;90(163)–(164) supplies conditional tensor replication.
Dependencies P53/P54 exact orthogonal quotient, P57 forward gate, P58/P59.

Keep H=C^2,P=I,F=fI,f>0,K=kappa J,J=j.sigma, Y=tI+y.sigma,
y perpendicular to j; fixed non-scalar witness perpendicular to j records phase.
The explicitly EXTRA preparation D=eta*i[Y,J], eta!=0, precedes each event.
J,Y,eta,t,r,s are dimensionless; kappa converts kernel units. No physical
energy, mechanical equation, fitted constant or new control is introduced.
Put k=2|eta|, s=|j|, x=k^2 s^2, q=h/t, h=r sqrt(1+x), z=q/sqrt(x).
Use x>0,t>0 physically; the axes below are canceled coordinate extensions.

For u_±=t(1±q), c_±=1/(1+u_±), b_±=u_±c_±, define

 m=t²+(tq)²(1-t)/(1+t), alpha=m/(1+m), beta=1-alpha,
 e_±=alpha c_±²+beta b_±²,
 A=(e_++e_-)/2, V=(e_+-e_-)/2, B=V/(Aq),
 g=(alpha c_+c_-+beta b_+b_-)²/(e_+e_-).

Cancel rational expressions BEFORE using t=0 or q=0; A,B,g are even in q.
For q²=xz² define

 a(t,x,z)=A(t,q),  X(t,x,z)=x g(t,q),
 F(t,x,z)=z B(t,q) sqrt(1/g(t,q)+x).                 (1)

Thus the exact amplitude event is (t+,x+,z+)=(a,X,F), and
phi+=phi+atan(2eta s). Formula(1) has the positive root near z=1.
It is real analytic near t=0,x=0,z=1 after cancellation.
An invariant graph must satisfy EXACTLY

 F(t,x,Z(t,x)) = Z(a(t,x,Z(t,x)),X(t,x,Z(t,x))).      (2)

## Boundary identities and finite bounds
At t=0,z=1, for d=1+x+x²,

 a=0, X=x/d, F=1, F_z=d/(1+x)², F_t=-(2+x)d/(1+x)².

In particular F_z(0,0,1)=1, F_t(0,0,1)=-2, and F_x(0,x,1)=0.
Also a=t² times an analytic function, positive for t>0 locally, with
0<a<=C t², |a_t|<=C t, |a_x|+|a_z|<=C t².
These are identities/factorizations of the rational event, not fitted bounds.

Here is a rigorous radius specification without an invented numerical radius.
Choose 0<δ<1/9 and 0<ε0<1/4 small enough that on 0<=t<=ε0,0<=x<=δ,
1/2<=z<=3/2, F_z>=m=3/4, |F_t|<=4, denominators stay positive,
and 0<g<=1 on t>0, x>0, with the continuous values on axes.
Existence follows by the displayed identities at t=x=0, uniformly over the
compact z interval (there F=z, F_z=1, F_t=-2z).
Choose a finite C>=1 bounding the derivatives above, |X_t|,|X_x|,|X_z|,
and satisfying |F_x|<=C(t+|z-1|). The last estimate follows from
F_x(0,x,1)=0 and bounded F_xt,F_xz. Supremum bounds on the specified
compact box define such a C; this is not a numerical stability certification
for any particular experimental amplitude.

Set L=32, μ=m/2, M=4C(1+L)/μ. Choose 0<ε<=ε0 small enough that

 Lε<=1/2, sqrt(δ)(1+Lε)<1, ε<=1/2,
 Cε<=1/2, mL>4+LCε,
 LCε²+MC²ε²<=m/2,
 4+LCε+MC²ε²<=μL,
 C(1+L)+LCε+MC²ε<=μM,
 λ=Cε/μ<1, and C³ε³/μ<1.                         (3)

All inequalities can be satisfied: the constant terms have strict slack
(Lm=24>4, μL=12>4, μM=4C(1+L)>C(1+L)). Shrink δ first if needed.
Thus (3) specifies an actual nonempty local domain, with no claim that an
arbitrarily chosen numerical point has a certified radius. Include δ<1.
Nearby physical inputs obey P57 (choose chi=δ) and the strict prepared gate.

## Complete weighted graph transform proof
On D=[0,ε]x[0,δ], let K contain continuous graphs Z satisfying

 Z(0,x)=1, |Z(t,x)-1|<=Lt,
 |Z(t,x)-Z(u,x)|<=L|t-u|,
 |Z(t,x)-Z(t,y)|<=Mt|x-y|.

Equip K with d1(Z,W)=sup_{t>0,x}|Z-W|/t. It is complete: a d1-Cauchy
sequence converges uniformly, including on the boundary, and all displayed
closed inequalities pass to the limit. Z=1 and the sufficiently local P59
second jet belong to K. This norm is a graph-construction norm, not a physical
full-state norm.

For Z in K define TZ(t,x) as the unique root ζ in [1-Lt,1+Lt] of

 H_Z(ζ)=F(t,x,ζ)-Z(a(t,x,ζ),X(t,x,ζ))=0.           (4)

Both arguments stay in D: 0<=a<=Ct²<=ε and 0<=X<=x<=δ.
For ζ2>ζ1, the second term changes by at most
[LCt²+MC²t²]|ζ2-ζ1|, whereas F changes by at least m|ζ2-ζ1|.
Hence H_Z is strictly increasing with slope in the secant sense >=μ.
At the bracket endpoints, |F(t,x,1)-1|<=4t, F increases by at least mLt,
and |Z(a,X)-1|<=LCt². Inequality(3) gives opposite strict signs.
Existence follows from the intermediate value theorem and uniqueness from
strong monotonicity. At t=0 set TZ=1. Roots depend continuously on parameters.

Compare roots at two t values. At a fixed ζ, the t-Lipschitz bound on H_Z
is at most 4+LCε+MC²ε²; division by μ gives <=L. For two x values
at fixed t and ζ in the bracket, its x-Lipschitz bound is at most
[C(1+L)+LCε+MC²ε]t; division by μ gives <=Mt. Therefore TZ belongs
to K. Parameter comparisons may use the whole box 1/2<=ζ<=3/2;
the x estimate uses the common t bracket, and the t estimate uses box bounds.

For Z,W in K, compare (4) at W's root. Strong monotonicity gives

 |TZ-TW| <= μ^-1 |Z(a,X)-W(a,X)|
          <= (C/μ)t² d1(Z,W).

Consequently d1(TZ,TW)<=λ d1(Z,W), λ<1. Banach's theorem now gives
a unique Z* in K, with T Z*=Z*. By (4), this is an EXACT invariant graph(2),
not a polynomial jet, finite-time residual or a substituted external flow.
Its constructive iterates Z_(n+1)=T Z_n obey

 d1(Z_n,Z*) <= λ^n/(1-λ) d1(Z_1,Z_0).             (5)

Uniqueness is restricted to this local Lipschitz graph class; it does not
select eta, a physical initial state, a global continuation or every possible
singular amplitude surface.

## Certified relation to P59 and finite numerical controls
P59's Z2=1+(2+x)t+[P(x)/(1+x+x²)²]t², with
P=4x6+17x5+42x4+61x3+54x2+27x+6, has exact squared residual O(t³)
uniformly on this compact x interval. Shrink ε to keep Z2 in K.
Analyticity gives a finite E3=sup |F(t,x,Z2)-Z2(a,X)|/t³.
Strong monotonicity implies ||TZ2-Z2||_3<=E3/μ, where
||U-V||_p=sup |U-V|/t^p. The same argument used above gives

 ||TU-TV||_p <= λp ||U-V||_p, λp=C^p ε^p/μ.

Starting at Z2 and telescoping the convergent iterates proves

 |Z*(t,x)-Z2(t,x)| <= [E3/(μ(1-λ3))]t³.          (6)

Thus the exact surface inherits the two derived coefficients with a proved
uniform remainder order. This does not assert convergence of its full formal
Taylor series or differentiability in every variable. (5)/(6) are error
certificates with rigorously specified local constants; sampled numerical
residuals do not calibrate those supremum constants.

At the canceled x=0 axis, (2) additionally reduces to
Z(t,0)(1-t)/(1+t)=Z(A(t,0),0), so its bounded solution is the
convergent product product_j (1+t_j)/(1-t_j), t_(j+1)=A(t_j,0).
The quadratic t decay makes the sum of t_j finite and proves convergence.
This supplies an independent endpoint check, not a nonzero-kernel physical state.

Independent controls check boundary identities, 40 full Ambient events,
80-digit nested roots and preservation of P59 failures. Finite root-iteration
points are labeled computational controls; none is sold as a globally certified
physical preparation or a measured experiment. Terminal zero-load states remain
terminal, and x=0 loses kernel/phase observability.

## Exact factor interface, force, alternatives and levels
For positive t,x, the graph is an exact conditional invariant preparation
surface. Coordinates(t,x,phi) retain three observable degrees of freedom, with
return map (a(t,x,Z*),X(t,x,Z*),phi+sign(eta)atan(sqrt(x))).
It closes this three-coordinate discrete return by construction. Its Lipschitz
regularity alone does not establish the requested regular two-dimensional
continuous pendulum flow. Restricting t=T(x)>0 requires its OWN exact equation
T(X(T(x),x,Z*))=a(T(x),x,Z*). P55 excludes analytic zero-endpoint restrictions;
nonanalytic restrictions and the required regularity remain the next necessary dependency. No second
independent state variable is erased merely to get a desired dimension.

The phase increment has no phi-dependent sine restoring term. A smooth readout
and clock would still have to prove complete flow/force closure and physical
selection. Seconds-clock rescaling H->cH rescales any resulting acceleration by
c^-2; this dimensionless surface imposes no c. Inertia, calibrated energy and
interventions are not selected. A force in a subsequently chosen mechanical
readout would be an additional premise. No universal impossibility follows.

Whole-paper search:83–85 supplies exact dynamics;PartI62–64 supplies interior
chain rules, not regular physical axes;86 balanced loads/formation/witness and
entropy constrain accounting but supply no alternative mechanical selection;
87 excludes undeclared endless finite seeds;88.1's positive load boundary is
not repaired by a coordinate extension;88.2 constant input is a distinct model;
88.3 supports the P57 domain;88.4's mediator is not used as an event generator;
89 requires (2), and90 supports normalized full-persistence replication.
For D=eta*i[Y,J], replicated preparation is D tensor I. The full event commutes
with replication by(164); normalized geometric/kernel readouts recover t,x,z
on the replicated family. Thus the surface and its exact return transfer to that
family, preserving formation stock and witness normalization, multiplying rank,
and preserving terminal rules at positive geometry. Replication neither removes
the extra amplitude variable nor gives physical fractality. Nonreplicated
couplings and variable input would require a new declared transition and proof.

## Closure record
PROVED under the stated extra preparation and local graph bounds: an exact
unique Lipschitz amplitude surface in K, convergent construction and two-jet
remainder certificate. Numerical controls are separate from that theorem.
OPEN: positive nonanalytic invariant curve, regular2D flow, physical force,
energy/inertia, seconds and causal interventions. No real data or holdout opened,
no new empirical workflow/automation, no main merge or original-paper edit.
