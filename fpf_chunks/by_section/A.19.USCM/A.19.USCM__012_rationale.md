---
chunk_kind: "child"
pattern_id: "A.19.USCM"
pattern_title: "Scoring Mechanism"
section_id: "A.19.USCM:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.USCM/A.19.USCM__012_rationale.md"
commit_sha: "cadc8eb15721be464193af85206e345f34a64b04"
heading_path:
  - "A.19.USCM — Scoring Mechanism"
  - "A.19.USCM:10 — Rationale"
line_start: 40104
line_end: 40114
dependencies:
keywords:
  - "CG-Spec.MinimalEvidence"
  - "CSLC-lawful transforms"
  - "ScaleComplianceProfile (SCP)"
  - "ScoringMethodDescription"
  - "score profile"
  - "scoring"
  - "tri-state admissibility (pass\\"
---

### A.19.USCM:10 - Rationale

Scoring can lose semantic precision through hidden normalization, illegal arithmetic, implicit thresholds or uncertainty coercion. USCM requires the following commitments to remain explicit:

* **Admissibility first:** transformations satisfy the restrictions in `CG‑Spec.SCP` and CSLC.
* **No hidden steps:** normalization is explicit (UNM), aggregation is explicit (ULSAM), ordering is explicit (CPM/SelectorMechanism).
* **Uncertainty is visible:** admissibility is tri‑state; unknown is not coerced.
* **Recoverable audit basis:** effective editions and the effective evidence policy remain traceable.



