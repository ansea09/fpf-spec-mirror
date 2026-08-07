---
chunk_kind: "child"
pattern_id: "E.18.3"
pattern_title: "Constraint-Governed Transformation-Flow Unfolding Structure"
section_id: "E.18.3:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.3/E.18.3__006_solution.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "E.18.3 — Constraint-Governed Transformation-Flow Unfolding Structure"
  - "E.18.3:4 — Solution"
line_start: 84769
line_end: 84945
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.PROD"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.22.CGUS"
  - "A.3.4"
  - "A.6.3.NAR"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.30.TFS-REL"
  - "C.32.CONWAY"
  - "C.32.P2S"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.18.3"
  - "E.18.NET"
  - "E.23"
  - "G.11"
  - "G.5"
  - "U.Transfer"
keywords:
---

### E.18.3:4 - Solution

E.18.3 is a membership-and-use profile for one exact selected A.22.CGUS `U.Structure`. The selected structure keeps the four A.22 identity discriminators. Its applicable E.18 substrate is independently identified as one TFS, one parent-relative internal `SubflowRef`, or one E.18.NET network. E.18.3 asks whether the selected CGUS uses exact positions, bindings, and already-obtaining occurrences from that substrate, together with its current constraints and use frame, to satisfy the transformation-flow unfolding conditions below.

| Coordinate | Required transformation-flow recovery | Honest lower result |
| --- | --- | --- |
| A.22 identity | One exact `selectedCGUSRef` resolves independently identified constituents, selected already-obtaining relation occurrences, applied constraints and one named selection-use frame. | Keep the current record, graph, table or explanation and return the missing A.22 discriminator. |
| Flow case | Classify the independently identified E.18 substrate used by the selected CGUS as one exact TFS with several valuations, one parent-relative internal `SubflowRef`, or one E.18.NET network over independently identified TFS or nested-network members and exact cross-boundary occurrences. The substrate ref never resolves to `selectedCGUSRef`. | Keep the flow cue; do not mint another TFS, network member, reciprocal CGUS, or giant flattened flow. |
| Transformation subjects | Name each subject used by this unfolding question with its exact kind. When replay of kind membership needs its basis, cite the exact definition or test supplying the criterion and the current facts or evidence showing that the subject meets it. The ordinary case may have one transformed entity; a multi-object flow may need several independently identified subjects. | Keep the subject wording as a cue and stop before structure qualification. |
| Position mappings | More than one admitted `CGUSPositionLocator` maps through an exact E.18 `FlowPositionRef` and current position binding to the same selected constituent already named by that locator. | Keep the candidate places in an ordinary provisional explanation. Constitute a C.2.1 provisional episteme only when a persistent or replayable claim is current. |
| Relation occurrences | Every selected internal `U.Transfer`, dependency relation, cross-member relation, or independently defined guard-relation occurrence cites its exact already-obtaining occurrence, predicate-definition source, participant meanings, and current basis. A relation-reference episteme may classify that occurrence but creates neither kind nor occurrence. E.18.3 defines no generic guard relation. | Keep a proposed edge or question and use the A.6.RCD blocker selection stated in `4.1`; otherwise name the missing predicate definition, facts, occurrence, or binding. |
| Applied constraint or condition claim | A continuation condition that is a claim stays in `appliedConstraintClaimRefs[]` with the applicable predicate or test and the current facts or evidence that satisfy it. Its label does not turn it into a relation occurrence or event. | Keep the condition provisional and name the missing test or facts. |
| E.18 guard event | A `GuardFail` emitted by `USM.CompareGuard` or `USM.LaunchGuard` stays an E.18 event; the guard's `GuardOwnerGateId` aggregation assignment and current gate-assignment facts remain under E.18/A.21. The event is not a GateCheck or `U.Relation` occurrence. | Recover the event and aggregation-assignment facts, or omit the event claim. |
| Constraint and topology | Applied conditions, E.18 guard events, independently defined guard relations, branches, joins, cycles, partial orders, or many-to-many dependencies change admissible continuations for the named use without collapsing into one object kind. | Keep the linear display provisional or narrow the use. |
| Preservation and reconsideration | Exact preserved structures, relevant C.33 epistemes, ordinary stop, reconsideration conditions and currentness-dependent reopen are visible. | Keep a one-use explanation and state the missing loss or reconsideration question. |

