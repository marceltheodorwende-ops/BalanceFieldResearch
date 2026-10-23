# Eventual stable-class entry from the full positive-load persistence sector

23 October 2026. BFG-only; [preregistered protocol](EVENTUAL_CLASS_PROTOCOL.md).
Source: pinned complete Dynamic Order, Parts I/II, unchanged full ambient update. All conclusions below are mathematical source consequences under the explicit autonomous persistence assumptions. No external physical law is inserted.

## 1. Domain and endpoint envelope without an order assumption

Assume finite n, P=I, F>0, W>=0 with tr W=1, K Hermitian and 0<Y<I. Do NOT assume the earlier class C or simple spectrum.
The complete aligned update of DERIVATION.md section 1 applies:
Y_+=g_alpha(Y), F_+=F, W_+=W,
g_alpha(y)=[alpha+(1-alpha)y²]/(1+y)²,
alpha=L_B/(L_C+L_B).
In an eigenbasis of Y, alpha is a positive weighted mean of r(y)=y²/(1+y²), with weights f_i h(y_i), f_i=<e_i,F e_i>>0 and h(y)=(1+y²)/(1+y).
Thus alpha<=r(M), where M=max spec Y<1.

For 0<=y<=M<1, g_alpha(y)<=g_(r(M))(y) since partial_alpha g=(1-y)/(1+y)>0.
The derivative of the latter is
2(y-M²)/[(1+M²)(1+y)³].
It decreases then increases, with its only interior minimum at M². Its maximum on [0,M] is therefore at an endpoint:
M_+ <= max{g_(r(M))(0),g_(r(M))(M)}
     = max{r(M),f(M)},
f(M)=2M²/[(1+M)²(1+M²)].

Both endpoint values are <=M/2:
M/2-r(M)=M(1-M)²/[2(1+M²)]>=0,
f(M)/M <= 2M/(1+M)² <=1/2,
1/2-2M/(1+M)²=(1-M)²/[2(1+M)²]>=0.
In fact the envelope is strict for 0<M<1. Consequently
0<M_k <=2^-k M_0.

This proof does not require the eigenvalue order to survive before entry into C. It proves autonomous full persistence is invariant on this domain: Y_+ remains positive and below I, loads and analysis singular values are strictly positive, F remains positive and there is no selection loss or seed complement. It says nothing about arbitrary P, external drives or actual numerical rank cutoffs.

## 2. A lower bound that prevents indefinitely thin spectral extrema

Let delta=lambda_min(F)/tr(F)>0. It is unchanged by aligned persistence and source unitary coordinates.
For 0<=y<=1, 1/2<=h(y)<=1. Certificates are
1-h(y)=y(1-y)/(1+y)>=0,
h(y)-1/2=[2(y-1/4)²+7/8]/[2(1+y)]>0.
Choose any Y eigenvector with eigenvalue M. Its formation weight is at least lambda_min(F), while the full weighted denominator is <=tr(F). Hence
alpha >= (delta/2) r(M) >= delta M²/4.

For every eigenvalue y of Y,
g_alpha(y) >= alpha/(1+M)² >= delta M²/16,
and
g_alpha(y) <= alpha+(1-alpha)M² <=2M².
Thus
m_+ >= delta M²/16,   M_+ <=2M².
If M²<=delta/128, then
m_+ >= delta M²/16 >=8M^4 >=2M_+².
Also M_+<=M/2<1/2.
So the successor belongs to the earlier invariant class
C={0<m<=M<=1/2, m>=2M²}.

An explicit finite entry bound follows. Choose any integer k>=0 with
(M_0/2^k)²<=delta/128.
Then state k+1 is in C, regardless of earlier spectral reorderings or collisions.
For example a conservative choice is
k=max{0,ceil(log_2[M_0 sqrt(128/delta)])}.
The exact integer inequality is authoritative at equality/rounding boundaries.

**Advanced scope:** C need not be imposed as an initial restriction anywhere in this positive-formation autonomous full-persistence sector. Every such trajectory eventually reaches it. This is an exact finite-event statement, not a numerical guarantee that all events up to the conservative bound are resolvable by floating-point source code.

## 3. The missing simple-spectrum inference: an exact collision

