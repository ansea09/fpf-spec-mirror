---
chunk_kind: "child"
pattern_id: "A.15.5"
pattern_title: "Work-Entry Readiness and Full-Kit Preparation"
section_id: "A.15.5:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.5/A.15.5__001_intro.md"
commit_sha: "00a27c2889bb2f7b8e0a7669075826e74d4dd270"
heading_path:
  - "A.15.5 — Work-Entry Readiness and Full-Kit Preparation"
  - "A.15.5:intro — Intro"
line_start: 30662
line_end: 30683
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.3"
  - "A.15.4"
  - "A.2.8.PER"
  - "A.20"
  - "A.21"
  - "A.3.4.P"
  - "B.1.6"
  - "B.3"
  - "C.32.P2S"
  - "E.10.MOVE"
  - "E.11.PUR"
  - "E.18"
  - "E.18.1"
  - "E.24"
keywords:
  - "WIP and flow policy"
  - "blocked readiness overread"
  - "commitment disposition"
  - "full-kit condition"
  - "launch gate"
  - "planned slot fillings"
  - "prospective permission inputs"
  - "readiness before work entry"
  - "resource-readiness refs"
  - "retrospective exercise evidence"
  - "work-entry readiness"
---

## A.15.5 - Work-Entry Readiness and Full-Kit Preparation

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** Judge whether an intended performance in a WorkPlan and PlanItem satisfies a local work-entry criterion at the stated time. Apply that criterion to the current inputs it requires. Identify a separate checking Work only when its dated occurrence is claimed. Keep the result and its grounds recoverable for the receiving use; readiness creates neither the intended Work nor its prerequisite facts.

**Use this when.** Use this pattern when a team is about to commit, release, launch, or admit intended work and needs to test its work-entry conditions against the available facts and preparations.

**Primary EntityOfConcern.** The C.2.1 readiness-result episteme has the `U.WorkPlan` being judged as its exact EntityOfConcern. Its ClaimGraph designates the relevant `PlanItem`, intended performance, criterion, evaluated facts, verdict, and applicability window. Preserve the plan's exact intended-work kind or work-family classification when that distinction is current; it remains ClaimGraph content and does not instantiate a dated `U.Work`. The plan names the target `U.Method`; cite a separately constituted `U.MethodDescription` episteme only when the readiness criterion or planned use relies on that exact description. The intended-performance designator, intended-work kind, plan item, method, and description are not a dated target `U.Work` occurrence.

**First output.** A readable result identifying the WorkPlan, PlanItem and intended performance; criterion and evaluation time; readiness value; consumed input propositions and their qualification intervals; reliance window; and stop or recheck condition. Add a checking-Work reference only when that occurrence matters. Inputs keep their own predicates and identities.

**Ordinary route.** Identify the plan content, criterion and evaluation time. Check the criterion against its current inputs and return `ready`, `readyWithKnownGaps`, `notReady` or `unknown`, with the reliance window and stop or recheck condition. Reuse applicable input results. Stop when this answers the receiving question; add a separate checking Work, result-episteme reference, gate, permission or assurance claim only when the use needs it.

When degraded support, handoff, or continuation-state evidence can change work entry, use the present-WorkPlan branch of `A.15.8` to test the proposed performer, support, and state configuration, then return here with its bounded result. Ordinary full-kit checking does not require `A.15.8`.

**What this buys.** A team can decide the next bounded move—start no work yet, prepare an exact missing input, recheck, or submit declared checks to a gate—under the criterion and the entry conditions actually required.

**Not this pattern when.** Use `A.15.2` for the work plan itself, `A.15.3` for planned slot fillers, `A.15.1` for dated performed work, `A.21` for gate decisions, `A.15.4` only when a reliance appearance is already being used as a reason for work or reliance before the subject pattern slot, relation, or project-side reference is named, `B.1.6` for resource aggregation after work, `E.18` for transformation-flow structure, and `E.18.1` for P2W carry-through from accepted problem-side material.

