---
chunk_kind: "child"
pattern_id: "A.6.3.CR"
pattern_title: "ConservativeRetextualization — same-described-entity textual re-expression"
section_id: "A.6.3.CR:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.CR/A.6.3.CR__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "A.6.3.CR — ConservativeRetextualization — same-described-entity textual re-expression"
  - "A.6.3.CR:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 10943
line_end: 10951
dependencies:
  - "A.15"
  - "A.6.2"
  - "A.6.3"
  - "A.6.3.CSC"
  - "A.6.4"
  - "A.7"
  - "B.5.2"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.ID.CR"
  - "F.18"
  - "F.9"
  - "U.EffectFreeEpistemicMorphing"
  - "U.EpistemicRetargeting"
  - "U.EpistemicViewing"
keywords:
  - "direct vs correspondence-mediated rewrite"
  - "filtering"
  - "report rewrite"
  - "retextualization"
  - "same-described-entity textual re-expression"
  - "source tether"
  - "summary"
  - "translation"
---

### A.6.3.CR:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it is wrong | How to avoid it |
|---|---|---|
| Treating every summary as automatically conservative | summary demand hides omission and claim shift | publish loss/provenance discipline explicitly |
| Hiding correspondence in plain paraphrase | required correspondence support disappears into prose | declare `CorrespondenceModelRef` when needed |
| Letting a rewrite become explanation | explanation work quietly becomes a textual “rewrite” | move to explanation governance once didactic/explanatory work dominates |
| Letting `describedEntityRef` shift by topic similarity | same topic is not the same described entity | exit to `A.6.4` if `DescribedEntityRef` changes |