Use this compact display only as a recovery aid; it is neither another record kind nor structure identity:

```text
selectedCGUSRef
flowCase: oneTFS | internalSubflow | network        # Plain choice for this use
transformationSubjectRows[]:
  subjectRef
  subjectKindRef
transformationPositionMappingRows[]:
  admittedCGUSPositionLocator
  flowPositionRef
  exactPositionBindingRef
appliedConstraintClaimRefs[]?                 # each resolves to its predicate or test and current fact basis
e18GuardEventRefs[]?                         # GuardFail events emitted by E.18 guards, never relation occurrences
guardGateAssignmentFactRefs[]?               # required with cited E.18 guard events under E.18/A.21
relationReferenceEpistemeRefs[]              # EntityOfConcern is an exact already-obtaining relation occurrence only
neighboringValueUseRows[]
transformationFlowStructureRef?             # independently identified one-TFS substrate; never selectedCGUSRef
subflowRef?                                  # parent-relative internal substrate in one TFS; never selectedCGUSRef
transformationFlowStructureNetworkRef?      # independently identified E.18.NET substrate; never selectedCGUSRef
pathIds[]?
pathSliceIds[]?
flowValuationRef?
preservedTransformationStructureRefs[]
structureInformationAdequacyNoteRefs[]?
stopCondition
reconsiderationConditions[]:
  conditionClaimRef
  affectedStructureRef
  nextQuestion
  relevantPatternRef?: cite only when it locates a needed definition, constraint, predicate, test, evidence or assurance rule, or a Method's way of doing and applicability
```

The first four A.22 discriminators, not this display, identify the selected CGUS. The mutually exclusive substrate fields identify independently current E.18 objects used by that CGUS; none is another identity field and none resolves to `selectedCGUSRef`. `flowCase` and the remaining rows show why that one CGUS qualifies and let the current use replay its substrate, subject kinds, relation predicate definitions, position bindings, and reconsideration boundaries. No ambient context, transformed-subject label, path, valuation, tag, record edition, demonstration, or profile field becomes another identity discriminator.

The three continuation-condition branches remain different objects. `appliedConstraintClaimRefs[]` resolves claims with their predicate or test and current facts. `e18GuardEventRefs[]` resolves E.18 guard-failure events together with `guardGateAssignmentFactRefs[]`; neither field denotes a relation. `relationReferenceEpistemeRefs[]` resolves only epistemes whose EntityOfConcern is an exact already-obtaining relation occurrence. These optional fields are a recovery aid, not a new record or condition kind.

Paths and demonstrations remain different. `PathId`, `PathSliceId`, `FlowValuation` and the complete `FlowPositionRef` identity stay with one exact E.18 TFS. A post-admission A.22 demonstrative slice is a separate ordinary C.2.1 episteme whose EntityOfConcern is the admitted CGUS. Before admission, a flow card, worked example, or explanation may remain an ordinary explanation about the actual subject, question, or proposed continuation set. Constitute it as a C.2.1 provisional episteme only when the current use needs a persistent or replayable claim; a linear slice may teach one traversal while the selected structure branches, joins, cycles, or keeps alternatives live.

A pattern-selection flow, selected-pattern-application flow and downstream-subject-work flow keep different EntitiesOfConcern, changes, Work occurrences, results, applicable definitions and tests, constraints and reconsideration conditions. If all relevant positions and internal `U.Transfer` occurrences resolve to one TFS, use its exact positions and, when current, one complete top-level demonstration locator `<transformationFlowStructureRef, pathSliceId, DesignRunTag>`. A detailed internal portion remains one parent-relative `SubflowRef`. If independently identified TFS or nested-network members cross, use E.18.NET to recover the network membership and exact cross-member occurrence requirements, including the applicable predicates and current facts showing that the membership and occurrences obtain; the mutually exclusive A.22 network locator applies and the top-level one-TFS triple is absent.

