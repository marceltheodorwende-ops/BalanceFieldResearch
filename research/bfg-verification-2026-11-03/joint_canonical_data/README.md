# Joint canonical data: coordinate equivalence and genuine initial alignment

Date: 3 November 2026. Existing BFG verification-stage continuation; no new physical law or origin rule.

## 1. Which additional source quantities are used

The earlier future-identifiability test used balance and count information, not the source's full canonical datum. This step uses the actual finite state's five stored roles

```math
X=(K,\rho_F,\rho_W,Y,P)
```

on a common carrier, modulo **simultaneous unitary** coordinate change. This is the November finite contract and September 26 minimal state, not a new observable family invented to rescue a result. P is the ordinary orthogonal persistent projector, not the generally non-Hermitian graph-metric projection.

The plugin's richer nine-role state and primitive capacities/recursion are not silently reconstructed from this five-tuple. The earlier noninjective rich-to-reduced examples still apply. All comparisons here hold the finite model's units and normalization convention fixed.

Additional coordinate-invariant data include carrier dimension, ranks, individual spectra, and **mixed invariants** such as tr(KY) and ||[K,Y]||_F. Carrier dimension already distinguishes the two-/four-configuration replicas. Within the same dimension, individual spectra need not fix relative operator alignment. A finite list of mixed traces is useful evidence, but is not claimed here to classify every possible tuple completely. The following exact test supplies the complete coordinate-equivalence criterion.

## 2. Exact simultaneous-unitary criterion

Let A=(A_1,...,A_m) and B=(B_1,...,B_m) be Hermitian n-by-n tuples. Define the complex linear intertwiner space

```math
\mathcal L(A,B)=\{S:B_j S=S A_j\ \text{for every }j\}.
```

**Theorem.** A and B are simultaneously unitarily equivalent if and only if L(A,B) contains an invertible S.

Proof: a unitary intertwiner is invertible. Conversely, if S is invertible, taking adjoints in B_j S=S A_j gives S* B_j=A_j S*. Hence `S*S A_j=A_j S*S`. Its positive square root Q and inverse also commute with all A_j. The polar factor U=S Q^(-1) is unitary and satisfies B_j U=U A_j. Thus B_j=U A_j U* for every j. QED.

A nonzero intertwiner is not enough: it might identify only a shared proper subspace. The controls include a one-dimensional intertwiner space all of whose elements are singular.

Choose a basis S_1,...,S_d of L by solving its linear equations. The condition becomes

```math
p(z_1,...,z_d)=\det\left(\sum_a z_a S_a\right)\not\equiv0.
```

This is an exact algebraic certificate. A nonzero polynomial has an invertible evaluation over C; since its degree in each variable is at most n, a full grid `{0,...,n}^d` would also contain one. An identically zero polynomial proves that all intertwiners are singular. This gives a finite mathematical decision method for concrete exact algebraic entries, with no fitted tolerance.

The executable checker accepts rational/algebraic Hermitian matrices, rejects floating input, computes the exact nullspace and determinant polynomial, and verifies explicit unitary witnesses when found. Its bounded coefficient search supplies a convenient witness; the yes/no decision uses the polynomial itself. This is not offered as a scalable algorithm for very large tuples, an exact comparator for unspecified transcendental input expressions, or a physical-admissibility validator. Non-Hermitian general operators require their adjoint relations too; the theorem is applied here to the Hermitian stored finite state.

## 3. Same individual spectra, different canonical joint data

Take

```math
K=\operatorname{diag}(-2,1),\quad
\rho_F=2\Pi,\quad \rho_W=\Pi,\quad
\Pi=\operatorname{diag}(1,0),\quad P=I,
```

and

```math
Y_a=\operatorname{diag}(1/4,1/2),\qquad
H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad
Y_b=H Y_a H^*.
```

All five individual matrix spectra match between X_a and X_b; K, formation, witness and P are literally held fixed. But

```math
\operatorname{tr}(K Y_a)=0,\qquad
\operatorname{tr}(K Y_b)=-3/8.
```

No simultaneous unitary can relate the tuples. The exact intertwiner space is zero, independently confirming the mixed-trace distinction. By contrast, applying H to **all five** fields is a pure coordinate change, and the checker constructs and verifies its unitary certificate. Changing one operator's orientation while leaving the other fields fixed is a different initial state.

