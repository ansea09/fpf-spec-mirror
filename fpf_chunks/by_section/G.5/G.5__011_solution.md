---
chunk_kind: "child"
pattern_id: "G.5"
pattern_title: "Method-Family Registry, Dispatch and Selected-Set Result Declaration"
section_id: "G.5:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/G.5/G.5__011_solution.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "G.5 — Method-Family Registry, Dispatch and Selected-Set Result Declaration"
  - "G.5:4 — Solution"
line_start: 113177
line_end: 113614
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
  - "JointUseSet"
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
  - "selected-set result declaration"
  - "set-result outcome"
  - "tool choices are outside the core"
---

### G.5:4 - Solution
#### G.5:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; Default Governing Definition Index citation)

**GCoreLinkageManifest (normative; size-controlled via profiles and sets).**
For the operation in use, expand the applicable profile and set ids by union with its explicit deltas (per `G.Core:4.2.1`). The activation conditions below select those ids before expansion; `Nil‑elision` does not waive an activated obligation. `Select` retains its exact task, row editions and DRR/SCR-addressable audit result. `DeclareSetResult` instead consumes its exact result family, identified members, inclusion basis, ordering and named use where required; it acquires no TaskSignature, Method or registry row merely by declaring that set.

Select profile activation before expanding the G.Core sets. RegisterFamily always retains S1's immutable row edition, exact admitted members, grouping criterion and applicable eligibility/comparison basis. A project-local row without a CG-Frame activates neither AuthoringBase nor AuthoringMinimal; it still satisfies those S1 obligations. Intentional public registration adds EligibilityStandardRef, AssuranceProfileRef and UTS obligations even when no CG gate is in use. When a real CG-Frame registry or Select use is current, both authoring sets apply in full; omitting their required CN/CG pins is a failure, not nil-elision.

For crossing-aware selection, `CorePinsRequired` below lists the crossing pins individually. Each conditional pin is mandatory when its stated condition holds. When consuming `G.7` calibration records or a named `B.3` assurance account, retain all pins, editions, and evidence required by that account, including `CC‑G7‑SCRLinkage‑1` for cited calibration evidence.

* `CoreConformanceProfileIds :=`

  * `GCoreConformanceProfileId.PartG.AuthoringBase` *(when the current operation authors a registry in an actually selected CG-Frame or performs G.5-3 Select within that frame)*
  * `GCoreConformanceProfileId.PartG.TriStateGuard` *(when evaluating eligibility or acceptance predicates)*
  * `GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted` *(when public identities are minted or evolved, including intentional public registration under S1/S1′ and CC-G5.6; a reusable project-local row alone does not activate this profile)*
  * `GCoreConformanceProfileId.PartG.ShippingBoundary` *(when an output is shipped)*
* `CorePinSetIds :=`

  * `GCorePinSetId.PartG.AuthoringMinimal` *(for the same actual CG-Frame registry-authoring or G.5-3 Select use; local registration or a set declaration alone does not activate it)*
* `CorePinsRequired :=` *(delta over PinSets; pins and refs are id-only; prefer strengthening optional-to-required over restating pins already covered by PinSets)*

  * `TaskSignatureRef` *(the C.22 TaskSignature edition for `Select`; see `G.5:4.2`, S2)*
  * `TaskMapRef?` *(exact G.4 map edition, only when this selection uses G.4 CAL gates)*
  * `MethodFamilyRowRef[]` *(exact `<MethodFamilyId, rowEdition>` values when method-family rows are consumed or registered)*
  * `MethodRef[]` *(exact A.3.1 Methods resolved from every method-bearing registry row consumed or registered)*
  * `SelectedStructureRef[]?` *(exact independently selected A.22 Structures consumed only when their organization changes this selector use)*

  * `GeneratorFamilyRowRef[]?` *(exact `<GeneratorFamilyId, rowEdition>` values when generator families are in scope)*
  * `PathId[]?`, `PathSliceId[]?` *(when audit or evidence citations use a G.6 graph, or an independently applicable gate or shipping contract requires those citations)*
  * `UTSRowId[]?` *(when the operation mints, evolves or consumes a public identity; intentional public registration activates S1/S1′ and CC-G5.6 obligations)*
  * `FailureBehaviorPolicyId?` *(only when degrade or abstain behavior is explicitly policy‑bound)*
  * `SoSLogBranchId?` *(only when degrade or abstain behavior is explicitly policy‑bound)*
  * `BridgeId/BridgeCardId?` *(the obtaining Bridge actually used by this selection; a Bridge Card is cited only when that Card is relied on)*
  * `BridgeMatrixId?` *(when this selection uses a BridgeMatrix)*
  * `CL/CL^k/CL^plane?` *(the applicable values when cited or required by the consumed calibration or named assurance account)*
  * `Φ/Ψ/Φ_plane policy-ids?` *(the applicable policy ids and editions when required by the consumed calibration or named assurance account, or when crossing or plane penalties are applied)*
  * `CrossingBundleId?` *(when the selector cites a CrossingBundle or its named downstream use requires one under `E.18` or `CC‑G5.27`)*
