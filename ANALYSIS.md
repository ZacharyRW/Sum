# Project Analysis

**Reconciled:** 2026-07-18 (America/Denver)
**Local revision:** `main` at `53804bf`
**Scope:** current working tree and the GitHub issue inventory readable through the connected GitHub integration. This supersedes the 2026-07-14 snapshot, which evaluated the former root-level layout.

## Summary

Sum is an educational Python summation tutorial. The maintained reusable lesson is `demos/summing_methods.py`; `history/` preserves runnable original and AI-assisted examples as comparison and provenance artifacts. The previous flat source layout no longer exists.

The previously identified correctness, input-contract, duplicate-test, license, tooling, and canonical-implementation issues are resolved in the current working tree. The declared Python 3.9+ development environment is present, and the current Python 3.14 environment passes all local checks. The remaining open GitHub work is either remote verification/administration or optional product work; it is not evidence of an active defect in the lesson.

## Current repository map

| Current path | Role | Former root-level name, if any |
| --- | --- | --- |
| `demos/summing_methods.py` | Canonical reusable lesson and interactive demo. | Canonicalized from the former ChatGPT implementation. |
| `history/original_two_number.py` | Original two-number CLI artifact. | `Sum.py` |
| `history/claude_v1_integer_demo.py` | Claude v1 integer-input artifact. | `SumImprovedbyClaudeCode.py` |
| `history/claude_v2_multiple_numbers.py` | Claude v2 finite-float/many-number artifact. | `SumImprovedbyClaudeCodev2.py` |
| `history/claude_v3_menu_demo.py` | Claude v3 menu/sign-analysis artifact. | `SumImprovedbyClaudeCodev3.py` |
| `history/chatgpt_v1_entrypoint.py` | Historical entry point that delegates to the canonical lesson. | `SumImprovedbyChatGPT.py` |
| `history/chatgpt_v2_test_snapshot.py` | Non-collected historical pytest snapshot. | `SumImprovedbyChatGPTv2.py` |
| `tests/` | Active pytest suite. `test_summation_methods.py` is the one core arithmetic suite. | — |
| `pyproject.toml`, `requirements-dev.txt` | Declared Python 3.9+ test/lint toolchain. | — |
| `.github/workflows/ci.yml`, `.github/dependabot.yml` | CI and dependency-update configuration. | — |

`history/README.md` is the authoritative former-name mapping. New documentation and issue work should use the current paths above, not the old filenames.

## Verification

| Check | Result | Evidence |
| --- | --- | --- |
| Repository identity | Passed | `main` at `53804bf`; local `main` and `origin/main` point to the same commit. |
| Working tree | Passed | Clean before this documentation reconciliation. |
| Syntax | Passed | `python3 -B -m compileall -q demos history tests`. |
| Tests | Passed | `./.venv/bin/python -m pytest tests/`: **142 passed** on Python 3.14.6. |
| Lint | Passed | `./.venv/bin/python -m ruff check .`: **All checks passed** (Ruff 0.15.22). |
| Toolchain | Present | `pyproject.toml` and `requirements-dev.txt` declare the development tools and pytest test path. |
| CI configuration | Present locally | Workflow runs pytest and Ruff for Python 3.9, 3.11, and 3.14. A green remote Actions run was not inspected in this reconciliation. |
| Security scope | No reportable finding | Current runtime has no network, file, persistence, authentication, or external-service path. |

## Reconciliation of historical review findings

All items below were checked against the current filesystem and source rather than inferred from the former filenames.

