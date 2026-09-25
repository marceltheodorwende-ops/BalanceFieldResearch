# Closure-Depth Coordinate and Asymptotic Renormalization

## 1. Motivation

Every successful generated BFG state lies on a strictly positive active Gram carrier:

\[
Y>0.
\]

Therefore standard functional calculus permits the derived coordinate

\[
\boxed{
H:=-\log Y.
}
\]

This is not a new physical field or axiom. It is an invertible mathematical
reparameterization of the existing positive BFG load:

\[
\boxed{
Y=e^{-H}.
}
\]

It is useful because the difficult \(Y\to0\) boundary is moved to an infinite
coordinate distance

\[
Y\to0
\quad\Longleftrightarrow\quad
H\to+\infty
\]

on positive spectral modes.

---

## 2. Exact neutral geometry in closure-depth coordinates

Since

\[
Y=e^{-H},
\]

the exact BFG neutral pair becomes

\[
C_N
=
(I+e^{-H})^{-1},
\]

\[
B_N
=
e^{-H}(I+e^{-H})^{-1}.
\]

Using functional calculus,

\[
\boxed{
C_N
=
\frac12
\left(
I+\tanh\frac H2
\right),
}
\]

\[
\boxed{
B_N
=
\frac12
\left(
I-\tanh\frac H2
\right).
}
\]

Therefore the canonical exact neutral contrast is simply

\[
\boxed{
Z
=
C_N-B_N
=
\tanh\frac H2.
}
\]

This is an exact identity.

---

## 3. Selection becomes a sign projector

Under the living Neutral-Contrast Selection Principle,

\[
Q_{\rm retain}
=
\mathbf1_{(0,\infty)}(Z).
\]

Because \(\tanh(x/2)\) has the same sign as \(x\),

\[
\boxed{
Q_{\rm retain}
=
\mathbf1_{(0,\infty)}(H).
}
\]

Equivalently,

\[
H>0
\iff
0<Y<I,
\]

\[
H=0
\iff
Y=I,
\]

\[
H<0
\iff
Y>I
\]

spectrally.

Thus the selected/exported strata are ordinary positive/nonpositive spectral sectors of
the closure-depth operator.

---

## 4. Interpretation discipline

The name "closure depth" is mathematical shorthand only.

No claim is made that \(H\) is:

- physical time;
- energy;
- entropy;
- spacetime distance;
- action;
- a Hamiltonian.

Any such interpretation must be derived later from the frozen BFG master law.

For the present finite theory,

\[
H=-\log Y
\]

is simply a regular coordinate on the strictly positive load cone.

---

## 5. Scalar intrinsic-Gram recurrence

In the one-dimensional full-persistence regime,

\[
y_{n+1}
=
\frac{2y_n^2}
{(1+y_n)^2(1+y_n^2)}.
\]

Set

\[
h_n=-\log y_n.
\]

Then exactly

\[
\boxed{
h_{n+1}
=
2h_n
-\log2
+
2\log(1+e^{-h_n})
+
\log(1+e^{-2h_n}).
}
\]

For large positive \(h_n\),

\[
h_{n+1}
=
2h_n-\log2+o(1).
\]

Thus the neutral-load boundary \(y=0\) becomes an asymptotic large-\(H\) regime rather
than a finite-coordinate singularity.

---

## 6. Error bound

For \(h\ge0\),

\[
0
\le
2\log(1+e^{-h})
+
\log(1+e^{-2h})
\le
2e^{-h}+e^{-2h}.
\]

Hence

\[
\boxed{
2h-\log2
\le
h_+
\le
2h-\log2+2e^{-h}+e^{-2h}.
}
\]

The correction to the affine doubling law becomes exponentially small in closure
depth.

---

## 7. Renormalized scalar depth

Define

\[
\kappa_n
=
2^{-n}h_n.
\]

The recurrence gives

\[
\kappa_{n+1}-\kappa_n
=
2^{-(n+1)}
\left[
-\log2+\varepsilon(h_n)
\right],
\]

where

\[
\varepsilon(h)
=
2\log(1+e^{-h})
+
\log(1+e^{-2h}).
\]

For \(h\ge0\),

\[
0\le\varepsilon(h)\le3\log2.
\]

Therefore

\[
\sum_n
|\kappa_{n+1}-\kappa_n|
<\infty.
\]

So every scalar orbit with \(0<y_0\le1\) has a finite renormalized closure-depth limit

\[
\boxed{
\kappa_\infty
=
\lim_{n\to\infty}
2^{-n}h_n.
}
\]

This is a genuine asymptotic invariant of the selected scalar recurrence.

It is not yet assigned a physical meaning.

---

## 8. Why this matters for the field program

The finite master law now has two complementary coordinate descriptions:

### Load coordinate

\[
Y>0.
\]

Best for:

- Gram reconstruction;
- reciprocal loads;
- intrinsic positive geometry.

### Closure-depth coordinate

\[
H=-\log Y.
\]

Best for:

- exact Selection sign;
- asymptotic boundary analysis;
- renormalized large-depth limits.

This suggests a mathematically controlled route toward the later continuum program:

\[
\text{finite recursive depth}
\to
\text{renormalized closure-depth variables}
\to
\text{continuum generator}.
\]

The last arrow is still open and no spacetime or external field equation is assumed.
