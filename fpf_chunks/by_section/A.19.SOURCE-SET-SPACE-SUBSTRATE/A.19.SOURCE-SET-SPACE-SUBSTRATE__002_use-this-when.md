---
chunk_kind: "child"
pattern_id: "A.19.SOURCE-SET-SPACE-SUBSTRATE"
pattern_title: "Source-Set and Search/Outcome-Space Substrate"
section_id: "A.19.SOURCE-SET-SPACE-SUBSTRATE:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SOURCE-SET-SPACE-SUBSTRATE/A.19.SOURCE-SET-SPACE-SUBSTRATE__002_use-this-when.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "A.19.SOURCE-SET-SPACE-SUBSTRATE — Source-Set and Search/Outcome-Space Substrate"
  - "A.19.SOURCE-SET-SPACE-SUBSTRATE:0 — Use this when"
line_start: 25840
line_end: 25858
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

### A.19.SOURCE-SET-SPACE-SUBSTRATE:0 - Use this when

Use this pattern when one working line depends on all of the following at once:

- one declared source set still matters and must stay recoverable by name;
- one search-side space reference and one outcome-side space reference must both be explicit;
- the line must say whether those refs resolve to one declared `CharacteristicSpace` or to two distinct declared `CharacteristicSpace` declarations;
- the source-to-outcome relation is load-bearing enough that the reader must know what is being related, in which direction, and through which declared carrier, declared map ref, or qualifier ref;
- and distortion, uncertainty, or error cannot be left as vague atmosphere.

This is the right pattern for QD, OEE, archive/front, or adjacent synthesis lines when the problem is no longer only "what space exists?" and not yet "what shortlist or shipped result do we publish?".

Not this pattern when:

- you only need to declare or compare `CharacteristicSpace` itself, with no source-set or source-to-outcome requirement; use `A.19`;
- you are publishing selector or shipping metadata such as `SelectorOutcomeKind`, `SetResultFamily`, `HandoffKind`, or public shortlist identity; use `G.5` or `G.10`;
- you are building one interpretive view over an already-declared substrate; use `A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW` or a local specialization such as `G.2`;
- you are deciding live pool policy, frontier retention, or next-move planning; use `C.19` or `C.24`.

