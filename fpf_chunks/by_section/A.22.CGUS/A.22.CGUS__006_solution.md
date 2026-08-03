---
chunk_kind: "child"
pattern_id: "A.22.CGUS"
pattern_title: "Constraint-Governed Unfolding Structure"
section_id: "A.22.CGUS:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.22.CGUS/A.22.CGUS__006_solution.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "A.22.CGUS — Constraint-Governed Unfolding Structure"
  - "A.22.CGUS:4 — Solution"
line_start: 34852
line_end: 35124
dependencies:
  - "A.22"
  - "A.6.3.NAR"
  - "B.3.5"
  - "B.5.2"
  - "C.13"
  - "C.18"
  - "C.19"
  - "C.2.P.DR"
  - "C.3"
  - "C.32.P2S"
  - "C.33"
  - "C.35"
  - "E.10.MOVE"
  - "E.11"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.18.3"
  - "E.18.NET"
  - "E.18.NET-conforming"
  - "E.23"
  - "F.17"
  - "G.11"
  - "G.5"
keywords:
---

### A.22.CGUS:4 - Solution

Select `ConstraintGovernedUnfoldingStructure` as an A.22 profile of one selected `U.Structure`. Its exact independently identified constituents, selected obtaining relation occurrences, applied constraint claims, and named selection-use frame satisfy the four A.22 identity discriminators. `selectedCGUSRef` designates that selected organization being unfolded, not a topic label, container, record, or declared-use phrase. Typed position locators, relation signatures, guards, preserved and lost structure, admissible next-form kinds, and stop or return conditions make that selected organization usable; they do not create a parallel context or card ontology.

A constraint-governed unfolding structure states which continuations are admissible from the current selected organization and why. It makes no displayed-order claim about real work and fixes no cardinality of starting records, starting structures, or later results. It may branch, merge, cycle through subject relations, remain partially ordered, or leave alternatives live at once. A route, graph, table, narrative, prompt path, or seminar sequence may help a reader inspect it, but form and adjacency establish neither the structure nor any relation occurrence.

A narrower pattern such as `E.18.3` may recognize the same selected `U.Structure` under an additional transformation-flow membership condition. Do not manufacture a generic CGUS object plus a second narrower structure from reciprocal references. The current EntityOfConcern is the one selected structure whose exact A.22 discriminators and applicable narrower predicate are satisfied.

#### A.22.CGUS:4.1 - First useful structure result

Start with the smallest recovery aid that answers the working question:

```text
selectedCGUSRef: one exact selected U.Structure
selectedConstituentRefs[]: independently identified objects and already-current structures
selectedObtainingRelationOccurrenceRefs[]: exact occurrences already admitted by their direct owners
appliedConstraintClaimRefs[]: exact constraints used by this selection
namedSelectionUseFrame:
  questionOrAction: the concrete continuation decision this structure supports
  forbiddenOverread: what this selection does not establish
positionLocatorRows[]:
  positionSlotSpecRef: one exact A.6.5 SlotSpec
  selectedConstituentRef: one exact constituent occupying that position
  constituentKindRef: the constituent's independently governed kind
  directGovernorRef: the exact governing-pattern identifier or reference for that constituent
relationSignatureRefs[]: declarations for relation kinds actually used
guardedContinuationRows[]:
  exactGuardOrConstraintClaimRef
  selectedObtainingRelationOccurrenceRefs[]
  admissibleContinuationDescription
preservedStructureRefs[]
structureInformationAdequacyNoteRefs[]?: exact C.33 epistemes for captured, expected-but-uncaptured, lost, or hidden structure
admissibleNextFormKindRefs[]
stopCondition
governingPatternReturnConditions[]:
  conditionClaimRef: exact claim stating the return condition
  affectedStructureRef: exact selected structure whose use is bounded
  conditionalReceivingPatternRef: exact neighboring governing-pattern identifier or reference
currentnessRelationOccurrenceRefs[]?: exact already-obtaining G.11 or other directly governed currentness occurrences used by this selection
returnCondition: the first identity discriminator, guard, use, or source-currentness change that reopens selection
```

This is a recovery aid, not a new record kind and not an identity tuple with extra fields. The first four rows are exactly the A.22 identity basis. The remaining rows expose how the selected structure is being used and when to return. A row does not create its constituent, make its relation obtain, admit its constraint, or establish its direct governor.

