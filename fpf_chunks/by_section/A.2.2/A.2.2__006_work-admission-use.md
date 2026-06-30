---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "U.Capability - System Ability Envelope and Measures"
section_id: "A.2.2:5"
section_title: "Work-Admission Use"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__006_work-admission-use.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "A.2.2 — U.Capability - System Ability Envelope and Measures"
  - "A.2.2:5 — Work-Admission Use"
line_start: 2742
line_end: 2764
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

### A.2.2:5 - Work-Admission Use

A method step or work claim may require both role and capability conditions.

```text
WorkAdmissionCheck:
  roleAssignmentCurrent: A.2.1
  roleStateAdmitsWork: A.2.5
  methodStepRequires: A.3.1 or A.3.2
  holderCapabilityMeets: A.2.2
  performedWorkRecord: A.15.1 after execution
```

The checks are separate:

- role assignment says who is acting in which context;
- role state says whether that assignment is in a work-admitting state;
- method or method description says what capability threshold is required;
- capability says whether the holder can meet that threshold within the envelope and window;
- performed work says what actually happened.

Do not put the threshold into the role name. Do not treat a role assignment as proof of ability. Do not let a capability claim perform the work.

