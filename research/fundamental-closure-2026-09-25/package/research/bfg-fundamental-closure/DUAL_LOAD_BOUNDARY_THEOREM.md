# Exact Dual-Load Boundary Theorem

## 1. Source statement

The canonical BFG reciprocal-order source states that a branch with zero closure load
cannot support a genuine dual reclosure and is mapped to the terminal case by the
universal gate.

The exact retained/upward loads are

\[
\Lambda^{\rm keep}\ge0,
\qquad
\Lambda^{\uparrow}\ge0.
\]

For two positive loads, reciprocal balance gives

\[
\omega^{\rm keep}
=
\frac{\Lambda^{\uparrow}}
{\Lambda^{\rm keep}+\Lambda^{\uparrow}},
\qquad
\omega^{\uparrow}
=
\frac{\Lambda^{\rm keep}}
{\Lambda^{\rm keep}+\Lambda^{\uparrow}}.
\]

The cross-fed packet obeys

\[
\boxed{
\|\widetilde D^{DO}\|^2
=
\frac{
2\Lambda^{\rm keep}\Lambda^{\uparrow}
}{
\Lambda^{\rm keep}+\Lambda^{\uparrow}
}.
}
\]

---

## 2. Zero-load terminal theorem

Assume

\[
\Lambda^{\rm keep}+\Lambda^{\uparrow}>0.
\]

If either branch load is exactly zero, then

\[
\Lambda^{\rm keep}\Lambda^{\uparrow}=0
\]

and therefore

\[
\boxed{
\|\widetilde D^{DO}\|^2=0.
}
\]

Hence

\[
\boxed{
\widetilde D^{DO}=0.
}
\]

No nonzero dual-order successor packet exists.

Therefore the canonical BFG source gate

\[
\boxed{
\Lambda^{\rm keep}\Lambda^{\uparrow}=0
\quad\Longrightarrow\quad
\bot
}
\]

is not an arbitrary numerical convention. It is consistent with the exact reciprocal
packet algebra.

If both loads vanish, the reciprocal denominator also vanishes and there is likewise
no genuine dual-order state.

---

## 3. Exact \(Y=0\) corollary

At

\[
Y=0
\]

the exact neutral pair is

\[
C_N(0)=I,
\qquad
B_N(0)=0.
\]

Therefore

\[
D^{\uparrow}=0,
\qquad
\Lambda^{\uparrow}=0.
\]

For every nonzero admissible retained branch,

\[
\boxed{
Y=0
\quad\Longrightarrow\quad
\text{no genuine dual reclosure}
\quad\Longrightarrow\quad
\bot.
}
\]

Thus the zero-load point is an exact terminal boundary of the dual-order closure
architecture.

---

## 4. Kernel-supported terminality

Global \(Y=0\) is not the only way an exact branch load can vanish.

For the density formulation,

\[
\Lambda^{\uparrow}
=
\operatorname{tr}
\left(
G P B_N
\rho_F
B_N P^\dagger
\right).
\]

Since \(G>0\) and the inner operator is positive semidefinite,

\[
\Lambda^{\uparrow}=0
\]

iff the upward branch vanishes on the relevant formation/persistent support.

Thus an exact terminal can occur when the current formation density lies in a
load-kernel even if \(Y\neq0\) on other directions.

The terminal criterion is therefore branch-structural, not merely the scalar equation
\(Y=0\).

---

## 5. Near-zero is not zero

The exact terminal gate is

\[
\Lambda^{\rm keep}\Lambda^{\uparrow}=0.
\]

It is **not**

\[
\Lambda^{\rm keep}\Lambda^{\uparrow}<\varepsilon
\]

for an arbitrary floating tolerance.

A finite positive load, however small, remains mathematically positive.

Therefore a numerical implementation must distinguish:

\[
\boxed{\text{exact zero} \Rightarrow \bot}
\]

from

\[
\boxed{\text{positive but numerically unresolved} \Rightarrow
\text{numerical ambiguity}.}
\]

The package now reports

`dual_load_zero_terminal`

only when the branch operator is represented as exact zero in the current finite
arithmetic, and reports

`dual_load_numerical_ambiguity`

for a nonzero branch whose positive load falls below the declared floating-resolution
threshold.

The latter is a computational halt, not a BFG claim of physical terminality.

---

## 6. Scalar intrinsic-Gram orbit

Under the selected scalar intrinsic-Gram completion rule,

\[
y_{n+1}
=
\frac{2y_n^2}
{(1+y_n)^2(1+y_n^2)}.
\]

For every finite

\[
y_n>0,
\]

\[
0<y_{n+1}<y_n.
\]

Therefore

\[
y_n\downarrow0
\]

but

\[
\boxed{
y_n>0
\quad\text{for every finite exact step}.
}
\]

So this orbit approaches the exact dual-order terminal boundary asymptotically without
reaching it at any finite mathematical iterate.

This cleanly separates:

- **exact infinite iteration toward the boundary**, from
- **finite-precision inability to resolve arbitrarily small positive loads**.

---

## 7. Consequence for the finite master law

The \(Y\to0\) issue does not require a new BFG vacuum equation.

The source architecture already says what happens at the exact boundary:

\[
\boxed{
\text{zero branch load} \Rightarrow \bot.
}
\]

What remains open is not the boundary law itself, but whether the chosen completion
rules drive physically relevant states toward that boundary and whether the continuum
theory interprets the asymptotic approach as vacuum, loss of dual order, or another
derived physical regime.

Those interpretations are downstream and are not inserted into the finite master law.
