# A constructive finite configuration-to-Hilbert bridge

Date: 3 November 2026. Existing BFG-Engine research-stage continuation. No new physical law, published paper or event rule is introduced.

## 1. Concrete result

**Given a finite invariant configuration sector and its source comparison data, an explicit information-preserving Hilbert representation can be built.** A supplied primitive configuration transition can also be represented exactly by a linear operator. This completes a conditional representation construction rather than merely naming an unknown embedding.

It does not derive the configuration sector, comparison functional, threshold or first transition from the earlier quartic minimum. Nor does information preservation alone select the full Hilbert geometry or identify the resulting classical count observable with every role of the BFG informational coupling operator.

The source inputs are the Level-0 formula `i_x=log|C_theta(x)|`, the foundational source's primitive recursion, and its stated Hilbert-realization role. [SOURCES.json](SOURCES.json) records their actual anchors. The previous [count/domain audit](../origin_information_domain/README.md) remains valid; the construction below does not silently assign arbitrary configurations to preselected superpositions.

## 2. Always-available finite count representation

Let Omega={x_1,...,x_N} be a **specified finite sector**, let its nonempty comparison neighborhoods C_theta(x) be specified, and set `i_x=log|C_theta(x)|>=0` using a fixed log base greater than one. Define

```math
\mathcal H_{\rm cfg}=\ell^2(\Omega),\qquad
\iota(x)=e_x,\qquad
\widehat I_{\rm count}=\sum_x i_x|e_x\rangle\langle e_x|.
```

This map is injective and its basis vectors have norm one. The operator is positive semidefinite, and

```math
\langle\iota(x),\widehat I_{\rm count}\iota(x)\rangle=i_x.
```

It is the unique multiplication operator representing this classical function in the diagonal algebra of configuration labels. Relabelling configurations produces simultaneous unitary permutation of the vectors and operator.

This is a mathematical representation convention, not a newly asserted physical inner product. Its basis Gram is the Kronecker delta. It preserves the supplied scalar information values, but does not generally preserve the source similarity numbers or the corrected history-space metric. If those must be preserved too, additional compatibility tests are necessary. Also, uniqueness within the diagonal algebra is not uniqueness among all Hermitian operators: knowing only N basis expectations leaves off-diagonal entries unspecified.

## 3. Exact recursion representation from a given source transition

Suppose r:Omega->Omega is the specified primitive transition and Omega is invariant under it. Define the unique linear lift on the configuration basis by

```math
T_r e_x=e_{r(x)}.
```

Then `T_r^m e_x=e_{r^m(x)}` for every finite m. This is an exact intertwining of the supplied discrete configurations with their represented basis states, not a guessed state-transition matrix.

Every column of T_r^m has one entry equal to one, so its Frobenius norm is sqrt(N). Consequently

```math
\sup_m\|T_r^m\|_2\le\sqrt N.
```

Finite total deterministic configurations therefore give a power-bounded lift, even when r merges configurations. T_r is unitary exactly when r is a permutation. The construction neither supplies physical time nor identifies T_r with the complete BFG conjugate operator without the relevant source role/neutral-mediation conditions.

There are two distinct meanings of 'preserving information':

1. The representation preserves each configuration's scalar value at its image, as proved above.
2. Dynamical conservation would require an additional condition. On basis states it is `i_{r(x)}=i_x`. On every superposition it is the stronger operator identity `T_r* I_count T_r=I_count`.

The entries of that identity are

```math
(T_r^*I_{\rm count}T_r)_{xy}
=\mathbf1_{r(x)=r(y)}\,i_{r(x)}.
```

Thus constant information along basis transitions does not by itself imply conservation on all superpositions: collisions into a positive-information output create cross terms. This is a test of a proposed conservation requirement, not a new conservation law imposed on BFG.

## 4. Smaller representation when similarity really is an equivalence relation

If the supplied threshold relation is a partition Omega=C_1 disjoint-union ... disjoint-union C_r, let m_a=|C_a| and

```math
\chi_a=\mathbf1_{C_a}/\sqrt{m_a}\in\ell^2(\Omega).
```

The chi_a are orthonormal. On their span define the class representation

```math
v_x=\chi_{a(x)},\qquad
I_{\rm class}=\sum_a\log(m_a)|\chi_a\rangle\langle\chi_a|.
```

It preserves the source count values and has feature Gram `K_xy=1` within a class and zero across classes. The map is injective on these similarity classes, not on all original configurations. This quotient is not automatically the source's asymptotic-history quotient or its complete future-behavioral quotient.

A transition on classes exists exactly when

```math
x\sim y\Longrightarrow r(x)\sim r(y).
```

Without this congruence condition, collapsing a similarity class loses the ability to predict its next class. The exact controls include a failure example. Counting the same number of similar configurations is weaker still than belonging to the same class and does not imply dynamic equivalence.

Even for the correct class Gram, the full positive information operator need not be unique. Let c_a=log(m_a). The count observations fix only the diagonal `J_aa=c_a` in the chi frame. For c_a>0, all positive solutions have the form

```math
J=D^{1/2} C D^{1/2},\qquad
D=\operatorname{diag}(c_a),\quad C\succeq0,\quad C_{aa}=1.
```

