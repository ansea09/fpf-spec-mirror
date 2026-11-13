---
chunk_kind: "child"
pattern_id: "A.6.C"
pattern_title: "Contract Unpacking for Boundaries"
section_id: "A.6.C:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.C/A.6.C__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "A.6.C — Contract Unpacking for Boundaries"
  - "A.6.C:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 16342
line_end: 16354
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
  - "A.6.B separately classifies the claim"
  - "MVPK no-new-semantics"
  - "OPTIONAL or authority-looking wording is ambiguous"
  - "atomic L/A/D/E rows"
  - "commitment or grant"
  - "dated Work"
  - "description and publication"
  - "four-question contract lens"
  - "gate"
  - "marking it informative does not settle the claim"
  - "obtaining versus representation"
  - "promise content"
  - "recommendation-as-duty or prohibition enters D. When MAY"
  - "retain it as bounded source wording with that uncertainty"
  - "separate result and evidence"
  - "speech-act Work"
  - "the visible keyword alone does not establish its object or whether an individual relation obtains"
  - "use the A.6 A6-AW-* branch. If its object or meaning remains unresolved"
---

### A.6.C:8 — Common Anti-Patterns and How to Avoid Them

| Anti-pattern                                        | Why it fails                                                   | Repair                                                                                      |
| --------------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **Literal commitment assigned to a description** | An interface label does not select a description or an actual bearer; a carrier bears a publication form and is not thereby a description episteme. | Recover the claim and referent. Keep a semantic guarantee or clear policy metonymy. For a literal commitment, name the capable bearer, current policy and separately obtaining `U.Commitment`; keep any assignment as rule ground. Distinguish description, represented interface/access object, form and carrier only when the claim needs them. |
| **Guarantee-without-substrate** | The word hides whether the claim is semantic, deontic, an entry condition, or an operational claim such as an actual gate result or an observed or evaluated result | Classify semantic law as L, a generic prescription or claim about an individual commitment or current grant as D, an admission predicate as A, and an actual occurrence, condition or result as E; examples include an A.21 `GateDecisionResult` and other observed or evaluated results. Use `A6-AW-*` for permission-looking wording. |
| **SLA smuggled into laws** | Mixes governance with semantics; breaks substitution reasoning | State the target as a generic D prescription or an individual commitment, reference its L-defined metric and A conditions, and cite the E evaluated result plus A.10 support when current |
| **Gate written as obligation** | Confuses admissibility predicates with deontic claims | Write the predicate as A; write a generic prescription or separately instituted individual duty as a D→A reference. |
| **Work-result-evidence bundle** | “The delivered work and its log prove acceptance” makes one phrase carry occurrence, result, transfer, evidence, and verdict | Name the A.15.1 Work first; use the applicable `A.15.1:4.6` route for each current result, delivery/transfer, or acceptance claim. Use A.2.4 for first evidence-use classification or the direct rule for a further support claim. Use A.10 when provenance, currentness or bounded reliance must remain replayable, retaining the grounds required by that use. Omit absent claims. |
| **Face-level paraphrase drift** | A face silently changes a claim's object or quadrant | Use meaning-preserving face prose and cite the canonical claim ID or location, direct object, and selected `A6-AW-*` row when applicable. Add a new boundary claim to its canonical source before publishing it on a face. Use verbatim text when exactness is critical or disputed. |
| **Cross-scale contract collapse** | Commitments, grants, and conflict findings at different scales are treated as one D claim | Keep commitments and current grants as separate D claims; classify the permission conflict finding as E through `A6-AW-CONFLICT`; use mediation only under its subject pattern |
| **Mandatory four-question record** | Every clear use of contract wording creates rows for all four questions | Apply A.6.C only to a consequential ambiguity, answer only the live questions, and let a one-off repair end in the repaired atomic prose |

