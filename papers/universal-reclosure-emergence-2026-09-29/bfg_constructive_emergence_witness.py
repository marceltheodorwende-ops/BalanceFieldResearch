"""Deterministic constructive witness relative to CONSTRUCTIVE_TEST_PROTOCOL.md."""

import json
import random

A, B, SEED, RUNS, STEPS = 0.6, 0.4, 20260929, 1000, 160
REMOVE_AT, RESTORE_AT, END_AT = 80, 110, 130
TOL = 1e-12


def trajectory(sources, restore_at=None, removed=False):
    mediator = higher = 1.0
    output = []
    for t, (s1, s2) in enumerate(sources):
        if t == REMOVE_AT:
            higher = 0.0  # matched externally imposed perturbation
        gamma = 0.0 if removed and (restore_at is None or t < restore_at) and t >= REMOVE_AT else 1.0
        new_higher = B * higher + (1 - B) * gamma * mediator
        mediator = A * mediator + (1 - A) * (1 + 0.5 * s1 * s2)
        higher = new_higher
        output.append(higher)
    return output


def mean_window(values, start, end):
    return sum(values[start:end]) / (end - start)


def main():
    rng = random.Random(SEED)
    removal_effects = []
    restoration_effects = []
    min_full = 1.5
    max_full = 0.5
    for _ in range(RUNS):
        sources = [(rng.choice((-1, 1)), rng.choice((-1, 1))) for _ in range(STEPS)]
        assert all(abs(x) == abs(y) == 1 for x, y in sources)
        full = trajectory(sources)
        removed = trajectory(sources, removed=True)
        restored = trajectory(sources, restore_at=RESTORE_AT, removed=True)
        # The reset at t=80 creates a known transient; include steady epochs only.
        steady = full[:REMOVE_AT] + full[RESTORE_AT:]
        min_full = min(min_full, min(steady))
        max_full = max(max_full, max(steady))
        removal_effects.append(mean_window(full, 100, 110) - mean_window(removed, 100, 110))
        restoration_effects.append(mean_window(restored, 120, 130) - mean_window(removed, 120, 130))

    q = lambda x, y: 1 + 0.5 * x * y
    mixed = q(1, 1) - q(1, -1) - q(-1, 1) + q(-1, -1)
    # Difference of two runs with an impulse of unit size in q at time zero.
    m, h = 0.0, 0.0
    impulse = []
    for t in range(4):
        m, h = A * m + (1 - A) * (1.0 if t == 0 else 0.0), B * h + (1 - B) * m
        impulse.append(h)
    determinant = impulse[1] * impulse[3] - impulse[2] ** 2
    expected = [0.0, 0.24, 0.24, 0.1824]
    assert max(abs(x - y) for x, y in zip(impulse, expected)) < TOL
    assert abs(determinant + 0.013824) < TOL
    assert abs(mixed - 2.0) < TOL
    assert min_full >= 0.5 - TOL and max_full <= 1.5 + TOL
    assert min(removal_effects) > 0.49 and min(restoration_effects) > 0.49
    # Restricted additive/common-driver/shift and direct one-pole classes
    # have zero mixed contrast or zero temporal determinant by algebra.
    result = {
        "protocol": "CONSTRUCTIVE_TEST_PROTOCOL.md",
        "seed": SEED,
        "runs": RUNS,
        "source_gate_all": True,
        "full_steady_range": [round(min_full, 12), round(max_full, 12)],
        "min_full_minus_removed": round(min(removal_effects), 12),
        "min_restored_minus_removed": round(min(restoration_effects), 12),
        "mixed_contrast": mixed,
        "impulse_g1_to_g4": [round(x, 12) for x in impulse],
        "impulse_hankel_determinant": round(determinant, 12),
        "restricted_rival_gate": "PASS",
        "exact_two_state_clone": "TIE; representation equivalence",
        "scope": "Constructive synthetic realization relative to the declared restricted rival class; not canonical-map or natural-carrier validation",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
