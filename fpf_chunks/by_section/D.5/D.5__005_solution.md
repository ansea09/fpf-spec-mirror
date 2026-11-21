---
chunk_kind: "child"
pattern_id: "D.5"
pattern_title: "Bias Audit and Ethical Assurance"
section_id: "D.5:2"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/D.5/D.5__005_solution.md"
commit_sha: "dba39812b83cac74dd2a3251c134cdc23dfaec86"
heading_path:
  - "D.5 — Bias Audit and Ethical Assurance"
  - "D.5:2 — Solution"
line_start: 97486
line_end: 97524
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

For a claim about a group, state what the conclusion attributes to whom. An eligibility rule can establish who is entitled to a service under its stated conditions. Whether people received the service depends on what happened. For a measured rate, identify the unit counted, the numerator and denominator, the period and which eligible units entered the evidence. An overall rate can meet its target while a subgroup misses it. Rates for two overlapping groups can each meet the target while their intersection falls short. Subtracting a subgroup’s numerator and denominator from the corresponding population counts gives the counts outside that subgroup. Use them for another named group only if it covers exactly the remaining records. If the evidence already establishes the required outcome for every member of the covered population, the same member-by-member finding holds within each subgroup. A verified violation can refute such an all-member claim without establishing how frequent the violation is. For a different population or period, establish which conditions of the rule or of the empirical comparison still apply.

An intended audit, fairness, or assurance conclusion must satisfy its evidence conditions. A missing basis leaves that conclusion unsupported. Select further investigation and the record it needs for that claim or decision, using §3.1.

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

The frame organizes the audit account. Include relied-on evidence and any stronger-source return needed by the conclusion.

