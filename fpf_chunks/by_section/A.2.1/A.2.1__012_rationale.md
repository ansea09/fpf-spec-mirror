---
chunk_kind: "child"
pattern_id: "A.2.1"
pattern_title: "U.RoleAssignment - Contextual Work-Role Assignment"
section_id: "A.2.1:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.1/A.2.1__012_rationale.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "A.2.1 — U.RoleAssignment - Contextual Work-Role Assignment"
  - "A.2.1:10 — Rationale"
line_start: 2645
line_end: 2652
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

### A.2.1:10 - Rationale

The role `ontologicalNeighborhood` needs both role values and assignment relations. `A.2` keeps `U.Role` as a compact context-bound value. `A.2.1` gives that value a typed relation to a holder and context. `A.15` then lets work cite the assignment.

The selected ontology prevents two common explosions. First, it prevents every context-local role from becoming a system subtype. Second, it prevents every evidence or status use of an episteme from becoming another role assignment.

The open-world slot model is deliberate. FPF should not require dummy windows or provenance entries for low-risk recognition text. It should also not permit stronger claims to rely on missing windows, missing role-state admission, or missing assignment source. The slot is considered when the claim needs it.

