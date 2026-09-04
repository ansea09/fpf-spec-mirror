---
chunk_kind: "child"
pattern_id: "G.5"
pattern_title: "Multi‑Method Dispatcher and MethodFamily Registry"
section_id: "G.5:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/G.5/G.5__011_solution.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "G.5 — Multi‑Method Dispatcher and MethodFamily Registry"
  - "G.5:4 — Solution"
line_start: 103523
line_end: 104052
dependencies:
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.23"
  - "C.24"
  - "C.32.P2S"
  - "C.35"
  - "E.17"
  - "E.24.PUB"
  - "E.4.PFR"
  - "G.0"
  - "G.11"
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

When method dispatch compares causal uses, each compared Method declares its causal question/rung and whether it is being used as an observational predictor, intervention optimizer, counterfactual strategy, causal fairness estimator, causal-RL policy, or simulation-only Method.

```text
MethodFamily.causalUseDispatchSpec?:
  causalUseQuestionRef?: CausalUseQuestionRef
  targetCausalityLadderRung: CausalityLadderRung
  causalUseClaimKind: CausalUseClaimKind
  causalActionPolicyClass?: CausalActionPolicyClass
  causalSupportComponentRefs?: CausalSupportComponentRefs
  causalUseSupportResultRef?: CausalUseSupportResultRef
  causalMethodUseClassification:
    observationalPredictor |
    interventionOptimizer |
    counterfactualStrategy |
    causalFairnessEstimator |
    causalRLPolicy |
    simulationOnlyMethod
  supportedUse
  unsupportedUse
```

`CausalUseQuestionRef` identifies the question content used by C.28; it is not a durable root U-kind. `causalMethodUseClassification` describes the Method's proposed selector-facing use and supplies no system-role assignment, responsibility, authority, or causal certification.

A simulation-only Method cites `simulationResultRef` inside its support components and states bounded model use plus unsupported realized/interventional use. G.5 declares the dispatch result; C.28 supplies the causal-support result. A selector may still abstain even when a C.28 result is supported.

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

  * `TaskSignatureRef` *(the C.22 TaskSignature edition; see `G.5:4.2`, S2)*
  * `TaskMapRef?` *(exact G.4 map edition, only when this selection uses G.4 CAL gates)*
  * `MethodFamilyRowRef[]` *(exact `<MethodFamilyId, rowEdition>` values in scope)*
  * `MethodRef[]` *(exact A.3.1 Methods resolved from every method-bearing registry row in scope)*
  * `SelectedStructureRef[]?` *(exact independently selected A.22 Structures consumed only when their organization changes this selector use)*

  * `GeneratorFamilyRowRef[]?` *(exact `<GeneratorFamilyId, rowEdition>` values when generator families are in scope)*
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
    *(payload pins: `TaskSignatureRef`, `TaskMapRef?`, `CGSpecRef.edition`, `CNSpecRef.edition`, `MethodFamilyRowRef[]`, `GeneratorFamilyRowRef[]?`, `AcceptanceClauseId[]?`, `SoSLogBranchId?`, `FailureBehaviorPolicyId?`, `DescriptorMapRef.edition?`, `DistanceDefRef.edition?`, `TransferRulesRef.edition?`, `InsertionPolicyRef?`, `PathId`, `PathSliceId`, `SCRId`, `DRRId`, `RSCRTestId[]`)*

#### G.5:4.2 - Dispatcher and Registry object set (notation‑independent)

G.5 defines the **object-set components** below. Their purpose is to make dispatch **possible and auditable** without embedding any method-family semantics in the selector kernel.

**S1 — `MethodFamily Registry` (design‑time; per CG‑Frame).**
A registry row represents *a family*, not a single implementation. Minimal fields (conceptual, notationally independent):

* `Identity and continuity`: `MethodFamilyId` names the continuing row lineage; `rowEdition` names one immutable edition; `MethodFamilyRowRef := <MethodFamilyId, rowEdition>` designates that edition. Lineage and Tradition notes and `UTSRowId` remain descriptive or publication values.
* `Exact method members`: non-empty `MethodRef[]`, each resolving to one `U.Method` already admitted under A.3.1.
* `Grouping basis`: exact claim, criterion, or direct relation reference that justifies this row's grouping for the current selector use; if no ontic family or membership relation is directly governed, the basis is explicitly project-local and creates none.

One exact row edition fixes its method members, grouping basis, and every selection-changing pin. Changing any of those values creates a new `rowEdition`; retain the `MethodFamilyId` only while the declared grouping remains the same continuing row lineage. Old `MethodFamilyRowRef` values continue to resolve their old editions. Add task, eligibility, policy, scheme, source, `ClaimScope`, validity, or intended-use pins only when they change selection or a named receiver needs them; none replaces the members or grouping basis.

* `EligibilityStandardRef`: a typed predicate record (tri‑state per `G.Core`), expressed in CHR and CAL terms and pinned to the relevant editions.
* `AssuranceProfileRef`: evidence‑lane expectations and assurance-lane pins (SCR‑addressable).
* `AdmissibilityBindings`: explicit references to the **single** governance card and admissibility gate (`CNSpecRef`, `CGSpecRef`) and to any required admissibility constraints, for example scale and unit admissibility via CSLC.
* `EvidencePins`: citations to `G.6` (`PathId`, `PathSliceId`) for claims or guarantees where such claims are asserted.
* `CrossingAllowance`: references to the exact F.17 endpoint senses, one obtaining F.9 Bridge, the separate C.2.1 bounded-use proposition, and the current A.10 or B.3 reliance basis, plus CL or observed-loss evidence when material, **only** when expressions with distinct recovered source-local meanings are actually related for this selector use. These are audit references; the field makes none of the referenced facts obtain.

