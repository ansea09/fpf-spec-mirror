---
chunk_kind: "child"
pattern_id: "I.2"
pattern_title: "Expanded Entry Disambiguation Cases"
section_id: "I.2"
section_title: ".3 - Boundary unpacking and claim decomposition"
source_path: "FPF-Spec.md"
output_path: "by_section/I.2/I.2__004_3-boundary-unpacking-and-claim-decomposition.md"
commit_sha: "f4bad21274b54b57071afb2210a8bdb9f61a1c95"
heading_path:
  - "I.2 — Expanded Entry Disambiguation Cases"
  - "I.2 — .3 - Boundary unpacking and claim decomposition"
line_start: 108250
line_end: 108275
dependencies:
  - "E.10"
  - "E.11"
  - "F.17"
keywords:
  - "compact index"
  - "disambiguation"
  - "expanded comparison"
  - "first entry"
---

### I.2.3 - Boundary unpacking and claim decomposition

- **Case signal:** "The API or contract-language description says X."
- **Initial uncertainty:** the reader may be seeing one boundary description,
  an admissibility gate, a duty, an evidence claim, an action invitation, or an
  interface/access note.
- **Plausible candidate patterns:** `A.6`, `A.6.B`, `A.6.C`.
- **Nearby patterns:** `A.6.RSIG` if first-contact recognition is still live;
  `A.6.P` when relation wording hides participants or predicate; `C.16.Q` for overloaded quality wording; `A.6.A` for
  action invitation wording; `E.17` for reader-facing publication of an already accepted engineering account, `E.17.0` for view recognition, and `E.24.PUB` when publication occurrence, form, or carrier matters.
- **Tempting wrong pattern:** treat an API/access phrase as a promise of
  downstream effect, or treat one boundary phrase as a complete Contract Bundle.
- **Disambiguating fact:** the sentence mixes admissibility, gate, duty, evidence, and action-invitation
  claims, or the encountered description's defining `U.Episteme` is not yet
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

