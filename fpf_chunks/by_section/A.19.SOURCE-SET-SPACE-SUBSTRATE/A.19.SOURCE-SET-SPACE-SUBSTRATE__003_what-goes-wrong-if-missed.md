---
chunk_kind: "child"
pattern_id: "A.19.SOURCE-SET-SPACE-SUBSTRATE"
pattern_title: "Source-Set and Search/Outcome-Space Substrate"
section_id: "A.19.SOURCE-SET-SPACE-SUBSTRATE:0.1"
section_title: "What goes wrong if missed"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SOURCE-SET-SPACE-SUBSTRATE/A.19.SOURCE-SET-SPACE-SUBSTRATE__003_what-goes-wrong-if-missed.md"
commit_sha: "66e732dfef7a4a93ff23eec43b3f759a6664652d"
heading_path:
  - "A.19.SOURCE-SET-SPACE-SUBSTRATE — Source-Set and Search/Outcome-Space Substrate"
  - "A.19.SOURCE-SET-SPACE-SUBSTRATE:0.1 — What goes wrong if missed"
line_start: 28962
line_end: 28973
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

### A.19.SOURCE-SET-SPACE-SUBSTRATE:0.1 - What goes wrong if missed

If this pattern is missed, authors usually collapse several different things into one vague "space" or one vague "projection":

- the declared source set disappears behind bare words such as `front`, `archive`, `palette`, or `portfolio`;
- `SearchSpaceRef` and `OutcomeSpaceRef` never become explicit, or `SpaceRefRelationKind` never becomes explicit, so one line silently hides whether search and outcome use one declared space twice or two different declared spaces;
- `DescriptorMapRef` or `DistanceDefRef` gets mistaken for the space itself rather than one representation or metric qualifier;
- publication metadata in `G.5` or `G.10` starts standing in for substrate semantics;
- and distortion, uncertainty, or error is either hidden or treated as if every non-trivial case were only one bridge-loss story.

The result looks tidy, but the reader cannot tell what is being searched, what is being evaluated, what is only being published, and where uncertainty actually enters.

