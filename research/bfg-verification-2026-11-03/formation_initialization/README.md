# Formation-derived initial data: exact result and remaining premises

Date: 3 November 2026. This continues the existing verification stage; it is not a new paper. No event rule or physical law is added.

## 1. Question and source boundary

Which initial data follow from the existing formation problem, rather than merely being admissible inputs to the finite event? The complete finite state already contains `(K, rho_F, rho_W, Y, P)`. Its deterministic evolution does not establish a unique initializer for these fields.

The September 22 canonical architecture, Section 3 (extracted paragraphs 68–78), supplies the finite real profile functional

```math
F(d)=\tfrac12 d^*Kd+\tfrac14\|d\|^4,\qquad K=K^*.
```

The September two-density state explicitly uses `rho_F=dd*` in the rank-one case, while separating formation from inherited identity. Connecting a *fresh formed profile* d to a minimizer of F is the interpretation under which the following initialization result applies. The current general state category permits other positive, including mixed, formation densities. This result does not restrict that whole category to fresh ground states. Source versions and limitations are recorded in [SOURCES.json](SOURCES.json).

## 2. Exact formation theorem

Let lambda be the smallest eigenvalue of K. For t=||d||^2 and lambda<0,

```math
F(d)+\lambda^2/4
=\tfrac12 d^*(K-\lambda I)d+\tfrac14(t+\lambda)^2\ge0.
```

Equality requires d in the ground eigenspace and ||d||^2=-lambda. If the ground eigenvalue is simple, all real minimizers are `+/-sqrt(-lambda)e`; their phase-free density is uniquely

```math
\boxed{\rho_{F,0}=(-\lambda)\Pi_0},\qquad
\operatorname{tr}\rho_{F,0}=-\lambda,\quad F_{\min}=-\lambda^2/4.
```

In the finite complex version the minimizers differ by a global phase, with exactly the same unique density. No eigenvector sign or phase is selected. The identity is unitary covariant. It fixes formation amplitude in the *given* quartic normalization; changing that coefficient changes the amplitude, and is not authorized here.

If lambda>=0, F(d)>=||d||^4/4, so the unique minimizer is zero. It gives no nonzero formation input. If lambda<0 has multiplicity m>1, the minimizing radius is fixed but the pure density is not unique. The invariant mixed operator `(-lambda/m)Pi_ground` can describe an additional ensemble choice; it is not the outer product of a single minimizer when m>1. The source's simple-ground gate avoids this ambiguity. Finite dimension is essential to this argument's automatic attainment; no arbitrary infinite-dimensional extension is asserted.

## 3. What follows for the identity witness

**Conditional rank-one lemma.** If a normalized positive witness W is supported entirely on the newly formed one-dimensional line, then

```math
W=\Pi_0 W\Pi_0,\quad W\succeq0,\quad\operatorname{tr}W=1
\quad\Longrightarrow\quad W=\Pi_0=\rho_{F,0}/\operatorname{tr}\rho_{F,0}.
```

Proof: an operator supported on a rank-one space equals a scalar multiple of its projector; its trace sets the scalar to one. This is a mathematical uniqueness theorem *given that support premise*. Positivity and normalization alone do not supply the premise: for K=diag(-2,1), both `W_a=diag(1,0)` and `W_b=I/2` satisfy the general witness type under P=I, while the formed density is `diag(2,0)` in both cases. W_b is excluded if one additionally demands support on the formed line. This witness compares only those stated weaker conditions, not every historical BFG premise.

The reviewed two-density source supplies an **inherited** witness transport rule. It does not turn a genuinely new seed into inherited identity: on its emergent sector E, `E W_inherited=0` but `E rho_seed=rho_seed!=0`. Consequently, setting W equal to normalized total rho_F after every step is incompatible with that rule. At a first formation with no predecessor, the inheritance formula alone cannot create a normalized witness; an ancestry convention or a source-supported initial-witness rule must be identified. We have not adopted one. Nor does this bounded source review prove that no such rule occurs anywhere in the corpus.

## 4. What follows for persistence

Static formation supplies a ground line, not a recursion operator. Even power boundedness and preservation of that line do not determine the entire persistent space. With the same `K=diag(-2,1)` and formed density, take

```math
R_a=\operatorname{diag}(1,1/2),\qquad R_b=I.
```

Both preserve the formed line and are power bounded. Their peripheral projectors are respectively `P_a=diag(1,0)` and `P_b=I`. For scalar positive Y, these are also the graph-metric projectors. These operators are logical comparison witnesses under the specified conditions, not proposed BFG dynamics. A minimal-support requirement could select P_a, but cannot be silently added.

The existing rank-aware successor rule already promotes inherited support plus the canonical seed line. **If that declared successor rule is extended to a first event with zero inherited support**, it gives P_0=Pi_0. This is a conditional extension of its domain, not a proof that static minimization alone supplies it. Similarly, the existing rebuild `R=P+(I-P)(I+Y)^(-1)(I-P)` determines R once P and Y are given; it does not determine an unspecified Y or establish that a first formation has an inherited witness. Setting old witness mass to zero would trigger the current inheritance gate, not bootstrap an origin event.

## 5. Initializer ledger

| Quantity | Established here | Remaining premise/input |
| --- | --- | --- |
| K | The given capacity difference enters F | Capacities/carrier are not derived from nothing |
| rho_F,0 | Unique (-lambda)Pi_0 for a fresh simple-negative formed profile | Existing quartic functional and density identification |
| rho_W,0 | Unique Pi_0 if normalized and supported on that same line | Justification of the origin-witness support/ancestry rule |
| P_0 | Pi_0 under a minimal-support or zero-inheritance promotion extension | Justification that this rule applies at origin |
| Y_0 | Not fixed by the formation calculation | Previously audited source-neutral interface premises |

Thus one nontrivial initial quantity is derived conditionally from the existing formation law, while two further quantities have exact conditional formulas with explicit outstanding premises. The complete initializer is not yet derived from the original assumptions. No fit, empirical validation, proof-assistant certificate, or universal physical theory follows from these calculations.

## 6. Checks and next logical step

Run `python formation_initialization/check_formation.py` from the parent stage. [results.json](results.json) records exact symbolic square completion, real/complex phase removal, degenerate and nonnegative boundary examples, witness and persistence counterexamples, and an explicit seed/witness separation. These finite fixtures check the formulas and logical distinctions; the dimension-independent finite theorem is the argument above.

The next useful source question is specific: **does an existing original premise identify the first normalized witness with the first formed line and apply the seed-promotion rule at origin?** This must be traced separately from Y's interface initialization. Accepting a convenient initializer would define a model instance; it would not prove its necessity.
