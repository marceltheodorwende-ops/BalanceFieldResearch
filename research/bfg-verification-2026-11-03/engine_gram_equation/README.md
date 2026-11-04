# BFG-Engine synthesis: the coordinate-independent Gram equation

**4 November 2026.** The requested equation is now written as an equality of quadratic forms on explicitly typed spaces, with its coordinate and gauge transformations checked. A finite solvability theorem gives an exact criterion and construction for its weight. The BFG-Engine reference bundle supplies the covariance grammar; the previously traced September source supplies the master-Gram factorization. This completes the mathematical formulation and compatibility test, **not** a derivation of its right-hand side from the earliest BFG assumptions.

No physical metric, connection or source law is selected by reverse fitting. The existing L0-NC proposal remains proposed, and no new paper or event rule is introduced.

## 1. What was inspected in the BFG-Engine

All 20 indexed original references were located in the installed bundle and freshly SHA-256 checked against the earlier inventory. The actual reference directory contains those same 20 files. Seven foundational modules remain coequal in the prior [global synthesis](../plugin_synthesis/README.md): foundational BFG, conjugate closure, strongest formulation, compact recursive stability, neutral interface, Standard Model reconstruction and the recursive-existence stability source. The Level-0, trinitarian/domain and runtime materials remain separate parts of that larger field. This is a focused synthesis, not a new proof audit of every page.

Relevant source contributions are:

| Material | Contribution to this calculation | Input still needed |
|---|---|---|
| Neutral Interface and Recursive Stability modules | Positive neutral metric roles, covariance, admissible domains and stability conditions | The actual initial fields, metrics and operators |
| Strongest formulation and Standard Model module, connection-enforcement section | D_mu=partial_mu+A_mu, transformation law for A_mu and local representative covariance | A transformation law does not numerically determine a connection |
| Level-0 and trinitarian modules | Difference, mediation, configuration and admissibility roles | The representation and differential data connecting these roles to a specific finite master map |
| September master closure source, previously traced outside this 20-file bundle | B_C=D_cov c, H_C=B_C*W_N B_C, Y_C=L_C*H_C L_C | The typed meaning of c,D_cov,L_C,W_N and their bridge to the formed-source response |
| Bundled candidate runtime | A configured diagnostic realization of neutral adaptation and conjugate recursion | It is not an independent implementation of the proposed capacity-Gram initializer |

The plugin available here is a skill plus local reference files; no separate remote BFG proof/simulation API was exposed. No answer is attributed to a second model or hidden engine run.

### Read-only runtime trace

The original `bfg_runtime_strengthened_v4_candidate.py` has 1,489 lines. Its AST parses. Source inspection of BFGState initialization and BFGRuntime levels 9-10 shows configured initial N, seeded raw recursion, a gain/clipping neutral update and a spectral-target rescaling. It computes sqrt(N) R_raw sqrt(N)^T in that diagnostic model. Those routines do not establish the capacity-Gram target below from a formed capacity triple.

The AST has no identifier named Y, but that lexical fact alone would not prove that an equivalent computation is absent. The substantive conclusion rests on the inspected initialization and update dataflow. This is a limited static trace for the present mathematical question, not a general pass/fail judgment on runtime quality or consciousness claims. No simulation output is used as evidence for the target equation, and the original program is unchanged. Exact original source line ranges and hashes are recorded in [SOURCES.json](SOURCES.json).

## 2. Typed equation independent of coordinates

At a specified admissible configuration, let V be the finite source Hilbert space and K the closure-response Hilbert space. Supply:

- H:V->V, positive definite, the formed source Hessian;
- Q:V->V, self-adjoint, the original neutral capacity aleph_0;
- L_C:V->E, a source-to-closure map on a specified intermediate fiber E;
- B_C:E->K, the typed covariant closure-difference map;
- W_N:K->K, positive semidefinite in the supplied positive response inner product.

No Lorentzian spacetime contraction is used as a positive Gram metric. A spacetime metric and this positive admissibility weight are different roles unless a source establishes a compatible relationship. All adjoints below use the stated Hilbert metrics.

