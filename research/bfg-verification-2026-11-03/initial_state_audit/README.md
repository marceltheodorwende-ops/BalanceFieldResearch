# Initial data, complete finite state and initialization history

3 November 2026. Follow-up in the existing verification stage. No new paper, fundamental law or initial-state axiom is introduced.

## Finding

**For the specified November finite event, the complete five-tuple already includes Y0. No additional initial L or neutral metric M must be supplied to compute the next exact event once that five-tuple and its carrier conventions are given.** Unknown reconstruction of Y0 from a smaller primitive source packet is a separate initialization question, not nondeterminism of the defined event.

The original 26 September minimal-finite preprint explicitly lists `(K,rhoF,rhoW,Y,P)` in Section 3 (paragraphs 68-82 of the recorded DOCX extraction); it treats Y as its own role. The November paper Section 12 does likewise, allowing positive semidefinite Y at the general typed input before gates. The richer master-state contract also stores Y explicitly. This is source-explicit state specification, not a new input invented by this audit.

## 1. Original data are not one undifferentiated premise set

| Layer | Supplied data | Derived after the specified premises | Remaining question |
|---|---|---|---|
| Primitive formation sector | Finite real carrier, inner product, capacity triple (D,c,aleph), quartic formation functional | K=c+aleph-D; its simple negative formed branch and positive local Hessian H | A particular source-neutral joint assessment is not fixed by H alone in the audited quadratic class |
| Neutral-completion sector | A specified channel and carrier metrics, with the stated two-piece quadratic assessment | Resolvent and Gram of that same assessment | Why a particular channel/assessment must be selected from the primitive packet is a distinct source implication |
| Rich finite master state | Carrier, three capacities, rhoF, rhoW, Y and R_C | K and the appropriate persistent projector, plus the stipulated finite successor | Full rich-state role reconstruction is not the same as computing the reduced event |
| November finite kernel | K, rhoF, rhoW, Y and ordinary orthogonal P on a common finite carrier | Selection, loads, weights, analysis, active Gram, transported K/densities, seed or terminal | No further L/M input is called by this event; existence of a unique primitive initializer is not thereby proved |

These layers have different contracts. Calling the capacity triple the complete input of the five-tuple program would omit several explicitly stored state variables. Conversely, calling the five-tuple a lossless reconstruction of the whole primitive/rich theory would assert more than the paper does.

## 2. Exact finite input contract

The carrier is C^n (or its specified real restriction), n>=1, with a common fixed Hilbert inner product and adjoints. The matrices share this carrier:

- K=K*: formation geometry.
- rhoF>=0: formation/load density; a successful branch requires nonzero selected formation through its load gates.
- rhoW>=0, tr(rhoW)=1: inherited witness.
- Y>=0: neutral load at the typed input; successful outputs satisfy 0<Y+<I.
- P=P*=P^2: ordinary persistent projector.

The common carrier, metric and typing are part of the mathematical contract, even when implicit in array dimensions and standard conjugate transpose. They must not be confused with an extra state-dependent coupling parameter. An input can be typed and still terminate at a prescribed admission gate. The helper event() does not itself validate every mathematical type condition before execution.

The proposed L0-NC source initializer remains a proposed way to obtain one tangent channel. It is not needed as an extra argument to this finite event and is not silently adopted here.

## 3. Sufficiency theorem and what 'same initial state' means

**Proposition D1 (operational sufficiency of the supplied five-tuple).** Fix the exact Section 12 rules, including the selector boundary, ambient domain, polar kernel conventions and seed/terminal policy. Given a typed five-tuple, its next output is a unique simultaneous-unitary class or the prescribed absorbing terminal. No unspecified L or M remains in this next-event calculation.

**Proof.** Y fixes its neutral pair, graph metric and selector. Q and P fix the specified polar selection and selected support; density transport and normalization follow unless a gate terminates. The positive selected loads fix the reciprocal weights. These and the chosen ambient channel stacking fix A. Reduced SVD fixes its active singular spectrum and joint transported output up to a common active-frame unitary; repeated singular values rotate all outputs together. A simple negative ground mode fixes the phase-free seed projector and magnitude; non-simple or failed gates take the prescribed terminal branch. These are precisely the typed uniqueness steps of Theorem 13.1. H,L,M do not appear as additional arguments. QED.

