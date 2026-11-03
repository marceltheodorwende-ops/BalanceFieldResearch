# What complete future observations identify about an origin model

Date: 3 November 2026. BFG-Engine research-stage continuation. No new physical law or origin datum is installed.

## 1. Source connection and scope

The September 22 canonical BFG source, Section 11, paragraphs 225–230, defines equivalence by the complete future stream of its **full canonical datum** Xi_U and proves that this relation is a transition congruence. This is stronger than merely comparing a scalar order parameter or a count-information value.

We apply the same mathematical construction to a **specified** observable family o on a supplied finite configuration model. Our worked observations are the balance value and Level-0 class-count information. They are not claimed to exhaust Xi_U, the nine-role plugin state, or all source physical observables. The distinction prevents an observational limitation from being mistaken for a contradiction of the full canonical quotient.

The candidate configuration transition r is also not silently identified with the November finite event U; the congruence argument applies to each specified deterministic system, but their source roles and domains remain distinct.

The result has two parts: a unique minimal observable model can be computed from complete behavior, but even all future balance/count observations need not determine the underlying configurations or primitive transition.

## 2. Exact finite predictive quotient

Given finite Omega, transition r:Omega->Omega and observations o, define

```math
x\equiv_o y\quad\Longleftrightarrow\quad
o(r^n x)=o(r^n y)\ \text{for every }n\ge0.
```

Dropping the first observation proves `x equiv_o y => r(x) equiv_o r(y)`. Thus the quotient transition is well defined. This is the **coarsest transition congruence preserving o**: any other observation-preserving congruence must preserve every iterated observation, so it refines equiv_o.

There is a finite exact algorithm:

1. Partition configurations by their current observation o(x).
2. Split each block according to the block containing the successor r(x).
3. Repeat until no block changes.

After k refinements, two configurations remain together exactly when their observations agree through time k. Every proper refinement increases the number of blocks. With N configurations and b_0 initial observation blocks, at most N-b_0 proper refinements are possible. Once stable, the partition is a congruence, so equality at all future times follows by induction.

Consequently this procedure computes the infinite-future equivalence **exactly** for the supplied finite model. It is not a floating threshold, a conjecture from a finite simulation or a method for infinite unknown state spaces. For a single specified origin, inaccessible configurations can first be removed by restricting to its forward-reachable sector.

## 3. What is unique

Index a quotient state by its distinct infinite observation stream. Its output is the stream's first term and its successor is the left shift. This gives a separating deterministic realization of the supplied behavior set. Any other finite separating realization with the same complete behavior set is isomorphic through the map sending each state to that stream.

Thus the minimal observable model is unique up to state relabelling **once the complete behavior set is supplied**. The algorithm can compute it when the original finite model is supplied. It does not infer unknown future data from a single present value.

A free Hilbert representation of these quotient labels, as constructed in the previous step, is then determined up to unitary permutation for that chosen orthogonal-label convention. This is not a proof that every possible Hilbert geometry, inner product or physical state realization is uniquely fixed.

## 4. Information histories can expose hidden transitions

Take comparison classes `{a,b,c}` and `{d,e}`, whose source information values are log(3) and log(2). Use

```math
a\mapsto b,\ b\mapsto c,\ c\mapsto d,\ d\mapsto d,\ e\mapsto d.
```

At the current step a,b,c have identical count information. Their future count histories differ: the first reaches log(2) after three steps, the second after two and the third after one. Exact refinement produces four predictive classes `{a}`, `{b}`, `{c}`, `{d,e}`. The source similarity classes alone were not a transition congruence; the full count future resolves that ambiguity automatically.

This is a useful constructive improvement: it specifies a dynamics-respecting quotient without guessing how to merge configurations. It remains relative to the observations and transition supplied.

## 5. All such future observations still need not determine the underlying model

Consider two positive-information packets:

- Two configurations in one size-two comparison class, with a two-cycle transition.
- Four configurations in two size-two comparison classes, with a four-cycle transition.

