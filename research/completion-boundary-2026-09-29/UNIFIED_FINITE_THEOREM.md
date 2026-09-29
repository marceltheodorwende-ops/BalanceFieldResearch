# Unified finite neutral spine: conditional full-state preservation

**Scope.** This is a source-aligned mathematical assembly of the already **declared** finite rules in [Fundamental Closure Law](../fundamental-closure-2026-09-25/package/research/bfg-fundamental-closure/FUNDAMENTAL_CLOSURE_LAW.md) and the [Master State](../fundamental-closure-2026-09-25/package/research/bfg-fundamental-closure/MASTER_STATE.md). It does not promote their historical derivation status. All carriers below are finite-dimensional complex Hilbert spaces with specified inner products; the real case is the invariant real restriction. Exact terminal gates are part of the map, and numerical ambiguity is not exact terminality.

## 1. One neutral algebra and three role assignments

**Gram.** For the BFG canonical quadratic completion

```math
J_A(D,\nu)=\tfrac12\|D-A^*\nu\|^2+\tfrac12\|\nu\|^2,
```

the unique minimizer is `(I+AA*)^−1 AD`. Its reduced quadratic form is `(I+A*A)^−1`. If that form is by definition the neutral retained operator `C_N(Y)` of **this same** mediation in fixed metrics, injectivity of the inverse gives `Y=A*A` on active source support. Polar transport `A=J(A*A)^{1/2}` gives `Y_+=J(A*A)J*=(AA*)|Ran A`, represented by `Σ²` on the active target. In the weighted target metric, the corresponding source pullback is `A*H A`; the metric must be explicitly fixed. The Gram identification is thus a theorem **inside the chosen quadratic completion and role identification**, not a deduction of that completion from historical Level 0.

**Selection.** For any positive `Y`, put `C=(I+Y)^−1`, `B=I−C`, and `Z=C−B`. The algebraic identity `C²−B²=Z` holds because the two functions of `Y` commute and add to identity. Hence for each source vector `d`,

```math
\|Cd\|^2-\|Bd\|^2=\langle d,Zd\rangle.
```

If the BFG closure gain on a spectral channel is the difference of these **equal-metric squared channel responses**, then `gain>0` iff the corresponding eigenvalue of `Y` is below one. The same sign follows for the BFG metric `G=I+Y`: since it commutes with both channels, `||Cd||_G²−||Bd||_G²=<d,GZ d>=<d,(I−Y)d>`. The selected projector is `1_(0,∞)(Z)=1_[0,1)(Y)`. This supplies a sufficient internal meaning for the declared gain-sign rule in both stated metrics. Choosing this difference as the physically relevant gain is still a constitutive identification; the bare stationary equation for `J_A` does not name it.

**Recursion.** Let `P_+` be the ordinary orthogonal projector onto the selected inherited/seeded target persistence and `Q_+=I−P_+`. The declared rule uses the already computed target retained response and **then** projects its transverse output:

```math
R_{C,+}=P_++Q_+(I+Y_+)^{-1}Q_+.
```

This is a definite order of operations, not a unique consequence of power boundedness. It is generally different from minimizing a quadratic objective only after restricting it to `Ran Q_+`, whose response would be `(I_Q+Q_+Y_+Q_+|Q)^−1`. The exact `8/15` versus `1/2` example in [README](README.md) proves this even for a strictly positive two-dimensional `Y`. Thus one common quadratic spine makes G, S, R mutually compatible; it cannot silently erase the three role/ordering identifications.

## 2. Conditional rank-aware finite-state theorem

**Data and gates.** Let the input be the typed rank-aware state

```math
\Xi=(\mathcal H,\mathfrak D,\mathfrak c,\aleph,\rho_F,\rho_W,Y,R_C),
```

with Hermitian capacities, `rho_F>=0`, `tr rho_F>0`, `rho_W>=0`, `tr rho_W=1`, `Y>=0`, and a finite power-bounded `R_C`. Use the repaired peripheral Riesz subspace, the declared source Selection before reclosure, the `G=I+Y` metric projector, positive dual reciprocal loads, and the selected cross-fed analysis operator `A`. Return the absorbing terminal symbol when any exact admission gate fails. On a successful branch assume `rank A=r>0`, reduced SVD `A=UΣV*` with all `σ_i>0`, and the precise source/target witness polar transport `T` specified in the Master State. Assume the witness survival mass

```math
m=\operatorname{tr}(T^*T\rho_W)>0
```

