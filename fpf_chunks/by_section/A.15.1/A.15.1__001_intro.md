---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__001_intro.md"
commit_sha: "353d59d1c2167344cfff99cadbf413c587c14a66"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:intro — Intro"
line_start: 24951
line_end: 24987
dependencies:
  - "A.1"
  - "A.10"
  - "A.13"
  - "A.15"
  - "A.15.4"
  - "A.15.5"
  - "A.15.PROD"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.1"
  - "B.1.4"
  - "B.1.6"
  - "B.3"
  - "C.2.1"
  - "C.27.TA"
  - "C.32.P2S"
  - "E.10"
  - "E.10.ROLE"
  - "E.17"
  - "F.6"
  - "U.Method"
  - "U.MethodDescription"
  - "U.ReferenceScheme"
  - "U.WorkPlan"
keywords:
  - "A.13-qualified actual performer U.System"
  - "F.6 only after admission for precise assignment-bound attribution"
  - "conditional agency profile"
  - "containing System"
  - "enacted Method"
  - "exact performance history"
  - "independent U.Work admission"
  - "optional direct bindings and resource use"
  - "separate result or consequence"
  - "temporal extent"
  - "world-side dated occurrence"
---

## A.15.1 - U.Work

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** Use `U.Work` for one world-side dated occurrence only after each claimed performer is an admitted `U.System` with the current A.13 core basis for the exact action: one local agential system-role kind and its criterion, classification of that System under the kind, one obtaining assignment of that kind, and the scope, working situation, and window needed by the use. Evidence must support those core claims. Admit the occurrence in A.15.1 only when its performance history, at least one Method actually followed, temporal extent, and at least one obtaining locally declared containing-System relation are independently grounded. This membership closes before and does not depend on F.6 `performedUnderAssignment`; apply F.6 afterward only when the receiving use makes a precise assignment-bound performer attribution. Add an agency-characteristic profile only when the receiving claim consumes a Grade, autonomy or profile result, when the local criterion itself explicitly depends on such a characteristic, or when an assurance use requires it. A WorkPlan, MethodDescription, log, dashboard, assertion, or record is a different object and does not make the Work occur. Start with the ordinary sentence in the compact example below; open the technical relation path only when the receiving claim needs it.

**Use this when.** Use this pattern when a plan, MethodDescription, schedule, log, telemetry stream, dashboard, approval-looking cue, publication face, result statement, or evidence relation is being treated as if performed Work; or when the exact dated action, A.13-qualified performer basis, Method, interval, or containing-System relation needed for Work admission is missing. Use F.6 separately after admission when a precise claim about the assignment under which the Work was performed is current.

**Primary reader.** Engineers, operators, process owners, modelers, auditors, and FPF authors who need to say what actually happened without turning plans, descriptions, logs, outputs, measurements, or changes into Work.

**First useful object and short-account rule.** Name one independently identified dated candidate action, each actual performer System and its A.13 local agential kind, criterion, classification, obtaining assignment, scope, working situation, and window, the Method actually followed, when the action occurred, and one declared relation to a System whose stated boundary contains the complete occurrence. Keep evidence for those facts recoverable; add a characteristic profile only under the conditional branch above. When those facts pass A.15.1, admit the occurrence as `W : U.Work`. Only afterward, if precise assignment-bound attribution is current, let F.6 test `performedUnderAssignment(W, RA)` using the same obtaining A.13 assignment and the direct case fact for the exact pair. A Work-only account may stop after admission; a short attribution account may omit an unused identifier only when every required link remains recoverable. Add another enacted Method, containing-System relation, direct Work-to-referent relation, binding, resource-use relation, profile, or assurance result only when the receiving claim needs it. If the next sentence reports a result, change, production, delivery, or judgment, use the matching section 4.6 row; do not make it a Work field.

Use the following route:

