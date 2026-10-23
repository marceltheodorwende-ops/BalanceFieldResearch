# Retained-data tie resolution and the equal-load four-charge sector

23 October 2026. BFG-only continuation under MANDATE.de.md.
[Preregistered protocol](LEX_SELECTOR_PROTOCOL.md). Source: unchanged pinned complete Dynamic Order, Parts I/II, full ambient update and unitary quotient. Standard spectral theory supplies the readout constructions. Priority order and rank-two target below are declared candidates, not source-selected physical laws.

## 1. A partial selector that never splits unresolved symmetry by hand

Work on the autonomous full-persistence extrema class C, now allowing degenerate Y:
P=I, F>0, 0<m<=M<=1/2, m>=2M², W>=0, tr W=1.
Use the following ordered refinement:
1. Spectral projectors Q of Y, in ascending eigenvalue order.
2. Within each Q, spectral projectors R of the compressed operator QFQ on ran Q, in ascending formation-eigenvalue order.
3. Within each remaining F-degenerate R, spectral projectors L of RWR on ran R, in ascending Witness-eigenvalue order.

No global commutation of Y,F,W is assumed. These are successive COMPRESSIONS, not a simultaneous diagonalization of noncommuting full operators.
Retain every final refinement block as a whole, even when its rank exceeds one. Define S2 to be the sum of initial ordered blocks only if their cumulative rank equals exactly two. If a block straddles the rank-two cut, the candidate is UNRESOLVED. An arbitrary eigensolver basis is not an additional selector.

The readout may define a rank-two S2 even if a whole rank-two block remains unresolved internally. Existence of S2 must therefore be distinguished from existence of two canonically ordered eigenlines or an independent transverse frame.

## 2. Covariance and exact persistence on C

Spectral projectors of compressed self-adjoint operators transform covariantly under simultaneous source unitaries. Thus the entire refinement and S2, where defined, are unitary covariant.
Every leaf lies inside a Y eigenspace, so [S2,Y]=0.

The C theorem gives g_alpha'(y)>0 on the current spectral interval. Therefore distinct Y eigenvalues retain their order and do not merge on C; equal eigenvalues remain equal. Every Y spectral projector is an aligned constant.
Because F and W are also aligned constants, every compressed F spectrum/projector and every subsequent compressed W spectrum/projector is constant.
Consequently:
- all refined blocks and their ordering are retained;
- resolved versus unresolved status is invariant on C;
- S2,+ = V† S2 V in the actual source successor coordinates.

No remembered projector or gap threshold is required by the exact rule. This statement does not extend across pre-C collisions, external drives, selection/seed events or changes of multiplicity stratum without further analysis.
The preceding eventual-entry theorem proves all positive-formation full-persistence trajectories reach C. It does NOT guarantee that this partial selector is resolved upon entry.

## 3. The earlier spectral-environment factor remains closed

Let S=S2 be defined. Since S commutes with Y and is retained, the existing pair-factor proof applies without requiring two distinct selected Y eigenvalues.
Retain
Zeta=(K_S,F_S,W_S,Y_S,mu_E),
mu_E(B)=tr[F(I-S) 1_B(Y)].
The measure is positive and records complementary formation weight, including multiplicities through their total weight; no arbitrary basis inside a degenerate eigenspace is needed.

The source loads are
L_C=tr[F_S(I+Y_S)^-1]+integral (1+y)^-1 dmu_E,
L_B=tr[F_S Y_S²(I+Y_S)^-1]+integral y²/(1+y) dmu_E.
They determine the SAME global alpha. Put
M_S=alpha(I+Y_S)^-2+(1-alpha)Y_S²(I+Y_S)^-2,
T_C,S=sqrt(alpha)(I+Y_S)^-1 M_S^-1/2,
T_B,S=sqrt(1-alpha)Y_S(I+Y_S)^-1 M_S^-1/2.
Then Y_S,+=M_S, K_S,+=sum_j T_j,S K_S T_j,S, F_S/W_S are retained, and mu_E,+=(g_alpha)_*mu_E.
All successor entries depend only on Zeta. Current-state reselection does not introduce hidden complementary data because the selected S has just been proved invariant.

This is closure of a declared mathematical projection on its resolved domain, not a proof of physical locality, minimality or a uniquely selected rank-two law.

## 4. Formation and Witness resolve genuine examples

For the earlier exact collision successor
Y=diag(50/209,386/1881,50/209),
F=diag(1,1,41762/20625), W=I/3,
the lowest Y line is original mode 2. In the tied higher block {1,3}, F selects mode 1 first. The ordered pair is therefore {2,1} (one-based). The next source event retains it.

For
Y=diag(1/5,1/4,1/4,3/10), F=I4,
W=diag(1,2,3,4)/10,
formation cannot split the middle Y block. Witness does, selecting {1,2}. The source again retains the selected subspace.
Thus the rule is not merely the previous simple-Y selector under a different name.

## 5. Unresolved states and discontinuity are retained