Define the map

    T = B_C L_C H^(1/2) : V -> K.

The exact target is

    T^dagger W_N T = Q H^(-1) Q.                 (E)

Equivalently, without any matrix coordinates, **for every x in V**,

    ||B_C L_C H^(1/2)x||_(W_N)^2
       = ||H^(-1/2)Qx||_V^2.                  (E_form)

Equality for all x gives the operator equality by polarization. This is stronger than a scalar trace, one selected profile or an equality of spectra. If the existing master source response is validly identified with the normalized source Y, then (E) is necessary and sufficient for

    Y=(H^(-1/2)QH^(-1/2))^2.

Indeed Y=H^(-1/2)T^dagger W_N T H^(-1/2); substituting the target proves the formula. Conversely multiplying that formula by H^(1/2) on both sides yields (E). This is the [capacity-Gram criterion](../capacity_gram/README.md) with the actual source factors displayed.

The equation therefore states exactly what a proposed source bridge must establish. It is not itself newly imposed as a BFG origin law.

## 3. Covariance and nonorthonormal coordinates

Under a unitary source-frame change U and unitary response-frame change V_K,

    H'=U H U*, Q'=U Q U*,
    T'=V_K T U*, W_N'=V_K W_N V_K*,

both sides of (E) transform as U(T^dagger W_N T)U*. Thus the equality is frame independent.

Nonorthonormal coordinates work too, but their inner-product matrices must travel with them. If old source vectors equal S times new coordinates, and old response vectors equal R times new coordinates, then

    h_V'=S* S, h_K'=R* R,
    T'=R^(-1) T S, W'=R^(-1) W R,
    H'=S^(-1)H S, Q'=S^(-1)Q S,
    T'^dagger=(h_V')^(-1) T'^* h_K'.