This is not a new fundamental force or parameter. It is the joint geometry already carried by the source's stored matrices on a common carrier. Positivity and matching individual spectra do not erase it.

## 4. The unchanged event detects the alignment

Both Y choices lie strictly between zero and identity, so full input persistence and selection admit the compared event. The source load formulas give exact reciprocal weights

```math
\alpha_a=1/17,\qquad\alpha_b=13/101.
```

In a Y-eigenbasis the successor Gram eigenvalue at y is

```math
g_\alpha(y)=\frac{\alpha+(1-\alpha)y^2}{(1+y)^2}.
```

Therefore their successor Gram spectra differ:

| Initial alignment | Exact successor Y spectrum |
| --- | --- |
| Y_a, aligned | {32/425, 20/153} |
| Y_b, misaligned | {296/2525, 140/909} |

The successor kernels differ as well. In the aligned case K is inherited up to the active coordinate gauge and `||K_+||_F^2=5`. In the misaligned eigenframe K has diagonal entries -1/2 and off-diagonal magnitude 3/2. Its cross factor squared is

```math
c^2=\frac{(\alpha_b+(1-\alpha_b)y_1y_2)^2}
{(\alpha_b+(1-\alpha_b)y_1^2)(\alpha_b+(1-\alpha_b)y_2^2)}
=1152/1295.
```

Consequently

```math
\|K_+\|_F^2=1/2+(9/2)c^2=11663/2590<5.
```

These are exact consequences of the fixed finite event, not alternative successor rules. Four well-separated preserved-helper calls check this alignment pair and the next section's scalar pair against the analytic values. Their floating SVD output is not used as an exact equivalence or rank certificate.

## 5. Stored coordinate class versus behavioral quotient

Simultaneously equivalent input tuples have equivalent future outputs under the fixed covariant event; this follows from the existing complete-state sufficiency theorem and induction. No additional initial raw-recursion factor is needed for that event calculation.

The converse needs care. For

```math
P=\Pi,\quad K=\operatorname{diag}(-2,1),\quad
\rho_F=2\Pi,\quad\rho_W=\Pi,
```

compare Y_c=I/4 and Y_d=diag(1/4,1/2). The stored input tuples are not simultaneously equivalent. Their intertwiner space has dimension one but only singular members. Yet both Y commute with the one-dimensional persistent line and agree on it. Their first exact successors coincide:

```math
K_+=-2,\quad\rho_{F,+}=2,\quad\rho_{W,+}=1,
\quad Y_+=32/425,\quad P_+=1.
```

The transverse difference was discarded. The same complete scalar output then has the same further exact orbit by determinism.

Thus an observational signature that records only the successors can identify fewer distinctions than a signature containing the initial full stored tuple. The September full behavioral datum Xi_U must be interpreted with its actual source content; we do not automatically equate its quotient with either our earlier balance/count quotient or the stored simultaneous-unitary class. If initial canonical data are explicitly observed, they distinguish this pair; if deliberately discarded, that is a different observation contract.

## 6. What this establishes about the origin search

We now have a complete exact comparison criterion for the supplied finite joint state in the executable rational/algebraic sector. It removes coordinate ambiguity from comparisons of candidate initializers. It also identifies concrete source-canonical information missing from scalar or individual-spectrum descriptions: the relative alignment of the state roles.

Naming these invariants does not derive their initial values. A source premise must specify the joint source-neutral/capacity/identity geometry, or an actual state/preparation must supply it. Requiring a unique full signature without deriving its values would merely restate the desired origin theorem. The previous conditional channel/metric and operator bridges remain available; none is silently adopted as a uniquely forced law.

The positive result is an exact tool for distinguishing genuine candidate-state differences from coordinate copies, and a demonstrated case where those differences affect the event. The open result is the source necessity of the actual initial joint state, not its comparison once given.

Run `python joint_canonical_data/check_canonical.py`. Exact certificates and bounded implementation checks are in [results.json](results.json). [SOURCES.json](SOURCES.json) pins the role/contract sources and earlier plugin context. This does not prove the canonical nine-role correspondence, unique fundamental origin or empirical realization; the published paper and event rules remain unchanged.
