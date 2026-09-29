# Full finite successor execution and natural-emergence evidence audit

29 September 2026. This is a result for the [universal BFG reclosure and emergence preprint](BFG_Universal_Reclosure_and_Emergence_Preprint_2026-09-29.pdf), not an unconditional emergence proof.

## 1. Which map was actually executed

The repository's living [fundamental-closure candidate](../../research/fundamental-closure-2026-09-25/package/bfg_lab/fundamental_closure.py) contains `bfg_universal_state_update`, which applies the selection-first finite update to the full typed `UniversalOperatorState`: distinction, coherence and emergent capacities; separate formation and identity-witness densities; neutral load; and recursive transport. This is the **conditional finite candidate** that uses three explicitly declared BFG completion laws (intrinsic Gram successor load, neutral-contrast selection and neutral transverse recursion). The [package status](../../research/fundamental-closure-2026-09-25/package/README.md) does not say these laws were uniquely forced by the historical Level-0 corpus.

Using its own `repeated_rank_growth_fixture`, I executed four consecutive complete state updates with `tol=1e-12` and `boundary_tol=1e-10` (Python 3.12.14, NumPy 2.3.5). The fixture is mathematical and synthetic; none of its state coordinates was estimated from a natural carrier.

| Update | Result | Persistent rank after reclosure | Carrier dimension | Witness trace | Formation ground eigenvalue | Minimum neutral-load eigenvalue |
| ---: | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | nonterminal | 3 | 4 | 1.000000 | −0.8 | 0.0028649526 |
| 2 | nonterminal | 4 | 4 | 1.000000 | −0.8 | 0.0000794040 |
| 3 | nonterminal | 4 | 4 | 1.000000 | −0.8 | 0.0001352507 |
| 4 | nonterminal | 4 | 4 | 1.000000 | −0.8 | 0.0000001026 |

The first two steps grow persistence *inside* the same four-dimensional carrier. This verifies executable state transitions for this fixture. It does not show that each step has an irreducible higher relation. The prior [10,000-case audit](NUMERICAL_AUDIT_10000_README.md) checks finite algebra and the separately specified Schur novelty stratum; that audit was not an execution of this entire update map.

Reproduce from `research/fundamental-closure-2026-09-25/package`:

```sh
PYTHONPATH=. python3 - <<'PY'
import numpy as np
from bfg_lab.fundamental_closure import repeated_rank_growth_fixture, bfg_universal_state_update
s = repeated_rank_growth_fixture()
for i in range(4):
    out = bfg_universal_state_update(s, tol=1e-12, boundary_tol=1e-10)
    assert not out.terminal, out.reason
    s = out.state
    print(i+1, out.diagnostics['persistent_rank_after_reclosure'], s.dim,
          np.trace(s.witness).real, np.linalg.eigvalsh(s.formation()).min(),
          np.linalg.eigvalsh(s.Y).min())
PY
```

The packaged `pytest` regression suite was not run in this environment because `pytest` is not installed (`No module named pytest`). The direct execution above did run successfully. No package dependency or model law was changed to make a test pass.

## 2. Natural-system evidence versus the preprint's emergence criterion

The repository has natural-carrier *readiness* mappings for annual sunspots, Mauna Loa CO2 and ENSO SST. Its [portfolio status](../../research/emergence-studio-2026-09-23-r4/BFG_Emergence_Studio/validation/PORTFOLIO_STATUS.md) labels all three `READY_FOR_VALIDATION`, with the current held-out target unevaluated. These carrier implementations call the Studio `canonical_reclosure` on mapped observations; they do **not** feed independently measured full states into the above `bfg_universal_state_update`. Equating those two executions would change the claim under test.

The older, archived [sunspot blind result](../../research/emergence-studio-2026-09-23-r4/BFG_Emergence_Studio/validation/audit/sunspots/confirmatory_archive/SUNSPOT_EMPIRICAL_RESULT.md) is explicitly **FAIL** under its frozen primary rule: RMSE improvement against the matched adaptive null was 0.658%, below the required 1%; AR(12) performed better. The subsequent sunspot readiness mapping treats the already opened period as development data. Neither result supplies the paper's mediator-specific removal/restoration evidence.

| Required by the new paper's strong emergence criterion | Natural-carrier status in this repository |
| --- | --- |
| Full finite-state carrier map and complete successor executed on natural measurements | No such bridge was found for these three natural carrier snapshots. |
| Independently measured source closures and higher state | Not established by the stored forecast readiness scores alone. |
| Selective **generative** removal of the proposed relation with source continuity retained | No natural removal arm is recorded. |
| Restoration at fixed parameters | No natural restoration arm is recorded. |
| Fixed mechanistically distinct rivals under matched observations and interventions | Forecast baselines exist, but the required removal/intervention signatures and specific-mediator discrimination are not recorded. |

**Verdict:** The full conditional finite successor can be executed on a synthetic mathematical state. Irreducible emergence in a natural system is **not proved or presently decidable from these files**. Running more algebraic Monte Carlo cases or deleting a variable in a fitted observational model would not replace a physical or otherwise independently identified generative intervention. A natural-carrier study needs a prospectively fixed full-state measurement map, an independently measured higher channel, selective relation manipulation and restoration with surviving sources, and matched mechanistically different rivals. Negative outcomes must remain reportable.
