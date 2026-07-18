---
chunk_kind: "child"
pattern_id: "C.30"
pattern_title: "Grounded Architecture and Selected-Structure Adequacy"
section_id: "C.30:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30/C.30__010_consequences.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "C.30 — Grounded Architecture and Selected-Structure Adequacy"
  - "C.30:9 — Consequences"
line_start: 56573
line_end: 56581
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

### C.30:9 - Consequences

| Benefit | Cost or trade-off |
| --- | --- |
| Architecture claims become separable from diagrams, publications, generated relation graphs, ADRs, module lists, and decisions. | A conforming use names described holon, context, selected structure, and source, description, view, or publication role when the use has FPF-governed use. |
| The pattern enables first-principles architecture reasoning without forcing full measurement, synthesis, assurance, or decision machinery. | Some familiar architecture phrases become triggers for quick recovery rather than accepted claims. |
| Functional, flow, control, module structure, interface relation, information structure, placement structure, scale structure, work structure, evidence relation, and declared logical structures can coexist without one structure kind swallowing the rest. | Structural-view adequacy is governed by `C.30.ASV`, so practitioners can require an explicit view application. |
| C.29, E.18, LCA, module-and-interface repair, evidence, assurance, and gate patterns can supply source or reliance relations for architecture work without becoming architecture ontology. | Governing pattern applications are named by value whenever a source or reliance relation is used beyond C.30 architecture claim, selected-structure, or conditional description-use scope. |

