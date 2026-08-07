---
chunk_kind: "child"
pattern_id: "A.6.9"
pattern_title: "Cross-Context Sameness Disambiguation - Repairing cross-context \"same\", \"equivalent\", and \"align\" via explicit Bridges (RPR-XCTX)"
section_id: "A.6.9:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.9/A.6.9__013_sota-echoing.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "A.6.9 — Cross-Context Sameness Disambiguation - Repairing cross-context \"same\", \"equivalent\", and \"align\" via explicit Bridges (RPR-XCTX)"
  - "A.6.9:11 — SoTA-Echoing"
line_start: 20636
line_end: 20648
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.6"
  - "A.2.1"
  - "A.2.6"
  - "A.22"
  - "A.6.3.RT"
  - "A.6.6"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.2.1"
  - "C.29"
  - "C.3.3"
  - "E.17"
  - "E.17.0"
  - "E.19"
  - "E.24.PUB"
  - "F.0.1"
  - "F.17"
  - "F.18"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "A.10/B.3 reliance"
  - "LocalSenseClaim> projections"
  - "actual receiving object"
  - "ambiguous sameness"
  - "different <ReferenceScheme"
  - "direct-owner dispatch"
  - "exact F.17 SchemeSenseCell endpoints"
  - "explicit stop"
  - "relation-only F.9 Bridge"
  - "separate C.2.1 bounded-use claim"
---

### A.6.9:11 - SoTA-Echoing

(informative; post-2015 alignment)

| SoTA practice | Primary source | What A.6.9 echoes | What A.6.9 adds | Stance |
| --- | --- | --- | --- | --- |
| Correspondences between viewpoints | ISO/IEC/IEEE 42010:2022 | Correspondence is not identity and retains intent and constraints. | Separates the direct semantic relation from each proposed use and actual publication or view object. | **Adopt + specialise** |
| Declarative validation shapes | W3C SHACL (2017) | Make implicit conditions testable. | Uses a profile for relation truth, a claim for bounded-use suitability, and a card only for packaging. | **Adapt** |
| Scored entity alignment with error analysis | BootEA (Sun et al., 2018) and later KG-alignment literature | Alignment evidence is graded and fallible. | Keeps scores and counterexamples as evidence rather than relation identity or a use licence. | **Adapt** |
| Textual entity matching | BERT-INT (Tang et al., 2020); Ditto (Li et al., 2021) | Matchers yield conditional, error-prone correspondences. | Requires exact endpoint readings, a falsifiable Bridge predicate, and a separate action-specific claim. | **Adopt conceptually** |
| Heterogeneous schema matching | SMAT (Zhang et al., 2021) and later neural or LLM matching work | “Match” covers several relation types. | Distinguishes relation kind, relation orientation, proposed-use direction, rule, and tolerance. | **Adapt** |
| Human-in-the-loop matching | Mudgal et al. (SIGMOD 2018) and follow-on work | Scores require abstention and curated error cases. | Uses the exact A.10 evidence or B.3 assurance predicates and preserves explicit negative or blocked outcomes. | **Adapt** |