For an actual crossing, first resolve both exact F.17 `SchemeSenseCell` endpoints and establish the two-participant F.9 Bridge under its own predicate profile. Then identify a separate C.2.1 episteme whose exact `EntityOfConcern` is that Bridge and whose ClaimGraph states the proposed use `u`, direction `d`, use-specific rule `r`, tolerated loss `t`, and polarity. For ordinary reliance require the matching current A.10 evidence-provenance relation and local `RelianceDisposition`; when an assurance claim or B.3 material-reliance threshold is current, use B.3's separate assurance branch instead. Observed loss and CL are evidence, defeater or assurance-policy material, not Bridge participants or permission. Authorization and the actual `Select` application remain with their subject patterns. A Bridge id, `CrossingAllowance`, registry row, policy pin, `CrossingBundle`, DRR or SCR entry cannot substitute for any step.

* `PolicyHooksRef?`: optional pointers to policy records (not defined here; wired via Extensions).

Here “a registry row represents a family” means that the row is the auditable selector-facing record for one declared grouping. The family id preserves that row lineage; the row ref selects one immutable edition for replay. Neither value identifies the grouped Methods, makes a membership relation obtain, or turns a common label, shared description, lineage note, eligibility rule, maturity card, evidence record, or policy into a method-family fact. Changing a row edition changes the registry artifact; it changes a Method or a separate family relation only when that object's direct identity rule or the relation's predicate independently says so.


**S1′ — `GeneratorFamily Registry` (design‑time; optional; per CG‑Frame).**
A registry row for families that generate tasks and environments, and may co-evolve solver families. G.5 carries the registry-entry shape, not the generator semantics:

* `Identity and continuity`: `GeneratorFamilyId` names the continuing row lineage; `rowEdition` names one immutable edition; `GeneratorFamilyRowRef := <GeneratorFamilyId, rowEdition>` designates that edition. `UTSRowId` remains its publication value.
* `Exact generator members`: non-empty references, each resolving to a generator already identified under its subject pattern.
* `Grouping basis`: the independently established classification, membership relation, or explicit project-local criterion that groups those generators for this selector.
* `GeneratorSignatureRef`: conceptual input and output semantics plus budget semantics.
* `EnvironmentValidityRegionRef?`: pinned constraints for generated environments or tasks.
* `TransferRulesRef.edition?`: required when the Open-Ended mode is enabled (semantics come from the cited extension refs).
* `CouplerRefs?`: exact `MethodFamilyRowRef[]` values that may be coupled with this generator-row edition.

Changing generator members, grouping basis, or another selection-changing pin creates a new generator `rowEdition`; old `GeneratorFamilyRowRef` values continue to resolve their old editions.

**S2 — C.22 `TaskSignature` input and conditional G.4 map.**
C.22 constitutes the `TaskSignature` episteme and defines its edition rule. G.5 consumes its `TaskSignatureRef` and does not reconstruct it from a task, CAL pack, or map. Its function here is pinning and auditability, not over-specification.

When this selector actually uses G.4 CAL gates, it also consumes one exact `TaskMapRef`. Resolve that immutable map edition, require its `taskSignatureRef` to equal the C.22 `TaskSignatureRef` supplied to this selector, and follow its exact `CALCharterRef` and edition-bearing clause, operator, flow, and evidence-profile refs. The map supplies no TaskSignature field and no threshold value. If no G.4 gate is current, omit `TaskMapRef`; an ordinary selector does not need a CAL pack merely to return a truthful bounded result.

For the G.4 safety example, G.5 receives `TaskSignatureRef=SafetyPortfolioTaskSignature-E4` and `TaskMapRef=<SafetySelectionMap, E3>`. The map resolves `CALCharterRef=<SafetyCALCharter, E2>` and the cited gate declarations. A different signature ref or an unresolved charter or component blocks only that gated selector use.

**S3 — `Selection kernel boundary` (run‑time; policy‑governed).**
A notation‑independent selector that:

* consumes `TaskSignatureRef`, exact method- or generator-family row refs, pinned spec refs, and an exact matching `TaskMapRef` only when G.4 CAL gates are current,
* applies eligibility and assurance gating (tri-state),
* computes an admissible (possibly partial) order,
* returns one declared selector outcome over the exact Method candidates admitted through this kernel: most often `Shortlist` or `RankedShortlist`, and `JointUseSet` only when every returned Method candidate is included for one named use; otherwise it returns one `SpecialistHandoff`, one other narrowed handoff, one abstain outcome, or one escalation outcome (per `DefaultId.PortfolioMode` and explicit overrides),
* emits audit records with pins addressable by DRR and SCR records.