* `DefaultsConsumed :=`

  * `DefaultId.GammaFoldForR_eff`
  * `DefaultId.PortfolioMode`
  * `DefaultId.DominanceRegime`
* `RSCRTriggerSetIds :=`

  * `GCoreTriggerSetId.RefreshOrchestration`
    *(payload: exact changed source and affected-use scope; `SCRId`, `DRRId`; `TaskSignatureRef`, `MethodFamilyRowRef[]`, `CGSpecRef.edition` and `CNSpecRef.edition` for a `Select` result; and the actually applicable `TaskMapRef?`, `GeneratorFamilyRowRef[]?`, `AcceptanceClauseId[]?`, `SoSLogBranchId?`, `FailureBehaviorPolicyId?`, `DescriptorMapRef.edition?`, `DistanceDefRef.edition?`, `TransferRulesRef.edition?`, `InsertionPolicyRef?`, `PathId[]?`, `PathSliceId[]?`, `RSCRTestId[]?`. Nongraph scope uses the existing G.Core `PatternScopeId` branch.)*

#### G.5:4.2 - Dispatcher and Registry object set (notation‑independent)

G.5 defines the **object-set components** below. Their purpose is to make dispatch **possible and auditable** without embedding any method-family semantics in the selector kernel.

**S1 — `MethodFamily Registry` (design-time; project-local or within a selected CG-Frame).**
A reusable row represents one declared grouping. Choose its registry-identity contract: project-local reuse, or intentional registration under a stable public registry identity. This distinction concerns the identity contract, not who can see the row. Both branches fix these replayable values:

* `Identity and continuity`: `MethodFamilyId` names the continuing row lineage; `rowEdition` names one immutable edition; `MethodFamilyRowRef := <MethodFamilyId, rowEdition>` designates that edition. Lineage and Tradition notes and `UTSRowId` remain descriptive or publication values.
* `Exact method members`: non-empty `MethodRef[]`, each resolving to one `U.Method` already admitted under A.3.1.
* `Grouping basis`: exact claim, criterion, or direct relation reference that justifies this row's grouping for the current selector use; if no ontic family or membership relation is directly governed, the basis is explicitly project-local and creates none.

One exact row edition fixes its method members, grouping basis, and every selection-changing pin. Changing any of those values creates a new `rowEdition`; retain the `MethodFamilyId` only while the declared grouping remains the same continuing row lineage. Old `MethodFamilyRowRef` values continue to resolve their old editions. Add task, eligibility, policy, scheme, source, `ClaimScope`, validity, or intended-use pins only when they change selection or a named receiver needs them; none replaces the members or grouping basis.

* `Eligibility and comparison basis`: the actual rule and applicable editions used for this selection, including whether any comparison justifies ordering. A local row may cite its existing project rule; it need not manufacture a public eligibility artifact.
* `Assurance expectations`, only when the local use requires them, with the applicable evidence, unknown and failure rules. A real assurance or minimal-evidence gate keeps every input required by its governing clause.

