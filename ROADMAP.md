# Project Roadmap

**Date:** 2026-07-12 · **Derived from:** `ANALYSIS.md` (same date, commit `19cf2ec`)

Every item below traces to a finding verified in `ANALYSIS.md`. Nothing was copied from
older lists (`CODE_REVIEW.md`, `AUDIT.md`) without re-verification; items those documents
raised that are already fixed (CR-7, CR-8, the master→main migration) do not appear here.

## Roadmap Principles

Priority order is decided by, in order: (1) **user/reader impact** — this is an educational
repo, so anything that misleads a reader (wrong license, fake "distinct implementation",
false test confidence) outranks code polish; (2) **severity** — reachable crashes before
hygiene; (3) **risk reduction per unit effort** — CI and packaging are cheap and protect
everything after them; (4) **dependency order** — packaging before CI, CI before
refactoring, decisions (license, mission) before the docs that encode them;
(5) **strategic fit** — features must serve the teaching mission.

---

## Phase 0: Immediate Safety and Repository Hygiene

| Item | What / Why |
|---|---|
| **DOC-001** | **Resolve the license contradiction.** `LICENSE` = GPL v3; `README.md:39-41` and `CLAUDE.md` claim Apache 2.0. Owner decides: (a) keep GPL v3 → fix both docs; (b) relicense to Apache-2.0 or MIT (repo has a single copyright holder, so this is possible) → replace `LICENSE`. Until decided, docs must at minimum stop asserting Apache. |
| **BUG-001** | **Fix the reproducible crash** in `demos/summing_methods.py:66` (`show_two_number_demo`): entering one number raises `ValueError`. Loop until ≥2 numbers are supplied (fix sketch already in CODE_REVIEW.md CR-1). Add a regression test. |

*Not needed in Phase 0 (already done):* default-branch migration (`main` is default,
`master` deleted), branch cleanup (remote has only `main`), secret removal (none exist),
broken builds/failing tests (suite is green).

## Phase 1: Stabilization

| Item | What / Why |
|---|---|
| **BUG-002** | Replace `sys.path.append(".")` in `SumImprovedbyChatGPTv2.py:9` with `Path(__file__).parent` (last remaining instance; CR-2). |
| **ARCH-001** | Resolve the byte-identical duplicate: rewrite `SumImprovedbyChatGPT.py` as a short genuine demo that *imports* `demos.summing_methods` (matching what README/CLAUDE.md already claim it is), or delete it and update both docs. Decide `SumImprovedbyChatGPTv2.py`'s fate in the same pass (it is a test module, not a runnable variant — NEW-4). |
| **TEST-001** | Delete `tests/test_original_summing_methods.py` (100% duplicate of `test_summation_methods.py:1-108`; CR-4) and update CLAUDE.md's test table. |
| **TEST-002** | Add `get_number` tests for all three Claude variants (mock `builtins.input`; valid, invalid-then-retry, float/int modes, negatives; CR-5). Delete the misleading "we'll test it in integration" comment at `test_input_validation.py:141-143`. |
| **DX-001** | Add `requirements-dev.txt` (pytest, pytest-cov, ruff) and a minimal `pyproject.toml` with `requires-python >= 3.8` (N-4/DEP-1). Update README quick-start. |
| **DOC-005** | Small source-doc corrections: `SumImprovedbyClaudeCode.py:2` docstring says "number" but accepts only integers (CR-9); wrong `# file:` headers in 3 files (CR-14). |

## Phase 2: Maintainability and Developer Experience

| Item | What / Why |
|---|---|
| **GH-001** | Add `.github/workflows/ci.yml`: `pytest` + `ruff check` on a Python 3.9–3.13 matrix (N-3/CI-1). ~30 lines; protects everything else. |
| **DX-002** | Fix the 10 ruff findings (unused imports, `F541` at `SumImprovedbyClaudeCodev3.py:97`) and add ruff config that scopes `E402` for the test bootstrap pattern (NEW-6, CR-13). |
| **TEST-003** | Test source instead of copies: extract `analyze_numbers()` and `custom_sum()` to module level in `SumImprovedbyClaudeCodev3.py`/`v2` (keeping interactive wrappers), point `test_analysis_functions.py`/`test_custom_implementations.py` at the real functions (CR-10/CR-15), and make `test_module_has_docstring` assert a real docstring (add one to `demos/summing_methods.py`; CR-11). |
| **TEST-004** | Prune `tests/conftest.py`: all ~30 fixtures and 4 markers are unused (NEW-2). Keep the path bootstrap; delete or actually employ the rest. |
| **TEST-005** | Document that `get_multiple_numbers(count)` is uncapped and add a behavior test (CR-16). |
| **GH-004** | Add `dependabot.yml` for the `github-actions` ecosystem (only meaningful after GH-001). |