When `TaskMapRef` is present, resolve its exact immutable G.4 map edition before applying any cited gate. Its `taskSignatureRef` must match this selector's C.22 `TaskSignatureRef`; its `CALCharterRef` must recover the CG frame, EntityOfConcern, ReferencePlane, specification editions, and assumption envelope; and each cited clause, operator, flow, and evidence profile must resolve at its exact edition. Carry the exact map ref among the result basis and refresh pins. Do not copy thresholds or acceptance semantics into G.5.

For every `MethodFamilyRowRef` consumed here, resolve the exact immutable row edition and then its A.3.1 `MethodRef[]`, grouping basis, and selection-changing pins before admitting the candidate. Apply the same rule to `GeneratorFamilyRowRef`. The selector may compare or return exact row refs as auditable selector-facing addresses, but row selection neither creates its members nor proves that every listed member belongs, is admissible, is selected, or will be enacted. An unresolved Method reference or missing grouping basis blocks that row's method-bearing use; it is not repaired by a label, description, UTS identity, policy, or evidence pin.

When a selector consumes an organization among Methods, cite an exact `SelectedStructureRef` only after A.22 has independently identified the `U.Structure` from exact constituents, exact already-obtaining relation occurrences, applied constraints, and one named use frame. G.5 neither supplies those discriminators nor selects the Structure by listing it. If the organization instead constitutes one composite Method, consume the exact A.3.1 Method only after B.1.5 has qualified that candidate from its independent parts and whole-forming basis.

S3 states reusable selector behavior. It does not itself perform selection. For an actual selector use, first recover every precise performer's A.13 core for the exact selection action, scope, working situation, and window, including the same obtaining assignment later used by any exact attribution. A.15.1 then independently admits the dated selector Work from its exact performance history, enacted Method, temporal extent, and containing-System relation. State the actual A.6.1 `Select` application, its effective argument bindings, and the A.19 `SelectionSlot` binding that carries the selected set by value. Add F.6 afterward only when the receiving claim needs exact assignment-bound attribution through the same obtaining A.13 assignment. The declaration, planned pins, registry rows, policy, assignment, F.6 relation, and `CandidateSet` type create none of the A.13, Work-admission, application, or result facts.

A compact selector account may omit only an assignment identifier unused by its receiving claim; it omits no criterion, classification, assignment, Work-admission, or attribution fact that the claim consumes. A root-family reference, the same holder, overlapping times, or silence in the receiving text establishes or removes neither the assignment nor F.6 attribution. Ordinary selector discussion not admitted as `U.Work` does not enter this branch.

**S3.A — `TaskFamilySpecializationProfile@Context` (run‑time; conditional).**
When the real selector question is acquisition of usable specialization on a declared task family, the selector may emit one `TaskFamilySpecializationProfile@Context` for each candidate, one `SpecialistHandoff`, or one narrowed handoff plan. Here `profile` means one selector-time comparison record for bounded specialization, not a new U-kind and not a generic narrative profile. `G.5` carries this selector-time specialization question here; it does not redefine the adaptation-signature field vocabulary from `C.22.1`.

The profile should therefore cite one `AdaptationSignatureRef` or equivalent pinned field set carrying the declared `TaskFamilyRef` or `TaskSignature`, the work-measure threshold target, prior exposure declaration, time-to-threshold, budget-to-threshold, post-threshold efficiency when relevant, any declared transfer or retention claim, any downside cost or downside on adjacent tasks, and any specialization-entry baseline, specialization-entry evidence, or stepping-stone evidence item that materially affects comparison.

Admission rule for `SpecialistHandoff`: use that handoff kind only when the truthful declared result is one heterogeneous handoff bundle whose members occupy different specialization positions that still need to travel together. Do not use it when a `SetResultOutcome` with `Shortlist`, `RankedShortlist`, or `JointUseSet`, or a `HandoffOutcome` with another admitted handoff kind, already states the result more precisely.

When the declared task family is heterogeneous, the selector may return one `SpecialistHandoff`, one other narrowed handoff plan, or one `SetResultOutcome` with an admitted `SetResultFamily` that preserves rival specialists rather than collapsing them into a fake single winner. Low-human-overlap candidates remain admissible only when the profile, evidence basis, and policy constraints are explicit.

**S4 — `Composition and fallbacks` templates (design‑time).**
A library of composition shapes—`preconditioner -> solver -> verifier`, cascades, and meta-selectors—remains available **as design-time templates**, admissibility-checked and pinned. A template is a description or policy-bound arrangement for possible composition; its existence, diagram order, registry placement, or selection does not create a Method, `methodPartOf` occurrence, obtaining relation, or selected Structure.

If exact A.3.1 Methods, exact B.1.5 `methodPartOf` occurrences, all other required whole-forming claims and constraints, whole semantics, interface boundary, and reidentification rule qualify one already identified candidate as a composite `U.Method`, consume that exact Method through the B.1.5 branch. If independently identified Methods and already-obtaining relations are instead organized for one use without constituting one Method, consume an independently selected A.22 `U.Structure` only after its exact constituents, selected obtaining relation occurrences, applied constraints, and named selection-use frame are present. `MethodRelationStructure` may remain a local readable designator for that actually selected Structure; it is not a U-kind, relation kind, Method holon, registry-row identity, or generic `@BoundedContext` object.