For an admitted filled position, use the reference shape

```text
CGUSPositionLocator := <selectedCGUSRef, positionSlotSpecRef, selectedConstituentRef>
```

The locator resolves one constituent already selected into the structure. It is not a `U.Relation`, a new U-kind, or a replacement for the constituent's identity. An unfilled or merely proposed position remains claim content in a provisional demonstration; it does not become an admitted position by occupying a table row. `directGovernorRef` points to the governing pattern or exact declaration that owns the current object or relation. A pattern reference is not thereby a `U.MethodDescription`.

Every selected relation occurrence keeps its direct participant meanings, obtaining predicate, applicability, occurrence identity, and governor. A relation signature helps recover that declaration; an edge label or adjacency row is insufficient. A guard can constrain admissibility only through its exact current claim or obtaining relation under its owner. A stop or return sentence is a use boundary unless a direct pattern independently admits a relation occurrence for it.

Accepted starting records and starting structures remain different constituents. A record may describe, publish, evaluate, or recommend use of a structure without becoming that structure. A selected recommendation, intended realization, imperative sentence, or filled form establishes neither an obtaining relation nor Method, `U.MethodDescription`, `U.WorkPlan`, dated `U.Work`, or actual `U.Transformation`.

#### A.22.CGUS:4.2 - Admission test

A readable chain is not sufficient. Admit the CGUS use only when all applicable coordinates below are recoverable:

| Coordinate | Recovery for CGUS admission | Reduced use when absent |
| --- | --- | --- |
| A.22 structure identity | Exact independently identified constituents, exact selected obtaining relation occurrences, exact applied constraints, and one named selection-use frame. | Keep the current note, record, graph, table, or description and return the missing discriminator. |
| Typed positions | More than one filled `CGUSPositionLocator`, each resolving an independently governed constituent through one exact SlotSpec. | Keep candidate positions in a provisional demonstration. |
| Connecting relations | Direct relation declarations plus exact already-obtaining occurrence refs among selected constituents. | Keep an index or proposed connection until the direct predicate and occurrence are recoverable. |
| Cross-position constraints | Constraints, invariants, guards, branches, joins, cycles, partial orders, or many-to-many dependencies that change admissible continuations. | Keep a linear presentation as a provisional demonstration. |
| Preserved and omitted structure | Preserved structures and any C.33 adequacy notes needed by the declared use. | Narrow the use, state the loss, and retain the return condition. |
| Admissible next forms | Exact next-form kinds and the current conditions that keep each alternative live, not one forced next record. | Do not claim a usable unfolding structure. |
| Direct governing-pattern exits | Every stronger method, plan, work, transformation, production, evaluation, evidence, decision, publication, architecture, currentness, or mathematical claim points to its exact owner. | Stop the overread and use the owner of the actual claim. |
| Use boundaries | The concrete action, forbidden overread, ordinary stop, exact neighboring return, and reopen condition are explicit. | Keep the artifact as a one-use explanation. |

Branches and joins that are current remain visible. A subject-relation feedback cycle may be current without making selected membership cyclic. One displayed slice may be linear because attention needs one path; the selected structure remains graph-shaped when its exact relations are graph-shaped.

When transformation-flow vocabulary is current, decide among three ontically different cases before admitting the demonstration:

| Case | Exact object | Boundary |
| --- | --- | --- |
| Several `FlowValuation` values resolve to one exact `TransformationFlowStructure` | the same one TFS under E.18 | a changed valuation, path slice, or local tag does not mint another flow |
| A detailed portion resolves only through positions and internal `U.Transfer` occurrences of one exact parent TFS | one parent-relative E.18 `SubflowRef` | detail does not become an independent TFS or network member |
| Two or more independently identified TFS or nested-network values need exact obtaining relations across member boundaries | one recursively selected E.18.NET `TransformationFlowStructureNetwork : U.Structure` | do not flatten the members into one giant TFS |

A CGUS description or slice may present any admitted case, but its graph shape does not select the TFS, SubflowRef, or network. Every independently selected network member retains its own boundary, Work, actual transformations, valuations, and local composite flow-position locator.

#### A.22.CGUS:4.3 - Provisional descriptions, structure descriptions, and demonstrative slices