Let the balance observation be one in both. Every configuration in both models has count information log(2) at every future step. These underlying finite systems are not isomorphic: they have different cardinalities and cycle lengths. Their free transition representations also have different dimensions. Nevertheless their observation-stream sets coincide, and both reduce to the same single-state observable model.

This is **not** a counterexample to the source's full Xi_U quotient: canonical carrier dimension or a sufficiently rich transition invariant would distinguish the models if included in Xi_U. It is an exact non-identifiability result for the specified balance/count packet. It also does not prove that both examples solve every source field equation or represent natural systems.

There is a general replication construction. Given a finite model, make k copies with labels (x,a). Preserve comparison neighborhoods within each copy and use a positive threshold so different copies do not enlarge the original neighborhood counts. Define

```math
\widetilde r(x,a)=(r(x),\sigma(a)),\qquad
\widetilde o(x,a)=o(x),
```

where sigma is any copy transition. Every future observed value is still `o(r^n x)`, regardless of the copy or sigma. The original information counts are unchanged because each copy has the same comparison neighborhoods. Thus complete observations of this specified kind cannot determine hidden multiplicity or copy dynamics.

Source conditions capable of detecting the copies could rule out such extensions. A minimality requirement removes their unobservable distinction in the predictive quotient, but does not recover their microscopic existence from those observations. No claim is made that extra copies are a BFG physical law.

## 6. Count information must be transported, not recomputed from quotient cardinality

Because the observation family includes i_x, equivalent configurations have equal information, so the quotient information `i_bar([x])=i_x` is well defined. But this does not make it equal to the logarithm of a newly counted quotient neighborhood.

In the constant log(2) examples, the predictive quotient has one state, while its inherited information value is log(2). Counting its single point afresh would give log(1)=0 and lose the supplied source value. The source similarity class and the future-equivalence class are different objects; even the four-state example has one predictive class but original comparison classes of size two.

An information-preserving quotient must therefore retain that observable value, or appropriate source-supported multiplicity data, rather than silently reset the count law on the reduced labels. This is bookkeeping of already supplied information, not an invented physical conservation law. The quotient alone is not a derivation of its original class sizes.

## 7. Exact checks

`check_future.py` enumerates all comparison partitions and all total deterministic transitions on N=1,2,3,4 labels: **3,984 finite symbolic models**. Count equality is checked using integer class sizes, exactly equivalent to log-count equality at fixed log base. An independent pair-orbit cycle procedure checks every future-equivalence decision, giving **62,688 ordered state-pair comparisons**. The refinement result is checked for congruence, minimal separation and its finite stopping bound.

The delayed-information example, the two-/four-cycle ambiguity and all 27 copy maps on a three-copy version of the delayed model are also checked exactly. These are algebraic/symbolic consistency controls, not empirical data or certification that all enumerated models satisfy the complete BFG admissibility architecture.

## 8. Completed conclusion

We can now construct the unique minimal model of the **given observable behavior** and its exact information-preserving quotient. We also have an all-time counterexample and replication theorem showing why balance/count histories alone cannot recover every underlying configuration, transition or geometry.

The remaining source question is therefore not another missing matrix rearrangement: which already defined canonical observables are available at the origin, and what source premise fixes their values and transition grammar? The September full canonical stream is richer than our two-observable test, but its evaluation presupposes the frozen state/update data whose origin has been under investigation. It cannot be used as independent evidence for those same missing data without a source implication.

The result distinguishes operational uniqueness from microscopic uniqueness and narrows the latter's proof obligation. It does not establish that the BFG is inconsistent, that no richer source construction works, or that extra initial data are forbidden in a deterministic theory. No new paper, physical law or finite event rule is introduced.

Source anchors are in [SOURCES.json](SOURCES.json). Reproduce with `python future_identifiability/check_future.py`; exact results and worked quotient data appear in [results.json](results.json). The BFG-Engine's global module context remains in the [plugin synthesis](../plugin_synthesis/README.md).
