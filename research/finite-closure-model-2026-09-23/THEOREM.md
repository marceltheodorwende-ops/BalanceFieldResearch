# An explicit finite conditional completion of BFG reclosure

Date: 23 September 2026. BFG source framework: Marcel Theodor Wende. AI-assisted derivation. This is an explicit reduced-state model extension, not a claim that the original BFG axioms uniquely force its reconstruction law.

## 1. Declared category and additional laws

Let H be a nonzero finite-dimensional complex Hilbert space. A state is

```math
S=(\rho,K,Y,R),\qquad \rho=dd^*\ne0,\quad K=K^*,\quad Y>0,
\quad \sup_{n\ge0}\|R^n\|<\infty. \tag{1}
```

States are identified under simultaneous unitary change of coordinates. rho is a positive rank-one operator, retaining profile magnitude but removing global phase. This is a reduced formation-state category; separately stored source capacities are not reconstructed merely by naming K. No real two-polarity assertion is made for this complex category.

Use the repaired peripheral space W from the [finite amendment](../finite-repair-2026-09-23/REPAIR.md), and its G-orthogonal projector P for G=I+Y. Retain the distinct spectral projector E for dynamical statements. Put

```math
C=(I+Y)^{-1},\ B=Y(I+Y)^{-1},
\quad \ell_k=\operatorname{tr}(GPC\rho CP^*),
\quad \ell_u=\operatorname{tr}(GPB\rho BP^*). \tag{2}
```

When either load vanishes, or W is zero, define U(S)=bottom. Otherwise define

```math
\alpha=\ell_u/(\ell_k+\ell_u),\quad\beta=\ell_k/(\ell_k+\ell_u),
\quad A=\begin{bmatrix}\sqrt\alpha PC\\\sqrt\beta PB\end{bmatrix}.
\quad Q=(A^*A)^{1/2},\ J=AQ^+. \tag{3}
```

Let H_a=(ker A)^perp. J restricted to H_a is an isometry. Work on H_a as the next carrier, identified with Ran J through this isometry. Define

```math
K_+=J^*(K\oplus K)J|_{H_a},
\qquad Y_+=A^*A|_{H_a}. \tag{4}
```

The second equation is **the selected intrinsic-Gram law of this model**. It is available from existing data but is not uniquely forced by positivity. It resembles the Studio reference carrier's Gram choice, now explicitly restricted to active support to avoid a singular load on a redundant ambient complement.

If K_+ has no simple negative lowest eigenvalue, define U(S)=bottom. Otherwise, for its ground spectral projector Pi_0 and eigenvalue lambda_0, set

```math
\rho_+=(-\lambda_0)\Pi_0,
\qquad R_+=\exp(i\tau K_+),\qquad \tau\in\mathbb R\text{ fixed}. \tag{5}
```

The unitary recursion law is a **second explicit model choice**; tau=1 is the implementation default, not a newly derived BFG constant. After a successful step the entire next carrier is peripheral. This excludes nontrivial subsequent stable/peripheral splitting inside that reduced carrier; it is a material modeling restriction, not a solution for arbitrary prescribed recursion laws. Set U(bottom)=bottom.

## 2. Closure theorem and proof

**Theorem.** With the chosen laws (4)-(5) and fixed tau, U is a single-valued map on the unitary equivalence classes of (1), together with bottom. Every finite iterate exists in exact mathematics. This does not imply every iterate is nonterminal, convergence, or uniform numerical conditioning.

**Proof.** Power boundedness supplies a unique peripheral/stable decomposition, including for nonnormal R; the peripheral block is semisimple, and stable Jordan blocks are permitted. Positive G supplies a unique metric projector. Equation (2) consists of squared G norms, so its values are nonnegative. In the nonterminal branch they give unique positive weights in (3).

A is finite and nonzero. On H_a, A is injective, so for every nonzero x in H_a, <x,Y_+x>=||Ax||^2>0. Thus Y_+ is positive definite. Polar transport gives a self-adjoint K_+ by isometric compression. The simple negative ground gate makes rho_+ nonzero positive rank one, without choosing an eigenvector phase. Finally (5) is unitary since K_+ is self-adjoint, so all positive powers of R_+ have norm one. Hence the output is again in category (1).

Every construction is covariant under simultaneous unitary coordinate change: spectral subspaces, metric projections, functional calculus, traces and polar transport transform by the corresponding unitaries. Different orthonormal bases of H_a therefore yield simultaneously unitarily equivalent next quadruples. The map descends to the stated quotient. An arbitrary deterministic coordinate representative is not claimed to be a distinguished physical vector. Adding bottom gives a total map on the declared exact category; induction defines all finite iterates. QED.

