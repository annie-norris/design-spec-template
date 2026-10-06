# Changelog

Changes to the template, checker, and process. Newest first.

## 2026-10-06 — Initial release

- Template sections: Project Title, Problem Statement, User Stories, Audience, Deliverables, Success & Failure Criteria, Non-goals, Dependencies, Additional Context, Data, Constraints, Open Questions.
- `scripts/check_specs.py` checks every spec under `specs/` against the README's template.
- Pre-commit hook in `.githooks/`; turn it on with `git config core.hooksPath .githooks`.
- Filled-in example spec in `specs/_example/`.
