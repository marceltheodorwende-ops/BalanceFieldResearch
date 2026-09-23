# BalanceFieldResearch → BFG Emergence Studio Integration

## Integration rule

The GitHub repository `marceltheodorwende-ops/BalanceFieldResearch` is now used
as an additional mathematical source line for the master architecture.

The merge is claim-sensitive:

- exact theorems and identities enter the theorem/audit layer;
- conditional results enter the conditional-closure layer;
- explicit additional models enter the experimental upstream-model layer;
- negative and boundary results constrain what the universal core is allowed to
  claim.

Nothing is silently promoted from "proposal" or "model assumption" to
"universal BFG law".

## Integrated mathematical results

### Exact nonnormal recursive persistence certificate

A supplied real-rational invariant split

\[
S^{-1}RS=\operatorname{diag}(A,T)
\]

is now exactly certifiable when rational positive metrics \(M,N\) satisfy

\[
A^TMA=M,
\qquad
N-T^TNT\succ0.
\]

This proves power-boundedness for the supplied finite-dimensional operator
without assuming normality in the original Euclidean norm.

The implementation uses exact rational arithmetic and does not fit eigenvalues
or apply a floating unit-circle tolerance.

It returns the spectral/oblique projector

\[
P_{\rm spec}=S\operatorname{diag}(I_p,0)S^{-1}.
\]

This projector is not identified with the BFG graph-metric projector.

### Supplied-factor Gram rebuild

For explicitly supplied \(B_C,W_N,L_C\), the master can construct

\[
H_C=B_C^\dagger W_NB_C,
\qquad
Y=L_C^\dagger H_CL_C,
\]

followed by

\[
G=I+Y,\qquad
C_N=(I+Y)^{-1},\qquad
B_N=I-C_N,\qquad
Z=2C_N-I.
\]

The routine does **not** invent or infer \(B_C,W_N,L_C\).

### Retained-channel Gram identity

For an orthonormal active support basis \(U\), \(P=UU^\dagger\), and doubled
channel operator \(B_2\),

\[
B_{\rm tan}=U^\dagger B_2U,
\qquad
E=(I-P)B_2U.
\]

Then exactly

\[
U^\dagger B_2^\dagger B_2U
=
B_{\rm tan}^\dagger B_{\rm tan}+E^\dagger E.
\]

This closes the **Gram-energy bookkeeping** problem for retained external
channels.

It does not recover the external-channel direction, future coupling,
derivatives, or recursive transport from \(\Delta=E^\dagger E\) alone.

### G1 conditional compatibility

The inherited-load proposal

\[
Y_{\rm next}
=
U^\dagger(Y\oplus Y)U
\]

is integrated only as a conditional/proposal layer.

When the reconstructed factors satisfy the required intertwining conditions,
the equality follows from the Gram rebuild. Without those conditions, it is not
a universal BFG consequence.

### M3 finite connection model

The master now exposes the M3 upstream operator packet under the additional
assumptions

\[
D_{\rm cov}c=[A,c],
\qquad W_N=L_C=I,
\]

with skew-Hermitian \(A\) and Cayley transport

\[
R=(I-A)^{-1}(I+A).
\]

Under these assumptions \(R\) is unitary and hence power bounded.

M3 remains an optional finite connection model. The active master closure is the adopted 23-September reduced finite profile described below.

## Integrated closure boundaries

The architecture records two important mathematical boundaries.

First, finitely many local derivative data do not determine unrestricted local
field evolution without an additional evolution law. Increasing finite jet order
moves the ambiguity but does not remove it in the unrestricted analytic class.

Second, in the unbounded infinite-dimensional case an isometry into a Hilbert
space does not by itself guarantee that the restricted Gram form is admissible.
The support must meet the relevant form domain; stronger sufficient conditions
include bounded mapping into the graph norm, or suitable density/closability of
the composed operator.

These are architecture guards, not software failures.


## Master-runtime disposition

The 23-September finite-closure theorem changes the operational disposition of
the master architecture.

The Studio adopts the explicit reduced-state successor laws as its binding
finite closure profile. Therefore the following are now **closed inside the
master runtime**:

- active Gram rebuilding;
- successor factor assignment;
- successor recursive transport;
- total finite iteration with absorbing \(\bot\);
- finite nonnormal power-bounded inputs that satisfy the repaired persistence
  conditions;
- the restricted bounded infinite-dimensional finite-peripheral-rank entry
  class, via reduction to the finite profile.

The executable profile does not wait for an older-axiom uniqueness theorem
before running: the selected successor laws are now architectural laws.

This does not change source provenance. The 23-September theorem itself labels
the intrinsic-Gram and unitary-recursion laws as explicit choices. The master
therefore distinguishes **runtime closure** from a historical claim that those
choices were uniquely forced by earlier formulations.

For engineering and subsequent BFG development, runtime closure is the active
status.
