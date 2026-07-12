# Project Analysis

**Date:** 2026-07-12
**Auditor:** Claude Code (repository audit session)
**Audited commit:** `19cf2ec` ("Merge pull request #5 from ZacharyRW/master")
**Branch:** `claude/repository-audit-roadmap-turb0r`

This document supersedes `CODE_REVIEW.md` (2026-03-01) and `AUDIT.md` (2026-06-16) as the
current statement of repository health. Both earlier documents were re-verified item by item
against the working tree and against GitHub; their verification tables below record what is
still true, what has been fixed, and where those documents are now stale.

---

## Executive Summary

**What it is.** An educational Python repository (created 2020) demonstrating approaches to
summing numbers. It contains one original script plus five "improved by" variants authored by
different AI assistants, a shared `demos/summing_methods.py` library, and a 179-case pytest
suite. There is no build, deployment, or release process — the code is the product.

**Current health: fair, with one real bug and a licensing contradiction.** The test suite
passes cleanly (179/179 on Python 3.11), all sources compile, git hygiene is good (the
default-branch migration to `main` is already complete and the remote carries no stale
branches). The two prior review documents identified real issues, and almost none have been
acted on: the one reachable crash (P0) is still reproducible, a byte-identical duplicate file
still masquerades as a distinct implementation, and — most importantly for an educational
repository — the documentation contradicts the license: `LICENSE` is GPL v3, while **both**
`README.md` and `CLAUDE.md` claim Apache 2.0. GitHub's own license detection displays
"GPL-3.0" next to a README saying "Apache License 2.0".

**Strongest areas.** Test breadth relative to size; accurate, detailed CLAUDE.md structure
documentation; clean git history and completed `master` → `main` migration.

**Largest risks.** (1) License mismatch misleads anyone reusing the code. (2) The tests
create false confidence: they cover only `demos/summing_methods.py` — the five variant
programs that are the repository's stated subject have 0% coverage, and several tests verify
local re-implementations rather than source code. (3) No CI, so nothing guards the suite.

**Recommended direction.** Fix the license contradiction and the P0 crash immediately; then a
small stabilization pass (remove duplicates, add missing tests, add packaging + CI); then
decide the repository's primary mission (Python summation reference vs. AI-assistant
comparison) and align the docs. Full ordering is in `ROADMAP.md`.

---

## Project Overview

- **Purpose:** Educational demonstration of Python summation techniques and of iterative,
  AI-assisted code improvement.
- **Intended audience:** Python beginners; people studying input-validation patterns; people
  comparing AI coding assistants' output on the same task.
- **Main features:** Six interactive console programs of increasing sophistication (input
  validation, float support, menu system, positive/negative analysis), a typed shared library
  of summation functions (`+`, `sum`, `operator.add`, `reduce`, `math.fsum`), and a pytest
  suite.
- **Technology stack:** Pure Python (works on 3.8+; validated here on 3.11.15). Test-only
  dependencies: `pytest`, optionally `pytest-cov`. No runtime dependencies, no frameworks, no
  external services, no data persistence, no network use.
- **Architecture:** Flat scripts at the repo root + one package (`demos/`) + one test package
  (`tests/`). Each variant is self-contained; only the ChatGPT-lineage files relate to
  `demos/summing_methods.py`.
- **Maturity:** Complete as a demo; not packaged, not released (no tags), no CI.
- **Build/test/deploy/release:** No build step. Test with `pytest tests/`. No deployment or
  release process exists.

## Repository Structure

