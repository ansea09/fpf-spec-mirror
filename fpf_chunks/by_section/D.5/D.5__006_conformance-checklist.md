---
chunk_kind: "child"
pattern_id: "D.5"
pattern_title: "Bias-Audit & Ethical Assurance"
section_id: "D.5:5"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/D.5/D.5__006_conformance-checklist.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "D.5 — Bias-Audit & Ethical Assurance"
  - "D.5:5 — Conformance Checklist"
line_start: 55822
line_end: 55833
dependencies:
  - "B.3"
  - "B.3.3"
  - "C.28"
  - "E.5.4"
keywords:
  - "AI ethics"
  - "assurance"
  - "audit"
  - "bias"
  - "ethics"
  - "fairness"
  - "responsible AI"
  - "review cycle"
  - "taxonomy"
---

### D.5:5 - **Conformance Checklist**

*   **CC-D5.1 (Cycle Mandate):** Any project developing a holon that interacts with or makes decisions about humans **MUST** conduct the Bias-Audit Cycle.
*   **CC-D5.2 (Artifact Mandate):** The project **MUST** maintain a **Bias Register** and produce a **Bias-Audit Report** before any major release.
*   **CC-D5.3 (Blocking Issue Mandate):** A release **SHALL NOT** be considered conformant if its latest Bias-Audit Report contains any unresolved findings with `status: blocking`. The issue must either be moved to `resolved` (mitigated) or `risk-accepted` (formally signed off by a designated authority).
*   **CC-D5.4 (Role Mandate):** The Panel Review (BA-2) **MUST** involve at least three individuals representing distinct perspectives, ideally aligning with the roles of *Ethicist*, *Domain Sociologist*, and *UX Design Critic* from the Intellect Stack.
*   **CC-D5-CF-1:** A fairness claim MUST declare whether it is associative, interventional, or counterfactual.
*   **CC-D5-CF-2:** An interventional-action-rung fairness proxy MUST NOT be published as a counterfactual-rung fairness result.
*   **CC-D5-CF-3:** If a counterfactual fairness estimand is claimed actionable, it MUST cite `CausalIdentificationProfile` or `CounterfactualSamplingRealizabilityProfile`.
*   **CC-D5-CF-4:** A causal fairness audit MUST cite `C.28` for causal-use question, causality-ladder rung, causal estimand, causal evidence support basis, identification, realizability, evidence design, `causalUseSupportRecordRef` when one is consumed, and `CausalUseSupportVerdict`; `D.5` keeps ethical audit and fairness assurance.
*   **CC-D5-CF-5:** A local causal-fairness wording repair or support-reference repair does not trigger the full Bias-Audit Cycle unless `D.5` project, release, assurance, or human/group-impact audit conditions are live.

