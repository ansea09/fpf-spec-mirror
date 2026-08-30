---
chunk_kind: "child"
pattern_id: "A.6.4"
pattern_title: "EntityOfConcern retargeting"
section_id: "A.6.4:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.4/A.6.4__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "A.6.4 — EntityOfConcern retargeting"
  - "A.6.4:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 15876
line_end: 15884
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.6.0"
  - "A.6.1"
  - "A.6.2"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.5"
  - "A.7"
  - "B.3"
  - "C.2"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "E.10.D2"
  - "E.17"
  - "E.24.PUB"
  - "F.9"
keywords:
---

### A.6.4:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Correct action |
|---|---|---|
| Retargeting as viewing | A changed EntityOfConcern is treated as the same object under another viewpoint. | Use A.6.3 only when `EntityOfConcernRef` is preserved; use A.6.4 when it changes. |
| Retargeting as publication rendering | A diagram, export, or face is treated as the arrow or as support for its use. | Keep publication forms in E.17 and E.24.PUB; state r and the separate use claim q only when each is current. |
| Universal Bridge as admission | A `KindBridge`, F.9 Bridge, `CL`, mapping, or optic is required or used to inherit every downstream claim. | Use the A.6.4 minimum basis; add F.9 only for a separate local-sense relation and state every neighboring claim under its own rule. |
| Mathematical notation decides retargeting | A Fourier, graph, path, or category representation is treated as proof that the EntityOfConcern changed. | Use C.29 for the mathematical lens and repeat the C.2.1 identity test. Use A.6.3.RT when the entity is preserved; use A.6.4 only for independently different entities. |