A C.2.1 episteme may describe either governed object. A.3.2 applies only when the episteme's exact `EntityOfConcern` is one already admitted Method and its claims substantively describe that Method; an episteme whose exact concern is the selected Structure is not thereby a `U.MethodDescription`. Concrete strategy semantics stay in the referenced method families; G.5 only carries the composition template, selector relation, registry row, exact consumed Method or Structure reference, or selected-set result. None of those G.5 artifacts supplies the B.1.5 or A.22 construction facts.

Algebraic, graph, matrix, embedding, or neural selector notation remains a mathematical or representation lens when that representation is current; use C.29 for its correspondence and preserved-or-lost structure rather than reading notation as composition or selection.


**S5 — `Result, public identity, and telemetry` record boundary (run-time).**
A standard result-content boundary emits:

* `DRR` (decision rationale) and `SCR` (evidence and confidence citation) with explicit pins,
* declared selector and selected-set records produced either by method-family `G.5-3 Select` or by the already-grounded-member `G.5-6 DeclareSetResult` branch,
* telemetry pins to refresh orchestration (`G.11`), without governing orchestration.

S5 governs the selector-facing record boundary, not truth or actuality by record existence. A DRR, SCR, selected-set record, shortlist id, telemetry event, refresh cue, policy pin, or result label does not create dated Work, an actual operation application, the selected-set binding, a domain result, an evidence-provenance relation, assurance, authorization, or publication availability. Persist a selector-result claim as its own C.2.1 episteme when another use must rely on it; connect evidence through A.10, assurance through B.3, authorization through its direct governor, and actual availability through E.24.PUB only when each relation independently obtains.


When the current question is selector-facing set-result declaration rather than one generic registry trace, `Shortlist` names retained alternatives, `RankedShortlist` names those alternatives when the result orders them, `JointUseSet` names all members included for one named use, and `ChoiceSet` stays one mathematical gloss rather than a public result kind. `ShortlistId` is specific to a shortlist result; use a generic `publicId` for another result only when one stable public identity is needed.

**S6 — `Governance and evolution` declaration boundary (design-time).**
Versioning, deprecation, and registry evolution discipline (UTS publication; continuity), without minting new Part‑G‑wide types.

#### G.5:4.3 - Selector head and narrower selector families

Selection and dispatch stay one generic selector head. Narrower selector families may refine it, but they do not redefine the universal invariants pinned through `G.Core`, do not add hidden mandatory inputs beyond pinned policy or edition refs, and do not mutate SlotKinds.

Method- and generator-specific pressures such as `QD` archives, open-ended declared sets, explore and exploit lenses, or preference comparators do not become part of the selector head. They arrive only through explicit extension declarations and the pins those extensions require.

#### G.5:4.4 - Selector Relation Fields

| Selector relation                 | Consumes                                                                                                                                                     | Produces                                                                                                                                                                                                                                                   |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **G.5-1 RegisterFamily**          | one continuing `MethodFamilyId`; non-empty already admitted A.3.1 `MethodRef[]`; a reference to one independently established classification or membership relation, or an explicit project-local grouping criterion; new immutable row edition; CHR and CAL pins (from `G.3` and `G.4`); `CNSpecRef.edition`; `CGSpecRef.edition`; optional G.2 family card; and task, scheme, source, `ClaimScope`, validity, or intended-use pins only when they change this selection | One immutable `MethodFamily` registry row and its `MethodFamilyRowRef = <MethodFamilyId, rowEdition>`, fixing `MethodRef[]`, `GroupingBasisRefOrCriterion`, `EligibilityStandardRef`, `AssuranceProfileRef`, `UTSRowId`, and the applicable pinned refs. The G.2 card and the CHR, CAL, specification, and use pins are metadata or evidence inputs and cannot supply either the Methods or the grouping fact. |
| **G.5-2 RegisterGeneratorFamily** | one continuing `GeneratorFamilyId`; non-empty exact generator refs resolved under their subject patterns; exact independently established classification, membership relation, or explicit project-local grouping criterion; new immutable row edition; optional G.2 generator-family cards; and pinned refs, including `TransferRulesRef.edition` when applicable and separate task, scheme, source, `ClaimScope`, validity, or intended-use pins when action-changing | One immutable `GeneratorFamily` registry row and its `GeneratorFamilyRowRef = <GeneratorFamilyId, rowEdition>`, fixing the generator refs, grouping basis, `GeneratorSignatureRef`, `UTSRowId`, and applicable pinned refs. Cards, labels, policies, and pins create neither a generator nor its family membership. |
| **G.5-3 Select**                  | `TaskSignatureRef`; exact matching `TaskMapRef` when G.4 CAL gates are current; exact `MethodFamilyRowRef[]` in scope whose immutable editions resolve to non-empty exact A.3.1 `MethodRef[]` and exact grouping bases; optional exact `GeneratorFamilyRowRef[]`; pinned `CNSpecRef` and `CGSpecRef` editions; policy refs if any; audit citation pins (`PathId` and `PathSliceId`) | `CandidateSet` (set-returning), declared selector result with `PortfolioMode` recorded, exact row refs and any current `TaskMapRef` among the result basis pins, and `DRR` and `SCR` pins; if no admissible candidate exists: return `CandidateSet = EMPTY` plus an escalation hint (`ActionHint`) and the pins required to plan next steps (P2W split applies) |
| **G.5-4 Compose**                 | `CandidateSet`, composition template refs, pinned admissibility constraints                                                                                       | Composite strategy template (template-level; admissibility-checked; pinned)                                                                                                                                                                                      |
| **G.5-5 Telemetry**               | run outcomes, citations, and policy or edition pins                                                                                                               | refresh cues (typed RSCR causes and payload pins), parity deltas (if parity harness is in use), telemetry pins (selector-side; orchestration governing definition is `G.11`)                                                                                              |
| **G.5-6 DeclareSetResult**        | one exact `SetResultFamily`; exact already identified `memberRef[]`; `namedUse` for `JointUseSet`; ordering; inclusion or selection conditions; and sufficient `basisPins` to the already current choice, pool treatment, accepted decision, or other governed inclusion basis | one `SelectorOutcome` with `SelectorOutcomeKind = SetResultOutcome` and the exact membership form required by that family. For `JointUseSet`, it emits keyed unique `memberEntries`, `ordering = unordered`, the named use, inclusion conditions, and basis pins without a method-family row or `Select` pass. |

