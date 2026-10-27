---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work: Dated Performed Work Occurrence"
section_id: "A.15.1:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__001_intro.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "A.15.1 — U.Work: Dated Performed Work Occurrence"
  - "A.15.1:intro — Intro"
line_start: 28970
line_end: 29008
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

**At a glance.** Identify a dated action, its performer Systems, the Methods they followed and the interval of performance. Apply the full §4.1 test to admit that occurrence as `U.Work`. Its results, resource use and other relations need their own grounds. Plans and logs are epistemes describing intended and reported work.

**Use this when.** Use this pattern to identify a dated performed occurrence and establish its admission basis. It also resolves cases where a representation—for example, a plan, log or result statement—has been mistaken for the occurrence or leaves that basis unclear. Use F.6 separately after admission when a precise claim about the assignment under which Work was performed is current.

**Primary reader.** Engineers, operators, process owners, modelers, auditors, and FPF authors who need to establish what happened as performed Work and which claims the available evidence supports.

**First useful object and short-account rule.** Name the candidate dated action and keep the evidence needed by §4.1 recoverable. A Work-only account may stop after admission. Add another enactment, containment, attribution or neighboring claim only when the receiving use needs it; §4.6 routes result, change, production, delivery and judgment claims.

Use the following route:

1. Recover the direct subject first. If the question is only about a Method, plan, capability, result, change, resource, evidence item, or publication, use that subject's pattern and stop.
2. Identify the candidate performer as an exact System under A.1 without using the candidate Work to prove systemhood.
3. For every precise Agent claim, recover the A.13 core in §4.0 under independently stated criteria. Observed behavior may supply evidence; assuming that the candidate is already Work may not supply the proof. Open the characteristic-profile branch only under its stated receiving-use condition.
4. Apply the full §4.1 test, including the occurrence's A.1:4.2 construction and its Work-specific factual premises. Follow its candidate-facts-to-claims explanation to admit `W : U.Work` and then assert its obtaining typed relations.
5. Only after admission, and only when precise assignment-bound attribution is current, use F.6 with the same obtaining A.13 assignment for each performer.
6. Add direct Work-to-referent, operation-binding, resource-use, result, change, production, delivery, evaluation, or acceptance claims only when their own predicates and case facts obtain.

**Compact positive example.** On 27 July 2026, Robot-7 performed the 09:00–09:20 inspection in InspectionService-A, following TurbineInspectionMethod under InspectionAssignment-17.

**Basis of this example.** Before inspection, `Robot-7` is independently admitted as a System. `InspectionControllerSystemRole` has a declared A.2 membership criterion for goal-directed, condition-sensitive regulation of the inspection action; evidence shows that Robot-7 satisfies it. `InspectionAssignment-17` is an obtaining direct assignment of that kind for the service scope, working situation, and window. The same candidate inspection occurrence satisfies the six common constructive components in A.1:4.2. Together with the established construction and performer bases, the exact 09:00–09:20 inspection history on 2026-07-27, `TurbineInspectionMethod`, and the declared containment within `InspectionService-A` satisfy the A.15.1 occurrence test, so first admit `InspectionWork-17 : U.Work`. Then separately use the direct case fact for the pair to establish F.6 `performedUnderAssignment(InspectionWork-17, InspectionAssignment-17)` and say: `Robot-7 performed InspectionWork-17 under InspectionAssignment-17`. A separate assurance use can evaluate obstacle response, policy choice, persistence or operational closure under its declared criteria. Cite A.13 characteristic-profile values only when that use actually consumes those characteristics; the core Work claim needs no profile here.

**Nearest non-use example.** A dashboard says *inspection complete* but exposes only a schedule row and a copied log. Keep the schedule as WorkPlan content and the log as possible evidence. Inspect the log for the particular facts it supports; leave Work admission unresolved until the A.13 performer basis and all occurrence premises can be recovered.

**Recognition check.** Can the team recover the full §4.1 basis for one dated occurrence? When precise assignment-bound attribution is needed, can it also establish the separate F.6 relation under the conditions stated there?

**Stop condition.** Stop the admission branch once the candidate is admitted under §4.1 as one `U.Work` at the needed granularity, or the account has been limited to the independently supported neighboring claim. Keep an unresolved admission distinct from a failed proposed admission basis. If precise assignment-bound attribution is current, resolve that separate F.6 claim; missing or rejected attribution alone leaves established Work intact. Recheck an admission premise only when the same finding questions it under §4.1. A missing optional profile blocks only the Grade, autonomy, profile, criterion-dependent or assurance claim that requires it.

**What changes in practice.** A team establishes one occurrence and its actual performer basis from the available evidence, then adds only the result, change, resource, or evidence relations that the current decision consumes.

**What this buys.** An inspectable identity for one dated Work occurrence, with its admission basis recoverable and its attribution and neighboring claims judged separately when needed.

**Not this pattern when.** Use the direct pattern when the current question concerns agency (`A.13`), a Method (`A.3.1`), MethodDescription (`A.3.2`), plan or schedule (`A.15.2`), readiness (`A.15.5`), appearance-based reliance (`A.15.4`), evidence or assurance (`A.10` or `B.3`), publication-use behavior (`E.17`, with `E.24.PUB` for publication identity), or a declarative representation (`C.2.P.DR`).

