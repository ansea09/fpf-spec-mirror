---
chunk_kind: "child"
pattern_id: "C.16.P"
pattern_title: "Characteristic and Scale Precision Restoration"
section_id: "C.16.P:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.P/C.16.P__001_intro.md"
commit_sha: "646b0b9b164f7c13258633a33b92d2d0a569da28"
heading_path:
  - "C.16.P — Characteristic and Scale Precision Restoration"
  - "C.16.P:intro — Intro"
line_start: 42154
line_end: 42172
dependencies:
  - "A.10"
  - "A.15"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.ECS"
  - "A.20"
  - "A.21"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.Q"
  - "C.25"
  - "C.28"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.21"
  - "F.18"
  - "G.0"
  - "G.5"
  - "G.9"
keywords:
---

## C.16.P - Characteristic and Scale Precision Restoration

> **Type:** Characterization precision-restoration pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain-name.** Characteristic-scale wording repair.

**Intent.**
Recover characteristic, scale, coordinate, score, metric, indicator, threshold, comparison, and scalar-quality wording whose construction is hidden before a reader applies `C.16`, `A.17`, `A.18`, `A.19`, `C.25`, `C.29`, `E.21`, or another governing pattern.

This pattern is not a metrics-only pattern, not a measurement-method replacement, not a Q-bundle pattern, and not a gate or decision pattern. It repairs overloaded characterization wording so the exact `Characteristic`, `Scale`, `Coordinate`, `Value`, `Score`, `Unit`, `ScoringMethod`, indicator role, comparison reference or comparator set, proxy role, admissible use, and governing pattern become recoverable.

**Builds on.** `E.10`, `E.10.ARCH`, `A.17`, `A.18`, `C.16`, `A.19`, `C.25`, `C.29`, `E.21`, `F.18`, and `A.6.P`.

**Coordinates with.** `C.16.Q`, `A.19.ECS`, CHR mechanism patterns, `G.0`, `G.5`, `G.9`, `C.11`, `A.10`, `B.3`, `A.20`, `A.21`, `C.28`, `A.15`, evidence, assurance, gate, decision, causal-use, release, work, benchmark, and publication patterns governing those claims.

**E.10.ARCH governing relation.** When `E.10` encounters `metric`, `score`, `axis`, `dimension`, `feature`, `property`, `indicator`, `strong`, `weak`, `robust`, `level`, `coordinate`, `threshold`, `benchmark`, or scalar-quality wording whose characteristic and scale construction is hidden, `E.10.ARCH` selects `C.16.P` only until bearer, characteristic, scale, value or score construction, comparison reference or comparator set, threshold rule or reference, proxy relation, admissible use, and governing pattern are recovered. After that recovery, the governing pattern governs its own invariant.

