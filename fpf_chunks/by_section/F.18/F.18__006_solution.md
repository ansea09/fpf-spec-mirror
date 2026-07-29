---
chunk_kind: "child"
pattern_id: "F.18"
pattern_title: "Local-First Unification Naming Protocol"
section_id: "F.18:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/F.18/F.18__006_solution.md"
commit_sha: "2ada413629b846ef308222d16489a82cb5b40a71"
heading_path:
  - "F.18 — Local-First Unification Naming Protocol"
  - "F.18:4 — Solution"
line_start: 94724
line_end: 94922
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.6.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.6.REL"
  - "A.6.RSIR"
  - "B.3"
  - "C.2.1"
  - "E.10"
  - "E.10.ARCH"
  - "E.24.PUB"
  - "F.0.1"
  - "F.1"
  - "F.13"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.8"
  - "F.9"
  - "G.10"
  - "G.2"
  - "G.6"
keywords:
---

### F.18:4 - Solution

Use a local-first naming protocol:

1. Recover the governed value, its kind, and its direct governing pattern.
2. Decide whether the expression should remain local or the current use needs a durable reusable name; apply `F.14` before adding a card, cell, or row.
3. For a durable name, constitute one `NameCard` episteme under `C.2.1`; keep the value, its kind, the card, selected designations, exact local sense, and any basis or Bridge relation distinct.
4. Choose the Tech and Plain labels from the smallest candidate set that covers the live head-term families and plausible neighbouring objects.
5. Record the covered alternatives, rejected candidates, selection reason, lineage, and the smallest condition that reopens the settlement.
6. Only for public, Core-facing, durable-across-context, or cross-context reuse, test the then-current `F.17` entry. It must accept the exact governed value and kind, NameCard episteme, by-value scheme, local sense, and any actual Bridge. Public or durable reuse alone creates no Bridge. When the named use relates different `<ReferenceScheme, LocalSenseClaim>` projections, F.17 must also accept the separate affirmative C.2.1 claim and current A.10 or B.3 reliance through the row rationale or notes rather than treating either as NameCard content. Its result must supply the required public row. If any required input or result is absent, retain the durable name and NameCard locally, mark the public row pending, and stop.
7. Keep the Bridge, the separate claim about its named use, A.10 or B.3 reliance, authorization, and any actual Work, assertion episteme, publication occurrence, direct relation, operation application, status, evidence, slot, role, method, or interface object under their own governing patterns. F.18 decides only the naming settlement.

#### F.18:4.1 - Naming Invariants

Every durable name must satisfy these invariants.

| Invariant | Required content |
| --- | --- |
| Governed value first | Name the governed value or value family before naming the label. |
| Governing pattern visible | Cite the pattern that owns the value: for example `A.2` for role value, `A.2.1` for role assignment, `A.6.5` for relation slot discipline, `F.10` or `A.19.SPR` for status value use, `A.10` for evidence use. |
| Reference scheme visible | The NameCard carries the effective `U.ReferenceScheme` by value; a model-use structure, claim scope, project work, or other locality relation remains separate and appears only when the naming use needs it. |
| Local sense visible | Every card states one exact local-sense claim under the effective scheme. A progressive-minimum card may state it directly as `LocalSenseRef`; an expanded card uses `LocalSenseCellRef` only when it resolves to the current F.17 scheme-based coordinate. Any basis episteme and local-sense basis relation remain separate. |
| Two labels when reusable | The Tech label is precise; the Plain label helps ordinary readers. Both point to the same governed value. |
| Candidate comparison visible | At least two plausible head families are considered unless a cited external standard fixes the label. |
| Bridge only between different semantic-context projections | Compare the exact `<ReferenceScheme, LocalSenseClaim>` pairs. Same scheme plus same claim plus another expression routes to designation and no Bridge. Same scheme plus another claim opens F.9 and, for a named use, the separate claim-and-reliance branch. Different scheme opens only the Bridge question. No current correspondence use creates no Bridge or use claim regardless of scheme count. An obtaining Bridge establishes only the exact sense relation; it establishes neither governed-value identity nor authorization. |
| Lineage visible | Rename, split, merge, retirement, and alias decisions are recorded. |

