---
chunk_kind: "child"
pattern_id: "A.6.4"
pattern_title: "U.EpistemicRetargeting — EntityOfConcern retargeting morphism"
section_id: "A.6.4:5.2"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.4/A.6.4__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "A.6.4 — U.EpistemicRetargeting — EntityOfConcern retargeting morphism"
  - "A.6.4:5.2 — Common Anti-Patterns and How to Avoid Them"
line_start: 15631
line_end: 15639
dependencies:
  - "A.6.2"
  - "A.6.3"
  - "A.6.5"
  - "A.7"
  - "C.2"
  - "C.2.1"
  - "C.3"
  - "E.10.D2"
  - "E.18"
  - "F.9"
keywords:
---

### A.6.4:5.2 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Correct action |
|---|---|---|
| Retargeting as viewing | A changed EntityOfConcern is treated as the same object under another viewpoint. | Use A.6.3 only when `EntityOfConcernRef` is preserved; use A.6.4 when it changes. |
| Retargeting as publication rendering | A diagram, export, or face is treated as the retargeting relation. | Keep publication forms in E.17 and state the A.6.4 bridge/invariant relation separately. |
| Bridge as proof of all claims | A KindBridge is used to inherit gates, evidence, work authority, or temporal currentness. | State which commitments are preserved, lost, or non-admissible and state each other claim separately; use the pattern that defines or tests that claim. |
| Mathematical notation as retargeting object | Fourier, graph, path, or category notation is treated as the retargeting itself. | Use C.29 for the lens and A.6.4 for the episteme retargeting relation it expresses. |

