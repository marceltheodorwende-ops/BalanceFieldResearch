# Joint neutral-interface and recursive-origin constraints

Date: 3 November 2026. Existing verification-stage supplement. No new constitutive equation or origin rule is adopted.

## 1. Source distinction

The original conjugate-recursion grammar is `R_C=M R M*`, `M=sqrt(N_R)`. The September 22 canonical source paragraphs 107–108 name N_R separately and leave its carrier realization and raw R unspecified. The positive neutral **response** `C_N(Y)=(I+Y)^(-1)` is already derived once its interface Y is supplied. These symbols must not be silently equated merely because both describe neutral mediation.

The September 26 source paragraph 191 supplies the declared **successor** rebuild `R_C,+=P_++(I-P_+)C_N(Y_+)(I-P_+)`. It uniquely reconstructs a successor given its selected P_+ and Y_+; it does not supply the first raw R or prove an origin identification N_R=C_N(Y_0).

The earlier [interface classification](../foundation_audit/INTERFACE_IDENTIFICATION.md) remains intact: for a fixed formed Hessian H, the quadratic completion yields `Y=H^(1/2)L M_neutral^(-1)L*H^(1/2)` once the source-neutral channel and intrinsic metric are supplied. M_neutral here is not the square-root recursion mediator M above. The [existing-premise search](../foundation_audit/EXISTING_PREMISE_SEARCH.md) did not establish the missing historical implication fixing those blocks. No previously established conditional Gram derivation is revoked.

## 2. Exact joint theorem in a positive self-adjoint sector

Let N>0 and R>=0 be finite Hermitian operators. These are mathematical hypotheses for this theorem, not assertions that every historical BFG raw recursion is positive or self-adjoint. Put

```math
A=N^{1/2}R N^{1/2},\qquad D=N^{-1}-R.
```

Then

```math
0\le A\le I\quad\Longleftrightarrow\quad0\le R\le N^{-1},
```

and

```math
I-A=N^{1/2}D N^{1/2},\qquad
\ker(I-A)=N^{-1/2}\ker D.
```

**Proof.** Both order equivalences follow by congruence with the invertible N^(1/2) and its inverse. The kernel identity follows from `N^(1/2)D N^(1/2)x=0` exactly when `D N^(1/2)x=0`. QED.

Under this order condition, A is a positive contraction. Its only possible peripheral eigenvalue is +1. In finite dimension its complementary spectrum is strictly below one. For a given unit formed vector e, it has exactly that persistent line if and only if

```math
D\succeq0,\qquad
\ker D=\operatorname{span}(N^{1/2}e),
```

with R>=0 as assumed. This is the exact joint matching criterion. When N and R are supplied, A and its full persistent space are fixed. The theorem does not derive those inputs from formation.

Noncommutation is allowed in this theorem. In particular, Ae=e need not make e an eigenvector of N or R individually. Replacing the kernel condition by an unsupported scalar balance would lose that distinction.

## 3. Why a free raw R can compensate any neutral choice

Fix any N>0, any orthogonal P containing the formed line, and choose a diagnostic positive contraction `A=P+(I-P)/2`. Define

```math
R=N^{-1/2}A N^{-1/2}.
```

It is positive, satisfies the conjugate grammar exactly, and has the same protected P for **every** positive N. The constant 1/2 is a comparison fixture, not a proposed BFG decay constant. This proves that the product relation plus existence of bounded protected recursion cannot fix N while raw R is free. If a separately specified raw R is present, this compensation is not permitted and the joint kernel theorem must be applied to that R.

Consequently even a derived map N=N(Y) would not alone close Y's origin initialization while R remains unrestricted. Conversely, supplying N and R fixes recursion but does not determine Y unless the relation between Y and N has been established.

## 4. Conditional resolvent identification: what it would imply

For this section only, impose the **additional comparison hypothesis**

```math
N=C_N(Y)=(I+Y)^{-1}.
```

It is not adopted as a source-derived origin law. The joint positive-sector conditions become

```math
0\le R\le I+Y,\qquad
\ker(I-A)=(I+Y)^{1/2}\ker(I+Y-R).
```

