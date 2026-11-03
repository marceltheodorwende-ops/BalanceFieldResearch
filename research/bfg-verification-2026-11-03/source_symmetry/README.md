# Source symmetry, joint classes and original capacities

This milestone establishes a conditional symmetry restriction on matrix-valued initialization, proves why it cannot be transferred to quotient-valued initialization, and checks which information is lost when the original capacity tuple is replaced by its sum K. It does **not** derive a new BFG origin law or establish independence from every historical BFG premise. The preserved event and published preprint are unchanged.

The preceding [joint canonical analysis](../joint_canonical_data/README.md) showed that individual spectra do not determine a joint state. The next question is whether source symmetry itself determines that joint state. The answer depends on the output type and on which source objects are retained.

## 1. Single-valued matrix initialization from K alone

Let K be Hermitian on a finite-dimensional complex Hilbert space. Suppose a single-valued matrix assignment Y=F(K) is unitarily covariant:

    F(UKU*) = U F(K) U*.

Additional scalar spectral invariants of K may be arguments without changing this argument. If U stabilizes K, covariance gives UYU*=Y. Write K=sum_a lambda_a Pi_a with distinct eigenvalues. The stabilizer contains independent scalar phases on each eigenspace, eliminating off-diagonal blocks of Y, and every unitary within each eigenspace, forcing its diagonal block to be scalar. Therefore

    Y = sum_a y_a Pi_a,     [K,Y] = 0.

This is a pointwise restriction; the coefficient y_a may depend on the **entire** spectrum of K. It need not be the evaluation of a universal scalar function at lambda_a. A covariant, single-valued projector assignment from K alone likewise consists of complete eigenspaces. Adding inputs that are already spectral functions of K does not reduce its stabilizer and cannot evade the conclusion. A separately supplied non-spectral input can.

The September capacity source starts with a real Hilbert space. The analogous matrix result holds under the full orthogonal group: reflections separate blocks and all orthogonal transformations within a block force scalarity. The complex unitary version matches the common Hermitian finite-state convention used here. No real-to-complex physical identification is inferred.

### Consequence for the preserved finite event

Assume K,Y,P commute pairwise, Y is nonnegative, P is an orthogonal projector, and the fresh formation and witness densities are spectral in K. Consider a successful event, with positive selection mass and both positive branch loads. Its selector Q=1_[0,1)(Y) commutes with K,Y,P; the selected support is P_s=PQ. The G=I+Y metric projector onto this support is just P_s. With C=(I+Y)^(-1), B=YC and reciprocal weight 0<alpha<1, its stacked response is

    A = [sqrt(alpha) P_s C ; sqrt(1-alpha) P_s B].

The first branch is injective on P_s, so ker A=ker P_s. Consequently rank A=rank P_s and the inherited support fills the next carrier. There is no emergent complement and no seed. Also

    (K direct-sum K) A = A K.

Polar compression therefore gives K_next unitarily equivalent to K restricted to ran P_s. The next Y has eigenvalues h_alpha(y)=(alpha+(1-alpha)y^2)/(1+y)^2, strictly between zero and one. The next P is the identity, Y_next commutes with K_next, and subsequent successful events preserve K up to coordinates and cannot generate seeds. For the nonzero fresh formation retained by a successful first event, the later exact loads remain positive. Floating threshold termination is a separate implementation issue.

This restricts **formation spectrum and seeding**, not every observable: Y continues to evolve. It also does not guarantee that the first event passes its gates. The result is a conditional sector theorem, not a claim that all BFG states commute.

## 2. A unique class need not have an invariant representative

The preceding theorem requires an actual single-valued matrix F(K). A rule returning a joint equivalence class is different. For example, fix

    K = diag(-2,1),
    Y_theta = [[1/2, exp(i theta)/4], [exp(-i theta)/4, 1/2]].

Every Y_theta has spectrum {1/4,3/4} and fails to commute with K. All pairs (K,Y_theta) belong to **one** simultaneous-unitary class, since diagonal phase changes stabilize K and move theta. No member of that class is fixed by the whole stabilizer of K: diag(1,-1) reverses its off-diagonal entries.

An intrinsic relation can specify exactly this single class by requiring

    spectrum(Y)={1/4,3/4},
    tr((K - tr(K) I/2)(Y-I/2))=0.

Proof: write Y=[[a,z],[conjugate(z),1-a]]. The second condition forces a=1/2 because K has distinct eigenvalues; the specified determinant then gives |z|=1/4. The remaining phase is removed by the stabilizer. On the real source space z=+/-1/4 and the two representatives are related by a diagonal reflection, so the same distinction already occurs over the reals.

These equations are a **diagnostic example, not a BFG law**. They show that covariance does not by itself prohibit noncommuting, uniquely specified joint classes. Applying the matrix theorem to such a class would be invalid. What is still needed is a source implication fixing the relative invariants of that class; a new physical orientation object is not logically necessary for every quotient-based route.

