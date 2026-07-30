---
chunk_kind: "child"
pattern_id: "A.2.1"
pattern_title: "U.RoleAssignment - System Role Assignment"
section_id: "A.2.1:10"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.1/A.2.1__012_consequences.md"
commit_sha: "308edacfa2bdb2c60d07e4e10c0deb1f260a6a31"
heading_path:
  - "A.2.1 — U.RoleAssignment - System Role Assignment"
  - "A.2.1:10 — Consequences"
line_start: 3273
line_end: 3282
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

### A.2.1:10 - Consequences

| Gain | Cost or tradeoff |
| --- | --- |
| Assignment episodes become referenceable and distinguishable. | Reliance-bearing use must recover the required participant fillings and continuity of the assignment episode. |
| Ordinary prose remains lightweight. | Authors must decide when a receiving use really needs explicit occurrence identity. |
| Role meaning no longer depends on a mandatory `U.BoundedContext`. | Taxonomy episteme and reference scheme must be named rather than assumed. |
| Work attribution becomes inspectable without a duplicate enactment occurrence. | Assignment and Work must remain distinct occurrences linked by `performedUnderAssignment(W, RA)`, with the admitted System in `RA.HolderSystemSlot` named as actual performer. |
| Evidence and assignment-establishing decisions keep their own ontology. | A single assignment row can no longer hide every supporting claim. |