**Public-registry continuation.** Intentional registration under a stable public identity additionally requires `EligibilityStandardRef` as a typed predicate record (tri-state per G.Core, using CHR/CAL terms and applicable edition pins), `AssuranceProfileRef` for declared evidence-lane expectations and assurance-lane pins, and the UTS naming/continuity obligations of CC-G5.6. The AssuranceProfile states expectations; it is not a B.3 assurance result. The public contract retains the same immutable members and grouping basis. The remaining fields below apply when their subject conditions hold in either branch.
* `AdmissibilityBindings`: when the row is authored for an actual CG-Frame or consumed by its gate, cite its single governance card and gate (`CNSpecRef`, `CGSpecRef`) and every required admissibility constraint, such as scale/unit conditions for a measurement use. An ordinary local grouping with no such use adds no CN/CG reference.
* `EvidencePins`: the source and evidence citations supporting asserted claims or guarantees. Cite `G.6` `PathId` or `PathSliceId` values when that support is represented in a graph or an independently applicable receiving contract requires those citations.
* `CrossingAllowance`: references to the exact F.17 endpoint senses, one obtaining F.9 Bridge, the separate C.2.1 bounded-use proposition, and the current A.10 or B.3 reliance basis, plus CL or observed-loss evidence when material, **only** when expressions with distinct recovered source-local meanings are actually related for this selector use. These are audit references; the field makes none of the referenced facts obtain.

For an actual crossing, first resolve both exact F.17 `SchemeSenseCell` endpoints and establish the two-participant F.9 Bridge under its own predicate profile. Then identify a separate C.2.1 episteme whose exact `EntityOfConcern` is that Bridge and whose ClaimGraph states the proposed use `u`, direction `d`, use-specific rule `r`, tolerated loss `t`, and polarity. For ordinary reliance require the matching current A.10 evidence-provenance path and local `RelianceDisposition`; when an actual named assurance claim is current, use B.3's separate assurance branch. A consequential use without one retains its direct governing rule. Observed loss and CL are evidence, defeater or assurance-policy material, not Bridge participants or permission. Authorization and the actual `Select` application remain with their subject patterns. A Bridge id, `CrossingAllowance`, registry row, policy pin, `CrossingBundle`, DRR or SCR entry cannot substitute for any step.

* `PolicyHooksRef?`: optional pointers to policy records (not defined here; wired via Extensions).

Here “a registry row represents a family” means that the row is the auditable selector-facing record for one declared grouping. The family id preserves that row lineage; the row ref selects one immutable edition for replay. Neither value identifies the grouped Methods, makes a membership relation obtain, or turns a common label, shared description, lineage note, eligibility rule, maturity card, evidence record, or policy into a method-family fact. Changing a row edition changes the registry artifact; it changes a Method or a separate family relation only when that object's direct identity rule or the relation's predicate independently says so.


**S1′ — `GeneratorFamily Registry` (design‑time; optional; per CG‑Frame).**
A reusable row groups generators of tasks and environments, which may co-evolve solver families. It uses the same local/public identity-contract distinction as S1 while retaining its own generator member and signature rules:

* `Identity and continuity`: `GeneratorFamilyId` names the continuing row lineage; `rowEdition` names one immutable edition; `GeneratorFamilyRowRef := <GeneratorFamilyId, rowEdition>` designates that edition. `UTSRowId` is required by intentional public registration; project-local reuse does not require it.
* `Exact generator members`: non-empty references, each resolving to a generator already identified under its subject pattern.
* `Grouping basis`: the independently established classification, membership relation, or explicit project-local criterion that groups those generators for this selector.
* `GeneratorSignatureRef`: conceptual input and output semantics plus budget semantics.
* `EnvironmentValidityRegionRef?`: pinned constraints for generated environments or tasks.
* `TransferRulesRef.edition?`: required when the Open-Ended mode is enabled (semantics come from the cited extension refs).
* `CouplerRefs?`: exact `MethodFamilyRowRef[]` values that may be coupled with this generator-row edition.

Both branches also fix the applicable eligibility/comparison basis and every selection-changing source or policy pin; assurance expectations are conditional on the use. Changing generator members, grouping basis, or another selection-changing pin creates a new generator `rowEdition`; old `GeneratorFamilyRowRef` values continue to resolve their old editions. Intentional public registration activates CC-G5.6 naming, continuity and UTS obligations, with the applicable generator signature and use contracts. It does not import A.3.1 Method membership into generator rows.

