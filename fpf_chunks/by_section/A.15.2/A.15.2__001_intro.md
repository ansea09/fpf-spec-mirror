---
chunk_kind: "child"
pattern_id: "A.15.2"
pattern_title: "U.WorkPlan"
section_id: "A.15.2:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.2/A.15.2__001_intro.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "A.15.2 — U.WorkPlan"
  - "A.15.2:intro — Intro"
line_start: 24711
line_end: 24741
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.3"
  - "A.15.4"
  - "A.15.5"
  - "A.2.1"
  - "A.2.2"
  - "A.20"
  - "A.21"
  - "A.3.1"
  - "A.3.2"
  - "A.6.1"
  - "A.6.5"
  - "A.6.RCD"
  - "A.6.REL"
  - "B.1.4"
  - "B.1.6"
  - "B.3"
  - "C.2.1"
  - "C.32.P2S"
  - "E.17"
  - "E.24"
  - "E.24.UK"
  - "F.9"
  - "U.Method"
  - "U.MethodDescription"
  - "U.RoleAssignment"
  - "U.Work"
keywords:
  - "PlanItem content"
  - "horizon"
  - "intended-work episteme"
  - "no actuality by plan"
  - "performer and capability conditions"
  - "positive or governed-negative local fulfilment assertion"
  - "possible future performance"
  - "present EntityOfConcern"
  - "reusable predicate semantics"
  - "variance"
---

## A.15.2 - U.WorkPlan

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** Use `U.WorkPlan` when one exact episteme carries substantive claims for coordinating possible future performed work over a horizon through `PlanItem` content: intended method, planned window, performer and role conditions, capability-fit requirements, resource budgets, dependencies, commitments, acceptance targets, and a baseline for later comparison. C.2.1 keeps the episteme identity through one already identified present EntityOfConcern. A designator for merely possible future performance remains claim content; it neither designates a dated Work occurrence admitted under `U.Work` nor becomes another entity merely because it is planned.

**Use this when.** Use this pattern when a schedule, calendar, rota, Kanban ticket, Gantt bar, shift plan, rollout plan, reservation, planning cue, or P2W preparation note may be an episteme about intended work but is being treated as a method, method description, performed work, evidence, approval, gate result, publication cue, query-plan representation, or database query-optimizer representation. A system may use `U.WorkPlan` to coordinate intended work only when the plan's substantive claims, present EntityOfConcern, effective reference scheme, and intended-performance designators are recoverable. The episteme itself neither acts nor makes work happen.

**First useful object.** One exact `U.WorkPlan` episteme with one present EntityOfConcern and at least one `PlanItem` content component. The content names the possible future performance or repeated-work subject being coordinated, horizon, target `U.Method`, an exact method-description use when current, planned window, intended performer and role conditions, A.2.2 capability-fit requirement, constraints, resource budgets, dependencies, commitments, acceptance targets, planned preparation tasks when current, baseline, and the later local fulfilment or variance question that a receiving use needs.

**First-use checks.**
1. Identify one present `U.Entity` that the plan claims concern, as C.2.1 requires. It may be an exact existing system, asset, promise-content edition, or other direct-owner entity for which work is being coordinated; when the claims are expressly reflexive, C.2.1 permits the same plan episteme as its own EntityOfConcern. Name possible future performances, a repeated-work family, or a proposed group separately as plan-content designators. If no one joint present EntityOfConcern can be identified, split the claim content or lower the cue rather than treating a future Work occurrence as already existing.
2. Recover target method, exact method-description use when current, horizon, planned window, intended performer and role conditions, A.2.2 capability-fit requirement, planned resources, dependencies, commitments, acceptance targets, baseline, and effective reference scheme. A desired participant, operation argument, or operation result enters as A.15.3 declaration-local planned-filling content only against one exact declaration member whose direct pattern owns the member's reusable participant, argument, or result meaning and corresponding later actual-use predicate; A.15.2/A.15.3 own the intended-use claim. If no reusable planned filling is needed, keep the choice as ordinary plan content; if typed reuse is needed but the exact member, corresponding predicate, or direct owner is absent, return the exact missing-governor blocker. An expected effect enters only as a plan claim under its exact direct pattern.
3. Decide whether the encountered source or cue supports a `U.WorkPlan`, a method description, a performed Work occurrence admitted under `U.Work`, A.15.3 planned-filling content, `WorkEntryReadiness@Context`, evidence, a gate claim, an `A.15.4` appearance-based reliance repair case, a publication-use cue, a forecast or dynamics model, or a declarative representation. A record, cue, diagram, or plan element remains a representation or source item until its exact governed claim is recovered.
4. Declare the `PlanItem` organization, governed base claims or constraint semantics, baseline policy, and the exact later local fulfilment or variance question before coordinating or comparing the plan. A readable one-case answer may stop at A.6.RCD disposition 2 as a local compound assertion. Repeated use of the same parameterized rule may justify disposition 3's reusable predicate-definition episteme without a relation kind. Open a relation-kind candidate only when a receiving use genuinely consumes occurrence semantics, and then require the A.6.RCD admission route, a standalone direct governor, obtaining and applicability laws, and a non-optional occurrence-identity rule; otherwise return `missing-governor` for that dependent use.
5. When work occurs, first identify the exact Work occurrence independently as an individual admitted under `U.Work` by A.15.1. A separate plan-use assertion may then compare exact plan content with independently obtaining relations involving that occurrence under a named policy; it does not rewrite the plan, create an actual-use fact, or turn the local assertion into a universal relation kind.

**Ordinary use.** For simple coordination, one `PlanItem` content component inside one exact `U.WorkPlan`, with intended method, planned window, intended performer or role condition, resource budget, dependency, commitment or acceptance target, and baseline, is enough.

**Reliance-bearing use.** Use fuller WorkPlan claim content when cross-role coordination, budget reservation, delivery commitment, gate preparation, audit expectation, cross-context acceptance, release preparation, evidence-reference notes, source-currentness requests, or P2W carry-through depends on the plan.

**Stop condition.** Stop once a system can coordinate the intended work at the needed granularity or the encountered source or cue is assigned to method, method description, performed work, evidence, gate, publication use, representation, forecast or dynamics, or `A.15.4` appearance-based reliance repair without claiming to be a plan. Stop only the dependent typed-relation use when its direct governor is absent; the plan and any truthfully expressible local claim remain usable.

**What goes wrong if missed.** Teams treat calendars, tickets, reservations, or rollout notes as if work already happened; identify a possible future performance as an existing Work occurrence; let the plan episteme act; or treat a plan as method, evidence, gate result, approval, or publication authority.

**What this buys.** One identifiable intended-work episteme whose present subject, horizon, windows, intended performer and role conditions, capability-fit requirements, constraints, budgets, dependencies, commitments, acceptance targets, baseline, and later comparisons with independently identified Work occurrences remain inspectable.

**Not this pattern when.** Not this pattern when the current claim is a dated performed work occurrence (`A.15.1`), A.15.3 declaration-local planned-filling content, work-entry readiness or full-kit condition (`A.15.5`), a reliance appearance being used before the governing pattern or relation is recovered (`A.15.4`), a method (`A.3.1`), a method description (`A.3.2`), evidence or assurance (`A.10` or `B.3`), a gate or constraint decision (`A.20` or `A.21`), publication-use behavior (`E.17`), a non-agentive forecast or dynamics model (`A.3.3`), or a declarative representation overread as a work-control or method claim (`C.2.P.DR`).

