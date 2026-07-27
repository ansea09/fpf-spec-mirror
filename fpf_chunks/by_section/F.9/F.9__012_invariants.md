---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment and Bridge across Contexts"
section_id: "F.9:10"
section_title: "Invariants"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__012_invariants.md"
commit_sha: "66e732dfef7a4a93ff23eec43b3f759a6664652d"
heading_path:
  - "F.9 — Alignment and Bridge across Contexts"
  - "F.9:10 — Invariants"
line_start: 89889
line_end: 89903
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.6.3.CSC"
  - "A.6.5"
  - "A.6.9"
  - "B.3"
  - "C.2.1"
  - "C.26.1"
  - "C.26.2"
  - "C.29"
  - "E.17.ID.CR"
  - "F.0.1"
  - "F.10"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9.1"
keywords:
  - "A.10/B.3 reliance"
  - "LocalSenseClaim> projections"
  - "different <ReferenceScheme"
  - "exact F.17 SchemeSenseCell endpoints"
  - "inverse/composition checks"
  - "obtaining Bridge"
  - "optional CL evidence-strength shorthand"
  - "optional card"
  - "quantum/coarsening exit"
  - "relation-semantic profile"
  - "separate C.2.1 bounded-use claim"
---

### F.9:10 - Invariants

1. **Exact endpoints first.** A Bridge has exactly two F.17 `SchemeSenseCell` participants.
2. **No context object.** Semantic context is recovered from endpoint content and is not a relation participant.
3. **Different context is not enough.** Different projections trigger the question but do not establish the relation.
4. **Profile contains relation semantics only.** Receiving use, direction, use rule, loss tolerance, polarity, reliance, authorization, and receiving objects are absent from profile identity.
5. **Obtaining before occurrence reference.** A positive Bridge reference appears only after the fixed predicate is true and its dependencies are present.
6. **Use claim is separate.** Every proposed use names `u`, `d`, `r`, `t`, and polarity in a C.2.1 claim about the exact Bridge.
7. **Reliance is separate.** A.10 or B.3, not F.9 or the card, says whether current evidence or assurance supports relying on that claim.
8. **Role is not occurrence.** The named receiving-use role is ClaimGraph content; any actual Work, assertion, publication, relation, or operation application keeps its own identity and owner.
9. **Card separation.** Card identity, completion, approval, registration, and publication neither make the relation obtain nor make the use happen.
10. **Loss separation.** Observed semantic loss is evidence; permitted loss is tolerance inside the bounded-use claim.
11. **No authorization by implication.** Semantic suitability, evidence reliance, and assurance are not legal, policy, or deontic permission.
12. **No silent inverse or composition.** An inverse asymmetric relation and any direct A-to-C relation are tested independently.

