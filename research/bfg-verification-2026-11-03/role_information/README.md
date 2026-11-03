# Which role information determines a state, and which determines its response?

This milestone traces the remaining role question after the [admissible quotient analysis](../admissible_quotient/README.md). It gives a complete finite diagnostic for a pure state relative to one Hermitian information operator, credits the conditional two-dimensional source branch where mean information already suffices, and separates that reconstruction from the still distinct neutral-response initializer.

The result concerns the precisely stated finite objects below, not a reduction of the full nine-role BFG field. Moment values are diagnostics, not newly prescribed laws or measurement requirements. No new paper, physical constraint or change to the finite event is introduced.

## 1. The role relations actually checked

| Source relation | What is fixed conditionally | Remaining input |
|---|---|---|
| Neutral Interface, section 7.1: I[s]=<s,I_op s> and feedback derivative | Information value given the state and operator; feedback given state/operator dynamics | A scalar value does not in general fix the joint state or the operator. The information operator is a separate primitive role. |
| Recursive Stability, sections 4 and 8: primitive operators and R=I_op F I_op | R given I_op and F; F=I_op^(-1) R I_op^(-1) if I_op is invertible and R is already known | This factor relation does not itself select a state s. |
| Recursive Stability, section 21: d_id(Id(s(t_0)),Id(s(t)))<=epsilon | Continuity relative to a supplied initial identity profile and trajectory | A continuity condition does not specify the initial identity value. |
| Neutral Interface, sections 13-14: semantic kernel and identity flow F(M,S_c,C,Phi,I,N) | Semantic/identity evolution when their functions, roles and initial data are supplied | A named kernel or evolution function is not its numerical specification. We do not assume that all such functions ignore the distinctions found earlier. |
| September 26 minimal source, sections 3 and 14 | Five typed finite-event roles; memory as branch information for unique continuation | Continuation data do not automatically constitute an origin selector. Present formation and inherited identity remain distinct. |
| Same source, section 15, paragraphs 307-311 | Conditional minimal complex polar carrier C^2 under its explicit branch requirements | This is a downstream conditional carrier result, not an unconditional claim that every BFG carrier is two-dimensional. |

The seven foundational BFG-Engine modules remain in the [global source context](../plugin_synthesis/README.md). These are targeted role checks; no fresh complete proof audit of all plugin pages is claimed. Original 2025 provenance is retained through the [earlier trace](../foundation_audit/SOURCE_LEDGER.md).

### Persistence is not an initial-value selector

For any identity-profile function Id and a valid distance, every constant trajectory s(t)=s_0 satisfies d_id(Id(s_0),Id(s(t)))=0. Different admissible s_0 can therefore satisfy the same continuity inequality. This statement remains true even if Id is injective: preserving an initially supplied value is different from fixing that value. An additional specified dynamical law or initial condition could select one, but cannot be inferred from continuity alone.

In the preceding comparison family, each trajectory is constant, with the same information I=2 and Phi=1. Its feedback derivative is zero for the entire trajectory. Observing these constant scalar values for longer does not distinguish the members. This is a result about that supplied diagnostic dynamics, not all possible BFG dynamics or readouts.

## 2. Complete pure-state diagnostic from information moments

Let J be a fixed finite-dimensional Hermitian operator with **r distinct known eigenvalues** lambda_a and spectral projectors Pi_a. Let s be a unit vector. Define

    p_a = ||Pi_a s||^2,
    m_k = <s,J^k s> = sum_a lambda_a^k p_a.

**Proposition M1.** The moments m_0,...,m_(r-1), with m_0=1, determine the joint unitary class of (J,s). Conversely this class determines those moments. This remains true when J has degenerate eigenspaces.

**Proof.** The r-by-r Vandermonde matrix V_(k,a)=lambda_a^k has determinant equal, up to the chosen eigenvalue ordering, to the product of all distinct eigenvalue differences. Thus it is invertible and p=V^(-1)m is unique. Within each eigenspace, unitary transformations act transitively on vectors of a fixed norm. Two vectors with the same p_a are therefore related by a block-unitary commuting with J, including arbitrary actions on blocks where both components vanish. Conversely simultaneous unitary coordinate changes preserve each moment. QED.

Among these consecutive power-moment measurements, fewer than r scalar equations have rank less than r. At an interior probability vector they leave a nonzero probability direction. Thus r-1 nontrivial moments, in addition to normalization, suffice in general and the truncated consecutive sequence is insufficient in general. This is not a claim that an arbitrary cleverly encoded scalar could not store more data, nor does it replace the separate simultaneous-Hermitian-tuple certificate from [joint canonical data](../joint_canonical_data/README.md).

### Exact resolution of the previous three-mode ambiguity

For J=diag(1,2,3), inversion gives

    p_1=(m_2-5m_1+6)/2,
    p_2=-m_2+4m_1-3,
    p_3=(m_2-3m_1+2)/2.

With mean information m_1=2 this becomes

    (p_1,p_2,p_3)=((m_2-4)/2, 5-m_2, (m_2-4)/2).

