---
chunk_kind: "child"
pattern_id: "A.19.SOURCE-SET-SPACE-SUBSTRATE"
pattern_title: "Source-Set and Search/Outcome-Space Substrate"
section_id: "A.19.SOURCE-SET-SPACE-SUBSTRATE:0.a"
section_title: "TERM/LEX token-status guard (local-first)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SOURCE-SET-SPACE-SUBSTRATE/A.19.SOURCE-SET-SPACE-SUBSTRATE__003_term-lex-token-status-guard-local-first.md"
commit_sha: "5e9f4d868afa1f9db90d4c7ff6840bd55f3b8d18"
heading_path:
  - "A.19.SOURCE-SET-SPACE-SUBSTRATE — Source-Set and Search/Outcome-Space Substrate"
  - "A.19.SOURCE-SET-SPACE-SUBSTRATE:0.a — TERM/LEX token-status guard (local-first)"
line_start: 37113
line_end: 37124
dependencies:
  - "A.0"
  - "A.15.7"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.6.P"
  - "C.18"
  - "C.19"
  - "C.24"
  - "G.10"
  - "G.5"
keywords:
  - "DistortionPosture"
  - "SourceSetRef"
  - "SourceToOutcomeRelation"
  - "SpaceRefRelationKind"
  - "distinctDeclaredSpaceFrom"
  - "outcome-side space ref"
  - "sameDeclaredSpaceAs"
  - "search-side space ref"
  - "source set"
  - "source-set/space substrate"
---

### A.19.SOURCE-SET-SPACE-SUBSTRATE:0.a - TERM/LEX token-status guard (local-first)

Keep this token-status split explicit:

- `CharacteristicSpace` is the reused `A.19` kind. This pattern does not mint a second space kind.
- `SearchSpaceRef` and `OutcomeSpaceRef` are role-named local fields whose slot content is typed by the existing `CharacteristicSpaceRef` / `SpaceRef` idiom. They are not new heads, not slot aliases inside the space, and not `U.Role` claims. These field names distinguish the search-side and outcome-side uses of the referenced A.19 space.
- `SpaceRefRelationKind` is a local relation-kind field over those two refs. In this pattern, `sameDeclaredSpaceAs` and `distinctDeclaredSpaceFrom` are controlled token values for that field, not free prose.
- `SourceToOutcomeRelation` and `DistortionPosture` are local declaration fields. Their field names do not by themselves create one new generic ontology; the declaration requirement is satisfied only when their payload is explicit enough to audit.
- `SourceSetFamily`, `SourceSetComposition`, and `DerivedViewKind` are local fields in this `SourceSetSpaceSubstrate` declaration. Their use as fields does not establish a new object kind.
- `BasePaletteRef`, `OutcomeMapRef`, `SpaceMetricRef`, `TransitionRelationRef`, `BridgeDistortionNote`, `DescriptorMapRef`, and `DistanceDefRef` are neighboring refs or interpretive qualifiers reused here. This pattern may cite them, but it does not redefine them.
- `carrier` inside `SourceToOutcomeRelation` identifies the relation definition, map, model or operation that supplies the connection. Its definition can be stated or cited where the reader can recover it. A containing paragraph expresses that definition; the physical or digital entity bearing that text is identified separately under E.24.PUB.

