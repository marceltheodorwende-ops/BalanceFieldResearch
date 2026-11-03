# Can an existing BFG functional determine the initial response?

This focused continuation checks the functionals behind the [effective response criterion](../effective_response/README.md). It establishes a precise conditional Hessian route, identifies its local scope, and tests the actual source candidates. The checked clauses do not yet supply a complete source-to-initial-E implication. No replacement event, physical principle or new paper is introduced.

## 1. Source findings and limits

| Inspected source | What it supplies | Why this does not yet determine initial E |
|---|---|---|
| September 22 canonical architecture, section 3 | Quartic formation assessment A_Adm(delta)=delta* K delta/2+||delta||^4/4 | Its Hessian at the isolated real formed minimum supplies the positive source block H. There is no neutral argument in this assessment to eliminate. |
| Neutral Interface, May 21, sections 6 and 12 | Interface variation of Phi, primitive dynamics G, and a sum of balance, recurrence, interface-deviation and drift costs | Requires the underlying operators, fixed interface, dynamics, weights and norm. A source Hessian can be singular even at a zero-cost balanced point; see the exact specialization below. |
| Structured Level 0, sections 10.4 and 21 | Interface-completion score and neutral-stability score | The component functionals, weights, comparison/domain data and admissible updates are not numerical mixed source-neutral Hessian data. A threshold or descent condition alone does not specify E. |
| September 7 Unification, section 5.4, paragraph 217 | The same positive master load is reevaluated on a next-level candidate packet | Explicitly says its H_C and L_C are not replaced by a level-specific Hessian. An arbitrary score Hessian cannot be substituted into this rule. |
| Same September 7 source, section 6.2, paragraphs 259-264 | V_C(q)=<D_C(q),C_N(Y_C(q))D_C(q)>/2 and exact first/second derivatives of the resolvent | Its local response Hessian is derived **from supplied Y_C(q)** and its derivatives. This is valid response analysis, but not an upstream initializer without an independent specification of the potential or its curvature. |

These are source-local findings, not a nonexistence theorem over every BFG manuscript. The [prior source trace](../effective_response/SOURCES.json), including the original April 2025 feedback identity, remains part of this chain. The [global BFG-Engine synthesis](../plugin_synthesis/README.md) retains the seven foundational modules and their distinct roles; this is a targeted functional analysis rather than a new complete audit of that corpus.

Notation matters: H below is a formed **source Hessian**, E is a **neutral-minimized source Hessian**, and the September H_C is a **role-bearing master Gram geometry**. Their shared positive-matrix type does not identify them. The canonical field's nine roles are not reduced to these three symbols.

## 2. Conditional nonlinear elimination theorem

Work in finite real coordinates d and eta, with a twice continuously differentiable assessment J near (d_0,eta_0). Assume

    J_eta(d_0,eta_0)=0,
    Hess J(d_0,eta_0) = [[H,B],[B^T,N]],
    N>0.

The implicit-function theorem applied to J_eta=0 supplies a unique nearby stationary neutral branch eta=h(d), with

    Dh(d_0)=-N^(-1) B^T.

Continuity and N>0 make this a strict **local** minimum in the neutral variable near the base point. It need not be the global minimum over disconnected branches or remote neutral states. For j(d)=J(d,h(d)), the envelope identity Dj=J_d and differentiation give

    Hess j(d_0) = E = H-B N^(-1) B^T.

If the joint Hessian is positive definite, completing its quadratic form gives E>0 and E<=H. Conversely N>0 and E>0 imply joint positive definiteness by the same congruence. With a fixed identified H, the effective-response result then gives the unique tangent load

    Y_tan = H^(1/2) E^(-1) H^(1/2)-I >= 0.

This is a derivation **conditional on the joint functional, point, carrier and admissible variations**. It is not a derivation of those inputs from formation alone. A complex nonlinear functional must be analyzed in real coordinates or with a justified compatible complex structure; a holomorphic Hessian is not silently substituted for this real second variation.

### Local curvature does not fix the full nonlinear law

Let J_1(d,eta)=J_0(d,eta)+x^4, where x is one source coordinate and the base is x=0. Both assessments have the same Hessian at the base. Their minimizing neutral branches are identical, but their minimized assessments differ by x^4. Consequently they give the same Y_tan and different finite-amplitude assessments. This is an exact distinction, not a truncation error estimate.

The executable uses a positive quadratic completion plus (eta-x)^4, with and without x^4. It verifies the equal Schur Hessians. Substitution of the **linearized** neutral branch checks the second variation; it is not described as an exact solution of the nonlinear branch equation.

Thus a local Hessian bridge alone cannot replace the exact finite neutral completion. To feed Y_tan into the preserved finite event as its physical initial Y would require the source to justify that identification. No such identification is adopted here.

### Coordinate dependence must also be controlled

Under x=psi(u), the scalar Hessian transforms as

    Hess_u(f composed with psi)
      = Dpsi^T Hess_x(f) Dpsi + sum_a (partial_a f) Hess_u(psi_a).

