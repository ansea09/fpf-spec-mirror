---
chunk_kind: "child"
pattern_id: "A.19.SURF-SPACE"
pattern_title: "Cross-Surface and Cross-Space Substrate"
section_id: "A.19.SURF-SPACE:0.2"
section_title: "What this buys"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SURF-SPACE/A.19.SURF-SPACE__004_what-this-buys.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "A.19.SURF-SPACE — Cross-Surface and Cross-Space Substrate"
  - "A.19.SURF-SPACE:0.2 — What this buys"
line_start: 22950
line_end: 22961
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

### A.19.SURF-SPACE:0.2 - What this buys

This pattern buys one conservative but expressive substrate declaration:

- the active source surface stays visible;
- the search-side and outcome-side references over `A.19` spaces stay distinct;
- the relation between those refs becomes inspectable instead of being hidden in one overloaded noun or verb;
- heavier support pins remain available without being forced into every case;
- and support-view or publication neighbors can reuse the substrate without changing what it means.

The practical payoff is simple: readers can tell what the line is acting on, what relation between the two space refs it assumes, what kind of qualification they must keep in view, and which neighboring pattern governs the next move if that requirement grows.

