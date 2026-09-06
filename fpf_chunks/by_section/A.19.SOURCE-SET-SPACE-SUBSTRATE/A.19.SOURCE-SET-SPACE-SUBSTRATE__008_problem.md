---
chunk_kind: "child"
pattern_id: "A.19.SOURCE-SET-SPACE-SUBSTRATE"
pattern_title: "Source-Set and Search/Outcome-Space Substrate"
section_id: "A.19.SOURCE-SET-SPACE-SUBSTRATE:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SOURCE-SET-SPACE-SUBSTRATE/A.19.SOURCE-SET-SPACE-SUBSTRATE__008_problem.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "A.19.SOURCE-SET-SPACE-SUBSTRATE — Source-Set and Search/Outcome-Space Substrate"
  - "A.19.SOURCE-SET-SPACE-SUBSTRATE:2 — Problem"
line_start: 30754
line_end: 30766
dependencies:
  - "A.0"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.6.P"
  - "C.18"
  - "C.19"
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

### A.19.SOURCE-SET-SPACE-SUBSTRATE:2 - Problem

How should one declare a source-set and search/outcome-space line so that:

1. the declared source set remains explicit and recoverable;
2. `SearchSpaceRef` and `OutcomeSpaceRef` stay guarded refs to declared `A.19` `CharacteristicSpace`, not new free-floating space kinds;
3. the text states whether those refs point to one declared space or to two distinct declared spaces;
4. the source-to-outcome relation is explicit enough for the reader to know which source-to-outcome relation mode is being claimed: mapped, projected, translated, scored, or otherwise connected;
5. distortion, uncertainty, and error are stated honestly rather than hidden in prose;
6. `SourceSetComposition` and `DerivedViewKind` remain conditional fields rather than fabricated mandatory baggage;
7. qualifier refs such as `OutcomeMapRef`, `SpaceMetricRef`, `TransitionRelationRef`, and `BridgeDistortionNote` remain available but substrate-side only;
8. and neighboring declarations such as `A.19`, `C.18`, `G.5`, `G.10`, and `A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW` can dock to the substrate without redefining it?

