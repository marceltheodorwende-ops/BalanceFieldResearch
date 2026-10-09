# P61 — C1,1 regularity and exact tangent of the P60 amplitude surface

## Active claim, hypotheses and closure criteria
Prove that P60's EXACT local invariant surface Z*(t,x) has continuously
Lipschitz first derivatives after restricting its domain, and compute its
canonical tangent/return rank. This is the regularity dependency needed before
constructing a positive nonanalytic t=T(x). Complete with a uniform derivative
argument, boundary/counterexample audit, independent controls, publication and
verified register/ledgers. We do not mark the 2D pendulum or force as solved.

Sole source: Dynamic Order,8October2026,144pages,SHA256
1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba.
PartI62–64 supplies the complete interior differential chain including witness
transport;83(121)–(123),84(124)–(138),85(141)–(143) supplies the canonical
quotient event;88.3(157) viability;89(161)–(162) factor/clock;90(163)–(164)
conditional replicated family. DependenciesP53/P54,P57,P59/P60.
Use unchanged extra fixed D=eta*i[Y,J],eta!=0,J=K/kappa, P=I,F=fI;
y perpendicular to j and a non-scalar witness records relative phase.
The extra preparation stays an assumption, not an autonomous-core theorem.
All amplitude/phase variables are dimensionless; no seconds, joules or torque
calibration is inserted.

Retain P60's canceled functions a(t,x,z), X=x g(t,q),
F=z B(t,q)sqrt(1/g(t,q)+x), q²=xz²; x=4eta²s².
They are analytic on the specified compact coordinate box; physically use t,x>0.
P60 defines an invariant Lipschitz graph by

 F(t,x,Z*)=Z*(a(t,x,Z*),X(t,x,Z*)).                 (1)

Its graph transform T solves F(t,x,ζ)=Z(a(t,x,ζ),X(t,x,ζ)) for ζ near1.
P60 gives positive denominator lower bound μ, first-derivative/Lipschitz bounds
|Z_t|<=L, |Z_x|<=Mt where derivatives exist, and uniform graph convergence.
We use that convergence, not an assumption that limits can be differentiated.

## Uniform second-derivative control of the construction
Start with analytic Z0=Z2 from P59. On a sufficiently small P60 rectangle,
Z0 belongs to its graph class. For a C2 member Z, implicit differentiation
makes ζ=T Z a C2 graph (one-sided derivatives at rectangle edges).
Finite iterates may be extended locally at edges for this calculation; no
canonical boundary event is inferred. Put S=(a,X), evaluated at(t,x,ζ), and
p=Z_t(S), v=Z_x(S). Define

 D=F_z-p a_z-v X_z >= μ,
 ζ_i=(p a_i+v X_i-F_i)/D, i=t,x.                   (2)

For b_t=(1,0,ζ_t), b_x=(0,1,ζ_x), the EXACT second derivative is

 D ζ_ij = -D²F[b_i,b_j] + DZ(S)·D²S[b_i,b_j]
          +D²Z(S)[DS b_i,DS b_j].                (3)

Here partial derivatives of a,X,F are before substituting ζ; the terms containing
ζ_ij have already been gathered into D. Equation(3) includes all moving-frame
and preparation terms through the canonical quotient formulas.

Use the seminorm

 R(Z)=max(sup|Z_tt|,sup|Z_tx|,sup_{t>0}|Z_xx|/t).

It is finite for Z0: Z0(0,x)=1 and the polynomial coefficients are smooth.
Analytic a=t² a0 gives a_t=O(t), a_x,a_z=O(t²), a_tt=O(1),
a_tx,a_tz=O(t), and a_xx,a_xz,a_zz=O(t²). All first/second derivatives
of X and F are bounded on the fixed box. Since F(0,x,1)=1 identically,
F_xx(0,x,1)=0; bounded third derivatives therefore imply
F_xx(t,x,ζ)=O(t+|ζ-1|)=O(t) on |ζ-1|<=Lt.

Choose finite constants C,K>=1 on a fixed P60 box, independent of R(Z),
such that a<=Ct² and the transported components obey

 |(DS b_t)_a|<=Kt, |(DS b_x)_a|<=Kt²,
 |(DS b_t)_X|<=K,  |(DS b_x)_X|<=K.

