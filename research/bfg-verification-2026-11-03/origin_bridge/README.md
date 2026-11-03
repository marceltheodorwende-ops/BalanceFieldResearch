# Original identity and persistence premises: origin-to-operator audit

Date: 3 November 2026. Continuation of the existing BFG verification stage, in English. No new paper, physical law, initialization axiom or event implementation is introduced.

## Finding

The reviewed origin corpus already contains primitive identity and persistence. In particular, the June origin manuscript, paragraphs 107–108, places primitive persistence and primitive identity before difference potential, neutral holdability and information. It would therefore be inaccurate to say that BFG has no original identity premise, or to demand that its primitive identity be created from a later formation minimum.

What is **not established by this review** is a unique representation bridge from those primitives to the finite initial operators `rho_W,0` and `P_0`, tied specifically to the simple ground line of the later quartic formation problem. A conceptual primitive, a criterion for admissible persistence, a supplied recursion operator and a theorem identifying a unique operator are distinct logical ingredients. The missing implication is now more precise; no universal absence theorem over all BFG documents is claimed.

The preceding [formation audit](../formation_initialization/README.md) remains valid: for a freshly minimized profile under the existing quartic law, a simple negative ground eigenvalue gives `rho_F,0=(-lambda_0)Pi_0`. It does not itself generate the earlier logical prerequisites.

## 1. Source trace

The local extracted corpus was searched for identity, persistence, initial/origin conditions, recursion and their German equivalents. The following relevant passages were then inspected directly. [SOURCES.json](SOURCES.json) pins extraction hashes, line/paragraph anchors and repository versions. Extractions can omit equation layout, and this targeted review does not certify every theorem in every source.

| Source | Relevant existing content | Consequence for this question |
| --- | --- | --- |
| March 14, 2025 universal BFG, Section 3 | Scalar order ratio built from supplied energetic, informational and structural quantities | Does not, in the inspected passage, specify a finite origin witness or recursion spectrum |
| April 17 and 18, 2025 formulations | Order, feedback, equilibrium and structure; April 18 Sections 1–2 give the ratio and balance interpretation | These roles must be preserved, but a scalar balance condition is not an operator identification theorem |
| June 29, 2025 English BFG, Sections 9.1–9.3 | Semantic memory field, semantic persistence condition and recursive identity criterion | Criteria for continuity of a supplied field, rather than a construction of the later normalized witness from a quartic ground line |
| May 16, 2026 recursive conjugate extension, Sections 2 and 5 | `R_C=MRM*`, `M=sqrt(N)`; bounded near-critical recursion | Supplies the operator grammar; the product alone does not impose a unique persistent space or norm preservation |
| May 21, 2026 compact stability, Sections 8–10 | Same conjugate form; identity as persistent recursive trajectory continuity | Credits the existing identity role; still needs particular operator constraints and a representation map |
| June 1, 2026 structured Level-0, Theorem 8.3, Section 9 and Section 23 | Invariant retention and recurrence are hypotheses; proto-modes must retain identity; recursive closure requires boundedness | These conditions restrict admissible candidates, rather than proving the first candidate is uniquely generated |
| June 2026 origin architecture, paragraphs 101–108 | Primitive persistence and identity precede difference and information | Corrects any suggestion that identity is entirely absent upstream; no equality with the finite ground projector is stated there |
| Same origin source, paragraphs 171–179 and 715–724 | Conjugate recursion and explicit boundedness/invariant-subspace requirements | Recognizes that the encoded state must lie in a suitable invariant sector; does not automatically solve that requirement |
| September two-density state, Sections 5–8 and 10 | Inherited witness transport; no fabricated inherited identity in seed sectors; seed promotion and recursive rebuild are declared completions | Solves continuation conditionally, with origin still outside the inherited-witness gate unless an origin rule is specified |

This audit checks the relevant implication, not empirical claims about cognition or nature in those manuscripts. Terminology is not silently identified across dates: primitive `P_0` and `I_0` in the June origin chain are **not** automatically the November persistent projector P or an identity matrix. Likewise early information reference `I_0` is a different role.

## 2. What conjugate recursion does and does not force

Assume N is positive definite, M=sqrt(N), and `R_C=MRM*`. Norm preservation would require

```math
R_C^*R_C=I
\iff R^* N R=N^{-1}.
```

This follows by multiplying `M R* N R M=I` on both sides by M inverse. Positive N alone does not provide the identity. More generally `||R_C|| <= ||N|| ||R||` is an upper bound, not a persistence theorem.

For the same `N=I/2`, `K=diag(-2,1)`, formed profile `d=sqrt(2)e_1` and density `2 Pi_0`, consider these exact diagnostic witnesses:

| Raw R | R_C | Outcome |
| --- | --- | --- |
| I | I/2 | Power bounded, every profile decays, no peripheral space |
| diag(2,1) | diag(1,1/2) | Formed line fixed, one persistent direction |
| 2I | I | Formed line fixed, two persistent directions |
| diag(4,1) | diag(2,1/2) | Unbounded powers |

