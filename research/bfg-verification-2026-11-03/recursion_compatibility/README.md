# Compatibility of normalized, conjugate and canonical recursion

Follow-up dated **4 November 2026**, within the existing research stage. This tests a concrete possible bridge from the original recursion roles to the initial response. It does not derive or adopt that bridge. The main result is a conditional compatibility restriction and a sharp quantitative bound: some tempting identifications would force a zero complementary load if exact zero Lyapunov cost were also imposed. Explicit exception controls prevent extending that result beyond its hypotheses.

## 1. The three source objects must first be distinguished

The May conjugate-recursion sources use the same positive N and raw operator R in

    R_N=N^(-1/2) R N^(-1/2),
    R_C=N^(1/2) R N^(1/2).

The displayed Lyapunov cost includes lambda_R ||R_N s-s||^2. Exact zero total cost, with positive weights, therefore requires R_N s=s. The usual source bounds permit nonzero cost, so exact zero is a stronger special regime.

The September 26 finite source, paragraphs 190-193, instead gives the **post-update rich-state representative**

    A_can=P+(I-P)C_N(Y)(I-P),     C_N(Y)=(I+Y)^(-1).

It is determined after the finite state is supplied and updated. This formula is not a proof that the initial old R_C equals A_can, or that the old neutral N equals C_N(Y). The source even distinguishes phase-rich continuum branches from the finite canonical representative in paragraph 306. A representative sufficient for the finite quotient need not equal every earlier role-bearing operator as a matrix.

All proofs below use one specified reference inner product, with the displayed adjoints and orthogonal P. If the two source carriers or metrics differ, their identification must be justified before these comparisons apply. The [earlier joint-origin analysis](../joint_initialization/README.md) and [raw-recursion audit](../raw_recursion/README.md) retain their conclusions.

## 2. Two simultaneous fixed-point conditions

Let N>0, s be a nonzero vector, and suppose **both** R_N s=s and R_C s=s. Set

    u=N^(-1/2)s,     v=N^(1/2)s.

Multiplying the fixed-point equations by the appropriate square roots gives

    R u=v,    R v=u,
    R(u-v)=-(u-v),    R(u+v)=u+v.

These identities are exact and require no commutation assumption.

**Consequence A.** If R has no eigenvector of eigenvalue -1, then u=v, hence Ns=s and Rs=s. In particular this holds for positive semidefinite Hermitian R. Conversely Ns=s and Rs=s imply both original fixed-point equations. A nontrivial difference between u and v therefore needs a raw -1 mode; it is not ruled out by bounded recursion alone.

**Consequence B.** If R is self-adjoint and either N<=I or N>=I, the same conclusion Ns=s follows even if R has a -1 mode. Indeed

    ||u||^2=<u,Rv>=<Ru,v>=||v||^2,
    <s,(N^(-1)-N)s>=0.

For a one-sided positive N, the operator N^(-1)-N has a fixed sign, and its kernel is exactly ker(N-I). The spectral decomposition therefore gives Ns=s. No assumption that s is an eigenvector of N was made beforehand.

Self-adjointness of raw R is not asserted universally. The inspected primitive clauses define R through supplied information and feedback operators; they do not, by that factor formula alone, prove every possible feedback operator positive or self-adjoint.

### Why a phase-flip exception matters

For N=diag(2,1/2), R=[[0,1],[1,0]] and s=(1,1)/sqrt(2), both fixed-point conditions hold while Ns differs from s. Here N straddles I, raw R has eigenvalues +/-1, and R_C is exactly unitary. This fixture shows why the no-minus-one or one-sided hypotheses cannot be omitted. Its N is not a retained resolvent C_N(Y) of a nonnegative Y.

## 3. Consequences of the additional retained-resolvent identification

For this comparison only, add N=C_N(Y), Y>=0. Then 0<N<=I, and Ns=s is equivalent to Ys=0. Hence either consequence above, together with the stated fixed-point assumptions, forces zero load on that direction.

If the current formation density is a positive multiple of ss*, and that same direction is the retained formation/persistence direction, B_N(Y)s=Y(I+Y)^(-1)s=0. The complementary formation load vanishes and the finite event fails its strictly positive dual-load gate. A mixed density with load elsewhere is different, and is not excluded by this rank-one statement.

This is a restriction on the **conjunction of comparison premises**, not a contradiction between the source documents. In particular N=C_N(Y), common carrier/metric, same-vector role matching, exact zero cost and a chosen recursion representative must not be silently added as if all were established origin axioms.

### Exact global norm preservation is stronger than bounded propagation

The source prose mentions norm preservation as well as bounded recursive propagation. They are different conditions. From the definitions one has R_N=N^(-1) R_C N^(-1). If R_N s=s, then R_C N^(-1)s=Ns. If R_C preserves the norm of **every** vector, this implies ||N^(-1)s||=||Ns||. One-sided N again forces Ns=s, even without raw self-adjointness or a separately assumed R_C s=s.

