---
chunk_kind: "child"
pattern_id: "E.24.UK"
pattern_title: "U-kind Governance and Ontic Settlement Coupling"
section_id: "E.24.UK:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.UK/E.24.UK__002_use-this-when.md"
commit_sha: "9b6d71cff42a9ac45e46a2be2d9450f766868bc4"
heading_path:
  - "E.24.UK — U-kind Governance and Ontic Settlement Coupling"
  - "E.24.UK:0 — Use This When"
line_start: 74354
line_end: 74383
dependencies:
  - "A.11"
  - "A.6.5"
  - "A.8"
  - "C.3"
  - "C.3.1"
  - "E.10"
  - "E.10.ARCH"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "F.18"
  - "F.5"
  - "F.8"
keywords:
---

### E.24.UK:0 - Use This When

Use this pattern when an FPF text, heading, title, filename, ToC row, table, or source passage uses a `U.*`, type, kind, or subkind spelling and the author must decide whether it names a durable U-kind, a dependent durable value under an existing ontic settlement, a C.3 `U.Kind`, a Concept-Set or naming object, a slot position, a relation structure, a record, a publication form, a lens, a local frame, or wording that must stay outside current FPF vocabulary.

Typical moments:

- a proposed `U.*` name appears in a pattern title, host filename, monolith heading, or ToC row;
- a current pattern uses type, kind, or subkind wording and the governed value is unclear;
- a structural name looks useful for search, but may advertise a false root kind;
- a slot name, relation position, record field, diagram node, table column, graph expression, or publication form has acquired a `U.*` spelling;
- a single E.24 ontic settlement appears to govern one root value plus several dependent durable values.

**Primary EntityOfConcern.** The EntityOfConcern is the U-kind admission relation for one candidate `U.*`, type, kind, or subkind name. The pattern governs whether the candidate is retained as a durable U-kind, retained as a dependent durable value under a root settlement, governed by C.3 typed-reasoning law, or treated as a non-U object governed elsewhere.

**Primary working reader.** The first reader is an FPF pattern author or reviewer deciding whether a public FPF name should remain `U.*`. The downstream reader is the practitioner who uses public pattern titles, headings, ToC rows, and names as orientation cues and needs those cues to point to the real governed object.

**First useful move.** Recover the current governed object and the current use before judging the spelling. Then ask which existing FPF law governs the value: E.24 ontic settlement, C.3 typed reasoning, A.8 universal-core admission, A.11 parsimony, F.8 mint-or-reuse, F.5 naming, a direct subject pattern, or E.10 precision restoration.

**What goes wrong if missed.** FPF grows a shadow ontology by punctuation. A slot label becomes a kind, a publication form becomes an ontic, type and kind wording becomes active beside ontic law, and a useful title survives because it is searchable rather than because it names the governed object.

**What this buys.** Public `U.*` names become trustworthy. Root U-kinds, dependent durable values, C.3 `U.Kind` values, Concept-Set rows, slot names, relation structures, records, publication forms, lenses, local frames, and source wording outside current FPF use are separated before naming.

**Not this pattern when.**

- If the question is whether FPF needs a durable ontic at all, use `E.24`.
- If the question is only detecting an ontic candidate before the durable decision, use `E.24.CD`.
- If the question is the difference among an ontic, its description episteme, publication, and publication form, use `E.24.PUB`.
- If the question is one phrase-level precision issue with no durable name pressure, use `E.10`, `E.10.ARCH`, or the direct precision-restoration pattern.
- If the current value is already recovered and only its public label must be chosen, use `F.8`, `F.5`, `F.18`, or `F.17` according to the naming use.