1. Recover the direct subject first. If the question is only about a Method, plan, capability, result, change, resource, evidence item, or publication, use that subject's pattern and stop.
2. Identify the candidate performer as an exact System under A.1 without using the candidate Work to prove systemhood.
3. For every precise Agent claim, recover the A.13 core basis in section 4.0 before using actual performance as evidence; open the characteristic-profile branch only under its stated receiving-use condition.
4. Test the actual bounded candidate action, every actual performer's A.13 core, at least one Method actually followed, the interval, and one declared Work-to-System relation whose stated boundary contains the complete occurrence. On pass, admit `W : U.Work` and its A.15.1-owned relations.
5. Only after admission, and only when precise assignment-bound attribution is current, use F.6 with the same obtaining A.13 assignment for each performer.
6. Add direct Work-to-referent, operation-binding, resource-use, result, change, production, delivery, evaluation, or acceptance claims only when their own predicates and case facts obtain.

**Compact positive example.** Before inspection, `Robot-7` is independently admitted as a System. `InspectionControllerSystemRole` has a declared A.2 membership criterion for goal-directed, condition-sensitive regulation of the inspection action; evidence shows that Robot-7 satisfies it. `InspectionAssignment-17` is an obtaining direct assignment of that kind for the service scope, working situation, and window. The exact 09:00–09:20 inspection history, `TurbineInspectionMethod`, and the declared containment within `InspectionService-A` independently satisfy the A.15.1 occurrence test, so first admit `InspectionWork-17 : U.Work`. Then separately use the direct case fact for the pair to establish F.6 `performedUnderAssignment(InspectionWork-17, InspectionAssignment-17)` and say: `Robot-7 performed InspectionWork-17 under InspectionAssignment-17`. This example's assurance use also compares obstacle response, policy choice, persistence, and operational closure, so it cites the corresponding A.13 profile evidence; Work admission itself consumes no such profile unless its criterion or receiving use requires one.

**Nearest non-use example.** A dashboard says *inspection complete* but exposes only a schedule row and a copied log. Keep the schedule as WorkPlan content and the log as possible evidence. Until the A.13 performer basis and performed occurrence can be recovered, do not call either one Work.

**Recognition check.** First, can the team point to one exact dated action, every actual performer System with its A.13 core, at least one Method actually followed, the extent, and one exact containing-System relation? If not, do not admit `U.Work`. Second, if precise assignment-bound attribution is current, can it point from that already admitted Work to the same obtaining A.13 assignment through the direct F.6 case fact, holder equality, declared species, and coverage? If not, retain the Work and leave only that attribution unresolved.

**Stop condition.** Stop the admission branch once the candidate is either admitted as one `U.Work` individual at the needed granularity from the A.13-qualified performer, occurrence, Method, extent, and containing-System facts, or lowered to a truthful neighboring claim. If precise assignment-bound attribution is current, continue only until F.6 establishes or rejects the exact Work-assignment relation. Missing or rejected F.6 attribution never revokes independently established Work membership; it lowers only the assignment-bound attribution. A missing optional profile blocks only the Grade, autonomy, profile, criterion-dependent, or assurance claim that requires it.

**What changes in practice.** A team no longer promotes a plan, log, output, state change, or assignment into Work. It identifies one occurrence and its actual performer basis first, then adds only the result, change, resource, or evidence relations that the current decision consumes.

**What this buys.** One independently admitted dated Work identity whose A.13-qualified actual performer Systems, enacted Methods, temporal extent, and required containing-System relations remain inspectable, plus a separately decidable F.6 relation whenever a receiving use needs exact assignment-bound attribution, together with only the direct neighboring relations and conditional profile or assurance claims used by the current decision.

**Not this pattern when.** Not this pattern when the current question is whether agency obtains (`A.13`), only a Method (`A.3.1`), MethodDescription (`A.3.2`), plan or schedule (`A.15.2`), readiness (`A.15.5`), appearance-based reliance (`A.15.4`), evidence or assurance (`A.10` or `B.3`), publication-use behavior (`E.17`), or a declarative representation (`C.2.P.DR`).

