---
chunk_kind: "child"
pattern_id: "A.15.2"
pattern_title: "U.WorkPlan"
section_id: "A.15.2:4"
section_title: "Solution - U.WorkPlan as the time-bound intention for U.Work"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.2/A.15.2__005_solution-u-workplan-as-the-time-bound-intention-for-u-work.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "A.15.2 — U.WorkPlan"
  - "A.15.2:4 — Solution - U.WorkPlan as the time-bound intention for U.Work"
line_start: 24771
line_end: 24867
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

### A.15.2:4 - Solution - `U.WorkPlan` as the time-bound intention for `U.Work`

#### A.15.2:4.1 - Definition, membership, and identity

`U.WorkPlan` is a same-individual dependent kind under `U.Episteme`. C.2.1 first identifies exact episteme P by:

```text
<exact ClaimGraph, one already identified present EntityOfConcern, effective U.ReferenceScheme>
```

A.15.2 recognizes that same P as `U.WorkPlan` when its ClaimGraph substantively declares coordination of possible future performed work over one exact horizon through at least one `PlanItem` and, when several items are current, their plan-content organization. The intended-performance designator may denote one proposed future performance, a named repeated-work family, or one bounded proposed group. It remains claim content: planning it neither asserts the existence of a dated Work occurrence nor makes a merely possible performance into C.2.1's already identified EntityOfConcern.

The present EntityOfConcern is the exact existing entity that the plan claims concern under its direct pattern. It may be an existing system, asset, promise-content edition, or another identified entity for which work is being coordinated. When the plan claims are expressly about their own coordination commitments, C.2.1's reflexive option permits P itself. When the claims concern several entities jointly, C.2.1 still requires one independently identified joint EntityOfConcern; otherwise split the claim content rather than filling the position with a list of unrelated or merely possible referents.

The stable positive membership condition is substantive intended-work content. At least one `PlanItem` must name its intended-performance designator and state the intended method or method family, planned window or entry condition, intended performer or role condition, and the constraints, resources, dependencies, commitments, acceptance targets, or baseline needed by the named receiving use. A calendar picture, ticket title, publication, approval cue, method description, forecast, or list of dates that supplies no such intended-work claims does not gain `U.WorkPlan` membership by format.

The dependent kind supplies no second identity rule. Changing exact ClaimGraph content, the present EntityOfConcern, or the effective `U.ReferenceScheme` identifies another episteme under C.2.1. An explicit `EpistemeEditionRelation` may preserve historical continuity only when its own predicate obtains. Changing only a file path, carrier, layout, publication occurrence, ticket key, or version label leaves identity unchanged when the three C.2.1 discriminators are preserved.

Planned methods, possible-performance designators, performer designations, role conditions, windows, desired fillings, capability-fit requirements, resource budgets, dependencies, commitments, acceptance targets, and expected effects are claim content or separately governed planned claims. They establish no dated work occurrence, obtaining `U.RoleAssignment`, capability-fit result, actual participant, resource use, transformation, result value, result episteme, produced entity, delivery, acceptance verdict, or downstream outcome.

> **Strict distinction (memory aid):**
> **Method** = *how in principle*. **MethodDescription** = *how it is written*.
> **WorkPlan** = *when, by whom in intent, under which constraints*.
> **Work** = *how it went this time*.

#### A.15.2:4.2 - `PlanItem` content

A `PlanItem` is a declaration-local content component in one exact `U.WorkPlan`, not a U-kind, future or performed work occurrence, method part, assignment, relation occurrence, or result record. Its designator is interpreted inside that exact plan edition. A receiving episteme may refer to the content component, but the designator or reference does not make its intended claims actual.

The following is an open recognition palette, not a closed record schema or an unnamed kind defined by enumeration. Include only the claim families needed by the receiving use, and keep every current neighboring relation under its direct governor:

