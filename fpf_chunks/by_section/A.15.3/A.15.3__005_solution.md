---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__005_solution.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:4 — Solution"
line_start: 25655
line_end: 25760
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

#### A.15.3:4.0 - What the plan item is—and is not

`SlotFillingsPlanItem` is a content form inside one `U.WorkPlan` ClaimGraph. It is not a U-kind, dependent durable kind, `U.Relation` occurrence, ontic `SlotRelation`, independent record, or second slot ontology. Its item and row designators have meaning only within that WorkPlan episteme.

C.2.1 and A.15.2 identify the WorkPlan episteme. Changing an identity-bearing row creates different WorkPlan claim content and therefore another WorkPlan episteme. The two are historical editions only if an `EpistemeEditionRelation` predicate obtains between them; a shared file, label, carrier, or revision order does not supply that continuity. A reference may point to the WorkPlan and this content component, but it gives the PlanItem no separate identity or edition rule.

A **planned-filling claim** says: for this intended future performance and under these conditions, use this value or designation for this declared member. A.15.2 and A.15.3 state that intention. The member's own pattern still defines what the participant, argument, or result means and what must hold for its later actual use.

The phrase **planned filling** does not mean that a declaration is filled, a relation obtains, an application occurs, or a value is actually bound. The row is plan content and needs no relation kind of its own. A later claim that the plan was fulfilled, missed, or changed belongs to A.15.2, A.6.RCD, or the applicable comparison pattern.

A planned-filling row states a positive intention. To prohibit or exclude a value, require its absence, or claim the list is complete, write a separate constraint or negative plan claim with its own applicability and polarity rule. Omission, an empty filler, and a negated reference do not express those claims.

#### A.15.3:4.1 - Use only members that a declaration already defines

Each row points to one member in one declaration edition selected for the intended future use. First choose what is being planned; then open the pattern that defines that member and the rule for its actual use:

| Planned choice | Existing declaration member | What remains defined elsewhere |
| --- | --- | --- |
| participant in a future direct-relation claim | one `SlotSpec` in one `RelationSignature` edition | the relation pattern defines participant meaning and the obtaining predicate; A.6.5 defines the local `SlotKind`, `ValueKind`, and `refMode`; A.15.3 records only the planned designation |
| argument in a future operation application | one `ArgumentDeclaration` in one A.6.1 `OperationDeclaration` | A.6.1 and the cited mechanism define the argument meaning, ValueKind, designation rule, binding predicate, and cardinality; A.15.3 records only the planned value |
| expected result of a future operation application | one `ResultDeclaration` in one A.6.1 `OperationDeclaration` | A.6.1 and the cited mechanism define result meaning and the result-binding predicate; an expected value is not a returned value |
| another declared future use | one declaration member whose own pattern defines both the member meaning and its actual-use predicate | cite that pattern and declaration; if either definition is absent, return `missing-governor` instead of inventing a target |

A `U.MethodDescription` is not a target merely because it mentions inputs, effects, parameters, bounds, or acceptance conditions. Nor does a suite description, kit description, table, schema, card, checklist, interface form, or database field expose an A.6.5 SlotSpec unless a cited `RelationSignature` actually contains that SlotSpec. Operation arguments and results stay in A.6.1 declarations; planning them does not turn them into A.6.5 SlotSpecs.

One item may contain several rows when they serve the same intended performance, baseline policy, and rule for revising the plan. Each row still resolves to its own declared member. Split the item when those three controls differ. The WorkPlan's present EntityOfConcern remains its C.2.1 identity discriminator; a merely possible future performance does not replace it.

#### A.15.3:4.2 - State one planned-filling row

A conforming item contains or resolves these values:

```text
SlotFillingsPlanItem:
  planItemDesignator
  workPlanRef
  intendedPerformanceDesignator
  plannedFillingRows:
    - rowDesignator
      targetDeclarationRef
      targetOperationDesignator?
      targetMemberDesignator
      targetMemberFamily:
        RelationSignatureSlotSpec |
        OperationArgumentDeclaration |
        OperationResultDeclaration |
        OtherDeclaredMember
      memberDefinitionPattern
      plannedValueOrDesignation
      planningConditions?
      declarationEditionPin?
      plannedValueEditionPin?
  baselinePolicyRef?
  laterComparisonPolicyRef?
```

This block represents WorkPlan claim content; it is not an ontic record schema or a second authority for rows. `targetMemberFamily` is an open local dispatch vocabulary, not a public kind or closed inventory. For an operation argument or result, `targetOperationDesignator` is required so the member resolves inside the cited mechanism edition; it stays absent for relation SlotSpecs. The `memberDefinitionPattern` field points to the pattern that defines the member and its actual-use predicate. A.15.3 still states only the plan's intention.

