---
chunk_kind: "child"
pattern_id: "A.15.5"
pattern_title: "Work-Entry Readiness and Full-Kit Preparation"
section_id: "A.15.5:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.5/A.15.5__001_intro.md"
commit_sha: "9d38fbfe4ce5b72d8fe05e839cbca0025a5b31cf"
heading_path:
  - "A.15.5 — Work-Entry Readiness and Full-Kit Preparation"
  - "A.15.5:intro — Intro"
line_start: 32110
line_end: 32131
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

**At a glance.** Work back from the promised result to what must be secured before work begins. This gives a team a criterion for admitting jobs in the intended range. To judge one proposed start, apply the criterion to that WorkPlan and PlanItem at the relevant time. Keep the grounds for the verdict available to the recipient. Identify a separate checking Work when its occurrence is claimed.

**Use this when.** A team needs a rule for admitting work or a verdict on a particular proposed start. It can design a rule for recurring work before any individual job has been planned.

**Primary EntityOfConcern.** The C.2.1 readiness-result episteme has the `U.WorkPlan` being judged as its exact EntityOfConcern. Its ClaimGraph designates the relevant `PlanItem`, intended performance, criterion, evaluated facts, verdict, and applicability window. Preserve the plan's exact intended-work kind or work-family classification when that distinction is current; it remains ClaimGraph content and does not instantiate a dated `U.Work`. The plan names the target `U.Method`; cite a separately constituted `U.MethodDescription` episteme only when the readiness criterion or planned use relies on that exact description. The intended-performance designator, intended-work kind, plan item, method, and description are not a dated target `U.Work` occurrence.

**What to return.** For a criterion, give the conditions on which entry depends and why they cover the promised work across the intended range (§4.2). For a readiness verdict, identify the WorkPlan, PlanItem, intended performance, criterion, evaluation time, readiness value, inputs and their validity intervals, reliance window and stop or recheck condition. Identify a checking Work when that occurrence matters.

**Ordinary route.** Work back from what the recipient is promised. If you are designing the entry rule, establish which combinations of demand it must cover, what must be secured at entry and what may be obtained later in time. The resulting rule can answer this commission. When judging a particular start, apply the agreed criterion to that plan item and its current inputs. Return `ready`, `readyWithKnownGaps`, `notReady` or `unknown` with its reliance window. Add a separate checking Work, gate, permission or assurance claim when the receiving use needs it.

When support loss, handoff or recovery can affect entry, use `A.15.8` to establish what the service requires under those conditions. In designing a criterion, carry the resulting conditions into the admission rule. For a verdict on a proposed start, use the present-WorkPlan branch to assess the intended configuration.

**What this buys.** A team can decide the next bounded move—start no work yet, prepare a missing input, recheck, or submit declared checks to a gate—under the criterion and the entry conditions required.

**Not this pattern when.** Use `A.15.2` for the work plan itself, `A.15.3` for planned slot fillers, `A.15.1` for dated performed work, `A.21` for gate decisions, `A.15.4` only when a reliance appearance is already being used as a reason for work or reliance before the subject pattern slot, relation, or project-side reference is named, `B.1.6` for resource aggregation after work, `E.18` for transformation-flow structure, and `E.18.1` for P2W carry-through from accepted problem-side material.

