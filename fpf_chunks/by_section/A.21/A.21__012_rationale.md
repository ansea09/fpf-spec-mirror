---
chunk_kind: "child"
pattern_id: "A.21"
pattern_title: "Gate Decisions from Independent Check Results"
section_id: "A.21:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.21/A.21__012_rationale.md"
commit_sha: "f4bad21274b54b57071afb2210a8bdb9f61a1c95"
heading_path:
  - "A.21 — Gate Decisions from Independent Check Results"
  - "A.21:10 — Rationale"
line_start: 35455
line_end: 35460
dependencies:
  - "A.10"
  - "A.15.5"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.20"
  - "B.3"
  - "C.3.2"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.19"
  - "F.6"
  - "F.9"
  - "G.11"
  - "G.6"
keywords:
---

### A.21:10 - Rationale

Constraint truth, evidence about that truth, policy application, and bounded action are different claims. The source patterns establish check results. A.21 applies one current profile and records the consequence. Keeping those claims separate makes the decision independent of evaluation order and keeps failures useful for repair.

The join lattice gives a compact, deterministic aggregation after every source result has been identified and mapped. It does not supply applicability, evidence, permission, authority, or a missing result.

