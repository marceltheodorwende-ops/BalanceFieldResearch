# Direct derivation attempt from the BFG Level-0 formation functional

**Scope and source.** This note checks the precise junction in Marcel Theodor Wende's original [Strong Universal Reclosure Whitepaper, 8 September 2026](../../papers/BFG_Strong_Universal_Reclosure_Whitepaper_2026-09-08.pdf), §3.1 equations (2)–(7) and §3.2 equations (8)–(16). The [7 September whitepaper](../../papers/BFG_Universal_Reclosure_Unification_Whitepaper_2026-09-07_revised_final.pdf) has the same local formulas and section boundary. These are BFG sources, not imported physical theories. The source itself calls §3.2 a canonical *quadratic neutral completion*. The task is to see whether it is a mathematical consequence of §3.1 alone.

## 1. What Level 0 actually computes

For the real one-dimensional admissible example `K_0=-1`, Level 0 gives

```math
F_0(\delta)=-\tfrac12\delta^2+\tfrac14\delta^4,
\qquad\delta_*=1.
```

The formed-state perturbation energy is **exactly**

```math
f(z):=F_0(1+z)-F_0(1)=z^2+z^3+\tfrac14z^4.
```

The Hessian is `f''(0)=2`, so its second-order tangent is `z²`. Thus a local pullback through a linear channel `L` yields `L*H_*L`, with `H_*=2` here. This is a genuine internal BFG calculation and explains the availability of a positive local Gram geometry. It does **not** make the exact quartic function quadratic at nonzero displacement.

## 2. Test the strongest natural two-channel assembly

Even if we add the favorable interpretation that two neutral pieces are evaluated by **the same** formed-state energy, a symmetric scalar channel `A=1` would give the candidate

```math
J_{F_0}(D,\nu)=f(D-\nu)+f(\nu).
```

For every `D>=0`, the symmetry point `nu=D/2` is in fact the **unique global minimizer** of this symmetric example. Write `z=D/2`, `nu=z+t`. Direct expansion gives

```math
f(z+t)+f(z-t)-2f(z)
=t^2(2+6z+3z^2)+\tfrac12t^4>0\quad(t\ne0,z\ge0).
```

Its exact minimum is therefore

```math
J_{F_0}(D,D/2)
=2f(D/2)=\tfrac12D^2+\tfrac14D^3+\tfrac1{32}D^4.
```

By contrast, the canonical §3.2 quadratic completion at `A=1` gives

```math
J_A(D,\nu)=\tfrac12(D-\nu)^2+\tfrac12\nu^2,
\qquad\min_\nu J_A(D,\nu)=\tfrac14D^2.
```

**Normalization matters.** The Hessian of `f` is `2`, whereas `J_A` assigns unit Hessian to each of its two pieces. If we normalize the formed-state energy by `1/2` to match that quadratic coefficient, the symmetric candidate becomes

```math
\widetilde J_{F_0}(D,\nu)=\tfrac12f(D-\nu)+\tfrac12f(\nu),
\quad \widetilde J_{F_0}(D,D/2)
=\tfrac14D^2+\tfrac18D^3+\tfrac1{64}D^4.
```

It now agrees with the canonical BFG neutral minimum to second order and still differs by nonzero cubic and quartic terms. The coefficient-normalized comparison avoids mistaking a factor-of-two convention for the actual obstruction. At `D=1/10`, the excess is exactly `1/8000+1/640000=81/640000`, as checked in [verify_exact.py](verify_exact.py).

This is a **counterexample to the inference** “the quartic Level-0 formation functional alone gives the exact quadratic neutral minimum for finite displacements.” The comparison uses the exact global minimum for positive `D`, not merely a truncated Taylor series. It is not a counterexample to the later BFG definition in §3.2: that section explicitly chooses the quadratic completion as an additional canonical sector. Nor does choosing the symmetric two-piece `J_{F_0}` follow uniquely from §3.1; it is merely a particularly favorable test of the proposed inference.

## 3. The successful BFG-internal derivation and its boundary

Once §3.2's `J_A` is accepted, minimizing it gives `(I+AA*)nu=AD` and `min J_A=1/2<D,(I+A*A)^−1D>`. Identifying the resulting retained response with the same BFG `C_N(Y)` uniquely gives `Y=A*A`, transported to `AA*` on the active target. The neutral channel identity `C²−B²=C−B` then gives the selection sign **if** closure gain is defined by the difference of equal-metric squared channel responses. The target recursion `P+QCQ` is the chosen order “neutral response, then transverse projection”; it is not the same as minimizing only after restriction to the complement when `P` and `Y` fail to commute. [UNIFIED_FINITE_THEOREM.md](UNIFIED_FINITE_THEOREM.md) proves type preservation of the resulting declared finite map.

The source-to-conclusion chain therefore has two legitimate stopping points:

| Premises used | Derived conclusion | Further identification needed |
| --- | --- | --- |
| §3.1 real Level-0 formation and its Hessian | Positive local formed-state tangent geometry | Identify mediation's measured closure with that same tangent geometry. |
| §3.2 exact quadratic neutral completion and fixed channel metrics | Exact neutral resolvent and source Gram | To call it a theorem **of §3.1 alone**, derive §3.2's exact quadratic-sector choice independently. |
| Declared gain meaning and transverse response/projection order | Exact selected finite successor preserving the stated type or terminal gate | The gain meaning and order are BFG constitutive rules, not algebraic consequences of positivity or power boundedness. |
| The resulting finite state and a synthetic removal test | A conditional finite dynamics and an operational constructed effect | Distinguish an independently measured physical mediator from a matched-memory direct representation; test a natural carrier. |

**Conclusion.** The later BFG **does** contain enough declared mathematics for the conditional finite closure theorem. Its earliest Level-0 quartic equation **does not by itself imply** the later exact quadratic neutral completion; the explicit higher-order terms prove the gap at nonzero displacement. Repeatedly substituting the later rule into the earlier one cannot turn that declaration into a historical derivation. This is a precise source-scoped result, not a universal assertion about unpublished BFG axioms.
