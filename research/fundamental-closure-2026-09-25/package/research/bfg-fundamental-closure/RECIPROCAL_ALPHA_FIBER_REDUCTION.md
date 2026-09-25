# Reciprocal-Alpha Fiber Reduction Theorem

## 1. Purpose

Fixed-dimension o-minimality gives a uniform bound on every finite continuation fiber.

The only remaining route to non-finite memory is therefore a positive-dimensional
inverse fiber whose points have different continuation tangents.

For the selected full-persistent commuting load suspension, such a fiber can be reduced
to one continuous reciprocal variable.

---

## 2. Inverse equations at fixed phase

Let

\[
0<\omega<1
\]

and define

\[
q=\frac{1-\omega}{\omega}>0.
\]

Let the current anchor load be

\[
0<y_i<1.
\]

For a fixed reciprocal weight

\[
0<\alpha<\frac12,
\qquad
\beta=1-\alpha,
\]

the BFG endpoint is

\[
y_i^+
=
\frac{\alpha+\beta y_i^2}{(1+y_i)^2}.
\]

Let \(x_i\) denote the closure-depth phase readout:

\[
x_i
=
(1-\omega)(-\log y_i)
+
\omega(-\log y_i^+).
\]

Exponentiating gives

\[
\boxed{
c_i
=
e^{-x_i/\omega}
=
y_i^q
\frac{
\alpha+\beta y_i^2
}{
(1+y_i)^2
}.
}
\]

Thus, once \(\alpha\) is fixed, the inverse problem separates mode by mode.

---

## 3. Scalar derivative polynomial

Define

\[
f_{\alpha,\omega}(y)
=
y^q
\frac{
\alpha+\beta y^2
}{
(1+y)^2
}.
\]

The logarithmic derivative has the same sign as

\[
P_{\alpha,\omega}(y)
=
q\alpha
+
\alpha(q-2)y
+
\beta(q+2)y^2
+
q\beta y^3.
\]

This is cubic.

More strongly, its coefficient signs imply the following.

### Early phase

If

\[
q\ge2
\]

or equivalently

\[
\boxed{
\omega\le\frac13,
}
\]

all coefficients are nonnegative and the constant term is strictly positive.

Therefore

\[
\boxed{
f'_{\alpha,\omega}(y)>0
}
\]

for every \(y>0\).

So every coordinate inverse is unique.

### Later phase

If

\[
q<2,
\]

the coefficient sign pattern is

\[
+,-,+,+.
\]

By Descartes' rule of signs, \(P\) has at most two positive roots.

Therefore \(f\) has at most two positive critical points and any horizontal level has
at most three positive preimages.

Hence

\[
\boxed{
\#f_{\alpha,\omega}^{-1}(c)
\le3
}
\]

for every fixed \(\alpha,\omega,c\) in the selected domain.

The canonical three-root witness shows that this upper bound is attained.

---

## 4. Multi-mode sheet bound conditional on alpha

For \(d\) modes, fixed \(\alpha\) makes the inverse equations independent:

\[
f_{\alpha,\omega}(y_i)=c_i.
\]

Each coordinate has at most three selected solutions.

Therefore

\[
\boxed{
N_{\rm sheets}(\alpha)
\le
3^d
}
\]

for

\[
\omega>\frac13.
\]

For

\[
\omega\le\frac13,
\]

each coordinate inverse is unique:

\[
\boxed{
N_{\rm sheets}(\alpha)=1.
}
\]

This is an explicit sheet bound, unlike the qualitative o-minimal constant \(B_d\).

---

## 5. Why alpha lies in the selected interval

The full-persistent reciprocal weight can be written as

\[
\alpha
=
\frac{
\sum_i
r_i y_i^2/(1+y_i)
}{
\sum_i
r_i(1+y_i^2)/(1+y_i)
}.
\]

Equivalently, it is a positive weighted average of

\[
\frac{y_i^2}{1+y_i^2}.
\]

Since

\[
0<y_i<1,
\]

every term satisfies

\[
0<
\frac{y_i^2}{1+y_i^2}
<
\frac12.
\]

Therefore

\[
\boxed{
0<\alpha<\frac12.
}
\]

So the selected inverse problem uses one scalar reciprocal parameter in a bounded open
interval.

---

## 6. Fiber-dimension reduction

Consider one inverse fiber at fixed readout and fixed phase.

Map every anchor in that fiber to its reciprocal weight

\[
\alpha.
\]

For each fixed \(\alpha\), there are at most

\[
3^d
\]

anchor points.

Therefore the fiber is a finite-to-one cover of a subset of the one-dimensional
\(\alpha\)-interval.

Consequently

\[
\boxed{
\dim(\text{anchor fiber})\le1.
}
\]

This conclusion uses only the separated fixed-alpha inverse equation.

No positive-dimensional fiber of dimension two or higher can occur in this
full-persistent commuting load sector.

---

## 7. Continuous-memory upper bound

If the inverse fiber is finite, the earlier o-minimal theorem supplies a finite branch
label.

If the inverse fiber is positive dimensional, its continuous part can be parametrized
by

\[
\boxed{\alpha}
\]

together with a discrete coordinate-sheet index.

Thus the worst-case continuation memory in this sector has the form

\[
\boxed{
M=
(\alpha,\sigma),
}
\]

where

\[
\sigma
\in
\{1,\ldots,3^d\}
\]

is a fixed-alpha sheet label.

This is an upper bound on representation complexity, not a claim that all \(3^d\)
sheets coexist for one \(\alpha\).

---

## 8. Early-phase simplification

For

\[
0<\omega\le\frac13,
\]

the fixed-alpha coordinate inverse is unique.

Therefore any positive-dimensional ambiguity can involve only variation in the single
global reciprocal coordinate \(\alpha\).

No additional per-mode sheet bit is required in this early-phase region.

This gives a particularly simple memory chart:

\[
\boxed{
M=\alpha
}
\]

only if a positive-dimensional inverse fiber actually exists.

---

## 9. Consequence for full-persistent locked orbits

Once an exact orbit enters

\[
P=I,
\qquad
0<Y<I,
\]

it remains in the full-persistent selected class.

Its carrier dimension is fixed.

Within the declared closure-depth suspension, any continuation ambiguity is therefore
bounded by:

- one continuous reciprocal coordinate \(\alpha\);
- a finite sheet index;
- no growing carrier coordinate.

So even if a dynamically inequivalent positive-dimensional fiber exists, the required
continuous memory dimension is at most one in this locked load sector.

---

## 10. What remains open

The theorem does **not** prove that positive-dimensional fibers actually occur for
strictly positive formation weights.

It proves:

\[
\boxed{
\text{if they occur, they are at most one-dimensional and alpha-parametrizable.}
}
\]

The strongest remaining question is now:

> Does the BFG reciprocal self-consistency equation permit an interval of \(\alpha\)
> values on one fixed readout fiber, or are all admissible fibers in fact finite?

If no such interval exists, then every full-persistent finite-dimensional orbit needs
only finite continuation-memory state under the current continuum completion.
