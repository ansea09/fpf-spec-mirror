---
chunk_kind: "child"
pattern_id: "A.2.5"
pattern_title: "RoleStateRelation - Windowed Role-State Recognition and Work Admission"
section_id: "A.2.5:8"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.5/A.2.5__011_conformance-checklist.md"
commit_sha: "036c056e98c38522172c6b7b3ad08214281cc4e4"
heading_path:
  - "A.2.5 — RoleStateRelation - Windowed Role-State Recognition and Work Admission"
  - "A.2.5:8 — Conformance Checklist"
line_start: 4683
line_end: 4699
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

### A.2.5:8 - Conformance Checklist

| Check | Question |
|---|---|
| `CC-A2.5-01` | Is the current object one `RoleStateRelation : U.Relation`, rather than a role value, capability, assertion episteme, evidence relation, diagram, gate outcome, or work occurrence? |
| `CC-A2.5-02` | Does `RoleAssignmentSlot` resolve to one obtaining `U.RoleAssignment` with its four exact participants and maximal continuous assignment extent? |
| `CC-A2.5-03` | Is `StatePredicateSlot` present by value, with an exact truth condition and temporal reading rather than only a state label? |
| `CC-A2.5-04` | Is actual role-state extent derived from uninterrupted predicate truth while the assignment obtains, with any target evaluation window kept in the receiving use? |
| `CC-A2.5-05` | When occurrence identity is needed, does the identity rule use the fixed assignment, fixed predicate value, and uninterrupted obtaining rather than a representation key or temporal participant? |
| `CC-A2.5-06` | Are a demonstrated predicate gap and a mere evidence gap distinguished? |
| `CC-A2.5-07` | Does `RoleStateAssertion` keep predicate, exact direct claim-family reference, affirmative or negative assertion polarity, known actual extent only for an affirmative claim about an independently established occurrence, and any receiving-use window distinct, while supported, refuted, or unresolved reliance and evidence relations remain separate and fabricate no occurrence? |
| `CC-A2.5-08` | Are capability fit, method selection, gate outcome, assurance, and performed work left with their direct patterns? |
| `CC-A2.5-09` | If several predicates hold together, are they composed explicitly rather than forced into one exclusive state label? |
| `CC-A2.5-10` | Does cross-taxonomy reuse preserve predicate meaning and admission effect through the same scheme or an explicit bridge relation? |
| `CC-A2.5-11` | Is any selected model-use structure designated only in the receiving assertion or use, with no optional `ModelUseStructureSlot` in the generic relation? |
| `CC-A2.5-12` | If a statechart or graph is used, is it kept as a lens or description of possible configurations and changes? |

