---
chunk_kind: "child"
pattern_id: "A.2.5"
pattern_title: "RoleStateRelation@BoundedContext - Role State Space and Enactable-State Admission"
section_id: "A.2.5:0.1"
section_title: "Kind Settlement"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.5/A.2.5__003_kind-settlement.md"
commit_sha: "6bbbb622859fbbcddc02b23ea76bee4dd71c6291"
heading_path:
  - "A.2.5 — RoleStateRelation@BoundedContext - Role State Space and Enactable-State Admission"
  - "A.2.5:0.1 — Kind Settlement"
line_start: 3689
line_end: 3721
dependencies:
  - "A.15"
  - "A.2.1"
keywords:
  - "RSG"
  - "enactability"
  - "role state"
  - "role-state evolution"
  - "state machine"
---

### A.2.5:0.1 - Kind Settlement

A.2.5 does not admit `U.RoleStateGraph` as a durable U-kind. The governed object is `RoleStateRelation@BoundedContext`: a selected context-local relation structure over `U.Role`, `U.BoundedContext`, role-state values, state predicates, state assertions, and work-admission relations. State-machine or graph notation is a mathematical or representation lens over that relation structure, not the object itself and not a new root beside `U.Role`.

Use this pattern when a project needs to decide whether a role assignment is currently in a state that admits a work claim, a method-step claim, an incompatibility claim, or a role-readiness claim.

Typical moments:

- a work record says that a person, team, device, service, agent, or machine acted as technical checker, operator, deployer, verifier, surgeon, sensor, or incident commander, but the current role state is unclear;
- a method description names a required role, and the project needs to state which role states admit the step;
- a role assignment is current, but the holder may be suspended, stale, uncalibrated, fatigued, not yet authorized, or otherwise not in an enactable state;
- a role-relation claim such as role-requirement substitution, incompatibility, or bundle expression depends on role states rather than labels alone;
- a source says "ready", "approved", "validated", "authorized", "active", "stale", or "blocked" and it is unclear whether this is a role state, an evidence or status relation around an episteme, an admission result, a capability value, or a work occurrence.

**Primary EntityOfConcern.** The EntityOfConcern is `RoleStateRelation@BoundedContext`: the selected context-local state-space relation for one `U.Role` in one `U.BoundedContext`. It names role states, state predicates, state-change predicates when current, and the subset of states that admit work through a `U.RoleAssignment`. It is a real FPF object, but it is not a new `U.*` kind beside `U.Role`; its identity is carried by the role value, bounded context, state set, state predicates, and work-admission relation.

**Primary working reader.** The first reader is an engineer-manager, analyst, safety checker, operations lead, or FPF author who needs to keep role assignment, role state, holder capability, method requirement, and performed work distinct while still deciding whether a work claim may proceed.

**First useful move.** Name the role and bounded context, list the states that matter for the current claim, mark which states admit work, and state what observation, evaluation, speech act, work record, or source relation can justify a `StateAssertion` for the relevant window.

**What goes wrong if missed.** A role label becomes a permission slip. A role assignment is treated as ability. A certificate, report, standard, status marker, or dashboard is treated as if it held a work-facing role. Separation-of-duties checks operate on labels instead of states. Source phrases such as "approved evidence role" or unlabeled readiness marks create a second role ontology.

**What this buys.** Role admission becomes inspectable without making forms heavy. The same role value can have different current states in different contexts and windows; method and work claims can ask only for the state evidence they need; episteme evidence and status uses stay with their direct patterns.

**Not this pattern when.**

- If the current claim is the role value itself, use `A.2`.
- If the current claim is the assignment relation linking holder, role, bounded context, and assignment window, use `A.2.1`.
- If the current claim is ability or operating envelope, use `A.2.2`.
- If the current claim is role-requirement substitution, incompatibility, or bundle expression independent of current state, use `A.2.7`.
- If the current claim is selected method, method description, work plan, or performed work, use `A.15` and the direct A.15 subpattern.
- If the current claim is an episteme used as evidence, source, standard, requirement, definition, explanation, publication, status bearer, assurance input, or admission input, use the direct pattern for that relation. Do not turn the episteme into a role holder or role state.

