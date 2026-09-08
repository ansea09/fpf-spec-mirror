---
chunk_kind: "child"
pattern_id: "D.1"
pattern_title: "Ethical Value Plurality and FPF Boundary"
section_id: "D.1:2"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/D.1/D.1__005_solution.md"
commit_sha: "2154d21570c891bd5ed30fd6e6136f17f1942cae"
heading_path:
  - "D.1 — Ethical Value Plurality and FPF Boundary"
  - "D.1:2 — Solution"
line_start: 68927
line_end: 68962
dependencies:
  - "A.1"
  - "A.1.CSD"
  - "A.10"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.11.DUA"
  - "C.28"
  - "C.30.ILC"
  - "D.1"
  - "D.2"
  - "D.3"
  - "D.4"
  - "D.5"
  - "E.2"
keywords:
---

### D.1:2 - Solution

Start with the ethical claim or question, the affected EntityOfConcern, the value concern, and the present use of the answer. Name evidence and material uncertainty when the answer relies on them. If the task is to recognize the concern, a short statement of the value concern and next question completes that task; use `D.3` when its sides and tension need description.

To judge a use ethically admissible, explain how the value premises and available evidence support that judgement and where it remains limited. Recognizing a concern supplies neither that judgement nor permission to act.

Use an `EthicalValueFrame@Context` when the present reasoning or a later reader needs to compare value premises, distinguish the uses a judgement supports, or revisit a premise that can change it. This content can remain in the answer or an existing decision record. The following form groups the applicable content:

```text
EthicalValueFrame@Context:
  ethicalClaimRef
  affectedEntityOfConcernRef
  intendedEthicalUse
  claimScopeRef?: U.ClaimScope
  qualificationWindowRef?
  valueConcernRefs
  valueFrameEditionRefs?
  ethicalTheoryOrTraditionRefs?
  affectedHolonRefs?
  affectedSystemRefs?
  affectedEpistemeRefs?
  directResponsibilityRelationRefs?
  systemRoleAssignmentRefs?: FinSet(U.RelationRef constrained to U.SystemRoleAssignment)
  methodOrWorkRefs?
  transformationRefs?
  evidenceRefs?
  uncertaintyOrCurrentnessCondition?
  admissibleUse
  inadmissibleOverread?
  strongerSourceReturnCondition?
```

Include a source-return condition when a particular stronger claim or changed use needs it. Use `C.11.DUA` when the contribution or burden of a proposed frame, report, or evidence request is unresolved. The form creates no obligation to invent a further check or explain an inactive one.

This frame makes the value premises inspectable; the ethical judgement still needs its own reasoning. A utilitarian consequence claim, a deontic constraint, a virtue or character claim, a care-ethics concern, a rights claim, a professional-duty claim, and a project-specific value trade-off may all be admissible starting points, but they must not be presented as the same claim merely because the same word "ethical" appears.

