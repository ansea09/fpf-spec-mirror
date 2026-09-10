---
chunk_kind: "child"
pattern_id: "D.5"
pattern_title: "Bias Audit and Ethical Assurance"
section_id: "D.5:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/D.5/D.5__011_conformance-checklist.md"
commit_sha: "a87d0ef4f3712507edd6e5a59f4de5bf7a55905a"
heading_path:
  - "D.5 — Bias Audit and Ethical Assurance"
  - "D.5:7 — Conformance Checklist"
line_start: 70026
line_end: 70034
dependencies:
  - "A.10"
  - "B.3"
  - "C.11.DUA"
  - "C.16"
  - "C.28"
  - "D.1"
  - "D.2"
  - "D.3"
  - "D.4"
  - "E.13"
  - "E.17"
  - "E.5.4"
keywords:
---

### D.5:7 - Conformance Checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| CC-D5-1 | The result names the audited EntityOfConcern, intended use, affected populations or Systems, and the bias, fairness, impact, or ethical concern being answered. Relied-on evidence and material limitations qualify its warranted use. Assurance use, repair return, ClaimScope, and qualification window are explicit when they delimit the audit; record and investigation depth follow the particular reliance in §3.1. | Keeps audit scope inspectable. |
| CC-D5-2 | Metric, causal fairness, evidence, assurance, publication, and architecture-residual claims use their direct owners. | Prevents D.5 from swallowing neighboring patterns. |
| CC-D5-3 | Ethical assurance is recorded as assurance or evidence relation, not moral permission. | Keeps assurance from becoming ethical authorization. |
| CC-D5-4 | If the audit exposes interlevel conflict, use D.3 for the conflict description and D.4 for mediation or decision use. | Keeps D.5 connected to the D cluster without replacing it. |