Nonnegative probabilities require 4<=m_2<=5. The previous theta family is recovered exactly by theta=(m_2-4)/2. Thus one additional number, the second information moment, resolves **that pure-state/J quotient ambiguity**. It is not a free parameter fitted here: no value of m_2 is prescribed or adopted as a BFG principle.

### Positive result for the conditional two-mode branch

When r=2, normalization and mean information alone give

    p_1=(lambda_2-m_1)/(lambda_2-lambda_1),
    p_2=(m_1-lambda_1)/(lambda_2-lambda_1).

So if the September source's conditional C^2 carrier applies, its source roles are validly identified with a fixed Hermitian J and a pure state, and its mean information is already known, there is no extra pure-state alignment ambiguity of the three-mode kind. For J=diag(1,2), m_1=3/2 fixes p_1=p_2=1/2. For r=1 the sole eigenspace is already one unit-vector orbit.

This credits a genuine route to closing the **state-class** part of the problem on that branch. The premises that fix the carrier, operator J, mean information and purity must still be justified; the three-dimensional comparison family was never a counterexample to a branch restricted to C^2.

## 3. Limits: mixed densities and the full finite state

The theorem concerns a pure vector and one operator. For a mixed positive trace-one density rho, the moments tr(rho J^k) determine only the spectral-block weights tr(rho Pi_a). They generally omit coherences and within-block structure.

For J=diag(1,2,3), take

    rho_a=I/3,
    rho_b=I/3 + (|e_1><e_2|+|e_2><e_1|)/12.

Both densities are strictly positive and trace one. Every power moment of J agrees because J^k is diagonal, but tr(rho_a^2)=1/3 while tr(rho_b^2)=25/72. Their spectra differ, so they are not jointly unitarily equivalent with J. The executable checks the first nine moments; the diagonal argument proves equality for **all** powers.

The finite BFG event contains positive densities that need not both be pure. Its source explicitly distinguishes formation from inherited identity. Therefore the pure-state moment theorem cannot be transferred to the complete five-tuple, to a general witness, or to all nine canonical field roles.

## 4. Even a fully known state class does not supply an unsourced response law

Hold the entire previous primitive tuple and a particular state fixed, not merely its mean information:

    J=diag(1,2,3), E_exp=J^(-1), B_bind=N=I,
    F=J^(-2), R=I,
    s=(sqrt(2)/4,sqrt(3)/2,sqrt(2)/4)^T.

All information moments and the joint state class are then fixed. In the already classified positive quadratic interface packet, with fixed H=diag(4,3,5), compare the two diagnostic loads

    Y_1=J/tr(J),     Y_2=(J/tr(J))^2.

Both admit a strictly positive quadratic completion with M=I and L=H^(-1/2) sqrt(Y_i). Their minimized assessments E_i=H^(1/2)(I+Y_i)^(-1)H^(1/2) differ:

    E_1=diag(24/7,9/4,10/3),
    E_2=diag(144/37,27/10,4).

The original primitive N remains fixed in this comparison. No identification N=C_N(Y) has been established or used. If an accepted source supplied that identification, or another exact joint assessment, these comparisons would have to satisfy it and could be excluded. The example tests exactly the weaker enumerated packet without that constitutive bridge; it is not a realization of every historical BFG equation or a proposed physical law.

The same separation already occurs in dimension two. Fix J=diag(1,2), the pure class with p_1=p_2=1/2 and H=diag(4,3). The two diagnostic loads J/3 and (J/3)^2 still give different positive effective assessments. Closing the C^2 pure-state ambiguity alone therefore does not close the upstream response law. The H blocks here are compatible with the earlier formed-Hessian examples; no unproved role bridge between their formed profiles and these primitive states is asserted.

## 5. Verification and present conclusion

The exact script checks 48 probability reconstructions for one through six distinct eigenvalues, the three-mode inverse formulas, an explicit unitary equivalence inside a degenerate eigenspace, the mixed-density limitation, and distinct quadratic responses with identical primitive state data in dimensions two and three. The written proofs establish the general finite statements; no empirical or formal proof-assistant certification is claimed.

The source search now separates three obligations:

1. **State identification:** given a fixed Hermitian information operator and pure-state branch, enough moments determine its class; the conditional two-mode case needs only normalization and mean information.
2. **Origin selection:** the moment values, initial identity and primitive operator inputs must themselves follow from accepted source relations or remain supplied data. Preservation and reconstruction are not selection principles.
3. **Response identification:** an actual source-to-neutral assessment or invariant response relation is still needed for E and Y, even if the state class is completely known.

No missing moment value or penalty is invented to close these obligations. The exact finite event remains defined and deterministic on its supplied input. The present work narrows which source implication must be established rather than declaring the full BFG framework impossible or complete.

Provenance: [SOURCES.json](SOURCES.json). Exact controls: [results.json](results.json). Reproduce:

```sh
python role_information/check_roles.py
python validate_stage.py
```
