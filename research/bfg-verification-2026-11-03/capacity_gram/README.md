# A coordinate-invariant capacity-Gram target for initial Y

**4 November 2026.** This follow-up reduces the candidate initial-Y proof obligation to one neutral-coordinate invariant identity. It also checks an existing source factor, B_C=D_cov c, and distinguishes its possible operator and field meanings. This supplies a more focused source test without adopting the proposed L0-NC blocks or adding a physical law.

The [direct candidate audit](../initial_y_closure/README.md) already completed the conditional computation Y_NC=(H^(-1/2) Q H^(-1/2))^2, where H is the formed source Hessian and Q is the original neutral-capacity operator aleph_0. Its two literal block prescriptions are sufficient for that formula, but they are stronger than identifying Y itself. Here Q does **not** denote the finite neutral-selection projector.

## 1. A single exact invariant replaces two coordinate prescriptions

Write a positive joint quadratic assessment with fixed source H>0 as

    J(d,eta)=(d*H d+2 Re(d*B eta)+eta*N_joint eta)/2,
    M=N_joint-B*H^(-1)B>0.

B is its mixed block and M is its intrinsic completed-square neutral metric, not the full neutral diagonal block. The existing elimination and whitening formulas give

    Gamma := B M^(-1) B*,
    Y = H^(-1/2) Gamma H^(-1/2).

**Proposition G1.** For fixed H>0 and Q=Q*, the equality Y=Y_NC holds if and only if

    Gamma = Q H^(-1) Q.                         (G)

**Proof.** Multiplying Y=Y_NC by H^(1/2) on both sides gives precisely (G). Conversely, substitute (G) into the displayed Y formula. All factors remain in their stated order, so no commutation assumption is needed. QED.

This is a necessary-and-sufficient test **for this candidate response**, not a source axiom and not a derivation of (G) from the original capacities. Another source-derived Y could be different. The earlier E-based criterion remains equivalent: E=H^(1/2)(I+Y)^(-1)H^(1/2).

Under an invertible change of neutral coordinates eta=T zeta,

    B'=BT,   M'=T*MT,
    B'(M')^(-1)B'^*=B M^(-1)B*.

Thus (G) can be checked without choosing particular neutral coordinates. Under a common unitary source-frame change, H, Q and Gamma transform together and the identity is covariant. No arbitrary general-linear identification of the source capacity operators with bilinear forms is assumed.

### The literal proposed blocks are not necessary for the response

The L0-NC proposal uses B=-Q and M=H. They imply (G). But applying a nonorthogonal neutral-coordinate change to that same assessment generally changes both literal equalities, while Gamma and Y remain identical. The exact example in the executable uses

    H=diag(2,3), Q=[[1,1/4],[1/4,1]], T=[[2,1],[0,1]].

It gives B'=[[-2,-5/4],[-1/2,-5/4]] and M'=[[8,4],[4,5]], neither of the literal proposed blocks in those neutral coordinates, yet the same Gamma and Y. An uncoupled positive neutral direction may also be appended without changing the response. These are coordinate/padding controls, not new microscopic laws.

Consequently we need not prove more than the response requires. An accepted source implication establishing (G), even through other factors or coordinates, would determine this Y. The prior statement that two particular L0-NC clauses remain proposed is unchanged; the present work weakens the target to their observable quadratic consequence.

## 2. Rank information follows directly from that target

Because H>0 and Q is self-adjoint,

    x*Gamma x=||H^(-1/2)Qx||^2,
    ker(Gamma)=ker(Q),
    rank(Y_NC)=rank(Gamma)=rank(Q).

The kernel of the whitened Y is H^(1/2)ker(Q), not generally ker(Q) itself. In particular a full-rank Q gives a full-rank candidate Y, even if the coherence capacity has smaller rank. Exact fixtures check capacity ranks zero, one and two.

This provides a quick compatibility test before attempting a long source derivation.

## 3. Existing master-Gram source relation, with its roles retained

A wider screen covered **75 byte-deduplicated UTF-8 text extractions** from the existing plugin, original-source and coupling-search collections. These are extracted files, not 75 independently audited papers; some contain overlapping source material. A capacity/factor co-occurrence query found 35 overlapping candidate contexts in six September source files. The search includes the retained early source collection, including 2025 material. The machine screen is not a full semantic or theorem audit, and a failed text match is not evidence of mathematical impossibility.

