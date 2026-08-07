---
chunk_kind: "child"
pattern_id: "G.5"
pattern_title: "Multi‑Method Dispatcher and MethodFamily Registry"
section_id: "G.5:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/G.5/G.5__011_solution.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "G.5 — Multi‑Method Dispatcher and MethodFamily Registry"
  - "G.5:4 — Solution"
line_start: 100302
line_end: 100770
dependencies:
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.23"
  - "C.24"
  - "C.32.P2S"
  - "C.35"
  - "G.0"
  - "G.2"
  - "G.2-G.4"
  - "G.5"
  - "G.6"
  - "G.9-G.11"
  - "G.Core"
keywords:
  - "RankedShortlist"
  - "SelectorOutcomeKind"
  - "Shortlist"
  - "ShortlistId"
  - "SpecialistHandoff"
  - "abstain/escalation result"
  - "are forbidden in registry"
  - "assurance"
  - "basis pins"
  - "dispatcher"
  - "eligibility"
  - "generator-family registry"
  - "in core registry and eligibility fields"
  - "method-family registry"
  - "no hidden scalar winner"
  - "or selector‑kernel obligations (E.5.*)"
  - "selected-set publication"
  - "set-result outcome"
  - "tool choices are outside the core"
---

### G.5:4 - Solution
#### G.5:4.6a - Causal method dispatch declarations

Method selection involving causal methods must declare whether a compared method is an observational predictor, an intervention optimizer, a counterfactual strategy, a causal fairness estimator, a causal-RL policy, or a simulation-only method.

Optional `MethodFamily.causalUseDispatchSpec?`:

```text
MethodFamily.causalUseDispatchSpec? {
  causalUseQuestionRef?: CausalUseQuestionRef
  targetCausalityLadderRung: CausalityLadderRung
  causalUseClaimKind: CausalUseClaimKind
  causalActionPolicyClass?: CausalActionPolicyClass
  causalEvidenceSupportBasis?: CausalEvidenceSupportBasis
  causalUseSupportRecordRef?: CausalUseSupportRecordRef
  causalUseSupportVerdict?: CausalUseSupportVerdict
  causalMethodUseClassification:
    observationalPredictor |
    interventionOptimizer |
    counterfactualStrategy |
    causalFairnessEstimator |
    causalRLPolicy |
    simulationOnlyMethod
  supportedUse: CausalUseSupportStatement
  unsupportedUse: CausalUseUnsupportedStatement
}
```

`CausalUseQuestionRef` is a local reference to the causal-use question governed by the causal, evidence, intervention, or simulation pattern current for the case. It is not admitted here as a durable root U-kind.

`causalMethodUseClassification` is a selector-facing method-use classification, not a `U.Role`, role assignment, responsibility, or actor position. `simulationOnlyMethod` maps to `CausalEvidenceSupportBasis = simulationOnlyCounterfactualOutputBasis`, bounded simulation-supported use, and unsupported intervention-effect or realized-counterfactual-sample use unless another `C.28` support basis is cited.

What changes in practice: a selector must not compare "methods that improve outcome" unless each causal method declares the causality-ladder rung, causal method-use classification, and `C.28` support record and verdict when causal-use support is being consumed.

What this does not authorize: `G.5` does not identify causal effects, decide fairness, certify off-policy causal evaluation, or compare cross-rung causal methods as one undifferentiated improvement set; it keeps method dispatch and selected-set publication while `C.28` governs causal-use support.

#### G.5:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; Default Governing Definition Index citation)

**GCoreLinkageManifest (normative; size-controlled via profiles and sets).**
Effective obligations, pins, and triggers are computed by union expansion of the referenced ids (per `G.Core:4.2.1`). Profile and set expansion is combined with explicit deltas; `Nil‑elision` applies.

* `CoreConformanceProfileIds :=`

  * `GCoreConformanceProfileId.PartG.AuthoringBase`
  * `GCoreConformanceProfileId.PartG.TriStateGuard`
  * `GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted`
  * `GCoreConformanceProfileId.PartG.ShippingBoundary`
* `CorePinSetIds :=`

  * `GCorePinSetId.PartG.AuthoringMinimal`
  * `GCorePinSetId.PartG.CrossingVisibilityPins` *(crossing‑aware use; pins from this set may be intentionally strengthened (optional→required) via `CorePinsRequired`)*
