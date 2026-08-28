---
chunk_kind: "child"
pattern_id: "A.20"
pattern_title: "Constraint Validity for Transformation Steps"
section_id: "A.20:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.20/A.20__006_solution.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "A.20 — Constraint Validity for Transformation Steps"
  - "A.20:4 — Solution"
line_start: 34159
line_end: 34268
dependencies:
  - "A.10"
  - "A.15"
  - "A.21"
  - "A.6.1"
  - "A.6.4"
  - "B.3"
  - "C.2.1"
  - "C.27"
  - "E.17"
  - "E.18"
  - "E.20"
  - "F.9"
  - "G.11"
keywords:
---

### A.20:4 - Solution

#### A.20:4.1 - Result ontology

`ConstraintValidityResult` is a C.2.1 result episteme. It is not a new U-kind and not a world-side relation. Its exact EntityOfConcern is the constrained subject. Its ClaimGraph states one application of one named constraint to one case.

The constrained subject is normally:

1. one independently identified `U.Transformation` used at an E.18 transformation position;
2. one A.6.1 operation application whose internal law is being tested; or
3. one exact claim that an A.6.4 retargeting is fit for the stated use when its invariant or declared loss boundary is the constraint. A.6.4 names this separate use assertion q; the arrow r named by q and any actual operation application remain separate.

Another subject is admissible only when its own pattern defines a named internal constraint and states why this result form applies. An E.18 locus label alone supplies neither the subject nor the constraint.

Minimum result content:

```text
ConstraintValidityResult:
  resultRef: C.2.1 episteme
  constrainedSubjectRef:
  constraintRef:
  constraintEdition:
  applicabilityValue: required | optional | notApplicable
  applicabilityBasis:
  caseFacts:
  referenceSchemeAndScope:
  evaluationWindow:
  evaluationState: evaluated | notRun
  outcome?: satisfied | violated | unknown | error
  witnessOrReason:
  effectiveUseWindow?:
  evaluationWorkRef?:
```

`outcome` is present only when `evaluationState=evaluated` and `applicabilityValue` is `required` or `optional`. A not-applicable constraint records the reason it is outside this case. A not-run constraint records that evaluation work has not produced a result. Neither is `unknown` and neither silently counts as success.

If a dated evaluation Work occurrence matters, cite it separately through `evaluationWorkRef`; the Work and result episteme do not become one object.

The legacy label `FlowConstraintValidity` may be retained only as a locator for this result family. It does not name a relation, gate status, publication record, or flow-wide property.

#### A.20:4.2 - Applicability, required set, and summary

Before evaluation, name the constraints applicable to the current subject and case. Mark each as `required`, `optional`, or `notApplicable` and state why. The required set is complete only when every constraint that the current use depends on is named.

For one evaluated applicable constraint:

- `satisfied` means the test established the named constraint for the stated case and window;
- `violated` means the test established a counterexample or failed condition;
- `unknown` means required facts, applicability facts, or witness content could not be determined;
- `error` means the selected evaluation could not complete correctly.

When a consumer needs one local summary over the complete required set, use:

`ConstraintValiditySummary ∈ {satisfied, violated, unresolved, notApplicable}`.

The summary rule is:

1. `notApplicable` only when the declared required set is empty because no A.20 internal constraint applies to this subject and use;
2. `violated` when at least one required result is `violated`;
3. `unresolved` when no required result is violated but at least one required constraint is `notRun`, `unknown`, or `error`; and
4. `satisfied` only when every required applicable constraint has an evaluated `satisfied` result.

Optional results do not change the summary unless a separately accepted use decision moves their constraints into the required set. A missing required result can therefore never disappear beside a satisfied result.

#### A.20:4.3 - Constraint families and outcome rules

The following families are recognition aids, not a universal required list. Each application still names the actual constraint, edition, assumptions, case facts, and test.