**S2 — C.22 `TaskSignature` input and conditional G.4 map.**
C.22 constitutes the `TaskSignature` episteme and defines its edition rule. G.5 consumes its `TaskSignatureRef` and does not reconstruct it from a task, CAL pack, or map. Its function here is pinning and auditability, not over-specification.

When this selector actually uses G.4 CAL gates, it also consumes one exact `TaskMapRef`. Resolve that immutable map edition, require its `taskSignatureRef` to equal the C.22 `TaskSignatureRef` supplied to this selector, and follow its exact `CALCharterRef` and edition-bearing clause, operator, flow, and evidence-profile refs. The map supplies no TaskSignature field and no threshold value. If no G.4 gate is current, omit `TaskMapRef`; an ordinary selector does not need a CAL pack merely to return a truthful bounded result.

For the G.4 safety example, G.5 receives `TaskSignatureRef=SafetyPortfolioTaskSignature-E4` and `TaskMapRef=<SafetySelectionMap, E3>`. The map resolves `CALCharterRef=<SafetyCALCharter, E2>` and the cited gate declarations. A different signature ref or an unresolved charter or component blocks only that gated selector use.

**S3 — `Selection kernel boundary` (run‑time; policy‑governed).**
A notation‑independent selector that:

* consumes `TaskSignatureRef`, exact method- or generator-family row refs, pinned spec refs, and an exact matching `TaskMapRef` only when G.4 CAL gates are current,
* applies the declared eligibility conditions and any assurance gates actually required for this use (tri-state),
* computes an admissible (possibly partial) order,
* returns one declared selector outcome over the exact Method candidates admitted through this kernel: most often `Shortlist` or `RankedShortlist`, and `JointUseSet` only when every returned Method candidate is included for one named use; otherwise it returns one `SpecialistHandoff`, one other narrowed handoff, one abstain outcome, or one escalation outcome (per `DefaultId.PortfolioMode` and explicit overrides),
* emits audit records with pins addressable by DRR and SCR records.

When `TaskMapRef` is present, resolve its exact immutable G.4 map edition before applying any cited gate. Its `taskSignatureRef` must match this selector's C.22 `TaskSignatureRef`; its `CALCharterRef` must recover the CG frame, EntityOfConcern, ReferencePlane, specification editions, and assumption envelope; and each cited clause, operator, flow, and evidence profile must resolve at its exact edition. Carry the exact map ref among the result basis and refresh pins. Do not copy thresholds or acceptance semantics into G.5.

If a cited gate consumes R, resolve the quantity and support model under `CC‑G5.4` before evaluating its threshold. Keep formal and empirical inputs, required premises, complementary support, dependence, scope, and counterevidence distinguishable. No common model means no invented aggregate: retain a qualified synthesis, and apply the clause's unknown behavior only where that missing quantity is actually required. The ordinary selector result in §0.4 is not an assurance claim and needs no new R calculation.

For every `MethodFamilyRowRef` consumed here, resolve the exact immutable row edition and then its A.3.1 `MethodRef[]`, grouping basis, and selection-changing pins before admitting the candidate. Apply the same rule to `GeneratorFamilyRowRef`. The selector may compare or return exact row refs as auditable selector-facing addresses, but row selection neither creates its members nor proves that every listed member belongs, is admissible, is selected, or will be enacted. An unresolved Method reference or missing grouping basis blocks that row's method-bearing use; it is not repaired by a label, description, UTS identity, policy, or evidence pin.

When a selector consumes an organization among Methods, cite an exact `SelectedStructureRef` only after A.22 has independently identified the `U.Structure` from exact constituents, exact already-obtaining relation occurrences, applied constraints, and one named use frame. G.5 neither supplies those discriminators nor selects the Structure by listing it. If the organization instead constitutes one composite Method, consume the exact A.3.1 Method only after B.1.5 has qualified that candidate from its independent parts and whole-forming basis.

