# Exact Level-0 to neutral-sector bridge

**Amendment, 29 September 2026.** Source: Marcel Theodor Wende's [Strong Universal Reclosure Whitepaper](../../papers/BFG_Strong_Universal_Reclosure_Whitepaper_2026-09-08.pdf), §3.1 equations (2)–(7) and §3.2 equations (8)–(16); the [7 September source](../../papers/BFG_Universal_Reclosure_Unification_Whitepaper_2026-09-07_revised_final.pdf) has the same pair. This note supplies a mathematically consistent **coordinate and scope bridge**. It does not assert that the historical text had already specified this bridge, or that its quartic formation energy is globally quadratic.

## 1. Formed branch and its exact Hessian

Work in the real finite-dimensional Level-0 carrier. The source gives

```math
F_0(\delta)=\tfrac12\langle\delta,K_0\delta\rangle
             +\tfrac14\|\delta\|^4,
\quad K_0=K_0^*,
\quad\lambda_0=\min\sigma(K_0)<0
```

with a simple lowest eigenvalue, normalized eigenvector `e_0` and positive spectral gap. At either formed minimum `delta_* = ±sqrt(−lambda_0)e_0`, differentiation gives

```math
H_*:=D^2F_0(\delta_*)
=K_0-\lambda_0 I-2\lambda_0 e_0e_0^*.
```

It has eigenvalue `−2lambda_0>0` on `e_0` and eigenvalues `lambda_j−lambda_0>0` on perpendicular eigenspaces. Hence `H_*>0`. The **exact quadratic tangent model** at this formed branch is the second-order jet

```math
Q_*(x):=\tfrac12\langle x,H_*x\rangle.
```

“Exact” here means exact as a quadratic form defined by the Hessian. Taylor's theorem gives `F_0(delta_*+x)-F_0(delta_*)=Q_*(x)+O(||x||³)`, which is *not* an exact equality to the original quartic energy for finite `x`.

## 2. The neutral mediation calculation in normalized tangent coordinates

Let `D` be a perturbation on this formed carrier with metric `H_*`, and let the neutral channel have a **declared** positive metric `M` and a linearized mediation map `L` from neutral variables to formed perturbations. On the tangent sector define the two-piece neutral completion with the *same* quadratic source geometry on the mediated difference:

```math
J_*^{(2)}(D,\eta)
=\tfrac12\|D-L\eta\|_{H_*}^2
 +\tfrac12\|\eta\|_M^2.
```

The first metric `H_*` is derived from §3.1. The neutral channel and its metric `M` must be identified: for a neutral piece of the same formed branch, take `M=H_*`; for a distinct formed neutral carrier, `M` can be its independently derived Hessian. The assertion that the mediation cost is this **quadratic tangent** two-piece completion is the sector/role identification connecting §3.1 to §3.2, and must be printed explicitly.

Set `d=H_*^{1/2}D`, `nu=M^{1/2}eta`, and define the ordinary-adjoint map `A* = H_*^{1/2} L M^{-1/2}`. The invertible whitening is then an exact change of variables *inside this tangent model*:

```math
J_*^{(2)}(D,\eta)
=\tfrac12\|d-A^*\nu\|^2+\tfrac12\|\nu\|^2
=J_A(d,\nu).
```

Thus §3.2's printed quadratic functional is the normalized representation of the Hessian tangent model. Its exact elimination gives

```math
Y=A^*A
=H_*^{1/2} L M^{-1}L^*H_*^{1/2},
\quad C_N(Y)=(I+Y)^{-1},
\quad\min_\eta J_*^{(2)}(D,\eta)
=\tfrac12\langle D,H_*^{1/2}C_N(Y)H_*^{1/2}D\rangle.
```

The Gram formula is on the whitened **source**. If the successor is represented on the active target, use the polar partial isometry to transport `A*A` to `AA*`; source and target operators are not literally equal. With a separately prescribed target metric, that metric must be retained in the adjoints and whitening.

## 3. Two exact checks

**Same formed branch.** In one dimension choose `K_0=−1`, `delta_*=1`, so `H_*=2`. Set `L=1`, `M=H_*=2`. Then `d=sqrt(2)D`, `nu=sqrt(2)eta`, `A*=1`, `Y=1` and

```math
\min_\eta J_*^{(2)}(D,\eta)=D^2/2
=d^2/4.
```

This agrees with the **quadratic** term of the exact same-branch energy `f(D−eta)+f(eta)`, whose global minimum for `D>=0` is `D²/2+D³/4+D⁴/32`. The latter retains the cubic and quartic corrections. Comparing `D²/2` in physical coordinates with `D²/4` in *unnormalized* coordinates would be a normalization error: §3.2's `d` here is `sqrt(2)D`.

**Distinct neutral metric.** Let `H_*=2`, `M=3`, `L=1/2`. Then `Y=H_* L²/M=1/6`, `C_N=6/7`, and the exact tangent minimum is `6D²/7`. Direct minimization of `(D−eta/2)²+(3/2)eta²` gives `eta_*=2D/7` and the same value. The [exact verifier](verify_exact.py) checks both cases with rational arithmetic (including the unwhitened minimum).

## 4. What is now consistent, and what remains conditional

Sections 3.1 and 3.2 fit into one mathematical chain **if §3.2 is explicitly the neutral theory on the formed branch's Hessian tangent sector, written in whitened coordinates**. In that sector the §3.2 minimizer, resolvent split and Gram load are exact for every tangent-sector input. The approximation occurs only in replacing the full quartic Level-0 energy by its second-order jet. The BFG source's use of the word “exact” for elimination is therefore correct *within its declared quadratic sector*; it must not be read as a global identity for the quartic §3.1 energy.

This bridge fixes a compatibility and units problem without changing the historical sources. It does not uniquely derive the choice of a two-piece neutral cost, the metric on a distinct neutral channel, its physical mediator role, the later target projection order, or strong emergence from §3.1 alone. Those are constitutive identifications of the completed BFG, already kept explicit in the [unified finite theorem](UNIFIED_FINITE_THEOREM.md) and [source derivation audit](SOURCE_DERIVATION_ATTEMPT.md).
