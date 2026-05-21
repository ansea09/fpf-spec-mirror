---
chunk_kind: "child"
pattern_id: "C.19"
pattern_title: "Explore–Exploit Governor (E/E‑LOG)"
section_id: "C.19:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19/C.19__017_relations.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "C.19 — Explore–Exploit Governor (E/E‑LOG)"
  - "C.19:12 — Relations"
line_start: 40896
line_end: 40906
dependencies:
  - "B.3"
  - "C.11"
  - "C.17"
  - "C.18"
  - "C.24"
  - "C.28"
  - "G.5"
  - "G.9"
keywords:
  - "DecisionSubject clarification"
  - "EmitterPolicy"
  - "InsertionPolicy"
  - "dominance default routing"
  - "explore-exploit"
  - "keep frontier"
  - "lens id"
  - "live candidate pool"
  - "narrow to subset"
  - "pool-policy result"
  - "reroute"
  - "sunset line"
  - "widen"
---

### C.19:12 - Relations

**C.27 temporal-claim relation.**

- C.27 may flag: a temporal claim that changes exploration, exploitation, narrowing, widening, convergence speed, or search cadence in a way that changes admissible use.
- This pattern keeps: pool-policy result and explore/exploit governance, including `keep frontier`, `narrow to subset`, and `sunset line`.
- Non-admissible use: faster narrowing is not automatically a positive result; it may collapse exploration health, diversity, archive coverage, or frontier discovery.
- Exit: use C.19 for the pool-policy result; use C.27 only for the temporal-claim adequacy question when speed or change affects admissible use.

Builds on: `Decsn-CAL`, `B.3`. Coordinates with: `C.11` for local choice among already-available options, `C.18` for candidate generation and open-ended search, `C.24` for post-choice enactment planning, `G.5` for selector-facing publication, `C.28` for causal-use question/rung/support vocabulary when pool policy is used causally, `C.17`, and `G.9`.

