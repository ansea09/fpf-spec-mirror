---
chunk_kind: "child"
pattern_id: "C.19"
pattern_title: "Explore-Exploit Live-Pool Governor"
section_id: "C.19:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19/C.19__016_rationale.md"
commit_sha: "d064720b072b822cbb2f1d41e555cf08e2904f11"
heading_path:
  - "C.19 — Explore-Exploit Live-Pool Governor"
  - "C.19:10 — Rationale"
line_start: 49190
line_end: 49197
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

### C.19:10 - Rationale

`C.19` exists because pool governance is neither local choice nor execution. Once several candidate lines remain live, the key question is no longer which single option should survive now; it is how the pool should be governed next under one explicit lens or policy. That question needs its own explicit pool-policy result, otherwise frontier drift, silent scalarization, and policy amnesia return immediately.

- Post-2015 bandit and Bayesian-optimization practice treats explore and exploit policy as an explicit policy object, not as one hidden side effect of whichever candidate looked best first. The practical implication here is to emit one explicit pool treatment plus one change trigger, not one atmospheric frontier story.
- Contemporary frontier and quality-diversity practice also distinguishes the live frontier from any scalarized pick taken under one declared lens. The practical safeguard is to keep `keep_frontier`, `narrow_to_subset`, and `sunset_line` as visible alternatives rather than silently totalizing the pool.
- When an applicable policy independently admits coverage or heterogeneity pressure, keep that pressure explicit until one declared reason justifies retirement or use of a different subject pattern. The practical implication is simple: sunset or name the next subject pattern only when the current pool-policy result can already say why the pool no longer belongs to `C.19`.

