"""Small reproducible checks for the proposed L0-NC law; not a proof."""

from fractions import Fraction as F
from math import sqrt


def matmul(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def inverse2(a):
    det = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    assert det > 0
    return [[a[1][1] / det, -a[0][1] / det],
            [-a[1][0] / det, a[0][0] / det]]


# Exact scalar coefficients with the same historical capacities.
h, neutral, d = F(2), F(2), F(7, 5)
l = neutral / h
assert l == 1
s = h + neutral * neutral / h
eta = neutral * d / s
assert eta == d / 2
j = h * (d - l * eta) ** 2 / 2 + h * eta ** 2 / 2
assert j == d * d / 2
eta_alt = d / 3
j_alt = (d - eta_alt) ** 2 + 2 * eta_alt ** 2
assert j_alt == 2 * d * d / 3

# A positive two-dimensional full capacity triple and a non-scalar Gram load.
k = [[-1.0, 0.0], [0.0, 2.0]]
n = [[1.0, 0.25], [0.25, 1.0]]
c = [[0.0, 0.0], [0.0, 3.0]]
cap_d = [[2.0, 0.25], [0.25, 2.0]]
for i in range(2):
    for j in range(2):
        assert abs(c[i][j] + n[i][j] - cap_d[i][j] - k[i][j]) < 1e-14

a = [[0.5, 1 / (4 * sqrt(6))], [1 / (4 * sqrt(6)), 1 / 3]]
y = matmul(a, a)
assert abs(y[0][1] - 5 / (24 * sqrt(6))) < 1e-14
assert abs((k[0][0] - k[1][1]) * y[0][1] + 5 / (8 * sqrt(6))) < 1e-14
assert max(sum(abs(x) for x in row) for row in a) < 1

# Cross-check Schur complement against the whitened resolvent.
h2 = [[2.0, 0.0], [0.0, 3.0]]
hinv = [[0.5, 0.0], [0.0, 1 / 3]]
s2 = matmul(matmul(n, hinv), n)
s2 = [[s2[i][j] + h2[i][j] for j in range(2)] for i in range(2)]
left_correction = matmul(matmul(n, inverse2(s2)), n)
schur = [[h2[i][j] - left_correction[i][j] for j in range(2)] for i in range(2)]
res = inverse2([[float(i == j) + y[i][j] for j in range(2)] for i in range(2)])
root = [[sqrt(2.0), 0.0], [0.0, sqrt(3.0)]]
resolvent = matmul(matmul(root, res), root)
for i in range(2):
    for j in range(2):
        assert abs(schur[i][j] - resolvent[i][j]) < 1e-12

print("L0-NC scalar and two-dimensional consistency checks passed.")