A result, tool, context, constraint, shared label or displayed arrow neither merges network members nor supplies their relation. Every member keeps its boundary, Work, actual transformations, valuations and leaf-local position state. Nested pattern-selection content is present only while its exact source or selection-provenance relation is current for the declared demonstration use. When present, it contributes its own candidate, fit finding or recommendation rather than borrowing a later application result.

Preserved transformation structure is carried by exact `U.Structure` refs. Captured, expected-but-uncaptured, lost and hidden structure for the declared use remains in exact C.33 epistemes. A stop or reconsideration condition is an ordinary use boundary unless an exact relation occurrence is independently defined and shown to obtain by its applicability conditions and current facts. G.11 supplies the source-currentness and decay tests; E.18 supplies one-TFS slice-local refresh.

There is no generic method-to-work linkage here. When one named use relies on a Method-to-Work claim, cite the exact already-obtaining relation or result and the concrete definition, test or rule that supports it; keep Method, qualifying MethodDescription, WorkPlan, readiness and dated Work separate. A pattern ref, intended realization, selected continuation, imperative sentence or displayed sequence does not admit any episteme as `U.MethodDescription`. A.3.2 supplies the membership test: one already identified C.2.1 episteme whose exact EntityOfConcern is one admitted `U.Method` and whose ClaimContent makes at least one substantive way-of-doing claim. Each exact Method, qualifying MethodDescription, WorkPlan, work-entry result, dated Work, actual Transformation, production/inception/completion, evidence, evaluation, or source-use object must first be independently identified; any membership, occurrence, evidence, evaluation, or source-use claim obtains only when current facts or evidence satisfy the applicable definition, test, predicate, or rule. Only current objects and already-obtaining relations may enter the structure.

#### E.18.3:4.0 - Ordinary start and conditional formal recovery

Begin with the ordinary branch: name the concrete thing being transformed, mark two recognizable places or states, state the proposed connection or guard in domain language, and ask which continuation depends on it. Return a provisional explanation that either answers the question or names the missing relation, fact, or constraint. If that is sufficient, stop; neither the explanation nor the flow card must first be constituted as an episteme, position mapping, or selected structure.

Use the numbered recovery branch below only when the current use must assert E.18.3 qualification, compare or publish the structure, or support a stronger downstream claim. The branch preserves the exact admission criteria; it is not a prerequisite for understanding or correcting an ordinary route-like card.

1. Recover one selected A.22.CGUS and its four exact identity discriminators; do not create a reciprocal E.18.3 structure.
2. Name the current transformation subject or subjects, their kinds and the exact E.18 positions and bindings used by the question.
3. Classify the independently identified E.18 substrate used by `selectedCGUSRef` as one TFS with its valuations, one parent-relative internal `SubflowRef`, or one E.18.NET network of independent members and exact crossings; do not resolve the substrate ref to the selected CGUS.
4. Discriminate every continuation basis before citing it. Keep an applied constraint or condition claim in `appliedConstraintClaimRefs[]` with its predicate or test and current facts; keep a `GuardFail` emitted by `USM.CompareGuard` or `USM.LaunchGuard` as an E.18 event with its E.18/A.21 gate-assignment facts; and use a relation-reference episteme only for an independently defined exact relation occurrence. Cite every selected internal `U.Transfer`, dependency relation, or cross-member relation occurrence and its predicate-definition source; a condition informally called a guard enters this relation branch only when its relation kind and obtaining occurrence independently exist. Carry a relation signature only when replay needs the exact declaration.
5. For each `neighboringValueUseRows[]` entry, recover the independently identified neighboring value through its exact kind and ref and one already-obtaining supporting relation. If the row makes a stronger claim, state in ordinary content-bearing language what the neighboring content contributes; a bare label such as `test` or `method` is not enough. A definition, constraint, predicate, test, evidence rule, or assurance rule may supply the applicable criterion, with current facts or evidence showing that the claim obtains. A Method contributes a reusable way of doing and its applicability or bounds, and a MethodDescription may state that content; any claim that its use produces, supports, evaluates, evidences, or assures a result still needs a separate applicable rule and current basis. Require an exact claim-bearing episteme, ClaimGraph, edition, or other content identity only when that identity changes the selected stronger use, and reuse an existing exact ref when available. Cite a relevant pattern only when it locates that content. A result label, return arrow, or comparison layout is not the relation.
6. Name preserved structures, relevant C.33 adequacy notes, an ordinary stop and the exact reconsideration conditions. For a post-admission demonstration, choose exactly one complete A.22 locator family: top-level one-TFS, network, or neither for a generic slice.
7. If any A.22 discriminator, position binding, direct relation, network row, or required loss or reconsideration value is missing, keep the artifact as an ordinary provisional explanation and state the exact blocker. Constitute a C.2.1 provisional episteme only when persistence or replay of that narrower claim is current.