At Y=I3/4,F=I3,W=I3/3,K=I3 the full state is U(3)-symmetric. The procedure returns one unresolved rank-three block and no S2.
A globally covariant rank-two projector cannot be assigned there: invariance under every unitary would force it to be a scalar multiple of I3, and a scalar projector has rank zero or three.
This is consistent with, and does not weaken, the prior symmetric-state obstruction.

Even where the partial selector is resolved at a tie, it need not be continuous across nearby multiplicity strata.
Let
Y_e=diag(1/5,1/4-e,1/4+e), F=diag(1,2,1), W=I3/3.
These states are in C for the specified sufficiently small nonnegative e.
For e>0, the first two Y modes are {1,2}; for e=0, the F tie-break selects {1,3}.
The projector difference has squared Hilbert-Schmidt norm two, independent of how small positive e becomes.
Exact checks retain e=1/1000 and 1/100000. The discontinuity proof is for every sufficiently small e>0, not an extrapolation from those samples.

This rule is therefore a persistent partial selector on fixed strata, not a globally smooth physical event field. Other normalized/prioritized readouts can be proposed, but must declare their priority, covariance, closure and failure domain independently.

## 6. A constructive equal-load alternative with four invariant kernel coordinates

If the selected S lies entirely inside one Y eigenspace, then Y_S=yS.
Both restricted channel operators are scalar multiples of S:
T_j,S=t_j S, sum_j t_j²=1.
Hence K_S,+=K_S for EVERY local Hermitian K_S, including arbitrary couplings of the full K to the complementary subspace.
The fixed local linear-charge space now has real dimension four. This does not contradict the earlier two-charge theorem, which required DISTINCT selected Y eigenvalues; its damping factor becomes h=1 exactly at equal loads.

To obtain invariant relational coordinates, use two stable refined eigenlines (when available) for Z and an independent nonzero retained F or W offdiagonal for the transverse reference. This requirement is separate from merely having rank-two S.
A concrete nontrivial-global-dynamics example is:
Y=diag(1/5,1/5,3/10,3/10);
F has diagonal (1,2,3,4), F13=1/4, F24=i/5 and Hermitian conjugates;
W=I4/4 with W12=(1-2i)/40 and conjugate.
Exact positive leading principal minors establish F>0 and W>0. The selector takes modes {1,2}; their distinct compressed formation eigenvalues define Z, and W12 supplies the transverse axes.
The source alpha is exactly 76/1101. All selected K coordinates are constant because their Y loads agree, while cross-Y coherences can still be damped.

The prescribed full-source witness has all four input coordinates nonzero:
(1/2,-1/sqrt(5),-3/sqrt(5),3/2).
Their successor difference has norm <9e-16, while the full ambient kernel changes by about 0.01548 in Hilbert-Schmidt norm.
This is a sectorial, gauge-invariant four-component K conservation result FROM THE SAME SOURCE UPDATE, without inverse-history weighting.
It is not yet physical energy-momentum conservation: no Joule/momentum normalization, spatial translation, current through event boundaries, action or physical Lorentz dynamics has been derived. The local kernel is stationary here; conservation alone is not a propagation law. This equal-load equality is a domain condition, not a generic stability/robustness theorem.

## 7. Fresh evidence and numerical scope

Final lex_selector_audit.py run:
- 12 complex preparations in n=3,4,5,6, two complete source events each: 24. They include repeated Y eigenvalues, nondegenerate F resolutions and cases needing W.
- Four extra simultaneous-unitary full-source controls.
- Three source witness calls (collision successor, Witness fallback, equal-load charge example): 31 complete calls in the final run.
- Exact symbolic diagonal selection, positive-reference minors, equal-load identity and discontinuity examples.
- Largest projector residual <2e-13, pair-kernel residual <1e-14 and gauge-successor residual <3e-14. All meet the preregistered 1e-10 criterion.
- The pair test computes global alpha from selected data PLUS the complementary spectral weights, not from a substituted local alpha.

Numerical spectral grouping reproduces deliberately degenerate families in floating-point unitary representatives. Its tolerance is 1e-10 max(1,operator norm) and is NOT the exact mathematical degeneracy definition. Every resolved numerical test gap exceeded its grouping tolerance by more than 2.3 million; within-group spread was below 2.7e-5 of tolerance.
The initial audit passed. Explicit grouping-gap diagnostics were then added to record the already preregistered numerical separation criterion, followed by a fresh final run. No coefficients, source tolerances or witness inputs changed.
CI is recorded separately for the published code commit.

## 8. Next physical dependency

Advanced: current-state retained-data tie resolution, a closed pair factor beyond simple Y spectra, and an equal-load sector with four relational kernel coordinates conserved.
Remaining mathematical limits: unresolved symmetry, discontinuity at multiplicity changes, reference-chart zeros and selection/seed transitions.
Next substantive physical test: specify a BFG-internal event adjacency/spatial observable and check its actual transport and local continuity law. A selected internal subspace, four constant coordinates or a determinant cone alone cannot supply spatial displacement or an energy-momentum current. The Einstein step remains downstream of that missing bridge.