Eventual entry of the EXTREMA into C does not imply a simple spectrum there.
For distinct a,b,
g_alpha(a)-g_alpha(b)
=(a-b)[a+b+2ab-2alpha(1+a)(1+b)]/[(1+a)²(1+b)²].
This can vanish even if the initial eigenvalues differ.

Take
Y=diag(1/10,1/2,9/10),
F=diag(1,1,41762/20625), W=I/3, P=I.
The positive formation weights give alpha=59/209 exactly, and
Y_+=diag(50/209,386/1881,50/209)
in the aligned frame.
The middle source mode is now the unique lowest successor mode, while the first and third modes tie for second. The successor already lies in C.
Therefore the Y-only projector onto exactly TWO lowest modes is not uniquely defined at this selection boundary, although the initial spectrum was simple.
All later Y updates are functions of the current Y, so the coalesced block remains degenerate; C cannot split it.

This counterexample limits the universal Y-only selector, not all BFG-internal selectors. As a natural post-witness diagnostic, compress F to the colliding block: its eigenvalues are 1 and 41762/20625>1. F therefore resolves this particular tie. In this example the resulting lexicographic Y-then-F choice is retained after entry because the Y blocks and F are retained in alignment.
The final audit explicitly checks that strict F inequality, with unchanged witness inputs. No general globally unique tie-resolution theorem is claimed; fully symmetric states retain the earlier stabilizer obstruction.

If no finite spectral collision occurs before entry, simple spectrum survives to C and the earlier current-state pair/relational-frame results then apply, subject to their nonzero-reference chart condition. We do not promote this conditional statement to every initially simple state, nor claim a genericity measure theorem.

## 4. Do not extend the trace-log clock by the maximum bound

Although M contracts everywhere on the domain, individual small eigenvalues may increase. Even tr(Y) may increase.
Use
Y=diag(1/100,1/50,9/10), F=diag(1,1,100), W=I/3, P=I.
The source gives
alpha=417235807/951620807,
and an exact positive trace jump
tr(Y_+)-tr(Y)
=154001028484979585789/911494874535213692700
≈0.1689543548596554.
At the same event M_+<M/2.
Therefore ln[tr(Y)/tr(Y_+)] is NEGATIVE in this admissible state and is not a universal positive clock on the broader sector.

The previous positivity proof was explicitly on C and remains valid there. The global envelope instead gives the positive load-duration bound
sum_k tr(Y_k)/n <=sum_k M_k <=2M_0.
This strengthens the reach of the mathematical summability statement, not a physical time calibration.
Maximum contraction is not a substitute for trace monotonicity, pointwise ordering or current conservation.

## 5. Fresh verification and numerical limits

eventual_class_audit.py checks the exact envelope/collision identities and rational witnesses, then imports the pinned original source after its Git-blob check.
- 12 broad rational diagonal preparations in n=2,3,4,5, with three formation-weight profiles each. Independent exact eigenvalue evolution reached C in 20 events overall; every preparation entered within the predeclared ten-event cap and its conservative proven bound.
- 12 complex preparations, n=3,4,5,6, two complete source events each: 24 events. All checked upper/lower bound violations were zero at recorded precision.
- Two additional complete source calls reproduce the designed collision and trace increase: 26 new full source calls overall.
- Exact eigenvalue collision is established algebraically. A numerically tiny successor gap is corroboration, not the definition of degeneracy.
- The exact orbit controls are not additional source calls. The general theorem extends beyond the finite numerical horizon; the source's previously recorded small-rank numerical cutoff is retained.

The initial audit passed the preregistered identities and controls. A later diagnostic added the explicit check that F resolves THIS collision, followed by a fresh final run; this observation is not misreported as a preregistered universal selector.
GitHub CI evidence is recorded separately for the published code commit.

## 6. Remaining dependency

A broad basin for stable spectral extrema is now proved. The choice of rank two and its physical locality are still not selected; even a unique spectral pair needs conditions excluding or resolving degeneracy, plus a nonzero relational reference.
Next constructive step: test a current-state, source-covariant tie-resolution using retained formation/Witness blocks, keeping the fully symmetric counterexample and any lost closure data. Selection/seed transitions remain an additional domain extension.
Physical event adjacency, displacement, calibrated clock, joint local four-current and Einstein dynamics remain open. Neither eventual damping nor an internal selector supplies them by itself.
