---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transformation Flow Structure"
section_id: "E.18:11"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__014_rationale.md"
commit_sha: "5801dc610c657ac7b1efee349b18e80ce6d7df6f"
heading_path:
  - "E.18 — Transformation Flow Structure"
  - "E.18:11 — Rationale"
line_start: 82861
line_end: 82871
dependencies:
  - "A.15.1"
  - "A.15.PROD"
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.3.4"
  - "A.6.RCD"
  - "A.7"
  - "C.29"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.17"
  - "E.18.1"
  - "E.18.2"
  - "E.18.NET"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
---

### E.18:11 - Rationale

E.18 states **strict separation of concerns** (selected-structure scope only); **the patterns named below supply the definitions and tests for those current relations**:

* **What the selected structure is:** structure-positioned transformation and slot-filler loci plus the single relation kind `U.Transfer`; graph, morphism, tuple, category, or algebra language is used only when a current mathematical description or lens expresses the relation.
* **Where and when structural state changes:** only at one `OperationalGate(profile)`, with exact source and receiving positions, changed `CtxState` bindings, a per-binding account for each change, and `CrossingRef`. GateDecision and any permission claim remain separate; an F.9 Bridge, bounded-use claim, reliance, optional card, and optional `CL` appear only for a separately established cross-semantic use.
* **How comparability works:** UNM is the single declaration locus for unit, plane, and transport declarations, and selectors operate **only** on normalized, edition-pinned comparators, returning sets or archives rather than totals. Edition-aware pins and archive semantics are checked through `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` for current selector or archive cases.
* **How change propagates:** sentinel-bounded `PathSlice` refresh; editions are monotone. When the selected structure contains an exact current `LaunchGate` relation for one prospective `workEntryClaimRef`, that gate is the pre-run decision locus for that claim. Actual launch values are established only through independently obtaining direct relations or A.6.1 bindings involving a later Work occurrence and may be cited by a separate finalization witness.

This arrangement gives checkable conditions for functorial publication on crossings and keeps inner constraint validity distinct from profile fit. A.21 can therefore aggregate mapped check results without evaluation order changing which independently established facts remain available.

