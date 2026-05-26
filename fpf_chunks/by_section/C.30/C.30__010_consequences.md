---
chunk_kind: "child"
pattern_id: "C.30"
pattern_title: "Architecture Description Adequacy (ADA)"
section_id: "C.30:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30/C.30__010_consequences.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "C.30 — Architecture Description Adequacy (ADA)"
  - "C.30:9 — Consequences"
line_start: 50651
line_end: 50659
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
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30.ASV"
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
  - "ArchitectureOf@Context"
  - "architecture claim"
  - "architecture description"
  - "architecture question card"
  - "artifact-as-architecture guard"
  - "selected structure"
---

### C.30:9 - Consequences

| Benefit | Cost or trade-off |
| --- | --- |
| Architecture claims become separable from diagrams, publications, generated relation graphs, ADRs, module lists, and decisions. | A conforming use names described holon, context, selected structure, and artifact role when the use is load-bearing. |
| The pattern supports first-principles architecture reasoning without forcing full measurement, synthesis, assurance, or decision machinery. | Some familiar architecture phrases become triggers for quick recovery rather than accepted claims. |
| Functional, flow, control, module/interface, information, placement, scale, work/evidence, and declared logical structures can coexist without one structure kind swallowing the rest. | Structural-view adequacy moves to `C.30.ASV`, so practitioners may need an explicit view application. |
| C.29, E.18, LCA, module/interface, evidence, assurance, and gate patterns can support architecture work without becoming architecture ontology. | Neighboring exits are named whenever a support source is used beyond description adequacy. |

