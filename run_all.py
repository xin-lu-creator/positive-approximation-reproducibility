#!/usr/bin/env python3
"""Run all scientific verification tasks and compare the regenerated exact CSV."""
from __future__ import annotations
import hashlib, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FROZEN = ROOT / "results" / "frozen" / "counterexample_chord_bounds.csv"
GENERATED = ROOT / "results" / "generated" / "counterexample_chord_bounds.csv"

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main() -> None:
    subprocess.run([sys.executable, str(ROOT / "python" / "run_01_verify_schatten_counterexamples.py")], check=True)
    subprocess.run([
        sys.executable,
        str(ROOT / "python" / "run_02_verify_exact_counterexample.py"),
        "--csv", str(GENERATED),
    ], check=True)
    if GENERATED.read_bytes() != FROZEN.read_bytes():
        raise AssertionError("Regenerated certificate CSV differs from the frozen submission reference")
    print(f"frozen_csv_sha256={digest(FROZEN)}")
    print("Full reproducibility verification: PASS")

if __name__ == "__main__":
    main()
