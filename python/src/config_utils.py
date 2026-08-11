"""Configuration helpers for deterministic verification scripts."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


PROGRAMS_DIR = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG = PROGRAMS_DIR / "config" / "verification_config.json"


def load_config(path: Path | None = None) -> dict[str, Any]:
    """Load the shared verification configuration JSON file."""
    config_path = DEFAULT_CONFIG if path is None else Path(path)
    if not config_path.exists():
        raise FileNotFoundError(f"Verification config does not exist: {config_path}")
    with config_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def rational(pair: list[int] | tuple[int, int]) -> sp.Rational:
    """Convert a two-integer numerator/denominator pair to a SymPy Rational."""
    if len(pair) != 2:
        raise ValueError(f"Expected [numerator, denominator], got: {pair}")
    numerator, denominator = int(pair[0]), int(pair[1])
    if denominator == 0:
        raise ZeroDivisionError("Rational denominator must be nonzero")
    return sp.Rational(numerator, denominator)
