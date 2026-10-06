# Design Spec Template

A shared template and process for writing design specs (briefs) for product work. Use it to start your own private repo of specs, and suggest improvements to the template here.

## Getting started

1. Click **Use this template → Create a new repository** at the top of this page. Set the new repo to **Private**. Your client specs live only in your copy, so nobody else can see them.
2. Clone your new repo and turn on the spec check (once per clone):
   ```
   git config core.hooksPath .githooks
   ```
   Every commit then runs `scripts/check_specs.py` first and stops the commit if a spec doesn't match the template. You can also run it by hand with `python3 scripts/check_specs.py`.
3. Put your specs under `specs/`, one folder per client or project (e.g. `specs/Client Q3 2026/Feature-Spec.md`). See `specs/_example/` for a fully filled-in spec. Delete it once you no longer need it.
4. To draft a spec with an AI assistant, give it this README along with your meeting transcripts and notes. The Instructions and Template sections below are written to be handed over as-is.

You can change the template in your copy to fit your clients. The checker always reads your own README, so it enforces your version.

Have an improvement, or advice on the process? See [CONTRIBUTING.md](CONTRIBUTING.md). Changes to the template are listed in [CHANGELOG.md](CHANGELOG.md).

## Intention

As a contract designer, an effective project brief is imperative for communicating with product teams, especially those not aware of the requirements and information needed to help the designer complete tasks. This is meant to clear up miscommunications, reduce redesigning later in the product development process, and give project managers and designers a consistent documentation process so they can work better together.

## Instructions (do not skip):

Design specs (previously called "brief", may be used interchangeably) must follow this format. Be concise and direct. Design specs are written for the UI/UX contractor on the project.

Below is the template you should follow. It includes the section headers, instructions on what to include, and examples to follow. After being given the transcripts and notes, go section by section and develop the design brief. Flag any missing information, and prompt me with questions to fill in the gaps. Go in order from Problem Statement.

Flag anything unresolved as a blockquote (a line starting with `>`), wherever in the document it comes up — a missing piece of data, an assumption that needs confirming, a note you're not sure how to resolve. This is a standing convention across every finished spec, not just while we're drafting: when a spec gets handed to the PM, every `>` line in it is a question still waiting on an answer, and the PM's AI assistant should prompt the PM directly on each one rather than letting them get silently skipped over.

## Template

### Project Title

Instructions:
- Two tables. The first is document metadata; the second is who owns the work and where each owner stands.
- Prototype/Designs is not a separate field — exploration artifacts, mockups, and prototypes go under Contextual Documents alongside research and background docs. Handoff Link is the one link field reserved for the current design artifact (whichever is current: still exploring, or the final handoff file).

