---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work: Dated Performed Work Occurrence"
section_id: "A.15.1:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__001_intro.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "A.15.1 — U.Work: Dated Performed Work Occurrence"
  - "A.15.1:intro — Intro"
line_start: 28895
line_end: 28931
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

## A.15.1 - `U.Work`: Dated Performed Work Occurrence

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** Identify one dated performed occurrence from its actual history, each performer System's A.13 core, at least one Method actually followed, temporal extent and a locally declared containing-System relation. A.15.1 admits Work on that basis before any F.6 assignment-bound attribution. Add the A.13 characteristic profile only when its values are consumed by the local criterion or receiving claim. A plan or log is an episteme about Work, not the occurrence. Start with the compact example; use the precise account when the claim needs it.

**Use this when.** Use this pattern when a plan, MethodDescription, schedule, log, telemetry stream, dashboard, approval-looking cue, publication face, result statement, or evidence relation is being treated as if performed Work; or when the exact dated action, A.13-qualified performer basis, Method, interval, or containing-System relation needed for Work admission is missing. Use F.6 separately after admission when a precise claim about the assignment under which the Work was performed is current.

**Primary reader.** Engineers, operators, process owners, modelers, auditors, and FPF authors who need to say what actually happened without turning plans, descriptions, logs, outputs, measurements, or changes into Work.

**First useful object and short-account rule.** Name the dated candidate action, actual performer Systems and their §4.0 agency bases, Method followed, extent and the declared System boundary containing the complete occurrence. Keep their evidence recoverable. Admit `W : U.Work` after these facts pass §4.1. Only then, if precise assignment-bound attribution is needed, use F.6 with the same obtaining assignment and the case fact for that pair. A Work-only account may stop after admission. Add another enactment, containment, binding, resource-use, profile or assurance claim only when the receiving use needs it; §4.6 gives the direct route for a result, change, production, delivery or judgment.

Use the following route:

1. Recover the direct subject first. If the question is only about a Method, plan, capability, result, change, resource, evidence item, or publication, use that subject's pattern and stop.
2. Identify the candidate performer as an exact System under A.1 without using the candidate Work to prove systemhood.
3. For every precise Agent claim, recover the A.13 core in §4.0 under independently stated criteria. Observed behavior may supply evidence; assuming that the candidate is already Work may not supply the proof. Open the characteristic-profile branch only under its stated receiving-use condition.
4. Test the actual bounded candidate action, every actual performer's A.13 core, at least one Method actually followed, the interval, and one declared Work-to-System relation whose stated boundary contains the complete occurrence. On pass, admit `W : U.Work` and its A.15.1-owned relations.
5. Only after admission, and only when precise assignment-bound attribution is current, use F.6 with the same obtaining A.13 assignment for each performer.
6. Add direct Work-to-referent, operation-binding, resource-use, result, change, production, delivery, evaluation, or acceptance claims only when their own predicates and case facts obtain.

**Compact positive example.** Before inspection, `Robot-7` is independently admitted as a System. `InspectionControllerSystemRole` has a declared A.2 membership criterion for goal-directed, condition-sensitive regulation of the inspection action; evidence shows that Robot-7 satisfies it. `InspectionAssignment-17` is an obtaining direct assignment of that kind for the service scope, working situation, and window. The exact 09:00–09:20 inspection history on 2026-07-27, `TurbineInspectionMethod`, and the declared containment within `InspectionService-A` independently satisfy the A.15.1 occurrence test, so first admit `InspectionWork-17 : U.Work`. Then separately use the direct case fact for the pair to establish F.6 `performedUnderAssignment(InspectionWork-17, InspectionAssignment-17)` and say: `Robot-7 performed InspectionWork-17 under InspectionAssignment-17`. A separate assurance use can evaluate obstacle response, policy choice, persistence or operational closure under its declared criteria. Cite A.13 characteristic-profile values only when that use actually consumes those characteristics; the core Work claim needs no profile here.

**Nearest non-use example.** A dashboard says *inspection complete* but exposes only a schedule row and a copied log. Keep the schedule as WorkPlan content and the log as possible evidence. Until the A.13 performer basis and performed occurrence can be recovered, do not call either one Work.

**Recognition check.** First, can the team point to one exact dated action, every actual performer System with its A.13 core, at least one Method actually followed, the extent, and one exact containing-System relation? If not, do not admit `U.Work`. Second, if precise assignment-bound attribution is current, can it point from that already admitted Work to the same obtaining A.13 assignment through the direct F.6 case fact, holder equality, declared species, and coverage? If not, retain independently grounded Work and leave that attribution unresolved; use §4.1 if the finding also questions an admission premise.

**Stop condition.** Stop the admission branch once the candidate is either admitted as one `U.Work` individual at the needed granularity from the A.13-qualified performer, occurrence, Method, extent, and containing-System facts, or lowered to a truthful neighboring claim. If precise assignment-bound attribution is current, continue only until F.6 establishes or rejects the exact Work-assignment relation. Missing or rejected F.6 attribution alone does not revoke independently established Work membership. Recheck an admission premise only when the same finding questions that premise under §4.1. A missing optional profile blocks only the Grade, autonomy, profile, criterion-dependent, or assurance claim that requires it.

**What changes in practice.** A team no longer promotes a plan, log, output, state change, or assignment into Work. It identifies one occurrence and its actual performer basis first, then adds only the result, change, resource, or evidence relations that the current decision consumes.

**What this buys.** One independently admitted dated Work identity whose A.13-qualified actual performer Systems, enacted Methods, temporal extent, and required containing-System relations remain inspectable, plus a separately decidable F.6 relation whenever a receiving use needs exact assignment-bound attribution, together with only the direct neighboring relations and conditional profile or assurance claims used by the current decision.

**Not this pattern when.** Use the direct pattern when the current question concerns agency (`A.13`), a Method (`A.3.1`), MethodDescription (`A.3.2`), plan or schedule (`A.15.2`), readiness (`A.15.5`), appearance-based reliance (`A.15.4`), evidence or assurance (`A.10` or `B.3`), publication-use behavior (`E.17`, with `E.24.PUB` for publication identity), or a declarative representation (`C.2.P.DR`).