| Historical finding | Current status | Current evidence |
| --- | --- | --- |
| CR-1 / BUG-001: one-number crash | Resolved | `show_two_number_demo()` retries until it receives exactly two integers; direct regression test covers a one-number attempt. |
| CR-2 / BUG-002: `sys.path.append(".")` | Resolved | No path mutation remains; the former snapshot is `history/chatgpt_v2_test_snapshot.py` and is non-collected. |
| CR-3 / ARCH-001: duplicate ChatGPT implementation | Resolved | `history/chatgpt_v1_entrypoint.py` delegates to `demos.summing_methods.main`; it is no longer a duplicate implementation. |
| CR-4 / TEST-001: duplicate core suite | Resolved | The active core suite is `tests/test_summation_methods.py`; the duplicate is retained only as a historical non-collected snapshot. |
| CR-5 / TEST-002: Claude input untested | Resolved | `tests/test_claude_input.py` directly tests v1/v2/v3 retry, finite-float, EOF, menu, and bounded-count behavior. |
| CR-6 / CR-7: stale naming template/count claims | Obsolete | `CLAUDE.md` is now only a pointer to `AGENTS.md`; it contains neither stale filename template nor volatile test-count claim. |
| CR-8: machine-specific paths | Resolved | Repository docs use repository-relative paths. |
| CR-9 / DOC-005: v1 docstring | Resolved | `history/claude_v1_integer_demo.py` documents whole-number input. |
| CR-10 / TEST-003: local analysis replica | Resolved | `tests/test_analysis_functions.py` imports `history.claude_v3_menu_demo.analyze_numbers`. |
| CR-11: meaningless module-docstring test | Resolved | The canonical lesson has a module docstring, and `tests/test_integration.py` asserts that it is present and non-empty. |
| CR-12 / BUG-003: redundant `int(count)` | Resolved | Current v2/v3 callers pass the already-integer count directly. |
| CR-13 / DX-002: unused imports/lint | Resolved | Declared Ruff check is clean. |
| CR-14 / DOC-005: copied file headers | Resolved | No stale copied file headers remain; current module documentation matches each file's role. |
| CR-15 / TEST-003: local custom-sum replica | Resolved | `tests/test_custom_implementations.py` imports both historical source helpers directly. |
| CR-16 / TEST-005: uncapped count | Resolved | Historical v2/v3 examples enforce `MAX_INPUT_COUNT = 100`; direct tests cover both bounds. |
| CR-17: v2/v3 pattern presented as universal | Obsolete | The prior explanatory content was retired with the Claude guidance refresh. |
| License mismatch / DOC-001 | Resolved locally | `LICENSE`, `README.md`, and `pyproject.toml` specify GPL-3.0/GPL-3.0-only. GitHub repository metadata remains an owner-side check. |
| Missing dependencies, CI, Dependabot | Resolved locally | Declared tooling plus CI and Dependabot configuration are present. |
| Unused fixtures and markers / TEST-004 | Resolved | The unused fixture catalogue and marker registrations were removed. |
| Stale audit/review/coverage reports | Resolved | They were removed after reconciliation; this document and `ROADMAP.md` are the current local records. |

## GitHub issue reconciliation

The connected GitHub integration returned these open issues on 2026-07-18: `#15`, `#25`–`#29`, and `#44`. The integration has read access but returned HTTP 403 for issue edits, so no remote issue title, body, or state was changed by this reconciliation.

| Issue | Current assessment | Required next action |
| --- | --- | --- |
| #15 GH-001: CI | Implemented locally. Its old body describes a different version matrix and missing CI. | Inspect a green Actions run for the current 3.9/3.11/3.14 workflow; then update/close the issue with write-authorized GitHub access. |
| #25 FEAT-003: statistics | Optional enhancement. Its target is now `history/claude_v3_menu_demo.py`, not a maintained v3 root file. | Choose it only if extending a historical comparison artifact remains worthwhile. |
| #26 GH-002: public metadata | Owner-admin review, not a filesystem defect. | Review topics, presentation, and optional GitHub features manually. |
| #27 FEAT-001: CLI/file input | Optional; its proposal for a new `SumImprovedby…v4` root file is obsolete. | Consider CLI arguments in the canonical lesson; decide file input separately with a security review. |
| #28 FEAT-002: tutorial notebook | Optional and compatible with the current layout. | Build it around `history/` plus the canonical lesson if selected. |
| #29 GH-003: protection/release | Pending administration. Its proposed unconditional `v1.0` release is not an accepted current requirement. | Verify CI, then decide branch protection and release policy. |
| #44 SEC-001: security-scope closure | Current and accurate in substance. | Reassess before adding any file, network, web, plugin, persistence, hosted, or authentication path. |

The previously tracked issues #7–#14, #16–#24, and #30 correspond to the resolved items in the table above. In particular, #30 (redundant integer casts) is closed as completed. Their historical bodies may still name former paths; treat this current mapping and `history/README.md` as authoritative until a write-authorized GitHub session can refresh those records.

## Remaining local maintenance

No verified local defect remains from the reconciled historical issue set.
Feature work remains explicitly optional. CLI arguments, file input, expanded statistics, and a notebook should not be described as defects or revived merely because their historical issue bodies remain open.
