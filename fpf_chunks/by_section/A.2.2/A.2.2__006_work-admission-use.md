---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "U.Capability - System Ability Envelope and Measures"
section_id: "A.2.2:5"
section_title: "Work-Admission Use"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__006_work-admission-use.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "A.2.2 — U.Capability - System Ability Envelope and Measures"
  - "A.2.2:5 — Work-Admission Use"
line_start: 3626
line_end: 3650
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

A Method step or Work claim may require both an exact system-role assignment and capability conditions.

```text
WorkAdmissionCheck:
  systemRoleAssignmentCurrent: A.2.1 direct species under U.SystemRoleAssignment
  systemRoleAssignmentStateAdmitsWork: A.2.5
  methodStepRequires: A.3.1 or A.3.2
  holderCapabilityRef: A.2.2
  capabilityFitCondition: admission predicate over declared capability measures and any named characteristic, Q-Bundle, or architecture-characteristic inputs
  performedWorkRecord: A.15.1 after execution
```

The checks are separate:

- one `U.SystemRoleAssignment` species defines the holder and assigned-kind participant meanings, the local system-role-kind domain, and any other participant meaning that changes the assignment predicate or occurrence identity; an occurrence supplies the holder System and other values for the case, and neither species nor occurrence establishes capability or Work;
- `SystemRoleAssignmentStateRelation` says whether that assignment satisfies the selected state predicate over the required window;
- one exact `U.Method` supplies the method-side condition, while an independently admitted `U.MethodDescription` or work-admission episteme may state the capability threshold used by the check;
- capability names the holder system's ability within the envelope, measure set, and window;
- capability-fit condition tests whether that instance meets the current threshold or gate need;
- after execution, A.15.1 identifies the dated Work occurrence, F.6 `performedUnderAssignment(W, RA)` attributes it to the exact assignment whose holder system actually performed it, and actual `enactsMethod(W, M)` relates the Work to the exact Method.

Do not put the threshold into the local system-role-kind name. Do not treat a system-role classification or assignment as proof of ability or action. Do not let a local kind, assignment, capability instance, Method, or MethodDescription perform the Work. Do not treat a fit predicate, Q-Bundle, architecture-characteristic row, evidence relation, or currentness assessment as the capability instance. An algorithm-possession phrase is only a dispatch cue; it establishes neither dated performance nor `U.MethodDescription` membership.

