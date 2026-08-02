---
chunk_kind: "child"
pattern_id: "C.19"
pattern_title: "Explore-Exploit Live-Pool Governor"
section_id: "C.19:0.1"
section_title: "What goes wrong if missed"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19/C.19__003_what-goes-wrong-if-missed.md"
commit_sha: "9a9a42e4d154021ca3f7415e0009a4214832f65f"
heading_path:
  - "C.19 — Explore-Exploit Live-Pool Governor"
  - "C.19:0.1 — What goes wrong if missed"
line_start: 49450
line_end: 49455
dependencies:
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.22.PFR"
  - "C.24"
  - "C.28"
  - "C.32"
  - "C.32.P2S"
  - "C.35"
  - "E.23"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "already-live candidate pool"
  - "change trigger"
  - "explore-exploit"
  - "governing lens"
  - "keep frontier"
  - "narrow to subset"
  - "pool-policy result"
  - "sunset line"
  - "widen"
---

### C.19:0.1 - What goes wrong if missed

- scalarized top-1 picks are mislabeled as "the frontier", so it becomes unclear whether the result names one lens-ranked winner or the admissible live set
- exploration continues without one named pool, one named governing lens, or one explicit next treatment
- local option choice, pool policy, enactment planning, and published shortlist semantics collapse into one blurred result

