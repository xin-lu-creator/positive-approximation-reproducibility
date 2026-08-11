#!/usr/bin/env python3
"""Deterministic verification of the 2x2 Schatten counterexamples.

File        : run_01_verify_schatten_counterexamples.py
Project     : PositiveApproximation
Purpose     : Sanity-check the explicit strict-improvement constructions used
              in the Schatten characterization theorem.
Input       : ../config/verification_config.json; no external dataset.
Output      : Console PASS/FAIL report. The project runner captures it in
              05_output_results/log_files/.
Used in paper:
              Section 3, Schatten characterization theorem. This script is a
              deterministic sanity check and is not the mathematical proof.
Main parameters:
              a, b, c, p values, and perturbation epsilon are read from the
              shared verification configuration.
Software    : Python 3.10+; NumPy.
Author      : Xin Lu
Last update : 2026-08-08
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np

from src.config_utils import DEFAULT_CONFIG, load_config


def schatten_norm(matrix: np.ndarray, p: float) -> float:
    """Return the Schatten-p norm of a real matrix."""
    singular_values = np.linalg.svd(matrix, compute_uv=False)
    if np.isinf(p):
        return float(singular_values[0])
    return float(np.sum(singular_values**p) ** (1.0 / p))


def verify(config_path: Path) -> None:
    """Run all deterministic strict-improvement checks."""
    config = load_config(config_path)["schatten_counterexample"]
    a = float(config["a"])
    c = float(config["c"])
    b = float(config["b"])
    epsilon = float(config["perturbation_epsilon"])
    p_values = [float(value) for value in config["interior_p_values"]]

    if not (a > 0 and c > 0 and b > a and epsilon > 0):
        raise ValueError("Schatten configuration must satisfy a>0, c>0, b>a, epsilon>0")

    matrix_a = np.array([[-a, c], [c, b]], dtype=float)
    pinch_positive = np.diag([0.0, b])

    # p = infinity: balancing the residual diagonal is strictly better.
    balanced = np.diag([0.0, b - a])
    if not schatten_norm(matrix_a - balanced, np.inf) < schatten_norm(
        matrix_a - pinch_positive, np.inf
    ):
        raise AssertionError("Spectral-norm counterexample check failed")

    # p = 1: the trace-norm construction requires c >= a.
    if c < a:
        raise ValueError("Trace-norm counterexample requires c >= a")
    trace_candidate = np.diag([0.0, b + a])
    if not schatten_norm(matrix_a - trace_candidate, 1.0) < schatten_norm(
        matrix_a - pinch_positive, 1.0
    ):
        raise AssertionError("Trace-norm counterexample check failed")

    # 1 < p < infinity, p != 2: one signed perturbation must improve the value.
    for p in p_values:
        if not (1.0 < p < np.inf) or np.isclose(p, 2.0):
            raise ValueError(f"Interior p value must satisfy 1<p<infinity and p!=2: {p}")
        baseline = schatten_norm(matrix_a - pinch_positive, p)
        plus_value = schatten_norm(matrix_a - np.diag([0.0, b - epsilon]), p)
        minus_value = schatten_norm(matrix_a - np.diag([0.0, b + epsilon]), p)
        if not min(plus_value, minus_value) < baseline:
            raise AssertionError(f"Interior Schatten counterexample failed for p={p}")

    print("Schatten counterexample checks: PASS")
    print(f"config={config_path}")
    print(f"a={a:g}, c={c:g}, b={b:g}, epsilon={epsilon:g}")
    print("interior_p_values=" + ",".join(f"{p:g}" for p in p_values))


def main() -> None:
    """Parse arguments and run the deterministic checks."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG,
        help="verification configuration JSON file",
    )
    args = parser.parse_args()
    verify(args.config)


if __name__ == "__main__":
    main()
