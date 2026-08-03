---
chunk_kind: "child"
pattern_id: "I.2"
pattern_title: "Expanded Entry Disambiguation Cases"
section_id: "I.2"
section_title: ".3 - Boundary unpacking and claim decomposition"
source_path: "FPF-Spec.md"
output_path: "by_section/I.2/I.2__004_3-boundary-unpacking-and-claim-decomposition.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "I.2 — Expanded Entry Disambiguation Cases"
  - "I.2 — .3 - Boundary unpacking and claim decomposition"
line_start: 103809
line_end: 103834
dependencies:
keywords:
---

### I.2.3 - Boundary unpacking and claim decomposition

- **Case signal:** "The API or contract-language description says X."
- **Initial uncertainty:** the reader may be seeing one boundary description,
  an admissibility gate, a duty, an evidence claim, an action invitation, or an
  interface/access note.
- **Plausible candidate patterns:** `A.6`, `A.6.B`, `A.6.C`.
- **Nearby patterns:** `A.6.RSIG` if first-contact recognition is still live;
  `A.6.P` for relation wording; `C.16.Q` for quality wording; `A.6.A` for
  action invitation wording; `E.17` for publication or view question.
- **Tempting wrong pattern:** treat an API/access phrase as a promise of
  downstream effect, or treat one boundary phrase as a complete Contract Bundle.
- **Disambiguating fact:** the sentence mixes admissibility, gate, duty, evidence, and action-invitation
  requirements, or the encountered description's defining `U.Episteme` is not yet
  clear.
- **Recognition repair or entry-load reclassification:** use `A.6.RSIG` if the
  first question is "what description is this?"; otherwise inspect `A.6.B`
  / `A.6.C` for atomic boundary claim structure.
- **Actual governing FPF pattern body or projection role:** `A.6.B` and `A.6.C` govern
  L/A/D/E-classified claim decomposition; `A.6.RSIG` only governs first-contact
  description recognition.
- **Admissible entry stop:** boundary claim pattern opened, or one Claim Register or
  L/A/D/E-classified atomic claim set is ready for the next governing FPF pattern.
- **What not to infer:** one contract-language or API cue does not by itself create one
  work action, quality claim, or evidence relation.

