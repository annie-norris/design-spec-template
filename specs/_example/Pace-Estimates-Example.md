# Stride · Product Design (fictional example)

## Pace Estimates — Design Spec

> This is a made-up example showing a filled-in spec. Stride is not a real product. Delete this folder once you no longer need it.

| Field | Value |
| :---- | :---- |
| Last Updated | 2026-10-06, Example Designer |
| Sprint | 2026-10-12 - 2026-10-23 |
| Ticket | STR-412 (Pace Estimates section, all deliverables) |
| Contextual Documents | None yet — deliberate; no prior research exists for this feature |
| Research Status | Definition |
| Handoff Due Date | 2026-10-23 |
| Handoff recipient | Web and mobile app developers |
| Handoff Link | Link to the current design file |

| Role | Status |
| :---- | :---- |
| Project Manager | Handed off brief |
| Designer | Started |
| Developer | TBD |

## Problem Statement

After a strong training run, runners regularly ask coaches and club-mates what that effort would mean at another race distance, and the answers they get are inconsistent guesses. Runners can't plan race goals with confidence, coaches field the same question again and again, and club members comparing results have no shared reference point. Competitor apps already show this, and it is one of the most requested features in Stride's feedback channel.

## User Stories

- As a runner, I want to see what a training run suggests about my pace at other race distances, so I can set realistic race goals
- As a coach, I want my runners to see the same estimate I would give them, so I spend less time answering it by hand
- As a member, I want to see estimates on runs other runners have shared, so I can compare progress on equal terms

> Club admins are not listed — the source notes don't mention them. Confirm with PM whether that's deliberate.

## Audience

| Hierarchy | User | Access |
| :---- | :---- | :---- |
| Primary | Anyone already able to see the activity (the runner, their coach, followers of a public activity) | Inherited from the activity — sees the section wherever they see the activity detail. Read-only; no new rule defined here |
| Tertiary | Anyone not able to see the activity | No access to the activity, so no access to its estimate |

## Deliverables

A collapsible Pace Estimates section at the bottom of the existing activity detail screen.

- New section added to an existing screen; nothing is replaced.
- **Collapsible section** — sits last in the activity detail, closed by default.
- **Estimate table** — the runner's actual time beside an estimated range for each other race distance.
- **Empty states** — one for activities that will never get an estimate, one for activities still waiting on one.

## Success & Failure Criteria

**Success looks like**
- A runner can read the range and correctly say it is an estimate, without help.
- Runners who never open the section are unaffected — it adds no clutter to the activity detail.
- A runner viewing an activity that is still waiting on an estimate understands it will appear later.

**Failure looks like**
- A runner reads the range as a guaranteed result or an official race time.
- An activity still waiting on an estimate is read as broken.
- A runner waits for an estimate on an activity that will never get one.

> No adoption target was stated — confirm with PM what level of use would count as success.

## Non-goals

- Not a change to how estimates are calculated — this displays an existing model's output.
- Not a training-plan or goal-setting feature.

## Dependencies

- **Estimate model (Data team)** — produces the ranges this section displays; the design depends on its output format staying as described in Data.
- **STR-388 Activity detail redesign** — this section is added to the redesigned screen, so its layout must be final first.

> Whether STR-388 will be final before this sprint starts is unconfirmed — check with PM.

## Additional Context

Pace estimates predict a finish-time range at other race distances from a single run. They are widely used in running apps, but some coaches think they are misleading because they ignore terrain, weather, and fatigue. That is why the section sits last and arrives closed — a runner finds it only if they go looking. The placement is a decision, not an oversight.

## Data

1. **It is a range, not a single time.**
- Example: 48:10–49:30 for a 10K
- A single number implies a precision the model does not have.
2. **Estimates arrive hours after the activity syncs.**
- The model runs on a schedule, so a freshly synced activity has no estimate yet.
3. **Some activities never get an estimate.**
- Walks, hikes, and runs under 1 mile are skipped by the model.

## Constraints

#### Timeline
- [ ] Handoff by 2026-10-23 so development can start in the following sprint.

#### Structural
- [x] The section sits last in the activity detail, below splits and the route map.
- [x] Estimates appear only in the activity detail — never on the feed, leaderboards, or profile.

#### States
- [x] Collapsed: the default, on every activity.
- [x] Expanded with an estimate: actual time and estimated ranges side by side.
- [x] Empty — will never be estimated (walks, hikes, short runs).
- [x] Empty — not estimated yet (normal for a few hours after sync).
- [x] The two empty states must read differently, and neither may be blank.

#### Access
- [x] Inherits the visibility of the activity; no access rules of its own.

#### Behavior
- [x] Read-only: nobody edits, shares, or exports an estimate.
- [x] The section expands and collapses in place and links nowhere.

#### Content
- [x] Every distance is labelled explicitly.
- [x] The range is shown exactly as delivered — no confidence percentage.
- [ ] Wording for both empty states is the designer's to write; get PM sign-off.

#### Platforms
- [x] Web app
- [x] Mobile app

## Open Questions

1. **Does the section need a disclaimer?**
- Some coaches see estimates as misleading, and nothing on screen says how the range is produced.
- Options: a one-line note under the table (always visible, adds clutter) or an info icon (cleaner, easy to miss).
- PM to decide whether a disclaimer is required; design with space for one so it doesn't have to be wedged in later.
