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
- **DOC-001 — Resolve the GPL-3.0/Apache-2.0 contradiction.** Treat `LICENSE` as the current legal source; obtain the maintainer's intended license before changing `LICENSE`, README, CLAUDE, badges, or release metadata.
- **SEC-001 — Record security closure.** No confirmed exploitable security defect requires emergency code remediation. Keep this result scoped to the local CLI; reassess if file, network, web, plugin, or persistence functionality is added.

### Immediate behavior repair

- **BUG-001 — Fix the two-number demo contract.** Make `show_two_number_demo()` request/validate exactly two values and give a friendly retry message rather than destructuring an undersized list.
- Add a focused regression test before considering the historical “179 tests” claim meaningful.

**Exit criteria:** Fresh `main` is identified as the implementation base; intended license is recorded; the one-number crash has a direct failing-then-passing regression test; no user work or unmerged branch is discarded.

## Phase 1: Stabilization

### Correctness and reliability

- **BUG-004 — Preserve strict-integer precision.** Do not convert valid integer input through `float`. Decide whether integer-mode APIs return `int` values and how `math.fsum` is presented when values exceed exact floating-point range. Add a `2**53` regression case.
- **BUG-005 — Handle EOF cleanly.** Catch `EOFError` at prompt boundaries and exit/return with a user-facing message. Test redirected/closed stdin behavior.
- **UX-001 — Define the numeric contract.** Decide whether `nan`, `inf`, and `-inf` are supported lessons or rejected calculator input. Document the rule and test it.
- **TEST-005 — Define a count limit or explicit non-interactive alternative.** A menu-driven prompt loop should reject unreasonable counts or avoid prompting one number at a time for batch use. Test the chosen boundary.
- **BUG-002 — Remove fragile path manipulation.** Eliminate the root `sys.path.append(".")` test-module workaround through proper packaging or repository-relative test discovery.
- **BUG-003 — Remove redundant integer casts.** Make the `get_number(..., allow_float=False)` return contract explicit and remove `int(count)` noise.

### Direct evidence tests

- **TEST-002 — Test every Claude `get_number` variant directly.** Use patched `input()` and cover valid, invalid-then-valid, integer-only, float, negative, and EOF cases as applicable.
- **TEST-003 — Stop testing local reimplementations.** Extract pure `custom_sum` and sign-breakdown helpers from v2/v3 or explicitly remove false-coverage tests until an extraction is accepted.

### Documentation corrections that unblock use

- **DOC-005 — Correct copied headers and misleading docstrings.** This includes the integer-only v1 docstring and mismatched `# file:` comments.
- Correct README and CLAUDE license statements immediately after DOC-001 is decided; do not make other broad prose claims until tests and architecture are settled.

**Exit criteria:** Reproduced correctness/reliability defects have direct passing tests; input semantics are documented; no test claims coverage of a local copy instead of the implementation it purports to validate.

## Phase 2: Maintainability and Developer Experience

### Architecture decision and cleanup

- **ARCH-002 — Choose the primary identity.** Select one: (a) a concise Python summation tutorial with historical AI variants, or (b) an AI-code-evolution comparison artifact. This is a maintainer decision gate, not an automatic refactor.
- **ARCH-001 — Establish a canonical implementation.** After ARCH-002, label `demos/summing_methods.py` as canonical, rewrite `SumImprovedbyChatGPT.py` as a real example, or move/archive the duplicate as a documented historical artifact. Preserve provenance.
- Move input, summation, and statistics into testable pure functions only after the canonical structure is agreed.

### Test and tooling hygiene

- **TEST-001 — Consolidate duplicate core tests.** Preserve unique cases, delete only a proven duplicate after current CI passes.
- **TEST-004 — Remove or purposefully use unused fixtures and markers.** Do not retain a fixture catalogue that no test consumes.
- **DX-001 — Declare the development environment.** Prefer a small `pyproject.toml` with supported Python versions and pytest/Ruff/type-check dependencies, or an equivalent documented requirements file. Match the command set to the actual project size.
- **DX-002 — Establish and fix a current lint baseline.** Run Ruff from the declared environment, capture exact output, then fix/remediate all agreed rules; do not rely on the old “10 findings” count.
- Add a minimal formatter/type-check policy only if it fits the canonical Python version and code style.

### Automation and documentation

- **GH-001 — Add minimal GitHub Actions CI.** Run syntax/tooling, pytest, Ruff, and any chosen type check on supported Python versions. Keep the workflow simple and deterministic.
- **GH-004 — Add Dependabot after dependencies and CI exist.** Configure only ecosystems actually declared.
- **DOC-002 — Refresh `CLAUDE.md`.** Make it a concise, accurate guide to the canonical variant, historical variants, commands, branch policy, and repository-relative paths.
- **DOC-003 — Retire the stale coverage report as a live claim.** Replace it with CI-generated evidence or move it to historical documentation.
- **DOC-004 — Mark old reviews as historical.** Add a short superseded banner to `AUDIT.md` and `CODE_REVIEW.md`; retain provenance rather than deleting them.
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

