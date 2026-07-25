---
chunk_kind: "child"
pattern_id: "A.6.9"
pattern_title: "Cross-Context Sameness Disambiguation - Repairing cross-context \"same\", \"equivalent\", and \"align\" via explicit Bridges (RPR-XCTX)"
section_id: "A.6.9:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.9/A.6.9__012_rationale.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "A.6.9 — Cross-Context Sameness Disambiguation - Repairing cross-context \"same\", \"equivalent\", and \"align\" via explicit Bridges (RPR-XCTX)"
  - "A.6.9:10 — Rationale"
line_start: 20360
line_end: 20370
dependencies:
  - "A.6.6"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.3.3"
  - "E.10"
  - "E.10.D1"
  - "E.10.U9"
  - "E.17"
  - "E.19"
  - "F.0.1"
  - "F.5"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "CL"
  - "SenseCells"
  - "alignment"
  - "bridge"
  - "cross-context sameness"
  - "direction"
  - "loss notes"
  - "mapping"
  - "substitution licence"
  - "weakest-link"
---

### A.6.9:10 - Rationale

Cross‑Context “sameness” is a *family of relations*, not a single predicate. Making the Bridge explicit:

* preserves the locality of meaning (SenseCells are context‑bound);
* prevents licence creep (Naming‑only does not silently become substitution);
* supports auditability (BridgeId + slots, not adjectives);
* aligns prose with the formal reasoning primitives that govern safe substitution and row scopes.

A.6.9 turns a dangerous linguistic convenience into an explicit, reviewable, evolvable claim.

