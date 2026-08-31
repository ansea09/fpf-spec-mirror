---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__004_forces.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:3 — Forces"
line_start: 61123
line_end: 61131
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

### C.30.LCA:3 - Forces

* Control talk is useful and current engineering practice uses it, so deleting it would make architecture prose less usable.
* The same source labels can name different things. C.30.LCA applies after an exact direct control relation, rate-band relation, control-layer relation, or `B.2.5` supervisor-subholon relation is recovered. An assignment is neither required nor sufficient for control; include it only when it independently obtains. A model-use structure is cited only when that independently selected structure changes interpretation.
* Layered and multi-rate control descriptions often need timing and dynamics claims before they can carry stability or safety claims.
* `B.2.5` already gives FPF a supervisor-subholon feedback relation, but it does not turn every feedback or loop diagram into that occurrence, selected structure, or proof.
* E.18 `TransformationFlowStructure` values and their mathematical graph descriptions can describe flow, path, crossing, or transformation-flow relations that participate in control, but the selected flow structure, graph expression, and control structure remain distinct.
* Practitioners need one small first output; exact viewpoint conformance, dynamics, C.29, evidence, assurance, and gate records are used only when the question calls for them.