Read the designation rule from the selected member instead of copying it into the plan. An A.6.5 member uses its `refMode`; an A.6.1 member uses its `bindingDesignationRule`. A ByRef value must use the concrete reference kind required there and resolve to the declared ValueKind. A generic `Ref`, `SpecRef`, stored token, or merely compatible value does not pass.

Use the selected member's semantic cardinality. For a single-valued member, conditions and a resolution rule must make at most one planned value effective for one intended use. Alternatives need conditions and a rule that selects among them; row order supplies neither priority nor exclusivity. A multivalued member keeps the declaration's set, sequence, multiset, repetition, and ordering semantics. If the declaration and cited policy do not decide the needed cardinality, return `missing-governor` for the member cardinality or selection policy.

Omitting a row says only that this WorkPlan does not rely on that filling. It does not say the value or later participant is absent. Prohibition, exclusion, required absence, and closed-world completeness remain separate plan claims with their own applicability and polarity rules.

`intendedPerformanceDesignator` names the future use being planned; it does not make a future Work occurrence or entity exist. The enclosing WorkPlan keeps its already identified present EntityOfConcern under C.2.1 and A.15.2.

Add time, location, capability, readiness, gate, evidence, source-currentness, bridge, or publication conditions only when changing one would change whether the planned value applies or which value is selected. Cite the separate claims that establish those conditions. `planningConditions` points to them; it creates none of them and is not a generic condition bundle.

When a baseline or comparison policy selects a planned value or judges a later match, identify its concrete kind, defining pattern, edition, applicability, and reference scheme. A generic `PolicyRef` or shared label supplies no policy. Pin a declaration or edition-bearing value only when another resolution would change the planned meaning, and make the target reference and pin agree.

#### A.15.3:4.3 - Plan a future relation participant

For a RelationSignature row:

1. open the relation pattern and its obtaining predicate;
2. choose the `RelationSignature` edition the plan will use;
3. choose its declaration-local SlotSpec and `SlotKind`;
4. check the planned designation against the SlotSpec's `ValueKind` and `refMode`;
5. apply the declaration's semantic cardinality and participant constraints; and
6. record the row as a positive intended designation.

The row does not fill the SlotSpec. The SlotSpec remains reusable declaration content. The planned designation does not become the actual participant, and the direct relation does not obtain until its direct predicate is satisfied for independently identified participants.

#### A.15.3:4.4 - Plan a future operation argument or result

Open the cited A.6.1 mechanism edition, choose its `operationDesignator`, then choose the `argumentDesignator` or `resultDesignator`. Apply that declaration's ValueKind, `bindingDesignationRule`, binding predicate, semantic cardinality, and the plan's stated conditions.

The row plans a value; it is not an application or binding. An actual argument binding needs an identified application whose argument-binding predicate holds. An actual result binding additionally needs that application to return the value under the declared result meaning. Type compatibility, an expected result, a method phrase, a ticket value, or a matching token establishes neither binding.

#### A.15.3:4.5 - Compare later use without changing the plan

When work actually occurs, identify `W : U.Work` under A.15.1. Independently establish each relation participant through its obtaining predicate and each operation argument or result through the A.6.1 application-binding predicate. A matching plan row, label, type, or value establishes none of those facts.

If the team must state whether actual use matched the plan, name the comparison policy and the independently established actual facts. A one-off comparison may use A.6.RCD disposition 2 for a local compound assertion. Repeated parameterized comparisons may use disposition 3 for a predicate-definition episteme. Do not admit a comparison relation kind unless a later calculation or decision must refer to repeated comparison occurrences as such; then name that use and follow relation-kind admission. None of these comparisons changes the WorkPlan or creates a universal planned-to-actual relation.

An unplanned participant is still actual when its own predicate holds. To say that a planned value was missing, excluded, or substituted, apply the comparison policy's closure or negative criterion to the case facts. An absent log, unresolved reference, or unavailable fact yields `missing-information`, not a negative use or variance result; absent authority yields `missing-governor`.

#### A.15.3:4.6 - Preserve revisions and replay

Pin a declaration edition or edition-bearing planned value only when choosing another one could change the planned meaning. *Latest*, a mutable alias, a publication face, or an untyped policy label is not a reproducible reference.

If the selected declaration member changes before use, revise the WorkPlan claim content. An identity-bearing change creates another WorkPlan episteme; assert historical continuity only when `EpistemeEditionRelation` obtains. Preserve the earlier WorkPlan reference already cited by work or another actual use, and state substitution or variance separately. A carrier or representation change alone does not reidentify the plan while the C.2.1 discriminators stay fixed.

A card, table, view, index, or generated summary may show selected WorkPlan content under its publication-use pattern. It is read-only: it may not add planned rows, defaults, declaration meanings, cardinality, conditions, or baseline rules.

