---
chunk_kind: "child"
pattern_id: "F.10"
pattern_title: "Status Families Mapping: Evidence, Standard, and Requirement Status"
section_id: "F.10:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/F.10/F.10__005_solution.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "F.10 — Status Families Mapping: Evidence, Standard, and Requirement Status"
  - "F.10:4 — Solution"
line_start: 92936
line_end: 93086
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.4"
  - "A.6.1"
  - "B.3"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "E.17"
  - "E.24.PUB"
  - "F.17"
  - "F.18"
  - "F.9"
  - "G.11"
  - "G.6"
keywords:
  - "applicability windows"
  - "evidence"
  - "polarity"
  - "requirement"
  - "standard"
  - "status"
---

### F.10:4 - Solution

Recover the governed target and direct result before applying a local status. Treat status value, status-use occurrence, status assertion, source, evaluation, display, and receiving use as distinct.

#### F.10:4.1 - Three status families

F.10 supplies a small set of three status families—`EvidenceStatus`, `StandardStatus`, and `RequirementStatus`—for common project use. A family classifies local status values; it is not a universal result kind and does not create its targets.

| Status family | Modality | Typical exact target | What the family permits one status-use assertion to say |
| --- | --- | --- | --- |
| `EvidenceStatus` | epistemic | exact target-claim episteme or claim-bearing result episteme | The asserted evidential standing of that claim for one scope, polarity, window, and use, after exact A.2.4 evidence-use and direct input results are recovered. It is not the measurement/proof/causal result or evidence relation itself. |
| `StandardStatus` | deontic and curatorial | exact standard/profile edition, method description, governed configuration, or other admitted standard target | What the exact governing source sanctions, discourages, or supersedes for one scheme, edition, scope, window, and use. It is not an approval speech act, permission, runtime result, or requirement satisfaction. |
| `RequirementStatus` | deontic and compliance-facing | exact requirement, duty, constraint, acceptance, or obligation clause | What is asserted about applicability, satisfaction, violation, waiver, or pending evaluation for that clause under its direct rule, scope, conditions, and window. It is not the clause, evaluation work, result, gate, or assurance. |

A project may define local sublevels or labels, but each label resolves under one effective ReferenceScheme to one exact local sense and maps to one of these three families—`EvidenceStatus`, `StandardStatus`, or `RequirementStatus`—or another direct status owner. F.10 does not create a role kind or global synonym by adding a family row.

#### F.10:4.2 - Status value, use occurrence, assertion, and display

A local status value is designated through an exact F.17 `SchemeSenseCell`:

```text
<EffectiveReferenceScheme, LocalExpression, LocalSenseClaim>
```

An F.18 NameCard may govern its selected public designation. An F.17 row may collect one or more cells for a named unification use; one-cell rows are valid. Neither the cell, card, row, spelling, nor family membership applies the value to a target.

One `StatusUseRelation` candidate names:

```text
StatusUseRelation:
  StatusBearerRef:
  StatusTargetRef:
  DirectTargetAndResultGovernor:
  DirectResultRef:                 # when a domain result is consumed
  StatusValueCellRef:
  StatusFamilyRef:
  EffectiveReferenceScheme:
  StatusScope:
  StatusWindow:
  IntendedStatusUse:
  SourceClaimEpistemeRef:
  SourceRelationOrRegisterRef:
  EvaluationWorkRef:               # when a rule is applied
  EvaluationRuleAndApplicationRef: # when a rule is applied
  EvaluationResultClaimRef:        # when a result is produced
  ProvenancePathRef:
  CurrentnessRef:
  NotCarried:
```

For an F.10-family status, `StatusUseRelation(B,T,V,G,W,U)` obtains only when: `B` and `T` resolve to admitted governed objects; exact cell `V` has the required F.10 family/local sense under its effective ReferenceScheme; the family-specific source and any direct result/evaluation basis support applying `V` to `T`; `G` and `W` bound that application; and `U` is the named intended use without a stronger inference. Unknown or missing basis yields no positive occurrence and a `Pending`, `Inconclusive`, or explicit unresolved disposition only when that value's own rule is satisfied. Absence of evidence is never target falsity.

One F.10 occurrence is identified by the exact ordered tuple `<B,T,V,G,W,U>`. Repeated evaluations, assertions, displays, rows, records, or citations create no duplicates. A changed bearer, target, value cell, scope, window, or intended use identifies another candidate. A changed source, evidence path, evaluation, or currentness fact can change whether the fixed candidate is warranted or obtains; it is not silently copied into relation identity. A status governed by another direct pattern exits there instead of inheriting this predicate by family resemblance.

A distinct C.2.1 status-assertion episteme states affirmative or negative polarity for the exact `StatusUseRelation`. A separate display or publication form may render that assertion. The assertion does not perform evaluation, and the display does not become the assertion, source, or actual receiving use.

#### F.10:4.3 - Recover the target and result first

Use this order:

1. name the receiving question and exact target;
2. recover the target's identity and direct governor;
3. recover any measurement, formal, causal, conformance, diagnostic, comparison, acceptance, requirement-evaluation, gate, assurance, permission, or decision result under its own pattern;
4. identify the C.2.1 episteme that states that result;
5. resolve the local status expression to its exact F.17 cell and F.10 family;
6. recover the source, edition, scheme, scope, conditions, window, provenance, and currentness required by this status use;
7. when a rule is needed, identify dated evaluation work, enacted method, exact direct/A.6.1 application, and evaluation-result claim;
8. assert the status-use relation and its C.2.1 status-assertion episteme; then separately recover publication/display and any actual later premise, decision-use, status-use, gate-use, or operation-argument relation.

