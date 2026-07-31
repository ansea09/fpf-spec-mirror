---
chunk_kind: "child"
pattern_id: "A.19.UNM"
pattern_title: "Unified Normalization Mechanism (UNM)"
section_id: "A.19.UNM:11"
section_title: "SoTA‑Echoing (post‑2015 practice alignment)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.UNM/A.19.UNM__013_sota-echoing-post-2015-practice-alignment.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "A.19.UNM — Unified Normalization Mechanism (UNM)"
  - "A.19.UNM:11 — SoTA‑Echoing (post‑2015 practice alignment)"
line_start: 31676
line_end: 31690
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

### A.19.UNM:11 - SoTA‑Echoing (post‑2015 practice alignment)

UNM does not prescribe algorithms, but it is designed to wire in SoTA normalization families via `NormalizationMethodDescriptionRef` + evidence pins (typically shipped as `G.2` SoTA packs and wired via `GPatternExtension` modules, not as mutations of UNM’s surface). Examples of post‑2015 method families that often appear as evidence-backed normalization candidates (domain-dependent):
- **SoTA ≠ popular.** Method families enter UNM through `G.2` claim structures + edition pins + evidence pins; “widely used” is not a validity claim by itself.
- **Calibration of probabilistic coordinates** (e.g., temperature scaling; multiclass calibration families such as Dirichlet calibration).
  *Typical citations:* Guo et al., 2017; Kull et al., 2019.
- **Shift-/validity-region-aware normalization** where “validity window/region” is explicit and shift detection enters as *evidence*, not as hidden branching.
  *Typical citations:* Lipton et al., 2018 (shift estimation); Ovadia et al., 2019 (uncertainty under shift) — as evidence motifs.
- **Order-preserving transforms** for ordinal regimes (normalization constrained to monotone transforms; scale lawfulness forbids arithmetic).
  *Typical citations:* modern monotonic modeling toolkits (post‑2017) used as *method families*, not as silent arithmetic.
- **Set-valued / uncertainty-aware normalization outputs** where uncertainty is preserved as a first-class outcome (tri‑state guards + set-valued uncertainty carriers, rather than coerced point values).
  *Typical citations:* conformal-style families (post‑2018+) used as evidence/uncertainty carriers.

SoTA is connected as **wiring** (packs/extensions) while UNM’s surface remains stable.