Keep three epistemic uses separate from the selected structure. Each is an ordinary C.2.1 episteme identified by its exact `<ClaimContent, EntityOfConcern, effective ReferenceScheme>` triple. The labels below describe the current use; they add no ambient context field or second episteme identity.

**Before admission — provisional unfolding demonstration.** Its exact EntityOfConcern is the actual subject-domain object, question, or proposed continuation set, never a not-yet-admitted CGUS. Its ClaimContent may name visible candidate positions, proposed relations, possible continuations, presentation form, every unresolved admission coordinate, and the exact condition under which those coordinates would be resolved. Those claims guide discovery but create no constituent, admitted position, structure identity, relation occurrence, Method, plan, Work, or transformation. At least one unresolved coordinate remains explicit while the demonstration is provisional. When every coordinate is recovered, constitute a separate description or slice about the admitted CGUS; do not retype the provisional episteme.

**After admission — whole-structure description.** Its exact EntityOfConcern is the admitted CGUS. Its ClaimContent may describe positions, branches, joins, cycles, partial orders, exact relation occurrences, constraints, admissible next forms, preserved structure, relevant C.33 losses, declared use, and return condition without selecting one traversal. Diagram form, table layout, carrier, and publication location do not identify the episteme or the structure. Changed claim content, EntityOfConcern, or effective reference scheme identifies another episteme; a changed form, carrier, viewpoint qualification, publication occurrence, or model-use qualification does not by itself.

**After admission — demonstrative unfolding slice.** Its exact EntityOfConcern is the admitted CGUS, while its ClaimContent selects one traversal or ordering for a declared demonstration use. The slice cites only already admitted position locators and exact relation-reference epistemes or obtaining occurrence refs; it records relevant omissions and alternatives. It neither retypes a provisional explanation nor creates the selected structure. It may cite the earlier provisional episteme only through an exact source, derivation, or viewing-construction claim under its direct owner; mere file history is not such a relation. If later inspection invalidates CGUS admission, withdraw the slice claim while retaining any still-truthful provisional explanation under its narrower declared use.

Viewpoint, claim scope, empirical grounding, model-use structure, publication occurrence, form, carrier, and historical edition continuity remain optional neighboring uses under their direct patterns. Add one only when the current receiving use needs it. None enters the C.2.1 identity triple or structure identity, and neither a viewpoint nor a grounding holon is intrinsic merely because the episteme is a description.

Use this compact recovery shape for the slice's ClaimContent when needed:

```text
demonstrationUse: worked example | first-use example | actual-case replay | variant comparison | other declared use
presentationForm: ordered list | chain diagram | flow card | table | narrative path | slide sequence | prompt block | graph slice | other declared form
sourceProvisionalDemonstrationRef?: exact separately identified source episteme, with its direct source/derivation relation when claimed
selectedTraversalDescription
includedPositionLocators[]: exact admitted CGUSPositionLocator values
selectedRelationReferenceRefs[]: exact already-admitted relation-reference epistemes or obtaining occurrence refs
omittedStructureInformationAdequacyNoteRefs[]?: exact C.33 epistemes
alternativeSliceRefs[]?: separately identified slice epistemes
loopCompressionClaimRef?: exact episteme stating which repeated branches are omitted or compressed for this use
presentationOrderingClaimRef: exact episteme stating why this traversal or order is shown
admissibleUse
forbiddenOverread
sliceReturnCondition
oneTFSLocator?: complete one-TFS locator family
networkDemonstrationLocator?: complete network locator family
```

The loop-compression claim and presentation-ordering claim answer different questions and remain separately revisable. Neither is presumed to be a `U.MethodDescription`. One has that dependent membership only if A.3.2 independently finds one admitted `U.Method` as its exact EntityOfConcern and a substantive way-of-doing claim. Imperative grammar, ordering, intended realization, repeatability, recipe appearance, or inclusion in the slice is not enough. The local use and presentation-form vocabularies are Plain closed choices for this recovery aid, not U-kinds, carriers, or identity discriminators.

The one-TFS and network locator families are mutually exclusive. A one-TFS slice has the complete `<transformationFlowStructureRef, pathSliceId, DesignRunTag>` family and no network locator. A network slice has one `networkDemonstrationLocator` and none of those three top-level values. A generic CGUS slice may have neither family. No partial or mixed family is admissible.

For a network demonstration, retain this locator content by value:

