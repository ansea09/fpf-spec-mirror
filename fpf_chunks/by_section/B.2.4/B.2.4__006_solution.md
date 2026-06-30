---
chunk_kind: "child"
pattern_id: "B.2.4"
pattern_title: "Capability and Functioning Whole Reidentification"
section_id: "B.2.4:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.4/B.2.4__006_solution.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "B.2.4 — Capability and Functioning Whole Reidentification"
  - "B.2.4:4 — Solution"
line_start: 33742
line_end: 33816
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2.2"
  - "A.22"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.F"
  - "A.6.M"
  - "B.2"
  - "B.2.P"
  - "C.16"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.TFS-REL"
  - "E.18"
keywords:
---

### B.2.4:4 - Solution

Use B.2.4 as a decision bridge from capability and functioning evidence to B.2 whole reidentification.

#### B.2.4:4.1 - Capability-Functioning Whole-Reidentification Slice

Use this slice only when B.2 remains current after direct-owner explanations are checked.

```text
CapabilityFunctioningWholeReidentificationSlice@Context:
  existingWholeRef: U.Holon
  boundedContextRef:
  capabilityEnvelopeRef?
  functioningRelationRef?
  transformationFlowStructureRef?
  functionalStructureViewRef?
  candidateBearerRefs?
  methodRelationRefs?
  methodDescriptionRefs?
  workPlanRefs?
  workOccurrenceRefs?
  moduleAllocationRefs?
  characteristicOrThresholdRefs?
  evidenceOrMeasurementRefs:
  existingWholeExplanationCheckRef: ExistingWholeExplanationCheck@Context
  candidateB2RecordRef:
  blockedDirectOwnerOverreads:
```

This slice is not a U-kind and not a capability object. It carries the evidence needed to decide whether B.2 whole reidentification is current.

#### B.2.4:4.2 - Direct-Owner Test

Before using B.2.4 for whole reidentification, test whether a direct owner explains the evidence:

| Evidence under concern | Direct owner if sufficient | B.2.4 becomes current only when |
| --- | --- | --- |
| Capability envelope | `A.2.2`, `C.16`, `A.10` | the envelope belongs to a result whole that cannot be explained by the existing whole |
| Function or functioning relation | `A.6.F`, `A.3.4`, `C.16` | the relation creates or reveals a new whole-level EntityOfConcern |
| Transformation-flow structure | `C.30.TFS-REL`, `E.18`, `A.3.4`, `C.29` when mathematical lens is current | the flow structure changes the identity of the whole under B.2 |
| Method relation or method family | `A.15`, `A.3.1`, `G.5`, `C.29` when lens is current | method evidence changes the whole, not merely the way of doing |
| Method description or procedure text | `A.3.2` and `C.2.1`; use publication-use or source-use owners when publication or source reliance is current | description is not enough; in-life whole reidentification must be recovered |
| Work plan or work occurrence | `A.15.2`, `A.15.1` | performed or planned work is evidence for a result whole, not the whole by label |
| Module, component, or bearer allocation | `A.6.M`, `C.30`, `A.22`, `C.30.ASV` | allocation evidence changes the whole under concern |
| Metric, score, threshold, robustness, quality | `C.16`, `A.19`, `A.10` | the characteristic shift defeats existing-whole explanation |

#### B.2.4:4.3 - Existing-Whole Explanation

Use `ExistingWholeExplanationCheck@Context` before claiming whole reidentification.

Direct-owner explanations that often stop B.2.4:

- better measurement or benchmark normalization;
- improved component capability;
- corrected function-like wording;
- a clearer method relation or method family selection;
- a new method description without performed capability evidence;
- better work coordination inside the same whole;
- module allocation repair;
- architecture-view or transformation-flow-structure repair;
- evidence or source-currentness improvement.

If one of these explanations is sufficient, do not use B.2.4. Use the direct owner.

#### B.2.4:4.4 - When B.2.4 Returns To B.2

Return to B.2 when the evidence shows that the current object must be reidentified as a result holon. Examples:

- a production cell now has a capability envelope, coordination relation, transformation-flow structure, and assurance claim that cannot be explained by individual machines;
- a service platform now has a functioning relation and external commitments that cannot be assigned to one service or module;
- a team, toolchain, and method family now operate as one result system with new capability and work evidence;
- an episteme or standard now has a capability for explanation, prediction, or specification use that requires result-episteme reidentification.

After the return, B.2 owns the MHT record and result-kind admission. B.2.4 carries only the capability and functioning evidence slice.

