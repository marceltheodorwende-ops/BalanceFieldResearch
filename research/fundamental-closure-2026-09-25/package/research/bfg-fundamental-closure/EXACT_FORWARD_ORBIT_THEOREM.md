# Exact Forward-Orbit and Asymptotic Boundary Theorem

## 1. Purpose

The exact dual-load theorem distinguishes

\[
\text{exact zero load}\Rightarrow\bot
\]

from a merely tiny positive load.

The next question is stronger:

> Can a successfully generated BFG state develop an exactly zero reciprocal load at a
> later finite step?

For the current finite master candidate, the answer is **no**, provided the step has
successfully reclosed into the generated invariant class described below.

---

## 2. Generated-state invariant class

Call a finite state generated-admissible when

\[
\Xi=
(\mathcal H,\mathfrak D,\mathfrak c,\aleph,\rho_F,\rho_W,Y,R_C)
\]

satisfies

\[
\boxed{Y>0}
\]

on the active carrier,

\[
\boxed{
\rho_F=P\rho_FP\ne0,
}
\]

and

\[
\boxed{
\rho_W=P\rho_WP,
\qquad
\operatorname{tr}\rho_W=1,
}
\]

where \(P\) is the ordinary projector onto the current persistent Riesz space.

Every successful step of the living finite reclosure candidate has these properties:

1. the reduced SVD retains only nonzero singular values, hence
   \[
   Y_+=\Sigma^2>0;
   \]
2. inherited formation is transported into the inherited persistent support;
3. a new formation seed lies in the promoted seed projector;
4. therefore total \(\rho_{F,+}\) is supported in
   \[
   P_+=S_++\Pi_E;
   \]
5. the inherited identity witness is supported in \(S_+\le P_+\).

Thus the generated class is invariant under every successful exact step.

---

## 3. Branch-injectivity theorem

Let \(W=\operatorname{Ran}P\) be the current persistent subspace and choose an
orthonormal basis matrix \(Z\) for \(W\).

Set

\[
G=I+Y,
\qquad
C=G^{-1},
\qquad
B=YG^{-1}=I-C,
\]

and let

\[
P_G
=
Z(Z^\dagger GZ)^{-1}Z^\dagger G
\]

be the \(G\)-orthogonal persistent projector.

Assume

\[
Y>0.
\]

### Retained branch

For \(v=Za\in W\),

\[
P_GCv
=
Z(Z^\dagger GZ)^{-1}Z^\dagger v.
\]

Since \(Z^\dagger Z=I\),

\[
P_GCv
=
Z(Z^\dagger GZ)^{-1}a.
\]

All factors are invertible on \(W\). Hence

\[
\boxed{
P_GC|_W
\text{ is injective}.
}
\]

### Complementary branch

Since \(B=I-C\),

\[
P_GBv
=
v-P_GCv.
\]

Write

\[
M=Z^\dagger GZ
=
I+Z^\dagger YZ.
\]

Then

\[
P_GBZa
=
Z M^{-1}(M-I)a
=
Z M^{-1}(Z^\dagger YZ)a.
\]

Because \(Y>0\),

\[
Z^\dagger YZ>0
\]

and is invertible on \(W\). Therefore

\[
\boxed{
P_GB|_W
\text{ is injective}.
}
\]

---

## 4. Strict reciprocal-load theorem

Let

\[
\rho_F\succeq0,
\qquad
\rho_F\ne0,
\qquad
\rho_F=P\rho_FP.
\]

The density loads are

\[
\Lambda_C
=
\operatorname{tr}
\left(
G P_GC\rho_F C P_G^\dagger
\right),
\]

\[
\Lambda_B
=
\operatorname{tr}
\left(
G P_GB\rho_F B P_G^\dagger
\right).
\]

Because \(P_GC\) and \(P_GB\) are injective on the support carrier \(W\),
neither transformed positive density can vanish.

Since \(G>0\),

\[
\boxed{
\Lambda_C>0,
\qquad
\Lambda_B>0.
}
\]

Therefore a generated-admissible state cannot hit the exact dual-load terminal gate on
its next step.

---

## 5. No finite exact dual-load collapse corollary

Suppose

\[
\Xi_1
\]

is produced by one successful exact master-law step and every subsequent transition
avoids the other exact terminal/no-choice gates.

Then for every finite \(n\ge1\),

\[
Y_n>0,
\]

\[
\rho_{F,n}=P_n\rho_{F,n}P_n\ne0,
\]