| Path | Role |
|---|---|
| `Sum.py` | Original 2020 script (two summation methods, `main()` wrapper) |
| `SumImprovedbyClaudeCode.py` | v1: `get_number()` retry loop, integers only |
| `SumImprovedbyClaudeCodev2.py` | v2: `allow_float`, multi-number, custom-sum demo |
| `SumImprovedbyClaudeCodev3.py` | v3: interactive menu, positive/negative breakdown (most complete) |
| `SumImprovedbyChatGPT.py` | **Byte-identical copy of `demos/summing_methods.py`** (see finding CR-3) |
| `SumImprovedbyChatGPTv2.py` | A pytest test module at the repo root (not a runnable demo) |
| `demos/summing_methods.py` | Shared typed library: `parse_numbers`, `add_*`, `sum_*` functions |
| `tests/` (7 files + conftest) | 179 test cases, all passing |
| `CLAUDE.md` | AI-assistant guide (detailed, mostly accurate, a few stale spots) |
| `CODE_REVIEW.md` | 2026-03-01 review, 17 findings — superseded by this document |
| `AUDIT.md` | 2026-06-16 audit — superseded by this document |
| `TEST_COVERAGE_REPORT.md` | 2025-11-19 test report — counts now stale |
| `LICENSE` | **GNU GPL v3** (README/CLAUDE.md incorrectly say Apache 2.0) |

## Validation Results

Environment: Linux container, Python 3.11.15. `pytest`, `pytest-cov`, and `ruff` were **not
declared or preinstalled** (nothing in the repo declares them — see DEP-1) and were installed
ad hoc with pip for this audit.

| Check | Command | Result |
|---|---|---|
| Compile | `python3 -m py_compile <all 7 source files>` | ✅ clean |
| Tests | `python3 -m pytest tests/ -q` | ✅ **179 passed** in 0.33s |
| Tests from `tests/` cwd | `cd tests && python3 -m pytest . -q` | ✅ 179 passed (conftest path setup works) |
| Coverage | `pytest tests/ --cov=. --cov-report=term` | ⚠️ 73% total — see below |
| Lint | `ruff check .` | ⚠️ **10 errors** (6 auto-fixable) |
| Type check | — | ⏭️ skipped: no mypy/pyright config exists; source annotations only in `demos/` |
| CI | GitHub Actions API | ⚠️ **0 workflows configured** |
| P0 crash repro | `echo "5" \| python3 -c "...show_two_number_demo()"` | 💥 **crash reproduced**: `ValueError: not enough values to unpack (expected 2, got 1)` |
| Duplicate check | `diff -q SumImprovedbyChatGPT.py demos/summing_methods.py` | ⚠️ byte-identical |

Coverage by file (statements): `demos/summing_methods.py` 74%, `Sum.py` 18%,
`SumImprovedbyClaudeCode.py` / `v2` / `v3` / `SumImprovedbyChatGPT.py` /
`SumImprovedbyChatGPTv2.py` **0%**, `tests/conftest.py` 66%.

Ruff findings: `F401` unused imports (`types` in `SumImprovedbyChatGPTv2.py:4` and
`tests/test_original_summing_methods.py:4`; `pytest` in `tests/test_input_validation.py:4`;
`add_sum`, `sum_reduce` in `tests/test_edge_cases.py:13,15`), `F541` f-string without
placeholders (`SumImprovedbyClaudeCodev3.py:97`), and 4× `E402` late imports in tests
(structural consequence of the `sys.path` bootstrap; acceptable, should be configured away).

Marker scan: no `TODO`, `FIXME`, `HACK`, `XXX`, `BUG` markers, and no skipped or disabled
tests exist anywhere in the Python code.

## Existing Issue Verification

Sources searched: `CODE_REVIEW.md` (17 items, "CR-n"), `AUDIT.md` (N-1…N-9, SEC-1, DOC-1…5,
DEP-1, CI-1, ADD/DIR ideas), `TEST_COVERAGE_REPORT.md`, GitHub issues/PRs (no open items;
5 merged PRs, 0 issues ever filed), and in-code markers (none found).

### CODE_REVIEW.md findings (2026-03-01)