* `CorePinsRequired :=` *(delta over PinSets; pins and refs are id-only; prefer strengthening optional-to-required over restating pins already covered by PinSets)*

  * `TaskSignatureRef` *(see `G.5:4.2`, S2)*
  * `MethodFamilyId[]` *(registry keys in scope)*
  * `MethodRef[]` *(exact A.3.1 Methods resolved from every method-bearing registry row in scope)*
  * `SelectedStructureRef[]?` *(exact independently selected A.22 Structures consumed only when their organization changes this selector use)*

  * `GeneratorFamilyId[]?` *(when generator families are in scope)*
  * `PathId[]` *(audit citations for “why” and for evidence)*
  * `PathSliceId[]` *(audit citations for “why” and for evidence)*
  * `UTSRowId[]` *(published identities for selected families, registered families, and selector policy records)*
  * `FailureBehaviorPolicyId?` *(only when degrade or abstain behavior is explicitly policy‑bound)*
  * `SoSLogBranchId?` *(only when degrade or abstain behavior is explicitly policy‑bound)*
* `DefaultsConsumed :=`

  * `DefaultId.GammaFoldForR_eff`
  * `DefaultId.PortfolioMode`
  * `DefaultId.DominanceRegime`
* `RSCRTriggerSetIds :=`

  * `GCoreTriggerSetId.RefreshOrchestration`
    *(payload pins: `TaskSignatureRef`, `CGSpecRef.edition`, `CNSpecRef.edition`, `MethodFamilyId[]`, `GeneratorFamilyId[]?`, `AcceptanceClauseId[]?`, `SoSLogBranchId?`, `FailureBehaviorPolicyId?`, `DescriptorMapRef.edition?`, `DistanceDefRef.edition?`, `TransferRulesRef.edition?`, `InsertionPolicyRef?`, `PathId`, `PathSliceId`, `SCRId`, `DRRId`, `RSCRTestId[]`)*

#### G.5:4.2 - Dispatcher and Registry object set (notation‑independent)

G.5 defines the **object-set components** below. Their purpose is to make dispatch **possible and auditable** without embedding any method-family semantics in the selector kernel.

**S1 — `MethodFamily Registry` (design‑time; per CG‑Frame).**
A registry row represents *a family*, not a single implementation. Minimal fields (conceptual, notationally independent):

* `Identity`: `MethodFamilyId`, `ContextId`, lineage and Tradition notes, `UTSRowId` (twin labels where applicable).
* `Exact method members`: non-empty `MethodRef[]`, each resolving to one `U.Method` already admitted under A.3.1.
* `Grouping basis`: exact claim, criterion, or direct relation reference that justifies this row's grouping for the current selector use; if no ontic family or membership relation is directly governed, the basis is explicitly project-local and creates none.

* `EligibilityStandardRef`: a typed predicate record (tri‑state per `G.Core`), expressed in CHR and CAL terms and pinned to the relevant editions.
* `AssuranceProfileRef`: evidence‑lane expectations and assurance-lane pins (SCR‑addressable).
* `AdmissibilityBindings`: explicit references to the **single** governance card and admissibility gate (`CNSpecRef`, `CGSpecRef`) and to any required admissibility constraints, for example scale and unit admissibility via CSLC.
* `EvidencePins`: citations to `G.6` (`PathId`, `PathSliceId`) for claims or guarantees where such claims are asserted.
* `CrossingAllowance`: references to the exact F.17 endpoint senses, one obtaining F.9 Bridge, the separate C.2.1 bounded-use proposition, and the current A.10 or B.3 reliance basis, plus CL or observed-loss evidence when material, **only** if cross-semantic-context operation is claimed. These are audit references; the field makes none of the referenced facts obtain.

For an actual crossing, first resolve both exact F.17 `SchemeSenseCell` endpoints and establish the two-participant F.9 Bridge under its own predicate profile. Then identify a separate C.2.1 episteme whose exact `EntityOfConcern` is that Bridge and whose ClaimGraph states the proposed use `u`, direction `d`, use-specific rule `r`, tolerated loss `t`, and polarity. For ordinary reliance require the matching current A.10 evidence-provenance relation and local `RelianceDisposition`; when an assurance claim or B.3 material-reliance threshold is current, use B.3's separate assurance branch instead. Observed loss and CL are evidence, defeater or assurance-policy material, not Bridge participants or permission. Authorization and the actual `Select` application remain with their direct owners. A Bridge id, `CrossingAllowance`, registry row, policy pin, `CrossingBundle`, DRR or SCR entry cannot substitute for any step.

* `PolicyHooksRef?`: optional pointers to policy records (not defined here; wired via Extensions).

Here “a registry row represents a family” means that the row is the auditable selector-facing record for one declared grouping. It does not identify the grouped Methods, make a membership relation obtain, or turn a common label, shared description, lineage note, eligibility rule, maturity card, evidence record, or policy into a method-family fact. Changing a row or its `MethodFamilyId` changes the registry artifact; it changes a Method or a separately governed family relation only when that object's direct identity or obtaining rule independently says so.


**S1′ — `GeneratorFamily Registry` (design‑time; optional; per CG‑Frame).**
A registry row for families that generate tasks and environments, and may co-evolve solver families. G.5 carries the registry-entry shape, not the generator semantics:

