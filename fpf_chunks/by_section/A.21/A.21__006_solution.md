---
chunk_kind: "child"
pattern_id: "A.21"
pattern_title: "Gate Decisions from Independent Check Results"
section_id: "A.21:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.21/A.21__006_solution.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "A.21 — Gate Decisions from Independent Check Results"
  - "A.21:4 — Solution"
line_start: 35213
line_end: 35355
dependencies:
  - "A.10"
  - "A.15.5"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.20"
  - "B.3"
  - "C.3.2"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.19"
  - "F.6"
  - "F.9"
  - "G.11"
  - "G.6"
keywords:
---

### A.21:4 - Solution

#### A.21:4.1 - The decision result

`GateDecisionResult` is a C.2.1 result episteme. Its EntityOfConcern is the bounded action or transition being decided. Its ClaimGraph says that one identified profile application maps one complete effective set of check-application results to one decision and action consequence.

Minimum content:

```text
GateDecisionResult:
  resultId
  gateRef
  decisionSubjectRef
  boundedActionRef
  profileApplicationRef
  requiredCheckApplicationIds[]
  optionalCheckApplicationIds[]
  checkApplicationResultRefs[]
  scope
  qualificationWindow
  decisionValue: abstain | pass | degrade | block
  actionConsequence
  recheckCondition
  rationale
```

`decisionSubjectRef` names the proposal, transition, crossing, or prospective work-entry claim being decided. `boundedActionRef` names what the practitioner may do or must hold. Neither identifies a later Work occurrence.

One result is identified by the tuple containing the gate, decision subject, bounded action, profile application, canonical required and optional check-application identity sets, scope, and qualification window. A changed rule edition, checked subject, criterion, case, result, scope, or window requires another result. The decision value and rationale are the content derived for that fixed tuple; a contradictory value for the same tuple is an error, not another result to merge.

The rationale links every check-application result to its mapping rule and then to the aggregate and action consequence. A `GateDecisionExplanation` may restate that rationale in ordinary language; it is optional, carries no decision value, and cannot replace the result or rationale.

#### A.21:4.2 - One check application

A `GateCheckApplicationResult` is a C.2.1 result episteme that keeps the gate-facing use of one source result recoverable:

```text
GateCheckApplicationResult:
  checkApplicationId
  checkKind
  checkedSubjectRef
  criterionRef
  criterionEdition
  ruleApplicationRef?
  caseFactsRefOrValue
  scope
  qualificationWindow
  requirement: required | optional | notApplicable
  evaluationState: evaluated | notRun
  sourceResultRef?
  sourceOutcome?
  mappingRuleRef
  mappingRuleEdition
  mappedDecisionValue?: abstain | pass | degrade | block
  witnessOrReasonRefs[]
```

The pattern that defines or tests the source claim determines `sourceOutcome`; A.21 only applies the cited mapping rule. A not-applicable application states why the criterion does not apply. A not-run application states that evaluation work did not produce a result. Unknown, error, violation, and success keep the meanings supplied by their source patterns.

The application identity includes the checked subject, criterion and edition, applicable rule application, case facts, scope, and window. Two `SystemRoleFit` applications for different Systems and two `RegulatedConformance(X)` applications for different regulators or rule editions are different applications. Deduplicate only genuinely identical application results. If two copies claim different source outcomes for the same identity, stop and resolve the contradiction; do not join them by `checkKind`.

When a publication or selected structure needs a short `GateCheckRef`, that value refers to one identified `GateCheckApplicationResult`. It is not the old `{aspect, kind, edition, scope}` record and cannot omit the checked subject, criterion or rule application, case, scope, or window needed to resolve that result.

#### A.21:4.3 - Profile application

A `GateProfile` describes a policy. It does not show that the policy applies. Every gate decision points to the current application of one profile rule. That application identifies:

- the profile rule and edition;
- the gate, decision subject, and bounded action to which it applies;
- its scope and qualification window;
- the complete required and optional check set;
- the mapping rule for each applicable source outcome;
- the consequence attached to each aggregate decision; and
- any separately required authority or responsibility relation.

A.21 has no implicit default profile. A branch name, `PathSlice`, sentinel, publication mode, product label, or earlier decision does not select or authorize a profile. A new slice may bound changed data or trigger reevaluation; it cannot weaken inherited safety, regulatory, evidence, or other obligations. Any weakening needs another current rule application that permits it and any authority relation required for that change.

#### A.21:4.4 - Complete check set and independent results

Before aggregation, recover the complete effective required set from the profile application. Every required application is present even when it is `notRun`, `unknown`, `error`, or failed.

- `notApplicable` is allowed only when the application gives its scope or applicability reason.
- `notRun` never becomes `abstain` or `pass`.
- `unknown` and `error` remain visible before their explicit profile mapping.
- a failed A.20 result can prevent passage but cannot make freshness, channel, role-fit, regulatory, crossing, or another independent check inapplicable.
- evaluation work may defer an expensive check after a blocking result, but the deferred required check remains `notRun` in the result.

If a profile deliberately accepts known uncertainty, its mapping rule names the checked subject, tolerated uncertainty, permitted bounded action, consequence, and expiry or recheck condition. A generic neutral fold is insufficient.

