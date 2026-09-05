---
chunk_kind: "child"
pattern_id: "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
pattern_title: "Declared-Substrate Interpretive View"
section_id: "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:0.a"
section_title: "TERM/LEX token-status guard (local-first)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW/A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW__005_term-lex-token-status-guard-local-first.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW — Declared-Substrate Interpretive View"
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:0.a — TERM/LEX token-status guard (local-first)"
line_start: 31238
line_end: 31249
dependencies:
  - "A.0"
  - "A.19"
  - "A.19.SOURCE-SET-SPACE-SUBSTRATE"
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
  - "DeclaredSubstrateAtlasView"
  - "DeclaredSubstrateInterpretiveView"
  - "TraditionAtlasView"
  - "TypedSetViews"
  - "atlas-form interpretation"
  - "declared-substrate interpretive view"
  - "interpretive qualifiers"
  - "interpretive-only reading"
  - "thin interpretation"
---

### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:0.a - TERM/LEX token-status guard (local-first)

Keep this token-status split explicit:

- `DeclaredSubstrateInterpretiveView` is the ordinary/common interpretive-view head introduced here for domain-specific reuse over one already-declared substrate-bearing basis: either the substrate line itself or one declared source set or declared set result that keeps the substrate recoverable.
- `DeclaredSubstrateAtlasView` is the fuller specialization of that same family. It is not the common head and it is not automatically required.
- `TypedSetViews` is one local plural field over already-declared set-view heads or ids. It is not a new generic set-result ontology.
- `TraditionAtlasView` is one local `G.2` specialization of `DeclaredSubstrateAtlasView`, not the family head for all interpretive-view use.
- `OutcomeMapRef`, `SpaceMetricRef`, `TransitionRelationRef`, and `BridgeDistortionNote` are guarded neighboring refs or interpretive qualifiers reused here. This pattern may foreground them, but it does not mint them.
- `inspection question` is one local declaration field naming the interpretive load the current reading helps with. It is not a replacement for `U.Viewpoint`.
- `DerivedViewKind` and `BasePaletteRef` stay local recoverability aids here; they do not silently turn the derived reading into the base ontology.