* `Identity`: `GeneratorFamilyId`, `ContextId`, `UTSRowId`.
* `GeneratorSignatureRef`: conceptual input and output semantics plus budget semantics.
* `EnvironmentValidityRegionRef?`: pinned constraints for generated environments or tasks.
* `TransferRulesRef.edition?`: required when the Open-Ended mode is enabled (semantics come from the cited extension refs).
* `CouplerRefs?`: which `MethodFamilyId[]` can be coupled with this generator family.

**S2 — `TaskSignature` record (design‑time and run‑time).**
A minimal typed record the dispatcher consumes. Its function is **pinning and auditability**, not over-specification. It must be CHR and CAL typed and provenance-aware.
G.5 treats `TaskSignatureRef` as an input record; it does not define CHR or CAL semantics.

**S3 — `Selection kernel boundary` (run‑time; policy‑governed).**
A notation‑independent selector that:

* consumes `TaskSignatureRef`, registry entries, and pinned spec refs,
* applies eligibility and assurance gating (tri-state),
* computes an admissible (possibly partial) order,
* returns one declared selector outcome: most often one set-result outcome such as `Shortlist` or `RankedShortlist`, but sometimes one `SpecialistHandoff`, one other narrowed handoff, one abstain outcome, or one escalation outcome (per `DefaultId.PortfolioMode` and explicit overrides),
* emits audit records with pins addressable by DRR and SCR records.

For every `MethodFamilyId` consumed here, dereference the row to its exact A.3.1 `MethodRef[]` and grouping basis before admitting the candidate. The selector may compare or return registry rows as auditable selector-facing addresses, but row selection neither creates its Methods nor proves that every listed Method belongs, is admissible, is selected, or will be enacted. An unresolved Method reference or missing grouping basis blocks that row's method-bearing use; it is not repaired by a label, description, UTS identity, policy, or evidence pin.

When a selector consumes an organization among Methods, cite an exact `SelectedStructureRef` only after A.22 has independently identified the `U.Structure` from exact constituents, exact already-obtaining relation occurrences, applied constraints, and one named use frame. G.5 neither supplies those discriminators nor selects the Structure by listing it. If the organization instead constitutes one composite Method, consume the exact A.3.1 Method only after B.1.5 has qualified that candidate from its independent parts and whole-forming basis.

S3 states reusable selector behavior. It does not itself perform selection. For an actual selector use, identify the admitted `U.System` that performed the dated A.15.1 Work under an exact obtaining assignment, the enacted Method, and the actual A.6.1 `Select` application whose effective argument bindings and `SelectionSlot` binding carry the by-value selected set under A.19.SelectorMechanism. The declaration, planned pins, registry rows, policy and `CandidateSet` type create none of those occurrence-side facts.




**S3.A — `TaskFamilySpecializationProfile@Context` (run‑time; conditional).**
When the real selector question is acquisition of usable specialization on a declared task family, the selector may publish one `TaskFamilySpecializationProfile@Context` for each candidate, one `SpecialistHandoff`, or one narrowed handoff plan. Here `profile` means one selector-time comparison record for bounded specialization, not a new U-kind and not a generic narrative profile. `G.5` carries this selector-time specialization question here; it does not re-govern the adaptation-signature field vocabulary from `C.22.1`.

The profile should therefore cite one `AdaptationSignatureRef` or equivalent pinned field set carrying the declared `TaskFamilyRef` or `TaskSignature`, the work-measure threshold target, prior exposure declaration, time-to-threshold, budget-to-threshold, post-threshold efficiency when relevant, any declared transfer or retention claim, any downside cost or downside on adjacent tasks, and any specialization-entry baseline, specialization-entry evidence, or stepping-stone evidence item that materially affects comparison.

Admission rule for `SpecialistHandoff`: use that handoff kind only when the truthful published result is one heterogeneous handoff bundle whose members occupy different specialization positions that still need to travel together. Do not use it when one ordinary `Shortlist`, `RankedShortlist`, `ExplorationArchive`, or another narrower named result kind already states the result more precisely.

When the declared task family is heterogeneous, the selector may return one `SpecialistHandoff`, one other narrowed handoff plan, or one small admissible set that preserves rival specialists rather than collapsing them into a fake single winner. Low-human-overlap candidates remain admissible only when the profile, evidence basis, and policy constraints are explicit.

**S4 — `Composition and fallbacks` templates (design‑time).**
A library of composition shapes—`preconditioner -> solver -> verifier`, cascades, and meta-selectors—remains available **as design-time templates**, admissibility-checked and pinned. A template is a description or policy-bound arrangement for possible composition; its existence, diagram order, registry placement, or selection does not create a Method, `methodPartOf` occurrence, obtaining relation, or selected Structure.

