---
chunk_kind: "child"
pattern_id: "C.19"
pattern_title: "Explore-Exploit Live-Pool Governor"
section_id: "C.19:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19/C.19__018_relations.md"
commit_sha: "1602a8d0a6934a99a79ead914610b070cedd86d2"
heading_path:
  - "C.19 — Explore-Exploit Live-Pool Governor"
  - "C.19:12 — Relations"
line_start: 50015
line_end: 50025
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

### C.19:12 - Relations

**C.27 temporal-claim relation.**

- C.27 may flag: a temporal claim that changes exploration, exploitation, narrowing, widening, convergence speed, or search cadence in a way that changes admissible use.
- This pattern keeps: pool-policy result and explore and exploit governance, including `keep_frontier`, `narrow_to_subset`, and `sunset_line`.
- Non-admissible use: faster narrowing is not automatically a positive result; it may collapse exploration health, diversity, archive coverage, or frontier discovery.
- Exit: use C.19 for the pool-policy result; use C.27 only for the temporal-claim adequacy question when speed or change affects admissible use.

Builds on: `C.18`, `C.16`, `A.19.CPM`, `A.19.SelectorMechanism`, and `B.3`. Coordinates with: `C.22.PFR` for actual Problem identity, `E.23` for declared improvement loops, `C.11` for local choice among already-available options, `C.18` for candidate generation and archive/front stewardship, `C.32.P2S` when pool policy preserves architecture alternatives for problem-to-structure carry-through, `C.32` for candidate palette ownership, `C.35` when generated or discovered structure-bearing outputs need admission support before pool policy can use them, `C.24` and the A.15 family for planning and performed work, `G.5` for selector-facing publication, `G.11` for refresh, `C.28` for causal-use support, `C.17`, and `G.9`.