These give T'^dagger W'T'=Q'(H')^(-1)Q'. In such coordinates H',Q',W' are self-adjoint in their transformed metrics; they need not be ordinary Hermitian matrices under the untransformed conjugate transpose. An exact nonorthonormal fixture verifies the weighted identity and rejects the incorrect unchanged-adjoint version. No coordinates have been chosen as physically preferred.

## 4. What D_cov c means for an endomorphism field

The engine's gauge sources give the transformation law for vectors and a connection. If c is typed as an **endomorphism field**, rather than a vector, then c transforms as c'=U c U^(-1). For a compatible connection A_mu, the induced derivative is

    nabla_mu c = partial_mu c + [A_mu,c],
    A_mu'=U A_mu U^(-1)-(partial_mu U)U^(-1),
    nabla_mu' c'=U(nabla_mu c)U^(-1).

**Derivation.** Apply the product rule to partial_mu(UcU^(-1)), use partial_mu U^(-1)=-U^(-1)(partial_mu U)U^(-1), and substitute the displayed A_mu'. The derivative-of-U terms cancel. This is an induced mathematical consequence of the supplied covariance grammar, conditional on that field typing. It does not establish that every source occurrence of c has this type.

For several derivative directions, B_C can map a vector into the direct sum of the derivative-response fibers; W_N then pairs those fibers in a specified positive form. The base, connection, derivatives and fiber metrics must be supplied or derived. Merely writing D_cov does not provide them.

### Connection data are not eliminated by a gauge slogan

The exact fixture uses c(t)=[[t^2,t],[t,3]] and an anti-Hermitian real connection A=[[0,-a],[a,0]]. At t=0 its covariant derivative has off-diagonal entries 1-3a. It has rank two for a=0 and rank zero for a=1/3.

Changing a alone while holding the same full c(t) fixed changes its covariant derivative. A genuine gauge change transforms **both** the field and connection, and the code verifies that complete transformation symbolically using an exact rational unitary family. Gauge covariance guarantees consistency between representatives; it does not select which covariant field/connection data occur.

## 5. Exact finite solvability theorem

Let Gamma_0=Q H^(-1)Q>=0 and suppose T:V->K is already given. We can now answer whether **any** response weight can realize (E).

**Theorem E1.** In finite dimension, a W>=0 satisfying T^dagger W T=Gamma_0 exists if and only if

    ker(T) is contained in ker(Gamma_0)=ker(Q).

A strictly positive W>0 exists if and only if these kernels are equal.

**Proof.** If Tx=0, then x*Gamma_0 x=<Tx,WTx>=0, and positivity implies Gamma_0 x=0. If W>0, equality of this quadratic value to zero also forces Tx=0, giving equal kernels.

Conversely let T^+ be the Moore-Penrose inverse for the supplied Hilbert metrics and put

    W_0=(T^+)^dagger Gamma_0 T^+.

This is positive semidefinite. T^+T is the orthogonal projector onto ker(T)^perp. The kernel-inclusion assumption places the support of Gamma_0 in that space, so T^dagger W_0 T=Gamma_0. If the kernels are equal, W_0 is strictly positive on ran(T). Adding any positive definite form on ran(T)^perp, with zero cross block, yields W>0 on all K and preserves the pullback. QED.

For an invertible square T the weight is unique:

    W=(T^(-1))^dagger Q H^(-1) Q T^(-1).

For general T, the displayed extension is an existence construction, not a classification of every possible positive W with allowed cross blocks. The equation constrains only its pullback along T.

Equivalently, if Z=W^(1/2)T and Z_0=H^(-1/2)Q, equation (E) says Z and Z_0 have the same Gram. The map Z_0x -> Zx is then well-defined and isometric on its range, extending to the appropriate partial isometry. This explains why equality of every microscopic factor is unnecessary.

### A computable solution is not automatically a source derivation

The theorem solves a precise algebraic completion problem. If the original source already fixes W_N, one must insert that W_N and **test** (E). Replacing it by W_0 because the desired equality holds would use the target to choose a physical input. That would not prove the target from BFG assumptions, and is not done here.

This distinction also identifies a concrete failure condition: if a proposed B_C,L_C annihilates a direction on which Q is nonzero, no nonnegative W can repair it. It generalizes the [earlier finite-composition rank obstruction](../capacity_gram/README.md).

## 6. Worked source example and controls

For the existing proposal's H=diag(2,3) and Q=[[1,1/4],[1/4,1]], choose the diagnostic covariant jet at t=0,a=0, with L_C=I. Then B_C=[[0,1],[1,0]] and T=B_C H^(1/2) is invertible. The unique weight completing this target is

    W_0=[[35/288,5/(24 sqrt(6))],
         [5/(24 sqrt(6)),25/96]].

It is positive and yields exactly the earlier candidate Y. This is an explicit inverse completion. The source has **not** been shown to prescribe this W_0. Using W=I with the same map instead gives Y=I, illustrating the substantive role of the weight rather than proving either assignment physically correct.

Six exact solvability cases cover square and rectangular maps, complex adjoints, matching and mismatching kernels, and a zero target with a nonzero map. All pass the theorem's respective existence or impossibility conditions. Additional symbolic checks cover the endomorphism derivative, local gauge transformation, unitary pullback and nonorthonormal metrics. These are algebraic controls supporting the written proofs, not empirical confirmation or a proof-assistant certificate.

## 7. What is complete and what remains open

The user-requested stopping criterion and direct current assessment are fixed in [COMPLETION_CHECK.md](COMPLETION_CHECK.md). The coordinate-equation subtask is complete. The original initial-Y derivation is not yet established; further work must target that implication rather than expand the objective.

The coordinate-independent equation, its typed differential interpretation, its covariance and its exact finite solvability conditions are complete. The BFG-Engine material materially supports that formulation. The earlier foundational implication remains distinct: the sources must determine the actual field, connection, maps and positive weight, or otherwise imply (E_form), without selecting them to reproduce the desired candidate.

Neither the configured runtime nor the fact that a positive solution W_0 exists proves that origin implication. The original proposal, published PDF and finite-event baseline remain unchanged. No missing metric or connection is adopted as a new law.

Source fingerprints, runtime trace and focused anchors: [SOURCES.json](SOURCES.json). Exact results: [results.json](results.json).

```sh
python engine_gram_equation/check_engine_equation.py
python validate_stage.py
```
