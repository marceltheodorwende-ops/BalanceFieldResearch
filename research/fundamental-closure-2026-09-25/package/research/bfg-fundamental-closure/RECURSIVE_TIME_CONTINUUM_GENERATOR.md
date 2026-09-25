# Exact Recursive-Time Generator in the Selected Scalar BFG Sector

## 1. Why a naive continuum limit is not allowed

The finite BFG master law is a discrete reclosure map.

A single step is not parametrized by a small number \(\varepsilon\to0\), and on the
scalar closure-depth coordinate the asymptotic step is approximately

\[
h_{n+1}\simeq2h_n-\log2.
\]

Therefore

\[
h_{n+1}-h_n
\]

is not an infinitesimal increment.

So one may **not** simply declare

\[
\partial_t h=h_{n+1}-h_n
\]

and call the result the BFG field equation.

A legitimate continuous description must embed the exact discrete map into a
one-parameter flow.

---

## 2. Scalar selected map

In the one-dimensional full-persistence intrinsic-Gram sector,

\[
\boxed{
f(y)
=
\frac{2y^2}{(1+y)^2(1+y^2)}.
}
\]

For every \(y>0\),

\[
f(y)\le\frac14.
\]

Indeed,

\[
(1+y)^2(1+y^2)-8y^2
=
(y-1)^2(y^2+4y+1)\ge0.
\]

Also,

\[
f(y)=f(y^{-1}),
\]

so the map is not globally one-to-one on \((0,\infty)\).

But

\[
f'(y)
=
-\frac{
4y(y-1)(y^2+y+1)
}{
(y+1)^3(y^2+1)^2
},
\]

hence

\[
\boxed{
f'(y)>0
\quad\text{for}\quad
0<y<1.
}
\]

This is exactly the neutral-contrast retained branch

\[
0<y<1.
\]

Thus the BFG Selection rule removes the branch ambiguity and leaves an invertible
scalar reclosure sector.

---

## 3. Böttcher coordinate

The fixed point \(y=0\) is superattracting because

\[
f(y)=2y^2+O(y^3).
\]

Standard Böttcher conjugacy therefore motivates the normalized coordinate

\[
\phi(y)
=
\lim_{n\to\infty}
\left(
f^{\circ n}(y)
\right)^{1/2^n},
\]

with

\[
\phi(y)\sim2y
\qquad
(y\to0^+).
\]

Equivalently define the logarithmic coordinate

\[
\boxed{
\theta(y)
=
-\log\phi(y)
=
\lim_{n\to\infty}
2^{-n}
\left[
-\log f^{\circ n}(y)
\right].
}
\]

This is precisely the renormalized closure-depth limit already obtained in the
asymptotic audit.

It satisfies the exact functional equation

\[
\boxed{
\theta(f(y))=2\theta(y).
}
\]

Equivalently,

\[
\boxed{
\phi(f(y))=\phi(y)^2.
}
\]

This is a mathematical conjugacy result, not a new physical law.

---

## 4. Exact continuous recursive time

Define the dimensionless recursive-time parameter \(\tau\) by

\[
\boxed{
\theta(y(\tau))
=
e^\tau\theta(y_0).
}
\]

Then

\[
y(0)=y_0
\]

and the family has the semigroup property

\[
\boxed{
F_{\tau+\sigma}
=
F_\tau\circ F_\sigma.
}
\]

Choose one discrete BFG step to correspond to

\[
\Delta\tau=\log2.
\]

Then

\[
\theta(F_{\log2}(y))
=
2\theta(y)
=
\theta(f(y)).
\]

By injectivity on the selected branch,

\[
\boxed{
F_{\log2}(y)=f(y).
}
\]

Thus the continuous flow is an **exact embedding** of the discrete selected scalar
BFG reclosure, not a finite-difference approximation.

The parameter \(\tau\) is recursive time only. It is not yet identified with physical
time.

---

## 5. Continuous generator

Differentiate

\[
\theta(y(\tau))
=
e^\tau\theta(y_0).
\]

Then

\[
\theta'(y)\frac{dy}{d\tau}
=
\theta(y).
\]

Therefore the exact scalar generator is

