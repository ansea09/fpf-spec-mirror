---
chunk_kind: "child"
pattern_id: "C.3.2"
pattern_title: "Kind Intent, Membership Judgment, and Extension"
section_id: "C.3.2:6"
section_title: "Admissibility and One Candidate Judgment"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.2/C.3.2__008_admissibility-and-one-candidate-judgment.md"
commit_sha: "3c3f968398a938bc10e83da22d509b7b8f642d83"
heading_path:
  - "C.3.2 — Kind Intent, Membership Judgment, and Extension"
  - "C.3.2:6 — Admissibility and One Candidate Judgment"
line_start: 45409
line_end: 45432
dependencies:
  - "A.14"
  - "A.2.6"
  - "A.6.0"
  - "C.2.1"
  - "C.2.3"
  - "C.29"
  - "C.3"
  - "C.3.1"
  - "C.3.3"
  - "C.3.4"
  - "E.24.UK"
keywords:
---

### C.3.2:6 - Admissibility and One Candidate Judgment

For exposition, this pattern uses:

`A(candidate, kind, signatureEdition, slice) ∈ {admissible, not-applicable}`

and, only when `A = admissible`:

`J(candidate, kind, signatureEdition, slice) ∈ {true, false, unknown}`

These are local result notations, not newly admitted kinds, A.14 membership occurrences, direct classification relations, or evidence relations. For a fixed candidate, kind, signature edition, and slice, unchanged governed conditions yield the same result; the slice resolves concrete versions and an explicit temporal selector rather than implicit `latest` or `current`.

1. **Recover the candidate first.** An entity is already individuated under its direct pattern. A non-entity value keeps the identity, unit, scale, and interpretation supplied by its governor.
2. **Pin the inputs.** Name candidate, kind, exact signature edition, and exact slice; avoid implicit `latest` or `current`.
3. **Check admissibility.** If the candidate does not satisfy the declared candidate `ValueKind` or interpretation, or the slice is outside declared applicability, return `not-applicable` and stop. Do not form `J`.
4. **Evaluate the governed condition.** For an admissible candidate, a satisfied criterion gives `true`; a known failed criterion gives `false`.
5. **Keep non-settlement visible.** Missing support or an unavailable declared dependency gives `unknown`, not `false`.
6. **Distinguish condition from evidentiary use.** A measurement result, source episteme, certification, registration, publication occurrence, legal-status relation, or record may itself be a criterion condition only when the signature says so and its direct pattern makes that condition obtain. Its mere use as evidence for some other condition creates neither that condition nor membership.
7. **Separate guard disposition.** A guard checks admissibility, scope coverage, and any judgment as separate predicates. It may decline use on `not-applicable` or `unknown` without converting either to `false`.

When a separate claim-bearing classification assertion is current, it is a C.2.1 episteme. Its content designates the candidate, kind, signature edition, slice, admissibility, any judgment, and relied-on support. Its exact `EntityOfConcern` is the governed entity about which classification matters; a value classification may stay in another claim's content rather than fabricating a value-shaped entity. The assertion creates neither candidate nor kind.

A domain that genuinely needs a durable classification-relation occurrence must supply a separate direct pattern with exact participants, obtaining condition, identity, and relation to these results. C.3.2 does not mint that occurrence.

