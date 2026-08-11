# Paper-to-code map

| Manuscript content | Verification entry point | Configuration | Frozen output |
|---|---|---|---|
| Schatten characterization strict examples | `python/run_01_verify_schatten_counterexamples.py` | `config/verification_config.json` | Console PASS report |
| Rational 4 x 4 strict obstruction and chord certificate | `python/run_02_verify_exact_counterexample.py` | `config/verification_config.json` | `results/frozen/counterexample_chord_bounds.csv` |

The scripts audit explicit calculations. They do not replace the proofs.