The ordinary branch and conditional recovery sequence guide use of the pattern. They are not a local mantra, `U.Method`, `U.MethodDescription`, WorkPlan, or performed Work; completing the rows admits nothing by itself.

#### E.18.3:4.0a - Exact relation references

When another person or later use must replay how one selected relation occurrence participates in the selected transformation-flow structure or supports a separately current subject use, materialize one ordinary C.2.1 episteme. Its exact EntityOfConcern is the already-obtaining relation occurrence, its ClaimContent contains only the current reference use below, and its effective ReferenceScheme governs every designation. *Transformation-flow relation reference* is Plain wording for this use, not a local U-kind. Its edition and currentness remain ordinary C.2.1 and G.11 concerns; they do not add an identity field or ambient context.

```text
transformationFlowRelationReferenceClaimContent:
  selectedCGUSRef
  exactRelationOccurrenceRef
  exactRelationKindRef
  predicateDefinitionRef: exact source that defines the obtaining predicate and participant meanings
  exactParticipantRefsInPredicateOrder[]
  currentFactOrEvidenceRefs[]
  relationSignatureRef?: exact declaration ref only when the replay needs it
  subjectUse?: evidence | assurance | architecture | narrative | publication
  exactSubjectUseClaimOrRelationRef?: required when subjectUse is present
  networkEndpointBindingSets[]?:
    networkCrossFlowRelationRowRef: exact E.18.NET NetworkCrossFlowRelationRowRef
    endpointRows[]:
      relationParticipantPositionRef
      endpointMemberRef
      endpointFlowPositionRef: FlowPositionRef | ExposedFlowPositionRef
      endpointPositionBindingRef
```

The exact relation kind, predicate definition, ordered participants, current basis, and any network endpoint bindings carry the transformation-flow role; E.18.3 adds no separate structural-function classifier. An internal transfer is cited only as an exact `U.Transfer` occurrence whose positions resolve inside one TFS. A dependency is recoverable only when the exact predicate truth conditions make one admitted continuation, state, or value depend on another and the participant order preserves that direction. A cross-member connection is recoverable only from an exact obtaining relation whose ordered endpoints bind admitted positions in different selected E.18.NET members. These conditions are distinguishable by value and none relabels or substitutes for the exact relation kind or predicate. An E.18 `GateCrossing` is a structure-local transition, not a `U.Relation` occurrence, and never enters this relation-reference field. A domain condition informally called a guard enters a relation reference only when an independently defined relation kind and exact obtaining occurrence exist.
An applied constraint or condition claim is not the EntityOfConcern of this relation-reference episteme; keep it in `appliedConstraintClaimRefs[]` with its test and current facts. A `GuardFail` emitted by `USM.CompareGuard` or `USM.LaunchGuard` is an E.18 event, not a relation occurrence; recover the event and `GuardOwnerGateId` aggregation-assignment facts under E.18/A.21 instead. The word guard alone admits neither branch.

`subjectUse` records a separately current use only when the cited exact evidence, assurance, architecture, narrative, or publication claim or relation is already shown to obtain: the cited rule supplies the applicable criterion and current facts or evidence satisfy it. The classifier alone makes none of those uses obtain. One selected relation occurrence may also support a separate use without becoming two occurrences. For example, one exact cross-member relation may support an evidence use only when the cited evidence rule and current facts support the exact use claim; its transformation-flow participation and `subjectUse=evidence` neither duplicate the occurrence nor make the evidence claim obtain.

