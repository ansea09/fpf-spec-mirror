---
chunk_kind: "child"
pattern_id: "A.19.UNM"
pattern_title: "Normalize Coordinate Values under Declared Invariants"
section_id: "A.19.UNM:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.UNM/A.19.UNM__001_intro.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "A.19.UNM — Normalize Coordinate Values under Declared Invariants"
  - "A.19.UNM:intro — Intro"
line_start: 38919
line_end: 38934
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

## A.19.UNM - Normalize Coordinate Values under Declared Invariants

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative (unless marked informative)
> **Boundary:** A.19.CN defines the CN-Spec fields that select normalization and comparability. This pattern defines the normalization operation and how it uses those fields.

**Use this when** a coordinate value must be re-expressed for a declared comparison or characterization use. First recover the input, selected transformation and the distinctions the receiver needs. If direct comparison already has an adequate common basis, use it without introducing normalization.

**For a claimed normalization, recover:**
1) Which **`UNM_id`** (if applicable) and which **`NormalizationMethodInstanceId`** (and its validity window) was used?
2) Which **`NormalizationInvariant[*]`** were declared (i.e., *what is preserved*)?
3) Which **bearer, reference or comparison basis, evidence and intended use** qualify the value, including any scope or data window? Does the receiving use rely on an obtaining F.9 Bridge, kind relation or plane relation?

**Mental model.** UNM applies a declared directed transformation from an input coordinate value (`CV`) to an output (`NCV`). State its domain, target and preserved or lost distinctions. An inverse, an equality-of-output class or an operation on those classes is a narrower result requiring its own conditions.