```text
networkDemonstrationLocator:
  transformationFlowStructureNetworkRef: one independently selected E.18.NET-conforming network
  selectedNetworkPositionMappingRows[]:
    networkPositionRef: FlowPositionRef | ExposedFlowPositionRef
    memberPath[]: finite ordered path of exact direct-member refs
    admittedIncludedPositionLocator: the same exact CGUSPositionLocator already included in this slice and its admitted E.18.3 structure
  selectedCrossFlowRelationReferenceRows[]?:
    networkCrossFlowRelationRowRef: exact E.18.NET NetworkCrossFlowRelationRowRef
    admittedTransformationFlowRelationReferenceRef: exact E.18.3 relation-reference episteme already used by the admitted structure
  memberLocalFlowLocatorRows[]?:
    memberPath[]: finite ordered path to one leaf TFS
    transformationFlowStructureRef: that exact leaf TFS
    pathSliceId: local to that leaf TFS
    DesignRunTag: local to this exact leaf position binding
    leafFlowPositionRef: FlowPositionRef in that TFS
    positionBindingRef: already governed E.18 position/valuation binding
```

The locator does not admit structure. Resolve every member path hop through exact direct members. A `FlowPositionRef` names the final TFS. An `ExposedFlowPositionRef` must repeat the same network, complete member path, and leaf position; otherwise omit the mapping. The included locator must be the same exact admitted position already present in the slice and the E.18.3 structure, not a copied raw-position list.

Resolve every selected cross-flow row first through the exact current E.18.NET record edition for this same network and require exactly one match on occurrence plus complete ordered endpoint-binding identity. Then resolve the cited E.18.3 relation-reference episteme separately. The row and episteme must agree on exact occurrence, relation kind, direct governor, signature, participant order, endpoint members, positions, and bindings. A record row, raw occurrence ref, edge label, unresolved locator, or diagram adjacency alone is not admitted.

The complete one-TFS locator may recur only in a member-local row for one leaf position. A network slice has no global `FlowValuation`, `pathSliceId`, or `DesignRunTag`; every valuation, slice, tag, Work reference, actual transformation reference, and boundary remains local to one exact member or leaf-TFS binding. Network membership paths are finite and acyclic, while exact cross-flow feedback relations may form cycles when their direct owners permit them.

Every selected cross-flow relation remains the exact occurrence admitted by its direct owner; do not substitute universal `creates`, `produces`, `uses`, `input`, `output`, `result`, `handoff`, or `transfer` edges. A C.32.CONWAY result can contribute at most one exact transformer-role-system/transformed-holon architecture-correspondence occurrence as one qualified network row after its direct occurrence and endpoint bindings are recovered; it is never the whole network. A source phrase or source graph enters only through an exact source-to-use claim or relation. A bounded model-use structure appears only when the receiving assertion or use explicitly selects that already identified structure for one independently obtaining crossing; shared wording, adjacency, or the crossing display creates neither.

**Positive case.** A four-level build-the-builder demonstration follows a finite member path to one already admitted leaf position, maps it to the same included CGUS/E.18.3 position, cites one exact admitted cross-flow relation-reference episteme, and keeps the path slice and tag in one leaf-local row. **Near miss.** A graph supplies raw positions or an edge label, mixes locator families, duplicates positions, or assigns one tag to the network; keep it provisional or return the exact missing member, relation, position, or binding.

#### A.22.CGUS:4.3.1 - Plain `move` and displayed continuations

`Move` is not a universal U-kind, record, or relation. In a display, *move* remains Plain wording and must resolve to the exact current object: a proposed PlanItem, pattern-use recommendation, admitted CGUS continuation, dated performed `U.Work`, actual `U.Transformation`, or another independently governed occurrence. Proposed or chosen work remains distinct from performed Work; no shared move identity connects them.

```text
displayedContinuation:
  plainMoveLabel
  exactCurrentObjectRef
  exactCurrentObjectKindRef
  directGovernorRef
  actionOrProposedUseClaimRef
  directPatternRef
  practicalUseQuestionClaimRef
  relevantSolutionClaimRef
  expectedResultClaimRef
  currentContinuationConditionClaimRef
  alternativeContinuationRefs[]?
  returnContinuationRefs[]?
  sourcePracticeContinuationRef?: exact source episteme plus direct source-to-use relation
  basis: exactly one public-template basis or project-candidate basis
  nestedPatternSelectionClaimRef?: separate claim-bearing episteme
  applicabilityFindingRef?: only if already current
  recommendationRef?: only if already current
  workPlanRef?: only if one U.WorkPlan already exists
  performedWorkRef?: only if one dated U.Work already exists
```

