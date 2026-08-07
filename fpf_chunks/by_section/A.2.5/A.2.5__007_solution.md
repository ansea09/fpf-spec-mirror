---
chunk_kind: "child"
pattern_id: "A.2.5"
pattern_title: "RoleStateRelation - Windowed Role-State Recognition and Work Admission"
section_id: "A.2.5:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.5/A.2.5__007_solution.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "A.2.5 — RoleStateRelation - Windowed Role-State Recognition and Work Admission"
  - "A.2.5:4 — Solution"
line_start: 4496
line_end: 4597
dependencies:
  - "A.15"
  - "A.2.1"
keywords:
  - "RSG"
  - "enactability"
  - "role state"
  - "role-state evolution"
  - "state machine"
---

### A.2.5:4 - Solution

Start from a readable assertion:

> `Robot-7`'s current `InspectorRole` assignment satisfies `InspectionReady` throughout the inspection window.

When a receiving use needs reusable participant typing, use the declared `RelationSignature`. When it needs occurrence identity, apply the world-side identity rule in section 4.3.

#### A.2.5:4.1 - Direct Relation Declaration

This pattern directly governs the `RelationSignature` for `RoleStateRelation`:

| SlotKind | ValueKind | refMode | Meaning |
|---|---|---|---|
| `RoleAssignmentSlot` | `U.RoleAssignment` | `U.EntityRef` | A reference resolving to the exact obtaining assignment occurrence whose holder-in-role state is current. |
| `StatePredicateSlot` | `RoleStatePredicate` | `ByValue` | The exact predicate interpreted through that assignment's role-taxonomy episteme and effective reference scheme. |

These are the only two generic participants. `RoleStateRelation` obtains exactly while the referenced assignment obtains and the by-value predicate is true under its declared temporal reading. Its actual extent is the maximal continuous interval of that obtaining. An affirmative assertion or occurrence description may state the known extent as `roleStateExtent` only for an independently established occurrence; a receiving evaluation may state a separate `declaredRoleStateEvaluationWindow`. Neither temporal value, assertion polarity, nor reliance posture is a relation participant or makes the relation obtain.

When a selected `BoundedModelUseStructure` changes interpretation, designate it in the receiving assertion or work use. It is not an optional participant of generic `RoleStateRelation`. A genuinely structure-dependent relation species requires its own direct pattern, required structure participant, stronger predicate, and occurrence-identity rule.

Evidence is not a participant that makes every role-state relation obtain. A relied-on assertion about the relation uses a direct evidence-use relation. Another world-side occurrence affects predicate truth only when the exact truth condition cites that occurrence under its direct governing pattern.

#### A.2.5:4.2 - Predicate Meaning and Role-Taxonomy Locality

A `RoleStatePredicate` states one exact truth condition for one exact `U.RoleAssignment` under its declared temporal reading. Its by-value content names:

- the role-state designator under the effective reference scheme;
- the exact truth-condition clauses, each naming its world-side object or relation and direct governing pattern;
- the temporal reading, such as truth at an instant, throughout a receiving-use window, or for a declared tolerated portion of that window.

This list defines one predicate value; it is not a union kind. The direct claims keep their own kinds and governing patterns.

The role-taxonomy episteme may state several predicates for one role. The direct consumer separately declares which predicate or conjunction its own admission rule uses. Predicates need not be mutually exclusive. `Calibrated`, `Synchronized`, and `InRange` can obtain simultaneously; `InspectionReady` may be a conjunction over them. Use an exclusive state configuration only when the subject-domain model actually needs one.

A shared label does not establish shared meaning. Reuse across role taxonomies needs either the same by-value predicate under a common effective scheme or an explicit comparison or bridge relation showing which truth and admission effects are preserved.

#### A.2.5:4.3 - Occurrence Identity and Repeated Episodes

Do not replace the identity rule with a tuple key. One `RoleStateRelation` occurrence begins when one fixed `U.RoleAssignment` starts satisfying one fixed `RoleStatePredicate` under that predicate's temporal reading. It continues while the assignment obtains and the predicate remains true without interruption. It ends when the assignment ceases, the predicate ceases to hold, or either participant changes. A later return to truth starts another occurrence.

An affirmative assertion or occurrence description may state the currently known `roleStateExtent` for an occurrence whose obtaining A.2.5 independently establishes. Recording an end boundary for a previously open extent refines the description of the same occurrence when assignment obtaining and predicate truth were uninterrupted. A demonstrated predicate gap separates occurrences. Two descriptions refer to the same occurrence only when they resolve to the same assignment, the same predicate value, and temporal information belonging to that one uninterrupted period.

A changed evidence relation, assertion edition, dashboard display, selected model-use structure in a receiving use, or publication does not create a new world-side occurrence while the same predicate continues to hold. A genuinely structure-dependent relation species can have another identity law only under its own direct pattern.

An evidence gap gives the receiving use unresolved reliance on the assertion. It does not demonstrate a gap in predicate obtaining or add a third assertion polarity. A direct observation or constituting occurrence may demonstrate such a gap only when its governing pattern supports that stronger world-side claim.

#### A.2.5:4.4 - Assertion and Evidence Use

For a relied-on role-state claim, keep this order:

