---
chunk_kind: "child"
pattern_id: "B.3.4"
pattern_title: "Evidence Decay & Epistemic Debt"
section_id: "B.3.4:5"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.4/B.3.4__006_conformance-checklist.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "B.3.4 — Evidence Decay & Epistemic Debt"
  - "B.3.4:5 — Conformance Checklist"
line_start: 31139
line_end: 31146
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

### B.3.4:5 - **Conformance Checklist**

*   **CC-ED.1 (Freshness Mandate):** Every evidence carrier anchored via `verifiedBy` or `validatedBy` **MUST** include a `valid_until` attribute. A value of `null` (perpetual) **MUST** be justified in the evidence carrier's rationale.
*   **CC-ED.2 (Debt Budget Mandate):** Every project or `U.System` at `AssuranceLevel:L1` or higher **MUST** declare an `epistemic_debt_budget` in its manifest.
*   **CC-ED.3 (Aggregation Mandate):** The total Epistemic Debt of a composite holon **MUST** be the sum of the debt of its constituent parts, consistent with the aggregation rule `ED_t(S) = Σ_j ED_t(child_j)`.
*   **CC-ED.4 (Downgrade Mandate):** An assurance target with `ED_t > epistemic_debt_budget` **SHALL** have its effective `AssuranceLevel` provisionally downgraded until the debt is resolved via `Refresh`, `Deprecate`, or `Waive`.
*   **CC-ED.5 (Waiver Auditability):** Any `Waive` action **MUST** be recorded as a formal, auditable event, citing the responsible authority, the rationale, and a new, short-term expiry date for the waiver itself.

