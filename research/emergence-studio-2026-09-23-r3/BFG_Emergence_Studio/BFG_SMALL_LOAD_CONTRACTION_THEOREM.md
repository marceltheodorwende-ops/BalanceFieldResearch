# BFG Multidimensional Small-Load Contraction Theorem

## Status

This theorem is part of the finite reduced master runtime.

It explains the observed near-quadratic neutral-load contraction from the
operator structure of the adopted update. It is not fitted from the real-carrier
exponents.

---

## 1. Setup

Let the finite reduced state be

\[
S=(\rho,K,Y,R),
\]

with

\[
Y\succeq0,
\qquad
\rho=dd^\dagger\neq0,
\qquad
\mu=\operatorname{tr}\rho=\|d\|^2.
\]

Define

\[
G=I+Y,
\qquad
C=(I+Y)^{-1},
\qquad
B=Y(I+Y)^{-1}.
\]

Let \(P\) be the \(G\)-orthogonal persistent projector.

The reciprocal loads are

\[
\lambda_{\rm keep}
=
\|PCd\|_G^2,
\]

\[
\lambda_{\rm up}
=
\|PBd\|_G^2,
\]

and

\[
\alpha
=
\frac{\lambda_{\rm up}}
{\lambda_{\rm keep}+\lambda_{\rm up}},
\qquad
\beta=1-\alpha.
\]

The master packet is

\[
A=
\begin{bmatrix}
\sqrt{\alpha}\,PC\\
\sqrt{\beta}\,PB
\end{bmatrix}.
\]

On the active support the successor neutral load is

\[
Y_+=A^\dagger A
\]

up to the active-support unitary coordinate identification used by the runtime.

---

## 2. Neutral up-load lemma

Let

\[
y=\|Y\|_2.
\]

Because \(P\) is an orthogonal projector in the \(G\)-metric,

\[
\|Pv\|_G\le\|v\|_G.
\]

Therefore

\[
\lambda_{\rm up}
=
\|PBd\|_G^2
\le
\|Bd\|_G^2.
\]

Since \(Y\), \(B\), and \(G\) are commuting spectral functions of \(Y\),

\[
B^\dagger G B
=
Y^2(I+Y)^{-1}.
\]

For \(Y\succeq0\),

\[
0\preceq
Y^2(I+Y)^{-1}
\preceq
Y^2
\preceq
y^2 I.
\]

Hence

\[
\boxed{
\lambda_{\rm up}\le\mu y^2.
}
\]

This bound does not require Euclidean orthogonality of \(P\).

---

## 3. Reciprocal-weight lemma

Assume a nondegenerate keep channel

\[
\lambda_{\rm keep}\ge\eta>0.
\]

Then

\[
\alpha
=
\frac{\lambda_{\rm up}}
{\lambda_{\rm keep}+\lambda_{\rm up}}
\le
\frac{\lambda_{\rm up}}{\lambda_{\rm keep}}
\le
\frac{\mu}{\eta}y^2.
\]

Thus

\[
\boxed{
\alpha=O(y^2).
}
\]

This is the operator-level reason that the keep/up packet enters the small-load
regime quadratically.

---

## 4. Multidimensional quadratic contraction theorem

### Theorem

Let \(S=(\rho,K,Y,R)\) be a finite reduced master state satisfying the setup
above, and suppose

\[
\lambda_{\rm keep}\ge\eta>0.
\]

Let

\[
p=\|P\|_2.
\]

Then the successor neutral load obeys

\[
\boxed{
\|Y_+\|_2
\le
p^2\left(1+\frac{\mu}{\eta}\right)
\|Y\|_2^2.
}
\]

Equivalently, with

\[
C
=
p^2\left(1+\frac{\mu}{\eta}\right),
\]

one has

\[
\boxed{
\|Y_+\|_2\le C\|Y\|_2^2.
}
\]

### Proof

Because \(Y\succeq0\),

\[
\|C\|_2\le1
\]

and

\[
\|B\|_2
=
\max_{\lambda\in\sigma(Y)}
\frac{\lambda}{1+\lambda}
\le
\|Y\|_2
=
y.
\]

For the stacked packet,

\[
A^\dagger A
=
\alpha C^\dagger P^\dagger P C
+
\beta B^\dagger P^\dagger P B.
\]

Therefore

\[
\|A\|_2^2
\le
p^2
\left(
\alpha\|C\|_2^2
+
\beta\|B\|_2^2
\right).
\]

Using

\[
\alpha\le\frac{\mu}{\eta}y^2,
\qquad
\beta\le1,
\qquad
\|C\|_2\le1,
\qquad
\|B\|_2\le y,
\]

gives

\[
\|A\|_2^2
\le
p^2
\left(
\frac{\mu}{\eta}y^2+y^2
\right),
\]

hence

\[
\|A\|_2^2
\le
p^2
\left(
1+\frac{\mu}{\eta}
\right)y^2.
\]

