---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "System Capability: Conditions, Measures and Fit"
section_id: "A.2.2:5"
section_title: "Work-Admission Use"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__006_work-admission-use.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "A.2.2 — System Capability: Conditions, Measures and Fit"
  - "A.2.2:5 — Work-Admission Use"
line_start: 4239
line_end: 4263
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

### A.2.2:5 - Work-Admission Use

A Method step or Work claim may require both an exact system-role assignment and capability conditions.

```text
WorkAdmissionCheck:
  systemRoleAssignmentCurrent: A.2.1 direct species under U.SystemRoleAssignment
  systemRoleAssignmentStateAdmitsWork: A.2.5
  methodStepRequires: A.3.1 or A.3.2
  holderAbilityClaim: A.2.2 qualified claim about the assignment holder
  capabilityFitCondition: admission predicate over declared capability measures and any named characteristic, Q-Bundle, or architecture-characteristic inputs
  performedWorkRecord: A.15.1 after execution
```

The checks are separate:

- one `U.SystemRoleAssignment` species defines the holder and assigned-kind participant meanings, the local system-role-kind domain, and any other participant meaning that changes the assignment predicate or occurrence identity; an occurrence supplies the holder System and other values for the case, and neither species nor occurrence establishes capability or Work;
- `SystemRoleAssignmentStateRelation` says whether that assignment satisfies the selected state predicate over the required window;
- one exact `U.Method` supplies the method-side condition, while an independently admitted `U.MethodDescription` or work-admission episteme may state the capability threshold used by the check;
- the ability claim states what the holder can achieve under the declared conditions and attained bounds;
- the capability-fit condition compares that qualified claim with the current work conditions and required bounds;
- after execution, A.13 first recovers the exact actual performer and A.15.1 independently admits the dated Work occurrence; F.6 `performedUnderAssignment(W, RA)` is added only when this capability account or its receiving use expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment, while actual `enactsMethod(W, M)` separately relates the Work to the exact Method;

Do not put the threshold into the local system-role-kind name.

