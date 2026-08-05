---
chunk_kind: "child"
pattern_id: "A.20"
pattern_title: "Flow Constraint Validity — Eulerian"
section_id: "A.20:7.1"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.20/A.20__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "A.20 — Flow Constraint Validity — Eulerian"
  - "A.20:7.1 — Common Anti-Patterns and How to Avoid Them"
line_start: 33792
line_end: 33800
dependencies:
  - "A.19.SelectorMechanism"
  - "A.21"
  - "C.18"
  - "C.19"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.6"
keywords:
  - "ConstraintValidity"
  - "Eulerian"
  - "GateFit"
  - "MVPK"
  - "PathSlice"
  - "Sentinel"
  - "SquareLaw"
  - "TransformationFlowStructure"
  - "flow"
---

### A.20:7.1 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Correct action |
|---|---|---|
| CV as gate passage | Internal step validity is treated as release, safety, launch, or admission readiness. | Keep `CV.Status` local to the step and use `A.21` when gate fit or gate decision is current. |
| CV as scalar ranking | A valid set return is folded into one best item without a comparator relation. | Keep set, archive, and comparator claims with the neighboring loci named in Relations. |
| CV as evidence freshness | A witness that supports internal validity is treated as current evidence for a different claim. | Use `A.10`, `G.6`, or the source-currentness pattern when freshness or provenance is current. |
| Publication face as CV object | A dashboard or MVPK face is treated as the constraint-validity relation itself. | Keep publication use in `E.17` and cite A.20 only for the step-local CV relation. |

