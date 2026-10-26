---
chunk_kind: "child"
pattern_id: "A.19.UNM"
pattern_title: "Normalize Coordinate Values under Declared Invariants (UNM)"
section_id: "A.19.UNM:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.UNM/A.19.UNM__011_consequences.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "A.19.UNM — Normalize Coordinate Values under Declared Invariants (UNM)"
  - "A.19.UNM:9 — Consequences"
line_start: 37506
line_end: 37517
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

### A.19.UNM:9 - Consequences

**Benefits**
- Makes “normalize-then-compare” a first-class governance choice.
- Centralizes governing-pattern assignment, improving usability and reducing drift.
- Supports evolvability: method families can evolve via packs/extensions without mutating the mechanism surface.
- Makes known admission failures explicit through the declared guard result; correctness still depends on the grounds used by the evaluation.

**Costs**
- Requires explicit declarations (method instance, invariants, validity window, evidence pins).
- Class-level use requires compatibility/query arguments; ordinary transformed-value use need not construct a quotient or fix.

