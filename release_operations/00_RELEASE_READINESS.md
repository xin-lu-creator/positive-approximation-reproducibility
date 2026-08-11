# Release readiness

Before publishing the GitHub release:

- [ ] Repository is public.
- [ ] `main` has been pushed without local changes.
- [ ] Tag `v1.0.1-submission` points to the frozen commit.
- [ ] Zenodo is connected to the correct GitHub account.
- [ ] Zenodo GitHub page has been synced.
- [ ] `positive-approximation-reproducibility` is enabled in Zenodo before the GitHub release is published.
- [ ] `CITATION.cff` is present and `.zenodo.json` is intentionally absent.
- [ ] `python run_demo.py` passes.
- [ ] `python run_all.py` passes.
- [ ] No private data, reviewer files, tokens, passwords, or local absolute paths are present.
- [ ] Release asset checksum has been recorded.

After publishing:

- [ ] GitHub release page and attached asset are visible.
- [ ] Zenodo has processed the release.
- [ ] Version DOI has been recorded.
- [ ] README/CITATION/manuscript availability text are updated only after the DOI is known.
- [ ] Public downloads are checked again.
