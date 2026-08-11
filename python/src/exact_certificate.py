"""Exact linear-algebra helpers for the rational counterexample certificate."""
from __future__ import annotations

from itertools import combinations
from math import ceil

import sympy as sp


def principal_minors_nonnegative(matrix: sp.Matrix) -> bool:
    """Return whether every principal minor of a square matrix is nonnegative."""
    if matrix.rows != matrix.cols:
        raise ValueError("principal_minors_nonnegative requires a square matrix")
    n = matrix.rows
    for size in range(1, n + 1):
        for indices in combinations(range(n), size):
            if sp.factor(matrix.extract(indices, indices).det()) < 0:
                return False
    return True


def dyadic_eigenvalue_upper_bound(
    matrix: sp.Matrix,
    denominator: int,
) -> sp.Rational:
    """Return the smallest certified upper bound on the specified rational grid."""
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    if matrix.rows != matrix.cols:
        raise ValueError("matrix must be square")

    lower_value = max(matrix[i, i] for i in range(matrix.rows))
    upper_value = max(
        matrix[i, i]
        + sum(abs(matrix[i, j]) for j in range(matrix.cols) if j != i)
        for i in range(matrix.rows)
    )
    lo = ceil(lower_value * denominator)
    hi = ceil(upper_value * denominator)

    while lo < hi:
        mid = (lo + hi) // 2
        rho = sp.Rational(mid, denominator)
        if principal_minors_nonnegative(rho * sp.eye(matrix.rows) - matrix):
            hi = mid
        else:
            lo = mid + 1

    rho = sp.Rational(lo, denominator)
    if not principal_minors_nonnegative(rho * sp.eye(matrix.rows) - matrix):
        raise AssertionError("Failed to certify the computed eigenvalue upper bound")
    return rho
