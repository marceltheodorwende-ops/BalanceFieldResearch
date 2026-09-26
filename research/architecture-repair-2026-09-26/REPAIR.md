# Architecture repair: persistence and successor Gram
Date: 26 September 2026.
Status: AI-assisted mathematical repair note for author review. BFG source author: Marcel Theodor Wende. This is not a new author-approved preprint, a software patch, an independent review or empirical validation.

## Source and scope
Primary source: *The BFG Canonical Universal Reclosure Architecture*, 22 September 2026, supplied FINAL PDF, 15 pages, especially p. 5 equations (23)–(27), p. 6 equations (38)–(45), and p. 11 section 15.

Existing BFG source checks, read on main before this addition:
- [Fundamental Closure Law](../fundamental-closure-2026-09-25/package/research/bfg-fundamental-closure/FUNDAMENTAL_CLOSURE_LAW.md), sections 2 and 3.1.
- [Universal Update Derivation Audit](../fundamental-closure-2026-09-25/package/research/bfg-fundamental-closure/UNIVERSAL_UPDATE_DERIVATION_AUDIT.md), sections 2 and 4–5.

Those sources already use the repaired peripheral Riesz sector and explicitly label intrinsic-Gram reconstruction a declared finite completion. This note does not rediscover or upgrade those decisions. It gives explicit replacement text and proofs for using the September 22 architecture as the working basis. The removed September 26 preprint and balance-law packages are not reinstated.

## A. Repair of equation (23)
### A1. Exact defect
The closure of the span of bounded, non-decaying forward-orbit vectors is not generally the peripheral subspace.

Take H=R², G=I and R=diag(1,1/2). Both e1 and e1+e2 have bounded forward orbits with strictly positive asymptotic norm. Their difference is e2, whose orbit decays to zero. Thus the span in (23) is all of H, while the intended persistent subspace is span(e1).

More generally, in a finite-dimensional power-bounded system with a nonzero peripheral sector, every stable vector s is the difference (w+s)−w of two bounded non-decaying vectors, for any nonzero peripheral vector w. Hence the original span includes the stable sector as well. The defect is in taking that span, not in the existence of spectral projectors.

### A2. Finite-dimensional replacement
Assume:
1. H is a fixed finite-dimensional complex Hilbert space (complexify a real carrier when needed).
2. G is positive definite and R is power bounded.
3. The peripheral sector is nonempty for a nonterminal persistent event. Its complement has spectral radius below one.

Define
    W_per = direct sum over |lambda|=1 of ker(R−lambda I).       (R1)
Equivalently,
    E_per = (1/(2 pi i)) integral_Gamma (zI−R)^(-1) dz,
    W_per = Ran(E_per),                                       (R2)
where Gamma is a positively oriented union of contours enclosing exactly the peripheral eigenvalues.

Power boundedness rules out eigenvalues outside the unit disk and nontrivial Jordan blocks on its boundary: either would produce an unbounded orbit. On every Jordan block with |lambda|<1, polynomial growth is dominated by geometric decay. Consequently
    H = W_per direct-sum W_stable,
    R^n restricted to W_stable tends to zero.                  (R3)
The direct sum is algebraic/spectral; it need not be orthogonal.

For nonzero w in W_per, its forward orbit is bounded above and bounded away from zero. To see this, diagonalize R on W_per as S diag(lambda_j) S^(-1). The diagonal powers and their inverses have norm one in spectral coordinates, so uniform norm-equivalence bounds give both assertions. This proves that (R1) extracts the intended non-decaying spectral component without retaining stable admixtures.

On a real carrier, take the real invariant space associated with the conjugation-invariant peripheral spectral set; do not discard conjugate pairs.

### A3. Replacement of the projector, preserving equation (26)
For any full-column-rank matrix W spanning W_per, set
    P_G = W(W†GW)^(-1)W†G.                                   (R4)
Then P_G²=P_G, P_G†G=GP_G and Ran(P_G)=W_per. These follow by direct multiplication, because W†GW is positive definite. For z=P_G z+(I−P_G)z the two terms are G-orthogonal, so
    ||P_G z||_G <= ||z||_G.                                  (R5)
Changing W to WS with invertible S leaves P_G unchanged.

Do not substitute E_per for P_G in metric-contractivity arguments. For
    R = [[1,−1/2],[0,1/2]], G=I,
one has
    E_per=[[1,−1],[0,0]], P_G=[[1,0],[0,0]].
Both have the same range, but E_per is oblique and has Euclidean norm sqrt(2). P_G need not commute with R; range invariance alone does not make the orthogonal complement invariant.

### A4. Infinite-dimensional boundary
The finite replacement is fully proved above. It does not establish universal persistence for arbitrary bounded operators, unbounded operators or continuous peripheral spectrum.

A sufficient extension uses an explicitly isolated spectral split into a finite-dimensional semisimple peripheral block and a bounded stable restriction with spectral radius strictly below one, with a bounded coercive G on the Hilbert carrier. The same proofs then apply. If G is an unbounded form metric, domain invariance and closed-form compatibility require separate proofs.

