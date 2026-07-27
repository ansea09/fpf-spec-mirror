---
chunk_kind: "child"
pattern_id: "C.30.AD.BA"
pattern_title: "Built-Asset Architecture Description and Reference Designation"
section_id: "C.30.AD.BA:5"
section_title: "Digital Twin and Design-Run Boundary"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD.BA/C.30.AD.BA__008_digital-twin-and-design-run-boundary.md"
commit_sha: "1f413fcd23f4ea26956a45d67dde57bb233f6ad9"
heading_path:
  - "C.30.AD.BA — Built-Asset Architecture Description and Reference Designation"
  - "C.30.AD.BA:5 — Digital Twin and Design-Run Boundary"
line_start: 59950
line_end: 59957
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.F"
  - "A.6.M"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.TFS-REL"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.24.PUB"
  - "F.18"
keywords:
---

### C.30.AD.BA:5 - Digital Twin and Design-Run Boundary

A digital twin can describe, monitor, simulate, or forecast a built asset. It does not become the built asset by being connected to sensors or operations data.

Use `DesignRunTagRefs` when a description crosses design-side and run-side material. A design model, built asset, sensor relation, operation record, maintenance work, and physical transformation remain different objects unless a direct governing pattern relates them.

Example boundary: a lathe can transform a workpiece without becoming the workpiece's super-holon. Likewise, a building-management system can change equipment state without becoming part of that equipment merely because the dashboard shows both in one operational view. Use `HolonBoundaryCrossingRelation@Context`, `U.Transformation`, `U.Work`, evidence, source, and architecture-description relations before any MHT or part-whole claim is admitted.