and

\[
\boxed{
\Lambda_{C,n}>0,
\qquad
\Lambda_{B,n}>0.
}
\]

Thus

\[
\boxed{
\text{exact dual-load terminality cannot appear spontaneously at any later finite step.}
}
\]

A numerical implementation may still lose resolution as one load becomes extremely
small. That is a computational precision issue, not an exact orbit endpoint.

---

## 6. Carrier-dimension and persistent-rank bounds

Let

\[
d_n=\dim\mathcal H_n,
\qquad
p_n=\operatorname{rank}P_n.
\]

The cross-fed analysis operator has domain \(\mathcal H_n\), so

\[
\boxed{
d_{n+1}
=
\operatorname{rank}\mathcal A_n
\le
d_n.
}
\]

Therefore

\[
\boxed{
d_n\le d_0
}
\]

for every finite step, and the integer carrier dimension can strictly drop only
finitely many times.

The previous branch-rank estimate remains valid,

\[
p_{n+1}\le p_n^{sel}+1\le p_n+1,
\]

but the stronger global finite-orbit bound is simply

\[
\boxed{
p_n\le d_n\le d_0.
}
\]

Thus repeated persistence growth is possible inside the existing carrier, but the
current finite master law does not create new carrier dimensions.

---

## 7. Maximal exact orbit theorem

Use exact spectral projectors and exact sign conditions, not floating tolerances.

For an admissible initial state \(\Xi_0\), recursively define

\[
\Xi_{n+1}
=
\mathcal U_{\rm BFG}^{NC}(\Xi_n)
\]

whenever the exact gates permit the step.

Because the finite candidate is single-valued, there is a unique maximal forward orbit
of one of two forms:

### Finite orbit

\[
\Xi_0,\ldots,\Xi_N,\bot
\]

ending at an exact structural/no-choice terminal gate.

### Infinite orbit

\[
\Xi_0,\Xi_1,\Xi_2,\ldots
\]

defined for every \(n\in\mathbb N\).

For a generated infinite orbit, the reciprocal-load denominator remains strictly
positive at every finite step. No hidden finite-time singularity is introduced by the
dual-load balance.

---

## 8. Asymptotic terminal boundary is not finite terminality

An infinite orbit may approach the closure of the admissible state space.

For example, the scalar intrinsic-Gram orbit obeys

\[
y_n>0
\quad\text{for every finite }n
\]

but

\[
y_n\to0.
\]

The point \(y=0\) is an exact dual-order terminal boundary, but

\[
\boxed{
\lim_{n\to\infty}y_n=0
}
\]

does not imply that any finite iterate equals \(\bot\).

It is useful to distinguish:

- **operational terminality:** an exact finite gate maps the state to \(\bot\);
- **asymptotic boundary approach:** an infinite admissible orbit converges in one or
  more state coordinates toward a boundary at which a further dual-order step would
  be terminal.

No new physical "vacuum law" is inserted by making this mathematical distinction.

---

## 9. Scalar double-exponential approach

For

\[
0<y\le1,
\]

the scalar intrinsic-Gram map satisfies

\[
f(y)
=
\frac{2y^2}{(1+y)^2(1+y^2)}.
\]

Because

\[
1\le(1+y)^2(1+y^2)\le8,
\]

\[
\boxed{
\frac{y^2}{4}
\le
f(y)
\le
2y^2.
}
\]

Let

\[
x_n=-\log y_n.
\]

Then

\[
2x_n-\log2
\le
x_{n+1}
\le
2x_n+\log4.
\]

Thus once the orbit is in this scalar regime,

\[
\boxed{
x_n=\Theta(2^n)
}
\]

and \(y_n\) approaches zero at a double-exponential scale in iteration count.

This explains why ordinary floating arithmetic loses the positive branch after only a
small number of steps even though exact mathematics still has \(y_n>0\).

---

## 10. Current consequence

The dual-load boundary problem is now separated into three levels:

1. **Exact finite mathematics:** generated states have strictly positive reciprocal
   loads; no spontaneous finite dual-load collapse.
2. **Exact infinite dynamics:** an orbit may approach a terminal boundary
   asymptotically.
3. **Numerics:** finite precision may become unable to certify positivity long before
   the exact boundary is reached.

The next mathematical task is therefore no longer to invent a boundary rule. It is to
study the asymptotic classes and continuum/renormalized descriptions of infinite
BFG orbits.
