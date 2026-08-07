---
chunk_kind: "child"
pattern_id: "C.19"
pattern_title: "Explore-Exploit Live-Pool Governor"
section_id: "C.19:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19/C.19__016_rationale.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "C.19 — Explore-Exploit Live-Pool Governor"
  - "C.19:10 — Rationale"
line_start: 50007
line_end: 50014
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

### C.19:10 - Rationale

`C.19` exists because pool governance is neither local choice nor execution. Once several candidate lines remain live, the key question is no longer which single option should survive now; it is how the pool should be governed next under one explicit lens or policy. That question needs its own explicit pool-policy result, otherwise frontier drift, silent scalarization, and policy amnesia return immediately.

- Post-2015 bandit and Bayesian-optimization practice treats explore and exploit policy as an explicit policy object, not as one hidden side effect of whichever candidate looked best first. The practical implication here is to emit one explicit pool treatment plus one change trigger, not one atmospheric frontier story.
- Contemporary frontier and quality-diversity practice also distinguishes the live frontier from any scalarized pick taken under one declared lens. The practical safeguard is to keep `keep_frontier`, `narrow_to_subset`, and `sunset_line` as visible alternatives rather than silently totalizing the pool.
- When a context independently admits coverage or heterogeneity pressure, C.19 keeps that pressure explicit until one declared reason justifies retirement or use of a different governing pattern. The practical implication is simple: sunset or name the next governing pattern only when the current pool-policy result can already say why the pool no longer belongs to `C.19`.