`RegisterFamily` produces only the registry row described in S1. It does not produce any A.3.1 Method or independently governed membership fact. `Select` may address candidates through those rows only after their exact Methods and grouping bases resolve; its returned candidate or selected-set value does not retroactively ground a row member.

`Compose` produces only the pinned template named in its output column. It neither qualifies one composite Method under B.1.5 nor selects one A.22 Structure. When a later selector use consumes either governed object, the exact Method or Structure reference is an independently grounded input rather than a result inferred from this template.

`DeclareSetResult` begins only after its exact members and inclusion or selection basis are current. An upstream C.11 `ChoiceResult`, C.19 pool treatment, accepted decision, or another governed basis may appear among `basisPins`; the G.5 branch does not repeat or perform that decision. It declares the selector-facing set-result content and stops. It creates no member identity or relation, method-family row, `Select` application, dated selection Work, persisted C.2.1 result episteme, assurance or authority claim, or E.24.PUB availability occurrence.

#### G.5:4.4a - Worked selector slice

- A catalyst-search team is choosing among three method families for the same declared `TaskSignature` and `C.22.1` adaptation signature.
- The shared profile pins one work-measure threshold target, one freshness window, one prior-exposure declaration, and one adaptation budget. One family reaches threshold quickly but carries high downside on adjacent tasks. One family is slower but transfers cleanly. One family never clears `MinimalEvidence` and must abstain.
- An admissible `G.5` result therefore declares a set-return shortlist or a narrowed handoff plan, with DRR and SCR records citing why the third family was excluded and why the first two remain non-dominated. The selector does not invent one scalar winner and does not hide the specialization profile in auxiliary side notes.
- If the project also claims that this selection actually occurred, A.13 first recovers `CatalystSelectorSystem-17 : U.System` for exact action `CatalystFamilySelectionAction-17`. `CatalystSelectorBoundary-17` contains the deployed selector runtime, its effective policy state, and its registry/evidence interfaces; it excludes the method-family rows, `TaskMap`, result records, assignment, and containing team System. The action applies the effective selector to the three candidate families and returns the retained set. Its scope is `CatalystFamilySelectionClaimScope-17`, its working situation is `CatalystSearchSelectionSituation-17`, and its window is `2026-07-30T10:00:00Z` through `2026-07-30T10:08:00Z`. `CatalystSelectionAdmissibilityNorm-17` directs the selector to exclude candidates that fail `MinimalEvidence`, preserve admissible non-dominated alternatives, and abstain rather than manufacture a scalar winner. Relevant conditions include the exact `CatalystTaskSignature-17`, current row and map editions, eligibility evidence, comparison policy, and adaptation-signature values.
- A.2 declares local agential kind `CatalystMethodSelectorSystemRole`. Its membership criterion requires the stable work-facing contribution of method-family selection and goal-directed, condition-sensitive regulation under `CatalystSelectionAdmissibilityNorm-17`: the holder must apply the current gates, preserve the admissible set-return semantics, and abstain or escalate when no candidate qualifies. `CatalystSelectorDecisionTrace-17` shows `CatalystSelectorSystem-17` excluding the third family for failed `MinimalEvidence`, retaining the first two as non-dominated, and emitting no scalar winner. A.10 evidence-use claims connect that trace and the boundary/runtime records to the criterion. The case independently classifies `CatalystSelectorSystem-17` under `CatalystMethodSelectorSystemRole`; neither the assignment nor the candidate Work supplies the classification. No Grade, autonomy result, characteristic profile, or stronger assurance claim is consumed.
- The same A.13 core uses `CatalystSelectorAssignment`, a directly declared species under `U.SystemRoleAssignment`. The species declares holder, assigned-kind, and task-signature participant meanings and the assignment predicate. `CatalystSelectorAssignment-17` obtains with `CatalystSelectorSystem-17`, `CatalystMethodSelectorSystemRole`, and `CatalystTaskSignature-17` as its exact participant values; its maximal uninterrupted predicate-true interval covers the stated scope, situation, and window.
- Only after that core is established does A.15.1 independently admit `CatalystSelectionWork-17 : U.Work` from the exact selection-action history, enacted `CatalystFamilySelectionMethod`, temporal extent, and obtaining containing-System relation to independently admitted `CatalystSearchTeamSystem`. Actual application `CatalystSelectApplication-17` separately carries its effective candidate, criteria, and A.19 `SelectionSlot` bindings. Neither the assignment nor F.6 is an A.15.1 admission premise.
- Because this account explicitly attributes the Work under `CatalystSelectorAssignment-17`, F.6 afterward establishes `performedUnderAssignment(CatalystSelectionWork-17, CatalystSelectorAssignment-17)` through that same obtaining A.13 assignment. The direct case fact links the exact pair, holder equality holds, and the assignment interval covers the Work. A different overlapping assignment held by the same System would not establish this attribution. A short result may omit the assignment identifier only after every fact consumed by the attribution remains recoverable.
- A persisted shortlist assertion is a separate C.2.1 episteme; its DRR or SCR references do not by themselves prove the exclusion facts, warrant the result, authorize downstream action, or make that episteme available to an audience.

