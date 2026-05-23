---
chunk_kind: "child"
pattern_id: "A.19.SURF-SPACE"
pattern_title: "Cross-Surface and Cross-Space Substrate"
section_id: "A.19.SURF-SPACE:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SURF-SPACE/A.19.SURF-SPACE__015_consequences.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.19.SURF-SPACE — Cross-Surface and Cross-Space Substrate"
  - "A.19.SURF-SPACE:9 — Consequences"
line_start: 23456
line_end: 23469
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

### A.19.SURF-SPACE:9 - Consequences

**Benefits**

- Readers can see what the line is acting on, what spaces it distinguishes, what relation is declared between the two space refs, and what outcome load it claims.
- `A.19`, `C.18`, `G.5`, and `G.10` stay coordinated without collapsing into one layer.
- Heavier supports such as maps, metrics, transitions, and bridge-loss notes remain usable without being forced into every first slice.

**Trade-offs**

- The line must expose one explicit relation and one explicit posture instead of hiding them in umbrella prose.
- Some cases that used to look "simple" will expose real uncertainty or loss that now needs to be declared.
- Neighboring support-view or publication patterns may need to be read as companions rather than assumed from local shorthand.

