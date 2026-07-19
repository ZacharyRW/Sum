# Project Roadmap

**Source of truth:** Verified findings in [ANALYSIS.md](ANALYSIS.md), audited 2026-07-14.

**Planning boundary:** This roadmap does not authorize a broad refactor, branch deletion, history rewrite, release, issue closure, or GitHub settings change. A 2026-07-17 `git fetch --prune origin` confirmed that local `master` is fully merged into `origin/main` (0 unique commits; 9 commits behind), so future implementation should start from fresh `main`.

## Roadmap Principles

Prioritize work by:

1. User impact and correctness before feature growth.
2. Legal, security, data-integrity, and repository-source-of-truth risk before cosmetic cleanup.
3. Explicit dependency order: decide the canonical product/architecture before moving or deleting variants.
4. Directly tested behavior over test count or historical coverage claims.
5. Reproducible local tooling before required CI/protection rules.
6. Small, reviewable changes that preserve historical teaching artifacts.
7. A clear distinction between verified defects, maintenance work, committed plans, optional enhancements, and speculative directions.

Each implementation change should begin from a fresh, clean `main` worktree, use focused commits, and update the canonical tracker rather than copying stale checklists forward.

## Phase 0: Immediate Safety and Repository Hygiene

### Decision and source-of-truth gate

- **GH-005 — Completed 2026-07-17: reconcile the stale local clone with GitHub `main`.** A fresh fetch/prune confirmed `master` has no unique commits and `origin/master` is absent. Do not delete the active local `master` worktree automatically; start new implementation branches from current `main`.
- **DOC-001 — Completed locally 2026-07-18: resolve the GPL-3.0/Apache-2.0 contradiction.** The maintainer selected GPL-3.0; `LICENSE`, README, and repository guidance now agree. Verify any GitHub metadata before claiming remote alignment.
- **SEC-001 — Record security closure.** No confirmed exploitable security defect requires emergency code remediation. Keep this result scoped to the local CLI; reassess if file, network, web, plugin, or persistence functionality is added.

### Immediate behavior repair

- **BUG-001 — Completed locally 2026-07-18: fix the two-number demo contract.** `show_two_number_demo()` now retries with a friendly message until exactly two integers are supplied; a direct regression test covers a one-number attempt.

**Exit criteria:** Fresh `main` is identified as the implementation base; intended license is recorded; the one-number crash has a direct failing-then-passing regression test; no user work or unmerged branch is discarded.

## Phase 1: Stabilization

### Correctness and reliability

- **BUG-004 — Completed locally 2026-07-18: preserve strict-integer precision.** Integer mode returns exact `int` values; direct tests cover values above `2**53`.
- **BUG-005 — Completed locally 2026-07-18: handle EOF cleanly.** Interactive input helpers return from the current demo with a user-facing message when standard input closes.
- **UX-001 — Completed locally 2026-07-18: define the numeric contract.** Float prompts accept finite values only; `nan`, `inf`, and `-inf` are rejected and the rule is documented and tested.
- **TEST-005 — Completed locally 2026-07-18: define a count limit.** Count-based Claude v2/v3 demos reject counts outside 1–100 before prompting for values.
- **BUG-002 — Completed locally 2026-07-18: remove fragile path manipulation.** The root pytest-style historical module no longer mutates `sys.path`.
- **BUG-003 — Completed locally 2026-07-18: remove redundant integer casts.** Count input returns an `int` in integer mode and callers pass it directly.

### Direct evidence tests

- **TEST-002 — Completed locally 2026-07-18: test every Claude `get_number` variant directly.** Mocked-input tests cover retry, integer-only values, finite floats, negative values, and EOF.
- **TEST-003 — Completed locally 2026-07-18: stop testing local reimplementations.** `custom_sum` and `analyze_numbers` are extracted source helpers and their tests import them directly.

### Documentation corrections that unblock use

- **DOC-005 — Completed locally 2026-07-18: correct copied headers and misleading docstrings.** Corrected the integer-only v1 docstring and replaced mismatched copied file headers.
- Correct README and CLAUDE license statements immediately after DOC-001 is decided; do not make other broad prose claims until tests and architecture are settled.