#### A.21:4.5 - Aggregate and action meaning

In ordinary language: **the worst mapped result wins**. Only after every required application is present and its mapping is known, the technical aggregation is the order-independent join:

`abstain <= pass <= degrade <= block`.

The join is associative, commutative, and idempotent. `abstain` is neutral and `block` absorbs other values, but those algebraic properties do not change the source results.

| Decision | Meaning for the bounded action |
| --- | --- |
| `abstain` | The applicable profile says this gate makes no decision for this action and names the remaining decision route or absence of one. It grants no permission. It is not used for missing, unknown, failed, or unrun required checks. |
| `pass` | Every required application is present and the current profile accepts the bounded action without an added restriction, within the stated scope and window. |
| `degrade` | The profile accepts only the named restricted or conditional form of the action. The result states the restriction, stop or exit condition, and recheck condition. It is not an unspecified “proceed carefully”. |
| `block` | The profile refuses or holds the bounded action under the current facts and states what change or new result can reopen the decision. |

An optional application affects the aggregate only when the cited profile rule says it does. A required missing or `notRun` result can map to `degrade` or `block` under an explicit rule, never to `pass` or neutral `abstain`.

#### A.21:4.6 - Scope, composition, and change

Compose check sets only through the exact profile applications that cover the decision subject and scope. A more specific application may add, replace, or remove a check only when its policy rule and applicability fact say so. Preserve parameterized identities such as regulator X and its rule edition.

`lane`, `locus`, `subflow`, and `profile` may be used as scope values only when the selected structure or policy defines the corresponding boundary for this application. A scope label alone neither selects a profile nor merges check applications.
Recompute the result when the decision subject, bounded action, profile application, required set, check application identity or result, scope, or window changes. A refresh, edition bump, expired evidence window, changed crossing, or changed path slice matters only when it changes one of those inputs under its own pattern.

#### A.21:4.7 - Optional LaunchGate use

Use `LaunchGate` only when an A.21 gate-decision relation is current for one prospective `workEntryClaimRef`, WorkPlan or PlanItem entry question, and bounded attempted action. The gate refers to that prospective claim; it never targets a not-yet-existing Work individual.

`A.15.5` remains the ordinary route for full-kit and work-entry readiness. Add a LaunchGate only when the selected transformation-flow structure actually contains that gate use. Freshness, design-run-tag consistency, A.20 ingress validity, structural crossing, and SquareLaw are checks only when their exact claims, rules, and defining patterns are current. No one of them is mandatory merely because the word “launch” appears.

If a required ingress A.20 summary is not `satisfied` and the applied profile defines a pre-run barrier, the aggregate is `block`. Other available results remain visible; deferred checks remain `notRun`.

#### A.21:4.8 - Crossing and semantic-Bridge boundary

For a structural crossing, receive the exact changed-binding and crossing facts from E.18. Add a crossing check only when its criterion applies. SquareLaw is required only when the E.18 crossing rule for that case requires it.

A structural crossing does not imply an F.9 semantic Bridge. Add an F.9 Bridge, bounded-use claim, reliance, optional Bridge Card, or optional `CL` only when the separate semantic-correspondence relation and downstream use obtain. A non-crossing gate carries none of this apparatus. Do not encode absent Bridge material as mandatory fields with `none` values.

#### A.21:4.9 - Guards and check families

A guard event is not automatically a GateCheck. When a selected structure assigns a guard failure to a gate, the current profile may consume that identified event through a declared check application and mapping rule.

The following names are recognition aids, not a universal catalogue: freshness, design-run-tag consistency, reference-plane crossing, comparator constraints, evidence completeness, safety envelope, regulator conformance, system-role fit, channel fit, equivalence preservation, outflow audit, and snapshot consistency. Each application names its checked subject, criterion, rule edition, case, and source result. Use A.10 or B.3 for evidence and assurance truth, A.2 and C.3.2 for system-role classification, A.2.1 and F.6 for exact assignments, A.2.6 for channel claims, and E.18 plus the comparison patterns for crossing and comparator claims.

#### A.21:4.10 - Publication, rationale, and reuse

The ordinary one-time result needs the fields in section 4.1 and a short rationale. It does not require a Multi-View Publication Kit (MVPK) face, AssuranceLane, evidence bundle, Bridge apparatus, cache key, or equivalence witness.

When publication is current, E.17 defines the publication form and carrier relations. A publication mode changes only that form; it neither selects a profile nor changes the required check set or aggregate. The published minimum is the result identity, decision subject, profile application, check-application refs, decision, action consequence, scope, window, and recheck condition. Crossing, evidence, regulation, safety, and assurance fields appear only when the corresponding claim is current.

A `DecisionLog` is an optional audit or reuse record that cites one or more `GateDecisionResult` values. It may retain source outcomes, mappings, rationale, evidence refs, and change history; it neither creates nor changes the decision.

Require an equivalence witness only when reuse, cacheability, or a stability interval is claimed. That witness covers every input whose equality is needed for the claimed reuse. A changed profile edition, required set, checked subject, criterion, case, source result, mapping, scope, or window defeats reuse and requires another decision.

