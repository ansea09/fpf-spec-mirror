---
chunk_kind: "child"
pattern_id: "E.17.ID.CR"
pattern_title: "ComparativeReading — bounded comparative reading over comparative review units"
section_id: "E.17.ID.CR:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.ID.CR/E.17.ID.CR__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "E.17.ID.CR — ComparativeReading — bounded comparative reading over comparative review units"
  - "E.17.ID.CR:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 58450
line_end: 58463
dependencies:
  - "A.15"
  - "A.15.4"
  - "A.16.0"
  - "A.20"
  - "A.21"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.CSC"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.9"
  - "A.6.P"
  - "B.5.2"
  - "B.5.2.0"
  - "C.11"
  - "C.2.2a"
  - "E.14"
  - "E.17.AUD.LHR"
  - "E.17.AUD.OOTD"
  - "E.17.EFP"
  - "F.9"
  - "F.9.1"
keywords:
---

### E.17.ID.CR:8 - Common Anti-Patterns and How to Avoid Them


| Anti-pattern | Why it is wrong | How to avoid it |
| --- | --- | --- |
| **Governed-object instability** | The text sounds as if it governs a note in one section, a publication unit in another, a reading move in a third, and a whole review process in a fourth. | Stabilise one governed object early and keep note, sheet, UI, and rendering labels explicit as ordinary forms of that object rather than stylistic substitutes. |
| **Bridge gloss inflation** | A helpful comparative sentence starts acting like a bridge licence the declared bridge card and stance do not allow. | Keep bridge-mediated comparative posture tied to required `bridgeCardRef`; use optional `bridgeStanceRef` only as a subordinate overlay under `F.9.1`. |
| **Soft prompt smuggling** | The review unit is really opening a question or action-selection case, but hides it in gentle prose. | If prompt selection or action-selection claim becomes live, publish `U.AbductivePrompt` with explicit `promptSpecies`, `openQuestion`, and cue or action-selection provenance instead of keeping it here. |
| **Viewing capture** | Same-entity restatement or representation-shift work is pulled into interpretation just because the result is more readable. | Name the base source relation or representation work first and use comparative reading only when bounded comparative lift is primary. |
| **Explanation-face laundering** | Interpretation language is used to avoid explicit `E.17.EFP` class and admissibility review. | If face class or bounded connective prose is primary, stay with `E.17.EFP`. |
| **Gentle-tone advisory overread** | A calm explanatory tone makes work or reliance, assurance, or gate guidance sound harmless. | Publish `allowedUse`, `misuseRisk`, `worldContactPolicy`, and `downstreamAuthorityLimit` explicitly. |
| **Described-entity shift** | A changed target is mislabeled as interpretation because the prose still sounds comparative. | Exit to `OntologicalReframing` or `A.6.4` once continuity witnesses or changed target become load-bearing. |
| **Interface neutrality fiction** | A guided or contrastive aid pretends to be audience-neutral while steering non-admissible downstream use. | Make `targetUserModel`, `interactionMode`, and `contrastiveQuestion` explicit and keep the non-admissible use forbidden. |

