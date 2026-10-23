# Changelog

Changes to the template, checker, and process. Newest first.

## 2026-10-23 — Tighter sections, location-first Deliverables

- Read top to bottom: point forward to later sections, and check every `>` note against the rest of the spec before handoff.
- Title table: new **Figma File** row for the working design file; **Handoff Link** now means the final handoff artifact only.
- Problem Statement: two sentences — the concrete moment, then the question the user can't answer. Why it matters, statistics, and secondary users move to Additional Context.
- Deliverables: organized by location (existing or new), with each deliverable listed once beneath it. New "Location to be decided" pattern for features the designer places.
- Non-goals: one short line each; check them against every deliverable.
- Additional Context: opens with the why-it-matters material; no rationale that restates other sections; bold headings only for multi-sentence rationale.
- Data: plain terms (no coined terms), describe the data not the screen, worked-example tables.
- Example spec updated to match.

## 2026-10-06 — Initial release

- Template sections: Project Title, Problem Statement, User Stories, Audience, Deliverables, Success & Failure Criteria, Non-goals, Dependencies, Additional Context, Data, Constraints, Open Questions.
- `scripts/check_specs.py` checks every spec under `specs/` against the README's template.
- Pre-commit hook in `.githooks/`; turn it on with `git config core.hooksPath .githooks`.
- Filled-in example spec in `specs/_example/`.
