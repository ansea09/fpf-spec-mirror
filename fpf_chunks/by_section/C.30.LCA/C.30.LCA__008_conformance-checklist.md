---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__008_conformance-checklist.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:7 — Conformance Checklist"
line_start: 53723
line_end: 53736
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
  - "C.30.ASV"
  - "C.30.LCA"
  - "C.30.STRAT"
  - "C.30.TGA-FLOW-REL"
  - "E.18"
  - "G.6"
keywords:
  - "control layer"
  - "control-structure view"
  - "controller/plant"
  - "layered control architecture"
  - "proof overread"
  - "rate band"
  - "supervisor loop"
---

### C.30.LCA:7 - Conformance Checklist

| ID | Check | Why it matters |
|---|---|---|
| CC-LCA-1 | A conforming use names the `ArchitectureOf@Context` or recoverable described holon and bounded context whose control structure is being viewed. | Prevents free-floating control diagrams. |
| CC-LCA-2 | A conforming use records control roles and relations: planner, regulator or controller, observer or estimator, plant or controlled system, supervisor, or the local subset actually present. | Keeps the view action-guiding. |
| CC-LCA-3 | A conforming use sends `layer`, `level`, `tier`, or `stack` wording to `C.30.STRAT` unless the text already recovers a control-specific `controlLayerRef`, `controlRelationRef`, `interLayerControlRelationRef`, `rateBandRef`, bounded context, or `B.2.5` supervisor-subholon relation. | Prevents pseudo-level or pseudo-layer overread inside C.30.LCA. |
| CC-LCA-4 | A conforming use records observation, actuation, feedback, and externality boundaries when they are live in the view. | Makes the control relation inspectable. |
| CC-LCA-5 | Stability, safety, dynamics, temporal adequacy, causal use, evidence, gate, and assurance claims are assigned to their exact governing patterns. | Prevents LCA-as-proof. |
| CC-LCA-6 | `B.2.5` is used only as a supervisor-subholon feedback-loop relation or check pattern, not as proof of stability, safety, evidence, gate validity, or assurance. | Keeps existing FPF control relation bounded. |
| CC-LCA-7 | A TGA path slice used by the control view remains a flow or transduction description or relation to E.18, not the control structure itself. | Keeps TGA and LCA relations distinct. |
| CC-LCA-8 | A C.29 or mathematical-lens use is opened when LCA is transferred across domains or used for prediction, reusable explanation, or assurance input. | Preserves mathematical-lens use. |
| CC-LCA-9 | The record states admissible use, non-admissible use, and source-return condition. | Prevents narrowed recognition from becoming unchecked reliance. |

