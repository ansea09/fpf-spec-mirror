---
chunk_kind: "child"
pattern_id: "B.1.3"
pattern_title: "Γ_epist - Knowledge‑Specific Aggregation"
section_id: "B.1.3:7"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.3/B.1.3__008_conformance-checklist-normative.md"
commit_sha: "421266f0a37ab295b1ffd9e214ace6541e21f5be"
heading_path:
  - "B.1.3 — Γ_epist - Knowledge‑Specific Aggregation"
  - "B.1.3:7 — Conformance Checklist (normative)"
line_start: 37183
line_end: 37195
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.13"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.15.PROD"
  - "A.6.1"
  - "B.1"
  - "B.1.1"
  - "B.1.4"
  - "B.1.6"
  - "B.2"
  - "B.3"
  - "C.2"
  - "C.2.1"
  - "E.17"
  - "E.24.PUB"
  - "F.6"
  - "F.9"
  - "U.Work"
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
| **CC‑B1.3.1** | Inputs to Γ\_epist MUST be `U.Episteme` holons; **ComponentOf** is forbidden; use **ConstituentOf**, **UsageOf**, or **ReferenceTo** for their different claims; use a collection's own belongs-to predicate only for collections. | Prevent category errors. |
| **CC‑B1.3.2** | Provenance and **SCR** MUST be preserved in the aggregate; dropping sources or methods is non‑conformant.                                                      | Enforce Evidence Graph Referring.    |
| **CC‑B1.3.3** | Aggregate **R** MUST follow the **pathwise min** rule with **Φ(CL\_min)** penalties; no averaging of reliability.                                                   | Guard conservatism (WLNK).     |
| **CC-B1.3.4** | Contradictions MUST NOT be smoothed by arithmetic; handle them by exact scope or interpretation-basis separation, **provisional** status, or B.2 only for a separately grounded whole-reidentification question. | Keep incoherence visible. |
| **CC‑B1.3.5** | Every `U.Episteme` serving as an input to `Γ_epist` **MUST** declare its `mode` (`axiomatic` or `postulative`). An aggregate holon's mode **MUST** be `postulative` if any of its constituents is `postulative`. | Prevent category errors in reliability calculation. |
| **CC-B1.3.6** | A cross-context meaning use names explicit mappings, exact source and receiving F.17 cells, an obtaining F.9 Bridge, a separate bounded-use claim and permitted loss, and any reliance result the fold consumes. **CL** alone never grants the use. | Make semantic crossing inspectable. |
| **CC‑B1.3.7** | If order matters, Γ\_ctx **NC‑1..3** MUST hold. If an episteme history matters, exact C.2.1 endpoint identities and any obtaining `EpistemeEditionRelation` MUST be named; any proper restriction or B.1.4/**Γ\_time** aggregation MUST cite only already recovered temporal relations. | Preserve order, identity, continuity, and temporal integrity. |
| **CC-B1.3.8** | Keep design-time synthesis, target-scheme compilation, one actual operation application and its returned value, dated Work, performer and any relied-on assignment, production or first existence, publication, carrier, release, and acceptance separately governed. | Preserve semantic and practical boundaries. |

