# Project Roadmap

**Source of truth:** [ANALYSIS.md](ANALYSIS.md), reconciled 2026-07-19.
**Execution baseline:** Start implementation from clean `main`. Python 3.10+ is the maintained compatibility floor.

## Current state

The canonical lesson and historical artifacts are established, local correctness work is complete, and a former CI matrix passed on `main`. The active compatibility migration updates the supported matrix from Python 3.9/3.11/3.14 to **Python 3.10/3.11/3.14** and raises pytest to the compatible 9.x line. Do not call CI fully verified again until this revision passes remotely on `main`.

No open issue represents a verified local application defect. The remaining work is grouped below so administration, maintenance, and optional features do not blur together.

## Phase 1: Complete the Python 3.10+ migration

### COMPAT-001 — Drop Python 3.9 support

1. Declare `requires-python = ">=3.10"` in `pyproject.toml`.
2. Use `pytest>=9,<10` in `requirements-dev.txt`.
3. Run CI for Python 3.10, 3.11, and 3.14.
4. Keep README, agent guidance, analysis, roadmap, and GitHub issue text aligned with the same baseline.
5. Run the declared local pytest and Ruff checks, then push the focused change and verify a green `main` run.

**Success criteria:** package metadata, dependencies, documentation, and CI consistently require Python 3.10+; a remote `main` run is green for all three supported versions.

### Dependency follow-through

- Re-evaluate Dependabot PR #49 (pytest 9) after COMPAT-001; it formerly failed only because Python 3.9 cannot install pytest 9.
- Review #48, #50, #51, and #52 independently; green CI does not replace release-note and scope review.
- Merge no dependency update automatically unless repository policy later explicitly allows it.

## Phase 2: Close verified automation work

### #15 GH-001 — Verify CI workflow

After COMPAT-001 reaches `main`, link the green 3.10/3.11/3.14 Actions run in [#15](https://github.com/ZacharyRW/Sum/issues/15) and close it.

**Success criteria:** the issue records the actual commands and matrix, rather than a historical claim that CI is missing.

## Phase 3: GitHub administration

### #29 GH-003 — Protect `main` and define releases

After #15 closes:

1. Create a ruleset or branch-protection rule for `main`.
2. Require the CI workflow, or the `Python 3.10`, `Python 3.11`, and `Python 3.14` checks if workflow-level protection is unavailable.
3. Decide whether pull requests, approval dismissal, owner bypass, and Dependabot auto-merge fit the maintainer workflow.
4. Define releases as intentional user-facing milestones, using tags/releases only when warranted; do not infer an automatic `v1.0`.

### #26 GH-002 — Review public presentation

1. Align the description with the educational tutorial and historical-comparison identity.
2. Add only useful topics, such as `python`, `education`, `tutorial`, `summation`, and optionally `ai-assisted-development`.
3. Retain Wiki, Projects, or Discussions only if each has an explicit maintenance purpose.
4. Record settings selected; add a social image only if it materially improves discovery.

## Phase 4: Close the current security-scope item

### #44 SEC-001 — Preserve local CLI security closure

Confirm the maintained scope remains local and in-memory, then close the issue as a current-state result. Reopen security review before file input, network access, web/plugin integration, persistence, hosted execution, or authentication.

## Phase 5: Optional product work

Select at most one initiative after Phases 1–4.

| Issue | Initiative | Implementation boundary | Success criteria |
| --- | --- | --- | --- |
| #27 FEAT-001 | CLI arguments | Implemented locally: one-shot `--numbers` input in `demos/summing_methods.py` preserves no-argument interactive behavior. File input remains a separately approved feature. | Verify on remote CI, update/close #27, and retain the documented numeric/error/exit contract. |
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