\[
\boxed{
\frac{dy}{d\tau}
=
\mathcal V_{\rm BFG}(y)
=
\frac{\theta(y)}{\theta'(y)}.
}
\]

Because \(\theta'(y)<0\) on the retained branch,

\[
\mathcal V_{\rm BFG}(y)<0.
\]

In the Böttcher coordinate itself,

\[
\boxed{
\frac{d\theta}{d\tau}
=
\theta.
}
\]

This is the simplest exact continuous BFG recursion law obtained so far.

It is linear because all nonlinear scalar reclosure geometry has been absorbed into
the canonical conjugacy \(\theta\).

---

## 6. Closure-depth form

With

\[
h=-\log y,
\]

write the same Böttcher depth as

\[
\Theta(h)
=
\theta(e^{-h}).
\]

Then

\[
\boxed{
\Theta(h(\tau))
=
e^\tau\Theta(h_0)
}
\]

and

\[
\boxed{
\frac{dh}{d\tau}
=
\frac{\Theta(h)}{\Theta'(h)}.
}
\]

For large closure depth,

\[
\Theta(h)=h-\log2+o(1),
\]

so

\[
\frac{dh}{d\tau}
=
h-\log2+o(1).
\]

Again, this is an asymptotic recursive-depth flow, not yet physical spacetime
dynamics.

---

## 7. Why this is canonical only on the selected branch

The full positive scalar map obeys

\[
f(y)=f(1/y),
\]

so it cannot be globally inverted.

The BFG neutral-contrast Selection principle separates

\[
y<1
\]

from

\[
y>1.
\]

On the retained sector \(0<y<1\), the map is monotone and the continuous semigroup is
single-valued.

Therefore Selection is not an optional decoration of the continuum construction. It
is what makes the continuous recursive-time embedding well posed.

---

## 8. Conditional operator lift

Suppose a fixed finite stratum is spectrally decoupled so that its load update is
exactly modewise:

\[
Y_+
=
f(Y)
\]

by functional calculus, with

\[
0<Y<I.
\]

Then define

\[
\Theta(Y)
=
\theta(Y)
\]

by spectral functional calculus.

The discrete update obeys

\[
\boxed{
\Theta(Y_+)=2\Theta(Y).
}
\]

The exact continuous spectral flow is therefore

\[
\boxed{
\Theta(Y(\tau))
=
e^\tau\Theta(Y_0).
}
\]

This operator lift is **conditional** on genuine modewise closure.

The current general noncommuting BFG master update is not yet proved to reduce to
\(Y_+=f(Y)\), so this must not be promoted to the full operator field equation.

---

## 9. Stratified continuum architecture

The general finite BFG runtime contains exact events:

- Selection / Export;
- rank change;
- R4 polar support transport;
- no-choice formation seeding;
- terminal transitions.

Those operations can change dimension or support discontinuously.

Therefore the natural continuum object suggested by the current mathematics is not
yet one global smooth ODE.

It is a **stratified hybrid flow**:

\[
\boxed{
\text{continuous recursive flow inside a fixed stratum}
\quad+\quad
\text{exact BFG event maps between strata}.
}
\]

In schematic form,

\[
\dot X
=
\mathcal L_\sigma(X),
\qquad
X\in\mathfrak X_\sigma,
\]

followed at an exact event surface by

\[
X^+
=
\mathcal J_{\sigma\to\sigma'}(X^-).
\]

For the scalar retained stratum,

\[
\mathcal L_\sigma
\]

is now explicitly known through the Böttcher generator above.

For the full noncommuting operator state, deriving \(\mathcal L_\sigma\) remains open.

---

## 10. What has and has not been achieved

### Achieved

A canonical exact continuous interpolation of the selected scalar BFG reclosure:

\[
\boxed{
F_{\log2}=f.
}
\]

An exact recursive-time generator:

\[
\boxed{
\partial_\tau\theta=\theta.
}
\]

A mathematically clean explanation of why the finite recursion can have a continuum
description without pretending that the original step was infinitesimal.

### Not achieved

This is not yet:

- physical time;
- spacetime;
- a spatial field theory;
- gravity;
- quantum dynamics;
- a full noncommutative continuum generator.

Those must be derived later from the same frozen finite BFG architecture.
