---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__004_forces.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:3 — Forces"
line_start: 56704
line_end: 56712
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
  - "C.30.TFS-REL"
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
* The same source labels can name different things. C.30.LCA applies only to recovered control-layer, rate-band, control-relation, bounded-context, and `B.2.5` supervisor-subholon uses; other `layer`, `level`, `tier`, or `stack` uses are recovered with `C.30.STRAT` and then governed by their governing patterns when those claims are being made.
* Layered and multi-rate control descriptions often need timing and dynamics claim before they can carry stability or safety claims.
* `B.2.5` already gives FPF a supervisor-subholon feedback relation, but it does not turn every feedback or loop diagram into proof.
* `E.18` `TransformationFlowStructure` values and their mathematical graph descriptions can describe flow, path, crossing, or transformation-flow relations that participate in control, but the transformation-flow description or graph expression is still a description or view, not the control structure itself.
* Practitioners need one small first output; dynamics, C.29, evidence, assurance, and gate records are used only when the question under repair calls for that governing pattern use.

