---
chunk_kind: "child"
pattern_id: "B.3.3"
pattern_title: "Assurance Subtypes & Levels"
section_id: "B.3.3:7"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.3/B.3.3__008_rationale.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "B.3.3 — Assurance Subtypes & Levels"
  - "B.3.3:7 — Rationale"
line_start: 34954
line_end: 34957
dependencies:
  - "A.10"
  - "A.19"
  - "A.4"
  - "B.3"
  - "B.4"
  - "C.16"
  - "C.2.1"
  - "D.4"
  - "U.Episteme"
keywords:
  - "L0-L2"
  - "LA"
  - "TA"
  - "VA"
  - "assurance levels"
  - "typing"
  - "validation"
  - "verification"
---

### B.3.3:7 - **Rationale**

This pattern transforms the assurance framework from a descriptive taxonomy into a prescriptive, actionable Standard. By binding the computed `AssuranceLevel` to mandatory, well-defined evidence coverage, it makes the notion of "trustworthiness" in FPF an objective and auditable property. The rules ensure that as an assurance target's formality and claimed reliability increase, the rigor and balance of its supporting evidence increase in lockstep, operationalizing the principle of "no blind trust." The separation of `design-time` and `run-time` evidence, mandated by CC-B3.3.5, further ensures that claims made about a blueprint are not confused with claims made about a running system, preserving the integrity of the whole design-time and run-time evidence history.

