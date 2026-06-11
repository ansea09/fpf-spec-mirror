---
chunk_kind: "child"
pattern_id: "A.19.SOURCE-SET-SPACE-SUBSTRATE"
pattern_title: "Source-Set and Search/Outcome-Space Substrate"
section_id: "A.19.SOURCE-SET-SPACE-SUBSTRATE:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SOURCE-SET-SPACE-SUBSTRATE/A.19.SOURCE-SET-SPACE-SUBSTRATE__009_forces.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "A.19.SOURCE-SET-SPACE-SUBSTRATE — Source-Set and Search/Outcome-Space Substrate"
  - "A.19.SOURCE-SET-SPACE-SUBSTRATE:3 — Forces"
line_start: 23813
line_end: 23823
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

### A.19.SOURCE-SET-SPACE-SUBSTRATE:3 - Forces

| Force | Tension |
| --- | --- |
| `A.19` typing vs adjacent substrate requirement | `A.19` already declares `CharacteristicSpace`, but source-set and publication-form semantics still need a separate substrate declaration. |
| Precision vs over-typing | The line needs explicit ref positions, an explicit ref-to-ref relation kind, and explicit relation posture, but it should not fabricate composition, derivation, metrics, or transition qualifier when the case does not need them. |
| Reuse vs semantic collapse | `DescriptorMapRef`, `DistanceDefRef`, `OutcomeMapRef`, or `BridgeDistortionNote` are useful qualifiers, but they must not silently become the whole substrate. |
| User readability vs architectural honesty | Cold readers need a first-minute explanation, while specialist readers still need exact boundaries and docking rules. |
| Interpretive views vs substrate core | Atlas or interpretive-view lines can be valuable, but they should remain optional derived help rather than the default meaning of the substrate. |
| Uncertainty honesty vs fake closure | Many current lines use learned, adaptive, unstructured, or distribution-valued spaces or relations; the pattern must expose that posture without pretending the heaviest qualification posture is already settled. |

