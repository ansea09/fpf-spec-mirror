---
chunk_kind: "child"
pattern_id: "A.6.2"
pattern_title: "U.EffectFreeEpistemicMorphing — Effect‑free morphisms of epistemes"
section_id: "A.6.2:7.1"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.2/A.6.2__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "A.6.2 — U.EffectFreeEpistemicMorphing — Effect‑free morphisms of epistemes"
  - "A.6.2:7.1 — Common Anti-Patterns and How to Avoid Them"
line_start: 12953
line_end: 12961
dependencies:
  - "A.1"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.4"
  - "A.6.5"
  - "C.2.1"
  - "C.3"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.18"
  - "U.EpistemicRetargeting"
  - "U.EpistemicViewing"
  - "U.Mechanism"
  - "U.Signature"
keywords:
---

### A.6.2:7.1 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Correct action |
|---|---|---|
| EFEM as performed work | An episteme rewrite is treated as measurement, actuation, or work occurrence. | Use EFEM only for episteme-to-episteme morphisms; use A.15 when work in the world is current. |
| EFEM as publication rendering | A face, carrier, or rendering change is treated as the episteme morphism itself. | Use E.17 for publication forms and use EFEM only for the episteme relation being represented. |
| Retargeting as harmless view | EntityOfConcern changes without a declared bridge or retargeting witness. | State `EntityOfConcernChangeMode=retarget` and use the relevant KindBridge or retargeting pattern. |
| Representation lens as ontology | A category arrow, graph, or mapping notation is treated as a new root U-kind. | Keep the mathematical object as the lens over the EFEM relation and keep U-kind settlement in E.24/C.3. |

