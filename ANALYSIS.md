# Project Analysis

**Reconciled:** 2026-07-19 (America/Denver)
**Verified revision:** `main` at `15b7df5`
**Scope:** current working tree, current GitHub issue inventory, Actions history, and repository settings.

## Summary

Sum is an educational Python summation tutorial. `demos/summing_methods.py` is the maintained reusable lesson; `history/` preserves runnable original and AI-assisted examples as comparison and provenance artifacts.

The historical correctness, input-contract, duplicate-test, licensing, tooling, and canonical-implementation findings are resolved. The maintained project baseline is **Python 3.10+**. Python 3.9 is absent from the package contract and CI matrix, and the declared pytest 9 development dependency is supported by a green remote run.

No verified local application defect remains. The canonical one-shot CLI is implemented. The only remaining open GitHub issues are deliberately deferred optional work.

## Current repository map

| Path | Role |
| --- | --- |
| `demos/summing_methods.py` | Canonical reusable summation lesson and interactive demo. |
| `history/` | Runnable historical examples and the authoritative former-name mapping. |
| `tests/` | Active pytest suite; `test_summation_methods.py` is the active core arithmetic suite. |
| `pyproject.toml`, `requirements-dev.txt` | Python 3.10+ package and development-tool contract. |
| `.github/workflows/ci.yml` | Test and lint matrix for Python 3.10, 3.11, and 3.14. |
| `.github/dependabot.yml` | pip and GitHub Actions update configuration. |

## Verification status

| Check | Status | Evidence |
| --- | --- | --- |
| Current default branch CI | Passed | [CI run 29676990969](https://github.com/ZacharyRW/Sum/actions/runs/29676990969) passed pytest and Ruff on Python 3.10, 3.11, and 3.14 at `15b7df5`. |
| Python baseline | Verified | `requires-python` is `>=3.10`; CI targets 3.10/3.11/3.14; pytest is constrained to 9.x. |
| Security scope | No reportable finding | Current runtime has no network, file, persistence, authentication, or external-service path. |
| Branch protection | Configured | `main` requires the Python 3.10/3.11/3.14 checks; admin enforcement is enabled; force pushes and deletions are disabled. |

Run the declared checks after installing the repository-local environment:

```bash
python3 -m venv .venv
./.venv/bin/python -m pip install -r requirements-dev.txt
./.venv/bin/python -m pytest tests/
./.venv/bin/python -m ruff check .
```

## GitHub reconciliation

| Item | Current assessment | Next action |
| --- | --- | --- |
| #15 GH-001: CI | Closed 2026-07-19 after the verified 3.10/3.11/3.14 run. | None. |
| #25 FEAT-003: statistics | Optional historical-v3 enhancement. | Select only if changing a comparison artifact has clear teaching value. |
| #26 GH-002: public metadata | Closed 2026-07-19: description and five focused topics are configured; Wiki, Projects, and Discussions are disabled. | None. |
| #27 FEAT-001: CLI/file input | Closed 2026-07-19: canonical `--numbers` CLI mode is verified; file input remains a separate, unselected proposal. | Reassess only if file input is explicitly selected. |
| #28 FEAT-002: tutorial notebook | Optional. | Require a defined reader, maintained imports, and reproducible execution. |
| #29 GH-003: protection/release | Closed 2026-07-19 after branch protection was configured. Releases remain intentional user-facing milestones, not an automatic `v1.0`. | None. |
| #44 SEC-001: security-scope closure | Closed 2026-07-19 as a current-state result. | Reassess before file, network, web/plugin, persistence, hosted, or authentication capability. |

Dependabot PRs #48 (checkout), #50 (setuptools), and #51 (pytest-cov) were reviewed and merged on 2026-07-19. The pytest 9 proposal (#49) and Ruff proposal (#52) are closed as superseded by the compatibility and reconciliation commits.

## Historical findings

The reconciled historical correctness, input-validation, test-hygiene, license, and canonical-layout findings remain resolved. Their detailed mapping was retained in Git history and prior assessment revisions; this document is the current assessment and should not repeat stale test-count or coverage claims.