Status never defines or constitutes the target. A changed status may change a receiving disposition without changing target identity or the earlier domain result. Conversely, a changed target or direct result requires the status application to be re-evaluated; copying the old value is not continuation proof.

#### F.10:4.4 - A.2.4 status-use positions

When an A.2.4 first-use classification is current, retain its positions by value:

| Position | F.10 use |
| --- | --- |
| `StatusBearerSlot` | Exact bearer from which the status is asserted or read; not a role holder. |
| `StatusTargetSlot` | Exact governed target; required when different from the bearer. |
| `StatusScopeSlot` | Claim, requirement, admission, or use scope; not a generic context object. |
| `StatusValueSlot` | Exact local status-value cell or value governed here or by another direct status pattern. |
| `StatusWindowSlot` | Validity, edition, freshness, or source window. |
| `StatusUseSlot` | Named intended use; actual later use still needs its dated work and direct relation. |
| `StatusProvenanceConstraintSlot` | Exact source order, authority source, publication, proof, verification, register, or provenance condition. |

These are relation positions, not work-role qualifier slots, a record schema that applies status, or a new generic status ontic.

#### F.10:4.5 - Family value sets

**EvidenceStatus** local values:

1. `Observed` — seen or recorded once under declared observation conditions.
2. `Measured` — supported by a declared measurement method, model, calibration basis, value, and uncertainty.
3. `Corroborated` — supported by more than one independent source, procedure, or observation line.
4. `Replicated` — repeated by independent work or under varied declared conditions.
5. `Refuted` — counter-evidence defeats positive evidential standing inside the same scope and window.
6. `Inconclusive` — available input results and evidence-use relations are insufficient or mixed for the target claim.

These values classify evidential standing; they do not replace the observation, measurement, proof, causal, or other direct result, and `Inconclusive` is not target falsity.

**StandardStatus** local values:

1. `Candidate` — proposed and not yet normative for the named scheme/use.
2. `Draft` — worked text or profile, not yet the governing edition.
3. `Approved` — sanctioned by the exact governing source for the named scheme, edition, scope, window, and use.
4. `Deprecated` — discouraged, conditionally allowed, or being phased out.
5. `Superseded` — replaced by another named edition, profile, or governing source.

`Approved` does not mean that an approval act occurred unless its direct speech-act/decision relation is separately recovered; it grants no permission and proves no runtime satisfaction.

**RequirementStatus** local values:

1. `Applicable` — the exact clause binds under its governed scope, conditions, and window.
2. `Inapplicable` — the clause does not bind under those conditions.
3. `Satisfied` — a direct requirement/acceptance evaluation result says the clause is met for the exact target, scope, conditions, and window.
4. `Violated` — the direct evaluation result says it is not met there.
5. `Waived` — binding is suspended or excepted by an exact authorized source/relation and window.
6. `Pending` — the status application awaits a needed source, input result, evaluation, decision, or currentness repair.

`Satisfied`, `Violated`, `Waived`, and `Pending` do not replace the clause, evaluation work/result, waiver act or permission, gate decision, assurance result, or action.

#### F.10:4.6 - Bridge and interpretation discipline

Status meanings do not travel by label. When two local status senses under different ReferenceSchemes must be compared, use the actual F.9 Bridge occurrence between the exact F.17 SchemeSenseCells, with direction, bridge kind, tolerance/loss, and bounded use. Its Card or description is separate and optional; optional F.9 `CL` remains evidence-strength shorthand, not a use threshold. The Bridge makes no status-use occurrence obtain and produces no target result.

When one status-use occurrence is used to explain or evaluate a status question of another family, scheme, or modality, recover an exact `StatusInterpretationRelation`:

```text
StatusInterpretationRelation:
  SourceStatusUseOccurrenceRef:
  TargetStatusQuestionRef:
  Direction:
  InterpretationRuleRef:
  EffectiveReferenceScheme:
  ClaimScopeAndWindow:
  BridgeRef:                    # only when local senses cross schemes
  IntendedUse:
```

It obtains only when the named interpretation rule admits that source occurrence for the exact target question, direction, scope, window, and use. Its occurrence identity is the exact ordered `<SourceStatusUseOccurrenceRef, TargetStatusQuestionRef, Direction, InterpretationRuleRef, ClaimScopeAndWindow, IntendedUse>` tuple; a Bridge ref is a separate qualifying premise when local senses cross schemes. A family edge, shared word, Bridge, table row, or source order is not this relation. Applying the rule is separate dated evaluation work; its result claim is separate again. Even a positive interpretation relation does not by itself produce `RequirementStatus=Satisfied`, `StandardStatus=Approved`, a gate result, permission, assurance, or actual later reliance.

#### F.10:4.7 - Design-run discipline

Keep three questions separate:

* What do exact observation, measurement, proof, causal, or other input results warrant as evidence standing for this target claim and window?
* What does an exact governing source sanction for this method description, profile, standard edition, or configuration and use?
* What does direct requirement-evaluation work conclude about this exact clause, target, scope, conditions, and runtime/design window?

A standard-approved method description may be admissible for selection under that profile. It does not show that the method was enacted or that a runtime clause was satisfied. Runtime evidence may become an admitted input to requirement evaluation through an exact evidence-use and status-interpretation relation. It does not approve the method, standard, gate, or release.

