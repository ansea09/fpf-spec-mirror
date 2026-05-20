---
chunk_kind: "child"
pattern_id: "A.19.SUPPORT-VIEW"
pattern_title: "Cross-Surface Support View"
section_id: "A.19.SUPPORT-VIEW:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SUPPORT-VIEW/A.19.SUPPORT-VIEW__002_use-this-when.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "A.19.SUPPORT-VIEW — Cross-Surface Support View"
  - "A.19.SUPPORT-VIEW:0 — Use this when"
line_start: 23460
line_end: 23481
dependencies:
  - "A.0"
  - "A.19"
  - "A.19.SURF-SPACE"
  - "A.6.3"
  - "A.6.P"
  - "C.19"
  - "C.24"
  - "E.17"
  - "E.17.0"
  - "G.10"
  - "G.2"
  - "G.5"
keywords:
  - "CrossSurfaceAtlasView"
  - "CrossSurfaceSupportView"
  - "TraditionAtlasView"
  - "TypedSetViews"
  - "atlas support"
  - "support qualifiers"
  - "support view"
  - "support-only reading"
  - "thin support"
---

### A.19.SUPPORT-VIEW:0 - Use this when

Use this pattern when one already-declared substrate from `A.19.SURF-SPACE` is already in force, and the current passage either cites that substrate directly or works through one declared source-surface entry point or set-surface entry point that keeps the substrate recoverable, but the reader still needs one support view to see how the line should be read in practice.

Typical indicators are:

- the substrate is already declared, but one thinner interpretive view is still needed so the active source surface, search-side space, outcome-side space, or distortion posture stays understandable;
- one fuller atlas-form reading may help collect several typed set views, active set surfaces, cited spaces, mappings, or support qualifiers without changing the underlying substrate;
- one derived tradition or palette view must stay recoverable as a view over a base palette rather than silently becoming the palette's default meaning;
- or one line needs optional support pins such as `OutcomeMapRef`, `SpaceMetricRef`, `TransitionSupportRef`, or `BridgeDistortionNote`, but those pins must stay supporting qualifiers rather than the semantic center.

This is the right pattern when the working need is no longer "what substrate is declared?" and not yet "what shortlist, publication surface, or shipped result do we emit?".

Not this pattern when:

- you still need to declare the substrate itself, including source-surface and search/outcome-space roles; use `A.19.SURF-SPACE`;
- you only need `CharacteristicSpace`, its slots, or its typing hooks; use `A.19`;
- you are publishing selector outcomes, shortlist identity, or shipping metadata; use `G.5` or `G.10`;
- you are setting live pool policy, retained-set policy, or enactment/planning posture; use `C.19` or `C.24`;
- you are defining a new generic view law, viewpoint bundle, or publication-view family rather than one domain-specific support reading; use `A.6.3`, `E.17.0`, `E.17`, or `E.17.1`;
- the line would change the described entity rather than preserve it; use `A.6.4` or the appropriate retargeting pattern.

