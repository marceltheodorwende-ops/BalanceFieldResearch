# Exact consequences of the integrated BFG source formulas

## 1. Scalar feedback from the actual field equations

The plugin's Strongest Version, Sections 61.6–61.7 (PDF pp.94–95), gives

```math
\partial_t\Phi=F_\Phi+\frac{\beta\Phi(1-\Phi)}{I_0}I_B,
\qquad
\partial_t I=F_I+\delta I_B,
```

where

```math
F_\Phi=\Gamma\Phi(1-\Phi)+D_\Phi\nabla^2\Phi-\kappa\Phi|\nabla\Phi|^2,
\qquad
F_I=\nabla\cdot(D_I\Phi\nabla I)-\gamma I|\nabla\Phi|^2.
```

Substitution into its original I_B=I partial_t Phi+Phi partial_t I gives

```math
A=I F_\Phi+\Phi F_I,\qquad
B=\frac{\beta I\Phi(1-\Phi)}{I_0}+\delta\Phi,
\qquad (1-B)I_B=A.
```

If 1-B!=0, the unique scalar feedback is A/(1-B). At B=1 there is no finite solution when A!=0 and no unique feedback when A=0. This is a source-based conditional closure, not a new equation. It determines the local right-hand sides once the model, coefficients, fields and needed derivatives are specified. It does not prove unique initial fields, identify the cognitive operator F_op with scalar feedback, or establish a well-posed PDE on arbitrary domains.

The source's characterization of this as a minimal field form is a model/regime claim; the algebra here does not prove uniqueness among every admissible nonlinear PDE. No external physical equation is inserted.

## 2. Reconstructing the information operator from I[s]

The Neutral Interface, Section 7.1 (PDF p.8), supplies I[s]=<s,J s>. Work on a specified finite complex Hilbert space with J Hermitian. The Hermitian assumption and known inner product are explicit. Positivity of the functional only on a small admissible subset does not alone establish a unique positive operator on the whole carrier.

Let S be the available admissible profile family. The measurement map is

```math
\mathcal M_S(J)=\{\operatorname{tr}(Jss^*):s\in S\}.
```

**Identifiability theorem.** This map is injective on Hermitian operators exactly when

```math
\operatorname{span}_{\mathbb R}\{ss^*:s\in S\}=\operatorname{Herm}(n).
```

Proof: differences of two compatible operators lie in the Hilbert–Schmidt orthogonal complement of that span. The complement is zero exactly when the span is full. If it is not full, every nonzero Hermitian Delta in the complement is invisible to the observations. For a positive definite reference J, sufficiently small real perturbations J+t Delta remain positive definite, so positivity alone does not remove that ambiguity in the interior. A singular boundary operator can require a separate positivity analysis.

An explicit complete normalized probe family consists of e_i and, for each i<j,

```math
v_{ij}^{+}=(e_i+e_j)/\sqrt2,\qquad
v_{ij}^{\mathrm i}=(e_i+\mathrm i e_j)/\sqrt2.
```

Writing q(s)=I[s], the reconstruction is

```math
J_{ii}=q(e_i),
\quad\operatorname{Re}J_{ij}=q(v_{ij}^{+})-\frac{q(e_i)+q(e_j)}2,
\quad\operatorname{Im}J_{ij}=\frac{q(e_i)+q(e_j)}2-q(v_{ij}^{\mathrm i}).
```

There are n^2 real functional values. The sign of the imaginary term follows the convention q(s)=s*Js. For J=[[2,1+i],[1-i,3]], the four exact values are 2, 3, 7/2 and 3/2, which reconstruct J. For only s=e_1, q=2 cannot distinguish J from J+t diag(0,1) while positivity is maintained.

These are mathematical evaluations/probes, not quantum-measurement postulates or a requirement to purchase experimental equipment. All probes must actually belong to the source's admissible domain, or their use requires a justified extension. The theorem does not invent their functional values from the formation density. It identifies exactly what information would close J_0.

## 3. A full foundational admissibility family

Use the integrated source's simultaneous foundational conditions, not just an isolated spectral test. On a finite two-dimensional carrier take constant state s=e_1 and

```math
J=E=B_{\rm op}=N=N^*=I,\quad
F_{\rm op}(q)=\operatorname{diag}(1,q),\quad
R=J F_{\rm op}J,\qquad 0<q\le1.
```

Both inverse-neutral and conjugate representatives equal R because N=I. Then, on this path:

- Phi=<s,EJs>/<s,B_op N s>=1 and I[s]=1;
- dot Phi=dot I=dot N=0, hence I_B=0;
- the affine choice A_fb=0, B_fb=1/2 satisfies the source feedback equation and |1-B_fb|=1/2;
- rho(R_C)=1, sup_n ||R_C^n||=1 and R_C^n s=s;
- the source Lyapunov functional is exactly zero for every positive weight, and its derivative is zero;
- the interface is positive, invertible and regular.

Thus all the named balance/subcriticality/spectral/regularity/Lyapunov/boundedness tests of the foundational existence-domain conjunction hold. Yet q=1/2 and q=3/4 have different transverse decay rates, and q=1 has an additional persistent direction. These are exact comparison assignments, not proposed fundamental laws.

The subcritical margin is exactly 1/2, so the family uses source corridor bounds with epsilon_B<=1/2; the other errors and spectral logarithm vanish. All members use the same bounds. It is not claimed to satisfy an arbitrarily chosen incompatible corridor.

The affine values can also be obtained from the source's homogeneous constant field equations above: Phi=I=1 makes F_Phi=F_I=0, and choosing the supplied positive coefficient delta=1/2 gives B=1/2. All field time derivatives then vanish. The scalar interface equation is also stationary with N=N*, zero gradients and zero forcing. Thus this comparison need not evade the source's derived A/B relation. The displayed coefficient is a diagnostic value in a given source model, not a derived universal constant.

This is not asserted to solve every neural, biological or Standard-Model completion equation simultaneously with the same full input data. Those modules have extra domain-specific hypotheses and evolution prescriptions. The point is that the unified **foundational admissibility conjunction** alone does not imply a unique origin operator. Source definitions of a stable domain must not be confused with a uniqueness theorem for all its members.

## 4. What persistence costs can identify

For fixed monitored profiles s_k, the source-type residual cost is

```math
L(R)=\sum_k\|(R-I)s_k\|^2.
```

If their linear span V has rank r<n, every Hermitian perturbation Delta supported on V-perp has Delta s_k=0 and is invisible to this cost. The invisible Hermitian space has real dimension (n-r)^2. A single rank-one formed line therefore leaves transverse freedom; the family above is the n=2 case. When the profiles span the entire carrier, zero residual instead forces R=I on that carrier.

The Strongest Version's Section 61.3 persistence functional also includes order/information deviations and a feedback barrier. Holding those quantities fixed along the displayed operator family leaves the closure residual unchanged. This is a flat restricted direction of that cost, not a proof that every point is a stationary point with respect to all source field variations. No unproved full action minimization is claimed.

Together, the operator-identifiability and cost arguments sharpen the origin question: which admissible profiles and functional values are supplied by the original architecture? If only the formed line is specified, the transverse operator cannot be inferred merely by repeating its zero residual.
