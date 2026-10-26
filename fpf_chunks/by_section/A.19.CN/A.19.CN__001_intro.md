---
chunk_kind: "child"
pattern_id: "A.19.CN"
pattern_title: "CN-frame: Specify and Maintain Comparability and Normalization"
section_id: "A.19.CN:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CN/A.19.CN__001_intro.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "A.19.CN — CN-frame: Specify and Maintain Comparability and Normalization"
  - "A.19.CN:intro — Intro"
line_start: 36125
line_end: 36138
dependencies:
  - "A.19"
  - "A.6.1"
  - "C.16"
  - "F.9"
  - "G.0"
keywords:
  - "CL/loss notes"
  - "CN-Spec"
  - "CN-frame"
  - "RSG admission hooks"
  - "SCR/RSCR harness"
  - "WLNK discipline"
  - "bridges"
  - "chart"
  - "comparability modes"
  - "conformance checklist"
  - "indicator policy refs"
  - "normalization refs"
  - "registry"
  - "Γ-fold governance"
---

## A.19.CN - CN-frame: Specify and Maintain Comparability and Normalization

> **Status:** Stable

> **Scope.** Use a CN-frame to state which values may be compared for one bearer and intended use. Declare the characteristic space, chart, normalization and comparison basis in CN-Spec; maintain its editions and apply the conditions for each proposed reuse.
>
> **Use this when** readings need a recoverable comparison basis or a changed basis may affect their reuse. Keep the bearer, Characteristic and Scale meanings, observation or evaluation basis and intended comparison together. An already sufficient account can serve as CN-Spec; its notation is unrestricted. Apply the corresponding `A.19` mechanism pattern when normalization, indicatorization, scoring, aggregation, comparison or selection is actually needed. C.16 governs measurement backing and G.0 governs the applicable admission conditions.
>
> **Reader guide (fast navigation).**
> - “What does `NormalizationMethodId/…InstanceId/≡_UNM/NormalizationFix` mean?” → **A.19.UNM**.
> - “What is an Indicator / `IndicatorChoicePolicy` and why NCV ≠ Indicator?” → **A.19.UINDM**.
> - “Why can we trust a normalization / where does calibration or evidence live?” → **C.16 (MM‑CHR)**.
> - “What is admissible to compare or aggregate, and what is `MinimalEvidence`?” -> **G.0 (CG-Spec)**.

