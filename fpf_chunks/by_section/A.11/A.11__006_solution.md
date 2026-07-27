---
chunk_kind: "child"
pattern_id: "A.11"
pattern_title: "Ontological Parsimony"
section_id: "A.11:2"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.11/A.11__006_solution.md"
commit_sha: "66e732dfef7a4a93ff23eec43b3f759a6664652d"
heading_path:
  - "A.11 — Ontological Parsimony"
  - "A.11:2 — Solution"
line_start: 23059
line_end: 23092
dependencies:
  - "A.8"
  - "C.3"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.18"
  - "F.8"
keywords:
  - "U-kind admission"
  - "composition"
  - "kernel growth"
  - "non-redundancy"
  - "parsimony"
---

### A.11:2 - Solution

Use four gates before admitting the new ontology addition:

| Gate | Test question | Pass condition |
| --- | --- | --- |
| Composition | Can existing U-kinds, slots, relations, dependent values, or direct patterns express the claim? | Pass only when expression by composition loses a reviewable distinction. |
| Non-redundancy | Does the candidate overlap an existing governed value or relation? | Pass only when overlap is bounded and the remaining difference changes admissible claims. |
| Action-facing contribution | What can users claim, compare, repair, stop, rely on, or do because this addition exists? | Pass only when the contribution is not merely naming comfort or source prestige. |
| Sharp boundary | Is there a one-sentence inclusion and exclusion test? | Pass only when readers can distinguish included and excluded cases without private author intent. |

Use this compact record:

```text
ParsimonyAdmissionRecord:
  Candidate:
  RecoveredGovernedObject:
  E24UKDecisionRef:
  ExistingExpressionAttempt:
  MaterialLossIfComposed:
  OverlapWithExistingValues:
  ActionFacingContribution:
  BoundaryTest:
  Disposition:
```

Possible dispositions:

- retain as root U-kind;
- retain as dependent durable value under a root settlement;
- apply C.3 typed reasoning;
- express as slot, relation, record, publication form, lens, local frame, or direct governed value;
- keep as source wording or local name.

