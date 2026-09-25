# Fundamental Closure Law

## 0. Authoritative status

This file defines the **current living finite BFG master-law candidate** and then records
its derived/conditional continuum refinements.

It distinguishes three epistemic levels:

1. **SOURCE-DERIVED / KNOWN MATHEMATICS APPLIED TO BFG** — follows from the cited BFG
   structures plus standard mathematics.
2. **DECLARED FINITE BFG COMPLETION RULE** — BFG-internal and no-retuning, but not
   uniquely forced by the historical source corpus.
3. **DECLARED CONTINUUM COMPLETION RULE** — used only to interpolate between committed
   finite steps; it is not part of the discrete finite law.

The historical source corpus alone does **not** uniquely force the complete successor
map. The living package does define a single-valued finite candidate after the declared
completion rules below are adopted.

This is not an established Theory of Everything and does not import GR, QFT, Standard
Model, Schrödinger, Einstein, Yang–Mills, or other sector equations as fundamental BFG
laws.

## 1. Current finite committed state

The authoritative rank-aware finite state is

\[
\boxed{
\Xi=
(
\mathcal H,
\mathfrak D,
\mathfrak c,
\aleph,
\rho_F,
\rho_W,
Y,
R_C
).
}
\]

with

\[
\rho_F\succeq0,\qquad \operatorname{tr}\rho_F>0,
\]

\[
\rho_W\succeq0,\qquad \operatorname{tr}\rho_W=1,
\]

\[
Y\succeq0.
\]

The ordinary persistent projector \(P_{\rm per}\) is derived from the peripheral Riesz
space of \(R_C\) and may be cached numerically. It is not an additional fundamental
state coordinate.

A vector \(d\) is not fundamental in the current state. When \(\rho_F\) is rank one,
\(d\) may be used only as a phase-dependent chart satisfying \(\rho_F=dd^\dagger\).

The committed finite state does not contain the continuum phase/memory coordinates.
Those belong to the optional continuum extension described later.

## 2. Exact finite source structures

Formation:

\[
K=\mathfrak c+\aleph-\mathfrak D.
\]

Neutral pair and neutral metric:

\[
C_N(Y)=(I+Y)^{-1},
\qquad
B_N(Y)=Y(I+Y)^{-1},
\qquad
G=I+Y,
\]

\[
C_N+B_N=I.
\]

Exact neutral contrast:

\[
Z(Y)=C_N(Y)-B_N(Y)
=(I-Y)(I+Y)^{-1}.
\]

Finite persistence is the repaired isolated peripheral Riesz sector of \(R_C\).
The \(G\)-orthogonal projector onto that sector is used in reciprocal load analysis.

For a selected persistent projector \(P^{(G)}\), the density loads are

\[
\Lambda_C
=
\operatorname{tr}
\left(
G P^{(G)}C_N\rho_F C_N P^{(G)\dagger}
\right),
\]

\[
\Lambda_B
=
\operatorname{tr}
\left(
G P^{(G)}B_N\rho_F B_N P^{(G)\dagger}
\right).
\]

For strictly positive dual loads,

\[
\alpha
=
\frac{\Lambda_B}{\Lambda_C+\Lambda_B},
\qquad
\beta
=
\frac{\Lambda_C}{\Lambda_C+\Lambda_B}.
\]

## 3. Declared finite completion rules

The living finite candidate is single-valued only after the following three
BFG-internal completion rules are adopted.

### 3.1 Intrinsic-Gram successor load — DECLARED FINITE COMPLETION

After the selected cross-fed analysis map has reduced SVD

\[
\mathcal A=U\Sigma V^\dagger,
\]

the active successor load is declared to be

\[
\boxed{
Y_+=\Sigma^2
}
\]

in reduced target coordinates.

The historical corpus motivates positive Gram reconstruction but does not uniquely
force this identification with the cross-fed analysis Gram. Therefore this is not
labelled source-derived.

### 3.2 Neutral-Contrast Selection — DECLARED FINITE COMPLETION

The source Selection rule is sign based:

\[
S_A(x)=\mathrm{retain}
\iff
\Delta C_A(x)>0.
\]

The living package identifies the closure-gain sign with exact neutral contrast:

