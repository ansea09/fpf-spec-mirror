---
chunk_kind: "child"
pattern_id: "D.5"
pattern_title: "Bias Audit and Ethical Assurance"
section_id: "D.5:2"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/D.5/D.5__005_solution.md"
commit_sha: "aa10af7e8221518114822d00bb9cf11e6c41f6b2"
heading_path:
  - "D.5 — Bias Audit and Ethical Assurance"
  - "D.5:2 — Solution"
line_start: 69895
line_end: 69931
dependencies:
  - "A.10"
  - "B.3"
  - "C.11.DUA"
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

Identify the object, the bias or fairness concern, and the use the answer must support. Give the result warranted by the available basis, with the affected groups and limitations that change that use. A metric comparison can finish at its qualified measurement result; recognizing a value conflict returns to `D.3` or `D.4`.

An intended audit, fairness, or assurance conclusion must satisfy its own evidence conditions. A missing basis leaves that conclusion unsupported. Select further investigation and the record it needs for that particular claim or decision, using §3.1.

Use `BiasAuditAssuranceFrame@Context` to organize an audit whose recipient needs to inspect the connection among claims, evidence, constraints, and residuals. The applicable content may already be present in the result being used:

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
  evidenceRefs?
  assuranceClaimRefs?
  assuranceUseRef?
  mitigationOrConstraintRefs?
  acceptedResidualRefs?
  admissibleUse
  inadmissibleOverread?
  strongerSourceReturnCondition?
```

The frame organizes the audit account. It is neither the object being audited nor evidence that its use is fair. Include relied-on evidence and any stronger-source return needed by the particular conclusion.

