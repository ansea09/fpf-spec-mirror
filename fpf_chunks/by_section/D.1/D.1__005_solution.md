---
chunk_kind: "child"
pattern_id: "D.1"
pattern_title: "Ethical Value Plurality and FPF Boundary"
section_id: "D.1:2"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/D.1/D.1__005_solution.md"
commit_sha: "d1f696e7c7767705206a8cacd9f6ed48e4dc5b02"
heading_path:
  - "D.1 — Ethical Value Plurality and FPF Boundary"
  - "D.1:2 — Solution"
line_start: 67607
line_end: 67631
dependencies:
  - "A.1"
  - "A.10"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.28"
  - "C.30.ILC"
  - "D.2"
  - "D.3"
  - "D.4"
  - "D.5"
  - "E.2"
keywords:
---

### D.1:2 - Solution

Recover an `EthicalValueFrame@Context` before treating the claim as ethically admissible:

```text
EthicalValueFrame@Context:
  ethicalClaimRef
  affectedEntityOfConcernRef
  boundedContextRef
  valueConcernRefs
  ethicalTheoryOrTraditionRefs?
  affectedHolonRefs?
  affectedEpistemeRefs?
  roleAssignmentRefs?
  methodOrWorkRefs?
  transformationRefs?
  evidenceRefs
  uncertaintyOrCurrentnessCondition
  admissibleUse
  inadmissibleOverread
  strongerSourceReturnCondition
```

This frame does not settle the ethical question. It makes the value frame inspectable. A utilitarian consequence claim, a deontic constraint, a virtue or character claim, a care-ethics concern, a rights claim, a professional-duty claim, and a project-specific value trade-off may all be admissible starting points, but they must not be presented as the same claim merely because the same word "ethical" appears.