\[
\boxed{
\operatorname{sign}\Delta\mathcal C_A
=
\operatorname{sign}Z(Y).
}
\]

Hence

\[
\boxed{
Q_{\rm retain}
=
\mathbf1_{(0,\infty)}(Z(Y))
=
\mathbf1_{[0,1)}(Y)
}
\]

spectrally.

The **ordering** \(A\to S_A\to T_A\) is source BFG; the specific
Neutral-Contrast identification is the declared completion.

### 3.3 Neutral transverse recursion — DECLARED FINITE COMPLETION

After inherited/seeded persistence determines the exact successor projector \(P_+\),

\[
\boxed{
R_{C,+}
=
P_+
+
(I-P_+)C_N(Y_+)(I-P_+).
}
\]

This preserves the protected persistent sector and uses only the already-defined
neutral retained response on its complement. The historical source corpus does not
uniquely force this successor recursion.

## 4. Authoritative finite update order

The official finite candidate uses **Selection before next-state reclosure**.

Given \(\Xi_n\):

1. compute \(K_n\), \(C_n\), \(B_n\), \(G_n\), and \(Z_n\);
2. derive the current persistent Riesz projector;
3. apply current-state Neutral-Contrast Selection \(Q_n^{\rm sel}\);
4. use R4 polar transport to retain the closure-positive source witness/formation;
5. compute the \(G_n\)-orthogonal selected persistent projector;
6. compute density reciprocal loads and \((\alpha_n,\beta_n)\);
7. build the selected cross-fed analysis map;
8. take its reduced SVD \(\mathcal A_n=U_n\Sigma_nV_n^\dagger\);
9. set \(Y_{n+1}=\Sigma_n^2\) by the intrinsic-Gram completion;
10. transport \(\mathfrak D,\mathfrak c,\aleph\) to the active target;
11. transport inherited witness and formation by the R4 polar rule;
12. if an emergent complement exists, apply the existing simple-negative-ground
    no-choice formation seed;
13. set \(P_{n+1}\) to inherited persistent support plus the canonical seed projector;
14. rebuild \(R_{C,n+1}\) by the neutral transverse recursion rule.

The next carrier is the reduced active range, so

\[
\boxed{
\dim\mathcal H_{n+1}
=
\operatorname{rank}\mathcal A_n
\le
\dim\mathcal H_n.
}
\]

## 5. Exact terminal conditions versus numerical ambiguity

Exact structural/no-choice stops include, as applicable:

- no persistent source;
- no closure-positive selected source sector;
- exact witness annihilation;
- exact formation annihilation;
- exact zero dual branch load;
- zero analysis map;
- required emergent block lacking a unique simple negative ground seed.

Floating uncertainty is **not** promoted to physical terminality.

Examples of numerical-only stops include:

- `dual_load_numerical_ambiguity`;
- `numerical_rank_ambiguity`;
- `neutral_contrast_boundary_ambiguity`.

Exact zero branch load uses the distinct reason

- `dual_load_zero_terminal`.

## 6. Source-only underdetermination versus living candidate

Two earlier obstruction results remain important:

- positive Gram form alone does not uniquely select \(Y_+\);
- bounded persistence alone does not uniquely select \(R_{C,+}\).

Those are statements about the historical/source-only theory.

The living package closes them **conditionally** by the explicit finite completion
rules in Section 3.

Likewise, the source Selection axiom does not itself identify a universal gain
operator. The living package closes the sign choice conditionally by the
Neutral-Contrast Selection principle

\[
\Delta\mathcal C_A:=Z(Y)
\]

as the simplest normalized representative.

Thus the correct current statement is

\[
\boxed{
\text{source corpus alone: underdetermined;}
\qquad
\text{living finite candidate: deterministic conditional on declared completions.}
}
\]

See `TWO_LAW_OBSTRUCTION_THEOREM.md`,
`CANONICAL_SELF_RECLOSURE_AXIOM.md`,
`NEUTRAL_CONTRAST_CLOSURE_GAIN.md`, and
`UNIVERSAL_STATE_UPDATE_CANDIDATE.md`.

## 7. Continuum boundary

