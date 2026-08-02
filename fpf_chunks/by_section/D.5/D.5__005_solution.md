---
chunk_kind: "child"
pattern_id: "D.5"
pattern_title: "Bias Audit and Ethical Assurance"
section_id: "D.5:2"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/D.5/D.5__005_solution.md"
commit_sha: "9a9a42e4d154021ca3f7415e0009a4214832f65f"
heading_path:
  - "D.5 — Bias Audit and Ethical Assurance"
  - "D.5:2 — Solution"
line_start: 68809
line_end: 68836
dependencies:
  - "A.10"
  - "B.3"
  - "C.16"
  - "C.28"
  - "D.1"
  - "D.2"
  - "D.3"
  - "D.4"
  - "E.13"
  - "E.17"
  - "E.5.4"
keywords:
---

### D.5:2 - Solution

Open a `BiasAuditAssuranceFrame@Context`:

```text
BiasAuditAssuranceFrame@Context:
  auditedEntityOfConcernRef
  boundedContextRef
  intendedUseRef
  affectedPeopleOrGroupRefs?
  affectedHolonRefs?
  metricOrModelRefs?
  policyOrPublicationRefs?
  biasConcernRefs
  fairnessClaimRef?
  impactClaimRef?
  causalFairnessUseRef?
  evidenceRefs
  assuranceClaimRefs?
  mitigationOrConstraintRefs?
  acceptedResidualRefs?
  admissibleUse
  inadmissibleOverread
  strongerSourceReturnCondition
```

The frame is not a universal ethics owner. It is the local audit object used when bias, fairness, impact, or ethical assurance is current.