If exact A.3.1 Methods, exact B.1.5 `methodPartOf` occurrences, all other required whole-forming claims and constraints, whole semantics, interface boundary, and reidentification rule qualify one already identified candidate as a composite `U.Method`, consume that exact Method through the B.1.5 branch. If independently identified Methods and already-obtaining relations are instead organized for one use without constituting one Method, consume an independently selected A.22 `U.Structure` only after its exact constituents, selected obtaining relation occurrences, applied constraints, and named selection-use frame are present. `MethodRelationStructure` may remain a local readable designator for that actually selected Structure; it is not a U-kind, relation kind, Method holon, registry-row identity, or generic `@BoundedContext` object.

A C.2.1 episteme may describe either governed object. A.3.2 applies only when the episteme's exact `EntityOfConcern` is one already admitted Method and its claims substantively describe that Method; an episteme whose exact concern is the selected Structure is not thereby a `U.MethodDescription`. Concrete strategy semantics stay in the referenced method families; G.5 only carries the composition template, selector relation, registry row, exact consumed Method or Structure reference, or selected-set result. None of those G.5 artifacts supplies the B.1.5 or A.22 construction facts.

Algebraic, graph, matrix, embedding, or neural selector notation remains a mathematical or representation lens when that representation is current; use C.29 for its correspondence and preserved-or-lost structure rather than reading notation as composition or selection.


**S5 — `Publication and telemetry` record boundary (run-time).**
A standard publication boundary publishes:

* `DRR` (decision rationale) and `SCR` (evidence and confidence citation) with explicit pins,
* declared selector and selected-set records,
* telemetry pins to refresh orchestration (`G.11`), without governing orchestration.

S5 governs the selector-facing record boundary, not truth or actuality by record existence. A DRR, SCR, selected-set record, shortlist id, telemetry event, refresh cue, policy pin, or result label does not create dated Work, an actual operation application, the selected-set binding, a domain result, an evidence-provenance relation, assurance, authorization, or publication availability. Persist a selector-result claim as its own C.2.1 episteme when another use must rely on it; connect evidence through A.10, assurance through B.3, authorization through its direct governor, and actual availability through E.24.PUB only when each relation independently obtains.


When the current publication question is selected-set publication rather than one generic registry trace, `Shortlist` is the public selected-set label, `RankedShortlist` is the ordered specialization when order materially belongs to the published result, `ShortlistId` is the emitted public identity, and `ChoiceSet` stays one mathematical gloss rather than the public selected-set label.

**S6 — `Governance and evolution` declaration boundary (design-time).**
Versioning, deprecation, and registry evolution discipline (UTS publication; continuity), without minting new Part‑G‑wide types.

#### G.5:4.3 - Selector head and narrower selector families

Selection and dispatch stay one generic selector head. Narrower selector families may refine it, but they do not redefine the universal invariants pinned through `G.Core`, do not add hidden mandatory inputs beyond pinned policy or edition refs, and do not mutate SlotKinds.

Method- and generator-specific pressures such as `QD` archives, open-ended declared sets, explore and exploit lenses, or preference comparators do not become part of the selector head. They arrive only through explicit extension declarations and the pins those extensions require.

#### G.5:4.4 - Selector Relation Fields

| Selector relation                 | Consumes                                                                                                                                                     | Produces                                                                                                                                                                                                                                                   |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **G.5‑1 RegisterFamily**          | `SoTA` family card (from `G.2`), non-empty exact already admitted A.3.1 `MethodRef[]`, exact independently governed classification or membership-relation ref or explicit project-local grouping criterion, CHR and CAL pins (from `G.3` and `G.4`), `CNSpecRef.edition`, `CGSpecRef.edition`, `ContextId` | A `MethodFamily` registry row (`MethodFamilyId`, `MethodRef[]`, `GroupingBasisRefOrCriterion`, `EligibilityStandardRef`, `AssuranceProfileRef`, `UTSRowId`, pinned refs). The G.2 card and CHR/CAL/spec/context pins are metadata or evidence inputs and cannot supply either the exact Methods or the grouping fact. |
| **G.5‑2 RegisterGeneratorFamily** | `SoTA` generator family cards (from `G.2`), `ContextId`, pinned refs (including `TransferRulesRef.edition` when applicable)                                  | A `GeneratorFamily` registry row (`GeneratorFamilyId`, `GeneratorSignatureRef`, `UTSRowId`, pinned refs)                                                                                                                                                   |
| **G.5-3 Select**                  | `TaskSignatureRef`, `MethodFamilyId[]` in scope whose rows dereference to non-empty exact A.3.1 `MethodRef[]` and exact grouping bases, pinned `CNSpecRef` and `CGSpecRef` editions, policy refs if any, audit citation pins (`PathId` and `PathSliceId`) | `CandidateSet` (set-returning), declared selector result with `PortfolioMode` recorded, `DRR` and `SCR` pins; if no admissible candidate exists: return `CandidateSet = EMPTY` plus an escalation hint (`ActionHint`) and the pins required to plan next steps (P2W split applies) |
| **G.5-4 Compose**                 | `CandidateSet`, composition template refs, pinned admissibility constraints                                                                                       | Composite strategy template (template-level; admissibility-checked; pinned)                                                                                                                                                                                      |
| **G.5‑5 Telemetry**               | run outcomes, citations, and policy or edition pins                                                                                                               | refresh cues (typed RSCR causes and payload pins), parity deltas (if parity harness is in use), telemetry pins (selector‑side; orchestration governing definition is `G.11`)                                                                                              |