The continuum constructions later in this file do not alter the committed finite law.

In particular, affine interpolation in closure depth

\[
H=-\log Y
\]

is a **DECLARED CONTINUUM COMPLETION RULE**, and branch-continuity memory is likewise a
continuum rule.

Recursive phase \(\Omega\) and continuation memory \(M_b\) are used only for the
continuous suspension between committed finite states.

At the commit surface, the finite update in Section 4 remains authoritative.

## 8. Current claim boundary

Established within the current finite candidate:

- exact typed state and category conditions;
- exact neutral pair and reciprocal loads;
- source-faithful Selection-first ordering;
- deterministic successor under the three declared finite completions;
- carrier-dimension nonincrease;
- exact/numerical boundary separation;
- rank-aware witness/formation separation.

Not established:

- that the historical BFG corpus uniquely forces the three completion principles;
- a unique global smooth continuum law;
- derivation of spacetime, gravity, gauge/matter sectors, quantum statistics, or
  cosmology from the finite law;
- an established Theory of Everything claim.

## Fixed-stratum operator continuum

If a selected fixed carrier satisfies the stronger modewise closure

\[
Y_+=f(Y),
\qquad 0<Y\le I,
\]

then spectral functional calculus lifts the scalar Böttcher coordinate to

\[
\Theta(f(Y))=2\Theta(Y).
\]

Hence

\[
\Theta(Y(\tau))=e^\tau\Theta(Y_0)
\]

is an exact unitary-covariant operator semigroup with

\[
F_{\log2}(Y)=f(Y).
\]

This theorem applies only inside a fixed modewise stratum. The general BFG master map
contains noncommuting state dependence, SVD/polar transport, Selection, rank change and
formation events, so the global continuum remains a stratified hybrid-generator
problem.

See `FIXED_STRATUM_OPERATOR_CONTINUUM.md`.


## Coupled commuting stratum and frozen noncommuting generator

The full selected commuting multi-mode update is not a collection of independent
scalar maps. With diagonal formation weights \(r_i\),

\[
\Lambda_C=\sum_i\frac{r_i}{1+y_i},
\qquad
\Lambda_B=\sum_i\frac{r_i y_i^2}{1+y_i},
\]

and one global reciprocal pair \(\alpha,\beta\). Therefore

\[
y_i^+
=
\frac{\alpha+\beta y_i^2}{(1+y_i)^2}.
\]

The common diagonal algebra is invariant under the successful selected reclosure, and
the isotropic ray \(Y=yI\) reduces exactly to the scalar Böttcher map.

Separately, for frozen \(Y,P,\alpha,\beta\), the noncommuting formation sector obeys
the exact Schur reclosure

\[
K_+=\Chi\circ K,
\]

which has the continuous Hermiticity-preserving embedding

\[
K(\tau)=\Chi^{\circ\tau/\log2}\circ K_0.
\]

This does not in general define a positive/CP semigroup on arbitrary positive
matrices at fractional times.

See `COMMUTING_AND_NONCOMMUTING_CONTINUUM.md`.


## Frozen Schur CP-embeddability boundary

For frozen noncommuting formation reclosure, let

\[
D_{ij}=-\log\chi_{ij},
\qquad
J=I-\frac1n\mathbf1\mathbf1^T.
\]

Standard Schoenberg theory gives the exact positivity criterion

\[
-\frac12JDJ\succeq0
\]

for the fractional Schur interpolation to remain positive/CP at every recursive time.
All two-mode BFG multipliers satisfy this criterion; a deterministic three-mode BFG
multiplier with \(\alpha=\beta=1/2\) and \(y=(0.1,1,10)\) does not.

See `FROZEN_SCHUR_CP_EMBEDDABILITY.md`.


## Canonical two-channel CP suspension

For frozen neutral geometry,

\[
\tan\theta_i=\sqrt{\beta/\alpha}\,y_i
\]

gives

\[
\chi_{ij}=\cos(\theta_i-\theta_j).
\]

Therefore

\[
\chi_{ij}(s)=\cos(s(\theta_i-\theta_j)),
\qquad 0\le s\le1,
\]

is a correlation matrix for every within-step fraction.

