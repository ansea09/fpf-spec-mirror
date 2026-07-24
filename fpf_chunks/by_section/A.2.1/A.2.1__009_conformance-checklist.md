---
chunk_kind: "child"
pattern_id: "A.2.1"
pattern_title: "U.RoleAssignment - Contextual Work-Role Assignment"
section_id: "A.2.1:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.1/A.2.1__009_conformance-checklist.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "A.2.1 — U.RoleAssignment - Contextual Work-Role Assignment"
  - "A.2.1:7 — Conformance Checklist"
line_start: 2625
line_end: 2639
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.1"
keywords:
  - "RCS/RSG"
  - "RoleEnactmentFact"
  - "Standard"
  - "context"
  - "holder"
  - "performedBy"
  - "role"
---

### A.2.1:7 - Conformance Checklist

| ID | Check |
| --- | --- |
| `CC-A2.1-1` | A `U.RoleAssignment` identifies holder, role value, and bounded context. |
| `CC-A2.1-2` | The holder is an admitted `U.System` selected as system-like performer by the governing work, transformation, functioning, or method pattern. |
| `CC-A2.1-3` | No `U.Role`, `U.RoleAssignment`, or `U.Episteme` is used as holder merely because source language says "role". |
| `CC-A2.1-4` | Any claim depending on current assignment validity names the assignment window, inherits a declared bounded-context default, or lowers or blocks the stronger claim. |
| `CC-A2.1-5` | The assignment relation is not used as evidence of capability, selected method, planned work, performed work, gate passage, commitment, permission, or evidence-use relation. |
| `CC-A2.1-6` | `Work.performedBy` points to a concrete `U.RoleAssignment` when work attribution depends on role holding. |
| `CC-A2.1-7` | Any named `RoleEnactmentFact` is stated as derived over `U.Work` and `U.RoleAssignment`, not as a durable U-kind. |
| `CC-A2.1-8` | Evidence-use and status-use of epistemes are expressed through direct evidence, status, source, publication, requirement, definition, explanation, assurance, gate, or decision relations, not through `U.RoleAssignment`. |
| `CC-A2.1-9` | Role state and enactable-state admission are governed by `A.2.5`; role relation structure is governed by `A.2.7`; capability is governed by `A.2.2`; method and work are governed by `A.15` and A.15 subpatterns. |
| `CC-A2.1-10` | Shorthand notation is not used unless the typed relation and any current missing-slot disposition are recoverable. |

