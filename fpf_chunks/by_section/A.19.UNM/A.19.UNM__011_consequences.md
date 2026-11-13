---
chunk_kind: "child"
pattern_id: "A.19.UNM"
pattern_title: "Normalize Coordinate Values under Declared Invariants"
section_id: "A.19.UNM:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.UNM/A.19.UNM__011_consequences.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "A.19.UNM — Normalize Coordinate Values under Declared Invariants"
  - "A.19.UNM:9 — Consequences"
line_start: 39321
line_end: 39332
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

### A.19.UNM:9 - Consequences

**Benefits**
- Makes the selected normalization and comparison basis inspectable.
- Separates the common operation contract from each method's definition and applicability.
- Allows a method family to change without changing the common operation contract when its meanings and conditions remain compatible.
- Makes known admission failures explicit through the declared guard result; correctness still depends on the grounds used by the evaluation.

**Costs**
- Requires declarations (method instance, invariants, validity window, evidence pins).
- Class-level use requires compatibility/query arguments; ordinary transformed-value use need not construct a quotient or fix.

