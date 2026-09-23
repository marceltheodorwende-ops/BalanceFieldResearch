# BFG Stratum Transition Geometry

**No held-out target is opened.**

The finite runtime now records four separate bifurcation families:

1. formation-sign surface;
2. formation-simplicity surface;
3. persistent-runtime-rank surface;
4. active-runtime-rank surface.

The two rank surfaces are operational runtime surfaces. Exact algebraic rank and exact unit-circle persistence remain non-open under arbitrary ambient perturbations.

States audited: `40`

States whose nearest active-rank transition is upward activation: `40/40`

States whose nearest persistent-rank transition is loss of persistence: `40/40`

| Carrier | Formation eligible | Persistent rank | Active rank | Median formation margin | Median persistent runtime radius | Median active runtime radius |
|---|---:|---|---|---:|---:|---:|
| annual-sunspots | 2/2 | [4] | [4] | 0.863174 | 1e-08 | 2.38362e-10 |
| mauna-loa-co2 | 2/2 | [4] | [4] | 0.823529 | 1e-08 | 1.88394e-10 |
| enso-pacific-sst | 2/2 | [4] | [4] | 0.734548 | 1e-08 | 1.13037e-10 |
| zachary-karate-network | 13/34 | [4] | [4] | 0.0967446 | 1e-08 | 2.05873e-10 |

## Interpretation

The active-rank runtime surface is currently extremely close in packet operator norm because the latent singular values sit near zero while the declared rank threshold is around `1e-10`.

This is a numerical/runtime geometry fact, not evidence for a physical critical scale.

The next integration step is to transport the persistent- and active-rank radii into the parent product norm so all four surfaces can be compared inside one common continuity corridor.