- When one upstream `C.19` pass has already narrowed the live pool to one internal retained subset over registered families, `G.5-6 DeclareSetResult` may declare that result as one `Shortlist` with one `ShortlistId` and explicit basis pins only when selector-facing result declaration is now the question. Until that declaration occurs, the internal retained subset is not yet one G.5 shortlist result.
- When one upstream `C.11` pass has already fixed one local choice over one declared source set, `C.19` has fixed one retained pool treatment, an accepted decision has fixed all-member inclusion, or `C.24` has produced one enactment-facing narrowed handoff, use `G.5-6 DeclareSetResult` when selector-facing set-result content is now the question. Until that declaration occurs, the `ChoiceResult`, `PoolPolicyResult`, accepted inclusion basis, `CallPlan`, or `CheckpointReturn` is not itself that G.5 result. Non-Method members do not pass through `RegisterFamily` or `G.5-3 Select`.

#### G.5:4.4b - Declared selected-set result and closure rule

When the current question is selector-facing result declaration, state one explicit selected-set result rather than leave it implicit in a selector trace, comparison note, or local choice.

For method dispatch, that result closes selector work over grounded rows. For a `JointUseSet`, it records already identified members that are all included for one named use. It does not replace registry maintenance, comparison rules, the upstream choice or inclusion basis, or the patterns that identify the members and their relations.

The admissible selector outcome families here are:

- `SelectorOutcomeKind = SetResultOutcome`, whose closed `SetResultFamily` value set is `Shortlist` when alternatives are retained for later choice and the result does not order them, `RankedShortlist` when the result orders those retained alternatives, and `JointUseSet` when every named member participates in one named use;
- `SelectorOutcomeKind = HandoffOutcome`, with `HandoffKind = SpecialistHandoff` or one other narrowed handoff plan when heterogeneity is the truthful downstream result;
- `SelectorOutcomeKind = AbstainOutcome` when no admissible candidate exists and the truthful result is one abstain; and
- `SelectorOutcomeKind = EscalationOutcome` when no admissible candidate exists and the truthful result is one escalation.

`G.5-3 Select` may emit this family only over the exact Method candidates admitted through its kernel; `G.5-6 DeclareSetResult` emits it from exact already identified members and a current inclusion basis. Neither branch performs an upstream choice, makes a member relation obtain, or proves actual selection Work.

A `JointUseSet` uses this bounded representation:

- `namedUse` states the one joint use;
- `memberEntries` contains one keyed entry per included member;
- every entry has one exact `memberRef`; the membership result adds no per-member contribution or basis field;
- each exact `memberRef` occurs at most once, and entry order has no semantic effect;
- if a serialization also emits top-level `members`, it is only the unique set projection of `memberRef` values from `memberEntries`, never a second maintained list;
- `ordering`, inclusion conditions, and sufficient top-level `basisPins` remain explicit; and
- candidate-pool membership and excluded candidates stay separate from emitted joint-use membership.

Exact content, claims about a member's use or contribution, and direct relations keep their own governed records. When one supports the membership result, cite that existing record among `basisPins`; `memberEntries` creates neither the cited content nor a new contribution relation.

For framework use, `memberRef` may name an exact already identified edition under its existing identity rules. Do not populate `MethodRef`, create a registry row, or classify that edition as a Method merely to emit the result.

Every outcome still states its `SelectorOutcomeKind`, public result kind when applicable, members, keyed entries, handoff content, or blocking condition, ordering, and sufficient basis pins. A handoff also states its next downstream use boundary.

A compact retained-alternative result may look like:

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

A compact joint-use result may look like:

```text
SelectorOutcome(
  selectorOutcomeKind = SetResultOutcome,
  setResultFamily = JointUseSet,
  namedUse = cohort_review,
  memberEntries = [
    { memberRef = Core@C },
    { memberRef = Domain@D },
    { memberRef = Local@L }
  ],
  ordering = unordered,
  inclusionConditions = [all_three_editions_required_for_cohort_review],
  basisPins = [choice_result_12, edition_basis_7]
)
```
Close with `Shortlist` or `RankedShortlist` when the result retains alternatives. Close with `JointUseSet` only when every member is included for the named use and its keyed membership can be stated truthfully. Close with a handoff, abstain, or escalation outcome when that is the actual result. If the result omits its result family, members or member entries, ordering, named use where required, or basis pins, it is not a complete `G.5` result.

