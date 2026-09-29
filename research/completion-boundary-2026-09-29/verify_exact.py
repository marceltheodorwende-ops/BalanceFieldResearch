"""Exact rational countermodels to weak BFG completion conditions.

This does not formalize every historical BFG axiom or validate a natural carrier.
"""

from fractions import Fraction as F
import json


def witness_g():
    t = F(1, 2)
    first, second = t * t, t * t + t ** 4
    assert first == F(1, 4) and second == F(5, 16)
    assert first > 0 and second > 0 and first != second
    return [str(first), str(second)]


def witness_s():
    y = F(1, 2)
    z = (1 - y) / (1 + y)
    # Both functions are odd, weakly monotone and zero at balance.
    identity_gain, zero_gain = z, F(0)
    assert z == F(1, 3) and (identity_gain > 0) != (zero_gain > 0)
    return [str(z), str(identity_gain), str(zero_gain)]


def witness_r():
    c = F(1, 1) / (1 + F(1, 2))
    # P=diag(1,0), Q=diag(0,1): R=P+QCQ versus P+QC²Q.
    r1, r2 = (F(1), c), (F(1), c * c)
    assert r1 == (F(1), F(2, 3)) and r2 == (F(1), F(4, 9))
    assert r1 != r2 and all(F(0) < r[1] < F(1) for r in (r1, r2))
    return [[str(x) for x in r] for r in (r1, r2)]


def quadratic_bridges():
    c, b = F(2, 3), F(1, 3)
    assert c * c - b * b == c - b == F(1, 3)
    g_metric = F(3, 2)
    assert g_metric * (c * c - b * b) == F(1, 2)
    # For Y=[[1,1/2],[1/2,1]], I+Y has determinant 15/4.
    det = F(2) * F(2) - F(1, 2) ** 2
    response_then_project = F(2) / det
    project_then_response = F(1) / (1 + F(1))
    assert response_then_project == F(8, 15)
    assert project_then_response == F(1, 2)
    assert response_then_project - project_then_response == F(1, 30)
    return {
        "squared_channel_difference": str(c * c - b * b),
        "G_weighted_channel_difference": str(g_metric * (c * c - b * b)),
        "response_then_project": str(response_then_project),
        "project_then_response": str(project_then_response),
        "ordering_difference": str(response_then_project - project_then_response),
    }


def witness_e():
    a, b = F(3, 5), F(2, 5)
    signs = [(1, -1), (1, 1), (-1, -1), (-1, 1)] * 10
    h_state = h_history = m = F(1)
    inputs = []
    for t, (s1, s2) in enumerate(signs):
        if t == 12:
            h_state = h_history = F(0)  # matched perturbation
        gamma = F(0) if 12 <= t < 20 else F(1)
        r = a ** t + (1 - a) * sum(
            (a ** (t - 1 - k) * q for k, q in enumerate(inputs)), F(0)
        )
        assert r == m
        h_state = b * h_state + (1 - b) * gamma * m
        h_history = b * h_history + (1 - b) * gamma * r
        assert h_state == h_history
        q = F(1) + F(1, 2) * s1 * s2
        m = a * m + (1 - a) * q
        inputs.append(q)
    return {"steps": len(signs), "all_paths_equal": True, "exact_final_h": str(h_state)}


def main():
    print(json.dumps({"G": witness_g(), "S": witness_s(), "R": witness_r(), "E": witness_e(), "quadratic_bridges": quadratic_bridges()}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