This yields a continuous CP path through every frozen BFG one-step reclosure, even
when the frozen Schur channel is not infinitely divisible and therefore has no
time-homogeneous entrywise-power CP semigroup.

In a fixed-support gauge, the same CP path may be applied to
\(\mathfrak D,\mathfrak c,\aleph\), while the inherited
\(\rho_F,\rho_W,Y,R_C\) remain frozen. This gives the first positive continuous frozen
full-state path.

See `CANONICAL_TWO_CHANNEL_CP_SUSPENSION.md`.


## Phase-anchored state suspension

The discrete BFG master law fixes successor closures but does not uniquely determine
the continuous positive load path between them.

Two different unitary-covariant admissible bridges already exist between the same
strictly positive selected endpoints:

\[
Y_{\rm aff}(s)=(1-s)Y_0+sY_1,
\]

and

\[
Y_{\log}(s)
=
\exp\!\left(
(1-s)\log Y_0+s\log Y_1
\right).
\]

Therefore the living package explicitly adopts affine interpolation in closure depth

\[
H=-\log Y
\]

as a **new continuum completion principle**, not as a previously derived discrete BFG
theorem.

Using a normalized recursive phase \(\omega\) and a committed source anchor produces
an extended suspension state

\[
\widehat\Xi=(\Xi_\star,\omega),
\]

whose readout is continuous inside a no-event stratum and which commits the exact
discrete update when \(\omega=1\).

For equal-rank full-overlap R4 support motion, principal-angle interpolation gives a
continuous projector path whose endpoint partial isometry is exactly
\(\operatorname{polar}(P_1P_0)\).

Exact projector rank cannot change continuously in finite dimension, so rank-changing
BFG transitions remain genuine stratum events under the current persistence semantics.

See `PHASE_ANCHORED_STATE_SUSPENSION.md`.


## Local anchor elimination and memory criterion

For a within-step suspension

\[
X=\mathcal I_\Omega(X_\star),
\]

the committed anchor is not fundamentally required on every chart.

Whenever

\[
D_{X_\star}\mathcal I_\Omega
\]

is invertible, the inverse-function theorem yields a local reconstruction

\[
X_\star=\mathcal I_\Omega^{-1}(X),
\]

and therefore the phase-local law

\[
\boxed{
\dot X
=
\frac1{\log2}
\partial_\Omega\mathcal I_\Omega
\left(
\mathcal I_\Omega^{-1}(X)
\right),
\qquad
\dot\Omega=\frac1{\log2}.
}
\]

For the selected scalar/isotropic closure-depth suspension this inversion is global on
every open step, so \((Y,\Omega)\) already suffices.

Memory \(M\) becomes mathematically necessary only on non-injective continuation charts
where identical \((X,\Omega)\) readouts correspond to different future tangents.

The source BFG persistence channel supports this role but does not supply a universal
closed-form memory update.

See `LOCAL_ANCHOR_ELIMINATION_THEOREM.md`.


## Continuation-branch memory

The coupled commuting suspension develops genuine fold surfaces.

An explicit selected two-mode state has three distinct anchors mapping, at the same
recursive phase, to one identical readout while producing different local tangents.

Therefore a global law on \((X,\Omega)\) alone is impossible for the chosen continuum
completion.

The minimal extension is not a full anchor copy but a continuation-branch label

\[
M_b.
\]

On a branch,

\[
X_\star=\mathcal R_{\Omega,M_b}(X),
\]

and

\[
\dot X
=
\frac1{\log2}
\partial_\Omega
\mathcal I_\Omega
(\mathcal R_{\Omega,M_b}(X)).
\]

The living package adopts branch continuity

\[
\dot M_b=0
\]

between fold/event surfaces, with branch changes only when admissibility or an exact BFG
event forces them.

See `LOCAL_ANCHOR_ELIMINATION_THEOREM.md`.


## Simple-fold memory refinement

The first deterministic singularity of the coupled two-mode phase suspension is a
generic corank-one simple fold.

At the certified point,

\[
\sigma(D_aF)\approx(0.84798,\ 1.6\times10^{-11}),
\]

while

\[
\ell^TD_a^2F[v,v]\ne0
\]

and recursive phase unfolds the fold transversely.

