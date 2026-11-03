# Foundational balance-history quotient: exact error and coherent continuations

## 1. Source statement checked

In the plugin's BFG_BALANCE_FIELD_EQUATION_FW.pdf, the embedded **Foundational Balance–Field Framework** defines, at PDF pages 441–442 (internal pp.8–9),

```math
X\sim_\infty Y\iff |\Phi(R^nX)-\Phi(R^nY)|\longrightarrow0,
```

then proposes the distance on the resulting classes

```math
D(X,Y)=\sum_{n=0}^{\infty}2^{-n}
\frac{|\Phi(R^nX)-\Phi(R^nY)|}{1+|\Phi(R^nX)-\Phi(R^nY)|}.
```

Both formulas were verified visually in the actual plugin PDF. The source's proof checks that D=0 implies equivalence, but does not check that equivalent representatives have distance zero or leave all class distances unchanged.

## 2. Exact counterexample

Take configurations a,b,c with R(a)=R(b)=R(c)=c, and Phi(a)=Phi(c)=1, Phi(b)=5/4. Extend this assignment to any other finite primitive configurations by mapping them to c with Phi=1. All configurations lie in the source's epsilon=1/4 balance band, which is invariant here. Their relevant histories are

```math
h_a=(1,1,1,\ldots),\qquad
h_b=(5/4,1,1,\ldots).
```

They are asymptotically equivalent, so [a]=[b]. But D(a,b)=1/5, while D(a,a)=0. Hence the printed distance is not a well-defined metric on the stated quotient. The advertised metric-completion argument cannot use that pair of definitions unchanged.

This is a specific source-level mathematical obstruction. It does not refute the separate finite event, prove the whole BFG inconsistent, or establish that no other origin construction exists.

## 3. Coherent continuation A: retain complete histories

Keep D, but quotient by exact equality of **all** history entries. For f(t)=t/(1+t),

```math
f(a)+f(b)-f(a+b)
=\frac{ab(a+b+2)}{(a+1)(b+1)(a+b+1)}\ge0
\quad(a,b\ge0).
```

Monotonicity and this subadditivity give a triangle inequality term by term. D is a bounded pseudometric on configurations, D=0 exactly for equal complete histories, and thus induces a genuine metric on that finer quotient. Its bound is D<=sum 2^(-n)=2.

On an R-invariant domain, the history-shift action satisfies

```math
D(RX,RY)=2\big(D(X,Y)-f(|\Phi(X)-\Phi(Y)|)\big)\le2D(X,Y).
```

It therefore descends to the exact-history quotient and extends uniquely as a 2-Lipschitz map to its metric completion. This retains transient differences and changes the source's equivalence relation.

## 4. Coherent continuation B: retain asymptotic identity

Keep the source equivalence relation, but define instead

```math
d_\infty(X,Y)=\limsup_{n\to\infty}
f(|\Phi(R^nX)-\Phi(R^nY)|).
```

This is finite and bounded by one. The same pointwise triangle inequality, together with limsup(u_n+v_n)<=limsup u_n+limsup v_n, makes it a pseudometric. Its zero relation is exactly the source's asymptotic equivalence: limsup f(a_n)=0 for nonnegative a_n implies a_n->0, and the converse follows by continuity.

A pseudometric always has representative-independent distances on its zero quotient: if d(X,X')=d(Y,Y')=0, the triangle inequality gives both d(X,Y)<=d(X',Y') and the reverse. Hence d_infinity is a genuine metric on the intended asymptotic classes. On an R-invariant domain,

```math
d_\infty(RX,RY)=d_\infty(X,Y).
```

The induced recursion is an isometry and extends uniquely as an isometry to the completion. Surjectivity is not asserted. For the counterexample the repaired asymptotic distance is zero, as required.

This construction preserves asymptotic identity and discards finite transients. It is a mathematically valid repair option, not proof that this particular metric is uniquely forced by BFG primitives. The alternative complete-history construction retains different information. Neither option is silently substituted into the published paper or event code.

## 5. What is not obtained by either correction

The foundational source already introduces a primitive recursion map R before defining histories. Correcting the quotient does not derive R from Phi alone. Nor does metric completion uniquely choose a linear/Hilbert realization, the informational and feedback operators, a source-neutral completion, or their origin values. Section 10 of the embedded source states a Hilbert realization as a pair with a structure-preserving embedding; the metric argument does not uniquely construct that extra structure.

Thus the corrected mathematics supplies a coherent state-space route **given the selector and recursion**, with its equivalence choice explicit. It cannot be used circularly as a derivation of the same previously supplied primitive recursion.