`RegisterFamily` produces only the registry row described in S1. It does not produce any A.3.1 Method or independently governed membership fact. `Select` may address candidates through those rows only after their exact Methods and grouping bases resolve; its returned candidate or selected-set value does not retroactively ground a row member.

`Compose` produces only the pinned template named in its output column. It neither qualifies one composite Method under B.1.5 nor selects one A.22 Structure. When a later selector use consumes either governed object, the exact Method or Structure reference is an independently grounded input rather than a result inferred from this template.



#### G.5:4.4a - Worked selector slice

- A catalyst-search team is choosing among three method families for the same declared `TaskSignature` and `C.22.1` adaptation signature.
- The shared profile pins one work-measure threshold target, one freshness window, one prior-exposure declaration, and one adaptation budget. One family reaches threshold quickly but carries high downside on adjacent tasks. One family is slower but transfers cleanly. One family never clears `MinimalEvidence` and must abstain.
- An admissible `G.5` result therefore publishes a set-return shortlist or a narrowed handoff plan, with DRR and SCR records citing why the third family was excluded and why the first two remain non-dominated. The selector does not invent one scalar winner and does not hide the specialization profile in auxiliary side notes.
- If the project also claims that this selection actually occurred, it separately identifies the acting system, dated selection Work, actual `Select` application, effective candidate and criteria bindings, and the `SelectionSlot` binding. A persisted shortlist assertion is a separate C.2.1 episteme; its DRR or SCR references do not by themselves prove the exclusion facts, warrant the result, authorize downstream action, or make that episteme available to an audience.

- When one upstream `C.19` pass has already narrowed the live pool to one internal retained subset over registered families, `G.5` may publish that result as one `Shortlist` with one `ShortlistId` and explicit basis pins only when selector-facing publication is now the question. Until that emission occurs, the internal retained subset is not yet one public shortlist result.
- When one upstream `C.11` pass has already fixed one local choice over one declared source set, or one `C.24` pass has already produced one enactment-facing narrowed handoff, `G.5` may publish the selected-set or narrowed-handoff result only when selector-facing publication is now the question. Until this `G.5` emission occurs, the `ChoiceResult`, `CallPlan`, or `CheckpointReturn` is not itself one public `Shortlist`, `RankedShortlist`, or `ShortlistId`-bearing result.

#### G.5:4.4b - Published selected-set result and closure rule

A finished `G.5` pass should publish one explicit selected-set result from the dispatcher and registry question rather than one selector trace that leaves the public result implicit.

Publication here is the closure record for selector work over registered families. It does not replace registry maintenance, dispatcher comparison rules, or the upstream pool-policy and local-choice pattern authorities that supplied the retained members.

The admissible selector outcome families here are:

- `SelectorOutcomeKind = SetResultOutcome`, with `SetResultFamily = Shortlist` when one retained set is published without one material internal order and `SetResultFamily = RankedShortlist` when ordering materially belongs to the result;
- `SelectorOutcomeKind = HandoffOutcome`, with `HandoffKind = SpecialistHandoff` or one other narrowed handoff plan when heterogeneity is the truthful downstream result;
- `SelectorOutcomeKind = AbstainOutcome` when no admissible candidate exists and the truthful result is one abstain;
- `SelectorOutcomeKind = EscalationOutcome` when no admissible candidate exists and the truthful result is one escalation.

`SetResultFamily` belongs only inside `SetResultOutcome`. `Shortlist` and `RankedShortlist` are public selector results over registered rows. They are not merely one upstream internal retained subset copied forward under one prettier label. `G.5` is the governing pattern that turns selector state into one public result with one explicit outcome kind, one explicit selected-set label when applicable, one explicit member set or handoff content, and one explicit basis-pin set.

A publication result should state at least these fields:

- the selector outcome kind being emitted;
- the public selected-set label when the outcome is one set-result outcome;
- retained members, or the narrowed handoff content, or the abstain or escalation condition;
- ordering status when ordering matters;
- basis pins and policy pins sufficient to justify the result;
- one explicit next downstream use boundary when the result is a handoff rather than one terminal publication.

A compact result may therefore look like:

```text
SelectorOutcome(
  selectorOutcomeKind = SetResultOutcome,
  setResultFamily = Shortlist,
  members = [family_A, family_C],
  shortlistId = shortlist_17,
  ordering = unordered,
  basisPins = [pathSlice_41, scr_22],
  nextUse = downstream_comparison
)
```