At a critical point the gradient term vanishes, giving the expected congruence. Away from a critical point curvature can change under a nonlinear reparameterization. For f(x)=x+x^2/2 and x=u+a u^2, the second derivative at zero becomes 1+2a despite Dpsi(0)=1. For the critical f(x)=x^2/2 it remains 1. Both identities are checked exactly. A coordinate-free initial response therefore needs an identified stationary point or an additional justified differential-geometric structure, not merely a named score.

## 3. The actual neutral-interface Lyapunov candidate

The May source's section 12 defines

    L_C(s,N) = (Phi(s,N)-1)^2/2
       + lambda_R ||R_N s-s||^2
       + lambda_N ||N-N_star||^2
       + lambda_C ||dot N||^2.

In a smooth finite realization at a point where all residuals vanish, write L_C=||r||^2/2 using appropriately weighted residuals. Direct differentiation yields

    Hess L_C = (Dr)^T Dr.

Indeed the remaining second-derivative terms are multiplied by residual values and vanish there. This Hessian is positive semidefinite and is positive definite exactly when Dr is injective on the chosen variation space. Removing phase, scale or other null directions requires a justified quotient or restriction; positivity cannot be assumed from the word 'Lyapunov'. General operator norms may also require a separate differentiability check.

An exact scalar diagnostic makes the missing implication concrete. Set the primitive expansion, binding, information and raw recursion operators to 1, take N=n>0, N_star=1 and the supplied drift G=0. The source definitions give Phi=1/n and R_N=1/n. Its cost becomes

    L_C(s,n) = (1/n-1)^2/2
          + lambda_R (s/n-s)^2 + lambda_N (n-1)^2.

At s=1,n=1 this cost and its gradient vanish, but its Hessian in coordinates (s,n) is

    [[0,0],[0,1+2 lambda_R+2 lambda_N]].

The entire line n=1 is a zero-cost source-amplitude direction. Its source block and neutral-reduced source curvature are zero, which cannot be inverted to obtain the positive E needed in the preceding effective-response interval. The drift term vanishes identically in this diagnostic choice.

This is an algebraic specialization of the **displayed cost and operator definitions**, not a claim to instantiate every BFG dynamical equation, physical domain or origin axiom. It shows exactly why that cost's bare form does not guarantee the needed positive source curvature. Extra domain restrictions or operator dependencies might remove the flat direction, but would have to be sourced and checked. No extra restriction is installed.

## 4. The September local-response potential is conditional on Y

For C(q)=(I+Y(q))^(-1), differentiating (I+Y)C=I gives

    C_,a = -C Y_,a C,
    C_,ab = C Y_,b C Y_,a C + C Y_,a C Y_,b C - C Y_,ab C.

These are the source's resolvent identities. If D(q_0)=0 and J_D is the derivative of D at q_0, twice differentiating V(q)=D(q)^T C(q) D(q)/2 gives

    Hess V(q_0) = J_D^T C(q_0) J_D.

Terms involving derivatives of C vanish because they also contain D(q_0). Therefore a specified Hessian and an invertible known J_D could reconstruct C(q_0); the formula for V with unknown Y is not such an independent specification. A restricted J_D probes only its image and can leave response directions unidentified.

The scalar exact fixture D(q)=q, Y(q)=y_0+a q+b q^2/2 with y_0>0 gives V''(0)=1/(1+y_0). Different a,b produce the same local curvature, so even known Y(q_0) does not determine its full field dependence. These functions are comparison fixtures, not new BFG laws.

A nonnegative potential also need not have a positive Hessian at an arbitrary stationary point: D=1 and Y(q)=1+q^2 give V(q)=1/(2(2+q^2))>0 but V''(0)=-1/4. This does not refute positivity at a separately established stable minimum. It shows why the point and admissible domain are essential.

## 5. What is resolved

The possible functional route is now mathematically explicit: a justified joint functional and stationary neutral branch give a Schur Hessian; a positive identified source/reduced pair gives a unique tangent response. The actual source candidates do not permit an automatic identification: the formation quartic supplies H without neutral variables, the displayed Lyapunov cost can be flat, and the September response potential already uses Y. Level-0 score names and thresholds do not provide the missing derivatives numerically.

This rules out three shortcuts: equating every positive matrix named H, treating every nonnegative stability score as strictly convex, and treating local response curvature as an exact global initialization law. It does not prove that an original BFG derivation is impossible.

The remaining source obligation is the **specific joint assessment or invariant response law on a justified variation space**, together with its relation to the exact initial neutral completion. Until that implication is established, Y remains a supplied initial datum of the complete finite event. Repeating minimization with an arbitrarily chosen assessment would add no source justification. The existing proposed L0-NC amendment remains explicitly proposed.

See [SOURCES.json](SOURCES.json) for pinned clause provenance and [results.json](results.json) for the exact controls. The proof statements are analytic; the executable supplies finite algebraic checks, not formal proof-assistant or empirical certification. Reproduce with:

```sh
python functional_hessian/check_hessian.py
python validate_stage.py
```
