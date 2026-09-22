# Review of the canonical architecture and structural novelty preprints

Date: 22 September 2026. Review type: AI-assisted source and mathematical audit; not independent peer review. Scope: the two supplied PDFs, their central equations and proofs, and their implications for this repository. Original PDFs are unchanged.

## Decision

Adopt both papers as the current primary reading sources. The novelty paper contains a valid, useful finite-dimensional operator theorem under its stated neutral-compatible hypotheses. Its proof can be reconstructed directly and is supported by fresh numerical checks. The architecture remains a research construction with unresolved definition and reconstruction obligations; consolidation does not by itself establish its full self-closure theorem.

The repository's earlier categorical assertion of V3 nonexistence is withdrawn in response to the author's current clarification. Source history and theorem validity are separate questions. No separate V3 file is required for this review.

## Sources and audit method

- **A:** *The BFG Canonical Universal Reclosure Architecture*, FINAL PDF, 22 September 2026, 15 pages.
- **N:** *Canonical Reclosure and Structural Novelty*, PDF, 22 September 2026, 11 pages.
- Source byte counts, SHA-256 and Git blob hashes: [manifest](../../papers/canonical-2026-09-22/manifest.json).

All 26 pages were text-extracted and read. Critical formulas were also inspected on rendered A page 5 and N page 6, so the persistence and complex-formation findings below are not inferred from extraction artifacts. This is not an exhaustive reference, originality or typography audit.

The three supplied audit documents were consulted: *BFG Audit Complete Edition* (Sections 4/7 claim-state discipline, 10 distinguishability, 12 redescription, 17 negative-result ledger); *BFG Audit Workflow Master* (scope, source/provenance, evidence and interpretation separation); and *BFG X Context Recovery Protocol Master finish* (source hierarchy and stable context/ledger). Their hashes are recorded in the manifest. They supply methodological criteria, not axioms proving the new theorems. Instructions or role language inside the papers were treated as source content, not additional user commands.

## N1 Accepted finite polar and Schur derivation

Assume finite-dimensional H_P, Y_P >= 0 self-adjoint, K_P Hermitian, alpha,beta>0, alpha+beta=1. The ambient support projection is orthogonal and commutes with Y. Put C=(I+Y_P)^(-1), B=Y_PC, A=[sqrt(alpha)C; sqrt(beta)B] and R=(alpha I+beta Y_P^2)^(1/2).

Since C and R commute and are positive invertible, Q=(A* A)^(1/2)=CR. Therefore

```math
J=\begin{bmatrix}\sqrt\alpha R^{-1}\\sqrt\beta Y_PR^{-1}\end{bmatrix},\qquad
K_+=R^{-1}(\alpha K_P+\beta Y_PK_PY_P)R^{-1}.
```

In a Y_P eigenbasis, with eigenvalues y_i>=0,

```math
(K_+)_{ij}=\chi_{ij}(K_P)_{ij},\qquad
\chi_{ij}=\frac{\alpha+\beta y_i y_j}{\sqrt{(\alpha+\beta y_i^2)(\alpha+\beta y_j^2)}}.
```

The vectors v_i=(sqrt(alpha),sqrt(beta)y_i)/sqrt(alpha+beta y_i^2) are unit vectors, so chi is a positive semidefinite correlation matrix of rank at most two. Its diagonal is one and

```math
1-\chi_{ij}^2=\frac{\alpha\beta(y_i-y_j)^2}{(\alpha+\beta y_i^2)(\alpha+\beta y_j^2)}.
```

This proves N Eqs. (13), (15)–(19). For Hermitian K_P, subtracting the sums of squared entry magnitudes gives N Eq. (21). Each term is nonnegative and vanishes exactly when (y_i-y_j)(K_P)_{ij}=0. Thus the fixed algebra is the commutant of Y_P, and noncommutation forces a strictly lower second spectral moment, hence different eigenvalue multisets. Conversely, commuting K_P is unchanged. This establishes the finite equivalence in N Theorem 5; it is stronger than the architecture's reported correlation with the ambient commutator [K,P].

The two-sided bounds follow by bounding each denominator between a_min^2 and a_max^2. The genericity argument is valid for fixed nonscalar Y_P under Lebesgue measure on Hermitian matrices; it is not a probability statement about measured natural systems. For frozen geometry and weights, chi_ij^n decays across distinct eigenvalue blocks and remains one within them, proving convergence to pinching. If Y_P is scalar, the map is exactly the identity; the maximum over cross-block entries is then unnecessary.