#### F.18:4.2 - `NameCard` Fields

A NameCard is complete when its exact C.2.1 identity-bearing `U.ClaimGraph` is recoverable; completeness is not a field count. The accepted D11 progressive-minimum cards `NC-U-RELATION`, `NC-CROSS-CONTEXT-RELATION-STRUCTURE`, `NC-PROBLEM-CRITERION-APPLICABILITY-RELATION`, and `NC-PROBLEMATIC-FOR-RELATION` remain conforming. Each already states the governed value and direct owner, effective scheme and local-sense claim, one selected Tech/Plain pair, candidate set, rejections, rationale, lineage, and reopen condition. Its direct owner makes the governed kind unambiguous. These filled claims together constitute the card's complete claim graph; an omitted expanded field contributes no hidden claim. Section 4.2a carries the four current expanded bounded-model-use cards.

Use the expanded form only when the current naming use needs the additional position:

```text
NameCard:
  NameCardId:
  GovernedValueRef:
  GovernedValueKindRef: [add when the kind is not unambiguous from the value and direct owner, or a consumer needs the exact kind reference]
  GoverningPatternRef:
  ReferenceScheme:
  ClaimContent: [reference to the complete U.ClaimGraph constituted by all identity-bearing naming-settlement claims]
  LocalSenseCellRef: [add when a separately recoverable F.17 scheme-based SenseCell is current; otherwise LocalSenseRef carries the direct local-sense claim]
  LocalSenseBasisRelationRef: [add only for an actual separately governed basis relation]
  TechLabel:
  PlainLabel:
  CandidateSet:
  CandidateCoverage: [add when family coverage, an open alternative, or a forced exception must be explicit]
  RejectedCandidates:
  SelectionRationale:
  BridgeRefs: [add only for actual F.9 Bridge occurrences used to align exact local senses; no use direction, rule, tolerance, polarity, or reliance lives here]
  PublicRowStatus: [add when public-row use is current]
  UnifiedTermRowRef: [add only for a current row returned by section 4.4]
  LineageEntries:
  RefreshCondition:
```

Field discipline:

- The card is a `C.2.1` episteme. `GovernedValueRef` is its exact `EntityOfConcern`; the complete `U.ClaimGraph` constituted by all identity-bearing naming-settlement claims is its `ClaimContent`; and `ReferenceScheme` is the effective by-value `U.ReferenceScheme` under which that graph is interpreted. Changing any of those three identifies another card episteme. Changing only a graph designator, card designator, carrier, field order, or layout does not.
- In the expanded form, the `ClaimContent` field resolves to that complete graph; it is never a scalar summary beside other identity-bearing claims. The readable sibling fields designate graph nodes, edges, or projections. Changing a selected designation, declared use, local-sense claim, coverage, rejection, rationale, lineage, or reopen claim changes the graph and therefore the card episteme even if the displayed `ClaimContent` reference string stays the same.
- `NameCardId` designates the card episteme. It is not another identity discriminator and does not create a card kind.
- `GovernedValueRef` resolves to the exact already-governed object or value being named. `GovernedValueKindRef` is added when the kind is not already unambiguous from that value and its direct owner, or when a receiving use needs the exact kind reference. For relation-facing wording the value reference resolves to exactly one of the objects distinguished in section 5.6; a field label, card, table row, or local phrase is not a proxy for that object.
- `GoverningPatternRef` names the direct pattern that decides the value. `F.18` governs only the naming settlement recorded in the card; a pattern that merely presents or teaches the name governs neither the value nor this settlement.
- `LocalSenseRef` in a progressive-minimum card states the exact local-sense claim directly under the card's by-value scheme. `LocalSenseCellRef` in an expanded card resolves to the current F.17 coordinate `<ReferenceScheme by value, LocalExpression, LocalSenseClaim>` and does not require a context holon. `LocalSenseBasisRelationRef` is present only when a separately governed relation to a basis episteme is current; a source title, card field, or publication is not that relation.
- `CandidateSet` records the plausible labels considered by head-term family. When family coverage or an exception is not already recoverable from the set, rejections, and rationale, add `CandidateCoverage` to state which live families and neighbouring-object readings were tested and whether any plausible alternative remains open.
- `RejectedCandidates` records why tempting names were not selected. A usable alias is recorded in lineage as an alias, not left as a second selected Plain label.
- `BridgeRefs` contains only actual F.9 Bridge occurrences whose relation-semantic profiles obtain for the exact endpoint senses. It carries no naming-use direction, use-specific rule, tolerated loss, polarity, reliance, or permission. When naming across different semantic-context projections relies on a Bridge, recover the separate C.2.1 claim and its current A.10 or B.3 reliance outside the NameCard; omit `BridgeRefs` when the settlement makes no Bridge claim.
- `PublicRowStatus` is exactly one of `localOnly`, `pending`, or `current` when public-row use is current. `UnifiedTermRowRef` separately resolves to the exact row and is present only when status is `current` after the section 4.4 `F.17` entry/result gate passes. Omission in an accepted progressive-minimum card claims no row. A pending public use does not imply that a row already exists.
- `RefreshCondition` names the smallest value, kind, scheme, local-sense, Bridge, governing-pattern, use, or repeated-reader-error change that reopens this exact settlement.

