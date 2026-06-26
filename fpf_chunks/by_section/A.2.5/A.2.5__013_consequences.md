---
chunk_kind: "child"
pattern_id: "A.2.5"
pattern_title: "RoleStateRelation@BoundedContext - Role State Space and Enactable-State Admission"
section_id: "A.2.5:10"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.5/A.2.5__013_consequences.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "A.2.5 — RoleStateRelation@BoundedContext - Role State Space and Enactable-State Admission"
  - "A.2.5:10 — Consequences"
line_start: 3987
line_end: 4017
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

### A.2.5:10 - Consequences

Good consequences:

- work admission becomes reviewable without making every role assignment a large form;
- role relation structure can use current state rather than labels alone;
- role descriptions can publish state predicates without turning descriptions into states;
- evidence and status around epistemes no longer create shadow role kinds;
- cross-context role-state comparison becomes explicit rather than label-based.

Costs:

- high-consequence work needs state predicates and currentness windows;
- projects need to decide which role states actually admit work;
- role-state design can become too detailed if authors encode method order instead of admission predicates;
- cross-context reuse needs explicit mapping or comparison when state predicates differ.

#### A.2.5:10.1 - Lowering and Reopen Conditions

Lower a role-state claim or reopen A.2.5 when any of these changes:

- the role assignment, assignment window, or bounded context changes;
- the state predicates, state-change predicates, or enactable-state set change;
- a `StateAssertion` window expires, is contested, or loses the evidence or source relation that made it current;
- a method description changes its required roles or required role states;
- a capability claim changes the holder envelope needed by a state predicate;
- a role-relation structure changes role-requirement substitution, incompatibility, or bundle admission;
- an episteme previously used as evidence, source, standard, requirement, publication, or status value is reclassified by its direct pattern.

The smallest repair is normally local: update the state predicate, state assertion, window, role-relation-structure hook, or neighboring capability, method, work, evidence, or status relation that changed. Do not rewrite the whole role value or role assignment when only one role-state claim changed.

