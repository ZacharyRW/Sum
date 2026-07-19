# Project Analysis

**Reconciled:** 2026-07-19 (America/Denver)
**Base revision:** `main` at `5827008`
**Scope:** current working tree, current GitHub issue inventory, Actions history, and repository settings.

## Summary

Sum is an educational Python summation tutorial. `demos/summing_methods.py` is the maintained reusable lesson; `history/` preserves runnable original and AI-assisted examples as comparison and provenance artifacts.

The historical correctness, input-contract, duplicate-test, licensing, tooling, and canonical-implementation findings are resolved. The maintained project baseline is now **Python 3.10+**. This removes Python 3.9 from the package contract and CI matrix, and permits the declared pytest 9 development dependency. The compatibility change requires a green remote CI run after it reaches `main`.

No verified local application defect remains. The selected product improvement is canonical one-shot CLI input; remaining open GitHub work is repository administration, dependency review, security-scope bookkeeping, or deliberately deferred optional work.

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
| Current default branch CI | Passed before this compatibility change | [CI run 29671934081](https://github.com/ZacharyRW/Sum/actions/runs/29671934081) passed on the former 3.9/3.11/3.14 matrix at `5827008`. |
| New Python baseline | Local change pending remote verification | `requires-python` is `>=3.10`; CI targets 3.10/3.11/3.14; pytest is constrained to 9.x. |
| Security scope | No reportable finding | Current runtime has no network, file, persistence, authentication, or external-service path. |
| Branch protection | Not configured | GitHub returned “Branch not protected” for `main` on 2026-07-19. |

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
| #15 GH-001: CI | Former matrix was verified green; the new 3.10/3.11/3.14 matrix needs a post-push run. | Verify a green `main` run, then close the issue. |
| #25 FEAT-003: statistics | Optional historical-v3 enhancement. | Select only if changing a comparison artifact has clear teaching value. |
| #26 GH-002: public metadata | Description and five focused topics are configured; Wiki, Projects, and Discussions are disabled. | Close with the recorded settings. |
| #27 FEAT-001: CLI/file input | Canonical `--numbers` CLI mode is implemented locally; file input remains out of scope pending a separate security review. | Verify the new CLI on remote CI, then update/close the issue. |
| #28 FEAT-002: tutorial notebook | Optional. | Require a defined reader, maintained imports, and reproducible execution. |
| #29 GH-003: protection/release | CI is proven only for the former matrix; `main` is unprotected. | Configure protection after a green 3.10+ run and decide release policy separately. |
| #44 SEC-001: security-scope closure | Current and accurate. | Close as a current-state result while retaining explicit reassessment triggers. |

Dependabot PRs #48 (checkout), #50 (setuptools), and #51 (pytest-cov) were reviewed and merged on 2026-07-19. The pytest 9 proposal (#49) is superseded by the compatibility migration, and the Ruff proposal (#52) is superseded by the final reconciliation commit after becoming unmergeable against the updated requirement file.

## Historical findings

The reconciled historical correctness, input-validation, test-hygiene, license, and canonical-layout findings remain resolved. Their detailed mapping was retained in Git history and prior assessment revisions; this document is the current assessment and should not repeat stale test-count or coverage claims.
