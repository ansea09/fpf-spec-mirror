---
chunk_kind: "child"
pattern_id: "A.20"
pattern_title: "U.Flow.ConstraintValidity — Eulerian"
section_id: "A.20:8"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.20/A.20__010_consequences.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "A.20 — U.Flow.ConstraintValidity — Eulerian"
  - "A.20:8 — Consequences"
line_start: 27327
line_end: 27338
dependencies:
  - "A.19.SelectorMechanism"
  - "A.21"
  - "C.18"
  - "C.19"
  - "E.17"
  - "E.18"
  - "E.TGA"
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
  - "TransductionFlow"
  - "flow"
---

### A.20:8 - Consequences

**Benefits.**
*Clarity & composability.* Mechanism descriptions remain limited to internal laws; gates are the sole policy junction.

*Replayability.* With valuation plus MVPK pins, re-runs under fixed `E⃗` are comparable and slice-scoped through `E.18`, `A.20`, and `G.11` when refresh wiring is live.
*Didactic hygiene.* Readers can see what is internal mechanism constraint status vs. gate policy.

**Trade‑offs.**

* Two places to look (CV vs. GF) impose placement discipline; mitigated by the activation predicate and MVPK links.

