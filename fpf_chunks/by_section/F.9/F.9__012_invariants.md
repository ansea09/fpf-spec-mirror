---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment and Bridge across Contexts"
section_id: "F.9:10"
section_title: "Invariants"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__012_invariants.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "F.9 — Alignment and Bridge across Contexts"
  - "F.9:10 — Invariants"
line_start: 95796
line_end: 95813
dependencies:
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.6.3.CSC"
  - "A.6.5"
  - "A.6.9"
  - "A.6.REL"
  - "B.3"
  - "C.2.1"
  - "C.26.1"
  - "C.26.2"
  - "C.29"
  - "C.3"
  - "E.10.ROLE"
  - "E.17.ID.CR"
  - "E.24.PUB"
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
7. **Reliance is separate.** A.10 says whether ordinary evidence supports relying on the bounded-use claim. When an actual named assurance claim is current, B.3 supplies its bounded `AssuranceResult`. Neither answer comes from F.9 or the Card.
8. **Proposed use is not an occurrence.** The `u` designation in the ClaimGraph names the proposed use; any actual Work, assertion, publication, relation, or operation application keeps its own identity; apply the relevant pattern to each claim about it.
9. **Card separation.** Card identity, completion, approval, registration, and publication neither make the relation obtain nor make the use happen.
10. **Loss separation.** Observed semantic loss is evidence; permitted loss is tolerance inside the bounded-use claim.
11. **No authorization by implication.** Semantic suitability, evidence reliance, and assurance are not legal, policy, or deontic permission.
12. **No silent inverse or composition.** An inverse asymmetric relation and any direct A-to-C relation are tested independently.
13. **Two-SlotSpec declaration.** The reusable RelationSignature declares only source and receiving SenseCell participant meanings; `CL`, Loss Notes, scope/admitted use, evidence, counterexamples, policy, time, model-use structure, description, publication, and registry values remain qualifiers or neighbors.
14. **Recurrence and identity.** The non-optional identity rule uses the canonical exact endpoints and exact profile; one fixed tuple/profile is non-recurrent, and a changed applicability/as-of basis changes the profile before another candidate is admitted.
15. **Description and publication separation.** A Bridge description/Card is independently constituted under C.2.1, and E.24.PUB independently governs any selected edition's publication occurrence, form, and carrier. None establishes relation truth or identity.