S3 states reusable selector behavior. It does not itself perform selection. For an actual selector use, first recover every precise performer's A.13 core for the exact selection action, scope, working situation, and window, including the same obtaining assignment later used by any exact attribution. A.15.1 then independently admits the dated selector Work from its exact performance history, enacted Method, temporal extent, and containing-System relation. State the actual A.6.1 `Select` application, its effective argument bindings, and the A.19 `SelectionSlot` binding for any selected set returned by value. Add F.6 afterward only when the receiving claim needs exact assignment-bound attribution through the same obtaining A.13 assignment. The declaration, planned pins, registry rows, policy, assignment, F.6 relation, and `CandidateSet` type create none of the A.13, Work-admission, application, or result facts.

A compact selector account may omit only an assignment identifier unused by its receiving claim; it omits no criterion, classification, assignment, Work-admission, or attribution fact that the claim consumes. A root-family reference, the same holder, overlapping times, or silence in the receiving text establishes or removes neither the assignment nor F.6 attribution. Ordinary selector discussion not admitted as `U.Work` does not enter this branch.

In this actual-selector branch, the independently admitted dated selector Work and its actual Select application are required. Replay the upstream CPM applications through their own declaration-local bindings; separately admitted comparison Work is required only if the account asserts it. Evidence use, A.10 reliance/provenance, G.11 currentness and a C.2.1 result episteme retain their complete independent grounds when asserted or consumed by the receiving use. A bounded selection that consumes none of these additional claims requires no such additional object.

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
Declare the following S5 outputs:

* `DRR` (decision rationale) and `SCR` (evidence and confidence citation) with explicit pins,
* declared selector and selected-set records produced either by method-family `G.5-3 Select` or by the already-grounded-member `G.5-6 DeclareSetResult` branch,
* telemetry pins to refresh orchestration (`G.11`), without governing orchestration.

S5 governs the selector-facing record boundary, not truth or actuality by record existence. A DRR, SCR, selected-set record, shortlist id, telemetry event, refresh cue, policy pin, or result label does not create dated Work, an actual operation application, the selected-set binding, a domain result, an evidence-provenance relation, assurance, authorization, or publication availability. Persist a selector-result claim as its own C.2.1 episteme when another use must rely on it; connect evidence through A.10, assurance through B.3, authorization through its direct governor, and actual availability through E.24.PUB only when each claim has its independently established basis.


Use §4.4b for outcome kinds and §4.4c for conditional public-identity fields.

**S6 — `Governance and evolution` declaration boundary (design-time).**
Versioning, deprecation, and registry evolution discipline (UTS publication; continuity), without minting new Part‑G‑wide types.

#### G.5:4.3 - Selector head and narrower selector families

Selection and dispatch stay one generic selector head. Narrower selector families may refine it, but they do not redefine the universal invariants pinned through `G.Core`, do not add new mandatory inputs to inherited `Select`, and do not mutate inherited SlotKinds. Required policy and edition refs use the declared input meanings.

Method- and generator-specific pressures such as `QD` archives, open-ended declared sets, explore and exploit lenses, or preference comparators do not become part of the selector head. They arrive only through explicit extension declarations and the pins those extensions require.

#### G.5:4.4 - Selector Relation Fields

