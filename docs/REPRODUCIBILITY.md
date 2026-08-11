# Reproducibility

## Scientific scope

This archive supports independent checking of the finite-dimensional calculations accompanying **Positive Approximation under Subspace Decoupling: From Frobenius to Spectral Norm**. It is not an empirical experiment package.

## Verification tasks

### 1. Schatten counterexamples

Run:

```bash
python python/run_01_verify_schatten_counterexamples.py
```

This checks the explicit strict-improvement constructions used in the Schatten characterization theorem.

### 2. Exact rational 4 x 4 certificate

Run:

```bash
python python/run_02_verify_exact_counterexample.py --csv results/generated/counterexample_chord_bounds.csv
```

The verifier uses exact SymPy arithmetic and checks the stated dual lower bound, rank-(1,1) upper value, certificate ranks, block feasibility, dyadic chord bounds, and strict rational gap.

## Frozen comparison

`python run_all.py` regenerates the exact CSV and compares its bytes with the frozen submission reference. Expected SHA-256:

```text
56d1162d1e943ea7bcba5ecef0240d959d8364ba60510f3779265ea44572f936
```

## Randomness and data

There is no randomness and no external dataset. All fixed values are in `config/verification_config.json`.
