---
chunk_kind: "child"
pattern_id: "F.5"
pattern_title: "Naming Discipline for U-kind Names and SystemRoleKindDescription Labels"
section_id: "F.5:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/F.5/F.5__012_rationale.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "F.5 — Naming Discipline for U-kind Names and SystemRoleKindDescription Labels"
  - "F.5:10 — Rationale"
line_start: 92298
line_end: 92305
dependencies:
  - "A.10"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "A.6.RSIR"
  - "B.3"
  - "C.16"
  - "C.2.1"
  - "C.3"
  - "C.3.3"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.ROLE"
  - "E.24.UK"
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
  - "G.6"
keywords:
  - "Plain and Tech designations"
  - "SystemRoleKindDescription label"
  - "U-kind name"
  - "local meaning"
  - "naming after ontology recovery"
  - "system-role-kind name"
---

### F.5:10 - Rationale

Naming is late ontology, not early decoration. Durable names become references used in reasoning, search, publications, and pattern relations. A wrong name makes later readers inherit a false kind claim.

The design choice is to split naming by meaning source rather than source spelling. Bare *role* can point to many different objects or uses—for example, a local system-role kind, assignment, policy term, status, evidence use, relation position, representation position, or ordinary English. Do not decide by suffix. Use E.10.ROLE and the direct patterns to recover the object, then F.5 to name it.

F.5 remains narrower than F.18. Use F.18 for the full local-first protocol, NameCards, candidate comparison, lineage, and public naming. F.5 supplies the special discipline needed by U-kind names, concrete system-role-kind names, and `SystemRoleKindDescription` labels.

