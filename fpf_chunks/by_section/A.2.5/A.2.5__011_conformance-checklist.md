---
chunk_kind: "child"
pattern_id: "A.2.5"
pattern_title: "RoleStateRelation@BoundedContext - Role State Space and Enactable-State Admission"
section_id: "A.2.5:8"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.5/A.2.5__011_conformance-checklist.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "A.2.5 — RoleStateRelation@BoundedContext - Role State Space and Enactable-State Admission"
  - "A.2.5:8 — Conformance Checklist"
line_start: 3954
line_end: 3968
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
| --- | --- |
| `CC-A2.5-01` | Is the current EntityOfConcern a `RoleStateRelation@BoundedContext`, not a capability, method, work occurrence, evidence episteme, status assertion, or publication form? |
| `CC-A2.5-02` | Are `RoleValueRef` and `BoundedContextRef` named or inherited? |
| `CC-A2.5-03` | Is `RoleStateSet` finite enough for the current use, with state names local to role and context? |
| `CC-A2.5-04` | Is `EnactableStateSet` explicit, including the empty-set case when the role cannot admit work? |
| `CC-A2.5-05` | Does every work-admission claim name or inherit a current `StateAssertion` window? |
| `CC-A2.5-06` | Do state predicates use observable or reviewable values, evaluations, work records, speech acts, or source relations? |
| `CC-A2.5-07` | Are state-change predicates kept separate from method order and work planning? |
| `CC-A2.5-08` | Are capability requirements governed by `A.2.2`, with method claims and work claims governed by `A.15` and A.15 subpatterns? |
| `CC-A2.5-09` | Do evidence use, status use, source use, and publication use around epistemes remain governed by their direct patterns instead of becoming work-facing role states? |
| `CC-A2.5-10` | Do role-relation hooks preserve state-sensitive role-requirement substitution, incompatibility, and bundle boundaries without product-state explosion by default? |

