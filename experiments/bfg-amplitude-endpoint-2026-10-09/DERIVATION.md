# P55: endpoint obstruction for analytic amplitude graphs

## Claim fixed before analysis
Dependencies P53/P54. Test an invariant graph t=T(s), r=R(s)>0 retaining
the witness phase, with T,R real analytic at a finite endpoint s*=0 or s*>0,
T(s*)=0 and T not identically zero. For s*>0 require that the successor
parameter tends to the same endpoint. Require the strict prepared gate and
successors in the graph domain. We prove this class empty. This is not a
claim against all invariant curves, all C1 curves, or all BFG carriers.
Completion requires the proof, independent symbolic/numerical checks, recorded
limits, and verified publication/register entries. No empirical test is needed
for an impossible graph class; no holdout access is authorized here.

## Source and model
Only Dynamic Order is active: sections83–85, equations124–138 supply the
unchanged full-persistence event; PartI62–64 its regular differential chain;
section89(161) requires factor closure; 88.3(157) requires forward viability.
P54 derives the exact formulas used below from that event. Preparation is the
EXTRA hypothesis D=eta*i[Y,J], J=K/kappa, eta fixed and dimensionless.
H=C2, P=I, F=fI with f>0, Y=tI+y.sigma, J=j.sigma, y perpendicular j,
r=|y|, s=|j|. The non-scalar witness supplies phase as in P54, not a new
external reference. All graph variables dimensionless, kappa carries kernel
units; no seconds, energy in joules or torque calibration is supplied.

Set h=r*sqrt(1+4 eta²s²), u±=t±h, c±=1/(1+u±), b±=u±c±,
m=t²+h²(1-t)/(1+t), alpha=m/(1+m), beta=1/(1+m),
a±=alpha*c±²+beta*b±², A=(a++a-)/2, V=(a+-a-)/2,
G=(alpha*c+c-+beta*b+b-)/sqrt(a+a-).
The exact graph obligations, not an approximate flow, are

    S(s)=s G(T(s),h(s)), T(S(s))=A(T(s),h(s)),
    R(S(s))=V(T(s),h(s)), phi+=phi+atan(2 eta s).

Gate: 0<h<t and t+h<1. P54 proves V>0 and 0<G<1 on it.
Gauge-invariant t,r,s ensure the graph is representation independent.

## Proof
Write q=h/t in (0,1). Uniformly for q in [0,1] as t tends to zero,

    A/t² -> 2(1+q²), V/t² -> 2q,
    G -> g(q)=1/sqrt(1+q²+q⁴).

These follow by substituting h=tq in the rational formulas; the square-root
denominator divided by t² stays positive, including q=1. In particular A=O(t²)
and g(q)>=1/sqrt(3). Analytic nonzero T has finite vanishing order p>=1,
T(s)=a(s-s*)^p(1+o(1)) on the selected one-sided domain. The gate makes
R vanish with order k>=p, unless identically zero, which loses phase and is
excluded. Thus q has a limit q0 in [0,1].

If s*=0, S(s)/s -> g(q0)>0. Hence T(S(s))/T(s) -> g(q0)^p>0,
whereas A/T ->0. This contradicts the first geometry invariance equation.

If s*>0, endpoint preservation S(s)->s* forces g(q0)=1, hence q0=0
and k>p. Therefore q=O(|s-s*|), not just o(1). The exact G(t,tq)
is even analytic in q near (t,q)=(0,0), equals1 at q=0, and has bounded
second q derivative there. Consequently 1-G=O(q²)=O((s-s*)²).
Writing delta=s-s*, S(s)-s*=delta+O(delta²). Then
T(S(s))/T(s)->1, again contradicting A/T->0. QED.

This also excludes finite-order analytic preparations ending at a positive
stationary kernel while geometry vanishes; it does not prove that every orbit
has that endpoint. If S fails endpoint preservation, this theorem's positive
endpoint case does not apply and the proposed endpoint is not an orbit limit.

## Controls, counter-limits, and next dependency
Symbolic limits below are independent of Ambient implementation. Numerical
checks use 80-digit arithmetic to avoid small-geometry rank thresholds and
subtractive cancellation. They corroborate asymptotics, not graph nonexistence.
No robustness of physical predictions is claimed. Analytic endpoint regularity
is an additional restriction, not an axiom in the paper. Flat/nonanalytic
graphs and domains away from this endpoint remain possible; R=0 is the exact
scalar branch but its phase is undefined. A fixed positive geometric endpoint
is not covered (would require a separately declared driven model).

Sections86–87 balances/entropy/seed capacity do not impose an amplitude graph
or a physical sine law. Section88.2's constant scalar input is a different
model, so its positive fixed point cannot repair these equations unchanged.
Section90(163)–(164) permits full-persistence tensor replication: with normalized
tensor formation/witness, channels, loads and A,V,G agree with the base;
the commutator preparation tensor-lifts. Restricting a lifted graph to the
replicated family returns the same obstruction; new nonreplicated directions
require a new declared carrier and do not fall under this theorem.
The regular differential chain controls interior derivatives, not analytic
extension through zero-load boundaries. Neither a clock change nor invertible
pair calibration changes these exact graph equations. Thus no physical force
law follows from this candidate, and sine selection/seconds remain OPEN.

Status: proved conditional exclusion of this analytic endpoint class only.
Next necessary solvable dependency: nonanalytic invariant amplitude curves
with an explicit forward gate (or an independently constrained alternative
carrier), and their actual two-dimensional closure before flow/clock/force.
The parent invariant-curve obligation is still OPEN, not renamed completed.