For a selected network mapping, resolve `NetworkCrossFlowRelationRowRef` to exactly one row in its named current record edition. Then require that row, the relation-reference episteme and the direct occurrence to agree on exact occurrence, kind, predicate-definition source, optional signature, participant order, endpoint members, positions and bindings. The endpoint set adds no relation and makes none obtain; it preserves how the already-obtaining occurrence reaches admitted transformation positions.

A pattern identifier or reference is not a `U.MethodDescription`. A relation signature is carried only when the exact declaration exists and the replay needs it; citation does not make every use signature-dependent.

#### E.18.3:4.1 - Connections to independently identified neighboring values

E.18.3 mints no universal neighboring-value relation. A neighboring Method, plan, Work, evidence, assurance, gate, decision, architecture, narrative, publication, evaluation, or currentness value must be independently identified. A claim about its kind, current status, or use obtains only when current facts or evidence satisfy the criterion supplied by the applicable definition, constraint, predicate, test, evidence rule, or assurance rule. A Method contributes its reusable way of doing and applicability or bounds; a MethodDescription may state that content, but any truth, result, evidence, assurance, or Work claim about using it still needs its separate applicable rule and current basis. A positive connection exists only through an exact already-obtaining relation. A stronger neighboring claim states its concrete contribution in ordinary content-bearing language; an exact content identity is added only when that identity changes the selected use.

Use this display row when a reader must recover the connection:

```text
neighboringValueUseRow:
  admittedTransformationPositionLocator: exact CGUSPositionLocator already used by this E.18.3-qualified structure
  neighboringValueKindRef
  neighboringValueRef
  connectionQuestion: exact stated question
  exactSupportingRelationOccurrenceRef
  supportingRelationReferenceEpistemeRef?: ordinary C.2.1 episteme from 4.0a
  connectionRationaleClaimRef
  concreteContribution?: ordinary content-bearing statement of what the neighboring content contributes; never a bare category label
  relevantPatternRef?: only when it locates that content
```

`connectionQuestion` is one exact free-text question, not a code, kind, relation, or closed question-type set. Non-exhaustive examples include questions about basis dependency, a result, a governing constraint, or a comparison. A basis-dependency question creates no obligation. A result question is positive only after the exact result entity or relation and what it is a result of or for are recovered. A governing-constraint question needs the exact current constraint claim or occurrence. A comparison question needs its comparator, participants, scope and exact comparison definition or test; juxtaposition supplies none. Every stated question still requires an exact supporting relation. Direction, participant order, applicability, occurrence identity, dependence and currentness come from its predicate definition, exact declaration when replay needs it, and current facts, not from the question wording. When a stronger neighboring claim is made, `concreteContribution` states what the content actually does—for example, defines a term, constrains a claim, supplies a predicate or test, describes a Method's way of doing, or supplies an evidence or assurance rule. Those forms are non-exhaustive verbs, not field values; `definition`, `test`, or `method` alone cannot fill the field. `relevantPatternRef` is only a locator. An exact claim-bearing episteme, ClaimGraph, edition, or other content ref is required only when that identity changes the selected stronger use. Neither field creates a relation.

An ordinary stop uses `stopCondition`; reconsideration uses `reconsiderationConditions[]` to name the condition claim, affected structure and next question, with `relevantPatternRef` only when cited content supplies a needed contribution. Neither creates a receiver or connection relation. If the supporting relation is missing, keep the neighboring values separate and record the attempted question. Use the A.6.RCD `missing-governor` result only when no applicable relation kind or predicate is available for the exact participants and question; otherwise return unresolved-facts, false-predicate or missing-binding. Recommendation, intended realization, rationale text, common EntityOfConcern and graph adjacency are not substitutes.

#### E.18.3:4.2 - Ordinary provisional explanation and admitted slice

Before the selected A.22 structure passes admission and the E.18.3 membership condition, a path fragment, flow card, worked example, or first-use account may remain an ordinary provisional explanation. It can name the concrete subject, recognizable places or states, proposed relations, possible continuations, and the missing fact or constraint without asserting a structure, position, or relation occurrence.