If c_a=0, positivity forces that row and column of J to vanish. At least two positive c_a permit nontrivial off-diagonal correlations. Requiring J to commute with every individual class projector removes those entries and selects I_class, but that is the extra demand to represent the classical class algebra. The source count formula alone does not prove it is the full coupling operator used in R=J F_op J.

## 5. Preserving a supplied similarity kernel

If the requirement is instead `k(x,y)=<v_x,v_y>` for a fixed Hermitian kernel with k(x,x)=1, a finite Hilbert feature representation exists exactly when its matrix K is positive semidefinite. Necessity follows from `a*Ka=||sum a_x v_x||^2>=0`; sufficiency follows by factoring K=V*V. Its minimal feature dimension is rank(K), and the spanning feature system is unique up to unitary change of coordinates.

Feature existence alone does not guarantee an injective embedding of distinct labels. That additionally requires `K_xx+K_yy-2 Re(K_xy)>0` for every pair that must remain distinct. The class construction deliberately identifies labels within one comparison class; the free configuration representation does not.

Generic symmetric reflexive similarities need not pass that test. The chain matrix

```math
K=\begin{pmatrix}1&1&0\\1&1&1\\0&1&1\end{pmatrix}
```

has eigenvalue 1-sqrt(2)<0 and cannot be that exact Gram. Its threshold neighborhoods still have valid finite counts 2,3,2. The free configuration representation can preserve those count values, but does not preserve this indefinite similarity as an inner product. No spectral clipping or replacement kernel is adopted to conceal the failure.

There is also an exact positivity/compatibility criterion once a positive K is supplied. With V=K^(1/2) on the minimal feature carrier H=Ran(K), a positive J with configuration values i_x exists exactly when there is W satisfying

```math
W\succeq0,\quad\operatorname{diag}W=i,
\quad\ker K\subseteq\ker W.
```

Necessity uses W=V*JV. Conversely, define `J=K^(+1/2) W K^(+1/2)` on Ran(K); the support condition gives V*JV=W. Thus the bridge reduces to explicit finite linear/positive constraints, not an unnamed unknown map. This theorem does not assert that every source comparison has a positive kernel or supplies a unique W.

## 6. Worked positive example and precise limitations

The exact worked packet uses five labels a,b,c,d,e, comparison classes `{a,b}` and `{c,d,e}`, and transition

```math
a\mapsto b,\quad b\mapsto a,\quad
c\mapsto d,\quad d\mapsto e,\quad e\mapsto c.
```

The constructed configuration carrier is C^5, the count operator is

```math
I_{\rm count}=\operatorname{diag}(\log2,\log2,\log3,\log3,\log3),
```

and T_r is the exact permutation matrix recorded in [results.json](results.json). It is unitary, intertwines all basis transitions and preserves the count operator on the whole carrier. The similarity-class representation has dimension two and gives I_class=diag(log2,log3); its induced class transition is identity, correctly discarding the internal cycles. This is a successful explicit representation for the supplied packet, not a recovery of the entire original configuration dynamics from class information alone.

On the two-class carrier, an operator with off-diagonal entry `sqrt(log2 log3)/2` is also positive and gives exactly the same class-configuration information values. It differs on superpositions and is not a representation gauge when all feature vectors are held fixed: an intertwining unitary fixing their spanning basis is identity. Thus representing the classical observable and identifying the full operator are distinct.

One further boundary matters for the raw recursion grammar. If I_count>0, the **additional role identification** J=I_count would permit the conditional factor assignment `F_op=J^(-1)T_r J^(-1)`. That is algebraic factor reconstruction after a role choice, not proof of the historical primitive factors. If a comparison class is a singleton, log(1)=0 and J is singular. For identity configuration transition, `T_r e_x=e_x` on that zero-information label, whereas `J F_op J e_x=0` for every linear F_op. The simultaneous identifications then fail unless an appropriate source domain restriction or different role map is justified. No zero-information states are silently deleted here.

The existing source condition Phi>0 is relevant: under this same role identification and a positive binding denominator, J e_x=0 makes the balance numerator zero, so that individual zero-information basis state cannot belong to the positive-order operator sector. If the supplied transition keeps the positive-information configuration set Omega_+ invariant, its restricted count operator is invertible and the factor construction works there. Both that invariance and the sector restriction must be checked. Excluding zero-information basis states does not by itself prove that every admissible superposition lies in Ran(J), or that the representation of the complete pre-interface domain should be discarded.

The construction's superpositions are mathematical vectors. They are not automatically source origin configurations or admissible physical states, and their quadratic values need not be integer class-count logarithms. This is why the earlier finite-count/open-patch isotropy theorem is not contradicted. Actual local probe access remains a separate source obligation.

## 7. Outcome

We now have an explicit finite bridge builder and exact tests for information values, recursion, quotient congruence, Gram positivity and operator-role compatibility. The mathematical existence step is completed **for supplied finite configuration data**. A canonical diagonal count observable is available without inventing a physical equation.

What remains unestablished is that the BFG origin uniquely supplies that finite packet, selects this geometry/class algebra as its physical realization, permits the full superposition domain and identifies I_count with every informational coupling role. Those statements are not consequences merely of having an information-preserving representation.

Run `python configuration_hilbert_bridge/check_bridge.py`. The positive worked construction and the negative compatibility controls are recorded in [results.json](results.json). They do not prove empirical realization, the complete canonical nine-role state correspondence or a unique fundamental initializer. The published preprint and preserved event remain unchanged.
