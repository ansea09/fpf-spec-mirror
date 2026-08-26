---
chunk_kind: "child"
pattern_id: "E.24.UK"
pattern_title: "U-kind Admission and Ontic Settlement"
section_id: "E.24.UK:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.UK/E.24.UK__002_use-this-when.md"
commit_sha: "c7ac61bbaa8d3c10165b1a5a4a350956c87d77c9"
heading_path:
  - "E.24.UK — U-kind Admission and Ontic Settlement"
  - "E.24.UK:0 — Use This When"
line_start: 89291
line_end: 89321
dependencies:
  - "A.1.1"
  - "A.11"
  - "A.2.6"
  - "A.22"
  - "A.6.0"
  - "A.6.5"
  - "A.6.RCD"
  - "A.6.REL"
  - "A.8"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "C.3.1"
  - "C.3.2"
  - "E.10"
  - "E.17.0"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "F.17"
  - "F.18"
  - "F.8"
  - "U.Kind"
  - "U.SubkindOf"
keywords:
---

### E.24.UK:0 - Use This When

Use this pattern when a public FPF expression proposes a `U.*`, type, kind, or subkind and the author must choose among four outcomes: reuse an admitted durable kind, declare a bounded C.3.2 local kind, admit a genuinely needed durable kind, or recover a non-kind object under the rule that defines or tests it. A title, filename, ToC row, table, or source spelling opens the question but never answers it.

Typical moments:

- a direct relation family has stable occurrence identity and patterns for the next questions need one common kind for those occurrences;
- a proposed `U.*` name appears in a pattern title, host filename, monolith heading, or ToC row;
- a current pattern uses type, kind, or subkind wording and the governed object is unclear;
- a structural name looks useful for search, but may advertise a false root kind;
- a `RelationSignature` SlotKind, an assertion or description field, a `C.29` representation element, or an `E.24.PUB` reusable form has acquired a `U.*` spelling;
- a single E.24 ontic settlement appears to govern one root U-kind plus several dependent durable U-kinds.

**Primary EntityOfConcern.** Identify the exact object the admission decision is about before filling the shared E.24-family decision: an already recoverable C.3 `U.Kind`, the proposal episteme for an unadmitted distinction, or the source-construct entity being translated. Put the proposed criterion, candidate individuals, intended extent and non-member boundary, spelling, and dependent claims in the decision's ClaimGraph. If no decision subject is identifiable, keep the inquiry open. An extension, member list, rule bundle, title, or spelling cannot fill this position.

**Primary working reader.** The first reader is an FPF pattern author or reviewer deciding whether a public FPF name should remain `U.*`. The downstream reader is the practitioner who uses public pattern titles, headings, ToC rows, and names as orientation cues and needs those cues to point to the real governed object.

**First useful move.** First name the exact local kind, proposal episteme, or source-construct entity that the decision is about; if no such object is identifiable, retain the inquiry and stop. Then recover the proposed governed individuals, identity or membership rule, intended extent and non-member boundary, and the action-facing claim that needs the kind. Test whether existing U-kinds, direct relations, declaration SlotKinds, C.3 local kinds, or selected structures already preserve that distinction. Judge the public spelling only after the admission disposition is stable.

**What goes wrong if missed.** FPF grows a shadow ontology by punctuation. A slot label becomes a kind, a publication form becomes an ontic, type and kind wording becomes active beside ontic settlement, and a useful title survives because it is searchable rather than because it names the governed object.

**What this buys.** Public `U.*` names become trustworthy. A candidate distinction either passes one explicit root or dependent admission test, or stays with the actual governed object and uses its defining or testing rule, with the PatternID kept only as a locator, without creating an umbrella kind.

**Not this pattern when.**

- If the question is whether FPF needs a durable ontic at all, use `E.24`.
- If the question is only detecting an ontic candidate before the durable decision, use `E.24.CD`.
- If the question is the difference among an ontic, its description episteme, publication, and publication form, use `E.24.PUB`.
- If the question is one phrase-level precision issue with no durable name pressure, use `E.10`, `E.10.ARCH`, or the direct precision-restoration pattern.
- If the current governed object is already recovered and only its public label must be chosen, use `F.8`, `F.5`, `F.18`, or `F.17` according to the naming use.

