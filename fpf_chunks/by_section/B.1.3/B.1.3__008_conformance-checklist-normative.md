---
chunk_kind: "child"
pattern_id: "B.1.3"
pattern_title: "Γ_epist - Knowledge‑Specific Aggregation"
section_id: "B.1.3:7"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.3/B.1.3__008_conformance-checklist-normative.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "B.1.3 — Γ_epist - Knowledge‑Specific Aggregation"
  - "B.1.3:7 — Conformance Checklist (normative)"
line_start: 31511
line_end: 31523
dependencies:
  - "A.1"
  - "A.12"
  - "A.14"
  - "A.15"
  - "B.1"
  - "B.1.1"
  - "B.1.4"
  - "B.1.6"
  - "B.3"
  - "C.2"
keywords:
  - "KD-CAL"
  - "epistemic"
  - "knowledge aggregation"
  - "provenance"
  - "trust"
---

### B.1.3:7 - Conformance Checklist (normative)

| ID            | Requirement                                                                                                                                                         | Purpose                        |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **CC‑B1.3.1** | Inputs to Γ\_epist MUST be `U.Episteme` holons; **ComponentOf** is forbidden; use **ConstituentOf / UsageOf / ReferenceTo**; **MemberOf** only for **collections**. | Prevent category errors.       |
| **CC‑B1.3.2** | Provenance and **SCR** MUST be preserved in the aggregate; dropping sources or methods is non‑conformant.                                                      | Enforce Evidence Graph Referring.    |
| **CC‑B1.3.3** | Aggregate **R** MUST follow the **pathwise min** rule with **Φ(CL\_min)** penalties; no averaging of reliability.                                                   | Guard conservatism (WLNK).     |
| **CC‑B1.3.4** | Contradictions MUST NOT be smoothed by arithmetic; handle by **scope separation**, **provisional** status, or **MHT**.                                              | Keep incoherence visible.      |
| **CC‑B1.3.5** | Every `U.Episteme` serving as an input to `Γ_epist` **MUST** declare its `mode` (`axiomatic` or `postulative`). An aggregate holon's mode **MUST** be `postulative` if any of its constituents is `postulative`. | Prevent category errors in reliability calculation. |
| **CC‑B1.3.6** | Crossing bounded contexts requires either **explicit mappings with CL** or an **MHT (Context Reframe)**.                                                            | Make context explicit.         |
| **CC‑B1.3.7** | If order matters, Γ\_ctx **NC‑1..3** MUST hold; if versions matter, the **Γ\_time** slice MUST be identified.                                                       | Preserve order/time integrity. |
| **CC‑B1.3.8** | Design‑time **synthesis** and run‑time **compilation** MUST NOT be conflated; use the appropriate flavour.                                                          | Maintain A.15 separation.      |

