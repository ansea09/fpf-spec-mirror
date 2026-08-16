---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "U.Capability - System Ability Envelope and Measures"
section_id: "A.2.2:3"
section_title: "Positive Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__004_positive-solution.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "A.2.2 — U.Capability - System Ability Envelope and Measures"
  - "A.2.2:3 — Positive Solution"
line_start: 3576
line_end: 3613
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.3"
  - "E.24.UK"
keywords:
  - "ability envelope"
  - "capability-fit condition"
  - "currentness"
  - "holder-dependent capability instance"
  - "measure set"
  - "qualification window"
---

### A.2.2:3 - Positive Solution

Use `U.Capability` when the object under discussion is the holder's ability to achieve a result class within a declared envelope and measure set.

Minimal capability instance:

```text
ConcreteCapabilityInstance:
  holder: U.System
  canDo: WorkFamilyOrResultClass
  envelope: CapabilityEnvelope
  measures: CapabilityMeasureSet
  qualificationWindow: QualificationWindow
  currentnessCondition: CapabilityCurrentnessCondition
```

Separate supporting record:

```text
CapabilityStatementRecord:
  describedCapabilityRef: ConcreteCapabilityInstance
  statementSourceRef:
  evidenceOrSourceUseRefs:
  currentnessAssessmentRefs?:
```

Plain sentence form:

```text
<System> can perform <work family or result class>
within <envelope>
at <measures>
during <qualification window>,
with <evidence or source-use relation>.
```

This sentence form is a publication or statement about the capability instance. It is deliberately not a MethodDescription. It does not list the step order or algorithm. It also does not classify the holder under a system-role kind, assign the holder, assert that a Work occurrence happened, prove an architecture characteristic, or make the evidence relation into the capability.

