---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__005_solution.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:4 — Solution"
line_start: 25100
line_end: 25204
dependencies:
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.6.1"
  - "A.6.5"
  - "A.6.RCD"
  - "C.2.1"
  - "E.17"
  - "E.24.PUB"
  - "U.WorkPlan"
keywords:
  - "WorkPlan claim content"
  - "actual-use predicate"
  - "baseline replay"
  - "concrete RefKind and policy"
  - "direct owner"
  - "edition pin"
  - "exact declaration member"
  - "intended-performance designator"
  - "no actuality by plan"
  - "open-world omission"
  - "participant/argument/result meaning"
  - "positive planned designation"
  - "semantic cardinality"
---

### A.15.3:4 - Solution

#### A.15.3:4.0 - The governed object and ontic boundary

`SlotFillingsPlanItem` names a declaration-local `PlanItem` content form inside one exact `U.WorkPlan` ClaimGraph. It is not a U-kind, a dependent durable kind, a `U.Relation` occurrence, an ontic `SlotRelation`, an independent record, or a second slot ontology. Its item and row designators are interpreted only within that WorkPlan edition.

C.2.1 and A.15.2 keep the WorkPlan episteme identity. Changing an identity-bearing planned-filling row changes the WorkPlan ClaimGraph and lets C.2.1 identify the resulting episteme edition. A separate reference may resolve the WorkPlan and the designated content component, but the reference does not give the PlanItem an independent identity rule.

Here a **planned-filling claim** is WorkPlan claim content saying that, for one intended-performance designator and under exact planning conditions, a future use of one exact declaration member is intended to carry or designate one exact value or target-declared collection of values. A.15.2 and A.15.3 govern that positive intended-use claim. The declaration member's direct pattern separately owns its reusable participant, argument, or result meaning and the corresponding later actual-use predicate. Neither owner substitutes for the other.

The phrase **planned filling** does not mean that a declaration is filled, a relation obtains, an operation application occurs, or a value is actually bound. The row itself needs no relation kind or relation occurrence: A.15.3 is the direct pattern for this plan-content form. A later fulfilment, substitution, missing-filler, or variance claim remains a neighboring claim under A.15.2, A.6.RCD, or another exact comparison owner.

A planned-filling row is positive intention content. A prohibition, excluded value, required absence, or closed-world completeness claim needs its own exact constraint or negative-claim governor and cannot be encoded by omission, an empty filler, or a negated reference.

#### A.15.3:4.1 - Admit only exact governed declaration targets

Each planned-filling row targets exactly one member of one exact applicable declaration edition:

| Planned meaning | Exact target | Direct owner and boundary |
| --- | --- | --- |
| participant designation for a future direct-relation claim | one `SlotSpec` in one exact `RelationSignature` edition | the direct relation pattern owns the reusable participant meaning and obtaining predicate; A.6.5 owns the declaration-local `SlotKind`, `ValueKind`, and `refMode`; A.15.3 owns only the intended designation |
| argument value or designation for a future operation application | one `ArgumentDeclaration` in one exact A.6.1 `OperationDeclaration` | A.6.1 and the exact mechanism declaration own argument meaning, ValueKind, binding designation rule, binding predicate, and cardinality; A.15.3 owns only the intended value or designation |
| expected result value or designation for a future operation application | one `ResultDeclaration` in one exact A.6.1 `OperationDeclaration` | A.6.1 and the exact mechanism declaration own result meaning and the actual result-binding predicate; an expected value is not a returned value |
| another explicitly declared planned filling | one exact declaration member whose direct pattern owns its reusable participant, argument, result, or analogous member meaning and corresponding later actual-use predicate | cite that pattern and declaration by value; if either the reusable meaning or corresponding predicate lacks that owner, stop with the exact missing-governor blocker |

`U.MethodDescription` is not an admissible target merely because its claims describe generic inputs, effects, parameters, bounds, or acceptance conditions. A suite description, kit description, table, schema, card, checklist, interface form, or database field likewise exposes no A.6.5 SlotSpec unless one exact `RelationSignature` contains that SlotSpec. Operation arguments and results remain A.6.1 declaration content and never become A.6.5 SlotSpecs by being planned.

One `SlotFillingsPlanItem` may contain several rows when they serve the same intended-performance designator, baseline policy, and revision route inside one WorkPlan. Every row still resolves independently to its exact declaration member. Split the item when rows concern different intended performances, baseline policies, or revision routes. The WorkPlan's present EntityOfConcern remains a WorkPlan-level C.2.1 discriminator and is not replaced by the merely possible performance designator.

#### A.15.3:4.2 - State one planned-filling row

A conforming item makes these values recoverable:

```text
SlotFillingsPlanItem:
  planItemDesignator
  exactWorkPlanRef
  intendedPerformanceDesignator
  plannedFillingRows:
    - rowDesignator
      targetDeclarationRef
      targetMemberDesignator
      targetMemberFamily:
        RelationSignatureSlotSpec |
        OperationArgumentDeclaration |
        OperationResultDeclaration |
        OtherDirectlyGovernedDeclaration
      directOwnerPattern
      plannedValueOrDesignation
      planningConditions?
      declarationEditionPin?
      plannedValueEditionPin?
  baselinePolicyRef?
  laterComparisonPolicyRef?
```

The block is a representation of WorkPlan claim content, not an ontic record schema or a second row authority. `targetMemberFamily` is an open local dispatch vocabulary, not a public kind or a closed inventory. `directOwnerPattern` names by value the subject pattern that owns the target member's reusable meaning and corresponding actual-use predicate; it is not a generic reference kind. A.15.3 remains the owner of the planned intention.