These estimates use only P60's first-derivative bounds L,M. For example
(DS b_t)_a=a_t+a_z ζ_t and (DS b_x)_a=a_x+a_z ζ_x.
In the last term of(3), evaluated at S, one has |Z_xx(S)|<=R(Z)a.
Thus its normalized bounds are

 tt: R K²[2t+(1+C)t²],
 tx: R K²[t+(1+C)t²+t³],
 xx/t: R K²[(2+C)t+t³].                           (4)

The first two terms of(3), divided by D, have normalized bounds <=Q for some
finite Q independent of R: for xx the F_xx term is O(t), the F_xz ζ_x term
is O(t), F_zz ζ_x² is O(t²); the Z_t D²a term is O(t²) and
Z_x(S)D²X is O(t²). The tt and tx terms are bounded by the displayed
factorizations and bounded L,M. This explicitly explains why the xx/t weight
is required instead of assuming unweighted derivative contraction.

Consequently every C2 graph iterate satisfies

 R(TZ)<=Q+ρ R(Z),
 ρ=K²[(2+C)ε+(1+C)ε²+ε³]/μ.                     (5)

Q,C,K depend only on the fixed analytic box and L,M, not on iteration number.
Choose Rbar>=max(R(Z0),2Q,1), then shrink ε so ρ<=1/2 while retaining
P60's inequalities. Therefore R(Zn)<=Rbar for every n. This is a general local
bound with radius defined by derivative supremums, not a numerically inferred
experimental margin. It introduces no extra physical term.

## Passing to the exact graph: no derivative-limit assumption
P60 gives uniform Zn->Z*. The bounds above make the gradient sequence uniformly
bounded and equicontinuous on the closed rectangle: all Hessian entries are
bounded by a finite constant (|Z_xx|<=Rbar ε). Arzela–Ascoli gives convergent
gradient subsequences. For each such subsequence, pass to the limit in
Zn(b)-Zn(a)=integral of its gradient along any coordinate segment. The limiting
gradient is uniquely the continuous first derivative of Z*. All subsequences
therefore have the same limit, and the entire gradient sequence converges.
The common Lipschitz gradient bound passes to the limit. Hence

 Z* is C1,1 locally on this restricted rectangle.  (6)

Edges mean one-sided continuous derivatives of the canceled graph; the interior
has ordinary C1,1 regularity. We do NOT claim C2, C-infinity, analytic series
convergence or globally smooth continuation from these bounds. The same fixed
point is obtained on the restricted rectangle because T never evaluates beyond
it and P60 gives uniqueness there.
At t=0, Z*_x=0. Differentiating(1) gives

 Z*_t(0,x)=-F_t(0,x,1)/F_z(0,x,1)=2+x,

consistent with P59. This is a boundary coordinate statement, not a canonical
zero-load event. A valid general cautionary counterexample is fn(u)=sin(nu)/n:
uniform convergence to0 alone does not make fn' converge. The uniform second
bounds, integral argument and uniqueness above are the missing evidence.

## Exact canonical tangent and local return rank
With p=Z*_t(S),v=Z*_x(S), (2) now holds for the exact graph. Its amplitude
return is ahat=a(t,x,Z*), Xhat=X(t,x,Z*), with tangent

 J=[[a_t+a_z Z*_t, a_x+a_z Z*_x],
    [X_t+X_z Z*_t, X_x+X_z Z*_x]].                (7)

There are TWO independently evolving amplitude directions here, PLUS phase.
On the boundary z=1, X0=x/(1+x+x²),
X0'=(1-x²)/(1+x+x²)². Since a=2(1+xz²)t²+O(t³),
Z*=1+O(t), Z*_t bounded and Z*_x=O(t), uniformly in the local x interval,

 det J =4(1+x)(1-x²)/(1+x+x²)² * t +O(t²).       (8)

The coefficient is strictly positive for the chosen δ<1/9. Shrink ε again so
the uniform remainder preserves positivity. The inverse function theorem then
gives a C1 local diffeomorphism for every t>0,x>0 in this local domain.
It need not be onto the entire rectangle and no uniform inverse bound holds
as t->0. This proves a regular THREE-coordinate discrete return, not a2D flow.

