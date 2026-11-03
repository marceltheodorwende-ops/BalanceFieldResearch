# Initial persistent support: classification and conditional minimality

Date: 3 November 2026. Continuation of the existing verification stage; no new law or initial-state default is installed.

## 1. What is already fixed by a given recursion

For a supplied finite power-bounded R_C with the repaired peripheral/stable decomposition, its persistent subspace and ordinary orthogonal projector P are uniquely determined. Computing this projector is not the missing step. The unresolved origin question is whether earlier formation/identity premises uniquely specify that recursion or its full peripheral space.

The September 22 canonical source, Section 5, paragraphs 105–117, defines persistence through R_C and a graph-metric projector. Its older non-decay formulation must be read with the existing finite repair; this audit uses the peripheral subspace, not the span of arbitrary vectors with a surviving component. The September 26 minimal state instead stores the ordinary orthogonal persistent projector explicitly and constructs graph projection when needed. These two projectors are not interchangeable when [P,Y]!=0.

## 2. All protected supports containing the formed line

Let Pi be the rank-one fresh formation projector. Suppose the origin condition requires that the whole formed line be persistent, so Pi<=P for an orthogonal projector P. Then every such projector has the unique form

```math
P=\Pi+Q,\qquad Q=Q^*=Q^2,\qquad Q\Pi=\Pi Q=0.
```

Proof: Pi<=P means P Pi=Pi P=Pi. Therefore Q=P-Pi is self-adjoint and Q^2=P-Pi; its products with Pi vanish. Conversely, any such Q gives an orthogonal P containing Pi.

Thus Pi is the unique **least** containing projector, and it is the unique containing projector of rank one. Choosing the least support or the smallest rank would give P_0=Pi_0, but the requirement to choose it is an additional origin condition unless already justified by a source premise. Preservation of the formed line alone permits every Q in its orthogonal complement.

For every such P and any supplied Y>0, the existing neutral transverse rebuild formula defines the diagnostic recursion

```math
R(P,Y)=P+(I-P)(I+Y)^{-1}(I-P).
```

Its complementary block is positive with norm below one, and the other block is identity. Hence R is power bounded with peripheral space exactly Ran(P), and R fixes the formed line. This construction shows the freedom under the stated preservation/boundedness conditions. Applying a declared successor formula to origin is used here only to construct comparison recursions, not adopted as a fundamental origin rule. A prescribed original R_C could impose stronger restrictions and must not be overwritten.

## 3. A different minimality: neutral-invariant support

If one additionally requires that the support be invariant under the self-adjoint neutral geometry Y, there is a unique smallest such support containing a unit formed vector e:

```math
\mathcal C_Y(e)=\operatorname{span}\{e,Ye,\ldots,Y^{n-1}e\}.
```

Cayley–Hamilton makes this finite span Y-invariant. Every invariant space containing e contains all its powers and therefore contains C_Y(e). For self-adjoint Y this invariant space is reducing, so its ordinary projector P_cyc commutes with Y.

Equivalently, let E_j be Y's spectral projectors for its distinct eigenvalues. Polynomial interpolation gives

```math
\mathcal C_Y(e)=\bigoplus_{j:E_je\ne0}\operatorname{span}(E_je).
```

Each nonzero projected vector contributes one dimension, even inside a degenerate eigenspace; the formula does not automatically include that whole eigenspace. The construction is independent of the phase/sign of e and transforms covariantly under joint unitary coordinate changes.

Consequently P_cyc=Pi exactly when the formed vector is an eigenvector of Y, equivalently [Y,Pi]=0. Otherwise the minimal neutral-invariant support has rank at least two. In general its rank can be as large as n.

This is an exact mathematical theorem, **not a new BFG selection law**. The reviewed finite event allows [Y,P]!=0 and the previous fresh-origin example uses it. Therefore neutral invariance cannot silently be imposed on every input. Minimal containing support and minimal neutral-invariant support answer different questions.

## 4. Same fresh formation and same Y, different initial P

Use the fresh minimum

```math
K=\operatorname{diag}(-2,-1),\quad F=2\Pi,\quad W=\Pi,
\quad\Pi=\operatorname{diag}(1,0),\qquad
Y=\begin{pmatrix}1/4&1/8\\1/8&1/4\end{pmatrix}.
```

The smallest containing projector is P_a=Pi. Since e and Ye are independent, the smallest neutral-invariant containing projector is P_b=I. Both choices contain the witness and the formed line. Both associated R(P,Y) are power bounded and fix the profile; their peripheral ranks are respectively one and two. No new fitted quantity is used to distinguish them.

For the unchanged finite event these P choices have different consequences:

| Initial P | Active output dimension | Seed trace | Formation trace after step | tr(K_+) |
| --- | --- | --- | --- | --- |
| Pi | 2 | 2 | 4 | -4 |
| I | 2 | 0 | 2 | -3 |

The first row is the preceding fresh-origin analysis: both analysis branches have target support in copies of the first old direction, so K_+=-2I and an orthogonal seed is generated.

For P=I, selection is identity since 0<Y<I. C and B are functions of Y, and the full-rank analysis has polar blocks `sqrt(alpha) C H^-1/2` and `sqrt(beta) B H^-1/2`, where `H=alpha C^2+beta B^2`. Thus

```math
\operatorname{tr}K_+
=\operatorname{tr}\big(K H^{-1}(\alpha C^2+\beta B^2)\big)
=\operatorname{tr}K=-3.
```

Full input persistence gives full inherited active support, hence no seed. The common polar transport is unitary between equal-dimensional active carriers, so formation trace remains 2. These exact invariants distinguish the successors independently of SVD coordinate conventions. Fresh floating checks confirm the well-separated transition; they are not a certified numerical rank algorithm.

This does not prove that both choices satisfy every historical origin premise. It proves that the explicitly stated preservation/typed-input packet does not fix the same outcome.

## 5. Source and interpretation boundary

The original formation minimum fixes Pi and F; it does not, in the reviewed paragraphs, equate the entire persistent space with Pi. The existing successor seed-promotion rule supplies a definite P_+ after a successful inherited transition, but its declared domain and origin justification must not be conflated. The zero-predecessor gate remains terminal; setting inherited support to zero is not an origin constructor.

The September 26 phrase 'typed-operationally minimal' concerns retaining the five distinct roles needed for the event. It is not a principle minimizing rank(P). Likewise a no-choice failure discipline does not automatically choose the least projector among several admissible origin supports. The June primitive persistence symbol is not already a specified matrix on the later carrier.

The earlier 2025 and June source traces remain in the [origin audit](../origin_bridge/README.md). This step checks the September persistence/state clauses and develops their exact finite consequences, rather than claiming a fresh exhaustive search. [SOURCES.json](SOURCES.json) pins the current scope.

## 6. Conclusion

P_0=Pi_0 is uniquely determined **if** the origin uses the least persistent support containing the formed profile. It is not implied merely by profile preservation and bounded recursion. Requiring neutral invariance instead has a unique minimal solution too, but that solution can be larger and changes the event's seed/formation/kernel outcome.

The foundational task is therefore to justify the intended origin support criterion or derive the initial R_C, rather than choose a convenient meaning of 'minimal'. Neither criterion is adopted here. Given that unresolved criterion, the complete initial state remains conditional; the separate Y_0 interface question also remains open.

Run `python initial_persistence/check_persistence.py`. [results.json](results.json) separates exact controls and preserved-helper checks. No empirical result, new paper, new physical equation or changed event rule is claimed.
