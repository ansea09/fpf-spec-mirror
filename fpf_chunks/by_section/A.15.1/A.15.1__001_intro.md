---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__001_intro.md"
commit_sha: "f0b498ddfdf562242984ff7ab7a2557b55af6690"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:intro — Intro"
line_start: 23723
line_end: 23756
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.15.5"
  - "A.15.PROD"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
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
  - "E.10.ARCH"
  - "E.17"
  - "F.6"
  - "U.Capability"
  - "U.Method"
  - "U.MethodDescription"
  - "U.ReferenceScheme"
  - "U.System"
  - "U.SystemRoleAssignment"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "actual performer U.System"
  - "admitted U.Work kind"
  - "containing System"
  - "covering U.SystemRoleAssignment"
  - "enacted Method"
  - "optional direct bindings and resource use"
  - "performedUnderAssignment"
  - "separate result or consequence"
  - "temporal extent"
  - "world-side dated occurrence"
---

## A.15.1 - U.Work

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** Use `U.Work` for one world-side dated occurrence: a System performed it, it enacted a Method, and it happened over a time span. A WorkPlan, MethodDescription, log, dashboard, assertion, or record is a different object and does not make the Work occur. Start with the ordinary sentence in the compact example below; open the technical relation path only when the receiving claim needs it.

**Use this when.** Use this pattern when a plan, method description, schedule, log, telemetry stream, dashboard, approval-looking cue, publication face, result statement, or evidence-provenance relation is being treated as if it were performed work. `U.Work` is the admitted kind; one Work individual is the world-side occurrence. A separate assertion or description episteme may designate that occurrence and its obtaining relations, while surrounding records may constrain, evidence, schedule, publish, or judge it; none becomes the occurrence by being published.

**First useful object and short-account rule.** Name one independently identified dated Work occurrence, the System that performed it, the Method it enacted, when it occurred, and one declared relation to a System whose stated boundary contains the complete occurrence. Name another enacted Method or containing-System relation only when the use needs it. Use F.6 to establish the covering assignment for each performer. In a short account, show an assignment identifier only when the receiving claim uses its identity; the assignment and attribution must still obtain. Add a direct Work-to-referent relation, binding, or resource-use relation only when the receiving claim needs that obtaining fact. If the next sentence reports a result, change, production, delivery, or judgment, use the matching §4.6 row; do not make it a Work field.

**First-use route.**

1. Name the candidate occurrence and the question that depends on it.
2. Ask whether the source shows performed Work or only a plan, Method, MethodDescription, record, display, or evidence item. If it shows only the neighboring object, use that object's pattern and stop here.
3. For performed Work, name the System that acted, at least one Method actually enacted, the interval, and one declared Work-to-System relation whose stated boundary contains the complete occurrence. Use F.6 to establish the covering assignment and attribution for every performer. Add another enactment or containing-System relation only when the receiving use relies on it.

**Compact positive example.** `Robot-7 performed InspectionWork-17 under InspectionAssignment-17 from 09:00 to 09:20 within the declared service boundary of InspectionService-A; the Work enacted TurbineInspectionMethod.` This is enough for an ordinary Work assertion when the Work, System, Method, time, local Work-to-System relation, assignment, and F.6 attribution all independently obtain. Add bindings, resources, results, or changed referents only if the receiving claim uses their direct relations.

**Nearest non-use example.** A dashboard says *inspection complete* but exposes only a schedule row and a copied log. Keep the schedule as WorkPlan content and the log as possible evidence. Until the performed occurrence and its basis can be recovered, do not call either one Work.

The technical sections below give the full relation declarations, work-part distinctions, self-directed case, exact result routes, aggregation interfaces, and blockers. Open only the part needed by the current claim.

**Reliance-bearing use.** Add only the exact neighboring claims on which cost, quality, audit, evidence, conformance, gate, release, measurement, model use, or aggregation currently depends; do not turn them into fields of the work occurrence.

**Stop condition.** Stop once the occurrence is either recoverable as one Work individual admitted under `U.Work` at the needed granularity or lowered to a neighboring relation that no longer claims performed work.

**What goes wrong if missed.** Teams count plans, method descriptions, approval-looking cues, dashboards, telemetry, or evidence records as if work already happened, then attach cost, responsibility, quality, or result claims to the wrong EntityOfConcern.

**What this buys.** One dated occurrence identity whose actual performer systems, covering assignments, enacted methods, temporal extent, and required containing-system relations remain inspectable, together with any actually obtaining work-to-referent, binding, and resource-use relations used by the claim. A practitioner can then report a result or consequence through the concrete §4.6 branch without turning it into Work identity.

**Not this pattern when.** Not this pattern when the current claim is only a method (`A.3.1`), only a method description (`A.3.2`), only a plan or schedule (`A.15.2`), only declaration-local `SlotFillingsPlanItem` content inside an A.15.3-governed WorkPlan, only work-entry readiness or full-kit preparation before work entry (`A.15.5`), only a visible cue that needs `A.15.4` appearance-based reliance repair before reliance, only evidence or assurance (`A.10` or `B.3`), only publication-use behavior (`E.17`), or only a declarative representation overread as a work-control or method claim (`C.2.P.DR` or the direct representation pattern).

