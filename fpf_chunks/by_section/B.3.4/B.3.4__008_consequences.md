---
chunk_kind: "child"
pattern_id: "B.3.4"
pattern_title: "Evidence Decay & Epistemic Debt"
section_id: "B.3.4:7"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.4/B.3.4__008_consequences.md"
commit_sha: "7c617d5d0fa1abf94a21bac2dd909f68ed514249"
heading_path:
  - "B.3.4 — Evidence Decay & Epistemic Debt"
  - "B.3.4:7 — Consequences"
line_start: 33235
line_end: 33242
dependencies:
  - "A.10"
  - "B.3"
  - "B.3.3"
  - "B.4"
keywords:
  - "decay"
  - "epistemic debt"
  - "evidence aging"
  - "freshness"
  - "stale data"
---

### B.3.4:7 - **Consequences**

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Freshness honesty:** The framework provides a transparent, quantitative way to track the erosion of trust over time, preventing "assurance rot." | **Process Overhead:** Teams must now manage `valid_until` dates and respond to debt alerts. *Mitigation:* Tooling can automate much of this, suggesting default expiry dates based on evidence-carrier kind and providing one-click actions for the governance loop. |
| **Risk-Informed Maintenance:** Epistemic Debt becomes a leading indicator for maintenance and re-validation planning, allowing teams to allocate resources proactively, not reactively. | **Risk of False Positives:** Overly aggressive decay coefficients (`k`) could create excessive noise. *Mitigation:* The `k` value is configurable, and the `Waive` mechanism provides a safety valve for situations where a formal refresh is not yet warranted. |
| **Enhanced Auditability:** The entire state progression of evidence—from creation to expiry and resolution—is now a traceable, auditable part of the FPF model. | - |

