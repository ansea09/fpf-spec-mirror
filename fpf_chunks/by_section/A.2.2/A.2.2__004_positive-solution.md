---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "U.Capability - System Ability Envelope and Measures"
section_id: "A.2.2:3"
section_title: "Positive Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__004_positive-solution.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "A.2.2 — U.Capability - System Ability Envelope and Measures"
  - "A.2.2:3 — Positive Solution"
line_start: 2629
line_end: 2656
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.3"
keywords:
  - "ability"
  - "action"
  - "measures"
  - "performance"
  - "skill"
  - "work scope"
---

### A.2.2:3 - Positive Solution

Use `U.Capability` when the object under discussion is the holder's ability to achieve a result class within a declared envelope and measure set.

Minimal capability statement:

```text
CapabilityStatement:
  holder: U.System
  canDo: WorkFamilyOrResultClass
  envelope: CapabilityEnvelope
  measures: CapabilityMeasureSet
  qualificationWindow: QualificationWindow
  evidenceOrSourceUse: EvidenceOrSourceUseRefs
```

Plain sentence form:

```text
<System> can perform <work family or result class>
within <envelope>
at <measures>
during <qualification window>,
with <evidence or source-use relation>.
```

This form is deliberately not a method description. It does not list the step order or algorithm. It also does not assign the holder to a role or assert that a work occurrence happened.

