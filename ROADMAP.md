# Project Roadmap

**Source of truth:** [ANALYSIS.md](ANALYSIS.md), reconciled 2026-07-19.
**Execution baseline:** Start implementation from clean `main`. Python 3.10+ is the maintained compatibility floor.

## Current state

The canonical lesson and historical artifacts are established, local correctness work is complete, and the supported matrix is **Python 3.10/3.11/3.14**. The compatibility migration, CLI improvement, and dependency reconciliation are verified by [CI run 29676990969](https://github.com/ZacharyRW/Sum/actions/runs/29676990969).

No open issue represents a verified local application defect. The remaining work is grouped below so administration, maintenance, and optional features do not blur together.

## Completed: Python 3.10+ migration

### COMPAT-001 — Drop Python 3.9 support

Completed 2026-07-19: `requires-python` is `>=3.10`; pytest is constrained to 9.x; Ruff targets Python 3.10; documentation and issue text are aligned; CI passes on Python 3.10, 3.11, and 3.14.

**Success criteria:** package metadata, dependencies, documentation, and CI consistently require Python 3.10+; a remote `main` run is green for all three supported versions.

### Dependency follow-through

- Completed: reviewed and merged Dependabot PRs #48 (checkout), #50 (setuptools), and #51 (pytest-cov).
- Completed: #49 (pytest 9) and #52 (Ruff) are closed as superseded by the compatibility and reconciliation commits.
- Keep automatic dependency merging disabled unless repository policy later explicitly authorizes it.

## Completed: automation and GitHub administration

### #15 GH-001 — Verify CI workflow

Completed 2026-07-19: [#15](https://github.com/ZacharyRW/Sum/issues/15) is closed with the green 3.10/3.11/3.14 run.

**Success criteria:** the issue records the actual commands and matrix, rather than a historical claim that CI is missing.

### #29 GH-003 — Protect `main` and define releases

Completed 2026-07-19: `main` requires the Python 3.10, 3.11, and 3.14 checks; admin enforcement is enabled; force pushes and deletions are disabled. No review-count, automatic dependency-merge, or automatic-release policy was added. Releases remain intentional user-facing milestones.

### #26 GH-002 — Review public presentation

Completed 2026-07-19: [#26](https://github.com/ZacharyRW/Sum/issues/26) is closed; the description identifies the educational tutorial and historical-comparison identity; topics are `python`, `education`, `tutorial`, `summation`, and `ai-assisted-development`; Wiki, Projects, and Discussions are disabled. A social image remains unnecessary unless it materially improves discovery.

## Completed: security-scope record

### #44 SEC-001 — Preserve local CLI security closure

Completed 2026-07-19: [#44](https://github.com/ZacharyRW/Sum/issues/44) is closed as a current-state result. Reopen security review before file input, network access, web/plugin integration, persistence, hosted execution, or authentication.

## Phase 5: Optional product work

Select at most one initiative after Phases 1–4.

| Issue | Initiative | Implementation boundary | Success criteria |
| --- | --- | --- | --- |
| #27 FEAT-001 | CLI arguments | Completed and closed: one-shot `--numbers` input in `demos/summing_methods.py` preserves no-argument interactive behavior. File input remains a separately approved feature. | Reassess only if file input is explicitly selected. |
| #25 FEAT-003 | Historical v3 statistics | Extend only `history.claude_v3_menu_demo.analyze_numbers()` after defining empty-input, type, and precision behavior. | Direct helper tests and thin menu presentation; provenance remains clear. |
| #28 FEAT-002 | Tutorial notebook | Import maintained code rather than copy it; clearly distinguish canonical and historical material. | Renders on GitHub and executes from a clean, documented environment. |

For any file-input proposal, first define encoding, format, size/count limits, finite-number policy, error handling, and a scoped security review.

## Completion criteria

- Python 3.10+ is the only documented and tested compatibility baseline.
- CI passes on Python 3.10, 3.11, and 3.14 from `main`.
- #15 is closed with live CI evidence.
- Dependency updates are reviewed intentionally.
- `main` protection and release policy are explicitly decided.
- Optional features remain separate from verified maintenance work until selected.
