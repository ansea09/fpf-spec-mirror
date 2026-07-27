---
chunk_kind: "child"
pattern_id: "A.2.8"
pattern_title: "U.Commitment (Deontic Commitment Object)"
section_id: "A.2.8:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.8/A.2.8__012_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "66e732dfef7a4a93ff23eec43b3f759a6664652d"
heading_path:
  - "A.2.8 — U.Commitment (Deontic Commitment Object)"
  - "A.2.8:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 5898
line_end: 5907
dependencies:
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.3"
  - "A.2.6"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.6.B"
  - "A.6.C"
  - "A.7"
  - "E.8"
  - "U.PromiseContent"
  - "U.Work"
keywords:
  - ") but makes the structure explicit"
  - "BCP‑14 (RFC 2119/8174)"
  - "adjudication hooks"
  - "are cues for the modality field after the deontic relation is recovered"
  - "by themselves"
  - "commitment"
  - "deontics"
  - "evidenceRefs"
  - "modality normalization"
  - "obligation"
  - "prohibition"
  - "recommendation-as-duty"
  - "scope and validity window"
  - "they are not the governed object of this pattern"
---

### A.2.8:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern                                        | Why it fails                                               | Repair                                                                                |
| --------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Episteme-as-subject** (“the API SHALL…”)          | assigns agency to descriptions                             | use an accountable role or party as `subject`; keep the spec as `source.descriptionRef`  |
| **Missing scope/window**                            | commitments become unreviewable (“always/never” ambiguity) | declare `scope` + `validityWindow`; if global, say so explicitly via a policy/default |
| **Paraphrase drift**                                | drift across faces and docs                                | reference via `referents` using claim IDs; avoid restating the same constraint        |
| **Auditable rhetoric** (“guaranteed”) without hooks | not adjudicable                                            | add `adjudication.evidenceRefs` pointing to `E-*` claims and carrier expectations     |
| **Gate-as-duty**                                    | confuses admissibility with obligation                     | put predicate in `A-*`; make commitment reference it (`D→A`)                          |

