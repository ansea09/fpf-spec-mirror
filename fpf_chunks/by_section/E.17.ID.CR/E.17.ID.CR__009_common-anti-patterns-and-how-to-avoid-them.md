---
chunk_kind: "child"
pattern_id: "E.17.ID.CR"
pattern_title: "ComparativeReviewUnit - bounded comparison over comparative review units"
section_id: "E.17.ID.CR:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.ID.CR/E.17.ID.CR__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "66e732dfef7a4a93ff23eec43b3f759a6664652d"
heading_path:
  - "E.17.ID.CR — ComparativeReviewUnit - bounded comparison over comparative review units"
  - "E.17.ID.CR:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 80163
line_end: 80177
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

**Positive boundary-use profile.** Read the anti-pattern table below only after the ordinary working card has recovered the bounded comparative review unit. The ordinary result is positive: compared source epistemes or source publications, shared review frame, bounded comparative lift, blocked downstream claim or effect, and boundary trigger. If one row below fires, keep the comparison unit only for bounded review use and name the neighboring governing pattern for the crossed claim; do not turn the table into a general negative catalogue of every action the unit cannot perform.

| Anti-pattern | Why it is wrong | How to avoid it |
| --- | --- | --- |
| **Comparison-unit instability** | The text sounds as if it governs a note in one section, a publication unit in another, a comparative move in a third, and a whole review process in a fourth. | Stabilise one bounded comparative review unit early and keep note, sheet, UI, and rendering labels explicit as ordinary forms of that object rather than stylistic substitutes. |
| **Bridge gloss inflation** | A helpful comparative sentence starts acting like a bridge licence the declared bridge card and stance do not allow. | Keep bridge-mediated comparative relation tied to required `bridgeCardRef`; use optional `bridgeStanceRef` only as a subordinate overlay under `F.9.1`. |
| **Soft prompt smuggling** | The review unit is really creating an abductive prompt or action-selection case, but hides it in gentle prose. | If prompt selection or action-selection claim governs the next action, publish `U.AbductivePrompt` with explicit `promptSpecies`, `openQuestion`, and cue or action-selection provenance instead of keeping it here. |
| **Viewing capture** | Same-entity restatement or representation-shift work is pulled into interpretation just because the result is more readable. | Name the base source relation or representation work first and use bounded comparison only when bounded comparative lift is primary. |
| **Explanation-face laundering** | Interpretation language is used to avoid explicit `E.17.EFP` class and bounded-use review. | If face class or bounded connective prose is primary, stay with `E.17.EFP`. |
| **Gentle-tone advisory overread** | A calm explanatory tone makes work or reliance, assurance, or gate guidance sound harmless. | Publish `boundedComparativeUse`, `overreadRisk`, `worldContactPolicy`, and `downstreamAuthorityLimit` explicitly. |
| **EntityOfConcern shift** | A changed target is mislabeled as interpretation because the prose still sounds comparative. | Apply `OntologicalReframing` or `A.6.4` once continuity witnesses or changed target govern the claim. |
| **Interface neutrality fiction** | A guided or contrastive aid pretends to be audience-neutral while steering blocked downstream use. | Make `targetUserModel`, `interactionMode`, and `contrastiveQuestion` explicit and keep the non-bounded use forbidden. |