| # | Item | Current Status | Verification | Still Relevant? | Recommended Action |
|---|---|---|---|---|---|
| CR-1 | P0: `show_two_number_demo` crashes on <2 numbers (`demos/summing_methods.py:66`) | **Confirmed** | Crash reproduced with input `"5"` | Yes | Fix — ROADMAP BUG-001 |
| CR-2 | `sys.path.append(".")` in 2 files | **Partially confirmed** | `tests/test_original_summing_methods.py` was already fixed in commit `117f3c7` (Nov 2025, *before* the review was written); `SumImprovedbyChatGPTv2.py:9` still has it | Yes (1 file) | Fix — BUG-002 |
| CR-3 | `SumImprovedbyChatGPT.py` byte-identical to `demos/summing_methods.py` | **Confirmed** | `diff -q` empty; header comment names the other file | Yes | Resolve — ARCH-001 |
| CR-4 | `test_original_summing_methods.py` duplicates `test_summation_methods.py` lines 1–108 | **Confirmed** | Both files read; same 8 test functions, same parametrizations | Yes | Consolidate — TEST-001 |
| CR-5 | No tests for `get_number` in any Claude variant | **Confirmed** | `grep get_number tests/` → only the comment promising future coverage (`test_input_validation.py:141-143`) | Yes | Add tests — TEST-002 |
| CR-6 | CLAUDE.md naming template stray space (`SumImproved by<YourName>`) | **Confirmed** | Present in "AI Assistant Guidelines → Create a new version" | Yes | Fix — DOC-002 |
| CR-7 | Ambiguous "~1,495 lines" test-suite claim | **Already fixed** | CLAUDE.md now scopes it to "7 test files"; actual `wc -l` of those 7 files = exactly 1,495 | No | None |
| CR-8 | CLAUDE.md uses `/home/user/Sum/` absolute paths | **Already fixed** | All Location entries are now relative (e.g. `Sum.py:1`); fixed after AUDIT.md was written | No | None |
| CR-9 | Misleading `get_number` docstring in `SumImprovedbyClaudeCode.py:2` ("number" but int-only) | **Confirmed** | File read | Yes | Fix — DOC-005 |
| CR-10 | `test_analysis_functions.py` tests a local copy of the v3 analysis logic | **Confirmed** | Local `analyze_numbers` defined at lines 12–33 | Yes | Refactor — TEST-003 |
| CR-11 | `test_module_has_docstring` asserts nothing about docstrings | **Confirmed** | `test_integration.py:212-216` only checks `__name__` | Yes | Fix — TEST-003 |
| CR-12 | Redundant `int()` casts | **Confirmed** | `SumImprovedbyClaudeCodev2.py:45`; `SumImprovedbyClaudeCodev3.py:50,65,88` | Yes (cosmetic) | Fix — BUG-003 |
| CR-13 | Unused `import types` ×2 | **Confirmed** | ruff F401 in both files | Yes | Fix — DX-002 |
| CR-14 | Wrong `# file:` header comments ×3 | **Confirmed** | Headers read in all affected files | Yes | Fix — DOC-005 |
| CR-15 | `test_custom_implementations.py` tests a local `custom_sum_v1` copy | **Confirmed** | Local copy at lines 11–16 | Yes | Refactor — TEST-003 |
| CR-16 | No upper bound / test for `get_multiple_numbers(count)` | **Confirmed** | Code read; no guard, no test | Yes (low) | Document — TEST-005 |
| CR-17 | CLAUDE.md `get_number` pattern shows only the v2/v3 signature | **Confirmed** | "Key Code Patterns" section unchanged | Yes | Fix — DOC-002 |

### AUDIT.md findings (2026-06-16)

