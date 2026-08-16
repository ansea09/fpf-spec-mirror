---
chunk_kind: "child"
pattern_id: "A.6.C"
pattern_title: "Contract Unpacking for Boundaries"
section_id: "A.6.C:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.C/A.6.C__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "A.6.C — Contract Unpacking for Boundaries"
  - "A.6.C:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 11523
line_end: 11534
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.3"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.6"
  - "A.6.B"
  - "A.6.C"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "E.10"
  - "E.17"
  - "F.12"
  - "F.18"
  - "U.Commitment"
  - "U.PromiseContent"
  - "U.SpeechAct"
  - "U.Work"
keywords:
  - "MUST NOT"
  - "MVPK no-new-semantics"
  - "OPTIONAL"
  - "SHOULD"
  - "a mechanism entry predicate enters A"
  - "and SHOULD NOT enter D only for an individual duty"
  - "and authority-looking synonyms trigger the A.6 A6-AW-* branch: a current norm or grant enters D"
  - "are statement operators"
  - "atomic L/A/D/E rows"
  - "commitment or grant"
  - "dated Work"
  - "description and publication"
  - "four-question contract lens"
  - "gate"
  - "not ontology or quadrant selectors. MUST"
  - "obtaining versus representation"
  - "or prohibition. MAY"
  - "promise content"
  - "recommendation-as-duty"
  - "rewrite it or mark it informative"
  - "separate result and evidence"
  - "speech-act Work"
---

### A.6.C:8 — Common Anti-Patterns and How to Avoid Them

| Anti-pattern                                        | Why it fails                                                   | Repair                                                                                      |
| --------------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **Interface-as-promiser** (“the API promises…”) | Epistemes and publication carriers are descriptions; they do not commit | Name the actual duty bearer and exact separately obtaining `U.Commitment`; cite an assignment only as a rule ground; keep the API, signature, or interface description as a description episteme or publication carrier. |
| **Guarantee-without-substrate** | The word hides whether the claim is semantic, deontic, an entry condition, or observed or evaluated | Classify semantic law as L, a claim about an exact individual commitment or current grant as D, an entry predicate as A, and an observed or evaluated claim as E; use `A6-AW-*` for permission-looking wording. |
| **SLA smuggled into laws**                          | Mixes governance with semantics; breaks substitution reasoning | Put SLA targets as D claims referencing L-defined metrics and E evidence                    |
| **Gate written as obligation**                      | Confuses admissibility predicates with duties                  | Write predicate as A; write duty-to-gate as D→A reference                                   |
| **Work-result-evidence bundle** | “The delivered work and its log prove acceptance” makes one phrase carry occurrence, result, transfer, evidence, and verdict | Name the A.15.1 Work first; then use one `A.15.1:4.6` row for each current result, delivery/transfer, evidence, or acceptance claim. Omit absent rows. |
| **Face-level paraphrase drift** | A face silently changes a claim's object or quadrant | Cite the canonical claim ID, direct object, and selected `A6-AW-*` row rather than restating it |
| **Cross-scale contract collapse** | Commitments, grants, and conflict findings at different scales are treated as one D claim | Keep commitments and current grants as separate D claims; classify the permission conflict finding as E through `A6-AW-CONFLICT`; use mediation only under its subject pattern |

