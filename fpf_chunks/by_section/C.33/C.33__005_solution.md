---
chunk_kind: "child"
pattern_id: "C.33"
pattern_title: "Structural Information Adequacy for Architecture Capture and Missing-Structure Return"
section_id: "C.33:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.33/C.33__005_solution.md"
commit_sha: "d1f696e7c7767705206a8cacd9f6ed48e4dc5b02"
heading_path:
  - "C.33 — Structural Information Adequacy for Architecture Capture and Missing-Structure Return"
  - "C.33:4 — Solution"
line_start: 66625
line_end: 66647
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

### C.33:4 - Solution

Create one `StructuralInformationAdequacyNote@Context` for the declared architecture use.

Read the note as a small missing-structure return tool, not as a new documentation format. Its didactic question is simple: "What can I safely take from this carrier, what must I not take, and where do I go if the missing structure matters?"

Work in this order:

1. Name the architecture claim or pre-claim described holon and bounded context.
2. Name the selected structure refs or structure kinds being relied on. If they are not recoverable, stop and return to `C.30`, `C.30.ASV`, `A.22`, or `C.32.P2S`.
3. Name the carrier, selected source structure, description, view, narrative rendering, decision record, eval report, method handoff, generated relation graph, or realized observation being used.
4. State the captured selected structure in relation terms: relations, constraints, invariants, allocations, compositions, variation classes, operations, dynamics refs, or preserved organization.
5. State the expected but uncaptured structure when the next use needs it: hidden placement, data custody, runtime dependency, transformation-flow relation, source label semantics, confidence class, unexplored region, or missing bearer.
6. State lost or hidden structure. If no loss is claimed, justify why the carrier is adequate for the declared use rather than for all uses.
7. Add observer or budget boundary when the carrier comes from a bounded observer, learned representation, probe, relation graph, or epiplexity-style lens.
8. Add source label recovery when source terms come from a domain practice such as neural-network architectures, software modules, built assets, organizational roles, methods, or work.
9. Route mathematical-lens, measurement, eval, decision, evidence, assurance, gate, release, method, work, and publication claims to their direct governing patterns.
10. Stop when admissible use, non-admissible use, missing-structure return condition, receiving governing pattern, and receiving claim kind are clear.

CGUS-aware neighbor use: when a carrier, route card, narrative rendering, architecture description, framework publication, or generated relation graph is relied on because it preserves a constraint-governed unfolding structure, C.33 records only what that carrier captures and loses. The selected structure remains `ConstraintGovernedUnfoldingStructure@Context` or a local `U.Structure` block governed by `A.22.CGUS`, `E.18.3`, `C.32.P2S`, `A.6.3.NAR`, `E.23`, or another direct pattern.

A `DemonstrativeUnfoldingSlice@Context` may be the `U.Episteme` slice or presentation whose captured structure and lost structure C.33 records; it is not the selected `U.Structure` by itself. C.33 does not admit the CGUS; it tells the receiving pattern what the carrier actually preserved and where missing selected structure must be inspected or repaired.

