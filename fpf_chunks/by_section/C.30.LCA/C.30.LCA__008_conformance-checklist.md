---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__008_conformance-checklist.md"
commit_sha: "9a9c1b14df894386c664cf49a9ccbbd4a4063100"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:7 — Conformance Checklist"
line_start: 61615
line_end: 61628
dependencies:
  - "A.10"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.3.3"
  - "B.2.5"
  - "B.3"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "E.17.0"
  - "E.18"
  - "G.6"
keywords:
  - "control layer"
  - "control-structure view"
  - "controller and plant"
  - "layered control architecture"
  - "proof overread"
  - "rate band"
  - "supervisor loop"
---

### C.30.LCA:7 - Conformance Checklist

| ID | Check | Why it matters |
|---|---|---|
| CC-LCA-1 | A conforming full description or view has one C.2.1 identity whose EntityOfConcern is one exact selected control structure; the described and controlled holons and any actual `ArchitectureRelation` remain separately recoverable. | Prevents a free-floating diagram, claim, or unspecified relation set from becoming structure or episteme identity. |
| CC-LCA-2 | A conforming use records the direct control relations and participant meanings present: for example, reference provision, regulation or control, observation or estimation, plant or controlled-holon participation, or supervision. Systems, classifications, assignments, Methods, Work, and F.6 attribution are separate optional facts. | Keeps the view useful without making a label, kind, assignment, or description act. |
| CC-LCA-3 | `Layer`, `level`, `tier`, or `stack` wording enters only with a recovered direct control relation, inter-layer relation, rate band, or `B.2.5` supervisor-subholon relation. An assignment alone is insufficient. | Prevents generic stratification wording from standing in for control structure. |
| CC-LCA-4 | A claimed `U.View` names the exact viewpoint episteme and independently obtaining `EpistemeViewpointConformanceRelation`; bundle membership, viewpoint label, authoring, query, diagram, and publication are insufficient. | Keeps structural description and view membership distinct. |
| CC-LCA-5 | Use the relevant patterns to state or test stability, safety, dynamics, temporal-aspect or rate-band structure, authored temporal-claim adequacy, causal use, empirical grounding, evidence, gate, and assurance claims. | Prevents LCA-as-proof. |
| CC-LCA-6 | Use `B.2.5` only to state or test the supervisor-subholon feedback relation it defines. | Keeps a cited feedback relation distinct from stability, safety, evidence, gate, and assurance claims. |
| CC-LCA-7 | Use E.18 to identify and test any transformation-flow path slice used by the control view. The slice is not the control structure or actual transformation itself. | Keeps transformation-flow and LCA relations distinct. |
| CC-LCA-8 | C.29 or mathematical-lens use is opened when LCA is transferred across domains or used for prediction, reusable explanation, or assurance input. | Preserves mathematical-lens use and representation boundaries. |
| CC-LCA-9 | The record states admissible use, non-admissible use, and source-return condition; representation, E.24.PUB publication occurrence, publication form, and carrier remain separate. | Prevents narrowed recognition or publication from becoming unchecked reliance. |