If e is an eigenvector of both Y and R with respective eigenvalues y and r, then

```math
Ae=e\quad\Longleftrightarrow\quad r=1+y.
```

If the same origin direction must also survive the existing strict positive-load and neutral-contrast selection conditions, `0<y<1`, this gives the conditional admissible interval `1<r<2`. At r=1 the required y is zero and the complementary load vanishes; at r=2 the required y is one and the exact selector excludes that direction. This statement uses the common-eigenvector and comparison identification hypotheses explicitly; it is not a universal spectral bound on arbitrary raw BFG recursion.

The relation can determine the load *along the formed line* from a given r. It still need not determine the whole interface. With the same

```math
K=\operatorname{diag}(-2,1),\quad F=2\Pi_0,\quad
R=\operatorname{diag}(5/4,1),
```

both `Y_a=diag(1/4,1/4)` and `Y_b=diag(1/4,1/2)` satisfy the comparison identification and give

```math
A_a=\operatorname{diag}(1,4/5),\qquad
A_b=\operatorname{diag}(1,2/3).
```

Both have precisely the same protected ground line and a strictly stable complement. They have different transverse neutral responses. Thus even fixed raw R, this added N(Y) identification and unique persistence do not automatically fix all of Y. If the current finite state discards transverse raw-recursion rates, that quotient is a separate issue; it does not establish equality of the two initial Y matrices.

For clarity, this particular pair does **not** demonstrate different finite-event successors when P=Pi_0 and W=Pi_0. Both Y commute with that line, agree on it and lie below the selection boundary. The transverse directions are discarded, leaving the same scalar successor `K_+=-2`, `F_+=2`, `W_+=1`, `Y_+=32/425`. Whole-interface uniqueness is therefore stronger than determining the future reduced trajectory in this example. The earlier noncommuting witnesses are needed when claiming actual finite-event dependence.

## 5. Joint compatibility with the quadratic interface

These diagonal positive Y witnesses can also be represented with a fixed positive source H and fixed intrinsic metric M_neutral=H by

```math
L=H^{-1/2}Y^{1/2}H^{1/2}.
```

Direct substitution gives the previously derived Gram expression exactly. For the fresh K above, its quartic Hessian is H=diag(4,3). Both completions therefore share that H and M_neutral while using distinct L. This is a compatibility witness inside the already classified quadratic class, not proof that the historical meanings allow every such L. A stronger existing mixed-Hessian or same-completion premise could constrain L and must be applied explicitly. The proposed L0-NC condition remains proposed, not adopted.

## 6. Checkpoint

| Available input or premise | Exact consequence | What remains unproved |
| --- | --- | --- |
| Specified quadratic source-neutral completion | Its Y, resolvent pair and Gram are determined | Unique original choice of interface blocks |
| Specified N and raw R in the positive sector | Full persistence from the joint kernel criterion | Derivation of N and R from origin data |
| Conjugate grammar with raw R still free | Any positive N can be compensated | Unique neutral origin cannot follow from existence alone |
| Extra N=C_N(Y) plus a given common formed eigenmode of R | y=r-1 on that mode | Historical justification of the extra identification and transverse Y |
| Declared successor rebuild with P and Y supplied | Unique successor recursion | Initial P/Y and origin-domain identification |

We have a precise joint compatibility test and a conditional mode-matching equation, not a unique fundamental initializer. The outstanding source obligations are now explicit: (i) the initial source-neutral channel/metric, (ii) the relationship of that interface to N_R, and (iii) the raw-recursion prescription or an equivalent origin support rule. The present targeted source inspection does not establish a theorem that no such premises exist anywhere in the corpus.

Continuing without additional physical laws requires an implication from existing origin premises supplying those objects or relationships. Merely identifying similarly named neutral operators, solving for R after choosing Y, or treating a declared successor completion as an original boundary law would not supply that implication.

Run `python joint_initialization/check_joint.py`. Exact controls are recorded in [results.json](results.json). [SOURCES.json](SOURCES.json) records source anchors and prior trace. No model implementation or published PDF is changed; no empirical or proof-assistant claim is made.