Names such as "foundational principle pattern set", "FPF Core", "domain principle framework", and "local practice framework" require ordinary `NameCard` work before public stabilization under an effective reference scheme. Source aliases such as `ZPF`, `SPF`, `TPF`, or broad `xPF` labels remain intake aliases until `F.18` has settled the governed value and kind, by-value reference scheme, exact local sense, rejected candidates, and admissible short form.

#### F.18:4.2a - Current Bounded-Model-Use NameCards

The four expanded cards below are the current `FPFCoreReferenceScheme` naming settlements consumed by F.17:12.4d-12.4e. Each resolves to one exact current scheme-based F.17 cell and its separately governed local-sense basis relation. They publish designations for already governed values; they create no kind, structure, relation occurrence, assertion, Work, Bridge, use, reliance, row-availability occurrence, or other receiving action.

```text
NameCard:
  NameCardId: NC-BOUNDED-MODEL-USE-STRUCTURE
  GovernedValueRef: BoundedModelUseStructure
  GovernedValueKindRef: U.Kind
  GoverningPatternRef: A.1.1
  ReferenceScheme: FPFCoreReferenceScheme
  ClaimContent: NC-BOUNDED-MODEL-USE-STRUCTURE.ClaimGraph — complete C.2.1 U.ClaimGraph constituted by all identity-bearing naming-settlement claims designated below
  LocalSenseCellRef: SenseCell.BoundedModelUseStructure.FPFCore.2026-07-25
  LocalSenseBasisRelationRef: LocalSenseBasisRelation.BoundedModelUseStructure.FPFCore.2026-07-25
  TechLabel: BoundedModelUseStructure
  PlainLabel: bounded context
  CandidateSet: BoundedModelUseStructure; ModelApplicabilityStructure; ModelUseRelationStructure; BoundedContextStructure; U.BoundedContext
  CandidateCoverage: exact dependent-structure head; applicability-only neighbour; use-only neighbour; DDD retrieval head; false holon-kind neighbour; no plausible live head family remains untested
  RejectedCandidates: ModelApplicabilityStructure omits actual use and fixed-content expression coherence; ModelUseRelationStructure collapses the wider organization into one relation family; BoundedContextStructure hides what is bounded and invites a container reading; U.BoundedContext falsely claims another holon kind
  SelectionRationale: the Tech label names the A.1.1 dependent U.Structure specialization selected from one exact model edition, admitted model-use holons, obtaining applicability, actual-use, and fixed-content expression-coherence occurrences, exact applied constraint claims, and one named frame; the Plain label retains DDD retrieval without adding a context bearer or any crossing to that identity
  PublicRowStatus: current
  UnifiedTermRowRef: UTS.BoundedModelUseStructure.FPFCore.2026-07-25
  LineageEntries: DDD bounded-context wording retained as the Plain retrieval label; U.BoundedContext holon, boundary-container, semantic-frame-bundle, and crossing-bearing readings retired; any crossing belongs only to a distinct A.22 structure over already identified bounded model-use structures
  RefreshCondition: reopen when the A.1.1/A.22 membership or continuity rule, one of the three direct relation kinds, the exact constituent, selected-occurrence, applied-constraint, or frame discriminator, FPFCoreReferenceScheme, the current F.17 cell or row, or repeated container or crossing overreading changes
```

