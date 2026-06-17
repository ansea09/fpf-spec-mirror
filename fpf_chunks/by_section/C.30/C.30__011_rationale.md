---
chunk_kind: "child"
pattern_id: "C.30"
pattern_title: "Grounded Architecture and Selected-Structure Adequacy"
section_id: "C.30:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30/C.30__011_rationale.md"
commit_sha: "646b0b9b164f7c13258633a33b92d2d0a569da28"
heading_path:
  - "C.30 — Grounded Architecture and Selected-Structure Adequacy"
  - "C.30:10 — Rationale"
line_start: 53384
line_end: 53393
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.3"
  - "A.6.F"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.2.1"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
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
  - "ArchitectureOf@Context"
  - "architecture claim"
  - "architecture question card"
  - "architecture-description boundary"
  - "artifact-as-architecture guard"
  - "grounded architecture"
  - "selected structure"
---

### C.30:10 - Rationale

Architecture is most useful in FPF when it stays close to selected structure over a holon and far away from document-as-architecture, graph-as-architecture, model-as-architecture, and decision-as-architecture collapses. The `ArchitectureOf@Context` record gives the selected structure a project-side claim handle without minting `U.Architecture`.

C.30 and C.30.ASV establish an FPF architecture kernel: architecture as selected `EntityOfConcern` structure for a described holon, with Description epistemes and structural views, structure-kind discipline, correspondence and source-return boundaries, and characteristic-relation applications. They do not by themselves provide full measurement, synthesis, decision, causal proof, safety proof, or assurance.

The small first card is deliberate. Architecture discussions often need one immediate move: name the holon, choose the structure kind under consideration, recover a source, description, view, or publication role, assign an evidence or assurance claim to its governing pattern, or stop. A full architecture description is useful only when durable publication, cross-team use, comparison, regulated use, source reuse, or reliance-relation reuse is being made.

The DescriptionContext structure also preserves plurality. The same architecture claim may have several descriptions and views; several publications may render one description; several source records may be source relations for a view with different validation boundaries. C.30 keeps those variants usable without turning any one publication form into the architecture.

