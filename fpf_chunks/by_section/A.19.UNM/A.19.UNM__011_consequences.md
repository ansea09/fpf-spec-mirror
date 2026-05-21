---
chunk_kind: "child"
pattern_id: "A.19.UNM"
pattern_title: "Unified Normalization Mechanism (UNM)"
section_id: "A.19.UNM:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.UNM/A.19.UNM__011_consequences.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "A.19.UNM — Unified Normalization Mechanism (UNM)"
  - "A.19.UNM:9 — Consequences"
line_start: 25379
line_end: 25390
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
- Prevents silent illegality (unit, scale, and plane errors) by fail-closed guards.

**Costs**
- Requires explicit declarations (method instance, invariants, validity window, evidence pins).
- Some workflows must learn quotient/fix thinking (a conceptual overhead).

