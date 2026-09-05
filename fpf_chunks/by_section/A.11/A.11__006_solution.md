---
chunk_kind: "child"
pattern_id: "A.11"
pattern_title: "Ontological Parsimony"
section_id: "A.11:2"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.11/A.11__006_solution.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "A.11 — Ontological Parsimony"
  - "A.11:2 — Solution"
line_start: 23432
line_end: 23470
dependencies:
  - "A.6.P"
  - "A.6.RCD"
  - "A.8"
  - "C.3"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.18"
  - "F.8"
keywords:
---

### A.11:2 - Solution

Use four gates before admitting the new ontology addition. Apply every gate to the same exact candidate, receiving claim or use, and current facts. Record the best existing expression first; then state the exact loss, overlap discriminator, newly admissible claim or action, and nearest excluded case for that same use.

| Gate | Test question | Pass condition |
| --- | --- | --- |
| Composition | What is the best existing governed expression for this exact receiving claim or use? | Pass only when that expression loses a stated claim, boundary, or admissible use. |
| Non-redundancy | How far does the candidate overlap an existing governed value or relation, and what discriminates the remainder? | Pass only when the bounded remainder changes an admissible claim for the same use. |
| Action-facing contribution | Which exact claim or action becomes admissible because this addition exists? | Pass only when that contribution reaches the named use rather than supplying naming comfort or source prestige. |
| Sharp boundary | What is the one-sentence inclusion test, and which nearest case is excluded? | Pass only when both cases can be distinguished from stated facts without private author intent. |

Use this compact record:

```text
ParsimonyAdmissionRecord:
  Candidate:
  RecoveredGovernedObject:
  E24FamilySettlementDecisionRef: exact shared decision governed by E.24:4.0a
  ReceivingClaimOrUse:
  CurrentFactsRef:
  ExistingExpressionAttempt: best existing governed expression for that claim or use
  MaterialLossIfComposed: exact lost claim, boundary, or admissible use
  OverlapWithExistingValues: extent plus discriminator
  ActionFacingContribution: exact newly admissible claim or action
  BoundaryTest: inclusion test plus nearest excluded case
  Disposition:
```

Possible dispositions:

- retain as a root U-kind;
- retain as a dependent durable value under a root settlement;
- retain as a local C.3 kind or typed claim;
- express through an existing governed expression;
- keep as source wording or a local name;
- for a relation-kind candidate, stop at the exact `A.6.RCD` existing-predicate, local-compound, subject-bounded-law, or reusable-predicate-definition result;
- retain a derived relation-kind candidate only with the required occurrence semantics and direct settlement; or
- retain an irreducible primitive relation-kind candidate only when `A.6.RCD` disposition 4 passes.

