---
chunk_kind: "child"
pattern_id: "A.19.SURF-SPACE"
pattern_title: "Cross-Surface and Cross-Space Substrate"
section_id: "A.19.SURF-SPACE:0.b"
section_title: "First-minute operator cue and confusion map"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SURF-SPACE/A.19.SURF-SPACE__006_first-minute-operator-cue-and-confusion-map.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.19.SURF-SPACE — Cross-Surface and Cross-Space Substrate"
  - "A.19.SURF-SPACE:0.b — First-minute operator cue and confusion map"
line_start: 23028
line_end: 23050
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

### A.19.SURF-SPACE:0.b - First-minute operator cue and confusion map

If you are about to write one line that says what is being searched, what is being judged, and whether those two relations sit in one declared space or in two declared spaces, stop and fill this pattern before you write any more umbrella prose such as `space`, `projection`, `portfolio`, or `front`.

Do this in the first minute:

1. Name the active source surface.
2. Point `SearchSpaceRef` and `OutcomeSpaceRef` to declared `CharacteristicSpace`.
3. Choose `sameDeclaredSpaceAs` or `distinctDeclaredSpaceFrom`.
4. State the source-to-outcome relation in direction, mode, and carrier.
5. State the governing posture token.

If one of those five cells cannot yet be filled honestly, do not improvise around it. Either you are still in `A.19`, or you have really moved into support-view work, publication, or policy, or the current line is still missing one declared basis.

| If the live question sounds like... | Use now | Why |
| --- | --- | --- |
| "Which space are we searching in and which space are we judging in?" | `A.19.SURF-SPACE` | This pattern governs the dual-ref substrate stack. |
| "How should I help the reader inspect that already-declared line?" | `A.19.SUPPORT-VIEW` | That is one support reading over the substrate, not the substrate declaration itself. |
| "What do we publish, ship, keep live, or plan next?" | `G.5`, `G.10`, `C.19`, or `C.24` | Those are downstream output or policy questions. |
| "I only need one space declaration." | `A.19` | No source-to-outcome substrate stack is in play yet. |

Common confusion to kill early: descriptor maps, distance definitions, and outcome maps may discipline the line, but they do not answer the first-minute substrate question unless the five cells above are already filled.

