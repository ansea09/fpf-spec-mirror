---
chunk_kind: "child"
pattern_id: "A.19.UNM"
pattern_title: "Normalize Coordinate Values under Declared Invariants"
section_id: "A.19.UNM:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.UNM/A.19.UNM__003_problem-frame.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "A.19.UNM — Normalize Coordinate Values under Declared Invariants"
  - "A.19.UNM:1 — Problem frame"
line_start: 38962
line_end: 38973
dependencies:
keywords:
  - "CV→NCV"
  - "NormalizationFixSpec"
  - "NormalizationInvariant[*]"
  - "NormalizationMethodId"
  - "NormalizationMethodInstanceId"
  - "fail-closed tri-state guard (pass\\"
  - "normalization"
  - "validity window (no implicit “latest”)"
  - "≡_UNM"
---

### A.19.UNM:1 - Problem frame

To compare coordinate values, engineers need to establish:
- **What it means** to compare values across charts, slices, bearers, or reference bases, and
- **Which transformations preserve the required distinctions**, with their conditions and losses.

Teams routinely face a mismatch between:
- values that look comparable (“they’re numbers”), and
- values whose comparison basis differs, such as units, observation populations or validity windows. A supported normalization may make the needed values comparable; some differences instead require new measurements or evaluation grounds, a different comparison, or an unresolved result.

CHR distinguishes normalization, indicatorization, scoring, aggregation, comparison and selection. The chosen protocol determines which stages are needed; UNM supplies normalization when that comparison or characterization requires it.

