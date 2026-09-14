# BalanceFieldResearch

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
