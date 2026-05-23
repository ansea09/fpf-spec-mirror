---
chunk_kind: "child"
pattern_id: "A.19.SURF-SPACE"
pattern_title: "Cross-Surface and Cross-Space Substrate"
section_id: "A.19.SURF-SPACE:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SURF-SPACE/A.19.SURF-SPACE__012_bias-annotation.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.19.SURF-SPACE — Cross-Surface and Cross-Space Substrate"
  - "A.19.SURF-SPACE:6 — Bias-Annotation"
line_start: 23416
line_end: 23423
dependencies:
  - "A.0"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.SUPPORT-VIEW"
  - "A.6.P"
  - "C.18"
  - "C.19"
  - "G.10"
  - "G.5"
keywords:
  - "DistortionPosture"
  - "SourceSurfaceId"
  - "SourceToOutcomeRelation"
  - "SpaceRefRelationKind"
  - "cross-surface substrate"
  - "distinctDeclaredSpaceFrom"
  - "outcome-side space ref"
  - "sameDeclaredSpaceAs"
  - "search-side space ref"
  - "source surface"
---

### A.19.SURF-SPACE:6 - Bias-Annotation


- **Gov bias.** The pattern prefers explicit declaration over convenient shorthand.
- **Arch bias.** The pattern keeps substrate, support view, and publication consumers separated even when one merged story would read more smoothly.
- **Prag bias.** The pattern prefers a short explicit substrate declaration that can be reused across search, synthesis, and publication-adjacent lines.
- **SoTA bias.** The pattern assumes current QD and OEE work often uses learned, adaptive, unstructured, or uncertainty-bearing spaces and therefore resists premature geometric closure.

