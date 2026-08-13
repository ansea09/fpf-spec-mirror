---
chunk_kind: "child"
pattern_id: "C.3.2"
pattern_title: "Kind Intent, Membership Judgment, and Extension"
section_id: "C.3.2:6"
section_title: "One Candidate Judgment"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.2/C.3.2__008_one-candidate-judgment.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "C.3.2 — Kind Intent, Membership Judgment, and Extension"
  - "C.3.2:6 — One Candidate Judgment"
line_start: 45209
line_end: 45227
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
  - "C.3.5"
  - "C.3.A"
  - "E.24.UK"
keywords:
---

### C.3.2:6 - One Candidate Judgment

For exposition, this pattern uses:

`J(candidate, kind, signatureEdition, slice) ∈ {true, false, unknown}`

This is local notation for an evaluation result, not a newly admitted U-kind, an A.14 `MemberOf` occurrence, a direct classification relation, or an evidence relation. Evaluation is reproducible: fixed four inputs and unchanged governed candidate facts yield the same result. The slice names concrete versions and an explicit temporal selector; unqualified `latest` or `current` is not an evaluation input.

1. **Recover the candidate first.** An entity candidate is already individuated under its direct pattern. A non-entity value keeps the identity, unit, scale, and interpretation supplied by the pattern governing that value.
2. **Pin all four inputs.** Name the candidate, local kind, exact `KindSignature` edition, and exact `U.ContextSlice`.
3. **Evaluate direct governed features.** A satisfied criterion gives `true`; a known failed criterion gives `false`.
4. **Keep non-settlement visible.** Missing evidence, an unavailable declared dependency, or a candidate outside the declared evaluation domain gives `unknown`, not `false`.
5. **Separate support from satisfaction.** An observation, measurement result, source episteme, schema row, or evidence relation may support a classification assertion. It does not substitute for the candidate or make the criterion true merely by existing.
6. **Separate guard disposition.** A receiving guard checks scope coverage and the classification result as separate predicates and may decline use when the result is `unknown`. That fail-closed use decision does not convert the judgment to `false` and does not change the candidate's world-side features.

When a separate claim-bearing classification assertion is current, it is a C.2.1 episteme. Its exact `EntityOfConcern` is the governed entity about which the classification matters, and its claim content designates the candidate entity or value, local kind, signature edition, context slice, judgment, and relied-on evidence. A value classification may remain inside another claim's content instead of fabricating a value-shaped `EntityOfConcern`. The assertion creates neither candidate nor kind.

A domain that genuinely needs a durable classification-relation occurrence as an object of later relations must supply a separate direct pattern with exact participants, obtaining predicate, occurrence identity, and relation to this judgment. C.3.2 does not mint that occurrence by default.

