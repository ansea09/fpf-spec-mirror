---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transduction Graph Architecture (E.TGA)"
section_id: "E.18:11"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__012_rationale.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "E.18 — Transduction Graph Architecture (E.TGA)"
  - "E.18:11 — Rationale"
line_start: 62996
line_end: 63006
dependencies:
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.7"
  - "E.10"
  - "E.17"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "CSLC normalize-then-compare"
  - "CV⇒GF (ConstraintValidity → GateFit)"
  - "DesignRunTag"
  - "MVPK faces"
  - "OperationalGate(profile)"
  - "PathSlice/Sentinel refresh"
  - "Set-return selection"
  - "SquareLaw"
  - "UNM declaration locus"
  - "edge=U.Transfer (single-edge kind)"
  - "nodes=morphisms"
  - "transduction graph"
---

### E.18:11 - Rationale

E.TGA states **strict separation of concerns** (graph-architecture scope only); **specialized semantics are governed by the current neighboring patterns named below**:

* **What the graph is:** typed intensional morphisms and the single graph edge kind `U.Transfer`.
* **Where/when it crosses contexts:** **only** at `OperationalGate(profile)`, with Bridge+UTS, CL/CL^plane, and Φ published in R-lane.
* **How comparability works:** UNM is the single governing locus for unit, plane, and transport declarations, and selectors operate **only** on normalized, edition-pinned comparators, returning sets or archives rather than totals. Edition-aware pins and archive semantics are checked through `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` when live.
* **How change propagates:** sentinel‑bounded `PathSlice` refresh; editions are monotone; LaunchGate is the only binder of launch‑values.

This arrangement gives checkable conditions for **functorial publication** (commuting squares on crossings) and **orthogonality** of inner technical validity (ConstraintValidity) to context fit (GateFit), which in turn keeps gate aggregation **order-independent** under the CV=>GF activation predicate.