**Exit criteria:** Reproduced correctness/reliability defects have direct passing tests; input semantics are documented; no test claims coverage of a local copy instead of the implementation it purports to validate.

## Phase 2: Maintainability and Developer Experience

### Architecture decision and cleanup

- **ARCH-002 — Completed locally 2026-07-18: choose the primary identity.** Sum is a concise Python summation tutorial that retains historical AI-assisted variants for comparison and provenance.
- **ARCH-001 — Completed locally 2026-07-19: establish the canonical implementation.** `demos/summing_methods.py` is the canonical reusable lesson; historical examples now live in `history/`, and `history/chatgpt_v1_entrypoint.py` delegates to the canonical lesson.
- Move input, summation, and statistics into testable pure functions only after the canonical structure is agreed.

### Test and tooling hygiene

- **TEST-001 — Completed locally 2026-07-18: consolidate duplicate core tests.** Removed the collected duplicate module; `tests/test_summation_methods.py` is the single active core arithmetic suite, while the root-level ChatGPT v2 snapshot remains explicitly non-collected.
- **TEST-004 — Completed locally 2026-07-18: remove unused fixtures and markers.** Deleted the unconsumed fixture catalogue and marker registrations; active tests use only direct parametrization and fixtures local to their test modules.
- **DX-001 — Completed locally 2026-07-18: declare the development environment.** `pyproject.toml` declares Python 3.9+ and test/lint configuration; `requirements-dev.txt` declares pytest, pytest-cov, and Ruff; README documents the install and check commands.
- **DX-002 — Completed locally 2026-07-18: establish a current lint baseline.** Ruff 0.15.22 runs cleanly from the declared environment after removing path mutations and unused imports; do not rely on the old “10 findings” count.
- Add a minimal formatter/type-check policy only if it fits the canonical Python version and code style.

### Automation and documentation

- **GH-001 — Implemented locally 2026-07-18; remote verification pending.** The workflow installs the declared dependencies and runs pytest plus Ruff on Python 3.9, 3.11, and 3.14. Verify an Actions run after pushing.
- **GH-004 — Implemented locally 2026-07-18; remote verification pending.** Dependabot is configured for the declared pip dependencies and GitHub Actions. Verify it after the configuration reaches the default branch.
- **DOC-002 — Completed locally 2026-07-18: refresh agent guidance and public documentation.** README and `AGENTS.md` identify the canonical lesson, distinguish it from historical variants, and document the active core-test suite; `CLAUDE.md` remains a Claude-specific pointer.
- Create `CONTRIBUTING.md`, `SECURITY.md`, and `docs/testing.md` after the command baseline is known.

**Exit criteria:** A new contributor can install one declared toolchain, run the same checks locally and in CI, understand which implementation is canonical, and distinguish historical documents from current guidance.

## Phase 3: Product Improvements

These are optional user-facing improvements that fit the existing educational identity. Start only after Phases 0–2 exit criteria are met.

- **FEAT-003 — Extract and present number statistics.** Provide a pure function for count, positive/negative/zero groups, and totals; keep menu presentation thin. Value: demonstrates separation of concerns and enables direct tests. Complexity: small once ARCH-001 is complete.
- **FEAT-001a — Add documented command-line arguments.** Support a simple one-shot sum without interactive prompts. Value: makes examples scriptable. Complexity: small-to-medium; depends on UX-001, BUG-005, DX-001, and canonical CLI ownership.
- **FEAT-001b — Consider strict file input.** Only after arguments are stable. Define format, maximum size, encoding, errors, and finite-number policy. Complexity: medium; changes the security/resource model and needs renewed security review.
- **FEAT-002 — Create a tutorial notebook or narrative lesson.** Value: makes the evolutionary educational story legible. Complexity: medium; depends on ARCH-002 and accurate docs.
- Add compact README usage transcripts rather than a UI redesign. A screenshot/video is optional only if it materially improves discovery.

