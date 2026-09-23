from dataclasses import dataclass
import numpy as np
from .types import NumericalPolicy
from .seeds import make_random_seed_state
from .simulate import simulate

@dataclass
class SearchHit:
    score: float
    seed: int
    run: object

def run_score(run):
    score=0.0
    for s in run.steps:
        if s.success: score += 2.0
        if s.spectral_novelty: score += 1.5
        if s.formation_gap is not None and np.isfinite(s.formation_gap):
            score += min(1.0,max(0.0,s.formation_gap))
        gain=float(s.diagnostics.get("crossfed_gain",1.0))
        score -= max(0.0,gain-1.0)*5.0
    if run.states and not run.states[-1].terminal: score += 2.0
    return float(score)

def inverse_design(trials, dim, persistent_rank, steps, carrier, policy=None, seed=1, top_k=5):
    policy=policy or NumericalPolicy()
    rng=np.random.default_rng(seed)
    hits=[]
    for _ in range(int(trials)):
        s=int(rng.integers(0,2**31-1))
        initial=make_random_seed_state(dim,persistent_rank,s)
        run=simulate(initial,carrier,steps,policy)
        hits.append(SearchHit(run_score(run),s,run))
    hits.sort(key=lambda h:h.score,reverse=True)
    return hits[:int(top_k)]
