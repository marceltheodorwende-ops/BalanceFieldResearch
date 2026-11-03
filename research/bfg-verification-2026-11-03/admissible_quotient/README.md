# Admissible variations, normalization and quotient curvature

This milestone uses the BFG-Engine's source bundle to test whether the flat directions found in the [functional Hessian audit](../functional_hessian/README.md) disappear after normalization, fixed information or removal of coordinate redundancy. A general residual-rank criterion is proved. An exact finite comparison family shows that the enumerated stability conditions, even supplemented by normalization and a fixed information value, do not automatically satisfy that criterion.

This is a source-scoped result. It neither identifies the full nine-role field state with a finite operator tuple nor proves independence from the conjunction of all historical BFG axioms. No new initializer, physical rule, paper or modification to the finite event is introduced.

## 1. What the plugin contributes

The BFG-Engine skill treats seven foundational modules as an integrated architecture. Their existing [global inventory and synthesis](../plugin_synthesis/README.md) remains the context for this focused check. The source on why recursive stability can exist is particularly useful here: sections 12-15 explicitly combine balance, subcritical feedback, spectral criticality, interface regularity, Lyapunov bounds and bounded recursive iterates. Section 8 gives R=I_op F I_op. Sections 9-10 supply the normalized and conjugate recursion operators.

The Neutral Interface source, section 21, and Recursive Stability source, section 23, describe local internal transformations and their compensating connection. They do not, in the inspected clauses, identify every zero-cost variation with a gauge orbit or supply the particular initial source-neutral response. A local transformation law for effective field sectors does not itself specify the entire Level-0 quotient. The Standard Model module's effective gauge roles are retained as sector-specific context, not imported as an extra origin law.

The exact displayed finite stability packet tested below is:

- Phi>0 and nonnegative information;
- exact balance Phi=1, stronger than a finite balance band;
- scalar affine feedback with A=0, B=1/2 and I_B=0;
- positive invertible neutral interface, fixed interface N_star and zero drift;
- conjugate recursive radius one and bounded iterates;
- zero Lyapunov cost, hence the corresponding nonnegative cost bound and nonincrease along each constant comparison trajectory;
- the primitive factor identity R=I_op F I_op.

The subcritical margin holds for any permitted epsilon_B<=1/2. Zero cost satisfies any nonnegative L_crit. Remaining sector dynamics, operational role definitions, the complete nine-role coordinate and any independent definition of S_adm are **not** asserted to follow from this packet. Where a source treats membership in S_adm as a separate premise, it remains a separate premise. Normalization and fixed information are added as stronger diagnostic restrictions, not announced as original universal axioms.

## 2. Exact criterion for a positive residual Hessian on a quotient

Suppose a smooth nonnegative cost is L=||r||^2/2 near a point with r=0. Let T be the tangent space of a specified smooth admissible constraint manifold, and let V be the tangent space of a specified equivalence orbit, with V contained in T. Assume Dr annihilates V; this holds for residuals constant along those orbits. The previous audit gives

    Hess L(v,w) = <Dr(v),Dr(w)>.

Because Dr(V)=0, this quadratic form descends to T/V. Its induced form is positive definite exactly when

    ker(Dr restricted to T) = V.

**Proof.** The form is zero on v exactly when Dr(v)=0. Independence of the representative follows because adding a vector of V does not change Dr(v). A quotient class has zero quadratic value exactly when it has a representative in the displayed kernel. Only the zero class has zero value precisely when that kernel equals V. QED.

Equivalently rank(Dr|T)=dim(T)-dim(V). Normalization removes only the directions it actually excludes. A gauge quotient removes only its vertical directions. A remaining zero-cost direction that changes a joint invariant cannot be erased as a coordinate redundancy.

This criterion requires an actual smooth constraint manifold and specified equivalence. On singular strata or inequality boundaries one may instead need tangent cones or a stratified analysis; arbitrary linear projection is not automatically a justified physical quotient. Constraint curvature creates no extra term here because the ambient gradient of the zero-residual cost vanishes.

The executable includes a positive control: T=R^3, V=span(e_3) and Dr=diag(1,2,0) give the positive quotient Hessian diag(1,4). With Dr=diag(1,0,0), the same quotient retains a null direction and gives diag(1,0). Thus quotient removal can work; it must be checked rather than assumed.

## 3. A flat family after normalization and fixed information

Fix the same positive operators on C^3 throughout:

    J = I_op = diag(1,2,3),
    E_exp = J^(-1), B_bind=I, N=N_star=I,
    F=J^(-2), R=J F J=I,
    R_N=I, R_C=I.

Here the scalar feedback I_B and the primitive feedback **operator** F are distinct source roles. The latter is not set equal to the former. Let the supplied state and interface drifts be zero. For 0<theta<1/2 define

    s_theta = (sqrt(theta), sqrt(1-2 theta), sqrt(theta))^T.

