---
chunk_kind: "child"
pattern_id: "A.19.UNM"
pattern_title: "Normalize Coordinate Values under Declared Invariants"
section_id: "A.19.UNM:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.UNM/A.19.UNM__004_problem.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "A.19.UNM — Normalize Coordinate Values under Declared Invariants"
  - "A.19.UNM:2 — Problem"
line_start: 38974
line_end: 38986
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

### A.19.UNM:2 - Problem

Hidden or inadequately specified normalization causes four recurring difficulties:

1) **Normalization drifts into hidden places.** It gets embedded inside scoring, comparison, or selection, making admissibility and governance non-local.

2) **Comparability becomes rhetorical.** People say “we normalize” but cannot answer:
   *Which method and invariants? Which bearer, comparison basis and scope or window? Which evidence? Does the receiving comparison rely on an obtaining Bridge, kind relation or plane relation?*

3) **Basis and relation changes become invisible.** Teams reuse normalizations for another bearer, comparison basis, source-local meaning, or reference plane without naming what changed or the relation on which the new use depends.

4) **Engineers cannot reconstruct the operation.** Scattered definitions can hide its inputs, result, preservation conditions or limits, preventing a justified reuse.

