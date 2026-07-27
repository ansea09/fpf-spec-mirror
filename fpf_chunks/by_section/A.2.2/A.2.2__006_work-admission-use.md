---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "U.Capability - System Ability Envelope and Measures"
section_id: "A.2.2:5"
section_title: "Work-Admission Use"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__006_work-admission-use.md"
commit_sha: "66e732dfef7a4a93ff23eec43b3f759a6664652d"
heading_path:
  - "A.2.2 — U.Capability - System Ability Envelope and Measures"
  - "A.2.2:5 — Work-Admission Use"
line_start: 2986
line_end: 3010
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

### A.2.2:5 - Work-Admission Use

A method step or work claim may require both role and capability conditions.

```text
WorkAdmissionCheck:
  roleAssignmentCurrent: A.2.1
  roleStateAdmitsWork: A.2.5
  methodStepRequires: A.3.1 or A.3.2
  holderCapabilityRef: A.2.2
  capabilityFitCondition: admission predicate over declared capability measures and any named characteristic, Q-Bundle, or architecture-characteristic inputs
  performedWorkRecord: A.15.1 after execution
```

The checks are separate:

- role assignment says who is acting in which context;
- role state says whether that assignment is in a work-admitting state;
- method or method description says what capability threshold is required;
- capability names the holder's capability instance within the envelope, measure set, and window;
- capability-fit condition tests whether that instance meets the current threshold or gate need;
- performed work says what actually happened.

Do not put the threshold into the role name. Do not treat a role assignment as proof of ability. Do not let a capability instance perform the work. Do not treat a fit predicate, Q-Bundle, architecture-characteristic row, evidence relation, or currentness assessment as the capability instance.