The effective designation rule is resolved from the exact target member rather than copied into a competing plan-side declaration. For an A.6.5 target this is its `refMode`; for an A.6.1 target it is the `bindingDesignationRule`. A ByRef designation uses the concrete governed reference kind required there and resolves to a referent of the declared ValueKind; a generic `Ref`, `SpecRef`, stored token, or compatible value does not suffice.

The target member's semantic cardinality governs the planned choice. For a single-valued target, the exact baseline or selection policy must make at most one planned value or designation effective for any one intended use. Several alternatives require exact conditions and an exact resolution rule; layout supplies neither exclusivity nor priority. A multivalued member follows the target-declared set, sequence, multiset, repetition, and ordering semantics; row count or row order supplies none of them. If the target declaration and applicable policy do not settle the cardinality needed by the planned use, return the missing declaration or policy governor instead of inferring it from layout.

Omitting a possible row is not a negative claim that no such value, designation, or later participant exists. It means only that the current WorkPlan ClaimGraph does not rely on that filling. A prohibited or excluded value and any closed-world completeness claim remain separate governed plan claims with their own applicability and polarity basis.

`intendedPerformanceDesignator` is plan content, not a reference that makes a future Work occurrence or another future entity exist. The already identified present EntityOfConcern stays on the enclosing WorkPlan under C.2.1 and A.15.2.

Time, location, capability, readiness, gate, evidence, source-currentness, bridge, publication, or other conditions enter only through exact separately governed plan claims when the receiving use depends on them. This is an open recognition palette of neighboring claim families, not an unnamed kind or a generic field bundle. `planningConditions` cites those claims; it does not create them.

Any baseline or later-comparison policy reference states its concrete governed kind, direct owner, effective edition, applicability, and reference scheme when relied upon. A generic `PolicyRef` or shared label supplies no policy semantics. Pin a declaration edition or edition-bearing planned value only when another resolution could change the meaning relied on by the receiving use; the exact target reference and any explicit pin must agree.

#### A.15.3:4.3 - Read relation-declaration rows

For a RelationSignature row:

1. resolve the exact direct relation pattern and its corresponding obtaining predicate;
2. resolve the exact `RelationSignature` edition;
3. resolve the exact SlotSpec and its declaration-local `SlotKind`;
4. check the planned value or designation against the SlotSpec's `ValueKind` and `refMode`;
5. apply the exact semantic cardinality and participant constraints supplied by the direct relation pattern and declaration; and
6. retain the row as positive plan content.

The row does not fill the SlotSpec. The SlotSpec remains reusable declaration content. The planned designation does not become the actual participant, and the direct relation does not obtain until its direct predicate is satisfied for independently identified participants.

#### A.15.3:4.4 - Read operation-declaration rows

For an A.6.1 row, resolve the exact mechanism edition, `operationDesignator`, and `argumentDesignator` or `resultDesignator`. Apply that declaration's ValueKind, `bindingDesignationRule`, binding predicate, semantic cardinality, and planned conditions.

The row is not an operation application or operation-application binding. An actual argument binding requires one exact application occurrence and satisfaction of the declared argument binding predicate. An actual result binding requires that application to return the exact value under the declared result meaning. Type compatibility, an expected result, a method-description phrase, a ticket value, or a matching token establishes neither binding.

#### A.15.3:4.5 - Keep plan, work, and actual use separate

At later use, identify exact `W : U.Work` under A.15.1 only when dated performed work is actually current. Whether or not Work is part of the case, establish every actual relation participant through its obtaining direct predicate and every operation argument or result through the exact A.6.1 application-binding predicate. Work, WorkPlan, PlanItem, matching label, declaration compatibility, and shared value establish none of those actual facts by themselves.

A neighboring comparison claim may compare the planned row with the independently governed actual participant or binding under an exact comparison policy. One case may stop at A.6.RCD disposition 2's local compound assertion over the cited plan edition, exact actual-use facts, and substrate-admitted policy. Repeated parameterized semantics may stop at disposition 3's predicate-definition episteme. Only a named occurrence-facing need can open relation-kind admission; the comparison never enters the WorkPlan's identity-bearing content or creates a universal planned-to-actual relation.

Unplanned actual participation remains actual when its own predicate obtains. Conversely, a claim that a planned value was missing, excluded, or substituted needs the comparison policy's applicable closure or negative criterion plus exact case facts. An absent log, unresolved reference, or unavailable fact is `missing-information`, not a negative actual-use or variance result; absent authority is `missing-governor`.

#### A.15.3:4.6 - Revision and replay

Pin a declaration edition or edition-bearing planned value only when a different resolution could change the meaning relied on by the receiving use. “Latest,” a mutable alias, a publication face, or an untyped policy label is not a reproducible declaration, value, or policy reference.

If a declaration member changes before the planned use, revise the WorkPlan claim content and let C.2.1 identify the resulting edition. If work or another actual use has already relied on the prior plan edition, preserve that cited edition and state any substitution or variance in a neighboring governed claim. A changed representation or carrier alone does not revise the plan when the C.2.1 discriminators remain fixed.

A card, table, view, index, or generated summary may project selected WorkPlan claim content under its publication-use governor. It is not a second row authority and may not add planned fillings, defaults, declaration meanings, cardinality, conditions, or baseline semantics.

