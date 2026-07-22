# Project Roadmap

**Derived from:** `ANALYSIS.md` audited 2026-07-21 at `009058c`.
**Principle:** prioritize verified user-contract failures and release-confidence gaps before optional features; preserve historical artifacts unless a change explicitly selects them.

## Roadmap Principles

Order work by learner impact, risk reduction, evidence strength, effort, dependency order, and fit with the small local-tutorial identity. Completed historical work is not backlog. Speculative product directions remain exploratory until a maintainer selects them.

## Phase 0: Immediate Safety and Repository Hygiene

No critical security issue, broken test suite, unsafe branch, or default-branch migration is required. Keep `main` as default and do not delete branches: the only current branch is synchronized `main`.

## Phase 1: Stabilization

- **TEST-001:** Correct integer-mode test expectations to assert both values and `int` types; preserve the exact-large-integer case.
- **DOC-002:** State the current package-build decision in README/developer guidance: either supported distribution or tutorial-only tooling metadata.
- **NB-001:** Execute `notebooks/historical_progression.ipynb` on a normal host/CI runner and record a reproducible result.

## Phase 2: Maintainability and Developer Experience

- **PKG-001:** If distribution support is intended, add a build frontend/backend to the development validation path and build wheel+sdist in CI. Otherwise deliberately narrow/remove packaging expectations.
- **DX-001:** Decide formatting scope for historical Python and the notebook; enforce the chosen Ruff format policy in CI.
- **CI-001:** Add the chosen build/format/notebook checks only after they are deterministic and their support policy is documented.
- **TEST-002:** Separate canonical-contract tests from historical demonstration tests in documentation and, if useful, pytest markers; use coverage for the maintained module rather than an aggregate historical percentage.

## Phase 3: Product Improvements

- **FEAT-001:** Add a brief precision lesson comparing builtin `sum`, `reduce`, and `math.fsum`, with a small reproducible example.
- **FEAT-002:** Add property-based tests only if the educational value exceeds setup complexity; retain clear deterministic examples.

## Phase 4: Strategic Expansion

No expansion is committed. Hosted lessons, file input, network integrations, publishing automation, or web UI require a selected audience, maintenance owner, and a new security review.

## Exploratory Ideas

- A concise contributor guide if outside contributions become active.
- A `SECURITY.md` that states the local-only threat model and security reporting route before the attack surface grows.
- An intentional release/checklist process if versioned distributions are actually published.

## Deferred or Rejected Ideas

- File input: defer until format, encoding, size/count bounds, finite-number policy, error behavior, and a security review are approved.
- Automatic releases/dependency merging: do not add without an explicit release ownership policy.
- Reformatting history: do not do it as cleanup unless maintainers choose archival uniformity over literal historical presentation.

## Documentation Plan

1. Complete `TEST-001` and write the exact numeric contract.
2. Decide `PKG-001`; update README/setup instructions with the verified path.
3. Decide `DX-001`; document historical-code formatting scope.
4. Add `CONTRIBUTING.md`, `SECURITY.md`, changelog, or release guide only when their corresponding workflow exists.

## GitHub Improvement Plan

Manual GitHub review is required because authentication was unavailable: verify description/topics/social preview, open Issues and PRs (including whether completed notebook/statistics issues remain open), branch protection and required checks, Actions status, releases/tags, templates, and Dependabot alerts. Keep workflow permissions minimal. After `PKG-001`/`DX-001`, add only validated checks to the required-check policy.

## Branch Cleanup Plan

| Category | Action |
| --- | --- |
| Safe to delete now | None. |
| Review before deletion | None visible locally. |
| Keep | `main`, synchronized with `origin/main`. |
| Rename or migrate | None; default branch is already `main`. |
| Manual GitHub action required | Verify remote default/branch protection because local refs cannot prove settings. |

## Milestones

| ID | Initiative | Priority | Effort | Dependencies | Target phase | Success criteria |
| --- | --- | --- | --- | --- | --- | --- |
| TEST-001 | Assert exact integer type contract | High | S | None | 1 | Integer parser tests fail if values become floats. |
| NB-001 | Verify notebook on socket-capable host | Medium | S | Normal host/CI | 1 | Documented nbconvert command exits 0. |
| PKG-001 | Decide and validate package build | High | S-M | Maintainer decision | 2 | Wheel/sdist build is either green in CI or intentionally unsupported. |
| DX-001 | Establish formatting policy | Medium | S | Maintainer decision | 2 | `ruff format --check` is green for selected scope. |
| CI-001 | Align CI with supported validation | Medium | S | PKG-001/DX-001/NB-001 | 2 | Required checks match documented support. |
| FEAT-001 | Explain numeric precision tradeoffs | Low | S | None | 3 | Lesson includes tested, readable comparison. |

## Success Metrics

- All tests pass and integer type assertions protect the documented contract.
- Every documented setup/build command is reproducibly green on a supported host.
- CI runs every validation the project claims to enforce.
- `main` remains clean and synchronized; no unverified branch deletion.
- Planning documents are updated whenever selected work changes canonical behavior.

## Recommended Execution Order

1. Implement and verify TEST-001.
2. Decide whether the project is a distributable package; execute PKG-001 accordingly.
3. Run the notebook command outside this sandbox and choose its CI policy.
4. Decide formatting treatment for historical files, then implement DX-001/CI-001.
5. Re-authenticate GitHub CLI and perform the manual settings/issue review.
6. Select at most one Phase 3 improvement.
