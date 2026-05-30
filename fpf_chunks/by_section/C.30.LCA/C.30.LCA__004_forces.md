---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__004_forces.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:3 — Forces"
line_start: 52339
line_end: 52347
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

### C.30.LCA:3 - Forces

* Control talk is useful and current engineering practice uses it, so deleting it would make architecture prose less usable.
* The same labels can name different things: a control layer, a declared system level, a scale window, an organizational level, a work/evidence scope, or a publication grouping.
* Layered and multi-rate control descriptions often need timing and dynamics claim before they can carry stability or safety claims.
* `B.2.5` already gives FPF a supervisor-subholon feedback-loop pattern, but it does not turn every loop diagram into proof.
* TGA graphs can describe flow and transduction relations that participate in control, but the TGA graph is still a description or view, not the control structure itself.
* Practitioners need one small first output; dynamics, C.29, evidence, assurance, and gate records open only when the live question calls for that exact governing pattern use.