1. **Target method and description use** — the `U.Method` intended for enactment and, when current, an exact `U.MethodDescription` edition used by one named planned instruction, reliance, constraint, or justification claim. The description neither identifies the method, constrains or justifies it by itself, nor becomes the enacted object.
2. **Planned window or entry condition** — earliest start, latest finish, timebox, recurrence, blackout period, or another exact intended temporal condition.
3. **Intended performer and role conditions** — intended holder designation, `U.Role` value, role-admission conditions, and, when already obtaining, an exact `U.RoleAssignment` intended to cover later work. A proposed holder-role tuple is not an obtaining assignment.
4. **Capability requirement** — an exact A.2.2 threshold or `CapabilityFitCondition` needed for work admission, plus any current capability reference. The plan neither creates `U.Capability` nor evaluates fit for the later work interval.
5. **Resource budgets and reservations** — intended energy, materials, machine windows, money, and exact reservation claims. A planned budget is neither a performed resource-use fact nor a B.1.6 aggregate ledger result.
6. **Dependencies and commitments** — exact precedence, overlap, exclusivity, gate, approval, source-currentness, promise, or other planned claims under their direct predicates and conditions. A reference states neither gate passage, approval, promise fulfilment, nor world-side ordering by itself.
7. **Acceptance targets** — an exact criterion, quality window, or SLA target to be evaluated later under its direct owner; the target is not an evaluation or acceptance verdict.
8. **Location, affected-subject, and asset constraints** — where a proposed performance is intended to occur and which existing referent it is intended to concern, without asserting actual participation or change.
9. **Desired planned bindings** — only A.15.3 declaration-local `SlotFillingsPlanItem` content against a current governed RelationSignature participant declaration, A.6.1 operation argument or result declaration, or another exact declaration member whose direct pattern owns the member's reusable meaning and corresponding later actual-use predicate. A.15.2/A.15.3 own the intended-use claim. Without that exact member and direct owner, keep the choice as ordinary plan content when no reusable planned filling is needed; otherwise return the exact missing-governor blocker.
10. **Expected effect, result, or delivery target** — an exact planned claim under the direct pattern for the intended changed subject, characteristic, evaluation value, entity, publication, delivery, or other effect. The broad words `output`, `result`, `outcome`, `deliverable`, or `handoff` do not name one plan field or one universal kind.

A method description may describe generic participant meanings and intended effects, but it supplies no planned filling by itself. A desired filling remains planned; an expected result or effect remains expected. Neither establishes a dated Work occurrence admitted under `U.Work`, actual participant, operation application, actual change, returned value, result episteme, produced entity, acceptance verdict, delivery occurrence, or downstream outcome.

> **Didactic guardrail:** No log, telemetry value, performed-work fact, actual participant, or actual result belongs in WorkPlan identity-bearing claims merely because the plan later receives a comparison. Step logic and solver internals remain with the exact Method, MethodDescription, Mechanism, or representation pattern.

#### A.15.2:4.3 - Clear distinctions for schedule, process, and workflow wording

| If you say…                                 | In FPF it is…                                        | Why                                               |
| ------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------- |
| "The **schedule** for tomorrow's surgeries" | **`U.WorkPlan`** | Episteme declaring intended cases, windows, performer and role constraints, resources, dependencies, and targets without asserting occurrence. |
| "The **workflow** for appendectomy"         | **`U.MethodDescription`** and `U.Method`             | Recipe and semantic way, not a calendar.          |
| "The **process** already ran at 10:00" | A Work occurrence admitted under `U.Work` only when A.15.1 grounds that dated individual | Exact performer-assignment, enacted-method, temporal, containing-system, participant, affected-referent, and resource-use relations must obtain independently as required by the receiving claim; change, result, acceptance, and outcome stay separately governed. |
| "The **thermodynamic trajectory**" | **`U.Dynamics`** representation or model; add exact changed-subject and `U.Transformation` claims only when their direct predicates obtain | A trajectory expression is neither plan nor performed work by form. |
| "The **plan** assigns Dr. Lee" | **`U.WorkPlan`** carrying an intended holder and role claim; optionally cite an already obtaining `U.RoleAssignment` | The plan does not create or validate an assignment for the performed-work interval. |
| "The **budget** for Shift-B" | **`U.WorkPlan`** planned resource-budget claim | Actual performed resource use is established through independently obtaining relations involving exact Work occurrences under A.15.1 and the direct resource-use owners; any aggregate ledger or allocation result stays with B.1.6. |

> **Schedule-word guard.** Schedule-like words do not determine the kind by themselves. Use `U.WorkPlan` only when intended work, horizon or window, role constraints, resource constraints, dependencies, acceptance target, and baseline are current; otherwise recover method, method description, work, evidence, gate, publication-use, or declarative-representation claims separately.

#### A.15.2:4.4 - Plan mereology (composition of plans ≠ composition of methods or work occurrences)

Keep three separations crystal-clear:

* **Method composition** admits a composite `U.Method` only when A.3.1/B.1.5 or another exact method owner supplies recovered submethods, whole-forming relations, and whole-level commitments.
* **Work organization** starts with exact A.15.1 work-part relations. Temporal overlap is an independently governed interval fact under B.1.4, and coordination is a separate direct claim when it obtains. Shared parentage or overlap creates neither a `ConcurrentPartOf_work` primitive nor coordination.
* **Plan-content organization** arranges declaration-local `PlanItem` components inside the exact ClaimGraph for coordination. It is epistemic organization, not world-side work or method mereology.

Common plan-content claim families include:

* **precedence or dependency constraints** naming exact source and target item designators, start or finish conditions, and any prerequisite or gate condition;
* **overlap or exclusivity constraints** naming the exact scheduling policy and the windows it permits or excludes;
* **refinement claims** stating which intended-performance designator is preserved and exactly which window, constraint, target, or budget is tightened; and
* **alternative claims** stating the alternatives and the independently governed condition used to choose among them.

