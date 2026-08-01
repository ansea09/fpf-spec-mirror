---
chunk_kind: "child"
pattern_id: "A.2.5"
pattern_title: "RoleStateRelation@BoundedContext - Role State Space and Enactable-State Admission"
section_id: "A.2.5:9"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.5/A.2.5__012_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "1eb56cd0cfd6dccad65143e03d28509373bd8dd5"
heading_path:
  - "A.2.5 — RoleStateRelation@BoundedContext - Role State Space and Enactable-State Admission"
  - "A.2.5:9 — Common Anti-Patterns and How to Avoid Them"
line_start: 4687
line_end: 4697
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

### A.2.5:9 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Assignment-as-readiness | "She is assigned as verifier, so the verification work is admitted." | Keep `U.RoleAssignment`; add `StateAssertion` for an enactable state if the work claim needs it. |
| Capability-as-role-state | "The robot is in Ready because it has the inspection capability." | Capability stays in `A.2.2`; role state predicates may refer to capability evidence only when the relation is explicit. |
| Method-order drift | State-change predicates list the tasks in a procedure. | Move ordering to method description or work plan. Keep A.2.5 to state recognition and admission. |
| Evidence-role drift | A report, standard, dataset, or model card receives a role state. | Recover evidence-use, status-use, source-use, requirement-use, or publication-use relation around the episteme. |
| Label-only incompatibility | Two role labels conflict everywhere even when one assignment is suspended or non-enactable. | Declare incompatibility over enactable states and windows where the risk actually appears. |
| Product-state explosion | A bundle role creates every combination of states across component roles. | Use separate state assertions unless a composite role with its own `RoleStateRelation@BoundedContext` is maintained. |