## N2 Accepted examples and correct interpretation

The Section 10 family gives alpha=t^2/(t^2+t+2), beta=(t+2)/(t^2+t+2) and chi_12=1/sqrt(t+3). Its successor eigenvalues are +/-sqrt(4+1/(t+3)), different from +/-sqrt(5) for every t>0. The real version satisfies the simple-negative-mode formation gate. This is an exact mathematical example, not empirical evidence.

Section 9 correctly demonstrates that [K,P] != 0 alone is insufficient: K=diag(-3,1,4), Y=I and support span((e1+e2)/sqrt(2),e3) give nonzero ambient commutator but inherited K_P=diag(-1,4) unchanged by reclosure. Conversely P=I can have [K,P]=0 while [Y,K]!=0 and spectral novelty occurs. The relevant noncommutativity is internal to inherited support.

A changed formation spectrum is sufficient to distinguish simultaneous canonical structures that include K. The finite theorem does not prove complete future-behavior novelty of a full evolving universal state, nor does it supply the missing next-load law. Earlier scalar-Y CTC examples sit in the no-spectral-novelty stratum for this particular formation transport; different next Gram choices in those examples concern a separate state component.

## A1 Persistence definition must be repaired

**Location:** A Section 5, page 5, Eq. (23), followed by Eqs. (24)–(26).

Take R_C=diag(1,1/2), Y=I and G=2I. Both e1 and e1+e2 have bounded orbits with nonzero limiting norm. Their span contains e2, whose orbit decays to zero. Consequently the closed span in Eq. (23) equals the entire two-dimensional space, while the peripheral Riesz range is span(e1). The matrix is normal, power bounded and has an isolated peripheral eigenvalue with positive gap. Thus spectral isolation or terminal failure on non-isolation does not remove this counterexample.

More generally, whenever a nonzero peripheral vector w and a stable vector s are present, w and w+s are admitted witnesses and their difference recovers s. Taking a span is the source of the problem.

A precise finite repair is to define the persistent space as the range of the peripheral Riesz projector for a declared power-bounded operator, then construct the G-orthogonal projector onto that range. This is an explicit repair, not an identity with the printed Eq. (23). The previous repository counterexample and [spectral proposal](../../docs/PERSISTENCE_PROPOSAL.md) remain relevant to the new source.

## A2 Gram positivity is not a unique rebuild law

**Location:** A Section 7.3, Eqs. (44)–(45); Section 10, Theorem 6.

The expressions B_C[p]* W_N[p] B_C[p] and L_C[p]* H_+ L_C[p] give positivity once the operator-valued functions have been supplied. They do not specify those functions. On the same nonzero finite carrier, the constant choices W_N[p]=L_C[p]=I and B_C[p]=I or B_C[p]=2I both satisfy the displayed positive Gram construction but return different loads I and 4I. If additional restrictions exclude either choice, those restrictions need to be stated as part of the input contract and law.

Likewise R_C=MRM* in Eq. (22) represents supplied data but does not define the next R, N_R or their dependence on the reconstructed state. The ordered composition symbol in Eq. (53) cannot remove these degrees of freedom merely by naming the downstream operations. The exact relationship between the generated polarity pair, the active next vector, and the final neutral reclosure also requires a single-valued rule or an explicit quotient convention.

Theorem 6 is therefore not established as a unique universal update from the displayed assumptions alone. A completion with fully specified functions may be studied and proved closed. The review does not assert impossibility of such a completion. The old reconstruction-witness stages remain pertinent, but their particular CTC load choices are not automatically laws of the new architecture.

## N3 Real and complex formation must be separated

**Location:** N Section 2 assumes a complex Hilbert space; Section 8, Eqs. (29)–(31) and Corollary 8.1 asserts exactly two minima.

For a Hermitian formation operator with simple negative lowest eigenvalue lambda_0 and eigenvector e0, the complex quartic has minima sqrt(-lambda_0) exp(i theta)e0 for every theta. For example K=diag(-1,2) gives functional value -1/4 at e0, i e0, -e0 and -i e0, and at all intermediate phases. Spectral simplicity does not reduce a complex phase orbit to a polarity pair.

