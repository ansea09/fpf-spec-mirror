---
chunk_kind: "child"
pattern_id: "C.30.ASV"
pattern_title: "Architecture Structural View Adequacy (ASV)"
section_id: "C.30.ASV:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.ASV/C.30.ASV__003_problem.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "C.30.ASV — Architecture Structural View Adequacy (ASV)"
  - "C.30.ASV:2 — Problem"
line_start: 60182
line_end: 60196
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.3"
  - "A.6.F"
  - "A.6.M"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TFS-REL"
  - "C.32"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
  - "E.24.PUB"
  - "F.18"
  - "G.6"
keywords:
  - "ArchitectureStructureKindRef"
  - "VF.ARCH.STRUCTURE"
  - "architecture structural view"
  - "correspondence"
  - "hidden or lost structure"
  - "source return"
  - "structure kind"
  - "viewpoint bundle"
---

### C.30.ASV:2 - Problem

An architecture structural view is selected-structure triage for an `ArchitectureOf@Context` claim: which architecture-relevant structure is being viewed, which structure kind is under consideration, what relation, constraint, invariant, operation, dynamics description, hidden or lost structure, correspondence, source or reliance relation, and source-return condition changes the next architecture move. The view is represented as a Description episteme, including an episteme-lane `U.View` when the view claim is being made, only to record that selected-structure move. Publication faces, forms, units, and renderings may publish the view; they are not the view and do not become the selected structure.

Without this pattern:

- a module-interface view is treated as all architecture;
- a selected transformation-flow structure, mathematical graph description, or control diagram is treated as proof;
- a structure kind is treated as a `U.Viewpoint`;
- a TEVB viewpoint bundle is mutated to carry architecture-specific structure kinds;
- a diagram, table, dashboard, generated relation graph, or ADR is treated as the view itself;
- functional architecture is treated as a peer ontology rather than a structure-kind interpretation under C.30;
- cross-view consistency is asserted by prose instead of correspondence records;
- omitted structure is relied on in subsequent work without a source-return condition.