Template:
| Field | Value |
| :---- | :---- |
| Last Updated | Date and person created |
| Sprint | Start date - end date |
| Ticket | Every relevant ticket or range (Azure DevOps, Jira, Linear, etc.), each with a few words on what it covers. Spell out ranges and note which ticket owns which section |
| Contextual Documents | Links to research, background information, prototypes, mockups, or exploration artifacts. If none exist yet, write "None yet" (and say if that's deliberate) — never leave blank |
| Research Status | Description (Not Started, Discovery, Definition, Ideation, Prototyping, Validation, Complete) |
| Handoff Due Date | Date |
| Handoff recipient | Developer(s) |
| Handoff Link | Link to the current design artifact |

| Role | Status |
| :---- | :---- |
| Project Manager | Where the brief stands with PM (e.g. Handed off brief, Approved) |
| Designer | Where design work stands (e.g. Pending, Revisiting, Started, Need review) |
| Developer | Where development stands (e.g. TBD, Reviewed, Feedback pending) |


### Problem Statement

Instructions:
- Limit redundancy. Clearly frame who is affected, what the problem is, and why it matters, while deliberately avoiding any description of the solution at this stage.
- During the discovery/definition phase, naming a solution early narrows exploration and biases the work before the problem is validated. Implementation and requirements should be included in the deliverables and constraints respectively, not here.
- Keep it to a single paragraph, three to four sentences. Lead with the concrete moment the problem shows up (a season, an event, a comparison) rather than an abstract definition of it — let that moment imply why it matters instead of spelling it out as a separate clause.
- Name every user type who actually feels the problem in that same paragraph, not just the most obvious one.
- Possible reasons to justify the problem include: users have given feedback that this is what they want, business is saying we need it, and/or other competitors have it, etc.
- Make sure questions are answered before moving on. Prompt me to answer these questions if they aren't.
Source to consider: [Nielsen Norman Group Problem Statement Article](https://www.nngroup.com/articles/problem-statements/)

Example:
Right now, Stride doesn't surface a runner's milestones in one cohesive, easy-to-find place. To keep people running, we want to reward showing up as well as commitment and performance. Stride also wants a way for clubs to share achievements, creating a shared language of milestones and progress.

Tightened alternative (user–need–outcome format):
Runners — and the coaches and club members who follow them — need a consistent way to see and celebrate progress so that meaningful milestones keep them running.

### User Stories

Instructions:
- This section describes the goals of each user type. List every user type the product has (for example: runner, coach, club admin, follower). "Member" can be used as a broad descriptor for anyone logged into the experience, whether or not they hold a specific user type.
- Prompt me to make sure all the stakeholders are accounted for. If we choose to exclude a stakeholder, make a note of it at the end of the section. Please include reasoning if given. Member is not required, no need to have explanation.

Template:
- As a [user type], I want to ___
- As a [user type], I want to ___
- As a [user type], I want to ___

Examples:
- As a runner, I want to see and be notified about my milestones in one place that is easy to find and share with others
- As a coach, I want to see my runners' improvements, so I can find ways to celebrate them in front of the club
- As a club admin, I want to know when members hit club milestones, so I can recognize them in club updates
- As a member, I want to see other runners' milestones, and know when runners I follow earn something

### Audience

Instructions:
- This section is a little more technical than user stories, and instead of goals, it looks at the hierarchy of users that we want to cater to, and it outlines the permissions given to these users.
- If a feature's access is fully inherited from another object (e.g. an activity, a profile) rather than defined fresh, still fill in the hierarchy table — map each user type into Primary/Secondary/Tertiary/Other based on the access they inherit, and note in the Access column that it's inherited rather than a new rule. Don't skip the table.
- If two or more user types have identical access for this feature, put them in the same tier rather than giving each its own row — the hierarchy should reflect real differences in access, not just list every stakeholder.

Template:
| Hierarchy   | User | Access      |
| :---------- | :----| :---------- |
| Primary     | User | only access to ___ OR able to ___ |
| Secondary   | User | only access to ___ OR able to ___ |
| Tertiary    | User | only access to ___ OR able to ___ |
| Other       | User | only access to ___ OR able to ___ |


Example:
| Hierarchy   | User | Access      |
| :---------- | :----| :---------- |
| Primary     | Runner | Access to own milestones, able to share |
| Secondary   | Coach, Club admin | Access to their club's runners' milestones, not able to share |
| Tertiary    | Followers and general members | Only milestones a runner has chosen to share publicly |

### Deliverables

Instructions:
- List what's actually being asked for — the named screens/components/assets, not their detailed behavior (that belongs in Constraints).
- Open with one sentence describing the overall ask. Then a bullet on scope: is this new or iterative, and does it replace anything existing — state this explicitly even when the answer is "nothing replaces an existing screen," since it's a boundary the contractor needs.
- Then one bullet per named deliverable: a short bold label, followed by a one-line description. Keep each deliverable to a single line; anything more detailed belongs in Constraints.

Template:
[One-sentence overview of what's needed.]

- [Scope note: new vs. iterative, what if anything is replaced]
- **[Deliverable 1 name]** — [one-line description]
- **[Deliverable 2 name]** — [one-line description]

Example:
A collapsible Pace Estimate section at the bottom of the existing activity detail screen.

- New section added to an existing screen; nothing is replaced.
- **Collapsible section** — sits at the bottom of the activity detail.
- **Estimate table** — the runner's actual time beside the estimated finish-time range for other race distances.
- **Responsive screens** — web and mobile app, across all breakpoints.

### Success & Failure Criteria

Instructions:
- How will we know the design worked, and how will we know it didn't? Write 3–5 checkable statements per list — something a PM, designer, or developer could look at and answer yes or no. Prefer observable outcomes (what a user can do or understand) over internal ones (what we shipped).
- Two lists: **Success looks like** and **Failure looks like**. Failure is not the mirror image of success — name the specific ways this could go wrong (a misread, a dead end, a false impression), especially the ones the Constraints are guarding against.
- Do not invent metrics or thresholds. If the source material gives no target, say what would be measured and flag the missing number as a blockquote for the PM.
- Criteria describe outcomes, not screens. Anything that is a rule about the design itself belongs in Constraints.

Template:
**Success looks like**
- [Observable outcome]

**Failure looks like**
- [Specific way this goes wrong]

> [Missing target or unclear measure, flagged for the PM]

Example:
**Success looks like**
- A runner can read the estimated range and correctly say it is an estimate, without help.
- Runners who never open the section are unaffected — it adds no clutter to the activity detail.

**Failure looks like**
- A runner reads the range as a guaranteed result, or as an official race time.
- An activity that hasn't been estimated yet is read as broken.

> No adoption or usage target was stated in the source — confirm with PM what would count as the feature being used enough.

### Non-goals

Instructions:
- A short list of what this work is deliberately not — the boundaries a reader might otherwise assume are included. Feature-level, one line each, with a few words on why where it isn't obvious.
- Do not duplicate Constraints. A specific rule about the design ("no X this phase," "cannot Y") belongs in the matching Constraints category; Non-goals is only for the broader "this is not a redesign of Z" or "this is not for audience Y" statements. If the same fact is in both places, keep the Constraint and cut it here.
- Not a place for open questions — if it is undecided, it belongs in Open Questions or a blockquote.

Example:
- Not a change to how estimates are calculated — this displays an existing model's output.
- Not a replacement for any existing activity screen.

### Dependencies

Instructions:
- What has to exist, or be decided, before this can be designed or built, and what else depends on this. One line each, naming the other spec, ticket, team, or system and the nature of the dependency.
- Include other specs in this repo (e.g. one spec reusing another's component), platform or API readiness, and decisions owned by someone else. Link to the spec file or ticket where one exists.
- If a dependency's status is unknown, flag it as a blockquote rather than guessing.

Template:
- **[Spec, ticket, team, or system]** — [what this needs from it, or what it needs from this]

Example:
- **Training Trends spec** — the activity detail reuses its trend chart, so the mobile arrangement must be designed together.
- **Model output timing** — estimates run on a schedule, so the "not estimated yet" state depends on that schedule staying as described.

> Whether the schedule is guaranteed to stay as described is unconfirmed — check with engineering.

### Additional Context

Instructions:
- Background that doesn't fit anywhere else — domain knowledge the contractor needs to follow the rest of the document (what is this thing, how does it fit the broader product), and/or the reasoning behind a specific decision or constraint when knowing "why" will help the contractor make good calls on edge cases the brief doesn't cover.
- This isn't the place for data specifics (see Data) or hard rules (see Constraints) — just what's necessary to understand them.
- Litmus test: if a paragraph (or a sentence inside one) can be rephrased as a rule — "must," "can/cannot," "no X this phase" — it's a Constraint, not Additional Context. Move it into the matching Constraints category instead of leaving it here. What's left after that test should read as pure "why" or "what is this thing," with nothing actionable in it.

Example (domain background):
Club challenges score a runner across a set of five or six runs rather than a single one. Clubs use them to build training groups and pick runners for team events. They are not used for any official race qualification.

Example (decision rationale):
This feature is divisive. Some coaches and runners find pace estimates useful, others think they are misleading and should not exist. That is why the section sits last and arrives closed — a runner finds it only if they go looking. The placement is a decision, not an oversight.

### Data

Instructions:
- List the non-obvious characteristics of the underlying data itself — not rules you've already decided (see Constraints), and not why a decision was made (see Additional Context). These are facts about how the data behaves that the design has to account for.
- Order the items by importance — most important first, descending from there — as a numbered list, not bullets, so the ranking is visible at a glance. Don't group by category or chronology instead.
- Each number leads with a short **bolded** statement of the fact. Follow it with sub-bullets for the supporting detail — an example value, why it's true, what it implies for the design. Skip the sub-bullets only when the bolded line needs no elaboration.

Template:
1. **[Concise fact]**
- [Supporting detail, example, or design implication]
- [Additional detail, if needed]

Example:
1. **It is a range, not a single time.**
- Example: 48:10–49:30
- A single number implies a precision the model does not have.
2. **The range is delivered as one string.**
- No separate low and high values to lay out.
- Nothing to round or reformat.

### Constraints
Instructions:
Sort constraints into these categories. Propose a new one if something genuinely doesn't fit rather than forcing it in. No intro, just hop straight into each of the following categories.

Template:
#### Category
- [ ] Constraint description
- [ ] Constraint description

#### Timeline
Schedule constraints: sprint, launch, handoff deadlines, wiggle room, repercussions of delays, opportunities if done early.

#### Structural
Where this lives in the product and how it's organized — information architecture, what controls or views exist, what it does or doesn't appear alongside.

#### States
The states the screen or its data can be in — filled, and each kind of empty, separately.

#### Access
Who can see or use it — visibility and permission rules. Visibility can be in the context of specific user types or for logged-in status (logged in vs. not logged in).

#### Behavior
What the user can do, and what happens when they do it — interaction and action rules (e.g. users can ___, users cannot ___, a functionality requirement).

#### Content
What must be shown, what must not be, and wording requirements. Informational copy and descriptions of what to put in are very much encouraged; if not thought through, get PM approval that it is ok to make up or if we need to revisit.

#### Platforms
Which surfaces this has to work on (e.g. web app, mobile app, admin tools, social media/marketing). All breakpoints are implied, no need to repeat, just list the platforms out.

### Open Questions

Instructions:
- Only genuine open questions — things the design itself still needs to resolve, not something already decided elsewhere in the document.
- Numbered, even if there's only one. Each item leads with a short **bolded** one-line question.
- Sub-bullets: why it's hard or unresolved (the tension, with concrete numbers or examples where you have them), options already considered and their trade-offs, and a closing bullet on how to proceed despite the ambiguity — whose call it is, and/or how to design so it doesn't block the rest of the work.

Template:
1. **[One-line question]**
- [Why this is hard / the tension]
- [Options already considered, with trade-offs]
- [How to proceed / whose call it is]

Example:
1. **Where does the disclaimer live?**
- Pace estimates are not accepted for race seeding, and no policy currently governs publishing them, so some disclaimer statement is likely needed.
- The wording itself sits with Product and needs stakeholder input, but where it sits on screen is a design question — above the estimate table, under the range, or elsewhere.
- Design with the assumption that something will need to go there, so it doesn't have to be wedged in later.

If by the end of this, something in the document is left out we need to revisit. I don't want to cut any sections.
