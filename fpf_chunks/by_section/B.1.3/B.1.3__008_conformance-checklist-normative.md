---
chunk_kind: "child"
pattern_id: "B.1.3"
pattern_title: "Knowledge Aggregation (Γ_epist): Synthesis and Target-Scheme Compilation"
section_id: "B.1.3:7"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.3/B.1.3__008_conformance-checklist-normative.md"
commit_sha: "870fb0c2a5dcfe1e0165a111fdf2cf8659c85a54"
heading_path:
  - "B.1.3 — Knowledge Aggregation (Γ_epist): Synthesis and Target-Scheme Compilation"
  - "B.1.3:7 — Conformance Checklist (normative)"
line_start: 41861
line_end: 41873
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
  - "A.7"
  - "B.1"
  - "B.1.1"
  - "B.1.4"
  - "B.1.6"
  - "B.2"
  - "B.3"
  - "C.11"
  - "C.19.2"
  - "C.2"
  - "C.2.1"
  - "E.17"
  - "E.24.PUB"
  - "F.6"
  - "F.9"
  - "U.Work"
keywords:
---

### B.1.3:7 - Conformance Checklist (normative)

| ID            | Requirement                                                                                                                                                         | Purpose                        |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **CC‑B1.3.1** | Every knowledge constituent supplied to Γ\_epist MUST be a `U.Episteme` holon; **ComponentOf** is forbidden; use **ConstituentOf**, **UsageOf**, or **ReferenceTo** for their different claims; use a collection's own belongs-to predicate only for collections. | Prevent category errors. |
| **CC‑B1.3.2** | Material sources, methods and their contributions MUST remain recoverable with the aggregate; preserve any SCR details required by the receiving use. | Preserve source contributions and required reconstruction grounds. |
| **CC‑B1.3.3** | Any aggregate R MUST follow the justified input meanings, scales, support dependencies, and receiving model. No default min, max, or F-to-R conversion is supplied; absent a common model, retain a bounded synthesis and separate support. | Prevent unsupported assurance and preserve useful non-aggregate results. |
| **CC-B1.3.4** | Contrary evidence MUST remain visible. An established scope or interpretation difference may separate claims; an unresolved conflict must qualify, narrow, or defeat the affected conclusion. Use B.2 only for a separately grounded whole-reidentification question. | Keep the practical effect of disagreement visible. |
| **CC‑B1.3.5** | Any mode declaration consumed by the receiving use **MUST** follow that use's rule and the support operative in the claimed conclusion. Under the axiomatic/postulative distinction, an operative postulative input makes that conclusion postulative; separately supported formal subclaims remain usable. | Preserve the relevant warrant distinction without substituting a tag for support. |
| **CC-B1.3.6** | A cross-context meaning use names explicit mappings, exact source and receiving F.17 cells, an obtaining F.9 Bridge, a separate bounded-use claim and permitted loss, and the ordinary A.10 evidence-provenance path and same-use `RelianceDisposition` required by F.9:4.2. An actual named assurance claim additionally requires its B.3 result for that same bounded assurance use. **CL** alone never grants the use. | Make semantic crossing inspectable. |
| **CC-B1.3.7** | An order-dependent conclusion MUST meet PO-SYN-ORDER and B.1.4:4. If an episteme history matters, exact C.2.1 endpoint identities and any obtaining `EpistemeEditionRelation` MUST be named; any proper restriction or B.1.4/**Γ_time** aggregation MUST cite only already recovered temporal relations. | Preserve order, identity, continuity, and temporal integrity. |
| **CC-B1.3.8** | Keep design-time synthesis, target-scheme compilation, one actual operation application and its returned value, dated Work, performer and any relied-on assignment, production or first existence, publication, carrier, release, and acceptance separately governed. | Preserve semantic and practical boundaries. |

