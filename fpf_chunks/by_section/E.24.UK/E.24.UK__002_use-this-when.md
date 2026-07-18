---
chunk_kind: "child"
pattern_id: "E.24.UK"
pattern_title: "U-kind Admission and Ontic Settlement"
section_id: "E.24.UK:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.UK/E.24.UK__002_use-this-when.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "E.24.UK — U-kind Admission and Ontic Settlement"
  - "E.24.UK:0 — Use This When"
line_start: 83245
line_end: 83275
dependencies:
  - "A.11"
  - "A.3.2"
  - "A.6.0"
  - "A.6.3"
  - "A.6.5"
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
  - "F.18"
  - "U.MethodDescription"
  - "U.View"
  - "U.Viewpoint"
keywords:
---

### E.24.UK:0 - Use This When

Use this pattern when an FPF text, heading, title, filename, ToC row, table, or source passage presents a candidate `U.*`, type, kind, or subkind distinction and the author must decide whether FPF admits that classificatory distinction as a durable U-kind or instead reuses an already admitted durable U-kind, declares a C.3.2 local kind, or recovers a declaration SlotKind, selected `U.Structure`, episteme or publication form, representation element, or source wording governed elsewhere.

Typical moments:

- a direct relation family has stable occurrence identity and receiving patterns need one common kind for those occurrences;
- a proposed `U.*` name appears in a pattern title, host filename, monolith heading, or ToC row;
- a current pattern uses type, kind, or subkind wording and the governed object is unclear;
- a structural name looks useful for search, but may advertise a false root kind;
- a `RelationSignature` SlotKind, an assertion or description field, a `C.29` representation element, or an `E.24.PUB` reusable form has acquired a `U.*` spelling;
- a single E.24 ontic settlement appears to govern one root U-kind plus several dependent durable U-kinds.

**Primary EntityOfConcern.** The EntityOfConcern is the candidate classificatory distinction: the governed individuals it would classify, their identity or membership rule, the intended extent and non-member boundary, and the claims that would depend on that kind. The admission decision is a claim-bearing episteme recorded through `E.9`; it is not a project-side relation occurrence. A candidate spelling is only a naming input and does not identify or admit the kind.

**Primary working reader.** The first reader is an FPF pattern author or reviewer deciding whether a public FPF name should remain `U.*`. The downstream reader is the practitioner who uses public pattern titles, headings, ToC rows, and names as orientation cues and needs those cues to point to the real governed object.

**First useful move.** Recover the governed individuals, their identity or membership rule, the intended extent and non-member boundary, and the action-facing claim that needs the candidate kind. Then test whether existing U-kinds, direct relations, declaration SlotKinds, C.3 local kinds, or selected structures already preserve that distinction. Judge the public spelling only after the admission disposition is stable.

**What goes wrong if missed.** FPF grows a shadow ontology by punctuation. A slot label becomes a kind, a publication form becomes an ontic, type and kind wording becomes active beside ontic settlement, and a useful title survives because it is searchable rather than because it names the governed object.

**What this buys.** Public `U.*` names become trustworthy. A candidate distinction either passes one explicit root or dependent admission test, or returns to the actual governed object and its direct pattern without creating an umbrella kind.

**Not this pattern when.**

- If the question is whether FPF needs a durable ontic at all, use `E.24`.
- If the question is only detecting an ontic candidate before the durable decision, use `E.24.CD`.
- If the question is the difference among an ontic, its description episteme, publication, and publication form, use `E.24.PUB`.
- If the question is one phrase-level precision issue with no durable name pressure, use `E.10`, `E.10.ARCH`, or the direct precision-restoration pattern.
- If the current governed object is already recovered and only its public label must be chosen, use `F.8`, `F.5`, `F.18`, or `F.17` according to the naming use.

