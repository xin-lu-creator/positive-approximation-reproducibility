#!/usr/bin/env python3
"""Run the fastest deterministic verification check."""
from __future__ import annotations
import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def main() -> None:
    """Run the deterministic Schatten verification task."""
    subprocess.run([sys.executable, str(ROOT / "python" / "run_01_verify_schatten_counterexamples.py")], check=True)
    print("Demo verification: PASS")

if __name__ == "__main__":
    main()
