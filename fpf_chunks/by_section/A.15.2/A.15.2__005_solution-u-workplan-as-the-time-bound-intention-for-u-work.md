---
chunk_kind: "child"
pattern_id: "A.15.2"
pattern_title: "U.WorkPlan"
section_id: "A.15.2:4"
section_title: "Solution - U.WorkPlan as the time-bound intention for U.Work"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.2/A.15.2__005_solution-u-workplan-as-the-time-bound-intention-for-u-work.md"
commit_sha: "59c455329e49715c64dc1b16f22c1efba6a3cf6f"
heading_path:
  - "A.15.2 — U.WorkPlan"
  - "A.15.2:4 — Solution - U.WorkPlan as the time-bound intention for U.Work"
line_start: 25621
line_end: 25717
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
  - "U.SystemRoleAssignment"
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

A.15.2 recognizes that same P as `U.WorkPlan` when its ClaimGraph substantively declares coordination of possible future performed work over one exact horizon through at least one `PlanItem` and, when it contains several items, their plan-content organization. The intended-performance designator may denote one proposed future performance, a named repeated-work family, or one bounded proposed group. It remains claim content: planning it neither asserts the existence of a dated Work occurrence nor makes a merely possible performance into C.2.1's already identified EntityOfConcern.

The present EntityOfConcern is the already identified existing entity that the plan's claims are about: for example, a system, asset, or promise-content episteme for which work is being coordinated. When the plan claims are expressly about their own coordination commitments, C.2.1's reflexive option permits P itself. When the claims concern several entities jointly, C.2.1 still requires one independently identified joint EntityOfConcern; otherwise split the claim content rather than filling the position with a list of unrelated or merely possible referents.

The stable positive membership condition is substantive intended-work content. At least one `PlanItem` must name its intended-performance designator, intended method or method family, planned window or entry condition, intended performer System or local system-role-kind condition, and enough constraints, resources, dependencies, commitments, targets, or baseline to make one coordination decision—for example, reserve a machine, order two items, staff a window, or set the target to be checked later. A calendar picture, ticket title, publication, approval cue, method description, forecast, or list of dates that supplies no such intended-work claims does not gain `U.WorkPlan` membership by format.

The dependent kind supplies no second identity rule. Changing exact ClaimGraph content, the present EntityOfConcern, or the effective `U.ReferenceScheme` identifies another episteme under C.2.1. An explicit `EpistemeEditionRelation` may preserve historical continuity only when its own predicate obtains. Changing only a file path, carrier, layout, publication occurrence, ticket key, or version label leaves identity unchanged when the three C.2.1 discriminators are preserved.

Planned Methods, possible-performance designators, intended performer Systems, local system-role-kind conditions, windows, desired fillings, capability-fit requirements, resource budgets, dependencies, commitments, acceptance targets, and expected effects are claim content or separately governed planned claims. They establish no dated Work occurrence, obtaining `U.SystemRoleAssignment`, capability-fit result, actual participant, resource use, Transformation, result value, result episteme, produced entity, delivery, acceptance verdict, or downstream outcome.

> **Strict distinction (memory aid):**
> **Method** = *how in principle*. **MethodDescription** = *how it is written*.
> **WorkPlan** = *when, by whom in intent, under which constraints*.
> **Work** = *how it went this time*.

#### A.15.2:4.2 - `PlanItem` content

A `PlanItem` is a declaration-local content component in one exact `U.WorkPlan`, not a U-kind, future or performed work occurrence, method part, assignment, relation occurrence, or result record. Its designator is interpreted inside that exact plan episteme. A receiving episteme may refer to the content component, but the designator or reference does not make its intended claims actual.

Choose only the claims the team will use to coordinate the intended work. The list is an open recognition palette, not a record schema or a kind defined by enumeration. When one row mentions a neighboring relation, state its own participants and predicate rather than treating the row or reference as proof that it obtains:

