---
chunk_kind: "child"
pattern_id: "A.19.UNM"
pattern_title: "Normalize Coordinate Values under Declared Invariants"
section_id: "A.19.UNM:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.UNM/A.19.UNM__005_forces.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "A.19.UNM — Normalize Coordinate Values under Declared Invariants"
  - "A.19.UNM:3 — Forces"
line_start: 38987
line_end: 38997
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

### A.19.UNM:3 - Forces

| Force | Tension |
|---|---|
| **Evolvability vs Usability** | A stable operation contract supports evolving method families; readers still need to find the selected method and its conditions. |
| **Semantic precision vs Cognitive load** | Formal invariants/quotients ↔ a mechanism description that engineers can act on. |
| **Shared definitions vs Connected use** | UNM uses CN-Spec, CG-Spec and any required relation claims; each retains its own governing definition. |
| **Trustworthiness vs Overreach** | Evidence must support the normalization used; measurement meaning and calibration retain their own grounds. |
| **Locality vs Reuse** | A normalized value retains its declared bearer, basis, scope/window and use; a later use may require another relation or normalization. |
| **Fail-closed safety vs Convenience** | Unknown/insufficient evidence must not coerce ↔ teams want “a number anyway”. |

