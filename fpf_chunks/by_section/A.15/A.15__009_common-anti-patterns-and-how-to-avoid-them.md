---
chunk_kind: "child"
pattern_id: "A.15"
pattern_title: "Role–Method–Work Alignment"
section_id: "A.15:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15/A.15__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "66e732dfef7a4a93ff23eec43b3f759a6664652d"
heading_path:
  - "A.15 — Role–Method–Work Alignment"
  - "A.15:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 24205
line_end: 24216
dependencies:
  - "A.10"
  - "A.12"
  - "A.15"
  - "A.15.1-A.15.5"
  - "A.15.4"
  - "A.15.5"
  - "A.2"
  - "A.20"
  - "A.21"
  - "A.4"
  - "A.6"
  - "A.6.B"
  - "A.6.C"
  - "B.3"
  - "C.24"
  - "C.26.2"
  - "C.28"
  - "C.29"
  - "C.32.P2S"
  - "E.10"
  - "E.10.ARCH"
  - "E.16"
  - "E.17"
  - "E.17.EFP"
  - "E.18.1"
keywords:
  - "U.Method"
  - "U.MethodDescription"
  - "U.Role"
  - "U.WorkPlan"
  - "actual U.Work"
  - "appearance-based reliance boundary"
  - "contextual enactment"
  - "coordinated-work evidence"
  - "role-method-work distinction"
  - "work admission display"
  - "work-entry readiness"
---

### A.15:8 - Common Anti-Patterns and How to Avoid Them

- **Role-as-part.** Do not place `U.Role`, `U.Capability`, capability-support records or relations, or capability-fit predicates inside structural `partOf` decomposition; keep role interpretation under its role taxonomy and effective scheme, capability as the `A.2.2` admitted capability instance, support records or relations under their own governing patterns, and fit predicates as admission checks.
- **Recipe-as-evidence.** A `U.MethodDescription` or SOP may identify or constrain a method; a separate assertion or performed-work record may designate a dated Work occurrence, but the record is not the occurrence and cannot substitute for its world-side basis.
- **Plan-as-performed-work.** Do not let schedules, calendars, or intended assignments stand in for performed execution; use `U.WorkPlan` for intent, identify the actual Work occurrence independently under `U.Work`, and state its performed values through obtaining relations.
- **Capability-as-work.** Do not treat possession of a capability instance, a statement about it, or a passing fit predicate as if the task has already been performed; capability enables execution under conditions but is not execution.
- **Approval collapse.** Keep approval or authorization speech acts distinct from the operational steps they permit. When an approval is itself performed work, identify one separate Work individual admitted under `U.Work` and recover the exact speech-act or instituted-effect relation independently; the approval occurrence is not the later operational occurrence.
- **Process soup.** Do not leave "process", "workflow", or "activity" uninterpreted in FPF-governed passages; resolve the wording cue to `U.Method`, `U.MethodDescription`, `U.WorkPlan`, the `U.Work` kind, or one Work individual admitted under it.
- **Briefing-as-execution-cue.** A lighter review note, rollout summary, or redacted operations note may orient work; use `A.15.4` appearance-based reliance repair or the direct governing pattern for that reliance before relying on it for execution, approval, gate, evidence, or plan claims.
- **P2W publication as work occurrence.** A principle scheme, functional diagram, scenario, screen, or explanation may guide selected method or work-planning uses named by value; recover the project-side FPF kind and reference named by value for any selected-method, work-plan, work-occurrence, result, evidence, gate, or engineering-justification claim, and keep the `E.18.1` carry-through structure separate from those typed values.
- **Reliance appearance as work-relevance cue.** A dashboard tile, credential display, copied approval, generated explanation, provenance label, command-like cue, or composed source-relation chain is only a reliance appearance until `A.15.4` recovers the project-side kind and reference named by value required for the work or reliance claim under repair.