This argument applies only to that exact global interpretation. Norm preservation along a particular persistent trajectory, spectral radius one and power-boundedness do not imply it. Congruence by sqrt(N) does not automatically make an arbitrary supplied raw operator globally norm-preserving.

## 4. A bounded nonselfadjoint control with positive finite loads

The restriction must not be generalized to arbitrary power-bounded raw recursion. An exact counter-control uses

    N=diag(9/16,16/25),   s=(1,1)/sqrt(2),
    Y=N^(-1)-I=diag(7/9,9/16).

Let S=sqrt(N), u=S^(-1)s, v=Ss and choose the unique two-dimensional linear R sending u to v and v to u. The exact result is

    R=[[-256/31,875/93],[-1107/155,256/31]].

It is not self-adjoint and satisfies R^2=I. Both R_N s=s and R_C s=s hold. The conjugate spectrum is {1,-9/25}; its distinct eigenvalues make it power-bounded. More explicitly its spectral projectors give R_C^k=P_1+(-9/25)^k(I-P_1), which is uniformly bounded in k. Raw R is power-bounded as an involution. R_N has a transverse eigenvalue -25/9; its powers are bounded on s but not globally.

This example can satisfy the enumerated balance and zero-cost roles by setting information operator I_op=I, primitive feedback F=R, expansion E_exp=N, binding I, preferred interface N_star=N and both supplied drifts zero. Then Phi=1, I[s]=1, R=I_op F I_op and the displayed Lyapunov cost is zero. These choices are algebraic controls of that packet, not newly proposed BFG dynamics. They do not satisfy exact global norm preservation of R_C or the later canonical positive representative. No realization of all foundational or domain-specific dynamics is claimed.

For the supplied finite input K=I-3ss*, rho_F=2ss*, rho_W=P=ss*, every eigenvalue of Y is strictly between zero and one. The exact metric projection and loads give

    Lambda_C=576/481,    Lambda_B=37249/69264,

both positive. The exact stacked-response Gram has positive determinant and rank two. All output support lies in the two copied ground lines, so K_next=-2I. The inherited rank is one and the remaining one-dimensional complement gives seed trace 2. A fresh call to the unchanged baseline confirms rank, seed, next K and Gram trace. This finite event uses the supplied five objects; it does not identify the old nonselfadjoint R_C with its canonical reconstructed representative.

Thus bounded persistence and zero older cost alone do not rule out a positive-load comparison bridge. The omitted hypotheses materially matter.

## 5. A sharp bound when the canonical representative is identified

Now consider the **stronger** comparison packet

    N=C=(I+Y)^(-1),
    R_C=A_can=P+(I-P)C(I-P),
    ||s||=1, Ps=s,

all in the same reference coordinates. Solving the conjugate definition gives R=C^(-1/2) A_can C^(-1/2), which is positive and self-adjoint. Therefore

    R_N=(I+Y) A_can (I+Y).

Since A_can>=P, with y_bar=<s,Ys>>=0,

    <s,R_N s> >= ||P(I+Y)s||^2 >= (1+y_bar)^2,
    ||R_N s-s|| >= 2 y_bar+y_bar^2.

The first inequality is an order comparison, the second is Cauchy-Schwarz with Ps=s, and the last uses the unit-vector expectation bound. Consequently the source cost obeys the conditional lower bound

    L_C >= lambda_R (2 y_bar+y_bar^2)^2.

It is sharp: Y=yI on the source gives equality in the residual bound. Exact zero cost forces y_bar=0 and hence Ys=0. If a finite nonnegative threshold L_crit is supplied instead, then

    y_bar <= sqrt(1+sqrt(L_crit/lambda_R))-1.

This is a range restriction, not a unique numerical initializer. It does not fix transverse directions or derive the threshold and lambda_R from origin assumptions. The report uses the source's lambda_R>0 assumption and does not fit a new value.

The executable checks this bound exactly for the noncommuting N/P fixture, verifies equality for Y=I/4, and checks the Ys=0 boundary. For the nonselfadjoint example's same N and P, replacing its raw R by the one induced by A_can changes the old normalized-recursion residual from zero to a strictly positive exact value. It is a changed role assignment, not a harmless rewriting of the same operator data.

## 6. What the next source bridge must respect

We now have a stronger compatibility test, rather than another unspecified request for 'more coupling information'. Any proposed source derivation must say whether it identifies the older N with the retained response C_N(Y), whether it uses the same old and finite recursion representative, what inner product carries the adjoints, whether zero or bounded Lyapunov cost is intended, and which vector/density roles are matched.

The available source clauses do not establish that entire conjunction. In particular the September representative is a derived successor lift, not an initial boundary prescription. We therefore neither impose it as a new origin law nor infer a universal BFG inconsistency from the conditional zero-load result. Exact origin Y remains unresolved; the declared finite event remains unchanged.

Source provenance is in [SOURCES.json](SOURCES.json), exact controls in [results.json](results.json). General statements rest on the written proofs. The baseline comparison is numerical confirmation, not an empirical experiment or a proof-assistant certificate.

```sh
python recursion_compatibility/check_compatibility.py
python validate_stage.py
```