Theta labels different constant configurations; it is not a derived physical time. Direct calculation gives

    ||s_theta||^2 = 1,
    I[s_theta] = s_theta* J s_theta = 2,
    Phi[s_theta,N] = <s_theta,E_exp J s_theta>/<s_theta,B_bind N s_theta> = 1.

Since R_N s=s and N=N_star with zero drift, every term of the displayed source Lyapunov cost is zero. Also R_C^k s=s for every k, so its power bound is one and its spectral radius is one. Each constant comparison trajectory has I_B=d(Phi I)/dt=0 and satisfies the chosen scalar affine closure. Thus the family satisfies every equality and inequality in the **listed finite packet**, plus unit norm and the same information value.

### These are different joint coordinate classes

The joint invariant

    m_2(s,J) = s* J^2 s = 4+2 theta

changes along this family. Under a simultaneous unitary coordinate change (s,J)->(Us,UJU*), m_2 is unchanged. Therefore states with different theta are inequivalent as joint data, even if all common unitary coordinate changes are allowed. With J held fixed, its simple spectrum makes its unitary stabilizer diagonal phases, which also preserve the component probabilities and cannot change theta.

For theta=1/8 and theta=1/4, m_2 is respectively 17/4 and 9/2. Normalization, fixed mean information, removal of a global phase, and even quotienting all diagonal phase stabilizers do not identify these states. We do not claim that m_2 is an empirical observable or that it is an extra primitive BFG state coordinate; it is an exact invariant distinguishing the joint finite structures under examination.

The real positive representatives already provide a local phase-fixed slice. Their norm and fixed-information constraint gradients have rank two. The derivative ds_theta/dtheta is a nonzero tangent in their common kernel. Along it dm_2/dtheta=2, while every residual in the displayed cost remains zero. Hence the residual-rank criterion fails after removing the coordinate freedoms just described.

In the complex regular sector, unit norm and fixed information leave four real tangent dimensions; the diagonal phase stabilizer has three independent tangent directions because all three state components are nonzero. The remaining one-dimensional probability variation is precisely the non-gauge flat direction exhibited above. No assertion about additional unspecified foundational equivalences is made.

### Direct Hessian check of the displayed cost

Vary the interface within n I and retain the Frobenius norm for its matrix deviation. The same source definitions give Phi=1/n and R_N=I/n. The cost becomes

    L_C(s,n)=(1/n-1)^2/2
       +lambda_R (1/n-1)^2 ||s||^2
       +3 lambda_N (n-1)^2.

At either checked state with n=1 its Hessian in three real state coordinates and n is

    diag(0,0,0,1+2 lambda_R+6 lambda_N).

The state block and its mixed block vanish. The flat constrained direction therefore survives the neutral elimination as well. Considering more neutral directions cannot make a zero-cost path with N fixed cease to be a zero-cost path. A separately imposed state/interface coupling or narrower admissible domain could remove that path, but must be sourced.

## 4. Exact formation is a different restriction

The original real quartic with a simple negative ground eigenvalue selects only the two polarity-related minima. If admissible configurations are restricted to exactly that minimum set, there is no continuous real profile tangent near either minimum; quotienting the polarity gives one point. This does not provide a transverse response operator from functional values on that set.

For example K=diag(-2,1,3) has minimum profiles +/-sqrt(2)e_1 and ambient formed Hessian diag(4,3,5), checked exactly. That ambient Hessian uses virtual deviations away from the minimum. The existence of those virtual variations as a response domain, and their source-neutral assessment, are separate from the discrete exact-minimum state set. Restricting to exact minima is therefore not, by itself, a derivation of the missing E on an entire response carrier.

The family in section 3 is not asserted to be a fresh ground-state family for this K. Combining unrelated primitive operators with that formation example as if their role bridge had already been proved would be invalid.

## 5. Result and remaining task

The BFG plugin strengthens the analysis by making the simultaneous stability constraints explicit. In the enumerated packet they select a viability region but do not automatically supply a strictly positive quotient curvature. The stronger normalized, fixed-information example shows that the previous flatness issue cannot be dismissed solely as an amplitude or phase convention. This is not a theorem that every fully specified BFG sector has such a flat direction.

For a candidate source to determine the initial effective response, its **accepted variation space and equivalence relation** must now be supplied and tested with ker(Dr|T)=V, together with the positive source/reduced-response identification from the earlier audits. A newly imposed fixed value of m_2 or an arbitrary penalty would add information and is not adopted here. An already existing role constraint could potentially supply it; its precise source implication remains open.

The complete finite event still evolves its supplied state deterministically. This investigation concerns the source justification of that state, not a failure of the specified event law.

Source and plugin provenance: [SOURCES.json](SOURCES.json). Exact controls: [results.json](results.json). Reproduce from the stage folder:

```sh
python admissible_quotient/check_quotient.py
python validate_stage.py
```
