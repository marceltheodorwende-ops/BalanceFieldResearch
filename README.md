# BalanceFieldResearch

The [G1 compatibility audit](research/gram-compatibility-2026-09-18/README.md)
derives G1 under explicit intertwining conditions and gives a gate-admitted
counterexample to unrestricted compatibility with B_C = D_cov c.
G1 remains a restricted proposal, not a general internal BFG theorem.

The [G1 Gram inheritance proposal](research/gram-inheritance-proposal-2026-09-18/README.md)
uniquely fixes the next load under an explicit additional postulate.
It is not derived from existing BFG axioms and imposes a nonincreasing load-norm bound.

A [fully worked local reconstruction witness](research/reconstruction-witness-2026-09-18/README.md)
shows that the same split, polar transport and successful gate permit different
positive Gram rebuilds unless the reconstruction functions are additionally specified.

The [internal closure derivations](research/internal-closure-2026-09-18/README.md)
add a tested Gram rebuild for supplied factors and conditional mathematical results.
The seven universal realization problems are not claimed fully solved.

The [prediction audit and seven open realization problems](research/prediction-audit-2026-09-18/README.md)
separate possible empirical tests from unresolved universal reconstruction.
The galaxy branch overlaps a standard MOND interpolation; no BFG confirmation is claimed.

The [conditioning repair](research/conditioned-search-2026-09-16/README.md)
resolves the four remaining complete-graph cases with the optional
`fit_rcond=1e-8` setting and unchanged exact certification.

The [interior candidate stage](research/interior-search-2026-09-16/README.md)
certifies four additional network histories; four complete-graph cases remain
unresolved. Numerical proposals still require exact rational certificates.

The [new network evaluation](research/network-transfer-2026-09-16/README.md)
records 20 additional cases: eight remain unresolved, and the extended search
does not improve on the original assessor in this run.

The [exact two-node stage](research/exact-pair-2026-09-16/README.md) resolves the
last two cases in the existing 39-case catalogue. Its own subfolder preserves
the protocol, proof, audit and results alongside earlier stages.

The [audited boundary extension](docs/BOUNDARY_FINDINGS.md) reduces unresolved
cases from 23 to 2 in the same 39-case catalogue. See its
[method](docs/BOUNDARY_METHOD.md) and [BFG audit](docs/BOUNDARY_AUDIT.md).

The [39-case comparison](docs/CERTIFIED_COMPARISON.md) resolves 12 of 35 formerly
open regression cases at a fixed 255-box budget and diagnoses the remaining cases.

The [bounded family search](docs/CERTIFIED_SEARCH.md) now subdivides uncertain
weights and initial states to resolve additional open cases with certificates.
Run `python -m bfg_lab.certified_search --input examples/certified_search.json`.

The [reference-family repair](docs/CERTIFIED_FAMILY.md) now provides exact-rational
certificates for a common witness or exclusion of a declared healthy weight box,
and explicitly returns `unresolved` otherwise. Run
`python -m bfg_lab.certified --input examples/certified_family.json`.

**BFG Unified V4: reproducible mathematics and network experiments.**

Research by Marcel Theodor Wende. This repository starts a new development line
from *The BFG Compact Canonical Universal Reclosure Equation â€” Freedom-Closed
Unified V4*, dated 12 September 2026.

## Authoritative source collection

The project uses exactly [five owner-supplied BFG documents](papers/README.md):
Structural Strong Form V2 (DOCX), the three Reclosure papers of 7–8 September,
and Compact Unified V4 (PDF). Original files are preserved byte-for-byte.

**Correction: no standalone Freedom-Closed Unified V3 exists.**
Read the [V3 erratum](docs/ERRATUM_V3.md) before interpreting V4's predecessor claims.
See the [source completeness audit](docs/SOURCE_AUDIT.md) for what these five files
establish and what remains unspecified.

## Current status

This is an initial finite-dimensional reference laboratory, not an empirical
validation of BFG and not a complete implementation of the universal map U.

Implemented: exact neutral responses C and B, contrast Z, metric projection,
reciprocal branch weighting, compact/expanded split comparison and polar support
transport. The demonstration measures these structures on synthetic networks.

**Open mathematical issue:** Eq. 27's span definition does not in general equal
the peripheral eigenspace. The implementation explicitly uses the latter, for
normal power-bounded transport matrices only. [Details and counterexample](docs/MATHEMATICAL_STATUS.md).

## Run locally

Python 3.11+ and NumPy are required. From the repository root:

```sh
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python -m bfg_lab --output results
```

Open `results/network.html` in a browser. It works offline, with scenario and
measurement selectors. `results/network.json` contains all numerical data.

