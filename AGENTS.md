# Sum Repository Agent Guide

## Purpose and scope

Sum is an educational Python repository demonstrating summation techniques and preserving AI-assisted implementation iterations. Treat the variants as teaching artifacts unless a maintainer explicitly designates a canonical implementation.

## Authoritative sources

- Current code and `LICENSE` are authoritative for behavior and licensing. The repository currently contains the GPL-3.0 license text.
- `ANALYSIS.md` is the current dated assessment; `ROADMAP.md` is the current execution tracker.
- `README.md`, this guide, and generated reports must not make claims that conflict with current code, tests, or `LICENSE`.
- Historical audit, review, and coverage reports were reviewed and removed on 2026-07-17. Do not recreate their stale test counts or coverage estimates as current evidence.

## Repository layout

- `Sum.py`: original two-number CLI example.
- `SumImprovedbyClaudeCode*.py`: historical Claude iterations.
- `SumImprovedbyChatGPT*.py`: historical ChatGPT iterations; `SumImprovedbyChatGPT.py` currently duplicates `demos/summing_methods.py`.
- `demos/summing_methods.py`: reusable summation functions and the strongest candidate for a future canonical core.
- `tests/`: pytest suite.

## Working conventions

- Inspect current code, `ANALYSIS.md`, and `ROADMAP.md` before proposing or implementing work.
- Preserve historical variants unless the request explicitly authorizes moving, deleting, or rewriting them.
- Add focused regression tests for behavior changes. Do not claim coverage for a source function when a test exercises a local copy instead.
- Keep documentation repository-relative and avoid volatile assertions about test counts, line counts, coverage percentages, or branch state unless freshly verified.
- Use clear docstrings, type hints where they improve the lesson, PEP 8 formatting, and user-facing validation/error messages.
- Do not shadow built-ins such as `sum`.

## Current caution points

- The `LICENSE` is GPL-3.0 while public documentation may still contain older Apache-2.0 claims; resolve this through an explicit maintainer decision.
- `show_two_number_demo()` has a confirmed one-number input crash, and integer parsing currently loses precision above `2**53`.
- EOF handling, finite-number behavior, and input-count limits are not yet defined consistently.
- The suite contains duplicate and indirect tests. Treat historical test/coverage claims as non-authoritative until a declared toolchain and CI produce current results.

## Verification and Git

- Run the repository’s declared checks when available; at present there is no declared dependency manifest or CI workflow.
- Before making Git claims, check `git branch --show-current`, `git rev-parse --short HEAD`, and `git status --short`.
- Push only when explicitly requested. Confirm the branch and staged scope immediately before committing or pushing.
