---
chunk_kind: "child"
pattern_id: "C.33"
pattern_title: "Structural Information Adequacy for Architecture Capture and Missing-Structure Return"
section_id: "C.33:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.33/C.33__006_archetypal-grounding.md"
commit_sha: "4b75b56c13f5d61be5238fdbc7c20af5c6f89df7"
heading_path:
  - "C.33 — Structural Information Adequacy for Architecture Capture and Missing-Structure Return"
  - "C.33:5 — Archetypal Grounding"
line_start: 66234
line_end: 66247
dependencies:
  - "A.22"
  - "A.6.3.NAR"
  - "A.6.M"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ADR"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.18"
  - "F.15"
  - "F.9"
  - "G.5"
keywords:
  - "captured selected structure"
  - "carrier"
  - "lost structure"
  - "missing structure"
  - "missing-structure return"
  - "observer boundary"
  - "selected structure"
  - "structural information adequacy"
---

### C.33:5 - Archetypal Grounding

Tell: C.33 is the pattern for using a partial carrier that captures or describes selected structure without letting that carrier stand for the whole architecture. The carrier may be a diagram, decision record, query result, eval report, code-agent map, neural-network architecture review, method handoff, or observation of the realized holon. The grounding question is not whether the carrier is impressive. The grounding question is what selected structure it captures, what it leaves out, and which governing pattern receives the next claim.

Show - system case. An ADR-like record says "use event-carried integration with bounded exception." C.33 records that the carrier captures the selected integration style, exception boundary, and method expectation. It does not capture lower-level placement constraints, schema evolution burden, runtime data custody, or deployment topology. The admissible use is decision memory and method handoff; the non-admissible use is proof that the realized modules have the intended architecture. Missing-structure return goes to `C.32.PAD`, `C.32.ADR`, `C.30.AD`, and later `C.32` synthesis if actual structure diverges.

Show - episteme case. A code-agent relation graph finds imports, call edges, inferred module roles, and candidate invariants. C.33 records relation observation class `observed | inferred | unknownRegionPresent`, typed relation semantics, confidence class, active-passive gap when present, unexplored regions, and lost runtime or deployment structure. The graph can seed `C.34` preservation checks or `C.35` discovery, but it is not internal belief proof, release evidence, or full architecture adequacy.

Show - neural architecture case. A neural-network architecture review says a model changed attention, SSM block, router, cache placement, pruning mask, and distillation path. C.33 recovers which selected structures are being described: dataflow relation, path-selection relation, memory placement, cache placement, block substitution, and affected characteristics such as latency, compute, memory, and robustness. Source labels remain source labels until recovered through `C.30.STRAT`, `C.30.TFS-REL`, `C.31`, `C.32`, `C.16`, or `C.32.ACE` as applicable.

Show - architecture narrative case. A team narrative says "we moved from candidate A to candidate B because data custody forced placement P and made latency trade-off T acceptable." C.33 records which selected structures the narrative captures: candidate relation, data-custody constraint, placement constraint, trade-off, and missing-structure return condition. It also records lost or hidden structure such as rejected candidate details, quantitative evals, module interfaces, and realization evidence. The narrative can help decision memory or team orientation; it is not by itself an architecture description, decision authority, or evidence of realized structure.

The small working form is enough when it blocks a wrong next use. It is not enough when the next claim needs an architecture description, structural view, decision repair, eval program, evidence record, assurance case, gate, release, or work authorization. In those cases C.33 produces the missing-structure return condition and then exits.