The eight-node demonstration compares an impulse, an edge failure at step 20,
and progressively weakening coupling. Its evolution is a declared consensus toy
model; BFG quantities are readouts, not its governing universal law.

## Research plan

1. Audit the paper's definitions and reproduce its algebraic building blocks.
2. Specify the complete state and upstream Gram reconstruction functions, which V2 sections 23–24 explicitly leave as research tasks.
3. Capacity transport and the formation gate are implemented. Complete universal
   reclosure still requires the missing definitions and independent checking.
4. Freeze one network benchmark, its measurement mapping and comparison models.
5. Test held-out predictive value before making application or natural-realization claims.

See [the research protocol](docs/RESEARCH_PLAN.md),
[claim register](docs/CLAIMS.md), and [verification record](docs/VERIFICATION.md).

## Repository reset

The previous main contents are preserved at
[`archive/pre-unified-v4-2026-09-13`](https://github.com/marceltheodorwende-ops/BalanceFieldResearch/tree/archive/pre-unified-v4-2026-09-13).
The new main tree replaces the previous files. Commit history is retained for
traceability. Old preregistrations are historical records, not this lab's protocol.

## Rights

The original paper retains its existing authorship and rights. This reset does
not assign a new license to the paper or grant new reuse rights. Licensing for
the new implementation has not yet been designated by the repository owner.

## Candidate formation milestone

Capacity transport and the candidate formation gate are implemented in `bfg_lab.formation`. Run `python -m bfg_lab.formation` for admitted/rejected examples. The API `prepare_candidate(y, d, r, difference, coherence, neutral)` returns diagnostics, not a complete next state. See the [proposed persistence correction](docs/PERSISTENCE_PROPOSAL.md).

## Experimental multistep model

Run `python -m bfg_lab.minimal` for two reproducible multistep histories.
The [M1 specification](docs/MINIMAL_MODEL.md) defines every next-state variable
using explicit additional assumptions. Maintained capacity reaches the 12-step
budget; 20% depletion rejects the third candidate after two transitions.
This deliberately simple model is not the universal map; its diagonal example
reduces to a scalar state.

The alternative [M2 negative spectral transport](docs/MULTIMODE_MODEL.md)
preserves multiple negative formation directions. The same command also runs
its two-mode maintained/depleted examples. Both closure rules are explicitly
additional modeling assumptions; neither implements the full universal map.

## Paired comparison

`python -m bfg_lab.comparison` runs 72 paired synthetic simulations and saves
full JSON histories. The [comparison report](docs/COMPARISON.md) includes the
carried-transport baseline and negative findings: M2 has no advantage over that
baseline in the count of runs reaching the finite step budget.

## Independently specified diffusion reference

`python -m bfg_lab.diffusion` checks 72 cases against a transport derived from
an edge-flux law. The [findings](docs/DIFFUSION_FINDINGS.md) give a counterexample:
identical initial projected loads and dual gain do not identify diffusion recovery.
This is a bounded mathematical result, not an empirical validation of BFG.

## One early measurement

`python -m bfg_lab.early` tests a conditional recovery interval on 40 new
weighted graphs (80 state cases). The [derivation and findings](docs/EARLY_FINDINGS.md)
show how a measurement at step 5 bounds step 20 without feeding the graph or
future state to the predictor. This is a diffusion result, not BFG superiority.

## Robustness monitor prototype

`python -m bfg_lab.monitor` runs controlled fault scenarios. The [monitor guide](docs/MONITOR.md)
also explains how to supply JSON sensor samples. Partial observation blocks a
global forecast; full observation can flag some model violations, but can also
miss a connection failure. A conditional forecast is never a health certificate.

The [288-run detection catalogue](docs/DETECTION_FINDINGS.md) quantifies this
limit: all tested edge removals were missed, while 24/24 external inputs and
20/24 speedups were flagged with full observation. Two- and four-sensor runs
all abstain. Reproduce with `python -m bfg_lab.detection`.

The [known-reference monitor](docs/REFERENCE_FINDINGS.md) adds an exact reference
topology and full initial calibration. It detects 15/24, 20/24 and 21/24 edge
removals with 2, 4 and 8 ongoing sensors on the same catalogue. Reproduce with
`python -m bfg_lab.reference`. This improvement depends on additional information.

The [reference-error and excitation check](docs/REFERENCE_STRESS_FINDINGS.md)
tests 144 cases: a known impulse exposes some invisible cuts, but inaccurate
reference weights also cause alarms on intact networks. Reproduce with
`python -m bfg_lab.reference_stress`.