Therefore local inverse geometry is Whitney-fold type: two continuation sheets meet at
the fold.

Near one isolated fold, a single local branch bit is sufficient. The fold itself is
not a BFG terminal event because the forward suspension remains smooth there.

The explicit three-anchor same-readout witness proves that one bit is not globally
sufficient. Global memory is a branch/chart identifier that becomes redundant on
injective charts.

See `SIMPLE_FOLD_MEMORY_THEOREM.md`.


## Global memory-graph lower bound

The coupled commuting suspension admits a constructive exponential branch family.

A fixed-alpha scalar subproblem has three nondegenerate selected roots for one readout.
Using one dominant formation mode to pin the global reciprocal weight and \(n-1\)
weakly weighted secondary modes gives, in the decoupled limit,

\[
3^{n-1}
\]

continuation branches.

Because every product root has invertible Jacobian, all branches persist for
sufficiently small strictly positive secondary formation weights.

Therefore no dimension-independent finite branch-state memory can represent all
finite-dimensional admissible continuation charts under the current continuum
completion.

The binary information lower bound is

\[
\boxed{
b_n\ge
\left\lceil
(n-1)\log_2 3
\right\rceil.
}
\]

This does not yet prove unbounded memory growth along one committed BFG orbit.

See `GLOBAL_MEMORY_GRAPH_THEOREM.md`.


## Carrier-dimension monotonicity and full-persistence lock

The cross-fed analysis operator satisfies

\[
\mathcal A_n:\mathcal H_n\to\mathcal H_n\oplus\mathcal H_n,
\]

but the next carrier is its reduced range. Hence

\[
\boxed{
\dim\mathcal H_{n+1}
=
\operatorname{rank}\mathcal A_n
\le
\dim\mathcal H_n.
}
\]

So a finite initial carrier uniformly bounds every later carrier and persistence rank.

Repeated persistence growth can nevertheless occur inside that carrier; the package
contains a deterministic exact orbit

\[
2\to3\to4
\]

at fixed carrier dimension \(4\).

Once

\[
P=I,
\qquad
0<Y<I,
\]

the entire carrier is retained, the analysis map has full column rank, no emergent
complement remains, and the successor again satisfies \(P_+=I\), \(0<Y_+<I\).

Thus full persistence is a forward-invariant selected lock class.

See `CARRIER_DIMENSION_MONOTONICITY_THEOREM.md`.


## Fixed-dimension memory tameness

For fixed finite \(d\), the coupled commuting closure-depth suspension is definable in
the real exponential field.

Known o-minimal uniform-finiteness theorems therefore imply a finite constant \(B_d\)
bounding every **finite** anchor fiber of this fixed definable family.

Together with carrier monotonicity

\[
d_n\le d_0,
\]

this gives a uniform finite branch-label bound along every finite-fiber chart of one
orbit starting from finite \(d_0\).

Thus the only remaining route to genuinely non-finite continuation memory is a
positive-dimensional inverse fiber whose members have different continuation tangents.

See `FIXED_DIMENSION_MEMORY_TAMENESS.md`.


## Reciprocal-alpha fiber reduction

For fixed phase \(\Omega\) and fixed global reciprocal weight \(\alpha\), the inverse
load equation separates mode by mode.

Its derivative is controlled by a cubic polynomial with at most two positive critical
points. Therefore each selected mode has at most three inverse roots, and for

\[
\Omega\le\frac13
\]

the inverse is unique.

Hence a \(d\)-mode fixed-\(\alpha\) inverse problem has at most

\[
3^d
\]

coordinate sheets.

Since every anchor fiber maps finite-to-one to the one-dimensional reciprocal interval

\[
0<\alpha<\frac12,
\]

any positive-dimensional inverse fiber in the full-persistent commuting load sector has
dimension at most one.

Thus even the remaining continuous-memory case needs at most one real reciprocal
coordinate plus a finite sheet label.

See `RECIPROCAL_ALPHA_FIBER_REDUCTION.md`.


## Authoritative-status reminder

The authoritative discrete finite status is defined in Sections 0–8 above. Later continuum sections are conditional refinements and do not reclassify declared finite completion rules as source-derived.
