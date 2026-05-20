---
chunk_kind: "child"
pattern_id: "A.19.SURF-SPACE"
pattern_title: "Cross-Surface and Cross-Space Substrate"
section_id: "A.19.SURF-SPACE:0.a"
section_title: "TERM/LEX token-status guard (local-first)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SURF-SPACE/A.19.SURF-SPACE__005_term-lex-token-status-guard-local-first.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "A.19.SURF-SPACE — Cross-Surface and Cross-Space Substrate"
  - "A.19.SURF-SPACE:0.a — TERM/LEX token-status guard (local-first)"
line_start: 22962
line_end: 22973
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

### A.19.SURF-SPACE:0.a - TERM/LEX token-status guard (local-first)

Keep this token-status split explicit:

- `CharacteristicSpace` is the reused `A.19` kind. This pattern does not mint a second space kind.
- `SearchSpaceRef` and `OutcomeSpaceRef` are role-named local fields whose slot content is typed by the existing `CharacteristicSpaceRef` / `SpaceRef` idiom. They are not new heads, not slot aliases inside the space, and not `U.Role` claims. In cross-surface support or typed-set-view passages, read them as role-specific refinements of that older `SpaceRef` idiom rather than collapsing the roles back into one umbrella `SpaceRef`.
- `SpaceRefRelationKind` is a local relation-kind field over those two refs. In this slice, `sameDeclaredSpaceAs` and `distinctDeclaredSpaceFrom` are controlled token values for that field, not free prose.
- `SourceToOutcomeRelation` and `DistortionPosture` are local declaration fields. Their field names do not by themselves create one new generic ontology; the declaration requirement is satisfied only when their payload is explicit enough to audit.
- `SourceSurfaceKind`, `SourceSurfaceComposition`, and `DerivedViewKind` are local fields in this `CrossSurfaceCrossSpaceSubstrate` declaration. Whether any value later becomes a broader stable head is outside this pattern.
- `BasePaletteRef`, `OutcomeMapRef`, `SpaceMetricRef`, `TransitionSupportRef`, `BridgeDistortionNote`, `DescriptorMapRef`, and `DistanceDefRef` are guarded neighboring refs or support qualifiers reused here. This pattern may cite them, but it does not redefine them.
- `carrier` inside `SourceToOutcomeRelation` names the declared support, declared line, or declared object through which the relation is being realized in this local record. It is not a claim that the thing is `U.Carrier`.