Do not identify the orthogonal complement of the forward-decaying subspace with W_per in a general nonnormal system. Do not use a finite numerical eigenvalue tolerance as the definition of exact persistence.

## B. Repair of the Gram claim in equations (44)–(45)
### B1. What those equations establish
The displayed factorization
    Y_+ = L_+† B_+† W_+ B_+ L_+, W_+ >= 0                    (R6)
proves positivity once the maps and domains are fixed. It does not fix their dependence on the incoming packet.

On any finite nonzero target carrier, every Z>=0 is realized by L_+=I, W_+=I, B_+=sqrt(Z). In particular Z=I and Z=2I give different subsequent neutral operators, I/2 and I/3. This is exactly the non-uniqueness already recorded in the existing BFG audit. Positivity, dimensional consistency and basis covariance alone do not repair it.

### B2. Explicit finite completion, with its added premise visible
Let A be the already constructed cross-fed analysis operator in source equation (38). Fix the original Hilbert inner products used in that equation's adjoint and polar decomposition. Put
    S = support(A†A), H_+ = Ran(A),
    A = J Q, Q=(A†A)^(1/2).                                 (R7)
In finite dimensions the active range is closed. J:S -> H_+ is unitary between these active spaces.

The existing BFG finite-completion source can be expressed by the following conditional principle (not adopted here as an extra axiom of the September 22 architecture):
"The successor neutral load represents the quadratic form induced by the current analysis map, transferred to the active target through its polar isometry."

In formulas, require for every x in S
    <Jx,Y_+ Jx> = ||Ax||².                                  (R8)
This is the additional constitutive identification. It is not a consequence of positive Gram factorization alone.

Under (R8), the unique Hermitian successor load is
    Y_+ = J(A†A)|_S J† = (AA†)|_(H_+) > 0.                   (R9)
Proof: (R9) satisfies (R8). If two Hermitian loads satisfy (R8), their difference has zero quadratic form on all of H_+. Polarization implies that the difference is zero. Positivity is strict on the finite active carrier since A has no zero singular value there.

For a reduced SVD A=U Sigma V†,
    Y_+ = U Sigma² U† on H_+,
    [Y_+]_U = Sigma².                                       (R10)
Degenerate singular values allow different bases, but these are simultaneous unitary coordinate changes, not different basis-free loads. All transported capacities must use the same active frame. For A=0 the active carrier is empty and the terminal rule applies.

This matches the existing BFG finite completion, without importing the deleted September 26 paper or its Neutral-Contrast Selection rule into the older architecture.

### B3. The metric must be fixed, not silently exchanged
The September 22 paper uses G-weighted channel loads but an ordinary-adjoint polar decomposition in equations (38)–(40). The proposal above uses the latter inner products.

If instead the right side of (R8) were ||Ax||_(G direct-sum G)², the represented operator would contain A†(G direct-sum G)A, generally different from A†A. Even scalar A=1/4 gives Gram 1/16 in the unit target metric and 1/8 in metric 2. Thus "use the induced Gram" is insufficient until the metric is declared.

The fact that reciprocal weights were computed with G does not by itself turn the Euclidean Gram into the G-Gram.

### B4. An explicit factorization and its semantic boundary
On H_+, one factorization realizing (R9) is
    L_+=I, W_+=I, B_+=sqrt(Y_+), H_C,+=Y_+.                  (R11)
This is a factorization convention, not a proof that historical BC, WN and LC roles individually equal these operators. If they enter other equations independently, those equations must be checked.

For instance, if one additionally requires B_+=D_cov,+ c_+, then with invertible c_+ the convention gives D_cov,+=sqrt(Y_+) c_+^(-1). If c_+ is singular and Y_+ is positive definite, this equation cannot hold with L_+=I: a nonzero vector in ker(c_+) would also lie in ker(B_+), contradicting invertibility of sqrt(Y_+). More generally (R6) with B_+=D_cov,+ c_+ requires
    ker(c_+ L_+) subset ker(Y_+).                            (R12)
This is a compatibility test, not a license to discard a BFG role. Individual factor reconstruction remains open wherever additional semantic constraints are not specified.

## C. Precise verdict
- Persistence: replace (23) with (R1)–(R2) on the declared finite power-bounded category. This repairs a genuine mathematical error and agrees with the already intended spectral description.
- Gram reconstruction: (R9) is uniquely determined after the explicit principle (R8) is adopted. This is an existing BFG-internal completion candidate, not a derivation forced by the older architecture alone.
- Full universal iteration: not certified by these two repairs. Successor recursion, role reconstruction, carrier maps and infinite-dimensional domains remain separate obligations. The older audit already demonstrates that P+r(I−P), 0<=r<1, gives multiple admissible recursion operators with the same persistent space.
- Natural laws: no energy, gravity, gauge or quantum law has been established by this repair.

No historical PDF or executable code was changed. The mathematical counterexamples are preserved, not renamed successful tests. Next work should determine whether a BFG source forces (R8), or explicitly adopt it as a finite branch rule and check all independent BC/WN/LC constraints before pursuing physical reduction.
