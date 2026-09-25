# Carrier-Dimension Monotonicity and Full-Persistence Lock Theorem

## 1. Question

The global memory-graph theorem shows that branch multiplicity can grow at least as

\[
3^{n-1}
\]

across finite \(n\)-mode state spaces.

That raises a dynamical question:

> Can one exact finite BFG orbit keep increasing its carrier dimension and thereby force
> unbounded continuation memory?

For the current finite master candidate, the answer is no.

The carrier dimension is monotone nonincreasing.

---

## 2. Carrier-dimension monotonicity theorem

At step \(n\), the cross-fed analysis operator has the form

\[
\mathcal A_n:
\mathcal H_n
\longrightarrow
\mathcal H_n\oplus\mathcal H_n.
\]

The successor carrier is the reduced active range of this map.

Therefore

\[
\dim\mathcal H_{n+1}
=
\operatorname{rank}\mathcal A_n.
\]

But the rank of a linear map cannot exceed the dimension of its domain:

\[
\boxed{
\operatorname{rank}\mathcal A_n
\le
\dim\mathcal H_n.
}
\]

Hence

\[
\boxed{
d_{n+1}\le d_n,
\qquad
d_n:=\dim\mathcal H_n.
}
\]

So every exact finite orbit beginning with finite \(d_0\) obeys

\[
\boxed{
d_n\le d_0
\quad\text{for every finite }n.
}
\]

The doubled codomain does not imply carrier growth; the reduced SVD rank is bounded by
the original source dimension.

---

## 3. Finite number of carrier-dimension drops

Because

\[
d_n\in\mathbb N
\]

and

\[
d_{n+1}\le d_n,
\]

the carrier dimension can strictly decrease only finitely many times.

After at most

\[
d_0-1
\]

strict drops, it must stabilize at some integer

\[
d_\infty\le d_0.
\]

This does not imply that every other state coordinate converges.

It only proves eventual carrier-dimension constancy.

---

## 4. Persistence rank is bounded by the initial carrier

Let

\[
p_n=\operatorname{rank}P_n.
\]

Always

\[
p_n\le d_n.
\]

Therefore

\[
\boxed{
p_n\le d_0
}
\]

for every finite step.

Thus persistent rank may increase and decrease, but it can never exceed the initial
finite carrier dimension.

This corrects the earlier weaker estimate

\[
p_{n+1}\le p_n+1.
\]

That estimate is still true under the simple-seed completion, but by itself obscures
the stronger carrier bound.

---

## 5. Repeated rank increase is possible

Carrier non-growth does **not** mean persistence cannot grow repeatedly inside the
existing carrier.

A deterministic four-dimensional state in the package has

\[
d_0=4,
\qquad
p_0=2.
\]

The first exact successful update gives

\[
\boxed{
p_0=2\longrightarrow p_1=3,
\qquad
d_1=4.
}
\]

The second successful update gives

\[
\boxed{
p_1=3\longrightarrow p_2=4,
\qquad
d_2=4.
}
\]

So one orbit can realize repeated persistent-rank growth:

\[
\boxed{
2\to3\to4
}
\]

without any carrier-dimension increase.

This distinguishes:

- **formation/persistence expansion inside an existing carrier**, from
- **creation of new carrier dimensions**.

The current finite master law supports the first, not the second.

---

## 6. Full-persistence selected lock theorem

Assume a generated state satisfies

\[
P=I
\]

and

\[
0<Y<I.
\]

Then Neutral-Contrast Selection retains the entire carrier:

\[
Q_{\rm retain}=I.
\]

The \(G\)-orthogonal persistent projector is also

\[
P_G=I.
\]

With positive reciprocal weights,

\[
\mathcal A
=
\begin{bmatrix}
\sqrt\alpha\,C_N(Y)\\
\sqrt\beta\,B_N(Y)
\end{bmatrix}.
\]

Both \(C_N(Y)\) and \(B_N(Y)\) are strictly positive/invertible because \(Y>0\).

Hence

\[
\mathcal A^\dagger\mathcal A
=
\alpha C_N(Y)^2
+
\beta B_N(Y)^2
>0.
\]

Therefore

\[
\boxed{
\operatorname{rank}\mathcal A=d.
}
\]

So the next carrier has the same dimension.

There is no emergent complement to seed:

\[
E=0.
\]

The persistent projector remains

\[
\boxed{
P_+=I.
}
\]

---

## 7. Selected load interval remains invariant

In the eigenbasis of \(Y\), the full-persistent successor eigenvalues are

\[
y_i^+
=
\frac{
\alpha+\beta y_i^2
}{
(1+y_i)^2
}.
\]

If

\[
0<y_i<1,
\]

then

\[
0<\alpha+\beta y_i^2<1
\]

and

\[
(1+y_i)^2>1.
\]

Therefore

\[
\boxed{
0<y_i^+<1.
}
\]

Thus the class

\[
\boxed{
P=I,\qquad 0<Y<I
}
\]

is forward invariant under every successful exact full-persistent step.

Once an orbit enters this class, its persistence rank is locked to the carrier
dimension and no later Selection-driven rank loss or emergent rank gain occurs.

---

## 8. Consequence for the repeated-growth fixture

The deterministic orbit

\[
2\to3\to4
\]

reaches

\[
P=I
\]

on its second successful step.

From that point onward,

\[
\boxed{
p_n=d_n=4
}
\]

for every later exact successful step.

The remaining evolution occurs in the full-persistent load/capacity/density stratum,
with the familiar asymptotic approach of the positive load toward the neutral
dual-order boundary.

---

## 9. Consequence for memory growth

The earlier global memory theorem remains correct as a statement about the **whole
family of finite-dimensional state spaces**:

\[
N_{\rm branches}(d)\ge3^{d-1}
\]

for suitable \(d\)-mode continuum charts.

But a single orbit beginning in finite dimension \(d_0\) cannot access arbitrarily
large \(d\), because

\[
d_n\le d_0.
\]

Therefore:

\[
\boxed{
\text{unbounded memory growth via unbounded carrier dimension is impossible along one fixed finite orbit.}
}
\]

This is an important correction to the previous open-orbit discussion.

---

## 10. What remains open about single-orbit memory

Carrier boundedness does **not yet** prove that the continuation-memory requirement is
uniformly bounded along every fixed-\(d_0\) orbit.

A different mechanism could in principle produce increasing branch complexity inside
one fixed-dimensional suspension family.

The remaining question is therefore narrower:

> For fixed finite carrier dimension \(d\), is the number of dynamically distinct
> continuation branches uniformly bounded over all admissible readouts and phases?

The constructive exponential theorem gives a lower bound as dimension varies.

It does not answer this fixed-dimension upper-bound question.

So the single-orbit memory problem has been reduced from a rank-growth problem to a
fixed-dimensional inverse-geometry problem.

---

## 11. Corrected dynamical alternatives

For a finite initial carrier, the current master law allows:

1. finite carrier-dimension drops, after which \(d_n\) stabilizes;
2. persistent-rank gain/loss inside that bounded carrier;
3. entry into the full-persistent selected lock class;
4. continued full-rank load evolution toward an asymptotic boundary;
5. exact structural terminal events from the previously declared gates.

It does **not** allow unbounded carrier-dimension creation.

This sharply narrows the route by which BFG memory complexity could become unbounded
along one exact orbit.
