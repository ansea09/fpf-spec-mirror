---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "System Capability: Conditions, Measures and Fit"
section_id: "A.2.2:3"
section_title: "Positive Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__004_positive-solution.md"
commit_sha: "7bba05916e6e8ad42f868ed3aad0a7644fe0c354"
heading_path:
  - "A.2.2 — System Capability: Conditions, Measures and Fit"
  - "A.2.2:3 — Positive Solution"
line_start: 4191
line_end: 4226
dependencies:
  - "A.1"
  - "A.15"
  - "A.2.3"
  - "A.2.6"
  - "C.2.1"
  - "E.23.CDI"
keywords:
  - "attained bounds"
  - "capability fit"
  - "currentness"
  - "holder ability"
  - "qualification"
  - "support"
  - "work conditions"
---

### A.2.2:3 - Positive Solution

1. **Identify the holder and demanded result.** Recover the System and the work family or result class. Keep a desired development target distinct from what the holder can currently achieve.
2. **State the qualified ability.** Give the conditions and attained bounds claimed for that holder. Include relevant actual time or configuration. A useful sentence is “RobotArm_A can weld seam family W under conditions C at the stated precision and rate.”
3. **Recover sufficient support.** Reuse or obtain the evidence and source-use relations required by the receiving claim. Assess their currency under the applicable qualification policy. When sampled measurements support a bound, retain the uncertainty needed for the receiving decision; a point estimate close to its limit may leave the comparison unresolved. Missing support leaves reliance unresolved; it is not proof of inability.
4. **Compare with the receiving demand.** Under A.2.6, test whether the declared WorkScope covers the intended `JobSlice`, whether the claimed attained bounds meet the required bounds, and whether qualification holds at the evaluation time. If a necessary condition or translation is missing, name it instead of returning a positive fit.
5. **Apply the remaining entry conditions only when required.** Authority, assignment and assignment state, resources, interfaces, Method-side conditions and assurance retain their direct governors. Passing the capability comparison supplies only its part of the receiving decision.
6. **Return the bounded answer.** State the supported ability and fit, the mismatch, or the exact unresolved premise. Stop when that answer suffices. A described check does not assert that Work occurred or that a proposed intervention achieved its target.

One possible statement-and-use record is shown below. It is a way to preserve the claims needed by this use, not a mandatory new entity or classification.

```text
CapabilityStatementRecord:
  capabilityHolderRef: U.System
  canDo: WorkFamilyOrResultClass
  workConditionBasis: U.WorkScope
  attainedMeasureBounds:
  actualTimeOrConfiguration?:
  capabilityStatementRef?: C.2.1 episteme
  evidenceOrSourceUseRefs:
  qualificationPolicy:
  currentnessAssessmentRefs?:

CapabilityFitCheck:
  holderAbilityClaim: the qualified proposition above
  receivingJobSlice:
  requiredMeasureBounds:
  evaluationTime:
  scopeCoverage:
  measureComparison:
  qualificationResult:
  result: fit, mismatch, or named unresolved premise
```

The record separates what is claimed about the System from the grounds for believing it and from what another use demands. The same supported ability may fit one demand and fail another.