**Exit criteria:** Each feature has a documented user problem, a direct test path, and does not blur the canonical-vs-historical variant distinction.

## Phase 4: Strategic Expansion

These directions are possible but require an explicit product decision and a separate architecture/threat-model review.

- **STRAT-001 — AI assistant comparison corpus.** Capture prompt, model/tool context, immutable source snapshot, evaluation rubric, and provenance for multiple implementation variants. Value: turns current history into a reusable learning artifact. Complexity: high; it is more than a summation tutorial.
- **STRAT-002 — Multi-exercise learning collection.** Expand to other small programming tasks only if the project chooses the comparison/tutorial platform identity. Complexity: high; requires a new content model and release process.
- **STRAT-003 — Release/distribution model.** Add tags, releases, changelog discipline, and potentially a package only after users need installation rather than source reading.

## Exploratory Ideas

These are not committed backlog items. Validate them with a small written proposal or prototype first.

- Property-based tests for numeric contracts and parser edge cases.
- A benchmark lesson that teaches trade-offs among `sum`, `reduce`, and `math.fsum` without presenting educational variants as universal performance advice.
- A one-page comparison matrix showing purpose, behavior, and test status for historical variants.
- GitHub Pages documentation only if the tutorial/comparison direction gains enough material to justify it.

For each exploratory item, define target reader, expected learning value, maintenance cost, and exit/stop condition before implementation.

## Deferred or Rejected Ideas

| Idea | Decision | Reason |
| --- | --- | --- |
| Web service / Flask / FastAPI interface | Deferred | Adds deployment, network, input-validation, and security complexity without serving the present educational goal. |
| Database/history persistence | Deferred | No current user need; introduces state, privacy, migration, and release obligations. |
| Authentication, accounts, or cloud hosting | Rejected for current scope | Fundamentally changes the local CLI threat model and project identity. |
| Async summation | Rejected for current scope | Misleading for the CPU-bound, tiny educational calculations here. |
| Automatic deletion of branches | Rejected now | Local/remote refs are stale and one local branch has unmerged history. |
| Broad refactor during audit | Rejected | Must follow ARCH-002 and a fresh `main` reconciliation. |

## Documentation Plan

1. **DOC-001:** Record the intended license and make `LICENSE`, README, and `AGENTS.md` agree.
2. **DOC-005:** Correct concrete code headers/docstrings while behavior tests are added.
3. **DOC-002:** Refresh README and `AGENTS.md` around the selected canonical implementation and accurate test scope; keep `CLAUDE.md` Claude-specific.
4. **DOC-003 / DOC-004 (complete 2026-07-17):** Review findings from the historical audit, code review, and coverage report; reconcile material items into `ANALYSIS.md` and this roadmap; then remove the stale reports. Publish only CI-backed test evidence thereafter.
5. Create `CONTRIBUTING.md`, `SECURITY.md`, and `docs/testing.md` from the actual declared toolchain and CI commands.
6. Add `docs/architecture.md` only after ARCH-001/ARCH-002 are accepted; do not document a speculative structure as current fact.

## GitHub Improvement Plan

1. **GH-005:** Use fresh `main` for future implementation branches; retain local `master` until its active worktree is moved safely.
2. Coordinate with open PR #35 (DX-002) and #36 (DOC-005) before duplicating their scopes.
3. **GH-001 / DX-001:** Add declared tooling and a minimal CI workflow; verify it on a branch before requiring it.
4. **GH-002:** Manually review and improve description, URL, topics, social preview, README presentation, demo links, wiki/discussions/projects choice, and release visibility. Record exact settings changed separately from code commits.
5. Add issue forms/templates and a pull-request template when contribution flow is documented.
6. **GH-004:** Add Dependabot for declared ecosystems only.
7. **GH-003:** After CI proves stable, configure branch protection/rulesets, required checks, and a release/tag policy. Do not assume current settings.

## Branch Cleanup Plan

### Safe to delete now

None. `origin/master` was pruned as a stale local tracking ref on 2026-07-17; that was not deletion of a local or remote branch.

### Review before deletion

