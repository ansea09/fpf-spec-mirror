---
chunk_kind: "child"
pattern_id: "B.1.4"
pattern_title: "Contextual & Temporal Aggregation (Γ\\_ctx & Γ\\_time)"
section_id: "B.1.4:7"
section_title: "Conformance Checklist (normative checklist)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.4/B.1.4__008_conformance-checklist-normative-checklist.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "B.1.4 — Contextual & Temporal Aggregation (Γ\\_ctx & Γ\\_time)"
  - "B.1.4:7 — Conformance Checklist (normative checklist)"
line_start: 28987
line_end: 29000
dependencies:
  - "A.12"
  - "A.14"
  - "A.15"
  - "B.1"
  - "B.1.1"
keywords:
  - "composition"
  - "order-sensitive"
  - "temporal aggregation"
  - "time-series"
---

### B.1.4:7 - Conformance Checklist (normative checklist)

| ID            | Requirement                                                                                                                                                                     | Purpose                                       |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **CC‑B1.4.1** | **Γ\_ctx** input `D_ctx` SHALL use **only** `SerialStepOf` / `ParallelFactorOf` edges; **Γ\_time** input `D_time` SHALL use **only** `PhaseOf` edges.                           | Keep flavours matched to A.14 edges.          |
| **CC‑B1.4.2** | **OrderSpec `σ`** (for Γ\_ctx) or **TimeWindow `τ`** (for Γ\_time) SHALL be explicitly declared.                                                                                | Determinism and auditability (NC‑1/2, T‑2/3). |
| **CC‑B1.4.3** | An **independence declaration** (Γ\_ctx) or **coverage declaration** (Γ\_time) SHALL be attached, with join‑soundness statements (Γ\_ctx) and non‑overlap proof (Γ\_time).      | Make replaced COMM/LOC discipline explicit.   |
| **CC‑B1.4.4** | **WLNK cutset** SHALL be identified (critical path for Γ\_ctx; critical epoch for Γ\_time).                                                                                     | Conservative bounds.                          |
| **CC‑B1.4.5** | **MONO characteristics** SHALL be listed and justified for the call.                                                                                                                       | Prevent hidden regress.                       |
| **CC‑B1.4.6** | All nodes SHALL share the same `DesignRunTag` (`design` or `run`) in a single fold.                                                                                            | Ban DesignRunTag chimeras.                      |
| **CC‑B1.4.7** | Structural inclusion, mappings, and resource spending SHALL NOT be encoded as order/time edges; route to **Γ\_sys and Γ\_epist**, value-level links, or **Γ\_work** respectively. | Enforce A.15 Strict Distinction.              |
| **CC‑B1.4.8** | If coverage breaks or identity changes, the modeller SHALL refactor the graph or declare a **Meta‑Holon Transition** (B.2).                                                     | Make emergence explicit.                      |


