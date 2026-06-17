---
chunk_kind: "child"
pattern_id: "F.5"
pattern_title: "Naming Discipline for U.Type Names and RoleDescription Labels"
section_id: "F.5:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/F.5/F.5__012_rationale.md"
commit_sha: "646b0b9b164f7c13258633a33b92d2d0a569da28"
heading_path:
  - "F.5 — Naming Discipline for U.Type Names and RoleDescription Labels"
  - "F.5:10 — Rationale"
line_start: 73434
line_end: 73441
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "E.10"
  - "E.10.ARCH"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.7"
  - "F.8"
  - "F.9"
  - "U.Type"
keywords:
  - "U.Type naming"
  - "lexical rules"
  - "morphology"
  - "naming conventions"
  - "twin registers"
---

### F.5:10 - Rationale

Naming is late ontology, not early decoration. FPF can tolerate many local phrases, but durable names become references used in reasoning, search, publications, and pattern relations. If a name is wrong, subsequent users inherit a false kind claim.

The key design choice is to split naming by meaning source rather than by source spelling. `Role` in a source phrase may refer to a work-facing role, a policy term, a status label, an evidence-use relation, a relation position, or ordinary English. F.5 does not decide by suffix. It recovers the current value and then applies naming discipline.

This also keeps F.5 smaller than F.18. F.18 governs the fuller local-first naming protocol, Name Cards, candidate fronts, lineage, and public naming. F.5 supplies the special discipline needed by `U.Type` names and RoleDescription labels so that Part F does not preserve role and status fusion.