```text
NameCard:
  NameCardId: NC-MODEL-APPLICABILITY-RELATION
  GovernedValueRef: ModelApplicabilityRelation
  GovernedValueKindRef: U.Kind
  GoverningPatternRef: A.1.1
  ReferenceScheme: FPFCoreReferenceScheme
  ClaimContent: NC-MODEL-APPLICABILITY-RELATION.ClaimGraph — complete C.2.1 U.ClaimGraph constituted by all identity-bearing naming-settlement claims designated below
  LocalSenseCellRef: SenseCell.ModelApplicabilityRelation.FPFCore.2026-07-25
  LocalSenseBasisRelationRef: LocalSenseBasisRelation.ModelApplicabilityRelation.FPFCore.2026-07-25
  TechLabel: ModelApplicabilityRelation
  PlainLabel: this model applies to this holon within this claim scope
  CandidateSet: relation-kind heads {ModelApplicabilityRelation, ModelAppliesToRelation, ModelScopeRelation}; claim-or-predicate heads {ModelApplicabilityClaim, ModelApplicabilityPredicate}; temporal head {ModelApplicabilityInterval}
  CandidateCoverage: direct ternary relation kind; readable predicate direction; claim or predicate neighbour; scope-membership neighbour; derived temporal-extent neighbour; no plausible live head family remains untested
  RejectedCandidates: ModelAppliesToRelation suggests a binary relation and hides the participating claim scope; ModelScopeRelation mistakes A.2.6 scope membership for model applicability; ModelApplicabilityClaim and ModelApplicabilityPredicate name epistemic or semantic content; ModelApplicabilityInterval names the derived maximal continuous extent
  SelectionRationale: the Tech label names the direct relation kind over one model episteme, exact holon, and participating claim scope; the Plain sentence exposes the predicate while A.1.1 alone decides whether its applicability condition holds and reidentifies the maximal continuous occurrence, leaving scope membership, assertion, interval, and structure separate
  PublicRowStatus: current
  UnifiedTermRowRef: UTS.ModelApplicabilityRelation.FPFCore.2026-07-25
  LineageEntries: retains the A.1.1 relation-kind label; earlier broad applicable-model and context-boundary wording is not an alias; ModelApplicabilityInterval remains a local derived extent
  RefreshCondition: reopen when A.1.1 changes the participant kinds, applicability predicate, scope-alignment or model-scheme interpretation rule, temporal occurrence identity, FPFCoreReferenceScheme, the current F.17 cell or row, or the public receiving use
```