When replay, comparison, publication, or another current use needs that narrower account to persist as a claim, constitute one ordinary C.2.1 provisional episteme. Its exact EntityOfConcern is the actual transformation subject, current question, or proposed continuation set, never a not-yet-admitted structure. Its ClaimContent may name the visible candidate places, proposed relations, presentation form, unresolved coordinates, and the exact condition that would resolve each one. The explanation or episteme guides discovery but creates no constituent, structure identity, position, relation occurrence, Method, MethodDescription, plan, Work, or Transformation.

After admission, a separate ordinary C.2.1 demonstrative-slice episteme may teach one admissible traversal. Its exact EntityOfConcern is the same selected CGUS recognized by E.18.3. Its ClaimContent cites exact admitted `CGUSPositionLocator` values, already-admitted relation-reference epistemes or obtaining occurrence refs, relevant C.33 omissions, alternatives, loop-compression and presentation-ordering claims, admissible and forbidden uses, and the slice return condition. A source provisional episteme is cited only through an exact source, derivation, or viewing-construction relation whose predicate definition supplies the applicable criterion and whose current facts satisfy it, so that the exact use obtains; file history is not such a relation.

Do not infer that demonstrated order is project-work order. If ordered Work is current, use A.15.2 for the plan test and A.3.1/A.3.2 for independently identified Method and MethodDescription claims; the demonstration’s imperative or repeated wording admits none. Do not infer that a demonstrated path is the whole topology. When the selected structure branches, joins, cycles, keeps alternatives live or is partially ordered, record what the slice omits or compresses before relying on it for comparison, architecture, evidence or planning.

A pre-admission card can still help slot discovery. Each candidate position names the subject-domain object or question it concerns, the proposed E.18 position and binding, and the exact admission coordinate still unresolved. Once the A.22 identity, flow case, admitted position mappings, exact relations, constraints, preserved/lost structure and use boundaries are recoverable, admit the structure first and constitute a separate slice second. If later inspection invalidates admission, withdraw the slice claim while retaining any still-truthful provisional claim under its narrower use.

#### E.18.3:4.2a - Admit network-aware demonstration mappings

A network-aware demonstrative slice is post-admission only. First select and verify one E.18.NET-conforming network. Then recover the one selected A.22.CGUS, its E.18.3 transformation-position mapping rows, and every required relation-reference episteme. Only then may the slice use A.22.CGUS `networkDemonstrationLocator`; the locator supplies no missing member, position, relation, constraint or admission.

For each `selectedNetworkPositionMappingRows[]` entry, resolve the finite member path hop by hop through exact direct members to its leaf TFS. A `FlowPositionRef` must name that final TFS. An `ExposedFlowPositionRef` must name this slice’s selected network and repeat the same complete member path and leaf position; a different network, path or leaf leaves the mapping out. `admittedIncludedPositionLocator` must be the same exact `CGUSPositionLocator` already present in the E.18.3 position mapping and the slice’s `includedPositionLocators[]`. The network ref locates that admitted position; it does not create a copied raw-position list.

For each `selectedCrossFlowRelationReferenceRows[]` entry, require its `NetworkCrossFlowRelationRowRef` to name a current record edition whose EntityOfConcern is this slice’s selected network, then resolve exactly one row by occurrence and complete ordered endpoint-binding identity. Pair that row with one relation-reference episteme already cited by this E.18.3-qualified structure and with its matching `networkEndpointBindingSets[]` entry. Verify occurrence, kind, predicate-definition source, optional signature, participant order, endpoint members, flow positions and bindings by value. If the record describes another network, zero or several rows resolve, any field differs, or the relation reference is not already current, omit the mapping and name the exact missing or ambiguous network, row, position, occurrence, predicate definition or binding.

The complete top-level one-TFS locator is absent from a network slice. `FlowValuation`, `PathSliceId` and `DesignRunTag` remain member- or leaf-local; Work, actual transformations, boundaries and currentness also remain with their exact member and applicable definitions or tests. Member paths are finite and membership is acyclic, while exact cross-flow feedback occurrences may cycle when their predicates and constraints admit them.