This is display content in the slice's ClaimGraph, not a universal row type. `expectedResultClaimRef` is always recoverable for a result-bearing display but creates no result or result relation. A nested selection claim may return a candidate, finding, or recommendation to the display; it neither becomes the enclosing continuation nor performs it.

A displayed continuation may show the direct pattern, the practical-use question, the relevant Solution claim, the expected result claim, its current condition, alternatives, and return. It uses exactly one public-template or project-candidate basis and does not merge the two. Its source-practice continuation is cited only through an exact source-to-use relation. If the direct pattern is unresolved, stop that continuation and open a separate nested pattern-selection claim; the returned candidate, finding, or recommendation neither becomes the enclosing continuation nor performs it. Applicability finding, recommendation, WorkPlan, and Work remain separate and appear only when those values already exist. A filled row, an imperative verb, or selection wording performs nothing.

If a display says `next move: prepare the realization plan`, first identify whether the current object is an admitted CGUS continuation toward a possible `U.WorkPlan`, an already current PlanItem, or actual plan-authoring Work. The phrase establishes none of them. Open A.15.2 for the plan and A.15.1 for dated Work only when their own conditions are satisfied.

#### A.22.CGUS:4.3.2 - Pre-execution slot-filling scaffold

A provisional demonstration can hold attention on candidate positions before execution and before CGUS admission. First name the visible positions. Then recover the exact constituents, kinds, relation declarations and occurrences, constraints, invariants, guards, preserved structure, C.33 notes, next-form kinds, and stop or return conditions that would satisfy `4.2`. Keep every unresolved coordinate in the provisional episteme's ClaimContent.

**Minimal first use.** Show candidate positions `candidate`, `evaluate`, and `repair`; state that the relation and guard making repair conditional on an evaluation result are still proposed; and show both `accept candidate` and `repair candidate` as possible continuations. This helps the team hold a branch in attention. It remains a provisional description until the exact constituents, direct relation occurrence, guard, preserved structure, and use boundary are recoverable.

After admission, create a separate demonstrative-slice episteme and map only recovered material to exact position locators and relation refs. Neither the provisional nor admitted presentation asserts project Work order or authorizes Work.

#### A.22.CGUS:4.3.3 - Local mantra, filled use, and naming boundary

A local *mantra* is Plain compact recall wording for applying one pattern Solution. For A.22.CGUS use:

> **Objects — obtaining relations — constraints — next form; otherwise stop and return.**

The formula helps answer one working decision: *does the current selected organization admit this continuation, or must the practitioner stop and return to a neighboring governor?* Its terms map as follows:

| Formula term | Governed value |
| --- | --- |
| Objects | exact independently identified constituents and already-current structures |
| obtaining relations | exact selected occurrences under their direct relation owners |
| constraints | exact applied constraint claims, invariants, and guards used by the selection |
| next form | one admissible next-form kind and its current condition, not a forced record or performed step |
| stop and return | the ordinary non-admissible condition and one exact neighboring governing pattern |

**Filled architecture use.** The working decision is whether `prepare realization plan` may remain visible after a cooling-architecture choice. `CoolingStructure-v2`, exact composite project Work `CoolingUpgrade-2026`, `ArchitectureDecisionRelation@Project#AD-17` under `C.32.PAD`, and `ArchitectureUnfoldingStructureUse@Project#AU-17` under `C.32.P2S` are independently recovered. The selected relation occurrences are the exact decision and unfolding-structure-use relations; the applied constraints are `ThermalMarginConstraint` and `ServiceAccessConstraint`. The admissible next-form kind is `U.WorkPlan`, so *next move* is only Plain wording for the admitted CGUS continuation `prepare realization plan`. If the exact C.32.P2S use relation does not obtain—for example because its exact composite Work participant is absent—stop the CGUS continuation and return to `C.32.P2S`; do not infer project locality from `@Project`, create a plan from the display, or report performed Work. If a plan later exists, A.15.2 owns it; if dated realization Work occurs, A.15.1 owns it.