## 3. The original capacity tuple retains more information

The September 22 source introduces three separately supplied self-adjoint capacities, distinction D_cap, coherence c and neutral admissibility aleph, and defines

    K = c + aleph - D_cap.

Replacing this tuple by K is a reduction, not an invertible reconstruction. For any Hermitian tuple S=(S_1,...,S_m), define its complex commutant

    C(S) = {X : XS_j=S_jX for every j}.

A single-valued covariant matrix output from S must commute with every unitary stabilizing S and hence belongs to C(C(S)). To see this without assuming a classification theorem, take a Hermitian X in C(S): exp(itX) stabilizes S, so differentiating its invariance relation at t=0 yields [X,Y]=0. Every element of C(S) splits into Hermitian real and imaginary parts, proving the claim. This is a necessary symmetry condition, not a construction of Y.

For an exact positive example take

    c=I,  aleph=[[2,1],[1,2]],  D_cap=[[5,1],[1,2]].

Their combination gives K=diag(-2,1). All three capacities are positive definite. Exact linear algebra gives:

| Inputs retained | Dimension of commutant | Dimension of double commutant |
|---|---:|---:|
| K alone | 2 | 2 |
| c, aleph, D_cap jointly | 1 | 4 |

Thus the full capacity tuple has only scalar phase stabilizers in this complex example and imposes no nontrivial pointwise matrix restriction through symmetry alone. In particular the following two parameter-free comparison formulas are both covariant and invariant under common positive capacity rescaling:

    Y_1 = aleph/tr(aleph) = [[1/2,1/4],[1/4,1/2]],
    Y_2 = (aleph/tr(aleph))^2 = [[5/16,1/4],[1/4,5/16]].

Their eigenvalues are respectively {1/4,3/4} and {1/16,9/16}. Both are positive contractions and noncommuting with K. Their different spectra make them inequivalent even under unconstrained unitary coordinate changes. Positivity and covariance alone therefore do not choose between these formulas. This does **not** assert that both satisfy every original BFG premise; it identifies exactly the symmetry packet that fails to select one. Neither formula is installed as an initialization rule. Original aleph is not silently identified with a later recursion metric or response operator.

## 4. Exact event consequences and numerical cross-check

Using the preserved event with K=diag(-2,1), rho_F=2 Pi, rho_W=Pi and P=Pi, where Pi=diag(1,0), gives:

| Supplied Y | Exact active rank | tr(Y_next) | Seed trace | tr(rho_F,next) |
|---|---:|---:|---:|---:|
| diag(1/4,1/2) | 1 | 32/425 | 0 | 2 |
| Y_1 | 2 | 1/5 | 2 | 4 |
| Y_2 | 2 | 5632/41307 | 2 | 4 |

The executable computes A*A with exact rational arithmetic, including its determinant. For Y_1 the determinant is 4/2025; for Y_2 it is 26214400/15356414241. These positive determinants establish rank two without a floating-point rank decision. Every row of A lies in the first coordinate of its respective copied carrier, so compression gives K_next=-2 I on its active carrier. In the rank-two cases the inherited support has rank one; the one-dimensional emergent complement has formation eigenvalue -2, giving seed trace 2 and full next persistence. These are genuine event differences caused by supplied Y, not empirical results.

Three fresh binary64 calls to the unchanged baseline confirm dimensions, formation, seed, next K, next P and next Gram trace. Four exact phase representatives verify the quotient example; exact commutant equations and a separate commuting-sector compression identity provide additional controls. The executable checks fixtures; the general statements above rest on the written proofs, not on exhaustive testing or a proof assistant.

## 5. What this resolves and the next source question

The symmetry question is now sharply separated into three cases: matrix initialization from K alone is spectrally restricted; quotient initialization can specify a noncommuting class without selecting a phase; retaining the original capacity tuple can remove the K-only symmetry obstruction. None of these facts fixes the actual numerical origin response.

The next useful source test is therefore specific: **does an existing BFG relation connect the original capacity tuple, or its joint invariant data, to the retained neutral response Y?** Such a relation must preserve operator roles and specify its domain. If the source instead fixes only a quotient, test the relative invariants directly rather than demanding an invariant matrix representative. The conditional Gram construction from a fully supplied channel and metric remains valid; it must not be mistaken for a derivation of those upstream data from K alone.

Source provenance is in [SOURCES.json](SOURCES.json), exact fixtures and implementation comparisons in [results.json](results.json), and the reproducible script is [check_symmetry.py](check_symmetry.py). Earlier global plugin context remains in [the source synthesis](../plugin_synthesis/README.md); this milestone is a focused mathematical analysis, not another theorem audit of all indexed source pages.

Reproduce from the research-stage folder using its documented dependencies:

```sh
python source_symmetry/check_symmetry.py
python validate_stage.py
```