| Selector relation                 | Consumes                                                                                                                                                     | Produces                                                                                                                                                                                                                                                   |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **G.5-1 RegisterFamily** | declared local or public registry-identity contract; continuing MethodFamilyId and new immutable row edition; nonempty exact admitted A.3.1 MethodRef[]; obtaining grouping relation or explicit grouping criterion; eligibility/comparison basis; selection-changing source, policy and CHR/CAL/CN/CG pins as applicable; public-continuation fields when selected | One immutable MethodFamilyRowRef = <MethodFamilyId, rowEdition>, resolving the members, grouping, eligibility/comparison basis and applicable pins. Public registration additionally fixes EligibilityStandardRef, AssuranceProfileRef and UTSRowId under S1/CC-G5.6. A local row retains conditional assurance expectations without requiring a public UTS entry. Neither branch creates Methods or grouping facts. |
| **G.5-2 RegisterGeneratorFamily** | declared local or public registry-identity contract; continuing GeneratorFamilyId and immutable row edition; nonempty exact generator refs under their subject patterns; grouping basis; GeneratorSignatureRef; applicable eligibility/comparison, source and policy pins, including TransferRulesRef.edition when required | One immutable GeneratorFamilyRowRef = <GeneratorFamilyId, rowEdition>, resolving those members, basis, signature and applicable pins. Intentional public registration additionally meets S1′/CC-G5.6 naming, continuity and UTS requirements. Local reuse retains the same replayable member/basis core; neither branch creates generator identity or membership. |
| **G.5-3 Select**                  | `TaskSignatureRef`; exact matching `TaskMapRef` when G.4 CAL gates are current; exact `MethodFamilyRowRef[]` in scope whose immutable editions resolve to non-empty exact A.3.1 `MethodRef[]` and exact grouping bases; optional exact `GeneratorFamilyRowRef[]`; pinned `CNSpecRef` and `CGSpecRef` editions; policy refs if any; sufficient audit basis refs, with `PathId` or `PathSliceId` only for actual graph citations or an independently applicable gate or shipping contract | `CandidateSet` (set-returning), declared selector result with `PortfolioMode` recorded, exact row refs and any current `TaskMapRef` among the result basis pins, and `DRR` and `SCR` pins; if no admissible candidate exists: return `CandidateSet = EMPTY` plus an escalation hint (`ActionHint`) and the pins required to plan next steps (P2W split applies) |
| **G.5-4 Compose**                 | `CandidateSet`, composition template refs, pinned admissibility constraints                                                                                       | Composite strategy template (template-level; admissibility-checked; pinned)                                                                                                                                                                                      |
| **G.5-5 Telemetry**               | run outcomes, citations, and policy or edition pins                                                                                                               | refresh cues (typed RSCR causes and payload pins), parity deltas (if parity harness is in use), telemetry pins (selector-side; orchestration governing definition is `G.11`)                                                                                              |
| **G.5-6 DeclareSetResult**        | one exact `SetResultFamily`; exact already identified `memberRef[]`; `namedUse` for `JointUseSet`; ordering; inclusion or selection conditions; and sufficient `basisPins` to the already current choice, pool treatment, accepted decision, or other governed inclusion basis | one `SelectorOutcome` with `SelectorOutcomeKind = SetResultOutcome` and the exact membership form required by that family. For `JointUseSet`, it emits keyed unique `memberEntries`, `ordering = unordered`, the named use, inclusion conditions, and basis pins without a method-family row or `Select` pass. |

`RegisterFamily` produces only the local or public registry row selected under S1. It does not produce any A.3.1 Method or independently governed membership fact. `Select` may address candidates through those rows only after their exact Methods and grouping bases resolve; its returned candidate or selected-set value does not retroactively ground a row member.

`Compose` produces only the pinned template named in its output column. It neither qualifies one composite Method under B.1.5 nor selects one A.22 Structure. When a later selector use consumes either governed object, the exact Method or Structure reference is an independently grounded input rather than a result inferred from this template.

`DeclareSetResult` begins only after its exact members and inclusion or selection basis are current. An upstream C.11 `ChoiceResult`, C.19 pool treatment, accepted decision, or another governed basis may appear among `basisPins`; the G.5 branch does not repeat or perform that decision. It declares the selector-facing set-result content and stops. It creates no member identity or relation, method-family row, `Select` application, dated selection Work, persisted C.2.1 result episteme, assurance or authority claim, or E.24.PUB availability occurrence.

#### G.5:4.4a - Worked selector slice