The mantra is neither `U.Method`, `U.MethodDescription`, `U.WorkPlan`, performed `U.Work`, CGUS, nor a demonstrative slice. Imperative grammar does not admit a kind or execute anything. A displayed traversal is a separate C.2.1 episteme only after the CGUS is admitted. A cross-pattern long-memory aid may point to a distant result, but each intermediate object and relation retains its direct owner; it is outside this local-mantra rule unless one A.22.CGUS decision is the current use.

In public explanation, *demonstrative walkthrough* may remain Plain wording for a post-admission slice. *Mantra* names the recall formula above, not that slice, and *mantra move* creates no demonstrated-row kind. Established local words such as *mnemonic*, *watchword*, or *heuristic* may remain when they truthfully tell that pattern's readers what the aid does; a memorable acronym, title, or retrieval cue is not thereby a mantra.

If a seminar or another source uses those expressions differently, keep these decisions separate:

1. `F.17` identifies each exact local sense under its reference scheme and exact source basis; no carrier or remembered wording creates the sense.
2. `F.18` settles a local or public name only when that naming use is current; a NameCard is unnecessary for ordinary Plain wording and never creates the governed value.
3. `F.9` may establish one exact Bridge between two sense cells with its direction, predicate, applicability, and loss. The Bridge establishes neither governed-value identity nor permission to use it. In particular, the recall-formula sense of *mantra* and the demonstrative-slice sense of *walkthrough* are not one value merely because an earlier seminar used the first word for the second.
4. A separate C.2.1 assertion states the proposed receiving use, direction, correspondence rule, tolerated loss, and polarity. A.10 governs below-threshold reliance; B.3 opens only for a current assurance claim or material-reliance threshold.
5. The source episteme, publication occurrence, publication form, and carrier remain different objects. Dictionary evidence can support lexical interpretation; it cannot establish the Bridge, use claim, structure, relation occurrence, publication, Method, plan, or Work.
6. Changed local sense reopens that sense basis; changed Bridge endpoint or predicate reopens the Bridge; changed receiving use or tolerated loss reopens the C.2.1 use claim; changed evidence or threshold reopens only reliance. Changed wording reopens none of the selected structure's four A.22 discriminators unless the actual selected organization also changed.

This naming boundary preserves three useful distinctions without a local card ontology: the selected CGUS is world-side structure; a demonstrative walkthrough is a claim-bearing episteme about one traversal; and a mantra is Plain recall wording for one decision. Changes to wording reopen only the naming or source-use claim unless the selected structure's four A.22 discriminators actually change.

#### A.22.CGUS:4.4 - Direct Governing Pattern Exits

CGUS carries the unfolding structure. It does not absorb stronger claims.

| Stronger claim being made | Direct governing pattern or family |
| --- | --- |
| Atomic bounded change | `A.3.4` |
| Method or method description | `A.3.1`, `A.3.2`, and method-composition patterns |
| Work plan, work entry, or performed work | `A.15.2`, `A.15.5`, `A.15.1`, and neighboring work patterns |
| Evidence, assurance, or gate | `A.10`, `B.3`, `A.20`, `A.21`, `G.6` as current |
| Architecture use, architecture decision, or architecture description | `C.30`, `C.30.ASV`, `C.32.P2S`, `C.32.PAD`, `C.32.ADR`, `C.30.AD` |
| Variant archive, non-dominated front, live pool, or selected-set publication | `C.18`, `C.19`, `G.5` |
| Narrative rendering or publication use | `A.6.3.NAR`, `E.17`, `E.17.0` |
| Improvement of an object version | `E.23`, with evaluation patterns for the declared object |
| Source currentness, decay, edition shift, or refresh orchestration | `G.11` |
| Mathematical lens or formal modeling | `C.29`, `A.6.0`, `A.6.1` |

Use the word `refresh` only when a currentness, telemetry, edition, decay, or slice-local refresh claim is actually current. Otherwise use plain return, stop, split, or repair wording and name the direct governing pattern.

#### A.22.CGUS:4.4a - Direct governing-pattern dependent uses

Some CGUS uses cite adjacent method, plan, work, evidence, architecture, description, or publication objects. A.22.CGUS defines no generic linkage record for them. Select an adjacent relation occurrence into the CGUS only after its direct owner supplies the relation kind, participant meanings, obtaining predicate, applicability, occurrence identity, and current affirmative facts.

