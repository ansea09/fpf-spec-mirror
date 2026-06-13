---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transformation Flow Structure"
section_id: "E.18:11"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__012_rationale.md"
commit_sha: "cb17c555f343780e31e5fea236a74adc69295736"
heading_path:
  - "E.18 — Transformation Flow Structure"
  - "E.18:11 — Rationale"
line_start: 67885
line_end: 67895
dependencies:
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.3.4"
  - "A.7"
  - "C.29"
  - "C.30.TGA-FLOW-REL"
  - "E.10"
  - "E.17"
  - "E.18.1"
  - "E.18.2"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "P2W support"
  - "composition"
  - "crossings"
  - "flow valuation"
  - "guards"
  - "selected transformations"
  - "transformation flow structure"
---

### E.18:11 - Rationale

E.18 states **strict separation of concerns** (selected-structure scope only); **specialized semantics are governed by the patterns named below for those current relations**:

* **What the selected structure is:** structure-positioned transformation and slot-filler loci plus the single relation kind `U.Transfer`; graph, morphism, tuple, category, or algebra language is used only when a current mathematical description or lens expresses the relation.
* **Where/when it crosses contexts:** **only** at `OperationalGate(profile)`, with Bridge+UTS, CL/CL^plane, and Φ published in R-lane.
* **How comparability works:** UNM is the single governing locus for unit, plane, and transport declarations, and selectors operate **only** on normalized, edition-pinned comparators, returning sets or archives rather than totals. Edition-aware pins and archive semantics are checked through `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` for current selector or archive cases.
* **How change propagates:** sentinel‑bounded `PathSlice` refresh; editions are monotone; LaunchGate is the only binder of launch‑values.

This arrangement gives checkable conditions for **functorial publication** (commuting squares on crossings) and **orthogonality** of inner technical validity (ConstraintValidity) to context fit (GateFit), which in turn keeps gate aggregation **order-independent** under the CV=>GF activation predicate.

