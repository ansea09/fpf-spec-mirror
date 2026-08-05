---
chunk_kind: "child"
pattern_id: "A.2.5"
pattern_title: "RoleStateRelation - Windowed Role-State Recognition and Work Admission"
section_id: "A.2.5:9"
section_title: "Common Failure Modes and Repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.5/A.2.5__012_common-failure-modes-and-repairs.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "A.2.5 — RoleStateRelation - Windowed Role-State Recognition and Work Admission"
  - "A.2.5:9 — Common Failure Modes and Repairs"
line_start: 4688
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

### A.2.5:9 - Common Failure Modes and Repairs

| Failure | Observable symptom | Repair |
|---|---|---|
| Assignment-as-readiness | A work claim proceeds because a holder is assigned. | Name the selected admission predicate and establish the corresponding role-state relation and supported assertion for the work window. |
| State-label transport | Two taxonomies use `Ready` as if it meant the same predicate. | Compare predicates by value under their schemes or declare a bridge with preserved and lost effects. |
| Evidence-as-state | A certificate or dashboard display is entered as the role state. | Keep the state relation world-side; target its assertion with the direct evidence-use relation. |
| Evidence-gap-as-false | A missing current report closes a role-state episode. | Record unresolved reliance for the receiving use; close the occurrence only when the predicate's direct truth condition is demonstrated not to hold. |
| Capability-as-admission | Tool exposure or measured ability admits a concrete action. | Keep capability in A.2.2; require exact system-performed consumer evaluation of current state and action-specific conditions. |
| Method-order drift | Transition arrows are used as the procedure. | Name the work, transformation, decision, or event occurrences that change predicate truth and put order in the method description. |
| Product-state explosion | A multi-role work claim enumerates every combination of state labels. | Use separate role-state occurrences and the exact conjunction needed by the current claim; introduce a composite role only when its taxonomy and assignment are real. |

