---
chunk_kind: "child"
pattern_id: "A.2.5"
pattern_title: "SystemRoleAssignmentStateRelation - Assignment-State Recognition and Work Admission"
section_id: "A.2.5:8"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.5/A.2.5__011_conformance-checklist.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "A.2.5 — SystemRoleAssignmentStateRelation - Assignment-State Recognition and Work Admission"
  - "A.2.5:8 — Conformance Checklist"
line_start: 5147
line_end: 5163
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.7"
  - "A.21"
  - "A.6.5"
  - "A.6.REL"
  - "C.3"
keywords:
  - "Work admission"
  - "assignment-state predicate"
  - "assignment-state relation"
  - "evidence boundary"
  - "state condition"
  - "time window"
---

### A.2.5:8 - Conformance Checklist

| Check | Question |
|---|---|
| `CC-A2.5-01` | Is the current object one `SystemRoleAssignmentStateRelation : U.Relation`, rather than a system-role kind, assignment, capability, assertion episteme, evidence relation, diagram, gate outcome, or Work occurrence? |
| `CC-A2.5-02` | Does `SystemRoleAssignmentSlot` use a `U.RelationRef` constrained to `U.SystemRoleAssignment` and resolve to the exact assignment occurrence being evaluated, with its declared species, holder, and extent established under A.2.1? |
| `CC-A2.5-03` | Is `StatePredicateSlot` present by value with exact system-role-kind domain, normalized truth clauses, temporal reading, applicability, and only meaning-bearing semantic-basis refs? |
| `CC-A2.5-04` | Is actual state extent derived from uninterrupted predicate truth while the assignment obtains, with any target evaluation window kept separate? |
| `CC-A2.5-05` | When occurrence identity is needed, does it use the fixed assignment, fixed predicate value, and maximal continuous truth interval rather than a representation key? |
| `CC-A2.5-06` | Are a demonstrated predicate gap and a mere evidence gap distinguished? |
| `CC-A2.5-07` | Does `SystemRoleAssignmentStateAssertion` keep polarity, predicate, direct claim-family ref, known actual extent, target window, reliance posture, and evidence relations distinct? |
| `CC-A2.5-08` | Are capability, Method selection, gate outcome, authority, assurance, and performed Work left with their direct patterns? |
| `CC-A2.5-09` | If several predicates hold together, are they composed explicitly rather than forced into one exclusive state label? |
| `CC-A2.5-10` | Does cross-context reuse preserve the full predicate identity through an explicit continuity or bridge decision rather than label matching? |
| `CC-A2.5-11` | Is a meaning-bearing signature, scheme, bridge, or model-use structure included in predicate identity only when the clauses depend on it, and otherwise kept with the receiving use? |
| `CC-A2.5-12` | If a statechart or graph is used, is it kept as a lens or description of possible configurations and changes? |