```text
NameCard:
  NameCardId: NC-MODEL-USE-RELATION
  GovernedValueRef: ModelUseRelation
  GovernedValueKindRef: U.Kind
  GoverningPatternRef: A.1.1
  ReferenceScheme: FPFCoreReferenceScheme
  ClaimContent: NC-MODEL-USE-RELATION.ClaimGraph — complete C.2.1 U.ClaimGraph constituted by all identity-bearing naming-settlement claims designated below
  LocalSenseCellRef: SenseCell.ModelUseRelation.FPFCore.2026-07-25
  LocalSenseBasisRelationRef: LocalSenseBasisRelation.ModelUseRelation.FPFCore.2026-07-25
  TechLabel: ModelUseRelation
  PlainLabel: this assignment's holder uses this model during this work concerning this holon
  CandidateSet: relation-kind heads {ModelUseRelation, ModelUsageRelation, ModelApplicationRelation}; work-or-assignment heads {ModelUseWork, ModelUserRoleAssignment}; claim-or-record heads {ModelUseClaim, ModelUseRecord}
  CandidateCoverage: direct actual-use relation; availability-or-usage neighbour; applicability neighbour; Work neighbour; assignment neighbour; claim or record neighbour; no plausible live head family remains untested
  RejectedCandidates: ModelUsageRelation invites availability, access-count, or generic usage readings; ModelApplicationRelation collides with applicability and can suggest applying a method; ModelUseWork and ModelUserRoleAssignment name participants; ModelUseClaim and ModelUseRecord name epistemes about use
  SelectionRationale: the Tech label names the direct relation kind over one role-assignment occurrence, model episteme, performed Work occurrence, and use-locus holon; the Plain sentence exposes actual use by the derived assignment holder without adding that system as a fifth participant, while A.1.1 keeps applicability, assignment, Work, method application, claim, and record distinct
  PublicRowStatus: current
  UnifiedTermRowRef: UTS.ModelUseRelation.FPFCore.2026-07-25
  LineageEntries: retains the A.1.1 relation-kind label; availability, mention, method application, performed Work, role assignment, and use-claim readings remain separate and are not aliases
  RefreshCondition: reopen when A.1.1 changes the participant kinds, F.6 performed-under-assignment prerequisite, actual-use predicate, actor derivation, maximal-continuous-use identity, FPFCoreReferenceScheme, the current F.17 cell or row, or the public receiving use
```

```text
NameCard:
  NameCardId: NC-MODEL-EXPRESSION-COHERENCE-RELATION
  GovernedValueRef: ModelExpressionCoherenceRelation
  GovernedValueKindRef: U.Kind
  GoverningPatternRef: A.1.1
  ReferenceScheme: FPFCoreReferenceScheme
  ClaimContent: NC-MODEL-EXPRESSION-COHERENCE-RELATION.ClaimGraph — complete C.2.1 U.ClaimGraph constituted by all identity-bearing naming-settlement claims designated below
  LocalSenseCellRef: SenseCell.ModelExpressionCoherenceRelation.FPFCore.2026-07-25
  LocalSenseBasisRelationRef: LocalSenseBasisRelation.ModelExpressionCoherenceRelation.FPFCore.2026-07-25
  TechLabel: ModelExpressionCoherenceRelation
  PlainLabel: this model content and this expression content satisfy this declared coherence criterion under this comparison scheme
  CandidateSet: relation-kind heads {ModelExpressionCoherenceRelation, ModelConformanceRelation, ModelImplementationRelation, ModelExpressionAlignmentRelation}; predicate-or-assessment heads {ModelExpressionCoherencePredicate, ModelExpressionCoherenceAssessment}
  CandidateCoverage: direct fixed-content relation; conformance neighbour; implementation or realization neighbour; weaker alignment neighbour; local predicate-value neighbour; evaluation or result neighbour; no plausible live head family remains untested
  RejectedCandidates: ModelConformanceRelation invites compliance or status readings and hides the declared criterion and permitted loss; ModelImplementationRelation suggests realization, production, or causation; ModelExpressionAlignmentRelation is weaker than the declared Boolean condition; ModelExpressionCoherencePredicate names the five-part criterion participant; ModelExpressionCoherenceAssessment names evaluation Work or a result episteme
  SelectionRationale: the Tech label names the participant-determined direct relation over one model episteme, expression episteme, admitted five-part predicate value, and comparison scheme; the Plain sentence exposes the truth test after either the same-scheme branch or the predicate-declared bridged branch is established, while maintenance, transformation, evaluation, result, evidence, and assertion remain separate
  PublicRowStatus: current
  UnifiedTermRowRef: UTS.ModelExpressionCoherenceRelation.FPFCore.2026-07-25
  LineageEntries: retains the A.1.1 relation-kind label; earlier maintenance-alignment and implementation wording is narrowed to separate Work, transformation, evaluation, result, evidence, and assertion objects
  RefreshCondition: reopen when A.1.1 changes the participant kinds, five-part predicate-value membership, same-scheme or bridged-comparison branch, permitted-loss rule, participant-determined identity, FPFCoreReferenceScheme, the current F.17 cell or row, or the public receiving use
```