or:

```text
SelectorOutcome(
  selectorOutcomeKind = SetResultOutcome,
  setResultFamily = RankedShortlist,
  members = [family_B, family_A],
  shortlistId = shortlist_23,
  ordering = ranked,
  basisPins = [pathSlice_77, scr_44],
  nextUse = specialist_handoff
)
```

Close as `SelectorOutcomeKind = SetResultOutcome` with `SetResultFamily = Shortlist` when several retained members survive admissibly but no public internal order belongs to the result. Close as `SelectorOutcomeKind = SetResultOutcome` with `SetResultFamily = RankedShortlist` when order materially belongs to the published result. Close as `SelectorOutcomeKind = HandoffOutcome` with `HandoffKind = SpecialistHandoff` or one other narrowed handoff when heterogeneity itself is the truthful downstream result. Close as `SelectorOutcomeKind = AbstainOutcome` or `EscalationOutcome` when no admissible candidate exists under the pinned constraints.

If the publication still does not state what public result was emitted, who remained in it, whether order belongs to it, and which pins justify it, then the selector has not yet published one finished `G.5` result.

#### G.5:4.4bb - Public labels over archive, front, and style source sets

When a selector-facing publication uses labels such as `Shortlist`, `RankedShortlist`, declared `ExplorationArchive`, `Archive`, `Front`, `Q-front`, `SpecialistHandoff`, `StyleShortlist`, `TraditionShortlist`, abstain, or escalation, the G.5 question is the public selector outcome being emitted.

```text
SelectedSetPublicationLabelLine@Context:
  selectorOutcomeKind:
  setResultFamily?:
  sourceSetFamily:
  publicSelectedSetLabel?:
  derivedViewKind?:
  basePaletteOrArchiveRef?:
  membersOrHandoff:
  ordering:
  basisPins:
  nextUse:
```

`sourceSetFamily` may name a declared `Front`, `Q-front`, `ExplorationArchive`, `Archive`, current pool subset, or derived tradition view. `publicSelectedSetLabel` names the emitted selected-set label, normally `Shortlist` or `RankedShortlist`, and may use a domain label such as `StyleShortlist` or `TraditionShortlist` only when the term bridge is already clear. G.5 does not create the archive, compute the comparison, govern the pool policy, decide the cultural-evolution case, or repair the term bridge. Use `C.18`, `A.19.CPM`, `C.19`, `C.36`, `F.17`, `F.18`, and `F.9` for those relations.

#### G.5:4.4c - Publication quick card



The smallest useful `G.5` publication card usually states:

- `selectorOutcomeKind = SetResultOutcome | HandoffOutcome | AbstainOutcome | EscalationOutcome`
- `setResultFamily = Shortlist | RankedShortlist` when `selectorOutcomeKind = SetResultOutcome`
- `handoffKind = SpecialistHandoff | NarrowedHandoff` when `selectorOutcomeKind = HandoffOutcome`
- `membersOrHandoff = ...`
- `ordering = ranked | unordered | not applicable`
- `publicId = ...` when one public identity is emitted
- `basisPins = ...`
- `nextUse = downstream comparison | specialist handoff | escalation | none`

A short conforming card may therefore read:

```text
selectorOutcomeKind = SetResultOutcome
setResultFamily = Shortlist
members = [family_A, family_C]
ordering = unordered
shortlistId = shortlist_17
basisPins = [pathSlice_41, scr_22]
nextUse = downstream_comparison
```

If the card does not already state what was published, who survived, whether order belongs to the result, and which pins justify it, the publication is still unfinished `G.5` work.

#### G.5:4.4ca - Derived tradition-view publication stays derived over one declared palette

- If selector work consumes one declared source set such as `Front`, `Archive`, or one source-set composition through one derived tradition view such as `TraditionFront` or `TraditionArchive`, treat that derived view as one interpretation view over one declared `SoTAPaletteDescription`, not as the default meaning of `Tradition` or of the palette itself.
- When `SelectorOutcomeKind = SetResultOutcome`, the public selected-set label still closes as `Shortlist` or `RankedShortlist`; when `SelectorOutcomeKind = HandoffOutcome`, the result closes as one `SpecialistHandoff` or one other narrowed handoff. The derived tradition view disciplines the source, not the emitted outcome family.
- When such a derived tradition view is active, publish `SourceSetFamily`, use `DerivedViewKind` when the distinction matters to interpretation or later shipping, use `SourceSetComposition` only when several source-set families were genuinely composed, and keep `BasePaletteRef=SoTAPaletteDescriptionId` recoverable alongside the emitted result.
- If the derivation depends on one declared `Q` or one reachability or coverage rule, cite that declared basis directly in DRR and SCR records or equivalent basis pins rather than leaving the derivation implicit.
- If no derived tradition view is active, stay with the declared palette, front, archive, or shortlist families already named by the selector record.

