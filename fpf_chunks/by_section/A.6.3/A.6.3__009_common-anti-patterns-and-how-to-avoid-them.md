---
chunk_kind: "child"
pattern_id: "A.6.3"
pattern_title: "U.EpistemicViewing — EntityOfConcern-preserving morphism"
section_id: "A.6.3:6.2"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3/A.6.3__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "89fcd508edbf9a49dc956955a42884fbca43f88c"
heading_path:
  - "A.6.3 — U.EpistemicViewing — EntityOfConcern-preserving morphism"
  - "A.6.3:6.2 — Common Anti-Patterns and How to Avoid Them"
line_start: 12163
line_end: 12171
dependencies:
  - "A.6.0"
  - "A.6.2"
  - "A.6.5"
  - "A.7"
  - "B.5.3"
  - "C.2"
  - "C.2.1"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
keywords:
---

### A.6.3:6.2 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Correct action |
|---|---|---|
| View as retargeting | The output episteme is about a different system, function, scale, or concern object. | Use A.6.4 or a KindBridge retargeting relation when `EntityOfConcernRef` changes. |
| View as publication face | A document, GUI, export, or dashboard is treated as the viewing morphism. | Use E.17 for publication forms and A.6.3 for the episteme relation behind the face. |
| View as mechanism or work | Query execution, measurement, or LLM generation is treated as effect-free viewing. | Use A.6.1/A.15 for the performed operation and A.6.3 only for the resulting episteme relation when it is pure and conservative. |
| View as new commitment | The view adds claims about the same EntityOfConcern without entailment or witness. | State the conservativity witness or move the strengthening claim to its governing pattern. |