The active-support successor \(Y_+\) has operator norm no larger than
\(\|A^\dagger A\|_2=\|A\|_2^2\). Therefore

\[
\|Y_+\|_2
\le
p^2
\left(
1+\frac{\mu}{\eta}
\right)
\|Y\|_2^2.
\]

\(\square\)

---

## 5. Uniform graph-metric corollary

If

\[
\|Y\|_2\le\delta,
\]

then

\[
I\preceq G\preceq(1+\delta)I.
\]

Because \(P\) is \(G\)-orthogonal,

\[
\|P\|_2^2
\le
\kappa_2(G)
\le
1+\delta.
\]

If along a recursive corridor

\[
\mu\le\bar\mu,
\qquad
\lambda_{\rm keep}\ge\eta>0,
\qquad
\|Y\|_2\le\delta,
\]

then one may choose the uniform constant

\[
\boxed{
\bar C
=
(1+\delta)
\left(
1+\frac{\bar\mu}{\eta}
\right)
}
\]

and obtain

\[
\|Y_{n+1}\|_2
\le
\bar C\|Y_n\|_2^2
\]

for every step remaining inside that corridor.

---

## 6. Double-exponential depth corollary

Assume the same constant \(C>0\) remains valid along the trajectory and let

\[
y_n=\|Y_n\|_2.
\]

If

\[
y_{n+1}\le C y_n^2
\]

and

\[
q_0=Cy_0<1,
\]

then with

\[
z_n=Cy_n
\]

one has

\[
z_{n+1}\le z_n^2.
\]

Therefore

\[
z_n\le z_0^{2^n}
\]

and

\[
\boxed{
y_n
\le
C^{-1}(Cy_0)^{2^n}.
}
\]

Thus the small-load sector contracts double-exponentially in recursive depth.

For a numerical admissibility floor \(\varepsilon>0\), a sufficient depth is

\[
\boxed{
n
\ge
\left\lceil
\log_2
\left(
\frac{\log(C\varepsilon)}
     {\log(Cy_0)}
\right)
\right\rceil
}
\]

when \(0<Cy_0<1\) and \(C\varepsilon<1\).

This estimates a threshold crossing of the numerical runtime. It is not an exact
physical extinction theorem.

---

## 7. Relation to the exact scalar sector

For

\[
K=-1,
\qquad
\rho=1,
\qquad
Y=y>0,
\]

the master update gives exactly

\[
y_+
=
\frac{2y^2}
{(1+y)^2(1+y^2)}.
\]

Hence

\[
y_+\sim2y^2
\qquad
(y\to0^+).
\]

The multidimensional theorem shows that quadratic order is not peculiar to the
scalar example: it follows generally from neutral mediation, the \(G\)-orthogonal
persistent projector, a nondegenerate keep channel, and the adopted Gram
successor law.

---

## 8. Executable certificate

`bfg_studio.small_load` implements:

- `small_load_contraction_constant`,
- `explicit_small_load_bound`,
- `certify_small_load_step`,
- `termination_depth_bound`,
- `run_small_load_contraction_audit`.

The certificate verifies separately:

\[
\lambda_{\rm up}\le\mu\|Y\|_2^2,
\]

\[
\alpha\le\frac{\mu}{\lambda_{\rm keep}}\|Y\|_2^2,
\]

and

\[
\|Y_+\|_2
\le
C\|Y\|_2^2.
\]

The theorem does not depend on the numerical audit.

---

## 9. Current real-carrier audit

Using only the allowed development/calibration states of the three READY
carriers:

- successful master transitions certified: `3816`;
- explicit quadratic bound satisfied: `3816/3816`;
- intermediate \(\lambda_{\rm up}\), \(\alpha\), and successor bounds:
  `3816/3816`;
- no active held-out target metric opened.

By recursive depth:

- depth 1: `1375/1375` bounds satisfied;
- depth 2: `1375/1375` bounds satisfied;
- depth 3: `1066/1066` bounds satisfied.

The stronger strict local condition

\[
C\|Y\|_2<1
\]

is already satisfied by all successful depth-2 and depth-3 transitions in the
current audit. It is not required for the one-step quadratic theorem; it is the
extra condition needed for the simple uniform double-exponential iteration
bound.

This is consistent with the independent formation-dynamics result that the
observed depth-2 and depth-3 log-log exponents are close to two.

---

## 10. Claim boundary

What is now theorem-level:

\[
\boxed{
\text{nondegenerate keep channel}
\Longrightarrow
\|Y_+\|_2\le C\|Y\|_2^2
}
\]

for the adopted finite master update.

What remains conditional in the depth estimate is persistence of one uniform
constant \(C\) along the recursive corridor.

The real-carrier audit establishes that the current implemented
development/calibration transitions satisfy the explicit one-step certificate;
it does not by itself establish a universal empirical law of nature.