| Constraint family | Trigger | `satisfied` means | Other outcomes |
| --- | --- | --- | --- |
| Type, domain, and range | The subject consumes or produces typed values. | Every case input and result used by the claim lies in the declared type, domain, and range. | A counterexample is `violated`; unavailable values are `unknown`; a failed test is `error`. |
| Admissibility conditions | The operation or transformation declares guards or admissible cases. | Every required guard is true for the case and window. | A false guard is `violated`; undetermined guard truth is `unknown`. |
| Law or invariant set | The current claim relies on a named law or invariant. | The named invariant holds for the case under its assumptions. | A counterexample is `violated`; missing case facts or witness content are `unknown`. |
| Quantity and unit coherence | The current operation combines quantities or units. | The case is coherent under the already declared quantity, unit, and reference-scheme rules. | A mismatch is `violated`; an unrecovered declaration is `unknown`. A.20 does not define or translate units or planes. |
| Sensitivity or stability bound | A robustness, continuity, perturbation, safety-envelope, or stability claim actually depends on a bound. | The cited bound covers the stated domain, assumptions, distance or norm, and case. | A counterexample is `violated`; absent assumptions or certificate content are `unknown`. No bound is required without this trigger. |
| Return-shape preservation | A consumer relies on a declared set, archive, order, or other non-scalar result shape. | The transformation preserves that declared shape for the current case. | Hidden scalarization or lost required structure is `violated`; unrecovered shape facts are `unknown`. A.20 does not rank or select the result. |
| A.6.4 retargeting invariant | The constrained subject is the exact proposition in q, and the current use depends on its invariant or loss boundary. | The case support establishes the stated invariant and keeps loss within the stated boundary and use. | A counterexample or excess loss is `violated`; missing support is `unknown` unless the constraint itself makes absence a failure. The arrow r and any application remain separate. |

The constraint's own pattern supplies its truth condition. A.20 supplies the application result form and summary only.

#### A.20:4.4 - Gate and policy boundary

An A.21 gate may consume an exact A.20 result or summary as one declared input. A.20 does not translate `satisfied`, `violated`, or `unresolved` into `pass`, `degrade`, `block`, or `abstain`; A.21 applies the current gate rule to its complete check set.

Every other applicable gate-fit check keeps its own result. A failed or unresolved internal constraint may prevent the aggregate gate decision from passing, but it does not make freshness, system-role fit, channel fit, regulatory conformance, reference-plane crossing, or another independent fact undefined or not applicable.

An implementation may defer expensive evaluation work after an already blocking result. That is a Work or evaluation policy. A deferred required check remains `notRun`; it is not published as not applicable or as a successful neutral value. Any aggregate decision must preserve that incompleteness under A.21.

#### A.20:4.5 - Retargeting boundary

For a `StructuralReinterpretation` use, receive the exact A.6.4 arrow r and separate use assertion q. The A.20 constrained subject is the exact proposition in q: its invariant, visible loss, receiving use, conditions, support, and polarity. If an actual operation application is also current, identify and test it separately.

A.20 does not equate `EntityOfConcernRef` with a Bridge, require `KindBridge`, demand a UTS row, or require an isomorphism, lens, reverse `put`, Put-Get law, or Get-Put law. The proposition in q can satisfy its declared constraint when the stated invariant and loss boundary hold for that use; this result neither reidentifies r nor records an application.

Use F.9 separately only when the current claim also needs an obtaining semantic correspondence between two exact F.17 local senses. Keep its bounded-use claim, optional `CL`, evidence, and reliance separate; A.20 creates none of them.

#### A.20:4.6 - Neighboring claims

A.20 keeps only the result content needed to reuse the internal-constraint finding. When another claim is current:

- `E.17` defines publication relations and faces;
- `E.18` defines structure positions, transfers, paths, crossings, and `PathSlice` identity;
- `G.11` defines refresh planning and performed refresh work;
- `C.27` defines temporal-claim adequacy;
- `A.21` defines check applications, profile use, gate aggregation, and decision consequences;
- `A.10` and `B.3` define evidence use and assurance; and
- `A.15` defines plans and dated Work.

Citing an A.20 result in one of those claims does not copy that consumer's identity, scheduling, publication, or policy fields into A.20.

