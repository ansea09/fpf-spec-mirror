---
chunk_kind: "child"
pattern_id: "D.5"
pattern_title: "Bias Audit and Ethical Assurance"
section_id: "D.5:2"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/D.5/D.5__005_solution.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "D.5 — Bias Audit and Ethical Assurance"
  - "D.5:2 — Solution"
line_start: 68013
line_end: 68045
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
  intendedUseRef
  claimScopeRef?: U.ClaimScope
  qualificationWindowRef?
  affectedPopulationRefs?
  affectedSystemRefs?
  affectedHolonRefs?
  metricOrModelRefs?
  policyOrPublicationRefs?
  biasConcernRefs
  ethicalClaimRefs?
  fairnessClaimRef?
  impactClaimRef?
  causalFairnessUseRef?
  causalUseSupportResultRef?: CausalUseSupportResultRef
  evidenceRefs
  assuranceClaimRefs?
  assuranceUseRef?
  mitigationOrConstraintRefs?
  acceptedResidualRefs?
  admissibleUse
  inadmissibleOverread
  strongerSourceReturnCondition
```

The frame is not a universal ethics owner. It is the local audit object used when bias, fairness, impact, or ethical assurance is current.

