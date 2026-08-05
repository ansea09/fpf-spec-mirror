---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint-or-Reuse Decision"
section_id: "F.8:5"
section_title: "Invariants"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__007_invariants.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "F.8 — Mint-or-Reuse Decision"
  - "F.8:5 — Invariants"
line_start: 91962
line_end: 91978
dependencies:
  - "A.11"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "A.7"
  - "A.8"
  - "C.2.1"
  - "C.3"
  - "E.10"
  - "E.10.ARCH"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.24.UK"
  - "E.9"
  - "F.1"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.9"
keywords:
  - "decision lattice"
  - "minting new U-kinds"
  - "parsimony"
  - "reuse"
  - "type explosion"
---

### F.8:5 - Invariants

1. **Governed value before disposition.** The candidate expression, exact governed value or relation, direct pattern, and one proposed use are named before any F.8 result.
2. **One decision, one exact use.** Mixed expressions are split by governed value and use before deciding.
3. **Lightest sufficient result.** Local phrase, existing designation, alias, direct-pattern name, and admitted row reuse are tried before a cell, NameCard, new row, policy identifier, or U-kind candidate.
4. **Reuse preserves identity.** Reuse cannot change kind, scope, occurrence identity, local-sense claim, admitted use, or authority.
5. **Local senses do not globalize.** Reusing a designation under one effective ReferenceScheme establishes neither sameness with another cell nor an F.9 Bridge.
6. **Role names are work-facing.** A role name or RoleDescription label points to an independently recovered work-facing `U.Role`; status, evidence, access, source, publication, requirement, assurance, gate, decision, policy, and relation-position uses remain direct-pattern values.
7. **Role assignment and Work are not naming.** A name, decision result, NameCard, cell, row, or identifier neither assigns a holder nor demonstrates performed Work.
8. **Rows stay within admitted use.** F.8 may reuse an F.17 row only at its declared use and gains no equivalence from the row.
9. **Decision occurrence and description stay distinct.** A C.2.1 result episteme or displayed record can describe a separately identified decision occurrence but cannot perform it.
10. **Naming objects stay distinct.** Governed value, designation, alias, cell, basis relation, NameCard, row, identifier, publication occurrence, form, carrier, and currentness relation imply none of the others.
11. **Selected structure is conditional.** A bounded-model-use Structure is cited only when independently selected organization changes interpretation for this exact use; it is not a generic locality or identity slot.
12. **New U-kind candidates are rare.** Cross-family recurrence, irreducibility, `E.24.UK` admission, and accepted decision basis are necessary; F.8 itself admits no U-kind.
13. **Policy identifiers are resolvable.** A policy identifier remains distinct from its policy specification, mint decision occurrence, and decision-result episteme or record.
14. **Labels grant no authority.** Source titles, review labels, suffixes, rows, records, and identifiers create no ontology, evidence, status, equivalence, permission, or publication authority.