These prose families and any local spellings do not admit reusable relation kinds. Each current claim stays inside the exact WorkPlan ClaimGraph and names its predicate, participants, governed base claims or fully stated constraint semantics, derivation when compound, condition, scope, and qualification. A graph edge, row order, or repeated spelling creates no world-side ordering, assignment, resource use, work parthood, or typed relation. If another use repeats the same parameterized semantics, A.6.RCD may first yield a reusable predicate-definition episteme without occurrence ontology. Only a receiving need for distinct relation occurrences opens a derived- or primitive-kind candidate, the E.24/E.24.UK admission route, a standalone direct pattern, and A.6.REL occurrence discipline after admission. Absent the needed substrate, definition owner, or occurrence settlement, return the exact blocker rather than minting `Precedes_pl`, `MutuallyExclusive_pl`, `Refines_pl`, or another pseudo-kind here.

**Didactic rule:** A `PlanItem` does not force an identical work shape. A later one-case comparison with an independently identified Work occurrence remains a separate local plan-use assertion unless an admitted direct relation has actually been supplied.

#### A.15.2:4.5 - How `WorkPlan` meets `Work`

First identify exact `W : U.Work` under A.15.1. For an ordinary one-case question, use A.6.RCD disposition 2: create or cite a separate C.2.1 assertion episteme whose EntityOfConcern is exact WorkPlan edition P and whose ClaimGraph says whether W's independently governed performer assignments, enacted method, temporal extent, affected referent, application or subject-relation bindings, and performed resource-use facts satisfy exact content component I under named policy edition F. A negative answer is assertable only when F supplies an applicable explicit negative or closure criterion and the exact case facts satisfy it. F states the governed base predicates, mapping or derivation, applicability, polarity, and boundary needed by this use. This is a local compound assertion about P; it neither adds actual facts to P nor admits a `WorkPlanFulfilmentRelation` kind.

The assertion makes exact W, exact P edition, declaration-local I designator, exact F, polarity, and the supporting independently obtaining relations involving W recoverable. Failure of an applicable explicit criterion can support a governed negative claim; absent or unavailable occurrence relations return `missing-information`, while absent predicate or policy authority returns `missing-governor`. Neither stop is the negative claim. A shared label, schedule window, ticket key, record link, or policy name alone establishes nothing. Several exact Work occurrences may satisfy different parts of I, and one consolidated Work occurrence may satisfy several items, only when the local assertion states the exact split or consolidation mapping under F. Exact unplanned Work remains a valid Work occurrence admitted under `U.Work`; a separate plan-use assertion may classify it as unplanned for one named variance or improvement use.

If a receiving practice repeatedly needs the same parameterized fulfilment rule but consumes no relation-occurrence identity, use A.6.RCD disposition 3 to publish one predicate-definition episteme with one truthful exact EntityOfConcern, participant meanings, derivation, applicability, polarity, dependencies, and currentness; it is not a `RelationSignature` or relation kind. Only when a named receiver also needs distinguishable fulfilment occurrences may A.6.RCD return a relation-kind candidate for E.24/E.24.UK admission, a standalone direct subject settlement, and later A.6.REL discipline. Until those requirements are met, return the exact blocker only for the stronger use; do not infer partlessness, deny the local assertion or reusable predicate semantics, or add a universal `fulfils` edge.

A variance question is handled in the same economy. Use a separate local comparison assertion, or the exact measurement, evaluation, acceptance, resource, temporal, or other direct relation already governing the compared values. Name one planned value in exact P and I, one independently governed actual value, the comparison method, scale, qualification window, and exact result. Do not make variance an intrinsic field of a Work occurrence, enter it into P's identity-bearing claim content, or rewrite the plan. Common comparison questions include:

* **schedule variance:** actual Work extent against the planned window, using the exact temporal comparison and any B.1.4 aggregate needed by the receiving KPI;
* **resource or cost variance:** exact A.15.1 performed resource-use facts or a B.1.6 aggregate result against the planned budget;
* **method variance:** actual `enactsMethod` against the intended method, including an exact substitution claim when current;
* **description-selection variance:** the exact method-description edition cited by a named assertion about a Work occurrence or by a separately governed instruction-use claim, compared with the planned description reference, without treating that episteme as enacted;
* **acceptance-target variance:** a separately governed measurement, evaluation, or acceptance verdict against the planned target; and
* **assignment variance:** every exact performed-work `U.RoleAssignment` against the intended holder and role claims.

> **Manager's view:** A plan that cannot support one exact later local fulfilment or variance question is only a calendar picture for that use, not yet a reliance-bearing WorkPlan.