Every selected cross-flow relation remains the exact occurrence whose predicate-definition source fixes its kind and participant meanings and whose applicability conditions and current facts show that it obtains. Do not substitute universal `creates`, `produces`, `uses`, `input`, `output`, `result`, `handoff` or `transfer` edges. One C.32.CONWAY result may contribute one exact transformer-role-system and transformed-holon architecture-correspondence occurrence as one qualified network row after its occurrence and endpoint bindings are recovered; it never constitutes the network.

A source phrase or graph enters only through an exact source-to-use claim or relation. A separately identified `BoundedModelUseStructure` participates only when the current assertion or use selects it and its organization changes interpretation of that claim; shared wording, adjacency, or a crossing display is evidence of neither model-use qualification nor crossing.

**Positive case.** A four-level build-the-builder demonstration follows one finite member path to an already admitted leaf position, maps it to the same included CGUS/E.18.3 locator, cites one exact admitted cross-flow relation-reference episteme, and keeps path slice and tag in one leaf-local row. **Near miss.** A graph supplies raw positions or an edge label, mixes locator families, duplicates positions, assigns one tag to the network or cites a row without exact bindings; keep it provisional or return the exact missing member, relation, position or binding.

#### E.18.3:4.3 - Boundary

E.18.3 recognizes one selected A.22.CGUS `U.Structure`; it is not a second transformation ontology or reciprocal narrower structure. That selected CGUS uses one independently identified E.18 substrate branch and its exact positions, bindings, and already-obtaining occurrences; the substrate is not the selected CGUS. The selected structure is not a workflow, Method, MethodDescription, WorkPlan, performed Work, actual Transformation, mathematical graph, publication, evidence relation, gate decision, architecture decision, or architecture description. It organizes independently identified constituents, already-obtaining relations, and constraints for one transformation-flow unfolding use.

A graph, record, filled table, demonstration, imperative, selected continuation, recommendation, or intended realization is evidence of neither the A.22 identity nor the E.18.3 condition. It admits no MethodDescription or Work. A.3.2, A.15.1, A.3.4 and A.15.PROD supply the applicable membership or occurrence tests; every relation claim still needs its exact predicate definition, applicability conditions and current facts.

#### E.18.3:4.4 - Replay and change localization

Replay one use from the selected CGUS's exact four A.22 identity discriminators, the independently identified E.18 substrate branch and ref, transformation subjects, admitted position mappings, exact selected relation occurrences and relation-reference epistemes, applied constraint claims with their tests and current facts, any E.18 guard events with their gate-assignment facts, exact supporting relations to neighboring values, one-TFS path or valuation refs when current, any post-admission network mappings, preserved structures, C.33 adequacy notes, and ordinary stop and reconsideration conditions. For each continuation, recover the actual condition branch rather than inferring its type from a guard label. For every stronger neighboring claim, state in ordinary language what the neighboring content actually contributes: a definition, constraint, predicate, test, evidence rule, or assurance rule may supply its criterion, while a Method contributes a reusable way of doing and applicability or bounds and leaves every stronger result or support claim to a separate rule and current basis. Record exact content identity only when that identity changes the selected use.

Localize changes by the object they affect. A changed relation occurrence, predicate definition, participant, or current fact reopens its relation-reference episteme and dependent continuations. A changed applied-condition test or fact reopens that claim and its dependent continuations. A changed E.18 guard event or aggregation-assignment fact reopens that event branch and its E.18/A.21 gate account. A changed neighboring value, concrete contribution, or supporting relation reopens only that use row. A changed path or valuation reopens only dependent one-TFS slices and demonstrations. A changed network member, path, exposure, row, or endpoint binding returns first to the E.18.NET membership and mapping tests and then to dependent mappings. Changed omitted structure reopens its C.33 episteme. Source edition, source-use, freshness, telemetry, and decay use the G.11 currentness tests; E.18 supplies only one-TFS slice-local refresh.

Re-evaluate E.18.3 qualification when its flow case, position mapping or use claim changes. Reidentify the selected `U.Structure` only when one of the four A.22 discriminators changes; a changed description, demonstration, valuation, path slice, local tag or E.18.3 qualification result does not by itself create another structure.

