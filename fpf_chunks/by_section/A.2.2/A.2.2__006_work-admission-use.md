---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "System Capability: Conditions, Measures and Fit"
section_id: "A.2.2:5"
section_title: "Work-Admission Use"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__006_work-admission-use.md"
commit_sha: "6226816d8005a4c8ee3af338bb3752f6732449a9"
heading_path:
  - "A.2.2 — System Capability: Conditions, Measures and Fit"
  - "A.2.2:5 — Work-Admission Use"
line_start: 5575
line_end: 5601
dependencies:
  - "A.1"
  - "A.15"
  - "A.2.3"
  - "A.2.6"
  - "C.2.1"
  - "C.32.MWA.PP"
  - "E.23.CDI"
keywords:
  - "Method-relative capability"
  - "attained bounds"
  - "capability fit"
  - "currentness"
  - "holder ability"
  - "qualification"
  - "support"
  - "usable Method structure"
  - "work conditions"
---

### A.2.2:5 - Work-Admission Use

A Method step or a proposed performance can require an exact system-role assignment as well as a qualified ability. Decide which authority is needed to allocate work today and when each holder's assignment and state must obtain for performance. A.2.1 and A.2.5 govern those facts. When different local role kinds must be filled together, apply the holder rule in A.2.7:4.5. When the same kind is needed for several performances, use the required performances, times and allowed substitutions. A.15.2 can express that plan and its shared means. A personnel recommendation can finish an assessment commission. An appointment takes effect under the rule and authority that establish it.

```text
WorkAdmissionCheck:
  systemRoleAssignmentCurrent: A.2.1 direct species under U.SystemRoleAssignment
  systemRoleAssignmentStateAdmitsWork: A.2.5
  methodStepRequires: A.3.1 or A.3.2
  holderAbilityClaim: A.2.2 qualified claim about the assignment holder
  capabilityFitCondition: admission predicate on the required performance and any declared measure, characteristic, Q-Bundle or architecture criterion the decision uses
  performedWorkRef?: A.15.1, only for a separately asserted dated Work occurrence
```

The checks are separate:

- one `U.SystemRoleAssignment` species defines the holder and assigned-kind participant meanings, the local system-role-kind domain, and any other participant meaning that changes the assignment predicate or occurrence identity; an occurrence supplies the holder System and other values for the case, and neither species nor occurrence establishes capability or Work;
- `SystemRoleAssignmentStateRelation` says whether that assignment satisfies the selected state predicate over the required window;
- one exact `U.Method` supplies the method-side condition, while an independently admitted `U.MethodDescription` or work-admission episteme may state the capability threshold used by the check;
- the ability claim states the result the holder can achieve under the declared conditions and to what standard;
- the capability-fit condition compares that qualified claim with the work conditions and the criterion the recipient requires;
- after execution, A.13 first recovers the actual performer and A.15.1 independently admits the dated Work occurrence.

  F.6 `performedUnderAssignment(W, RA)` is added only when this capability account or its receiving use expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment, while actual `enactsMethod(W, M)` separately relates the Work to the exact Method.

Do not put the threshold into the local system-role-kind name.