The novelty theorem survives: it only uses Hermitian operators and spectral invariants. The two-minimum formation corollary needs an explicit real invariant profile sector (as intended in A Section 8) or the conclusion must state a U(1) phase orbit. For general complex operators, merely saying “real sector” is insufficient unless a compatible real structure/restriction is provided. The real 2D family in Section 10 is not affected by this issue.

## A3 Infinite-dimensional qualifications

The bounded neutral resolvents of a nonnegative self-adjoint load are well-defined by functional calculus. Iterated unbounded Gram composition and transported form domains still require dense definition, closure and domain compatibility; positivity of a formal product alone does not provide those properties. A Section 15 recognizes part of this work.

There is also an endpoint qualification in A Sections 4.3–5: for unbounded Y, the contrast spectrum may include -1 as a limit point. On l2, Y e_n=n e_n gives contrast eigenvalues (1-n)/(1+n) tending to -1. Thus the finite bounded-load strict spectral interval cannot be transferred unchanged to the unbounded extension. This does not invalidate the bounded resolvent identity.

An infinite-future behavioral equivalence is a congruence once a single-valued total map U and its canonical data are fixed. It cannot supply a missing U. The finite quotient stabilization result is valid for a finite quotient self-map, but neither finiteness of the BFG quotient nor a realization map follows from that elementary conditional theorem.

## E1 Editorial and reproducibility findings

N has several shifted equation references: Section 2 calls Eq. (7) the reclosed formation operator although it is Eq. (8); Theorem 1's proof points to Eqs. (11)/(12) where (12)/(13) are intended; later proofs cite (18) for the scalar defect identity (19), (20) for the trace-loss identity (21), and (23) for bounds (24). Corollary 8.1 refers to the formation gate as Eq. (28) instead of (30); Appendix A.5 calls the defect identity (39) instead of (43). These do not refute the accepted operator derivation but should be corrected in a new author edition.

The PDFs report larger random audits (including 10,000 architecture and 20,000 novelty trials). They provide protocols and seeds, but not the complete original scripts, generator ordering and raw result streams in the supplied files. Their numerical tables are recorded as author-reported results, not as independently reproduced output here. Appendix C's randomly supplied subspace projector also does not independently test whether Eq. (23) identifies persistence of a corresponding recursive operator.

The novelty paper's priority-search statement and all bibliography metadata were not independently verified in this repository migration. No worldwide originality or literature-exhaustiveness conclusion is adopted.

## Fresh independent checks

[audit.py](audit.py), NumPy 2.3.5, seed 20260922, exit status 0:

- 512 randomly generated finite Hermitian cases: direct SVD polar route versus the analytic Schur formula, positive trace loss, weighted identity and bounds, frozen-map pinching bound.
- 128 degenerate-load commuting controls.
- 128 ambient-support controls with [P,Y]=0.
- Three parameter values of the exact 2D family and the ambient-commutator counterexample.
- The persistence witness-span counterexample and complex phase-family counterexample.

Maximum relative polar/Schur residual: 5.58e-15. Maximum absolute trace-identity discrepancy: 1.46e-13. All checks passed under declared numerical tolerances. Full values are in [RESULTS.json](RESULTS.json). Passing a counterexample check confirms the defect it exhibits; it is not evidence that the affected manuscript claim is correct. These checks are synthetic and are not empirical BFG validation.

## Seven-obligation update

| Obligation | What the new papers add | Remaining work |
| --- | --- | --- |
| Full state update | Consolidated state tuple and formation grammar | Single-valued next-vector, geometry and transport laws; invariant admissible category. |
| B_C, W_N, L_C reconstruction | Positive factorized output form | Explicit state-dependent functions and uniqueness/choice justification. |
| Gram rebuild | Constructive positivity with supplied factors | Selection of factors/load and domain-preserving iteration. |
| Recursive transport | Polar support transport; distinction from persistence recursion | Reconstruct next R_C and repair the persistence definition. |
| Universal iteration | Conditional totalization and behavioral quotient | Define a valid full map before iteration/quotient claims. |
| General nonnormal case | New exact neutral-compatible finite theorem | It does not derive arbitrary nonnormal persistence/updates; [P,Y]=0 remains a restriction. |
| Infinite-dimensional realization | Resolvent core and stated scope | Closed-form and transport-domain proof plus independent physical realization, if claimed. |

The new finite inheritance–novelty theorem strengthens the mathematical program. It does not close all seven obligations by itself. The next productive step is a corrected architecture specification retaining that theorem and explicitly addressing A1, A2 and N3.