## Phase 3: Product Improvements

| Item | What / Why |
|---|---|
| **ARCH-002** | Decide and state the primary mission (Python summation reference vs. AI-assistant comparison; N-8). One paragraph at the top of README leads with the winner and names the other as secondary. |
| **DOC-002** | CLAUDE.md refresh: license line, stray-space naming template (CR-6), version note on the `get_number` pattern (CR-17), temper the "Sum.py is testable" claim (N-7), bump "Last Updated". |
| **DOC-003** | Refresh `TEST_COVERAGE_REPORT.md` numbers (179 passing / 0 skipped / 7 modules) or archive it once CI reports coverage (NEW-5). |
| **DOC-004** | Add "Superseded by ANALYSIS.md (2026-07-12)" banners to `CODE_REVIEW.md` and `AUDIT.md`, or move both to `docs/archive/` (NEW-9). |
| **FEAT-003** | Extend v3's analysis with mean/median/min/max — small, fits the lesson. |
| **GH-002** | Repo metadata: add topics (`python`, `education`, `tutorial`, `ai-assisted-development`), disable unused wiki/projects, consider a social preview image. |

## Phase 4: Strategic Expansion

| Item | What / Why |
|---|---|
| **FEAT-001** | `SumImprovedby…v4`: CLI arguments (`argparse`) and file input — continues the progression narrative into new teaching territory. |
| **FEAT-002** | `tutorial.ipynb` walking the v1→v2→v3 diffs with commentary (AUDIT DIR-2). Highest educational payoff of any expansion. |
| **GH-003** | Branch protection on `main` (require CI green) once GH-001 is stable; tag `v1.0` to mark the audited, stabilized state. |

## Exploratory Ideas (validate before committing)

- **Multi-problem AI benchmark** (AUDIT DIR-1): generalize "same prompt, many assistants" to
  FizzBuzz, etc., with published comparisons. Changes the repo's identity — prototype in a
  separate repo first, or decide via ARCH-002.
- **Doc↔file-set consistency checker** (N-6): a `scripts/check_variants.py` in CI. Only
  worth it if the variant count keeps growing.

## Deferred or Rejected Ideas

- **Web interface, database history, async summation, logging framework** (from CLAUDE.md's
  ideas list): rejected — operational complexity that teaches nothing about summation and
  dwarfs the 565-LOC core.
- **CONTRIBUTING.md / SECURITY.md / CODE_OF_CONDUCT.md / CHANGELOG.md**: deferred — single-
  owner educational repo; git history and README suffice until outside contributors appear.
- **Type-checking CI (mypy)**: deferred — only `demos/` is annotated; annotate first or not
  at all.
- **Renaming the repository**: deferred pending ARCH-002; a rename breaks inbound links for
  marginal benefit.

## Documentation Plan (dependency order)

1. DOC-001 license decision → edit `LICENSE` and/or README+CLAUDE.md license lines.
2. DOC-005 source docstrings/headers (independent, can land with Phase 1 code fixes).
3. ARCH-002 mission decision → README lead paragraph.
4. DOC-002 CLAUDE.md refresh (after ARCH-001/TEST-001 change the file/test tables it documents).
5. DOC-003 TEST_COVERAGE_REPORT refresh-or-archive (after TEST-001..004 settle final counts).
6. DOC-004 supersede banners on CODE_REVIEW.md / AUDIT.md (anytime; cheap).

## GitHub Improvement Plan

- **Now:** topics; disable unused wiki/projects (manual, Settings → General).
- **Phase 2:** CI workflow (GH-001); dependabot for actions (GH-004).
- **Phase 4:** branch protection requiring CI (GH-003); first release tag `v1.0`.
- **Manual-only checklist** (not API-accessible this session): social preview image, funding
  config, rulesets review.

## Branch Cleanup Plan

- **Safe to delete now:** none — remote already clean (only `main`).
- **Review before deletion:** none.
- **Keep:** `main` (default); `claude/repository-audit-roadmap-turb0r` until its PR merges,
  then delete the remote branch as normal PR hygiene.
- **Rename or migrate:** none — default branch is already `main`; `master` already removed.
- **Manual GitHub action required:** none for branches.

## Milestone Table