#### G.5:4.4d - Worked publication closure slice

Three short contrasts keep the publication closure rule practical.

**Several survivors, no public order belongs to the result.**
When the selector has retained more than one admissible family but no downstream public order belongs to the published result, `G.5` should close as one `Shortlist` over the registered surviving rows:

```text
Shortlist(
  members = [family_A, family_C],
  shortlistId = shortlist_17,
  ordering = unordered,
  basisPins = [pathSlice_41, scr_22],
  nextUse = downstream_comparison
)
```

**Order now materially belongs to the published result.**
When one ordered public handoff is required, `G.5` should say so directly instead of leaving order implicit:

```text
RankedShortlist(
  members = [family_B, family_A],
  shortlistId = shortlist_23,
  ordering = ranked,
  basisPins = [pathSlice_77, scr_44],
  nextUse = specialist_handoff
)
```

**No admissible candidate survives.**
When no family clears the pinned admissibility or evidence gates, `G.5` should close as one abstain or escalation result rather than as one empty shortlist pretending to be progress:

```text
Abstain(
  blockingPins = [cg_min_evidence, crossing_bundle_missing],
  basisPins = [pathSlice_91, scr_61],
  nextUse = escalation
)
```

The practical distinction is simple: an internal retained subset can remain real upstream without yet being one public selector result. `G.5` begins only when that selector-facing publication question starts, and it closes only after the declared outcome kind, any applicable public selected-set label, surviving members or handoff content, and basis pins are emitted directly.

Most selector-side use can stop after `G.5:4.4d`. The blocks below are extension declarations used only when the corresponding mode is actually active.

All blocks below are extension declarations: they declare `Uses` and required pins, but do not redefine semantics already defined in the referenced patterns.

**GPatternExtension block: `G.5:Ext.EELog`**

* `PatternScopeId`: `G.5:Ext.EELog`
* `GPatternExtensionId`: `EELog`
* `GPatternExtensionKind`: `MethodSpecific`
* `GoverningPatternId`: `C.19`
* `Uses`: `{C.19}`
* `⊑` and `⊑⁺`: `∅`
* Required pins, edition pins, and policy pins (minimum):

  * `EELensPolicyRef` *(or equivalent lens or policy id carried by `C.19`)*
  * `RiskBudgetRef?`
  * `ProbeAccountingRef?`
  * `FailureBehaviorPolicyId?` *(if degrade behavior is governed by policy)*
* `RSCRTriggerKindIds`: `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* `Notes (extension discipline; semantics cited):`

  * This block activates exploration and exploitation-governed dispatch.
  * Post‑2015 examples that typically land here: modern bandit‑style or Bayesian selection under explicit risk budgets; adaptive evaluation and probing regimes; safe‑exploration variants where “abstain” or “degrade” is policy-bound.

**GPatternExtension block: `G.5:Ext.SoSLOG`**

* `PatternScopeId`: `G.5:Ext.SoSLOG`
* `GPatternExtensionId`: `SoSLOG`
* `GPatternExtensionKind`: `MethodSpecific`
* `GoverningPatternId`: `C.23`
* `Uses`: `{C.23}`
* `⊑` and `⊑⁺`: `∅`
* Required pins, edition pins, and policy pins (minimum):

  * `SoSLogRuleId[]`
  * `SoSLogBranchId[]` *(including escalation branches, if used)*
  * `FailureBehaviorPolicyId` *(if degrade behavior is made explicit)*
  * `MaturityRungId[]?` *(when maturity ladders are used as gates; semantics come from `C.23`)*
  * `AdmissibilityLedgerRef?` *(when selector consumes admissibility rows rather than recomputing thresholds)*
* `RSCRTriggerKindIds`: `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.EvidencePathOrSourceRelationEdit}`
* `Notes (extension discipline; semantics cited):`

  * This block pins dispatch decisions to explicit rule and branch ids, enabling auditable “why” without inventing a fourth acceptance status.

**GPatternExtension block: `G.5:Ext.NQD`**

* `PatternScopeId`: `G.5:Ext.NQD`
* `GPatternExtensionId`: `NQD`
* `GPatternExtensionKind`: `MethodSpecific`
* `GoverningPatternId`: `C.18`
* `Uses`: `{C.18, C.19}`
* `⊑` and `⊑⁺`: `∅`
* Required pins, edition pins, and policy pins (minimum):

  * `DescriptorMapRef.edition`
  * `DistanceDefRef.edition`
  * `InsertionPolicyRef`
  * `TaskSignatureRef` *(when QD is enabled via TaskSignature flags or traits)*
  * `DHCMethodRef.edition?` *(when diversity and coverage telemetry is pinned to a DHC method)*
* `RSCRTriggerKindIds`: `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* `Notes (extension discipline; semantics cited):`

  * G.5 core remains QD‑agnostic; QD semantics are governed by `C.18`.
  * Post-2015 families that typically use this extension declaration: MAP-Elites-class QD including later archive-centric refinements, CMA-ME-class hybrids, modern illumination and coverage telemetry regimes where admissibility and edition pinning matter.