1. **DOC-001:** Record the intended license and make `LICENSE`, README, and CLAUDE agree.
2. **DOC-005:** Correct concrete code headers/docstrings while behavior tests are added.
3. **DOC-002:** Refresh README/CLAUDE around the selected canonical implementation and accurate test scope.
4. **DOC-003:** Move or label `TEST_COVERAGE_REPORT.md` as historical; publish only CI-backed results thereafter.
5. **DOC-004:** Add provenance-preserving historical banners to `AUDIT.md` and `CODE_REVIEW.md`.
6. Create `CONTRIBUTING.md`, `SECURITY.md`, and `docs/testing.md` from the actual declared toolchain and CI commands.
7. Add `docs/architecture.md` only after ARCH-001/ARCH-002 are accepted; do not document a speculative structure as current fact.

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
| DOC-001 | Resolve license contradiction | P0 | S | Maintainer decision | 0 | `LICENSE`, README, CLAUDE, and GitHub metadata agree. |
| BUG-001 | Fix one-number demo crash | P0 | S | Fresh implementation base | 0 | One-number input retries/messages cleanly; regression test passes. |
| SEC-001 | Preserve security-scope closure | P1 | S | None | 0 | Security posture accurately documented; renewed review gate exists for new I/O/network features. |
| BUG-004 | Preserve integer precision | P1 | S | Numeric contract decision | 1 | `2**53`-range input retains exact integer sum or is explicitly unsupported. |
| BUG-005 | Handle EOF | P1 | S | Canonical input helper | 1 | Closed stdin exits without traceback; direct test passes. |
| UX-001 | Define finite-number and count policy | P1 | S | Product behavior decision | 1 | NaN/Inf and large-count behavior is documented and tested. |
| TEST-002 | Direct Claude input tests | P1 | M | Testable input seam | 1 | Each supported variant has real mocked-input tests. |
| TEST-003 | Replace local-copy tests | P1 | M | ARCH-001 | 1 | Tests import/exercise source functions rather than replicas. |
| BUG-002 | Remove path hack | P2 | S | DX-001 or package decision | 1 | Tests run from documented working directories without `sys.path.append(".")`. |
| BUG-003 | Remove redundant casts | P3 | S | Tests/type contract | 1 | No redundant count casts remain; lint baseline is cleaner. |
| ARCH-002 | Choose project identity | P1 | S | Maintainer decision | 2 | One-sentence mission and canonical audience accepted. |
| ARCH-001 | Establish canonical variant | P1 | M | ARCH-002 | 2 | Duplicate variant is rewritten/labeled/archived; docs name one canonical path. |
| TEST-001 | Consolidate duplicate tests | P2 | S | Passing direct-test baseline | 2 | Duplicate suite removed or made meaningfully distinct. |
| TEST-004 | Clean fixtures/markers | P3 | S | Passing test baseline | 2 | Every retained fixture/marker is used or removed. |
| DX-001 | Declare toolchain | P1 | S | Supported Python decision | 2 | Fresh venv can install exact dev tools and run documented commands. |
| DX-002 | Establish Ruff baseline | P2 | S | DX-001 | 2 | Ruff output is zero or has explicitly accepted, documented exceptions. |
| GH-001 | Add CI | P1 | M | DX-001, direct tests | 2 | GitHub Actions runs documented checks reliably. |
| GH-004 | Add Dependabot | P3 | S | DX-001, GH-001 | 2 | Automated dependency PRs cover actual declared ecosystems. |
| DOC-002 | Refresh README/CLAUDE | P1 | M | DOC-001, ARCH-001, test baseline | 2 | Public docs match code, license, commands, and coverage scope. |
| DOC-003 | Retire stale coverage report | P2 | S | GH-001 | 2 | Historical report is labeled/moved; current evidence is CI-generated. |
| DOC-004 | Mark historical audits | P3 | S | ANALYSIS accepted | 2 | Old reports are retained with an explicit superseded marker. |
| DOC-005 | Correct local headers/docstrings | P2 | S | BUG/TEST stabilization | 1 | Source comments and docstrings name the correct file/behavior. |
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
- README, CLAUDE, LICENSE, and GitHub metadata agree on project purpose, license, and canonical usage.
- Old reports are visibly historical; the roadmap has one accepted current tracker.
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
10. Refresh README/CLAUDE and mark historical reports accurately.
11. Select at most one Phase 3 feature based on the chosen identity and demonstrated maintenance capacity.
