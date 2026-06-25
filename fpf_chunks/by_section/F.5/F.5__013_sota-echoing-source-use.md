---
chunk_kind: "child"
pattern_id: "F.5"
pattern_title: "Naming Discipline for U-kind Names and RoleDescription Labels"
section_id: "F.5:11"
section_title: "SoTA-Echoing - Source-Use"
source_path: "FPF-Spec.md"
output_path: "by_section/F.5/F.5__013_sota-echoing-source-use.md"
commit_sha: "6bbbb622859fbbcddc02b23ea76bee4dd71c6291"
heading_path:
  - "F.5 — Naming Discipline for U-kind Names and RoleDescription Labels"
  - "F.5:11 — SoTA-Echoing - Source-Use"
line_start: 80616
line_end: 80627
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "E.10"
  - "E.10.ARCH"
  - "E.24.UK"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "U-kind naming"
  - "lexical rules"
  - "morphology"
  - "naming conventions"
  - "role-description labels"
  - "twin registers"
---

### F.5:11 - SoTA-Echoing - Source-Use

| Practice line | What FPF adopts | Practical implication |
| --- | --- | --- |
| Bounded-context practice in domain modeling | Names are local to a model boundary unless a bridge or translation is declared. | RoleDescription labels stay local; cross-context sameness goes through `F.9`. |
| Terminology and controlled-vocabulary practice | Preferred labels, plain explanations, symbols, and aliases are different fields. | Tech label, Plain label, symbol, and alias are not interchangeable. |
| Ontology engineering practice | Class names and relation names should not encode accidental provenance, thresholds, or temporary use. | Context, edition, witness, window, and threshold values stay in their slots. |
| Human-centered technical writing | A teaching gloss helps only when it does not change the underlying concept. | Plain labels explain; they do not widen the Tech label. |
| Morphology-aware naming practice | Word form affects reader expectations about actor, action, state, result, and relation position. | Role, method, work, status, and slot names use different morphology when the kind differs. |

Source-use boundary: external labels are evidence for local meaning or common practice, not automatic FPF Tech labels. A source term becomes the selected label only after `E.24.UK`, the governing Concept-Set row, role-description episteme, or direct relation pattern admits it.

