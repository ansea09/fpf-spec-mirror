---
chunk_kind: "child"
pattern_id: "A.19.SURF-SPACE"
pattern_title: "Cross-Surface and Cross-Space Substrate"
section_id: "A.19.SURF-SPACE:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SURF-SPACE/A.19.SURF-SPACE__007_problem-frame.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "A.19.SURF-SPACE — Cross-Surface and Cross-Space Substrate"
  - "A.19.SURF-SPACE:1 — Problem frame"
line_start: 22997
line_end: 23010
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

### A.19.SURF-SPACE:1 - Problem frame


In many search, synthesis, and cross-surface lines, the live substrate-bearing line is not just one `CharacteristicSpace` and not just one published shortlist or archive either. The line actually depends on a stack such as:

- one declared source surface, for example one front, archive, palette, or another declared source-surface family;
- one search-side reference to an `A.19` `CharacteristicSpace`;
- one outcome-side reference to an `A.19` `CharacteristicSpace`;
- one explicit `SpaceRefRelationKind` over those two references, stating whether they resolve to the same declared space or to two different declared spaces;
- one relation from the source-side line into the outcome-side line;
- and one declared posture about whether that relation is transparent, approximate, learned, lossy, uncertain, or otherwise qualified.

Without an explicit substrate declaration for that stack, nearby declarations start carrying loads they are not meant to carry. `A.19` gets stretched from space typing into source-surface governance. `C.18` descriptor maps start masquerading as the whole search space. `G.5` and `G.10` publication fields start reading like ontology. Support views or atlas views drift into default meaning instead of staying optional derived help.

