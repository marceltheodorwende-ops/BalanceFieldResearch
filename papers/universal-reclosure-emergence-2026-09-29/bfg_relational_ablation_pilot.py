"""Exploratory BFG relational-ablation pilot; synthetic, not an empirical test.

Two persistent source channels share a driver. A measured mediator corrects their
relative state, while a separate reporter records the resulting joint pattern.
The same innovations and perturbations are used for all generative arms.

Run: python3 bfg_relational_ablation_pilot.py
"""

import json

import numpy as np


SEED = 20260929
N = 1000
T = 240
PERTURB_AT = 120
PERTURB_SIZE = 1.5
WINDOW = 30


def simulate(kind, u, e1, e2, ey, perturb):
    n, steps = u.shape
    x1 = np.zeros(n)
    x2 = np.zeros(n)
    m = np.zeros(n)
    y = np.ones(n)
    xs1 = np.zeros((n, steps))
    xs2 = np.zeros((n, steps))
    ms = np.zeros((n, steps))
    ys = np.zeros((n, steps))
    for t in range(steps):
        if perturb and t == PERTURB_AT:
            x1 = x1 + PERTURB_SIZE
        dx = x2 - x1
        if kind in ("full", "latent_clone"):
            correction = 0.35 * m
            m_next = 0.7 * m + 0.4 * dx / 2
        elif kind == "direct_dyad":
            correction = 0.15 * dx
            m_next = np.zeros(n)
        elif kind == "common_driver":
            correction = np.zeros(n)
            m_next = np.zeros(n)
        else:
            raise ValueError(kind)
        # The reporter is a separate dynamic variable. It reads the two source
        # states, never the mediator itself; this avoids witness overwrite.
        y_next = 0.8 * y + 0.2 * np.exp(-3 * (x1 - x2) ** 2) + ey[:, t]
        x1_next = 0.72 * x1 + 0.22 * u[:, t] + correction + e1[:, t]
        x2_next = 0.72 * x2 + 0.22 * u[:, t] - correction + e2[:, t]
        x1, x2, m, y = x1_next, x2_next, m_next, y_next
        xs1[:, t], xs2[:, t], ms[:, t], ys[:, t] = x1, x2, m, y
    return xs1, xs2, ms, ys


def fit_score(features, target, train_n):
    x_train = features[:train_n].reshape(-1, features.shape[-1])
    y_train = target[:train_n].reshape(-1)
    x_test = features[train_n:].reshape(-1, features.shape[-1])
    y_test = target[train_n:].reshape(-1)
    coeff, *_ = np.linalg.lstsq(x_train, y_train, rcond=None)
    return float(np.sqrt(np.mean((x_test @ coeff - y_test) ** 2)))


def main():
    rng = np.random.default_rng(SEED)
    e = rng.normal(0, 0.12, size=(N, T))
    u = np.zeros((N, T))
    for t in range(1, T):
        u[:, t] = 0.9 * u[:, t - 1] + e[:, t]
    e1 = rng.normal(0, 0.07, size=(N, T))
    e2 = rng.normal(0, 0.07, size=(N, T))
    ey = rng.normal(0, 0.01, size=(N, T))

    arms = {}
    for kind in ("full", "common_driver", "direct_dyad", "latent_clone"):
        baseline = simulate(kind, u, e1, e2, ey, False)
        challenged = simulate(kind, u, e1, e2, ey, True)
        # Lower deficit area means faster recovery after a matched perturbation.
        sl = slice(PERTURB_AT, PERTURB_AT + WINDOW)
        deficit = np.mean(np.abs(challenged[3][:, sl] - baseline[3][:, sl]), axis=1)
        source_sd = np.minimum(challenged[0][:, sl].std(axis=1), challenged[1][:, sl].std(axis=1))
        arms[kind] = {
            "mean_reporter_deficit": float(deficit.mean()),
            "source_sd_gate_rate": float(np.mean(source_sd > 0.04)),
            "deficit": deficit,
            "trajectory": challenged,
        }

    full = arms["full"]["deficit"]
    removed = arms["common_driver"]["deficit"]
    # Positive difference means the mediator reduced perturbation deficit.
    effect = removed - full
    direct_effect = arms["direct_dyad"]["deficit"] - full
    boot = np.empty(1000)
    direct_boot = np.empty(1000)
    for b in range(len(boot)):
        indices = rng.integers(0, N, size=N)
        boot[b] = effect[indices].mean()
        direct_boot[b] = direct_effect[indices].mean()

    x1, x2, m, y = arms["full"]["trajectory"]
    # Predict y_(t+1) from information available at t. Split by independent runs.
    x1, x2, m, y, u = (v[:, :-1] for v in (x1, x2, m, y, u))
    target = arms["full"]["trajectory"][3][:, 1:]
    ones = np.ones_like(y)
    relation = np.exp(-3 * (x1 - x2) ** 2)
    additive = np.stack((ones, y, x1, x2), axis=-1)
    common = np.stack((ones, y, u), axis=-1)
    dyad = np.stack((ones, y, x1, x2, relation), axis=-1)
    full_features = np.stack((ones, y, x1, x2, m, relation), axis=-1)
    shift_rng = np.random.default_rng(SEED + 1)
    shifted = np.empty_like(x2)
    for i in range(N):
        shifted[i] = np.roll(x2[i], int(shift_rng.integers(35, 121)))
    circular_autocorrelation_error = max(
        float(np.max(np.abs(np.sum(x2 * np.roll(x2, lag, axis=1), axis=1)
                            - np.sum(shifted * np.roll(shifted, lag, axis=1), axis=1))))
        for lag in (1, 2, 5, 10, 20)
    )
    shifted_relation = np.exp(-3 * (x1 - shifted) ** 2)
    shifted_features = np.stack((ones, y, x1, shifted, shifted_relation), axis=-1)
    scores = {
        "N1_common_driver": fit_score(common, target, 600),
        "N2_additive": fit_score(additive, target, 600),
        "N3_direct_dyad": fit_score(dyad, target, 600),
        "N4_circular_shift": fit_score(shifted_features, target, 600),
        "BFG_mediator_and_relation": fit_score(full_features, target, 600),
    }
    # N5 is an equal-capacity dynamic clone under a different semantic label.
    clone_max = max(float(np.max(np.abs(a - b))) for a, b in zip(
        arms["full"]["trajectory"], arms["latent_clone"]["trajectory"]
    ))
    print(json.dumps({
        "status": "exploratory synthetic pilot; no empirical BFG validation",
        "seed": SEED,
        "runs": N,
        "perturbation_time": PERTURB_AT,
        "perturbation_size": PERTURB_SIZE,
        "generative_ablation": {
            "mean_reporter_deficit": {k: v["mean_reporter_deficit"] for k, v in arms.items()},
            "source_sd_gate_rate": {k: v["source_sd_gate_rate"] for k, v in arms.items()},
            "paired_no_mediator_minus_full": float(effect.mean()),
            "exploratory_bootstrap_95_interval": [float(x) for x in np.quantile(boot, [0.025, 0.975])],
            "paired_direct_dyad_minus_full": float(direct_effect.mean()),
            "direct_dyad_bootstrap_95_interval": [float(x) for x in np.quantile(direct_boot, [0.025, 0.975])],
            "full_mean_absolute_mediator": float(np.mean(np.abs(arms["full"]["trajectory"][2]))),
        },
        "held_out_prediction_rmse": scores,
        "circular_shift_autocorrelation_max_error": circular_autocorrelation_error,
        "equal_capacity_latent_clone_max_trajectory_difference": clone_max,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
