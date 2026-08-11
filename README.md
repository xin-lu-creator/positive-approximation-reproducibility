# Positive Approximation under Subspace Decoupling — reproducibility package

This repository contains the deterministic verification code and exact-rational certificate files associated with the manuscript:

**Positive Approximation under Subspace Decoupling: From Frobenius to Spectral Norm**

Author: Xin Lu, Iwate University.

## Version

- Release tag: `v1.0.1-submission`
- Package version: `1.0.1-submission`
- Manuscript stage: initial submission

## Scope

The manuscript is a theoretical matrix-analysis study. This repository does **not** contain empirical datasets, benchmark experiments, stochastic simulations, or figure-generation pipelines. It contains only the deterministic checks used to audit the finite-dimensional constructions reported in the paper.

The two scientific verification tasks are:

1. explicit `2 x 2` strict-improvement checks supporting the Schatten counterexample constructions;
2. exact-rational verification of the certified `4 x 4` spectral-norm counterexample, including regeneration of the chord-certificate table.

The scripts are verification aids. They do not replace the mathematical proofs in the manuscript.

## Quick start

Python 3.10 or newer is recommended.

```bash
python -m pip install -r requirements.txt
python run_demo.py
python run_all.py
```

Windows PowerShell:

```powershell
python -m pip install -r requirements.txt
.\run_all.ps1
```

Linux/macOS:

```bash
python -m pip install -r requirements.txt
bash run_all.sh
```

A successful full run ends with:

```text
Full reproducibility verification: PASS
```

## Frozen output

The authoritative submission-version certificate table is:

```text
results/frozen/counterexample_chord_bounds.csv
```

A fresh run writes:

```text
results/generated/counterexample_chord_bounds.csv
```

and requires the regenerated file to be byte-identical to the frozen reference.

## Repository structure

```text
config/                 fixed theorem-verification constants
python/                 scientific verification scripts
python/src/             exact arithmetic and configuration helpers
results/frozen/         submission-version exact certificate table
results/generated/      fresh-run outputs; frozen results are never overwritten
environment/             environment and hardware notes
docs/                    reproducibility and paper-to-code documentation
archive_validation/      release validation records
release_operations/      GitHub/Zenodo release text and operational checklist
```

## No external data and no randomness

No external dataset, network connection, GPU, or random seed is required. The constants used in the manuscript constructions are frozen in `config/verification_config.json`.

## Reproducibility documentation

See:

- `docs/REPRODUCIBILITY.md`
- `docs/PAPER_TO_CODE_MAP.md`
- `docs/release_metadata_master.md`
- `archive_validation/validation_report.md`

## License

The verification code is released under the MIT License. See `LICENSE`.

## Citation

The submission release is permanently archived in Zenodo under the version-specific DOI [10.5281/zenodo.21883483](https://doi.org/10.5281/zenodo.21883483). Cite this DOI together with the fixed release tag `v1.0.1-submission`.

This repository is the frozen initial-submission reproducibility package. The scientific verification logic and frozen certificate data correspond to the submitted manuscript version.