| ID | Initiative | Priority | Effort | Dependencies | Target Phase | Success Criteria |
|---|---|---|---|---|---|---|
| DOC-001 | Reconcile license (GPL v3 vs docs) | Critical | XS (after decision) | Owner decision | 0 | `LICENSE`, README, CLAUDE.md agree; GitHub badge matches README |
| BUG-001 | Fix `show_two_number_demo` crash | Critical | XS | — | 0 | Single-number input retries instead of crashing; regression test passes |
| BUG-002 | Fix `sys.path.append(".")` | High | XS | — | 1 | File imports demos from any cwd |
| ARCH-001 | Resolve duplicate ChatGPT file(s) | High | S | Owner choice (rewrite vs delete) | 1 | No byte-identical files; docs describe reality |
| TEST-001 | Remove duplicate test module | High | XS | ARCH-001 decision | 1 | Each test exists once; suite still ≥ ~163 unique cases, green |
| TEST-002 | Test `get_number` (3 variants) | High | S | — | 1 | Coverage >0% on all three Claude variants |
| DX-001 | requirements-dev.txt + pyproject.toml | High | XS | — | 1 | Fresh clone: `pip install -r requirements-dev.txt && pytest` works |
| DOC-005 | Docstring + `# file:` header fixes | Medium | XS | — | 1 | ruff/grep confirm headers match filenames |
| GH-001 | CI workflow (pytest + ruff, 3.9–3.13) | High | S | DX-001 | 2 | Green check on PRs; badge in README |
| DX-002 | Fix 10 ruff findings + config | Medium | XS | — | 2 | `ruff check .` exits 0 |
| TEST-003 | Test source, not local copies | Medium | M | — | 2 | `test_analysis_functions`/`test_custom_implementations` import from source files |
| TEST-004 | Prune dead conftest fixtures | Medium | S | TEST-003 (may reuse some) | 2 | No unused fixtures/markers; suite green |
| TEST-005 | Document/test uncapped `count` | Low | XS | — | 2 | Docstring note + test exist |
| GH-004 | Dependabot for actions | Low | XS | GH-001 | 2 | Config present, first PR auto-opened on action update |
| ARCH-002 | Primary-mission decision + README lead | Medium | S | Owner decision | 3 | README first paragraph states one primary mission |
| DOC-002 | CLAUDE.md refresh | Medium | S | ARCH-001, TEST-001 | 3 | No stale claims; naming template correct |
| DOC-003 | Coverage report refresh/archive | Low | XS | TEST-001..004 | 3 | Report matches `pytest` output or is archived |
| DOC-004 | Supersede banners on old audits | Low | XS | — | 3 | Both files point to ANALYSIS.md |
| FEAT-003 | Stats in v3 analysis | Low | S | TEST-003 | 3 | New stats covered by tests |
| GH-002 | Topics, disable wiki/projects | Low | XS | Manual settings access | 3 | Topics visible on repo page |
| FEAT-001 | v4: CLI args + file input | Medium | M | ARCH-002 | 4 | New variant + tests + docs entry |
| FEAT-002 | Tutorial notebook | Medium | M | ARCH-002 | 4 | `tutorial.ipynb` renders on GitHub, walks v1→v3 |
| GH-003 | Branch protection + v1.0 tag | Low | XS | GH-001 | 4 | PRs require CI; release exists |

Effort scale: XS ≤ 30 min · S ≤ 2 h · M ≤ 1 day.

## Success Metrics

- `pytest tests/` green on a 3.9–3.13 CI matrix on every PR (currently: green locally only, no CI).
- `ruff check .` exits 0 (currently: 10 errors).
- Coverage >0% on **every** `Sum*.py` variant (currently: 0% on five of six).
- Zero byte-identical file pairs; zero duplicated test modules (currently: one of each).
- `LICENSE`, README, CLAUDE.md, and GitHub's license badge all agree (currently: contradictory).
- Fresh-clone setup is one documented command (currently: pytest undeclared).
- Interactive demos survive malformed input without tracebacks (currently: BUG-001 crash).
- Old planning docs carry superseded banners; ANALYSIS.md/ROADMAP.md are the live plan.

## Recommended Execution Order

1. **DOC-001** — get the license decision from the owner; apply the 3-line fix. *(blocked on a human decision; everything else can proceed meanwhile)*
2. **BUG-001** — fix the crash + regression test.
3. **DX-001** — requirements-dev.txt + pyproject.toml.
4. **GH-001** — CI workflow (so every later step lands under test).
5. **ARCH-001** — rewrite-or-remove `SumImprovedbyChatGPT.py`; decide `…ChatGPTv2.py`.
6. **TEST-001** — drop the duplicate test module.
7. **BUG-002, DOC-005, DX-002** — one small "hygiene" PR.
8. **TEST-002** — `get_number` tests.
9. **TEST-003 → TEST-004 → TEST-005** — source-truth tests, conftest prune, count note.
10. **ARCH-002 → DOC-002 → DOC-003 → DOC-004** — mission + documentation refresh.
11. **GH-002, GH-004** — metadata + dependabot.
12. **FEAT-003 → FEAT-001 → FEAT-002 → GH-003** — feature and release work as appetite allows.