**GPatternExtension block: `G.5:Ext.OpenEndedFamilyWiring`**

* `PatternScopeId`: `G.5:Ext.OpenEndedFamilyWiring`
* `GPatternExtensionId`: `OpenEndedFamilyWiring`
* `GPatternExtensionKind`: `GeneratorSpecific`
* `GoverningPatternId`: `G.2`
* `Uses`: `{G.2, C.19, C.23}`
* `⊑` and `⊑⁺`: `∅`
* Required pins, edition pins, and policy pins (minimum):

  * `GeneratorFamilyId[]`
  * `TransferRulesRef.edition` *(mandatory when Open‑Ended is enabled)*
  * `EnvironmentValidityRegionRef?`
  * `CoEvoCouplerRef[]?`
  * `SoSLogBranchId[]?` *(when validity of generated tasks is gated by explicit branches)*
* `RSCRTriggerKindIds`: `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* `Notes (extension discipline; semantics cited):`

  * This block enables declared sets of `{Environment, MethodFamily}` pairs without redefining generator semantics in G.5.
  * Post‑2015 examples typically referenced via `G.2` family cards: POET‑class and later open‑ended and co‑evolutionary regimes, including enhanced variants where transfer policies and validity gates must be edition‑pinned.

#### G.5:4.4e - Selector-facing outcome kinds

- `SelectionSlot` returns one selector outcome, not one forced single winner.
- The emitted result should declare its `SelectorOutcomeKind`.
- `SetResultFamily` is required only when `SelectorOutcomeKind = SetResultOutcome`.
- `HandoffKind` is required only when `SelectorOutcomeKind = HandoffOutcome`; `SpecialistHandoff` is one handoff kind, not one set-result family head.
- `Front` names the non-dominated source set under the declared `DominanceSet`.
- `Archive` names the retained exploration archive under the declared retention policy.
- `Shortlist` names the lens-declared selected set emitted from `SelectionSlot`.
- `RankedShortlist` names one ordered specialization of that shortlist result.
- `ShortlistId` is the emitted public token when the shortlist publication must be carried or cited.
- `ChoiceSet` may be used only as the mathematical set gloss for that shortlist when the set object itself is under analysis; it does not replace the public shortlist head.
- `PortfolioMode` states how the selector operated; it does not rename the emitted set result.
- The default `PortfolioMode=Archive` means that an unspecified selector or generator operating mode must preserve retained exploration evidence rather than pretending one current front or selected shortlist has already been emitted. It does not make every returned object an `Archive`, does not override `SetResultFamily`, and does not change the declared `DominanceSet`.
- If one selector consumes both a front and an archive, say so explicitly rather than blurring them into one generic portfolio.
- If one selector consumes one derived tradition view, keep that derived view explicit rather than silently treating it as the default meaning of `Tradition`.
- `SetResultFamily`, `SourceSetFamily`, `SourceSetComposition`, `SubjectKind`, `DerivedViewKind`, `BasePaletteRef`, `PromotionPolicy`, and `RetentionIntent=steppingStone` are declaration fields, refs, or policy pins around the returned outcome; they are not additional emitted set results.
- `SourceSetFamily` names the immediate declared source-set family.
- `SourceSetComposition` is used only when the selector genuinely consumed more than one source-set family such as `Front` and `Archive`.
- If that source set is one derived tradition view, keep the base palette recoverable alongside it.
- `DerivedViewKind` may name which derived tradition view is active when that distinction matters to interpretation or later publication.
- `DerivedViewKind` does not replace `SourceSetFamily`, `SetResultFamily`, or `Shortlist`.
- `BasePaletteRef` is one cited ref or id, not one kind.
- If one selected result comes from one declared source set, publish that `SourceSetFamily` rather than asking the reader to infer it from one mode flag.
- `PromotionPolicy` is required when tie-break or telemetry signals are promoted into dominance.
- The selector may consume one declared source set and one declared choice lens without trying to explain the whole reason why another probe was worth its cost.
- When `CostToProbe`, `ValueOfInformation`, `ValueOfComputation`, `explore_share`, `backstop_confidence`, or sequencing pressures matter, keep them explicit in the surrounding choice doctrine instead of smuggling them into set-result declaration fields.
- Selector-facing results should name the set-result kind, source-set kind, derived-view declaration when needed, the emitted shortlist family, and promotion or default declaration.
- Those selector-facing field values should use controlled tokens, cited ids, or already-declared head labels rather than selector-local prose values.