- A catalyst-search team is choosing among three method families for the same declared `TaskSignature` and `C.22.1` adaptation signature.
- The shared profile pins one work-measure threshold target, one freshness window, one prior-exposure declaration, and one adaptation budget. One family reaches threshold quickly but carries high downside on adjacent tasks. One family is slower but transfers cleanly. One family never clears `MinimalEvidence` and must receive an abstain verdict.
- The `G.5` result in this slice therefore declares one unordered `Shortlist` retaining the first two families, with DRR and SCR records citing why the third family was excluded and why the first two remain non-dominated. The selector does not invent one scalar winner and does not hide the specialization profile in auxiliary side notes.
- If the project also claims that this selection actually occurred, A.13 first recovers `CatalystSelectorSystem-17 : U.System` for exact action `CatalystFamilySelectionAction-17`. `CatalystSelectorBoundary-17` contains the deployed selector runtime, its effective policy state, and its registry/evidence interfaces; it excludes the method-family rows, `TaskMap`, result records, assignment, and containing team System. The action applies the effective selector to the three candidate families and returns the retained set. Its scope is `CatalystFamilySelectionClaimScope-17`, its working situation is `CatalystSearchSelectionSituation-17`, and its window is `2026-07-30T10:00:00Z` through `2026-07-30T10:08:00Z`. `CatalystSelectionAdmissibilityNorm-17` directs the selector to exclude candidates that fail `MinimalEvidence`, preserve admissible non-dominated alternatives, and abstain rather than manufacture a scalar winner. Relevant conditions include the exact `CatalystTaskSignature-17`, current row and map editions, eligibility evidence, comparison policy, and adaptation-signature values.
- A.2 declares local agential kind `CatalystMethodSelectorSystemRole`. Its membership criterion requires the stable work-facing contribution of method-family selection and goal-directed, condition-sensitive regulation under `CatalystSelectionAdmissibilityNorm-17`: the holder must apply the current gates, preserve the admissible set-return semantics, and abstain or escalate when no candidate qualifies. `CatalystSelectorDecisionTrace-17` shows `CatalystSelectorSystem-17` excluding the third family for failed `MinimalEvidence`, retaining the first two as non-dominated, and emitting no scalar winner. The trace and boundary/runtime records support the criterion facts under A.2's membership rule; A.10 makes that source-to-use account recoverable. The case independently classifies `CatalystSelectorSystem-17` under `CatalystMethodSelectorSystemRole`; neither the assignment nor the candidate Work supplies the classification. No Grade, autonomy result, characteristic profile, or stronger assurance claim is consumed.
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

- `SelectorOutcomeKind = SetResultOutcome`, whose closed `SetResultFamily` value set is `Shortlist` when alternatives are retained for later choice and the result does not order them, `RankedShortlist` when the result orders those retained alternatives, and `JointUseSet` when every named member is included for one named use;
- `SelectorOutcomeKind = HandoffOutcome`, with `HandoffKind = SpecialistHandoff` or one other narrowed handoff plan when heterogeneity is the truthful downstream result;
- `SelectorOutcomeKind = AbstainOutcome` when no admissible candidate exists and the truthful result is one abstain; and
- `SelectorOutcomeKind = EscalationOutcome` when no admissible candidate exists and the truthful result is one escalation.

`G.5-3 Select` may emit one of these outcome kinds only over the exact Method candidates admitted through its kernel; `G.5-6 DeclareSetResult` emits `SetResultOutcome` from exact already identified members and a current inclusion basis. Neither branch performs an upstream choice, makes a member relation obtain, or proves actual selection Work.

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

`sourceSetFamily` may name a declared `Front`, `Q-front`, `ExplorationArchive`, `Archive`, current pool subset, or derived tradition view. For retained alternatives, `publicSelectedSetLabel` normally names `Shortlist` or `RankedShortlist` and may use a domain label such as `StyleShortlist` or `TraditionShortlist` only when the term bridge is already clear. `JointUseSet` is not a shortlist label: it names an all-member result and therefore uses `namedUse` plus keyed `memberEntries`. G.5 does not create the archive, compute the comparison, govern the pool policy, decide the cultural-evolution case, establish member identity or relations, or repair the term bridge. Use `C.18` for archive formation, `A.19.CPM` for comparison, `C.19` for pool policy, `C.36` for cultural-evolution claims, each member's own identity and relation patterns for those facts, and `F.17`/`F.18`/`F.9` for local meanings, naming settlement, and any obtaining term Bridge.

#### G.5:4.4c - Result-declaration quick card

Use the outcome definitions in §4.4b and fill only the applicable fields:

| Field | When and what to state |
| --- | --- |
| `selectorOutcomeKind` | Every result: the admitted set, handoff, abstain or escalation kind. |
| `setResultFamily`, `members` | For retained alternatives: the admitted shortlist family and exact surviving refs; preserve a justified order for `RankedShortlist`. |
| `setResultFamily`, `namedUse`, `memberEntries`, `inclusionConditions` | For joint inclusion: `JointUseSet` and its §4.4b keyed membership declaration. |
| `handoffKind`, `handoffContent` | For a handoff: `SpecialistHandoff` or another admitted narrowed handoff and the content the next receiver needs. |
| `blockingPins` | For abstain or escalation: the actual blocking conditions. |
| `ordering` | Ranked, unordered or not applicable, as the outcome permits. |
| `basisPins`, `nextUse` | The supporting basis and next use boundary; `none` when there is no next use. |
| `publicId` | Only when stable public identity is needed; `ShortlistId` is specific to a shortlist. |

The pump result in §0.5 and the joint-use declaration in §4.4b show complete filled forms. A missing required value leaves the result incomplete.

#### G.5:4.4ca - Derived tradition-view result stays derived over one declared palette

When the source is `TraditionFront` or `TraditionArchive`, keep its base `SoTAPaletteDescription` recoverable. State `SourceSetFamily`; add `DerivedViewKind` when it changes interpretation or later publication and `SourceSetComposition` only when several source-set families were actually composed. Cite the derivation's declared Q, reachability or coverage rule among the DRR/SCR or equivalent basis pins. The view qualifies the source; §4.4b still defines the emitted outcome.

#### G.5:4.4d - Worked result-declaration closure slice

| Receiving situation | Complete result and changed action |
| --- | --- |
| The two pump Methods in §0.5 survive, with no admitted ordering. | Emit its unordered `Shortlist`; the receiver still has a choice to make. |
| A declared comparator orders family_B before family_A for the specialist handoff. | Emit a `RankedShortlist` with `[family_B, family_A]`, the comparator and supporting basis pins, and the handoff use. A request for an order alone supplies no comparator. |
| The cohort decision includes `Core@C`, `Domain@D` and `Local@L` together. | Emit the §4.4b `JointUseSet`; the receiver uses all three exact editions under the inclusion conditions. |
| No candidate clears the applicable admissibility/evidence gates. | Emit `AbstainOutcome` or `EscalationOutcome`, naming the blocking pins, basis and next use; an empty shortlist leaves the stop unexplained. |

The following extensions apply only when their corresponding mode is active. Their declared `Uses` and pins cite the governing semantics.

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
* `RSCRTriggerKindIds`: `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.EvidenceSurfaceEdit}`
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


#### G.5:4.4e - Source sets, operating modes and comparison policy

Use §4.4b for the emitted outcome and §4.4bb–ca for its source and public-label interpretation. An actual `SelectionSlot` binding carries the by-value selected candidate set; it is separate from G.5's declared `SelectorOutcome`. `ChoiceSet` remains an ordinary mathematical set gloss, not an additional public result kind.

| Declaration | Meaning and applicable condition |
| --- | --- |
| `Front` | The non-dominated source set under the declared `DominanceSet`. |
| `Archive` | The exploration set retained under its policy. |
| `PortfolioMode` | How the selector operated. The default `Archive` retains exploration evidence; it establishes neither an emitted Archive nor a different result family or DominanceSet. |
| `SourceSetFamily`, `SourceSetComposition` | State the immediate source family; use composition only when several source families were actually consumed, for example a front and an archive. |
| `DerivedViewKind`, `BasePaletteRef` | Qualify an actual derived view under §4.4ca; the latter is a reference, not a kind. |
| `PromotionPolicy` | Required when tie-break or telemetry signals are promoted into dominance. |
| `SubjectKind`, `RetentionIntent=steppingStone` | Qualify the relevant declaration or retention policy; neither names another emitted set result. |

Use controlled tokens, cited ids or already declared head labels for these fields. CostToProbe, ValueOfInformation, ValueOfComputation, explore_share, graduation conditions and sequencing pressure belong to the surrounding choice doctrine when they affect the decision; a result field does not establish them. All-member membership and candidate/exclusion records retain the separation in §4.4b.

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