| Ref | Required evidence before action |
| --- | --- |
| Local `master` | Move the active worktree safely to `main` and explicitly confirm the legacy local branch is no longer needed. It has no unique commits. |
| Any newly discovered remote branch | Confirm no open PR, no unique commits, no active worktree/user, and safe recoverability from `main`. |

### Keep

| Branch | Reason |
| --- | --- |
| GitHub `main` | Current default and canonical public branch. |
| Current local `master` | Active legacy checkout with no unique commits until the worktree is moved to `main`. |

### Rename or migrate

- GitHub needs no default-branch rename: `main` is already default.
- GH-005 has confirmed that a local migration can start from fresh `main` without preserving a `master`-only commit. Update README badges, workflow references, deployment scripts, and external integrations only if a fresh search finds a `master` dependency.

### Manual GitHub action required

- Verify default-branch settings, protection/rulesets, required checks, deployment integration, and stale-branch state in the GitHub UI/API after CI is added.
- Do not delete remote branches or change branch protection as part of documentation work.

## Milestone Table

| ID | Initiative | Priority | Effort | Dependencies | Target phase | Success criteria |
| --- | --- | --- | --- | --- | --- | --- |
| GH-005 | Reconcile stale local clone with `main` | Complete | S | Network access; review of divergence | 0 | Completed 2026-07-17: fresh refs, no lost local commit, and `master` confirmed fully merged. |
| DOC-001 | Resolve license contradiction | Complete locally | S | Maintainer decision | 0 | GPL-3.0 selected; `LICENSE`, README, and repository guidance agree. Verify GitHub metadata before declaring remote alignment. |
| BUG-001 | Fix one-number demo crash | Complete locally | S | Fresh implementation base | 0 | One-number input retries/messages cleanly; direct regression test added. |
| SEC-001 | Preserve security-scope closure | P1 | S | None | 0 | Security posture accurately documented; renewed review gate exists for new I/O/network features. |
| BUG-004 | Preserve integer precision | Complete locally | S | Numeric contract decision | 1 | Integer mode retains exact `2**53`-range values; direct regression test passes. |
| BUG-005 | Handle EOF | Complete locally | S | Canonical input helper | 1 | Closed stdin exits without traceback; direct tests pass. |
| UX-001 | Define finite-number and count policy | Complete locally | S | Product behavior decision | 1 | Float input rejects NaN/Inf and count-based prompts accept 1–100; both are documented and tested. |
| TEST-002 | Direct Claude input tests | Complete locally | M | Testable input seam | 1 | Each variant has real mocked-input retry, numeric-contract, and EOF tests. |
| TEST-003 | Replace local-copy tests | Complete locally | M | ARCH-001 | 1 | Tests import and exercise extracted source helpers. |
| BUG-002 | Remove path hack | Complete locally | S | DX-001 or package decision | 1 | Root historical test module no longer uses `sys.path.append(".")`. |
| BUG-003 | Remove redundant casts | Complete locally | S | Tests/type contract | 1 | No redundant count casts remain. |
| ARCH-002 | Choose project identity | Complete locally | S | Maintainer decision | 2 | Sum is a concise Python summation tutorial with historical AI-assisted variants. |
| ARCH-001 | Establish canonical variant | Complete locally | M | ARCH-002 | 2 | `demos/summing_methods.py` is canonical; `history/` preserves renamed historical examples and the ChatGPT entry point delegates to it. |
| TEST-001 | Consolidate duplicate tests | Complete locally | S | Passing direct-test baseline | 2 | The collected duplicate module is removed; one active core arithmetic suite remains. |
| TEST-004 | Clean fixtures/markers | Complete locally | S | Passing test baseline | 2 | The unused fixture catalogue and unconsumed marker registrations were removed. |
| DX-001 | Declare toolchain | Complete locally | S | Supported Python decision | 2 | `pyproject.toml`, `requirements-dev.txt`, and README declare a Python 3.9+ toolchain and documented checks. |
| DX-002 | Establish Ruff baseline | Complete locally | S | DX-001 | 2 | Ruff 0.15.22 exits cleanly in the declared environment. |
| GH-001 | Add CI | Ready for remote verification | M | DX-001, direct tests | 2 | Workflow runs documented checks on Python 3.9, 3.11, and 3.14 after push. |
| GH-004 | Add Dependabot | Ready for remote verification | S | DX-001, GH-001 | 2 | Configuration covers pip and GitHub Actions after it reaches the default branch. |
| DOC-002 | Refresh README and agent guidance | Complete locally | M | DOC-001, ARCH-001, test baseline | 2 | Public docs and `AGENTS.md` match the canonical lesson, historical variants, commands, and test scope; `CLAUDE.md` remains Claude-specific. |
| DOC-003 | Retire stale coverage report | Complete | S | Review reconciliation | 0 | Completed 2026-07-17: material claims were assessed in `ANALYSIS.md`, then the stale static report was removed. Future evidence must be CI-generated. |
| DOC-004 | Retire stale audit and code review | Complete | S | Review reconciliation | 0 | Completed 2026-07-17: material findings were reconciled into `ANALYSIS.md` and this roadmap, then both stale reports were removed. |
| DOC-005 | Correct local headers/docstrings | Complete locally | S | BUG/TEST stabilization | 1 | Source comments and docstrings name the correct file/behavior. |
| GH-002 | Improve public repository presentation | P2 | S | ARCH-002, DOC-002 | 2 | Description/topics/presentation reviewed and recorded. |
| GH-003 | Protection and releases | P2 | S | GH-001 | 2 | Required checks/protection/release policy configured and documented. |
| FEAT-003 | Add statistics lesson | P3 | M | ARCH-001, TEST-003 | 3 | Pure stats API and UI example have direct tests/docs. |
| FEAT-001a | Add CLI args | P3 | M | UX-001, DX-001 | 3 | One-shot command is documented, tested, and handles invalid/EOF input. |
| FEAT-001b | Add file input | P3 | M | FEAT-001a, renewed security review | 3 | Strict format/limits/errors/security behavior is defined and tested. |
| FEAT-002 | Tutorial notebook | P3 | M | ARCH-002, DOC-002 | 3 | Notebook tells an accurate, maintained learning story. |
| STRAT-001 | AI comparison corpus | Exploratory | L | ARCH-002; provenance proposal | 4 | Maintainer accepts a durable comparison model before expansion. |

