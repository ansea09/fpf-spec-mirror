---
chunk_kind: "child"
pattern_id: "C.30"
pattern_title: "Grounded Architecture and Selected-Structure Adequacy"
section_id: "C.30:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30/C.30__003_problem.md"
commit_sha: "434e17ec848bb7f49e6da99dfc268effb2b5b9af"
heading_path:
  - "C.30 — Grounded Architecture and Selected-Structure Adequacy"
  - "C.30:2 — Problem"
line_start: 58396
line_end: 58424
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
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
  - "C.18"
  - "C.19"
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
  - "C.32"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.CONWAY"
  - "C.32.MLAO"
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
  - "G.5"
  - "G.6"
keywords:
  - "ArchitectureOf@Context"
  - "architecture claim"
  - "architecture question card"
  - "architecture-description boundary"
  - "artifact-as-architecture guard"
  - "candidate architecture use"
  - "grounded architecture"
  - "selected structure"
---

### C.30:2 - Problem

Engineering teams use "architecture" for several different things:

- the selected structure of a holon;
- a diagram, model, table, dashboard, generated relation graph, or document;
- a module layout;
- a selected transformation-flow structure, flow description, or mathematical graph description;
- a functional, control, information, deployment, logical, or physical structure view;
- an ADR-like publication;
- a project-side claim defined or tested by another FPF pattern.

These uses are all useful in ordinary engineering speech, but they cannot carry the same FPF claim. The core distinction is the one already used across FPF: actual subject-relation occurrences; the exact A.22 structure selected from them; the direct `ArchitectureRelation` that may obtain between that structure and one holon; a C.2.1 claim about the holon, relation, or structure; the Description episteme or view; the representation and publication objects; and any project decision about changing architecture are different objects.

The first-minute practitioner asks four questions:

1. Are we recovering an actual architecture relation, considering a candidate structure, or only reading a representation?
2. Which subject relations actually obtain, and which exact A.22 structure is selected from them?
3. Which structure kind is in view—function, flow, control, module, Work, system-role-kind or assignment, enactor, information, data, placement, deployment, scale, or a declared logical structure—and which adjacent interface, evidence, or assurance relations matter?
4. How is the inspected material being used: as claim content, description, view, representation, publication form, decision, source relation, or mathematical lens?

How can FPF describe architecture without:

- creating `U.Architecture` as a new root kind;
- treating a description, view, diagram, graph, ADR, dashboard, or generated relation graph as the architecture;
- reducing architecture to module structure or interface relation;
- letting E.18 transformation-flow structures, LCA structures, control structures, C.29 lenses, quality language, evidence, assurance, gates, work, or decisions silently become architecture ontology;
- making architecture descriptions so heavy that ordinary practitioners cannot get a first useful architecture move.