They are comparison operators, not new BFG laws or replacements for a prescribed raw R. The middle pair both satisfy exact spectral radius one, power boundedness and preservation of the same formed profile, yet give distinct P. If a stronger source premise excludes a row, it must be applied explicitly. The first and last rows disprove automatic persistence/boundedness from the product grammar alone; they are not countermodels to a source that independently assumes bounded critical persistence.

Similarly, spectral radius exactly one does not alone imply power boundedness: the Jordan block `[[1,1],[0,1]]` has powers `[[1,n],[0,1]]`. A radius merely close to one also permits decay or growth. The later repaired peripheral-space assumptions are substantive and are preserved here.

## 3. A stronger conditional witness theorem

**Theorem.** On a finite Hilbert space, let Pi be a rank-one orthogonal projector, Q=I-Pi, and

```math
R=\Pi+T,\qquad T=QTQ,\qquad\|T\|<1.
```

If a positive trace-one witness W is stationary under the **unnormalized** operator transport,

```math
RWR^*=W,
```

then W=Pi.

**Proof.** Orthogonal blocks give `R^n=Pi+T^n`, hence `R^n -> Pi` in norm. Stationarity iterates to `W=R^n W(R*)^n`. Taking the limit gives `W=Pi W Pi`. Rank one and trace one imply W=Pi. This proves the statement in every finite dimension, not just the checked two-dimensional fixtures.

This replaces an explicit support hypothesis with two precise dynamical premises: a unique protected line with a strictly stable complement, and unnormalized witness stationarity. It is a consequence *if* existing BFG primitives are represented by those conditions; this audit does not adopt that identification. The existing neutral transverse rebuild supplies the requisite block structure **once P=Pi and Y>0 have already been supplied**. It cannot be used circularly to derive that same initial P.

For a protected sector of rank greater than one, the same proof only gives `W=PWP`. Many trace-one positive operators then remain. Thus persistence plus stationarity is not sufficient without the one-dimensional conclusion.

**Normalization caveat.** Fixed points of

```math
W\longmapsto RWR^*/\operatorname{tr}(RWR^*)
```

are insufficient. For `R=diag(1,1/2)`, `W=diag(0,1)` is fixed by that normalized map even though its unnormalized mass decays as `4^(-n)`. Renormalization can conceal loss of the physical/structural quantity being monitored. No interpretation of W as a measured physical density is assumed here.

**Phase caveat.** Rank-one density stationarity `R Pi R*=Pi` implies `Re=exp(i theta)e` for a unit generator e, not necessarily Re=e. A projector removes global phase. The existing finite rebuild fixes phase by its explicit identity block; that convention must not be attributed to density stationarity alone.

## 4. Why inherited continuation cannot silently initialize an origin

The two-density source defines `T=polar(overlap)`, retained mass `m=tr(T* T W)`, and returns terminal when m=0. With zero inherited support, T=0 and m=0. The formula `TWT*/m` cannot produce a normalized origin witness. Later seed promotion does not bypass the already failed gate.

This is a limitation of the **domain of an inherited continuation**, not a contradiction in primitive identity. An origin may have primitive identity without an ancestor; representing that origin requires its own source-supported boundary identification. Setting the origin witness equal to the normalized fresh formation is a mathematically consistent candidate under the previous rank-one lemma, but necessity has not been established. It is not adopted here. Nor may the same assignment be used indiscriminately after later seed formation, where it would fabricate inherited identity on a new sector.

The earlier persistence-inclusion theorem is also credited: conditional on a persistent sector, a witness supported there and positive reciprocal loads, the preselection cross-fed active support contains that sector. This protects a supplied witness at that step; it does not select its origin. The later exact selection stage has its own stated conditions.

## 5. Result and next obligation

| Question | Result |
| --- | --- |
| Are primitive identity and persistence already present? | Yes, explicitly in the reviewed origin lineage |
| Is the fresh formation density derived? | Yes, conditional on the existing quartic minimum/density identification and simple negative ground |
| Does `MRM*` alone force a unique persistent origin? | No, exact witnesses distinguish the stated weaker conditions |
| Can the normalized witness be uniquely proved? | Yes under the rank-one protected-sector and unnormalized stationarity premises; their origin identification remains to be justified |
| Does inherited R4 bootstrap an origin without inheritance? | No; its zero-mass branch is terminal |
| Has the full original BFG corpus been proved inconsistent or incomplete? | No; this is a bounded implication audit |

The next obligation is a **representation theorem**, not the invention of identity from nothing: find an original premise that maps primitive persistence/identity into (i) the unique formed ground line as the entire protected sector and (ii) a trace-one stationary witness on that sector. If the corpus provides only admissibility roles without this map, the initializer is conditional rather than uniquely derived. Y's initial interface remains a separate issue.

Reproduce exact diagnostics with `python origin_bridge/check_origin.py`. [results.json](results.json) records what was checked. These controls and the analytic theorem establish no empirical validation and no full-corpus independence theorem. The original PDF and event helper are unchanged.