The original Schur novelty equivalence can be applied on a step only when its ordinary-orthogonality and neutral-compatibility hypotheses hold. They need not hold at the first nonnormal step here. After the first successful step R_+ is unitary on the full reduced carrier, so P=I at the next step and neutral compatibility holds. The closure theorem itself does not rely on the Schur equivalence at incompatible steps.

## 3. Explicit factor reconstruction and its boundary

For the load already selected in (4), choose the square-root factor gauge

```math
B_{C,+}=Y_+^{1/2},\quad W_{N,+}=I,\quad L_{C,+}=I,
\quad H_+=B_{C,+}^*W_{N,+}B_{C,+}=Y_+. \tag{6}
```

Then L_C,+* H_+ L_C,+=Y_+ exactly. Equation (6) is an explicit factor assignment, not a demonstration that historical BFG meanings force those factors. It is compatible with a product B_C=D_K F under the **declared factor gauge** D_K=I, F=Y_+^(1/2). If D_K is independently specified instead, this assignment cannot overwrite it: invertible D_K requires F=D_K^(-1)B_C, while singular D_K requires Ran(B_C) subset Ran(D_K). Here B_C is invertible, so a singular square D_K cannot satisfy that product on the same full active space. Extra constraints on F require separate checks.

These distinctions are essential: an explicit admissible reconstruction proves existence for this reduced model, not uniqueness across all BFG interpretations. The earlier positive-load ambiguity examples remain valid.

## 4. Nontrivial exact iteration and numerical conditioning

In one dimension take rho=1, K=-1, Y=y>0 and |R|=1. Equations (2)-(5) give

```math
K_+=-1,\quad\rho_+=1,\quad R_+=e^{-i\tau},
\quad y_+=\frac{2y^2}{(1+y)^2(1+y^2)}>0. \tag{7}
```

Thus the model has an infinite nonterminal exact orbit, not merely the trivial all-terminal totalization. This scalar example has no spectral novelty. For small y, the update is asymptotic to 2y^2, so no uniform lower load bound follows. A positive exact orbit can become numerically unresolved rapidly. The code reports ambiguity at such thresholds rather than treating finite precision as a proof of mathematical termination or success.

The first 20-step numerical expectation in this stage failed because a dual load approached zero. The thresholds and laws were not retuned to make that run pass. The revised regression checks the actual numerical contract: each computed state preserves the category or an explicit ambiguity is raised. Exact arbitrary-iteration existence is supported by the proof, not by claiming a 20-step floating run succeeded.

## 5. A bounded infinite-dimensional entry class

A restricted extension is possible without unbounded products. Let H be separable, K bounded self-adjoint, Y bounded with Y>=mI for some m>0, rho=dd* nonzero, and R bounded and power bounded. Assume its peripheral spectrum is isolated, its peripheral Riesz range is finite dimensional, and the spectrum on the invariant stable complement has radius strictly below one.

The stable powers then decay in operator norm by the spectral-radius formula. The finite peripheral block is semisimple. Its G-metric projector has finite rank. Thus A in (3) is finite rank, with finite-dimensional H_a and closed range; the pseudoinverse on its nonzero singular support is bounded. Equations (4)-(5) therefore produce either bottom or a finite-dimensional state of (1), after which the closure theorem applies. This proves a restricted bounded-operator reduction theorem, not an arbitrary infinite-dimensional closure theorem.

Example: H=l2, R=diag(1,1/2,1/2,...), Y=I, K=-I and d=e1 reduce to the scalar nonterminal example after one step. This is a mathematical realization, not a measured natural carrier.

Unbounded loads/capacities, infinite-rank persistent supports, peripheral continuous spectrum without the stated decomposition, and transport of unbounded form domains are not covered.

## 6. Disposition of the seven obligations

| Obligation | This model | General source claim |
| --- | --- | --- |
| Full update | Reduced quadruple update defined and proved closed | Full original state tuple still needs all of its component laws |
| Factor reconstruction | Explicit square-root gauge | Internal uniqueness and independently constrained D_K,F remain unresolved |
| Gram rebuild | Chosen intrinsic-Gram law, positive on active support | Not uniquely forced by prior positivity conditions |
| Recursive transport | Chosen unitary successor | Arbitrary intended successor recursion not derived |
| Iteration | Total exact finite iteration, absorbing bottom, nonterminal example | No universal natural realization or no-collapse theorem |
| Nonnormal case | Any finite power-bounded input in the exact theorem | Floating admission is not a general exact certificate |
| Infinite-dimensional realization | Bounded operators with finite peripheral rank reduce to finite model | General unbounded/infinite-rank case open |

This is a constructive conditional strengthening. Calling every original obligation universally solved would exceed the result.
