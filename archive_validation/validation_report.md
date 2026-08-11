# Release validation report

Status before online publication: **PASS**.

Release: `v1.0.1-submission`.

Validated items:

- scientific scripts run successfully in the release-preparation environment;
- exact 4 x 4 certificate values reproduce exactly;
- regenerated chord-certificate CSV matches the frozen reference byte-for-byte;
- frozen CSV SHA-256 is `56d1162d1e943ea7bcba5ecef0240d959d8364ba60510f3779265ea44572f936`;
- no external dataset or randomness is required;
- public dependency list contains only NumPy and SymPy;
- no manuscript, cover letter, reviewer response, private key, credential, or local absolute path is included;
- public metadata contains no venue identifier;
- release metadata is centralized in `docs/release_metadata_master.md`;
- a single `CITATION.cff` is used and `.zenodo.json` is absent.