**Corollary D2 (initializer-fiber equivalence for this event).** Any two interface representations that produce the same Y0 and the same other four matrices in a common frame produce the same complete finite input, hence the same future quotient orbit under the fixed event. Induct on D1 and unitary covariance. This is deterministic factorization through the stored state, not a claim that all physical mediation mechanisms with the same Y are empirically identical.

The new controls compare H=2I, L1=I/2, M1=2I with L2=I, M2=8I. They give the same Y=I/4 and are genuinely the same assessment under neutral-coordinate scaling T=2I. Three fresh event calls agree. This is an expected coordinate-equivalence control, not evidence that inequivalent response spectra can be normalized away.

Different initial couplings that produce different Y do **not** give the same complete five-tuple. Earlier examples of different outcomes therefore demonstrate initialization dependence, not multiple outputs from a fixed complete input. For example, holding the other four scalar matrices fixed and changing Y from 1/2 to 1/4 changes the next load from 8/45 to 32/425. It follows that omitting Y loses operational information in this model. It does not follow that an extra L must be added on top of Y.

## 4. Why this is not a lossless reconstruction of the richer state

Distinct capacity triples can have the same K: with c=0, (aleph,D)=(1,2) and (2,3) both give K=-1. Distinct power-bounded recursion operators such as diag(1,1/2) and diag(1,1/4) have the same persistent projector diag(1,0). Therefore storing K and P does not recover all rich-state components. This noninjectivity is compatible with operational sufficiency for a reduced event whose formulas use only K and P at those roles. No complete equivalence of every richer BFG implementation with this reduced program is asserted.

Similarly, the primitive neutral channel may have additional outputs or carrier attributes that are absent from the finite kernel. Predictions of those extra observables would require their own state/measurement contract. The five-tuple sufficiency theorem concerns the model's declared outputs.

## 5. Mathematical completeness versus numerical configuration

The preserved audit helper accepts `event(state,tol=1e-10)`. Floating cutoffs, linear algebra and precision are implementation settings, not fundamental physical inputs. A concrete control at scalar Y=10^-6 has exact Lambda_B=Y^2/(1+Y)>0 and a positive successor under the mathematical event. The helper labels it a load stop at its default tolerance but succeeds with tol=10^-14. Thus the helper's stop string is not by itself proof of exact terminality.

This does not refute D1, whose gates use exact zero, and it does not establish physical nondeterminism. It identifies a limitation already recognized in the paper's exact-versus-floating distinction. The check is of this preserved audit helper, not every production program in the repository. No implementation was altered by this follow-up. A future numerical-contract improvement should distinguish uncertain small loads from proved zero rather than changing the mathematical law.

## 6. Disposition

| Question | Result |
|---|---|
| Does the current finite state already include the effective coupling information needed for its event? | Yes, in Y together with the other supplied coordinates. |
| Must the program receive L and M separately once Y is supplied? | No, not for the declared finite outputs. |
| Is the exact next event unique for a complete typed state and fixed rules? | Yes, up to simultaneous-unitary output coordinates or its prescribed terminal. |
| Do varying initial Y values contradict that uniqueness? | No; these are different complete initial states. |
| Does this derive a unique Y0 and all other state coordinates from the earliest capacity triple? | No. Initial-state reconstruction is an additional claim not proved by state sufficiency. |
| Can the current helper's tolerance-induced stop be read as exact physical termination? | No. Numerical policy must be distinguished from the exact event. |

The next useful work is to state whether the intended scientific claim is evolution **from supplied finite initial data** or the stronger reconstruction of those data from the primitive formation sector. The first is already mathematically specified; the second retains the narrow source-initialization obligations recorded in the foundation audit. No amendment is adopted to make those two claims artificially identical.

## Verification and sources

Run `python initial_state_audit/check_initial_state.py` from the verification-stage folder with its existing scientific Python environment. [Results](results.json) record exact interface identities, differing incomplete-input successors, fresh program calls and the numerical-policy control. General all-iterate sufficiency follows from the written induction, not from three simulated steps. No proof-assistant or empirical claim is made.

Pinned repository sources and the original September source-extraction identifier are in [SOURCES.json](SOURCES.json). The published PDF and preserved event helper are unchanged.
