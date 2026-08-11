#!/usr/bin/env python3
"""Exact verification of the rational 4x4 counterexample.

File        : run_02_verify_exact_counterexample.py
Project     : PositiveApproximation
Purpose     : Reproduce the exact rank-(1,2) dual certificate and the dyadic
              chord-bound certificate used in the strict-failure theorem.
Input       : ../config/verification_config.json; no external dataset.
Output      : Console verification report and exact CSV when --csv is given.
Used in paper:
              Section 5, certified rational 4x4 counterexample and the exact
              rank-(1,1) obstruction.
Main parameters:
              A*, V, c, w4, m, J, the dyadic denominator, and expected exact
              bounds are read from the shared verification configuration.
Software    : Python 3.10+; SymPy.
Author      : Xin Lu
Last update : 2026-08-08
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

import sympy as sp

from src.config_utils import DEFAULT_CONFIG, load_config, rational
from src.exact_certificate import (
    dyadic_eigenvalue_upper_bound,
    principal_minors_nonnegative,
)


def _matrix_from_integer_grid(values: list[list[int]], denominator: int) -> sp.Matrix:
    """Construct an exact rational matrix from an integer grid and denominator."""
    if denominator == 0:
        raise ZeroDivisionError("matrix denominator must be nonzero")
    return sp.Rational(1, denominator) * sp.Matrix(values)


def verify(
    config_path: Path,
) -> tuple[
    sp.Rational,
    sp.Rational,
    sp.Rational,
    sp.Rational,
    list[tuple[str, str, str, str, str]],
]:
    """Verify every exact rational assertion used by the counterexample."""
    config = load_config(config_path)["exact_counterexample"]

    matrix_a = _matrix_from_integer_grid(
        config["A_numerator"], int(config["A_denominator"])
    )
    matrix_v = _matrix_from_integer_grid(
        config["V_numerator"], int(config["V_denominator"])
    )
    matrix_v_u = matrix_v[:3, :]
    vector_c = sp.Matrix([rational(pair) for pair in config["c_rationals"]])
    vector_w = matrix_v_u * vector_c
    vector_w = vector_w.col_join(sp.Matrix([rational(config["w4_rational"])]))

    matrix_g1 = vector_w * vector_w.T
    matrix_g2 = matrix_v * matrix_v.T
    if matrix_g1.rank() != 1 or matrix_g2.rank() != 2:
        raise AssertionError("Dual certificate ranks are not (1,2)")
    difference = matrix_g1 - matrix_g2

    if not principal_minors_nonnegative(matrix_g1):
        raise AssertionError("G1 is not positive semidefinite")
    if not principal_minors_nonnegative(matrix_g2):
        raise AssertionError("G2 is not positive semidefinite")
    if not principal_minors_nonnegative(-difference[:3, :3]):
        raise AssertionError("U-block dual inequality failed")
    if difference[3, 3] > 0:
        raise AssertionError("U-perp scalar dual inequality failed")

    objective = sp.trace(matrix_a * difference)
    normalization = sp.trace(matrix_g1 + matrix_g2)
    lower_bound = sp.factor(objective / normalization)
    expected_lower = rational(config["expected_dual_lower"])
    if lower_bound != expected_lower:
        raise AssertionError(f"Unexpected dual lower bound: {lower_bound}")

    rank11_upper = rational(config["rank11_upper"])
    if not principal_minors_nonnegative(matrix_a + rank11_upper * sp.eye(4)):
        raise AssertionError("lambda_min upper certificate failed")

    coupling = matrix_a[:3, 3]
    phi_perp_sq = (coupling.T * coupling)[0]
    if phi_perp_sq != sp.Rational(9, 4):
        raise AssertionError(f"Unexpected phi_perp^2: {phi_perp_sq}")
    if sp.sqrt(phi_perp_sq) != sp.Rational(3, 2):
        raise AssertionError("Unexpected phi_perp value")
    if not phi_perp_sq < rank11_upper**2:
        raise AssertionError("phi_perp bound does not lie below the rank-(1,1) upper bound")

    matrix_a_u = matrix_a[:3, :3]
    gram = coupling * coupling.T
    m_bound = rational(config["m_bound"])
    if not principal_minors_nonnegative(matrix_a_u + m_bound * sp.eye(3)):
        raise AssertionError("m bound for A_U failed")

    interval_count = int(config["interval_count"])
    dyadic_denominator = int(config["dyadic_denominator"])
    if interval_count < 1 or dyadic_denominator < 1:
        raise ValueError("interval_count and dyadic_denominator must be positive")

    certificate_rows: list[tuple[str, str, str, str, str]] = []
    candidates = [dyadic_eigenvalue_upper_bound(gram, dyadic_denominator)]
    certificate_rows.append(("G", "", "", str(candidates[0]), str(candidates[0])))

    for index in range(1, interval_count + 1):
        t_left = -m_bound + (index - 1) * m_bound / interval_count
        t_right = -m_bound + index * m_bound / interval_count
        chord_matrix = (t_left + t_right) * matrix_a_u + gram
        rho = dyadic_eigenvalue_upper_bound(chord_matrix, dyadic_denominator)
        candidate = sp.factor(rho - t_left * t_right)
        candidates.append(candidate)
        certificate_rows.append(
            (str(index), str(t_left), str(t_right), str(rho), str(candidate))
        )

    phi_u_sq_bound = max(candidates)
    expected_phi_bound = rational(config["expected_phi_u_sq_bound"])
    if phi_u_sq_bound != expected_phi_bound:
        raise AssertionError(f"Unexpected certified phi_U^2 bound: {phi_u_sq_bound}")
    if not expected_phi_bound < rank11_upper**2:
        raise AssertionError("Certified phi_U bound does not lie below rank-(1,1) upper bound")
    if not lower_bound > rank11_upper:
        raise AssertionError("Strict certificate gap is not positive")

    # These cross-products are printed explicitly in the manuscript.
    if 2833673 * 1024 != 2901681152:
        raise AssertionError("First manuscript cross-product changed")
    if 2421 * 1196694 != 2897196174:
        raise AssertionError("Second manuscript cross-product changed")

    gap = sp.factor(lower_bound - rank11_upper)
    return lower_bound, rank11_upper, phi_u_sq_bound, gap, certificate_rows


def write_csv(path: Path, rows: list[tuple[str, str, str, str, str]]) -> None:
    """Write the exact chord-certificate rows without floating-point conversion."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "case",
                "t_left",
                "t_right",
                "certified_lambda_max_upper",
                "candidate_phi_U_sq_upper",
            ]
        )
        writer.writerows(rows)


def main() -> None:
    """Parse arguments, verify the theorem certificate, and optionally save CSV."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG,
        help="verification configuration JSON file",
    )
    parser.add_argument(
        "--csv",
        type=Path,
        help="write all exact chord-bound certificates to this CSV path",
    )
    args = parser.parse_args()

    lower, upper, phi_u_sq_bound, gap, rows = verify(args.config)
    if args.csv is not None:
        write_csv(args.csv, rows)

    print("Exact rational verification: PASS")
    print(f"config                 = {args.config}")
    print(f"dual lower bound       = {lower} = {float(lower):.12f}")
    print(f"rank-(1,1) upper bound = {upper} = {float(upper):.12f}")
    print(f"strict gap             = {gap} = {float(gap):.12f}")
    print(f"certified phi_U^2      <= {phi_u_sq_bound} = {float(phi_u_sq_bound):.12f}")
    if args.csv is not None:
        print(f"certificate table      = {args.csv}")


if __name__ == "__main__":
    main()
