---
chunk_kind: "child"
pattern_id: "A.19.UNM"
pattern_title: "Normalize Coordinate Values under Declared Invariants (UNM)"
section_id: "A.19.UNM:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.UNM/A.19.UNM__001_intro.md"
commit_sha: "3dae70bd0ef74188bc5ed0414e6630331457d07b"
heading_path:
  - "A.19.UNM — Normalize Coordinate Values under Declared Invariants (UNM)"
  - "A.19.UNM:intro — Intro"
line_start: 34657
line_end: 34671
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

## A.19.UNM - Normalize Coordinate Values under Declared Invariants (UNM)

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative (unless explicitly marked informative)
> **Placement:** Part A / CN‑Spec cluster (A.19) / CHR mechanism-governing patterns
> **Boundary:** A.19.CN defines the CN-Spec fields that select normalization and comparability. This pattern defines the normalization operation and how it uses those fields.

**If someone says “we normalized”, ask (in this order):**
1) Which **`UNM_id`** (if applicable) and which **`NormalizationMethodInstanceId`** (and its validity window) was used?
2) Which **`NormalizationInvariant[*]`** were declared (i.e., *what is preserved*)?
3) Which **bearer, scope/window, reference or comparison basis, evidence, and intended comparison** were recorded, and does this use actually rely on an F.9 Bridge, kind relation, or plane relation?

**Mental model.** UNM applies a declared directed transformation from an input coordinate value (`CV`) to an output (`NCV`). State its domain, target and preserved or lost distinctions. An inverse, an equality-of-output class or an operation on those classes is a narrower result requiring its own conditions.

