---
chunk_kind: "child"
pattern_id: "C.30.ASV"
pattern_title: "Architecture Structural View Adequacy (ASV)"
section_id: "C.30.ASV:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.ASV/C.30.ASV__003_problem.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "C.30.ASV — Architecture Structural View Adequacy (ASV)"
  - "C.30.ASV:2 — Problem"
line_start: 50732
line_end: 50746
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.3"
  - "A.6.F"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.TGA-FLOW-REL"
  - "E.10"
  - "E.10.D2"
  - "E.10.SEMIO"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
  - "F.18"
  - "G.6"
keywords:
  - "ArchitectureStructureKindRef"
  - "VF.ARCH.STRUCTURE"
  - "architecture structural view"
  - "correspondence"
  - "hidden/lost structure"
  - "source return"
  - "structure kind"
  - "viewpoint bundle"
---

### C.30.ASV:2 - Problem

An architecture structural view is not a generic view. It is a D/S view over one or more `candidate:U.Structure` references selected by an `ArchitectureOf@Context` claim record. A conforming architecture structural view keeps the D/S relation, described entity, bounded context, structure references, structure kind, viewpoint, hidden or lost structure, correspondence, support relation, source return, and admissible use recoverable.

Without this pattern:

- a module/interface view is treated as all architecture;
- a TGA graph or control diagram is treated as proof;
- a structure kind is treated as a `U.Viewpoint`;
- a TEVB viewpoint bundle is mutated to carry architecture-specific structure kinds;
- a diagram, table, dashboard, generated relation graph, or ADR is treated as the view itself;
- functional architecture is treated as a peer ontology rather than a structure-kind reading under C.30;
- cross-view consistency is asserted by prose instead of correspondence records;
- omitted structure is relied on in subsequent work without a source-return condition.