#### G.5:4.4bb - Public labels over archive, front, and style source sets

When a selector consumes a declared `ExplorationArchive`, `Archive`, `Front`, or `Q-front`, keep that object as a source-set family or source-set reference; it is not the emitted G.5 outcome. The emitted result states one admitted `SelectorOutcomeKind` and, for a set result, one admitted `SetResultFamily`. `StyleShortlist` and `TraditionShortlist` may be public domain labels over an admitted set-result family after their term bridges and cultural meaning are clear; they do not extend either closed set.

```text
SelectedSetResultLabelLine@Context:
  selectorOutcomeKind:
  setResultFamily?:
  sourceSetFamily:
  publicSelectedSetLabel?:
  namedUse?:
  memberEntries?:
  membersOrHandoff?:
  derivedViewKind?:
  basePaletteOrArchiveRef?:
  ordering:
  basisPins:
  nextUse:
```

Earlier records may keep `membersOrHandoff`. Read it as `members` for `Shortlist` or `RankedShortlist` and as `handoffContent` for a `HandoffOutcome`. It cannot replace keyed `memberEntries` in a `JointUseSet`; if it also lists joint-use members for compatibility, that list is only the unique set projection of the entry keys.

`sourceSetFamily` may name a declared `Front`, `Q-front`, `ExplorationArchive`, `Archive`, current pool subset, or derived tradition view. For retained alternatives, `publicSelectedSetLabel` normally names `Shortlist` or `RankedShortlist` and may use a domain label such as `StyleShortlist` or `TraditionShortlist` only when the term bridge is already clear. `JointUseSet` is not a shortlist label: it names an all-member result and therefore uses `namedUse` plus keyed `memberEntries`. G.5 does not create the archive, compute the comparison, govern the pool policy, decide the cultural-evolution case, establish member identity or relations, or repair the term bridge. Use `C.18`, `A.19.CPM`, `C.19`, `C.36`, `F.17`, `F.18`, and `F.9` for those distinct questions.

#### G.5:4.4c - Result-declaration quick card

The smallest useful `G.5` result card usually states:

- `selectorOutcomeKind = SetResultOutcome | HandoffOutcome | AbstainOutcome | EscalationOutcome`
- `setResultFamily = Shortlist | RankedShortlist | JointUseSet` when `selectorOutcomeKind = SetResultOutcome`
- `members = ...` for `Shortlist` or `RankedShortlist`
- `namedUse = ...` and keyed `memberEntries = ...` for `JointUseSet`
- `handoffKind = SpecialistHandoff | NarrowedHandoff` and `handoffContent = ...` when `selectorOutcomeKind = HandoffOutcome`
- `ordering = ranked | unordered | not applicable`
- `publicId = ...` when one public identity is emitted
- the applicable inclusion conditions and `basisPins = ...`
- `nextUse = downstream comparison | specialist handoff | escalation | none`

A short retained-alternative card may read:

```text
selectorOutcomeKind = SetResultOutcome
setResultFamily = Shortlist
members = [family_A, family_C]
ordering = unordered
shortlistId = shortlist_17
basisPins = [pathSlice_41, scr_22]
nextUse = downstream_comparison
```

A short all-member card may read:

```text
selectorOutcomeKind = SetResultOutcome
setResultFamily = JointUseSet
namedUse = cohort_review
memberEntries = [
  { memberRef = Core@C },
  { memberRef = Domain@D },
  { memberRef = Local@L }
]
ordering = unordered
inclusionConditions = [all_named_editions_required]
basisPins = [choice_result_12, edition_basis_7]
nextUse = cohort_material_preparation
```
If the card does not state the result kind, applicable members or keyed member entries, whether order belongs to the result, the named use for joint inclusion, and the basis pins, it does not yet state a complete `G.5` result.

#### G.5:4.4ca - Derived tradition-view result stays derived over one declared palette

- If selector work consumes one declared source set such as `Front`, `Archive`, or one source-set composition through one derived tradition view such as `TraditionFront` or `TraditionArchive`, treat that derived view as one interpretation view over one declared `SoTAPaletteDescription`, not as the default meaning of `Tradition` or of the palette itself.
- When `SelectorOutcomeKind = SetResultOutcome`, close with `Shortlist` or `RankedShortlist` for retained alternatives and with `JointUseSet` for all-member use; when `SelectorOutcomeKind = HandoffOutcome`, close with one `SpecialistHandoff` or another narrowed handoff. The derived tradition view disciplines the source, not the emitted outcome family.
- When such a derived tradition view is active, state `SourceSetFamily`, use `DerivedViewKind` when the distinction matters to interpretation or later shipping, use `SourceSetComposition` only when several source-set families were genuinely composed, and keep `BasePaletteRef=SoTAPaletteDescriptionId` recoverable alongside the emitted result.
- If the derivation depends on one declared `Q` or one reachability or coverage rule, cite that declared basis directly in DRR and SCR records or equivalent basis pins rather than leaving the derivation implicit.
- If no derived tradition view is active, stay with the declared palette, front, archive, or shortlist families already named by the selector record.

#### G.5:4.4d - Worked result-declaration closure slice

Four short contrasts keep the result-declaration closure rule practical.

