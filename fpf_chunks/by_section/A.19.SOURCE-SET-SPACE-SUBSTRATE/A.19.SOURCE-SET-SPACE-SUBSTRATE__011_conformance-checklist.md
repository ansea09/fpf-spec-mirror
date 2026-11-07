---
chunk_kind: "child"
pattern_id: "A.19.SOURCE-SET-SPACE-SUBSTRATE"
pattern_title: "Source-Set and Search/Outcome-Space Substrate"
section_id: "A.19.SOURCE-SET-SPACE-SUBSTRATE:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SOURCE-SET-SPACE-SUBSTRATE/A.19.SOURCE-SET-SPACE-SUBSTRATE__011_conformance-checklist.md"
commit_sha: "e307edbd91c04c1d85661bd309b9944fac251937"
heading_path:
  - "A.19.SOURCE-SET-SPACE-SUBSTRATE — Source-Set and Search/Outcome-Space Substrate"
  - "A.19.SOURCE-SET-SPACE-SUBSTRATE:7 — Conformance Checklist"
line_start: 35903
line_end: 35921
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

### A.19.SOURCE-SET-SPACE-SUBSTRATE:7 - Conformance Checklist

Apply these declaration checks to the claims and qualifiers actually used:

| ID | Check question | Fail when | Repair or governing pattern |
| --- | --- | --- | --- |
| `CC-A19SS-1` | Is the line really declaring one substrate-bearing relation rather than only `CharacteristicSpace`, publication metadata, or policy? | The line only names a space object, or only publishes, ships, or retains something, with no explicit source, ref, relation, or posture stack. | Move to `A.19`, `G.5`, `G.10`, `C.19`, or `C.24` as appropriate. |
| `CC-A19SS-2` | Is the source basis recoverable for the current case? | A contributing set, its family or its member contribution rule is ambiguous, or a primary source is invented for a composition that distinguishes none. | Recover each set identity and family and any actual composition under §4.7; use refs or accessible defining sources as needed. |
| `CC-A19SS-3` | Do `SearchSpaceRef` and `OutcomeSpaceRef` both resolve to declared `A.19` `CharacteristicSpace`, and is `SpaceRefRelationKind` explicit? | One or both refs are vague, or the line leaves the same-space versus cross-space question to inference. | Restore the two refs and declare `sameDeclaredSpaceAs` or `distinctDeclaredSpaceFrom` explicitly. |
| `CC-A19SS-4` | Is the source-to-outcome relation explicit in its participants, direction, mode and defining basis? | The relation remains hidden in an umbrella phrase with no recoverable map, model, operation or rule. | State the participants, direction, mode and defining basis directly or cite where they can be recovered. |
| `CC-A19SS-5` | Are the relevant qualifications explicit and supported for the claimed use? | Material limits are missing, or different qualified cases are blurred into one generic loss story. | State the qualifications and the basis needed by that use. If needed support is missing, retain the established content and withhold only the dependent conclusion; a primary token is required only by a selected interface. |
| `CC-A19SS-6` | Are conditional and qualifier fields used only when they really do work? | Composition, derivation, base-palette, declared map ref, metric, transition, or bridge qualifiers are fabricated everywhere or silently become core. | Remove unused qualifiers; keep only the fields the current case actually depends on. |
| `CC-A19SS-7` | If `DescriptorMapRef` or `DistanceDefRef` is active, does the text say they realize or qualify the relation rather than replace the space ref? | The representation or metric layer is treated as if it were the declared search-side or outcome-side space. | Re-state the docking rule and keep the two space refs visible. |
| `CC-A19SS-8` | Does the line stay out of publication and policy work? | The prose starts deciding shortlist identity, selector outcome, shipping closure, or live-pool/enactment policy. | Split the line and move those downstream decisions to their governing patterns. |
| `CC-A19SS-9` | Can the account establish the substrate claim needed by the current use without inventing facts? | A required source identity, space resolution, relation or material qualification remains unsupported. | Return the recovered components and the missing basis; withhold the complete claim and only uses that depend on that gap. |
| `CC-A19SS-10` | Could a cold reader take the next lawful declaration step from this line without surrounding memo help? | The line still speaks only in umbrella words such as `space`, `projection`, or `portfolio`, and the reader cannot tell what to fill next. | Use the declaration sequence in §4.5 and recover the needed content from §4.2 before reuse. |
| `CC-A19SS-11` | When the next question is interpretive-view, publication, or policy, is the next governing pattern explicit? | The text keeps talking as if substrate, interpretation, publication, and policy were one layer, so the reader cannot tell where to continue. | Split the line and cite `A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW`, `G.5`, `G.10`, `C.19`, or `C.24` as the next governing pattern. |
| `CC-A19SS-12` | Does the current use claim only the breadth its declared posture and qualifiers actually license? | The prose implies universal geometric closure or one universal heavy-qualification story, but the declared posture or qualifiers stay narrower, uncertain, learned/adaptive, or case-bound. | Narrow the claim explicitly or add the missing posture/interpretive qualifiers that make the broader claim honest. |