| Item | Current Status | Verification | Still Relevant? | Recommended Action |
|---|---|---|---|---|
| N-1: CLAUDE.md says Apache 2.0, LICENSE is GPL v3 | **Confirmed — and worse** | LICENSE head = GPL v3; GitHub API license detection = `GPL-3.0`. AUDIT.md claimed "README does not state a license at all" — **that is now stale**: `README.md:39-41` also says "Apache License 2.0" | Yes — top priority | Reconcile — DOC-001 |
| N-2: CLAUDE.md staleness | **Partially confirmed** | "Last Updated: 2026-02-21" stands, though a "Last verified 2026-07-09" footer was added; HEAD has moved past the verified commit | Yes (minor) | DOC-002 |
| N-3: No CI despite 179 tests | **Confirmed** | GitHub Actions API: 0 workflows | Yes | GH-001 |
| N-4: No `requirements.txt` / `pyproject.toml` | **Confirmed** | No packaging file exists; pytest had to be pip-installed for this audit | Yes | DX-001 |
| N-5: `conftest.py` is 286 lines, heavier than any source file | **Confirmed — and worse** | Grep of every fixture name across `tests/`: **all ~30 fixtures are unused** by any test, and the 4 custom markers (`slow`, `integration`, `performance`, `edge_case`) are never applied. Only the `sys.path` bootstrap does anything | Yes | TEST-004 |
| N-6: No automated doc↔file-set consistency check | **Confirmed** | No such script exists | Low | Deferred (see ROADMAP) |
| N-7: "Sum.py refactored to be testable" claim is half-true | **Confirmed** | `main()` still calls `input()` directly; coverage on `Sum.py` is 18% (import-only) | Yes (minor) | DOC-002 |
| N-8: Mission conflation (Python reference vs. AI comparison) | **Confirmed** (judgment) | README first paragraph still merges both missions | Yes | ARCH-002 |
| N-9: GPL v3 unusual for an educational snippet repo | **Confirmed** (judgment) | License choice is the owner's decision | Yes | Feeds DOC-001 |
| SEC-1: license is the only security-relevant finding | **Confirmed** | Threat model re-checked: no secrets, no I/O beyond stdin/stdout, no deps | Yes | — |
| DEP-1 / CI-1: add packaging + CI | **Confirmed** | Same as N-3/N-4 | Yes | DX-001 / GH-001 |

### TEST_COVERAGE_REPORT.md claims

| Item | Current Status | Verification |
|---|---|---|
| "178 passing, 1 skipped" | **Already fixed / stale** | Now 179 passing, 0 skipped (skip removed in `4fe6ee9`) |
| "6 specialized test modules" | **Stale** | 7 test files exist |
| Per-file test counts and structure | Broadly accurate | Cross-checked against `pytest` collection |

### GitHub project

No open or closed issues exist, no draft PRs, no milestones, no projects boards with content.
All 5 historical PRs are merged; none represent unfinished work.

## Newly Discovered Findings

### High