1. **Target method and description use** — the `U.Method` intended for enactment and, only when one plan claim relies on a particular `U.MethodDescription` episteme, that episteme and the relying instruction, constraint, or justification claim. Call the description an edition only when the C.2.1 `EpistemeEditionRelation` predicate obtains. The description neither identifies the method, constrains or justifies it by itself, nor becomes the enacted object.
2. **Planned window or entry condition** — earliest start, latest finish, timebox, recurrence, blackout period, or another exact intended temporal condition.
3. **Intended performer and system-role-kind conditions** — an intended performer `U.System` designator, the local system-role kind under which that performer is expected to qualify, its admission conditions, and, only when it already obtains, an assignment occurrence whose species is declared under `U.SystemRoleAssignment` and that is expected to cover later Work. A proposed holder-and-kind pair is not an actual assignment.
4. **Capability requirement** — an exact A.2.2 threshold or `CapabilityFitCondition` needed for work admission. Cite an existing capability claim only when the plan relies on it. The plan neither creates `U.Capability` nor evaluates fit for the later work interval.
5. **Resource budgets and reservations** — intended energy, materials, machine windows, money, and exact reservation claims. A planned budget is neither a performed resource-use fact nor a B.1.6 aggregate ledger result.
6. **Dependencies and commitments** — state the source item or commitment, the affected target item, and the condition that blocks, orders, overlaps, or excludes the planned work. A cited gate, approval, source-currentness, or promise claim keeps its own predicate; the citation establishes neither gate passage, approval, promise fulfilment, nor world-side ordering.
7. **Acceptance targets** — name the criterion and target value or window that a later evaluation will test. The target is not the evaluation or acceptance verdict.
8. **Location, affected-subject, and asset constraints** — where a proposed performance is intended to occur and which existing referent it is intended to concern, without asserting actual participation or change.
9. **Desired planned bindings** — use A.15.3 only when the plan intentionally fills one exact participant, argument, or result member already declared by A.6.5, A.6.1, or another pattern that states both the member meaning and its later actual-use predicate. A.15.2/A.15.3 state the intended choice; the declaration states what later counts as actual use. Without that member, keep an ordinary plan choice when typed reuse is unnecessary, or return `missing-governor` when it is necessary.
10. **Expected effect, result, or delivery target** — write the planned sentence with its intended subject and target: for example, the machine state sought, measurement window to be met, entity to be produced, or publication or delivery to be completed. Use the pattern that defines that effect. The broad words `output`, `result`, `outcome`, `deliverable`, or `handoff` do not name one plan field or universal kind.

A method description may describe generic participant meanings and intended effects, but it supplies no planned filling by itself. A desired filling remains planned; an expected result or effect remains expected. Neither establishes a dated Work occurrence admitted under `U.Work`, actual participant, operation application, actual change, returned value, result episteme, produced entity, acceptance verdict, delivery occurrence, or downstream outcome.

> **Didactic guardrail:** No log, telemetry value, performed-work fact, actual participant, or actual result belongs in WorkPlan identity-bearing claims merely because the plan later receives a comparison. Step logic and solver internals remain with the exact Method, MethodDescription, Mechanism, or representation pattern.

#### A.15.2:4.3 - Clear distinctions for schedule, process, and workflow wording

| If you say…                                 | In FPF it is…                                        | Why                                               |
| ------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------- |
| "The **schedule** for tomorrow's surgeries" | **`U.WorkPlan`** | Episteme declaring intended cases, windows, intended performer Systems and local system-role-kind conditions, resources, dependencies, and targets without asserting occurrence. |
| "The **workflow** for appendectomy"         | **`U.MethodDescription`** and `U.Method`             | Recipe and semantic way, not a calendar.          |
| "The **process** already ran at 10:00" | A Work occurrence admitted under `U.Work` only when A.15.1 grounds that dated individual | Identify its performer System, obtaining assignment, enacted Method, temporal extent, and containing System. Add participation, resource use, change, result, acceptance, or outcome only when that separate claim is actually being made. |
| "The **thermodynamic trajectory**" | **`U.Dynamics`** representation or model; add exact changed-subject and `U.Transformation` claims only when their direct predicates obtain | A trajectory expression is neither plan nor performed work by form. |
| "The **plan** assigns Dr. Lee" | **`U.WorkPlan`** carrying a claim about the System intended to perform the Work and its local system-role-kind condition; cite an assignment occurrence and its declared species only when that assignment already exists | The plan does not create or validate an assignment for the performed Work interval. |
| "The **budget** for Shift-B" | **`U.WorkPlan`** planned resource-budget claim | The plan states the budget. A.15.1 identifies later Work, the applicable resource-use predicate states what it consumed, and B.1.6 aggregates those facts only when a ledger or allocation result is needed. |

> **Schedule-word guard.** Schedule-like words do not determine the kind by themselves. Use `U.WorkPlan` only when the text actually states intended Work, a horizon or window, the System intended to perform the Work or its local system-role-kind conditions, and enough constraints, resources, dependencies, targets, or baseline to coordinate it. Otherwise use the pattern for the Method, instructions, dated Work, evidence, gate, publication use, or representation actually claimed.

#### A.15.2:4.4 - Plan mereology (composition of plans ≠ composition of methods or work occurrences)

Keep three separations crystal-clear:

* **Method composition** admits a composite `U.Method` only when A.3.1/B.1.5 supplies the submethods, whole-forming relations, and whole-level commitments.
* **Work organization** starts with exact A.15.1 work-part relations. Temporal overlap is an independently governed interval fact under B.1.4, and coordination is a separate direct claim when it obtains. Shared parentage or overlap creates neither a `ConcurrentPartOf_work` primitive nor coordination.
* **Plan-content organization** arranges declaration-local `PlanItem` components inside the exact ClaimGraph for coordination. It is epistemic organization, not world-side work or method mereology.

Common plan-content claim families include:

