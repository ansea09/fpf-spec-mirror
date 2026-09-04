---
chunk_kind: "child"
pattern_id: "C.19"
pattern_title: "Explore-Exploit Live-Pool Governor"
section_id: "C.19:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19/C.19__018_relations.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "C.19 — Explore-Exploit Live-Pool Governor"
  - "C.19:12 — Relations"
line_start: 50676
line_end: 50686
dependencies:
  - "A.10"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "B.3"
  - "C.11"
  - "C.11.CRC"
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.22.PFR"
  - "C.24"
  - "C.28"
  - "C.32"
  - "C.32.P2S"
  - "C.35"
  - "E.10.LRN"
  - "E.17"
  - "E.24.PUB"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "already-live candidate pool"
  - "audience availability"
  - "change trigger"
  - "explore-exploit"
  - "governing lens"
  - "keep frontier"
  - "narrow to subset"
  - "pool-policy result"
  - "publication face"
  - "publication occurrence"
  - "selector-facing declaration"
  - "sunset line"
  - "widen"
---

### C.19:12 - Relations

**C.27 temporal-claim relation.**

- C.27 may flag: a temporal claim that changes exploration, exploitation, narrowing, widening, convergence speed, or search cadence in a way that changes admissible use.
- This pattern keeps: pool-policy result and explore and exploit governance, including `keep_frontier`, `narrow_to_subset`, and `sunset_line`.
- Non-admissible use: faster narrowing is not automatically a positive result; it may collapse exploration health, diversity, archive coverage, or frontier discovery.
- Exit: use C.19 for the pool-policy result; use C.27 only for the temporal-claim adequacy question when speed or change affects admissible use.

Builds on: `C.18`, `C.16`, `A.19.CPM`, `A.19.SelectorMechanism`, and `B.3`. Coordinates with: `E.10.LRN` only for unresolved learning-family wording; `A.10` only for actual bounded reliance; `C.22.PFR` for actual Problem identity; `C.18` for generation, Archive, Front, and possibility-space change; `C.32.P2S`, `C.32`, and `C.35` for architecture-alternative carry-through and candidate admission; `C.28` for causal-use support; `C.17` and `G.9` for evaluation and parity inputs; `C.11.CRC` only for a missing finite configuration-relative comparison; `C.11` for local option or probe choice; and the other next-result patterns and transfer values named in `C.19:4.4`.