The full return is(ahat,Xhat,phi+sign(eta)atan(sqrt(x))). Its tangent is

 [[J11,J12,0],[J21,J22,0],
  [0,sign(eta)/(2sqrt(x)(1+x)),1]].                (9)

Its determinant equals det J. The phase derivative becomes unbounded at x=0;
kernel axis/phase observability and geometry load/gap also degenerate on the
axes. Interior canonical differential formulas do not provide uniform boundary
conditioning. No regular physical continuation across those terminals is asserted.

For a future C1 invariant curve t=T(x), a NECESSARY exact tangent equation is

 T'(Xhat) [X_x+X_t T'(x)] = a_x+a_t T'(x),        (10)

where a_x,a_t,X_x,X_t in(10) are derivatives of ahat,Xhat. If the denominator
is nonzero this determines the induced curve slope; it does not prove such a
positive nonanalytic curve exists. No coordinate is discarded to simulate closure.
That curve construction is the next necessary dependency, with complete nonlinear
invariance and nondegenerate2D return, then independent clock/physical selection.

## Force, alternatives, levels and robustness scope
The C1 tangent was derived from the nonlinear event and declared preparation,
not a mechanical generator in a readout. A tangent of a discrete3D return is
insufficient to infer a sine torque, inertia or calibrated energy. The phase
increment is independent of phi; a physical projection must prove all additional
flow/force equations and be independently selected. A clock rescaling H->cH
changes any resulting acceleration by c^-2. No seconds scale follows from(6)–(9).

Stability here means bounded first-derivative construction and local return rank
on the specified restricted domain; it is neither all-state Lyapunov stability,
nor measurement-robust prediction, nor arbitrary perturbation robustness.
The t->0 inverse and x->0 phase derivative provide concrete conditioning limits.
P59 failures remain archived, and P60's sample points are not certified radii.
No real development fitting or holdout access occurs in this prerequisite proof.

Accompanying whole-source search:83–85 supplies the quotient;PartI62–64 demands
all endogenous chain terms and warns of singular gaps;86 load/stock/entropy/
witness identities constrain accounting but do not pick the missing curve or
force;87 supplies no undeclared continuous seeding on full persistence;
88.1 distinguishes geometric decay from a canonical zero event;88.2's scalar
constant input is a different declared extension;88.3 supports P57 viability;
88.4 supplies no event generator;89 imposes exact factor/flow/clock closure;
90 preserves the result only on its specified replicated full-persistence family.

On that family use normalized trace/n readouts and the known family-return map;
D replicates as D tensor I, K/Y tangent variations replicate, formation stock
and witness normalization are preserved, and ranks multiply. By(164) the event
and tangent commute with that lift at admitted interior states (derivative of
the equality in compatible family coordinates). Quotient handling removes
replicated SVD degeneracy; an arbitrary componentwise inverse gap formula would
be invalid there. Returning to base coordinates preserves(7)–(9) and their
conditioning limits, and does not erase a degree of freedom or prove fractality.
Different inputs/nonreplicated directions need an explicitly declared new map.

## Verification and completion criteria
Freeze: exact factor/derivative identities; finite-depth implicit gradients
and Hessian against independent high-precision central differences; local determinant
asymptotics; complete Ambient matrix directional differences. Tolerances and
sample bounds live in check.py. These are synthetic math/code controls, not
measurements or a replacement for(3)–(6)'s general argument.

Observed controls: eight symbolic identities; 80-digit finite-depth gradient
error <=6.19e-24 and Hessian error <=1.18e-14; three independent complete
Ambient directional-Jacobian cases (12 events), max error6.28e-9.
All frozen tolerances passed. These finite-depth controls do not certify the
exact graph at the sample points or a numerical domain radius.

PROVED: C1,1 of the P60 local graph after domain restriction, exact tangent,
positive local interior return determinant. OPEN: positive nonanalytic invariant
curve, regular2D physical flow, force/energy/inertia/seconds/interventions.
Publish code/proof/control output and verified register/ledgers before moving on.
