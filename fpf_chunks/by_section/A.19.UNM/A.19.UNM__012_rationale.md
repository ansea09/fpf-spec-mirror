---
chunk_kind: "child"
pattern_id: "A.19.UNM"
pattern_title: "Normalize Coordinate Values under Declared Invariants (UNM)"
section_id: "A.19.UNM:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.UNM/A.19.UNM__012_rationale.md"
commit_sha: "4260875dd8bc4595bbca3b6dbfa61e6f35afa013"
heading_path:
  - "A.19.UNM — Normalize Coordinate Values under Declared Invariants (UNM)"
  - "A.19.UNM:10 — Rationale"
line_start: 37815
line_end: 37824
dependencies:
keywords:
  - "CV→NCV"
  - "NormalizationFixSpec"
  - "NormalizationInvariant[*]"
  - "NormalizationMethodId"
  - "NormalizationMethodInstanceId"
  - "fail-closed tri-state guard (pass"
  - "normalization"
  - "validity window (no implicit “latest”)"
  - "≡_UNM"
---

### A.19.UNM:10 - Rationale

UNM separates three contributions needed to justify a normalized value:
- The selected transformation defines its actual domain, output and preservation/loss conditions.
- CN-Spec states when normalization is needed and which configured method applies to the comparison.
- C.16 supplies measurement and calibration grounds for that use.
The receiving use determines which distinctions must survive and whether a relation to another meaning, kind or plane is required. Those relations and any assurance calculation retain their own conditions; a common numeric range supplies none of these grounds.