Targeted reading of the Strong Universal September 8 source, recovered V3 and V4 sections 3.2-3.3 confirms the existing equations

    B_C=D_cov c,
    H_C=B_C* W_N B_C,
    Y_C=L_C* H_C L_C.

Their paragraph anchors and extraction hashes are in [SOURCES.json](SOURCES.json). These equations must not be weakened by treating B_C as an unconstrained independent operator where the source explicitly gives its relation to D_cov and c.

If a justified role/coordinate bridge identifies this Y_C with the normalized source Y, then the invariant target becomes

    H^(1/2) L_C* B_C* W_N B_C L_C H^(1/2)
       = Q H^(-1) Q.                            (G_master)

This is the same condition as (G), expressed in the existing master factors. The left side is Z*Z with Z=W_N^(1/2)B_C L_C H^(1/2), and the right side is Z_0*Z_0 with Z_0=H^(-1/2)Q. It asks for equality of the induced quadratic forms, not equality of every microscopic factor. The [minimal Gram-factor result](../effective_response/README.md) explains the corresponding freedom of neutral factor realizations.

The inspected clauses supply the Gram factorization but do not establish (G_master) with these original capacity/Hessian roles. The formed source H, master H_C, original coherence capacity c_0, and any closure field written c must first be typed correctly. Shared notation is not that bridge.

## 4. A concrete rank obstruction to one literal interpretation

Suppose B_C=D_cov c is interpreted as a **composition of finite linear maps**, and c is identified with the original pointwise coherence-capacity matrix c_0. Then, for any compatible finite D_cov,L_C and positive W_N,

    rank(Y_C)<=rank(B_C)<=rank(c_0).

This follows directly from rank inequalities for a product, independently of choices of L_C and W_N.

The existing L0-NC two-dimensional source fixture has

    c_0=diag(0,3),       rank(c_0)=1,
    Q=[[1,1/4],[1/4,1]], rank(Q)=2.

Its candidate Y_NC has rank two. Therefore that literal finite-composition identification cannot make Y_C equal to Y_NC on this fixture. An invertible whitening cannot repair a rank mismatch. The executable checks a representative finite composition and the target ranks; the written product inequality proves the obstruction generally.

This is **not** a contradiction in the source corpus. It is a restriction on an explicit attempted identification of roles, domains and operator products. The source may mean a differentiated field rather than composition with its pointwise value, or a different closure carrier/role c. Those alternatives need their actual definitions before the rank test can be applied.

### Differentiating a field has different rank behavior

For a real local parameter t, consider the positive semidefinite matrix field

    c(t)=[[t^2,t],[t,3]].

It has determinant 2t^2, nonnegative diagonal entries and hence is positive semidefinite for every real t. At t=0 its value is diag(0,3), of rank one, but its derivative is [[0,1],[1,0]], of rank two. The derivative's ordinary Gram is I. A constant field with that same value at zero instead has derivative zero and zero derivative Gram.

Thus a relation B_C=D_cov c understood as a field derivative need not obey the pointwise composition rank bound. It also needs more than the point value c(0): the field derivative/connection data are additional input unless the source derives them. The parameter t in this diagnostic is not claimed to be fundamental physical time, and neither field is installed as BFG dynamics.

This explains precisely why a differential realization cannot be replaced by arbitrary finite multiplication, while a finite pointwise capacity tuple cannot by itself be assumed to contain its missing derivatives.

## 5. Present result

We have reduced the candidate proof target to one neutral-coordinate invariant equality and found a specific existing factor relation that any source bridge must respect. The rank test eliminates one literal operator interpretation for the published example; the positive-field control shows how a derivative interpretation changes the question and which information it requires.

No claim is made that (G) follows from the original assumptions. The proposed blocks remain unadopted. The next source obligation is now concrete: determine what c and D_cov mean in the master construction, which carrier/metric relates that construction to the formed source, and whether their existing equations imply (G_master). A proof of that identity could close this candidate's Y without selecting an arbitrary neutral basis. A new stipulation of the identity would still be an extra law and is not used here.

The exact controls cover neutral-coordinate changes, uncoupled padding, source covariance, three capacity ranks, the finite-composition obstruction and the positive-field derivative distinction. They support the written proofs; no empirical or proof-assistant certification is claimed. The published PDF, existing proposal and baseline event remain unchanged.

```sh
python capacity_gram/check_capacity_gram.py
python validate_stage.py
```

Provenance and search scope: [SOURCES.json](SOURCES.json). Exact results: [results.json](results.json).