**Several alternatives survive, and the result does not order them.**
When the selector retains more than one admissible family for later choice and the declared result does not order them, `G.5` should close as one `Shortlist` over the registered surviving rows:

```text
Shortlist(
  members = [family_A, family_C],
  shortlistId = shortlist_17,
  ordering = unordered,
  basisPins = [pathSlice_41, scr_22],
  nextUse = downstream_comparison
)
```

**The result orders the retained alternatives.**
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

**Every named member is included for one use.**
A cohort needs three already identified framework editions together. The result is not a shortlist of alternatives:

```text
JointUseSet(
  namedUse = cohort_review,
  memberEntries = [
    { memberRef = Core@C },
    { memberRef = Domain@D },
    { memberRef = Local@L }
  ],
  ordering = unordered,
  inclusionConditions = [all_three_editions_required_for_cohort_review],
  basisPins = [choice_result_12, edition_basis_7]
)
```

The edition refs keep their existing identities; G.5 creates no Method, registry row, dependency, compatibility, publication, access, content, claim, or contribution relation. Any content or claim that supports inclusion remains in its own governed record and may be cited among the top-level `basisPins`.

**No admissible candidate survives.**
When no family clears the pinned admissibility or evidence gates, `G.5` should close as one abstain or escalation result rather than as one empty shortlist pretending to be progress:

```text
Abstain(
  blockingPins = [cg_min_evidence, crossing_bundle_missing],
  basisPins = [pathSlice_91, scr_61],
  nextUse = escalation
)
```

The practical distinction is simple: an internal retained subset can exist upstream without yet being a public selector result. When the current question is to state that result for downstream use, `G.5` requires the result family, applicable members or keyed member entries, ordering, named use where required, and basis pins directly in the result.

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
  * active fields from C.21's DHC replay basis *(only when this telemetry consumes a C.21 DHC coordinate; carry exactly the fields that coordinate used)*
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

  * `GeneratorFamilyRowRef[]`
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
- `Shortlist` names alternatives retained for later choice and does not order them.
- `RankedShortlist` names an ordered result over such retained alternatives.
- `JointUseSet` names a result whose every keyed member is included for one named use; it is not a shortlist and has no semantic entry order.
- `ShortlistId` is the emitted public token when a stable shortlist identity must be carried or cited; another set result may use its own generic `publicId` when a stable public identity is actually needed.
- `ChoiceSet` may be used only as a mathematical set gloss when the set object itself is under analysis; it does not replace `Shortlist`, `RankedShortlist`, or `JointUseSet` as the public result kind.
- `PortfolioMode` states how the selector operated; it does not rename the emitted set result.
- The default `PortfolioMode=Archive` means that an unspecified selector or generator operating mode must preserve retained exploration evidence rather than pretending one current front or selected set has already been emitted. It does not make every returned object an `Archive`, override `SetResultFamily`, or change the declared `DominanceSet`.
- If one selector consumes both a front and an archive, say so explicitly rather than blurring them into one generic portfolio.
- If one selector consumes one derived tradition view, keep that derived view explicit rather than silently treating it as the default meaning of `Tradition`.
- `SetResultFamily`, `SourceSetFamily`, `SourceSetComposition`, `SubjectKind`, `DerivedViewKind`, `BasePaletteRef`, `PromotionPolicy`, and `RetentionIntent=steppingStone` are declaration fields, refs, or policy pins around the returned outcome; they are not additional emitted set results.
- `SourceSetFamily` names the immediate declared source-set family.
- `SourceSetComposition` is used only when the selector genuinely consumed more than one source-set family such as `Front` and `Archive`.
- If that source set is one derived tradition view, keep the base palette recoverable alongside it.
- `DerivedViewKind` may name which derived tradition view is active when that distinction matters to interpretation or later publication.
- `DerivedViewKind` does not replace `SourceSetFamily`, `SetResultFamily`, or the emitted result kind.
- `BasePaletteRef` is one cited ref or id, not one kind.
- If one selected result comes from one declared source set, state that `SourceSetFamily` rather than asking the reader to infer it from one mode flag.
- `PromotionPolicy` is required when tie-break or telemetry signals are promoted into dominance.
- The selector may consume one declared source set and one declared choice lens without trying to explain the whole reason why another probe was worth its cost.
- When `CostToProbe`, `ValueOfInformation`, `ValueOfComputation`, `explore_share`, a direct graduation condition, or sequencing pressure matters, keep it explicit in the surrounding choice doctrine instead of smuggling them into set-result declaration fields.
- A `JointUseSet` uses keyed `memberEntries`; every exact `memberRef` is unique, no per-member contribution or basis field is added, and any top-level `members` is only the derived unique set projection of those keys.
- **Well-formedness constraint:** every exact framework-edition or other non-Method `memberRef` resolves under its existing identity; joint-use membership adds no `MethodRef` value or registry row for that member.
- Candidate-pool and excluded-candidate records remain separate from the emitted `JointUseSet`; actual choice and selection Work remain with C.11 and the applicable A.6/A.15 occurrence patterns.
- Selector-facing results should name the set-result kind, source-set kind when applicable, derived-view declaration when needed, membership form, and promotion or default declaration.
- Those selector-facing field values should use controlled tokens, cited ids, or already-declared head labels rather than selector-local prose values.