* **precedence or dependency constraints** naming exact source and target item designators, start or finish conditions, and any prerequisite or gate condition;
* **overlap or exclusivity constraints** naming the exact scheduling policy and the windows it permits or excludes;
* **refinement claims** stating which intended-performance designator is preserved and exactly which window, constraint, target, or budget is tightened; and
* **alternative claims** stating the alternatives and the independently governed condition used to choose among them.

Start with the readable plan constraint—for example, “item B starts only after clearance claim C for item A is current.” Keep that claim inside the WorkPlan ClaimGraph and name the two item designators, the condition, scope, and qualification. A graph edge, row order, or repeated spelling creates no world-side ordering, assignment, resource use, work parthood, or relation kind. If several plans reuse the same parameterized rule, A.6.RCD may supply a predicate-definition episteme. Open relation-kind admission only when a named receiver must distinguish occurrences of that relation; then E.24/E.24.UK and the standalone direct pattern must supply obtaining and identity before A.6.REL is used. If the rule, its source predicates, or occurrence identity cannot be stated, return the corresponding A.6.RCD blocker rather than minting `Precedes_pl`, `MutuallyExclusive_pl`, `Refines_pl`, or another pseudo-kind here.

**Didactic rule:** A `PlanItem` does not force an identical work shape. A later one-case comparison with an independently identified Work occurrence remains a separate local plan-use assertion unless an admitted direct relation has actually been supplied.

#### A.15.2:4.5 - How `WorkPlan` meets `Work`

Ask one concrete question first: “Did Work W satisfy plan item I under policy F?” Identify W under A.15.1, then name exact WorkPlan episteme P, declaration-local item I, and policy episteme F. Check only the independently obtaining facts that F requires—for example, enacted Method, required assignments, and Work extent in the hospital case below. Put the answer in a separate C.2.1 assertion whose EntityOfConcern is P. The assertion neither changes P nor admits a `WorkPlanFulfilmentRelation` kind.

A positive answer requires every fact in F's positive criterion. State a negative answer only when F contains an applicable failure or closure criterion and the case facts satisfy it. Missing occurrence facts return `missing-information`; an absent predicate or policy authority returns `missing-governor`. Neither stop is a negative claim. The assertion keeps W, P, I, F, polarity, and the supporting facts explicit; a matching label, window, ticket, record link, or policy name closes nothing. Several Work occurrences may satisfy different parts of I, or one consolidated Work may satisfy several items, only when F states that mapping. Unplanned Work remains valid Work; a separate assertion may classify it as unplanned for one named variance or improvement use.

If a receiving practice repeatedly needs the same parameterized fulfilment rule but consumes no relation-occurrence identity, use A.6.RCD disposition 3 to publish one predicate-definition episteme with one truthful exact EntityOfConcern, participant meanings, derivation, applicability, polarity, dependencies, and currentness; it is not a `RelationSignature` or relation kind. Only when a named receiver also needs distinguishable fulfilment occurrences may A.6.RCD return a relation-kind candidate for E.24/E.24.UK admission, a standalone direct subject settlement, and later A.6.REL discipline. Until those requirements are met, return the exact blocker only for the stronger use; do not infer partlessness, deny the local assertion or reusable predicate semantics, or add a universal `fulfils` edge.

A variance question is handled in the same economy. Use a separate local comparison assertion unless the measurement, evaluation, acceptance, resource, or temporal pattern already states the exact comparison. Name one planned value in exact P and I, one independently established actual value, the comparison method, scale, qualification window, and result. Do not make variance an intrinsic field of a Work occurrence, enter it into P's identity-bearing claim content, or rewrite the plan. Common comparison questions include:

* **schedule variance:** actual Work extent against the planned window, using the exact temporal comparison and any B.1.4 aggregate needed by the receiving KPI;
* **resource or cost variance:** exact A.15.1 performed resource-use facts or a B.1.6 aggregate result against the planned budget;
* **method variance:** actual `enactsMethod` against the intended method, including an exact substitution claim when the comparison asserts substitution;
* **description-selection variance:** the method-description episteme cited by a named assertion about a Work occurrence or by a separately governed instruction-use claim, compared with the description reference planned earlier; call either object an edition only when the C.2.1 `EpistemeEditionRelation` predicate obtains, and do not treat that episteme as enacted;
* **acceptance-target variance:** a separately governed measurement, evaluation, or acceptance verdict against the planned target; and
* **assignment variance:** for every actual performer, compare the exact obtaining assignment occurrence used by F.6 with the corresponding intended performer and local system-role-kind conditions in the plan. Check the occurrence's directly declared species, actual holder System, assigned local system-role-kind value, every additional participant that the plan constrains, and the part of its covering interval constrained by the plan. Report a **species mismatch** when the actual occurrence instantiates a different assignment species; when the species matches, report an **occurrence-value mismatch** only for a holder, assigned-kind value, plan-relevant additional participant, or interval value that differs from the plan. Do not collapse either comparison into a label match.

> **Manager's view:** A plan that cannot support one exact later local fulfilment or variance question is only a calendar picture for that use, not yet a reliance-bearing WorkPlan.

