---
chunk_kind: "child"
pattern_id: "A.19.SUPPORT-VIEW"
pattern_title: "Cross-Surface Support View"
section_id: "A.19.SUPPORT-VIEW:0.a"
section_title: "TERM/LEX token-status guard (local-first)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SUPPORT-VIEW/A.19.SUPPORT-VIEW__005_term-lex-token-status-guard-local-first.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "A.19.SUPPORT-VIEW — Cross-Surface Support View"
  - "A.19.SUPPORT-VIEW:0.a — TERM/LEX token-status guard (local-first)"
line_start: 23507
line_end: 23518
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

### A.19.SUPPORT-VIEW:0.a - TERM/LEX token-status guard (local-first)

Keep this token-status split explicit:

- `CrossSurfaceSupportView` is the ordinary/common support-view head introduced here for domain-specific reuse over one already-declared substrate-bearing basis: either the substrate line itself or one declared source surface or declared set surface that keeps the substrate recoverable.
- `CrossSurfaceAtlasView` is the fuller specialization of that same family. It is not the common head and it is not automatically required.
- `TypedSetViews` is one local plural field over already-declared set-view heads or ids. It is not a new generic set-surface ontology.
- `TraditionAtlasView` is one local `G.2` specialization of `CrossSurfaceAtlasView`, not the family head for all support-view use.
- `OutcomeMapRef`, `SpaceMetricRef`, `TransitionSupportRef`, and `BridgeDistortionNote` are guarded neighboring refs or support qualifiers reused here. This pattern may foreground them, but it does not mint them.
- `support question` is one local declaration field naming the interpretive load the current reading helps with. It is not a replacement for `U.Viewpoint`.
- `DerivedViewKind` and `BasePaletteRef` stay local recoverability aids here; they do not silently turn the derived reading into the base ontology.

