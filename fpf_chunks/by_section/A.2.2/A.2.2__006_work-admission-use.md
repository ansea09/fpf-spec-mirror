---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "U.Capability - System Ability Envelope and Measures"
section_id: "A.2.2:5"
section_title: "Work-Admission Use"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__006_work-admission-use.md"
commit_sha: "036c056e98c38522172c6b7b3ad08214281cc4e4"
heading_path:
  - "A.2.2 — U.Capability - System Ability Envelope and Measures"
  - "A.2.2:5 — Work-Admission Use"
line_start: 3459
line_end: 3483
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

- role assignment identifies which admitted holder system holds which role value under the exact role-taxonomy episteme and effective reference scheme throughout its obtaining extent; it does not say that the holder is acting;
- role state says whether that assignment is in a work-admitting state;
- one exact `U.Method` supplies the method-side condition, while an independently admitted `U.MethodDescription` or work-admission episteme may state the capability threshold used by the check;
- capability names the holder system's ability within the envelope, measure set, and window;
- capability-fit condition tests whether that instance meets the current threshold or gate need;
- after execution, A.15.1 identifies the dated Work occurrence, F.6 `performedUnderAssignment(W, RA)` attributes it to the exact assignment whose holder system actually performed it, and actual `enactsMethod(W, M)` relates the Work to the exact Method.

Do not put the threshold into the role name. Do not treat a role assignment as proof of ability or action. Do not let a role value, capability instance, Method, or MethodDescription perform the work. Do not treat a fit predicate, Q-Bundle, architecture-characteristic row, evidence relation, or currentness assessment as the capability instance. An algorithm-possession phrase is only a dispatch cue; it establishes neither dated performance nor `U.MethodDescription` membership.