1. name the exact `U.RoleAssignment`, by-value `RoleStatePredicate`, exact direct role-state claim family, and affirmative or negative assertion polarity;
2. when A.2.5 independently establishes that the relation obtains and a receiving use needs occurrence identity, individuate it under section 4.3; neither negative polarity nor unresolved reliance invents an occurrence;
3. state a `RoleStateAssertion : U.Episteme` whose ClaimGraph carries the predicate, exact direct claim-family reference, affirmative or negative `assertionPolarity`, the known `roleStateExtent` only for an affirmative claim about an independently established occurrence, and any separately current `declaredRoleStateEvaluationWindow`; leave compact first evidence-use or status-use classification to `A.2.4`, and keep supported, refuted, or unresolved reliance with `A.10` or the separately constituted receiving-evaluation result or reliance assertion;
4. if a selected model-use structure changes this interpretation, designate it in that assertion or receiving use rather than in the generic relation;
5. use `A.2.4` for compact evidence use, expanding through `A.10` only when fuller evidence-basis detail changes the relied-on use;
6. let the direct consumer use the supported assertion under its own governing pattern.

When role-state evaluation itself is current, name the exact evaluation work `W_eval : U.Work`, the admitted system that performed it, and the exact evaluator assignment through `F.6` `performedUnderAssignment(W_eval, RA_eval)`. Any separately constituted evaluation result is a `C.2.1` episteme whose ClaimGraph states the role-state judgment about the subject assignment or independently established occurrence. That work, its performer and assignment, the result episteme, its provenance under exact direct relations, and the receiving reliance evaluation remain neighboring governed objects; none becomes a `RoleStateRelation` participant or identity discriminator.

The actual role-state extent, target evaluation window, and evidence-relevance interval answer different questions. The first is derived from uninterrupted world-side obtaining. The second asks whether the predicate holds over a window selected by the receiving use. The third states when a particular episteme remains relevant enough to support the assertion. A calibration report can remain the same episteme while its relevance expires; that expiration lowers reliance without retroactively rewriting an earlier role-state occurrence.

For the declared use, supported, refuted, or unresolved reliance belongs to the separately constituted receiving-evaluation result or reliance assertion. This posture is neither a third assertion polarity nor a world-side role-state value and does not enter relation identity.

#### A.2.5:4.5 - Work-Admission Use

A.2.5 supplies the current state relation and the exact `RoleStateAssertion` form with affirmative or negative assertion polarity. `A.10` or the separately constituted receiving-evaluation result or reliance assertion owns any supported, refuted, or unresolved reliance posture for the declared use. A.2.5 does not itself select a method, create a gate decision, or assert that work occurred.

For a consequence-bearing admission use, the system performing the consumer's exact evaluation or decision work applies that consumer's direct governor and checks these conditions:

1. the exact `U.RoleAssignment` obtains throughout the receiving decision or work window;
2. the direct consumer declares one exact `RoleStatePredicate`; its truth condition may contain an explicit conjunction;
3. each relevant assignment has an obtaining `RoleStateRelation` whose actual extent covers the receiving-use window under the same effective reference scheme or an explicit bridge relation;
4. the assertion relied upon has the evidence relation and currentness needed by that consumer;
5. every other admission condition used by that consumer is separately established under its direct governing pattern.

The consumer's direct governor, not A.2.5, defines any admit, deny, defer, or unresolved outcome; exact system-performed decision work and its result remain separately governed. A.2.5 contributes no generic admission outcome; it contributes the exact state relation on which that decision work relies.

#### A.2.5:4.6 - Role-Relation Structure Use

When `A.2.7` selects role-substitution, incompatibility, or role-bundle relations, state sensitivity is expressed over exact assignments, predicates, and windows.

- Substitution is preserved only when the candidate role's current predicate entails the selected admission predicate under the declared scheme or bridge.
- Incompatibility is stated over the overlapping windows and predicate conditions in which the conflict actually appears.
- A work claim needing several roles uses the relevant role-state occurrences for each assignment. It does not require a Cartesian product of every possible state label.

If a role taxonomy declares a genuinely distinct composite `U.Role`, that role may have its own predicates and assignments. Mere conjunction for one work claim does not create a composite role value.

#### A.2.5:4.7 - State-Machine and Change Lenses

Use statecharts or state machines when mutually exclusive configurations, orthogonal regions, guarded changes, or event handling improve the subject-domain model. The notation describes possible configurations and changes; it does not replace the direct relation occurrence.

A change arrow represents a proposed or observed change in predicate truth; it is not the world-side change by form. Recover the exact changed object or relation, then use the direct pattern governing the exact claim that establishes the change. The statechart neither supplies a common world-side kind nor prescribes method order by itself.

When the model needs continuous coordinates rather than discrete labels, use `A.19` for the characteristic space and let the by-value state predicate select a region, band, ordering condition, or other exact condition over those coordinates. Measurement and evaluation stay with `C.16` and their direct patterns.

#### A.2.5:4.8 - Interpretation Qualification in the Receiving Use

Most role-state claims need no bounded-model-use structure. The assignment's role-taxonomy episteme and effective reference scheme already supply generic semantic locality.

When an independently selected `BoundedModelUseStructure` changes how a receiving assertion or work use interprets the state predicate, designate that structure in that assertion or use. Do not add an optional participant to generic `RoleStateRelation`. The structure organizes model-use relations; it does not hold the role, evaluate the predicate, make the relation obtain, or admit the work.

