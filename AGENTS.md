# Sum Repository Agent Guide

## Purpose and scope

Sum is an educational Python summation tutorial that preserves AI-assisted implementation iterations as teaching artifacts. `demos/summing_methods.py` is the canonical reusable lesson; the root-level variants are historical, runnable examples unless their own documentation says otherwise.

## Authoritative sources

- Current code and `LICENSE` are authoritative for behavior and licensing. GPL-3.0 is the maintainer-selected license.
- `ANALYSIS.md` is the current dated assessment; `ROADMAP.md` is the current execution tracker.
- `README.md`, this guide, and generated reports must not make claims that conflict with current code, tests, or `LICENSE`.
- Historical audit, review, and coverage reports were reviewed and removed on 2026-07-17. Do not recreate their stale test counts or coverage estimates as current evidence.

## Repository layout

- `Sum.py`: original two-number CLI example.
- `demos/summing_methods.py`: canonical reusable summation functions and interactive lesson.
- `SumImprovedbyClaudeCode*.py`: historical, independently runnable Claude iterations.
- `SumImprovedbyChatGPT.py`: historical ChatGPT entry point that delegates to the canonical lesson.
- `SumImprovedbyChatGPTv2.py`: historical pytest snapshot; it is deliberately not collected.
- `tests/`: pytest suite; `test_summation_methods.py` is the single active core arithmetic suite.

## Working conventions

- Inspect current code, `ANALYSIS.md`, and `ROADMAP.md` before proposing or implementing work.
- Preserve historical variants unless the request explicitly authorizes moving, deleting, or rewriting them. Keep their provenance labels accurate when the canonical lesson changes.
- Add focused regression tests for behavior changes. Do not claim coverage for a source function when a test exercises a local copy instead.
- Keep documentation repository-relative and avoid volatile assertions about test counts, line counts, coverage percentages, or branch state unless freshly verified.
- Use clear docstrings, type hints where they improve the lesson, PEP 8 formatting, and user-facing validation/error messages.
- Do not shadow built-ins such as `sum`.

## Current caution points

- The suite contains duplicate and indirect tests. Treat historical test/coverage claims as non-authoritative until a declared toolchain and CI produce current results.

## Verification and Git

- Install the declared development tools with `python -m pip install -r requirements-dev.txt`, then run `python -m pytest tests/` and `ruff check .`. There is no CI workflow yet.
- Before making Git claims, check `git branch --show-current`, `git rev-parse --short HEAD`, and `git status --short`.
- Push only when explicitly requested. Confirm the branch and staged scope immediately before committing or pushing.
