---
chunk_kind: "child"
pattern_id: "A.2.1"
pattern_title: "U.RoleAssignment - System Role Assignment"
section_id: "A.2.1:9"
section_title: "Common Anti-Patterns"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.1/A.2.1__011_common-anti-patterns.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "A.2.1 — U.RoleAssignment - System Role Assignment"
  - "A.2.1:9 — Common Anti-Patterns"
line_start: 2613
line_end: 2623
dependencies:
  - "A.1.1"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.3.1"
  - "A.3.2"
  - "A.6.5"
  - "A.6.9"
  - "A.6.REL"
  - "C.2.1"
  - "F.6"
  - "F.9"
  - "U.Role"
keywords:
  - "AssignmentInterval"
  - "assignment occurrence"
  - "effective ReferenceScheme"
  - "holder System"
  - "performedUnderAssignment"
  - "role value"
  - "role-taxonomy episteme"
---

### A.2.1:9 - Common Anti-Patterns

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| `Alice is reviewer`, used for work attribution | Taxonomy, scheme, and assignment episode are unavailable. | Recover the four required participant fillings and the continuous assignment episode before attributing exact Work `W` under it through `performedUnderAssignment(W, RA)`. |
| `Alice#ReviewerRole:ReviewContext@Window` | The token hides the kind behind `Context` and omits taxonomy and scheme. | Expand to the exact `U.RoleAssignment` declaration and recover the denoted value and its kind through the direct pattern. |
| One assignment row reused for every shift | Storage identity collapses repeated relation occurrences. | Identify each assignment episode by its temporal extent under `A.6.REL`. |
| Assignment proves work | Role holding is confused with dated enactment. | Name exact `U.Work` `W`, exact assignment `RA`, its admitted holder System, and the direct `performedUnderAssignment(W, RA)` relation. |
| Durable `RoleEnactment` kind or occurrence | A derived attribution duplicates Work and assignment. | Let `A.15.1` govern the exact Work occurrence and `F.6` alone govern `performedUnderAssignment(W, RA)`; do not create another enactment kind or occurrence. |
| Report holds `EvidenceRole` | An episteme is made a system holder. | Use the direct evidence relation around the report and claim. |

