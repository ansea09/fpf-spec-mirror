---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__004_forces.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:3 — Forces"
line_start: 73415
line_end: 73423
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
  - "C.30.LCA"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "C.32.LCA"
  - "E.17.0"
  - "E.18"
  - "E.18.2"
  - "G.6"
keywords:
  - "control-structure view"
  - "controller"
  - "feedback closure"
  - "layered control architecture"
  - "observer"
  - "plant"
  - "rate band"
  - "supervisor"
---

### C.30.LCA:3 - Forces

* Control terminology helps engineers identify observations, commands, feedback and their participants; preserve it when its local meaning is clear.
* The same source labels can name different things. C.30.LCA applies after an exact direct control relation, rate-band relation, control-layer relation, or `B.2.5` supervisor-subholon relation is recovered. An assignment is neither required nor sufficient for control; include it only when it independently obtains. A model-use structure is cited only when that independently selected structure changes interpretation.
* Layered and multi-rate control descriptions often need timing and dynamics claims before they can carry stability or safety claims.
* `B.2.5` supplies a compound supervisor-subholon feedback claim grounded in observation, return and coupling facts. A feedback diagram alone establishes none of those facts.
* Mathematical graph descriptions of E.18 `TransformationFlowStructure` values can describe flow, path, crossing, or transformation-flow relations relevant to control, but the selected flow structure, graph expression, and control structure remain distinct.
* Practitioners need one small first output; exact viewpoint conformance, dynamics, C.29, evidence, assurance, and gate records are used only when the question calls for them.