**NEW-1 · README.md also contradicts the license (extends N-1/DOC-1)**
- Category: documentation / legal. Files: `README.md:39-41`, `CLAUDE.md` ("License: Apache
  License 2.0"), `LICENSE`.
- Evidence: `LICENSE` is GPL v3 (confirmed by GitHub's automated detection). Both user-facing
  docs claim Apache 2.0. AUDIT.md recorded only the CLAUDE.md half; the README section was
  added by PR #3 (2026-02-21), so the contradiction is now on the repository's public landing
  page directly beneath GitHub's "GPL-3.0 license" badge.
- Impact: anyone evaluating reuse gets contradictory terms; for an educational repo this is
  the single most misleading defect.
- Fix: owner decision (keep GPL v3 and fix docs, or relicense to Apache-2.0/MIT and replace
  LICENSE). Mechanics are trivial either way. Confidence: high.

### Medium

**NEW-2 · The entire conftest fixture library is dead code (sharpens N-5)**
- Category: test maintainability. File: `tests/conftest.py` (286 lines).
- Evidence: grep for every fixture name across `tests/test_*.py` — zero usages of all ~30
  fixtures; zero usages of the 4 registered markers. Only lines 1–9 (sys.path bootstrap) and
  `pytest_configure` execute usefully.
- Impact: ~270 lines of scaffolding imply coverage that doesn't exist and will silently drift.
- Fix: delete unused fixtures (or convert the best ones into actual parametrized tests).
  Confidence: high.

**NEW-3 · Tests cover only the library, not the six programs the repo is about**
- Category: test coverage. Files: all `Sum*.py` variants.
- Evidence: coverage run — 0% on all five variant files, 18% (import-only) on `Sum.py`; 100%
  of test assertions target `demos.summing_methods` or local re-implementations (CR-10/CR-15).
- Impact: "179 test cases" materially overstates protection; any regression in the variants
  ships silently. This aggregates CR-5/CR-10/CR-15 into their real consequence.
- Fix: TEST-002/TEST-003 (mock `input` to drive `get_number`/`demonstrate_sum_methods`;
  extract testable logic from v3). Confidence: high.

### Low

**NEW-4 · `SumImprovedbyChatGPTv2.py` is a mislabeled test module, and the same 8 tests exist in three places**
- Evidence: the file contains only pytest tests (no `main`, no `__main__` guard); running
  `python SumImprovedbyChatGPTv2.py` does nothing. Its first ~108 lines match
  `tests/test_original_summing_methods.py` and `tests/test_summation_methods.py:1-108`.
  README/CLAUDE.md call it a "test-driven variant", which under-explains that it is not a
  runnable improvement of Sum at all.
- Fix: fold into ARCH-001/TEST-001 decision: keep it (documented as the historical origin of
  the test suite) or remove it once the suite is consolidated. Confidence: high.

**NEW-5 · TEST_COVERAGE_REPORT.md is stale**
- Evidence: see verification table above (178+1 vs 179+0; 6 vs 7 modules; predates two fixes).
- Fix: refresh the numbers or archive it and let CI + this analysis be the record. DOC-003.

**NEW-6 · Lint debt (10 ruff errors) and no lint configuration**
- Evidence: ruff output in Validation Results; includes one source-file wart
  (`SumImprovedbyClaudeCodev3.py:97` `f"\nBreakdown:"` needs no `f`).
- Fix: DX-002 — add ruff config (allowing E402 in tests or moving the bootstrap into
  conftest-only), auto-fix the rest. Confidence: high.

### Informational

- **NEW-7** · GitHub metadata gaps: no topics, no website, wiki and projects enabled but
  unused, no releases or tags in 6 years, `main` unprotected, no Dependabot config (nothing
  for it to track, but an Actions-version updater becomes useful once CI exists). GH-002…004.
- **NEW-8** · No CONTRIBUTING/SECURITY/CHANGELOG/issue templates. For a single-owner
  educational repo these are mostly optional; see Documentation Assessment for which are worth
  creating.
- **NEW-9** · `AUDIT.md` itself now contains stale claims (its §2.1 table says CR-2 and CR-8
  are "still present" in full; CR-8 is fixed and CR-2 is half-fixed) — one more reason to mark
  it superseded rather than treat it as current truth.

## Architecture Assessment

**Strengths.** The flat, self-contained-variant layout perfectly serves the educational
narrative — each file is a complete, runnable lesson; `demos/` shows the "graduated to a
library" step; type hints and docstrings in `demos/summing_methods.py` are genuinely good
teaching material. There is no accidental complexity: no frameworks, no config sprawl.

**Weaknesses / debt.**
1. The v1→v2→v3 progression story is undermined by CR-3 (the "module-based architecture"
   exhibit is a copy, not a demonstration) and NEW-4 (the "test-driven variant" is a test file).
2. Logic and I/O are fused in the variants (`method_positive_negative_demo`, nested
   `custom_sum`), which is why the tests resort to local copies. Extracting pure functions
   (keeping the interactive wrappers) would fix CR-10/CR-15 without harming the lesson.
3. Triple duplication of the core test set (root file + two test modules).

**Scalability.** Not a concern at this size. The only structural risk is doc↔code drift
(N-6), which CI plus consolidated docs mitigates adequately without new tooling.

**Recommended improvements.** ARCH-001 (make `SumImprovedbyChatGPT.py` a real, short consumer
of `demos.summing_methods` — that is what the docs already claim it is), TEST-003 (extract
`analyze_numbers`/`custom_sum` to module level in v3), and ARCH-002 (write down the primary
mission and let the README lead with it).

## Test and Quality Assessment

179 tests, 100% passing, fast (<1s). Qualitatively: excellent breadth on
`demos.summing_methods` (edge cases, precision, inf/NaN, generators, large inputs) — and a
blind spot everywhere else (NEW-3). Specific gaps: `get_number` untested in all three Claude
variants (CR-5); two test classes verify re-implementations, not source (CR-10/CR-15); one
test is a no-op (CR-11); duplicate test file wastes runs (CR-4); dead fixture library (NEW-2).
No flaky tests observed across repeated runs.

## Security and Privacy Assessment

Threat model is essentially nil: interactive stdin/stdout scripts, no file/network I/O, no
secrets (confirmed by scan), no dependencies with CVE exposure (pytest is test-only and
undeclared). **Confirmed finding:** the license contradiction (DOC-001) is the only item with
legal/compliance consequence. **Potential risks requiring no action:** unbounded
`get_multiple_numbers(count)` lets a user request a billion prompts (CR-16) — a UX curiosity,
not a vulnerability.

## Performance Assessment

No confirmed bottlenecks; the heaviest operation anywhere is summing 200,000 integers in a
test (completes in milliseconds). No measurement work is warranted.

## Documentation Assessment

| Document | Status | Problems | Recommended Action |
|---|---|---|---|
| `README.md` | Mostly accurate | **License section wrong (GPL v3, not Apache 2.0)**; doesn't state install/test prerequisites; mission statement conflated (N-8) | **Update** |
| `CLAUDE.md` | Good, minor staleness | License line wrong; stray space in naming template (CR-6); `get_number` pattern lacks version note (CR-17); "testable" claim overstated (N-7); "Last Updated" stale | **Update** |
| `CODE_REVIEW.md` | Superseded | Findings re-verified here; keeping it unmarked invites re-auditing stale claims | **Archive** (add superseded banner pointing here, or move to `docs/archive/`) |
| `AUDIT.md` | Superseded | Contains now-stale claims (NEW-9) | **Archive** (same treatment) |
| `TEST_COVERAGE_REPORT.md` | Stale | Counts wrong (NEW-5); duplicates what CI + coverage tooling should report | **Update or Archive** |
| `LICENSE` | Authoritative but contradicted | Owner must decide GPL v3 vs. permissive | **Keep + Decide** (DOC-001) |
| `ANALYSIS.md` / `ROADMAP.md` | New | — | **Create** (this change) |
| `CONTRIBUTING.md` | Missing | Low value for a single-owner edu repo; CLAUDE.md already carries conventions | **Skip** (fold a short "Contributing" note into README if ever needed) |
| `SECURITY.md`, `CODE_OF_CONDUCT.md`, `CHANGELOG.md` | Missing | Not warranted at this scale; git history is an adequate changelog | **Skip** |
| Setup/testing docs | Partial | README's `pytest tests/` works but assumes pytest is installed | **Update** README once DX-001 lands (`pip install -r requirements-dev.txt`) |

**Recommended final structure:** `README.md` (mission, files, quick start, tests, license) +
`CLAUDE.md` (AI-assistant guide) + `ANALYSIS.md`/`ROADMAP.md` (planning) + `docs/archive/`
(or superseded banners) for `CODE_REVIEW.md`, `AUDIT.md`, `TEST_COVERAGE_REPORT.md`.

## GitHub Repository Assessment

Inspected via GitHub API this session: repo metadata, branches, PRs (all 5, merged), issues
(none exist), releases/tags (none), Actions workflows (none), license detection.

- **Presentation:** description present ("Shows different ways to sum in Python"); **no
  topics** (suggest: `python`, `education`, `tutorial`, `ai-assisted-development`); no
  website; README renders well but shows the wrong license next to GitHub's GPL-3.0 badge.
- **Contribution workflow:** no issue/PR templates, no CONTRIBUTING — acceptable for a
  single-owner repo; not worth adding until outside contributors appear.
- **Automation:** no workflows, no Dependabot. A single ~30-line test+lint workflow (GH-001)
  is the highest-value addition; pair with `dependabot.yml` for `github-actions` ecosystem
  updates once workflows exist.
- **Settings:** default branch **is `main`** ✅; `main` is **not protected** (optional for a
  solo repo — a minimal "require PRs to pass CI" rule becomes meaningful after GH-001); wiki
  and projects enabled but unused (disable for tidiness); Discussions off (fine).
- **Releases:** none in 6 years. Optional: tag `v1.0` once Phase 1 of the roadmap lands, so
  the "known-good, audited" state is referenceable.
- **Could not inspect** (no API access to these settings): social preview image, funding
  config, rulesets detail, webhook list. Manual checklist: Settings → General (social
  preview, features), Settings → Branches (protection), Settings → Code security.

## Branch Assessment

Default branch: **`main`** — the desired end state already holds. The `master` → `main`
migration was completed 2026-07-06/09 via PR #4 (docs) and PR #5 (final merge of `master`
into `main`), and `master` has been deleted from the remote. No action remains.

| Branch | Last activity | Merge status | Associated PR | Unique commits | Recommended action | Reason |
|---|---|---|---|---|---|---|
| `main` (remote+local) | 2026-07-09 (`19cf2ec`) | default | — | — | **Keep** | Default branch |
| `claude/repository-audit-roadmap-turb0r` (local, this session) | 2026-07-12 | ahead of main (this audit) | to be opened | this audit's commits | **Keep** | Active work |

No stale, merged-but-undeleted, dependency, or release branches exist on the remote
(verified via `git ls-remote --heads origin` and the GitHub branches API). Historical PR head
branches were already cleaned up. **Nothing is safe-to-delete because nothing is deletable.**

## Product and Feature Opportunities

*Evidence-based near-term improvements* (from confirmed findings): fix BUG-001; make
`SumImprovedbyChatGPT.py` a genuine ~30-line demo importing `demos.summing_methods`
(ARCH-001); extract v3's analysis logic into an importable `analyze_numbers()` (TEST-003) —
this simultaneously improves the code lesson and the tests.

*Larger feature ideas (creative, fit current identity):*
- **FEAT-001 · CLI arguments / file input:** a `SumImprovedby…v4` accepting `argv` numbers or
  a file — teaches `argparse`, keeps the progression narrative going. Low complexity.
- **FEAT-002 · Tutorial notebook** (AUDIT DIR-2): `tutorial.ipynb` walking v1→v3 diffs.
  Medium complexity; high educational value; fits identity.
- **FEAT-003 · Statistics extension:** mean/median/min/max alongside sum in v3's analysis.
  Low complexity.

*Alternative directions (exploratory, need validation):*
- **"Same prompt, many assistants" benchmark** (AUDIT DIR-1): generalize to N problems with
  published comparisons. This changes the repo's identity — validate appetite first.

*Not recommended:* web interface, database history, async summation, logging framework
(CLAUDE.md "Future Enhancement Ideas" #3, #7, #8, #9) — they add operational complexity that
teaches nothing about summation and would swamp the 565-LOC pedagogical core.

## Recommended Priorities

1. **DOC-001** — resolve the license contradiction (owner decision + 3-line doc fix).
2. **BUG-001** — fix the reproducible `show_two_number_demo` crash.
3. **ARCH-001 + TEST-001** — eliminate the duplicate file and duplicate test module.
4. **DX-001 + GH-001** — declare dev dependencies; add CI (pytest + ruff).
5. **TEST-002/003** — test `get_number`; test source instead of local copies.
6. **DOC-002…005** — CLAUDE.md/README corrections; archive superseded review docs.
7. **ARCH-002** — pick and state the primary mission.

## Limitations

- GitHub settings pages not exposed via API (social preview, funding, rulesets, webhooks)
  were not inspected; a manual checklist is given above.
- `pytest`/`ruff` were installed ad hoc; results reflect pytest 9.x/ruff current on Python
  3.11 only — no version matrix was run (that is what GH-001 adds).
- No type checker was run (none is configured); `demos/` annotations were only spot-checked.
- Interactive UX of each variant was exercised only for the crash repro, not exhaustively.
- License intent (GPL vs. Apache) cannot be determined from evidence — it is an owner decision.
