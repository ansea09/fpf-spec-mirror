---
chunk_kind: "child"
pattern_id: "C.30"
pattern_title: "Architecture Description Adequacy (ADA)"
section_id: "C.30:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30/C.30__003_problem.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "C.30 — Architecture Description Adequacy (ADA)"
  - "C.30:2 — Problem"
line_start: 51397
line_end: 51420
dependencies:
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
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TGA-FLOW-REL"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
  - "F.18"
  - "G.6"
keywords:
  - "ArchitectureOf@Context"
  - "architecture claim"
  - "architecture description"
  - "architecture question card"
  - "artifact-as-architecture guard"
  - "selected structure"
---

### C.30:2 - Problem

Engineering teams use "architecture" for several different things:

- the selected structure of a holon;
- a diagram, model, table, dashboard, generated relation graph, or document;
- a module layout;
- a TGA graph or flow description;
- a functional, control, information, deployment, logical, or physical structure view;
- an ADR-like publication;
- a decision, gate, evidence path, assurance case, or release claim.

These uses are all useful in ordinary engineering speech, but they cannot carry the same FPF claim. The core distinction is the one already used across FPF: the architecture-relevant selected structure, the architecture claim over that structure, the D/S description or view of that claim, the publication of that description or view, and the project decision about changing architecture are different records.

The first-minute practitioner can ask: Are we choosing an architecture, or just naming a module layout? Which structure is being described: function, flow, control, module/interface, work, role/enactor, evidence/assurance, information/data, placement/deployment, scale, or declared logical structure? What artifact are we looking at: architecture claim, description, view, carrier, publication, decision, source-relation object, or mathematical lens?

How can FPF describe architecture without:

- creating `U.Architecture` as a new root kind;
- treating a description, view, diagram, graph, ADR, dashboard, or generated relation graph as the architecture;
- reducing architecture to module/interface structure;
- letting TGA, LCA, C.29 lenses, quality language, evidence, assurance, gates, work, or decisions silently become architecture ontology;
- making architecture descriptions so heavy that ordinary practitioners cannot get a first useful move.