## Success Metrics

Measure improvement with evidence, not just checklist completion:

- A clean clone/venv can install declared tools and run one documented validation command successfully.
- CI runs the same suite on each proposed change and reports a clear pass/fail result.
- BUG-001, BUG-004, BUG-005, and the chosen count/finite-number policy have direct regression tests.
- No duplicate production implementation is described as independent without provenance.
- Every retained test fixture/marker and test file has a meaningful, direct purpose.
- README, `AGENTS.md`, LICENSE, and GitHub metadata agree on project purpose, license, and canonical usage.
- Material findings from retired reports are captured in `ANALYSIS.md`; the roadmap is the one accepted current tracker.
- Default `main` has required checks only after those checks are reliable.
- Zero reportable security findings remain for the local CLI scope; any new external I/O feature triggers a scoped security review.

## Recommended Execution Order

1. Start any implementation work from fresh GitHub `main`; do not delete the active legacy worktree as part of this documentation PR.
2. Coordinate with open PR #35 (DX-002) and #36 (DOC-005) to avoid duplicate scope.
3. Obtain the license decision and align the legal/public source of truth.
4. Add failing tests for the one-number crash and large-integer precision loss; implement only those narrow fixes.
5. Decide/implement EOF, finite-number, and count behavior with tests.
6. Make the maintainer decision on project identity and canonical variant.
7. Extract/directly test the agreed core; remove only proven duplicate tests and fixtures.
8. Declare Python/dev tooling, then run and fix the actual lint/type/test baseline.
9. Add minimal CI; verify it before Dependabot, protection, or release changes.
10. Refresh README and `AGENTS.md` after the canonical variant and test baseline are settled.
11. Select at most one Phase 3 feature based on the chosen identity and demonstrated maintenance capacity.