and apply the existing formation gate: if a new orthogonal complement needs a seed, it has a simple negative ground eigenspace and the prescribed positive seed; if not, inherited formation is required to have positive trace. Let the inherited persistent support plus seed support form the specified nonzero `P_+` (orthogonal sum); an empty required persistent support is terminal.

**Theorem.** With these already declared laws and successful gates, the full target tuple is a well-typed finite BFG state, unique up to simultaneous unitary choice of active frames. Its neutral load is strictly positive on the active carrier; the witness remains normalized; the formation density is positive with nonzero trace; the successor recursion is power bounded with peripheral space exactly `Ran P_+` when `P_+!=0`; and `dim H_+=r<=dim H`. Together with the absorbing terminal symbol, the exact selected finite update admits a well-defined next step and hence every finite iterate. The theorem does **not** assert that every iterate is nonterminal, that a natural carrier exists, or that the declared laws are historically necessary.

**Proof.** A finite power-bounded operator has no exterior spectrum or nontrivial Jordan block on its unit circle, so its peripheral Riesz sector is well-defined and semisimple. `G>0` makes the selected metric projection unique. The positive dual-load gate gives unique positive reciprocal weights, hence a fixed `A`; its reduced polar factor and active range do not depend on singular-vector basis choices.

The positive singular values make `Y_+=Σ²>0` on the `r`-dimensional active target. Capacity transport `U*(capacity⊕capacity)U` preserves Hermiticity (and any positive semidefiniteness separately assumed for a capacity), so `K_+=c_++aleph_+−D_+` is Hermitian. For the partial isometry `T`, positive congruence gives `T rho_W T*>=0`, and cyclicity of trace yields `tr(T rho_W T*)=tr(T*T rho_W)=m`; division by the positive gate mass normalizes the new witness to trace one. The inherited formation `T rho_F T*` is positive. The optional no-choice seed `rho_E=(−lambda_0)Pi_E` is positive because `lambda_0<0`, and its orthogonal support makes `P_+=TT*+Pi_E` an orthogonal projector. The explicit formation-survival gate gives `tr rho_F,+>0`. Thus the two densities keep their distinct types, including at rank events admitted by these gates.

Put `C_+=(I+Y_+)^−1`; since the target is finite and `Y_+>0`, `0<C_+<=qI` with `q=1/(1+lambda_min(Y_+))<1`. With `Q_+=I−P_+`, the recursion has orthogonal blocks `I` on `Ran P_+` and `Q_+C_+Q_+` on `Ran Q_+`. The latter has norm at most `q` and positive spectrum, so powers remain bounded, it decays geometrically, and the peripheral range is precisely `Ran P_+` if nonempty. All stated operations are intrinsic spectral calculus, traces, partial isometries, or compressions and therefore covariant under simultaneous unitary changes. A simple ground projector is intrinsic even when an eigenvector has an arbitrary phase. `rank A<=dim H` because `A` has that source dimension. The output is typed, or the exact gate selected the absorbing terminal state; induction gives all finite iterates. ∎

**Boundary.** The theorem is conditional on the full update's stipulated gates, support and seed semantics. It does not construct independent historical `B_C,W_N,L_C` factors wherever additional role constraints apply. It does not supply uniform conditioning, an infinite-dimensional domain theorem, a unique autonomous continuum suspension, strong emergence or identification of a physical mediator. Source statements [F135 and F133–F134](../fundamental-closure-2026-09-25/package/research/bfg-fundamental-closure/CLAIMS.md) retain these distinctions.

## 3. Why the conditional theorem cannot become an unconditional one by algebra

The [separate reduced conditional model](../finite-closure-model-2026-09-23/THEOREM.md) permits a scalar nonterminal orbit with `K_+=K=−1`, while the neutral load remains positive and can decrease rapidly. This suffices to show that well-defined finite iteration in that model does not imply strict internal novelty at each step. The exact Schur theorem also yields `K_+=K_P` for `Y_P=λI` on its own declared stratum. Moreover, a higher relation is a separately operationalized candidate; the matched-memory direct model in the [current emergence test](../../papers/universal-reclosure-emergence-2026-09-29/README.md) reproduces every reported signature under the declared interventions. None of these facts can be removed by rearranging the three finite completion identities.

**Result:** The mathematical composition gives a closed *conditional finite operator*. It does not furnish the missing implication from historical Level 0 to the three role assignments, or from a typed finite successor to universal irreducible emergence. Any further claim needs an explicit independent premise or a carrier-specific observation and intervention.
