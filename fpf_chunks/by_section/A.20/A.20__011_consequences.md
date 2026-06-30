---
chunk_kind: "child"
pattern_id: "A.20"
pattern_title: "Flow Constraint Validity — Eulerian"
section_id: "A.20:8"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.20/A.20__011_consequences.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "A.20 — Flow Constraint Validity — Eulerian"
  - "A.20:8 — Consequences"
line_start: 30080
line_end: 30091
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

### A.20:8 - Consequences

**Benefits.**
*Clarity & composability.* Mechanism descriptions remain limited to internal laws; gates are the sole policy junction.

*Replayability.* With valuation plus MVPK pins, re-runs under fixed `E⃗` are comparable and slice-scoped through `E.18`, `A.20`, and `G.11` when refresh wiring is present.
*Didactic hygiene.* Readers can see what is step-local mechanism constraint plus `CV.Status` vs. gate policy.

**Trade‑offs.**

* Two places to look (CV vs. GF) impose placement discipline; mitigated by the activation predicate and MVPK links.

