# GitHub repository and release text

## Repository name

```text
positive-approximation-reproducibility
```

## Repository description

```text
Exact-arithmetic verification code and reproducibility files for the manuscript “Positive Approximation under Subspace Decoupling: From Frobenius to Spectral Norm”.
```

## Topics

```text
matrix-analysis
positive-semidefinite
spectral-norm
schatten-norm
semidefinite-programming
reproducibility
exact-arithmetic
```

## Release tag

```text
v1.0.1-submission
```

## Release title

```text
v1.0.1-submission: Initial-submission reproducibility package
```

## Release description

```markdown
# v1.0.1-submission

This release provides the initial-submission verification code and reproducibility package for the manuscript **“Positive Approximation under Subspace Decoupling: From Frobenius to Spectral Norm.”**

This release provides the frozen initial-submission verification code and reproducibility files associated with the manuscript.

## Contents

This release includes:

- deterministic Python checks for the explicit Schatten counterexample constructions;
- exact-rational verification of the certified `4 x 4` spectral-norm counterexample;
- the frozen chord-certificate CSV used to audit the manuscript values;
- fixed verification constants and environment files;
- paper-to-code and reproducibility documentation.

No external dataset, random seed, GPU, or network connection is required for the verification tasks.

## Recommended first test

```bash
python -m pip install -r requirements.txt
python run_demo.py
```

## Complete verification

```bash
python run_all.py
```

A successful full run ends with:

```text
Full reproducibility verification: PASS
```

## Version information

- Release tag: `v1.0.1-submission`
- Paper status: Initial submission version
- Repository purpose: Exact-arithmetic verification and reproducibility support for the manuscript

## License and citation

Please see `LICENSE` and `CITATION.cff`.
```

## Release settings

- Pre-release: **No**
- Latest release: **Yes**
- Release asset: `PositiveApproximation_v1.0.1-submission_reproducibility-archive.zip`