All four current cards use one `FPFCoreReferenceScheme` cell apiece and therefore add no Bridge or use claim. If a named current use relates different `<ReferenceScheme, LocalSenseClaim>` projections, F.9 separately governs the obtaining Bridge, C.2.1 separately identifies the affirmative bounded-use claim, and A.10 or B.3 separately governs reliance; without that use, no Bridge or use claim is added. For `ModelExpressionCoherenceRelation`, an A.1.1 predicate may name an obtaining Bridge as a prerequisite of its bridged interpretation branch; a receiving assertion or structure selection that relies on that occurrence still needs its own bounded-use claim and reliance path. None of those objects becomes part of a NameCard or public row.

#### F.18:4.3 - Candidate Selection
Do not pick a durable label in one stroke or work toward a fixed candidate count. Build the smallest set that covers at least two live head-term families and every plausible neighbouring-object reading that could change the decision. Stop when each live family has a representative and no untested plausible alternative could overturn the selection. If a deadline forces closure while a plausible family or alternative remains untested, record that exception in `CandidateCoverage` and make it part of `RefreshCondition`.

Judge candidates on:

- semantic fidelity: does the label preserve the governed value without adding or losing required conditions?
- reader ergonomics: can the intended reader recognize, say, and remember it in the current situation?
- morphology fit: does the word shape fit the kind being named, for example role value, method, work, description, relation, slot, characteristic, or status value?
- alias risk: will a careful reader import a wrong sense from nearby FPF patterns or external practice?

Use these as ordinal comparisons. Do not average them into one score. If a Pareto-front or quality-diversity method is used, the dimensions and dominance rule must be visible on the card.

One candidate can win even when it is not perfect, but the `SelectionRationale` must say what it buys, what risk remains, and why the covered set is sufficient for this use.

#### F.18:4.4 - Public Term Rows

A durable local name needs no row. When public, Core-facing, durable-across-context, or cross-context reuse is current, test the then-current F.17 entry with the exact objects already recovered here. Public or durable reuse alone creates no Bridge. The entry must accept separate references to the governed value and its kind, direct pattern, NameCard episteme, selected Tech and Plain designations, effective by-value reference scheme, exact F.17 scheme-based SenseCell, any separate local-sense basis relation, and any actual F.9 Bridge. When the row use relates different `<ReferenceScheme, LocalSenseClaim>` projections, its rationale or notes must separately cite the affirmative C.2.1 claim for the row's exact action, direction, rule, and tolerance and that claim's current A.10 or B.3 reliance. Its result must return one row for one naming decision with the supported and blocked citation uses visible. If it cannot, keep the durable name and NameCard local and mark the public row pending. Do not repair or emulate the missing row inside F.18.

When that gate passes, keep these positions distinct:

- `GovernedValueRef`: the exact already-governed value;
- `GovernedValueKindRef`: its exact kind, never an alternative to the value reference;
- direct governing pattern;
- NameCard episteme and selected designation expressions;
- exact local-sense and basis-relation references;
- any actual Bridge occurrence;
- for reuse between different semantic-context projections, the separate affirmative C.2.1 claim about that Bridge and its current A.10 or B.3 reliance, cited in the row rationale or notes rather than absorbed into the NameCard;
- the row or row episteme, its edition, supported citation use, blocked use, and currentness condition.

The row is neither the governed value nor an agent of publication. When availability is needed, an `E.24.PUB` `EpistemePublicationRelation` occurrence makes the exact row-episteme edition available to a declared audience for a bounded use through a distinct publication form and presentation carrier. The form does not publish itself, and the row's currentness claim or relation remains separate from the availability occurrence.

A row for `ReviewerRole` points to the role value and its selected names; it neither creates the role nor makes an assignment obtain. A row for `EvidenceUseRelation` points to the admitted relation kind or other exact governed object; it does not make an episteme into a role or make the relation obtain. A row for `SlotKind` or `EndpointSlot` carries or designates selected vocabulary only after the exact slot object is governed; it neither makes that row edition available nor creates a generic interface ontology.