For method and work, keep one admitted `U.Method`, any already identified C.2.1 episteme, A.3.2 `U.MethodDescription` membership when its exact EntityOfConcern is that Method and its ClaimContent crosses the substantive way-of-doing threshold, `U.WorkPlan`, readiness claim, dated `U.Work`, actual `U.Transformation`, work-to-change claim, A.15.PROD production or inception claim, evidence, assurance, and gate result separate. A.3.4 independently identifies every actual transformation from its changed referent, extent or ordering boundary, conditions, actual change facts, and continuity rule. Intended realization use, a plan seed, imperative grammar, placement in a CGUS, shared Work, or adjacency admits none of these objects and establishes no transformation composition. Open A.15.PROD production, identity-inception, or completion only for the exact current claim; do not infer production or holonhood for every transformation. If only one adjacent claim is current, cite that exact object or occurrence rather than constructing a multi-stage linkage.

For architecture use, use the C.32.P2S-owned `ArchitectureUnfoldingStructureUse@Project` only when its exact predicate obtains. `@Project` is a compatibility and retrieval cue only. Every asserted occurrence includes the exact composite `U.Work` as a participant and the direct relation that connects that Work to this unfolding-structure use. C.32.PAD likewise owns `ArchitectureDecisionRelation@Project` and its exact composite-Work participation. A.22.CGUS neither infers nor owns either project-work relation.

If the current claim is only grounded architecture, structural view, architecture description, decision, ADR-like projection, measurement, evaluation, planned or performed realization Work, or actual structure, use its direct governor. P2S selected and expected structures remain claim content until their world-side obtaining basis is independently recovered; realization Work and actual structures remain world-side and are not created by a decision, description, model, table, or intended realization.

This keeps A.22.CGUS thin: it owns the selected constraint-governed structure and its safe next-use boundary, while A.15, A.3.4, A.15.PROD, C.30, C.32, evidence, gate, publication, source-use, evaluation, and domain patterns own adjacent objects and relations.

#### A.22.CGUS:4.5 - Promoted Core Family Cue Examples

The FPF core may promote a few short family cues when a cue helps readers recover a familiar governing pattern and a common blocked overread. This is an example device, not a maintained list of all CGUS families.

For example, `UF.P2S` can be useful when an architecture-facing question moves from problem pressure to candidate, selected, expected, or actual structures. The cue points the reader toward `C.32.P2S` and warns that a P2S card is not itself the architecture decision, architecture description, ADR, or realization work.

For example, `UF.IMP` can be useful when an object version, evaluation frame, candidate repairs, and re-evaluation are current. The cue points toward `E.23` and warns that a retry loop or prompt loop is not quality improvement by shape.

For example, `UF.REFRESH` can be useful when a `G.11` source-currentness relation, telemetry, evidence decay, or edition shift is current. The cue points toward `G.11` and warns that a stale reference set is not current authority.

If no promoted cue helps, omit the cue. Do not invent a core `UF.*` cue merely to make a CGUS use look governed. DPFs and project-local frameworks may carry their own local cue examples when useful, but the governing claim still comes from the local governing-pattern map and the relevant pattern bodies.

#### A.22.CGUS:4.6 - Replay and change localization

Replay one CGUS use from its exact four-part A.22 identity basis, filled position locators, relation declarations, current selected relation occurrences, constraints, invariants, guards, preserved structures, C.33 adequacy notes, admissible next-form kinds, and use boundaries. For each selected continuation, recover the occurrences and guards that admit it and the direct pattern governing every stronger claim. A demonstrative slice is replayable only as one claim-bearing presentation of that selected structure; it neither reidentifies the structure nor performs the continuation.

Localize a change before reopening wider work. A changed relation instance reopens that reference and its dependent guards or continuations. Changed omitted structure reopens the affected C.33 adequacy note and any slice relying on it. A changed presentation changes the demonstrative slice without changing the CGUS unless it reveals missing or false structure. A freshness, edition, telemetry, or decay change is handled by its exact `G.11` relation. A changed method, work, evidence, architecture, publication, or formal claim returns to the direct governing pattern for that claim. Rebuild the wider CGUS only when its structure identity, position set, relation structure, constraints, or declared use boundary has changed.

