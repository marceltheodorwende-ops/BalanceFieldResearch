"""Fresh exact checks for the archived-BFG energy-bridge comparison.

This is a scoped algebraic check, not a physical-energy derivation.
"""

from fractions import Fraction as Q


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def matmul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def outer(v):
    return [[v[i] * v[j] for j in range(len(v))] for i in range(len(v))]


def expectation(rho, observable):
    return trace(matmul(rho, observable))


def main():
    # A nondegenerate two-sector Y and its archived neutral pair C=(I+Y)^-1,
    # B=Y(I+Y)^-1.  rho is a normalized rank-one carrier state.
    y = [Q(1, 4), Q(1, 2)]
    c = [[1 / (1 + y[0]), 0], [0, 1 / (1 + y[1])]]
    b = [[y[0] / (1 + y[0]), 0], [0, y[1] / (1 + y[1])]]
    v = [Q(3, 5), Q(4, 5)]
    rho = outer(v)
    assert trace(rho) == 1
    r = expectation(rho, c)
    beta = expectation(rho, b)
    assert r + beta == 1

    # The archived fractions are unchanged by a positive rescaling of the
    # unnormalized carrier vector. They therefore do not themselves fix a
    # dimensional energy scale.
    scale = Q(7, 3)
    scaled = [scale * z for z in v]
    rho_scaled = outer(scaled)
    r_scaled = expectation(rho_scaled, c) / trace(rho_scaled)
    b_scaled = expectation(rho_scaled, b) / trace(rho_scaled)
    assert (r_scaled, b_scaled) == (r, beta)

    # Same BFG Y/state fractions admit inequivalent diagonal energy operators.
    # The neutral pair contains no coefficient that selects either operator.
    h1 = [[0, 0], [0, 1]]
    h2 = [[0, 0], [0, 3]]
    e1, e2 = expectation(rho, h1), expectation(rho, h2)
    assert e1 == Q(16, 25)
    assert e2 == Q(48, 25)
    assert e1 != e2

    # Both candidates commute with the same sector involution Z; compatibility
    # with the two-sector dephasing generator cannot select one of them.
    z = [[1, 0], [0, -1]]
    assert matmul(h1, z) == matmul(z, h1)
    assert matmul(h2, z) == matmul(z, h2)

    print("PASS: archived neutral fractions sum to one and are scale invariant")
    print("PASS: same BFG data admit distinct sector-compatible energy operators")
    print(f"r_N={r}; b_N={beta}; E_H1={e1}; E_H2={e2}")


if __name__ == "__main__":
    main()

