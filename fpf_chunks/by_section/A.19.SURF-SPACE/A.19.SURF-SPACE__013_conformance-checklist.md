---
chunk_kind: "child"
pattern_id: "A.19.SURF-SPACE"
pattern_title: "Cross-Surface and Cross-Space Substrate"
section_id: "A.19.SURF-SPACE:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SURF-SPACE/A.19.SURF-SPACE__013_conformance-checklist.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.19.SURF-SPACE — Cross-Surface and Cross-Space Substrate"
  - "A.19.SURF-SPACE:7 — Conformance Checklist"
line_start: 23424
line_end: 23442
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

### A.19.SURF-SPACE:7 - Conformance Checklist

Treat a line as conforming only if every gate below passes.

| ID | Gate question | Fail when | Repair or governing pattern |
| --- | --- | --- | --- |
| `CC-A19SS-1` | Is the line really declaring one substrate-bearing relation rather than only `CharacteristicSpace`, publication metadata, or policy? | The line only names a space object, or only publishes, ships, or retains something, with no explicit source, ref, relation, or posture stack. | Move to `A.19`, `G.5`, `G.10`, `C.19`, or `C.24` as appropriate. |
| `CC-A19SS-2` | Is the active source surface recoverable enough for the current case? | Only a vague family word such as `front` or `archive` remains, and several same-family surfaces are live with no way to tell which one is meant. | Add the concrete declared surface id or cite the neighboring governing pattern that makes the surface unique. |
| `CC-A19SS-3` | Do `SearchSpaceRef` and `OutcomeSpaceRef` both resolve to declared `A.19` `CharacteristicSpace`, and is `SpaceRefRelationKind` explicit? | One or both refs are vague, or the line leaves the same-space versus cross-space question to inference. | Restore the two refs and declare `sameDeclaredSpaceAs` or `distinctDeclaredSpaceFrom` explicitly. |
| `CC-A19SS-4` | Is the source-to-outcome relation explicit in direction, mode, and carrier? | The line hides the relation in one umbrella phrase such as `projection`, `portfolio`, or `maps into`, with no explicit carrier. | Rewrite into the canonical substrate form and state direction, mode, and carrier. |
| `CC-A19SS-5` | Is the active qualification posture explicit and honest? | The line is qualified in effect, but the posture is unstated or all non-transparent cases are blurred into one generic loss story. | Declare the governing posture token and any needed note; if that cannot be done honestly, keep the line informative only. |
| `CC-A19SS-6` | Are conditional and support fields used only when they really do work? | Composition, derivation, base-palette, map, metric, transition, or bridge qualifiers are fabricated everywhere or silently become core. | Remove unused qualifiers; keep only the fields the current case actually depends on. |
| `CC-A19SS-7` | If `DescriptorMapRef` or `DistanceDefRef` is active, does the text say they realize or support the relation rather than replace the space ref? | The representation or metric layer is treated as if it were the declared search-side or outcome-side space. | Re-state the docking rule and keep the two space refs visible. |
| `CC-A19SS-8` | Does the line stay out of publication and policy work? | The prose starts deciding shortlist identity, selector outcome, shipping closure, or live-pool/enactment policy. | Split the line and move those downstream decisions to their governing patterns. |
| `CC-A19SS-9` | Can the line be rewritten into one canonical substrate form without invention? | The line still depends on hidden assumptions or unresolved candidates. | Keep it as a working gloss or repair the missing recovery before reuse. |
| `CC-A19SS-10` | Could a cold reader take the next lawful declaration step from this line without surrounding memo help? | The line still speaks only in umbrella words such as `space`, `projection`, or `portfolio`, and the reader cannot tell what to fill next. | Use the substrate worksheet from `4.12` or rewrite into one canonical substrate form before reuse. |
| `CC-A19SS-11` | When the next question is support-view, publication, or policy, is the next governing pattern explicit? | The text keeps talking as if substrate, support, publication, and policy were one layer, so the reader cannot tell where to continue. | Split the line and cite `A.19.SUPPORT-VIEW`, `G.5`, `G.10`, `C.19`, or `C.24` as the next governing pattern. |
| `CC-A19SS-12` | Does the current use claim only the breadth it actually supports? | The prose implies universal geometric closure or one universal heavy-support story, but the declared posture or supports stay narrower, uncertain, learned/adaptive, or case-bound. | Narrow the claim explicitly or add the missing posture/support qualifiers that make the broader claim honest. |

