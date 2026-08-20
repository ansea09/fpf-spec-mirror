---
chunk_kind: "child"
pattern_id: "C.32.CONWAY"
pattern_title: "Architecture-Influence and Transformed-Architecture Correspondence"
section_id: "C.32.CONWAY:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.CONWAY/C.32.CONWAY__005_solution.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "C.32.CONWAY — Architecture-Influence and Transformed-Architecture Correspondence"
  - "C.32.CONWAY:4 — Solution"
line_start: 65616
line_end: 65700
dependencies:
  - "A.10"
  - "A.12"
  - "A.15.1"
  - "A.19.CPM"
  - "A.2.1"
  - "A.22"
  - "A.3.4"
  - "A.3.4.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.6.REL"
  - "B.3"
  - "C.11"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.TFS-REL"
  - "C.32"
  - "C.32.ACS"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "C.32.PAD"
  - "E.18"
  - "E.18.NET"
  - "F.6"
  - "G.5"
  - "U.Structure"
keywords:
---

### C.32.CONWAY:4 - Solution

Build the local synthesis frame first. Admit a relation kind only through the applicable E.24-family admission pattern and direct settlement. Use that pattern's predicate and applicability to test the current pair. If current facts or constituting history satisfy the predicate affirmatively, one world-side occurrence obtains and the row may cite its exact identity. If the predicate is false, no exact pair row is asserted. If the current facts do not decide it, keep the correspondence synthesis-local and name the missing grounding or information-sufficiency boundary. Use `missing-governor` only when no direct relation kind and predicate govern the intended pair and use.

#### C.32.CONWAY:4.1 - Keep acting, influence, and correspondence facts separate

1. **Name the domain action and changed referent.** Identify `changedReferentRef` independently. Add `actualTransformationRef` only when A.3.4 independently admits one bounded change of that same continuing referent; keep actor-side and Work-to-change relations under their subject patterns. Architecture influence identifies none of those facts.
2. **Add acting and performance facts only when claimed.** Every actor or performer is one exact `U.System`. A claimed work-facing assignment requires one obtaining occurrence of a directly admitted `U.SystemRoleAssignment` species under A.2.1. Claimed performance requires one exact dated `U.Work`, the exact F.6 occurrence `performedUnderAssignment(W, RA)`, and `S = RA.HolderSystemSlot`, plus the exact actor-side or Work-to-change relation needed by the claim. Use A.15.1 `CC-A15.1-17` when several systems jointly perform the top-level Work or when the use instead needs a parent Work with separately performed child occurrences.
3. **Name every influence source by kind.** Architecture, selected structure, Work, communication, constraint, and candidate-synthesis results retain their kinds and direct influence relations. Influence alone supplies no system identity, system-role kind or assignment, Work, performer status, changed-referent identity, or transformation participation.
4. **Select one architecture pair.** For an exact row, name one obtaining influence-source C.30 `ArchitectureRelation` and one obtaining transformed-side C.30 `ArchitectureRelation`, with each exact holon and selected-`U.Structure` participant. Their architecture-bearing holons may differ from every acting system. Record equality only when independent actor and architecture-bearer facts establish it. If either side is only candidate, required, desired, or expected, keep its exact `ArchitectureClaim` and the pair in the synthesis frame; do not assert an exact pair row.
5. **Map only structures and characteristics that change the candidate.** Name the source-side selected structure, transformed-side selected structure, expected gain, known loss, evolution window, pattern for the next question, and source-return condition. For each affected characteristic, reference only the few current `C.32.ACS` criteria rows and any declared `C.25` Q-Bundle slots that make this trade-off real.
6. **Prepare four candidate forms.** Change the influence-source side, change the transformed architecture, change both, or keep a bounded mismatch with an explicit cost and reopen trigger.
7. **Use C.29 only for structural-similarity claims.** A correspondence row does not establish homomorphism, equivalence, or architecture adequacy.
8. **Stop at the next governed claim.** Send comparison, selection, publication, choice, decision, evidence, assurance, gate, Work, or organization-governance claims to their direct patterns.

#### C.32.CONWAY:4.2 - Exact reusable architecture-pair row

```text
ArchitectureInfluenceTransformedArchitectureCorrespondenceRow@Context <: U.Episteme:
  entityOfConcernRef: exactArchitectureInfluenceOrCorrespondenceRelationOccurrenceRef
  entityOfConcernKindRef: exactArchitectureInfluenceOrCorrespondenceRelationKindRef
  relationFunctionClaimRef: subject pattern of that exact relation kind and occurrence
  influenceSourceArchitectureRelationRef: one exact obtaining C.30 ArchitectureRelation
  influenceSourceHolonRef: the exact architectureBearingHolonRef participant of influenceSourceArchitectureRelationRef
  influenceSourceSelectedStructureRef: the exact selectedArchitectureStructureRef participant of influenceSourceArchitectureRelationRef
  influenceSourceArchitectureClaimRef?: exact C.30 ArchitectureClaimRef when the current use also needs claim content about that same holon, relation, or structure
  transformedArchitectureRelationRef: one exact obtaining C.30 ArchitectureRelation
  transformedHolonRef: the exact architectureBearingHolonRef participant of transformedArchitectureRelationRef
  transformedSelectedStructureRef: the exact selectedArchitectureStructureRef participant of transformedArchitectureRelationRef
  transformedArchitectureClaimRef?: exact C.30 ArchitectureClaimRef when the current use also needs claim content about that same holon, relation, or structure
  changedReferentRef: exact independently identified referent of the current change
  actualTransformationRef?: U.EntityRef constrained to U.Transformation, only when A.3.4 independently admits the bounded change of changedReferentRef
  performerRows[]?:
    actingSystemRef: U.EntityRef constrained to U.System; for performance, this must equal actingSystemRoleAssignmentRef.HolderSystemSlot
    actingSystemRoleAssignmentRef?: U.RelationRef constrained to U.SystemRoleAssignment, required when an obtaining assignment is claimed and whenever performance is attributed under assignment
    workOccurrenceRef?: U.EntityRef constrained to U.Work, required when performance is claimed
    performedUnderAssignmentRelationRef?: U.RelationRef governed by F.6, required with workOccurrenceRef
    actorSideOrWorkToChangeRelationRefs[]: U.RelationRef
  additionalInfluenceSourceRows[]?:
    influenceSourceRef:
    influenceSourceKindRef:
    exactInfluenceRelationRef: U.RelationRef
    influencePatternLocator:
  affectedArchitectureCharacteristicRefs[]: current C.32.ACS criteria-row refs; exact C.25 Q-Bundle slot refs when composite
  evolutionWindowRef:
  correspondenceUse:
  expectedArchitectureGain:
  knownArchitectureLoss:
  receivingUsePatternLocator:
  sourceReturnCondition:
  networkCrossFlowRelationRowRef?: E.18.NET NetworkCrossFlowRelationRowRef
```

The row is a `U.Episteme` about one already obtaining direct influence or correspondence relation whose exact participants include the two obtaining C.30 architecture-relation occurrences required by this use. Because those occurrences fill participant positions of another relation, each is explicitly individuated under A.6.REL for this receiving use. The row neither creates the influence occurrence nor mints a universal Conway relation. Each C.30 occurrence keeps its exact holon and selected-`U.Structure` participants; the influence occurrence keeps its identity under its direct relation pattern and A.6.REL. This row only describes them for the current correspondence use. `entityOfConcernRef`, its kind, its governor, both C.30 occurrences and their participant pairs, and the changed referent are required. If the practitioner has only a useful local compound correspondence claim, or either architecture side is modal rather than obtaining, keep it in the frame for candidate synthesis. Assert the row only after the admitted influence relation kind's direct predicate is applicable and current facts satisfy it affirmatively. If the predicate is false, assert no row; if facts are unresolved, keep the frame and name that boundary; if the kind or predicate is absent, return `missing-governor`. None of these branches permits inferring a relation from two architecture claims, structures, diagrams, or names.

#### C.32.CONWAY:4.3 - Qualified network reading

The same exact pair row may appear in `architectureCorrespondenceRowRefs[]` of several `TransformationFlowStructureNetworkRecord@Context` values while its pair, relation occurrence, evolution window, correspondence use, and claim scope remain current. Each citation contributes only one qualified architecture reading. The row's optional singular `networkCrossFlowRelationRowRef`, when present, qualifies only the exact current record edition named by that locator; it does not qualify the row's citations from other records. No citation makes the pair row the network, adds a member, or satisfies the network's exact cross-flow-relation discriminator.

Set `networkCrossFlowRelationRowRef` only when the pair row's exact influence occurrence and architecture-relation participants are independently grounded in member-flow positions and the locator's `transformationFlowStructureNetworkRecordRef` names the same exact current record whose `architectureCorrespondenceRowRefs[]` citation this mapping is intended to qualify. Resolve that record first, then require exactly one `crossFlowRelationRow` to match the occurrence and complete ordered endpoint-binding identity. That row must preserve the same kind, governor, participant order, endpoints, and bindings as this correspondence row. Zero or several matches, a different record, or a stale record edition leaves the locator unresolved. Do not reuse one locator to qualify another record's citation. A record citation alone infers none of those facts.

Acting-system identity, system-role assignment, F.6 attribution, Work, actual transformation, actor-side or Work-to-change relation, influence relation, and network cross-flow relation remain separately governed even when one case cites all of them.


#### C.32.CONWAY:4.4 - Candidate moves and repair rows

Plain text begins with the domain action—builds, assembles, repairs, configures, treats, teaches, compiles, or evaluates. It then names the acting system and Work only when those facts are current. In a separate sentence it says which architecture or other source influences which candidate through which exact relation. `Creator`, `creation`, `producer`, `transformer architecture`, and `uses` remain ordinary cues, not universal technical labels.

Choose only pressures that change the candidate or protect against a concrete loss. Every `affectedArchitectureCharacteristicRefs[]` value in an exact pair row or comparison-ready candidate must resolve to a current `C.32.ACS` criteria row; when the pressure is one slot of a composite quality family, also resolve the declared `C.25` Q-Bundle and that exact slot. If those governed objects do not yet exist, put plain heads such as independent change, substitutability, evidence reuse, latency, coupling or cohesion, coordination load, and source-return cost only in the local frame's `provisionalArchitectureCharacteristicHeads[]`; never place them in `affectedArchitectureCharacteristicRefs[]`. These heads are discovery cues, not a universal catalogue and not criteria refs. Use `C.32.ACS` or `C.25` before making a stronger comparison, selection, or decision claim.

| Correspondence repair row | Use | Minimum repair against overread |
|---|---|---|
| `changedReferentRecovery` | The story names a team, line, tool, method, or organization but not what changes. | Identify the exact continuing changed referent; when actual change is asserted, identify its A.3.4 `U.Transformation`; keep actor-side and Work-to-change relations separately governed. |
| `performerRecovery` | A source is said to build, design, repair, or operate. | Name the exact `U.System`, exact A.2.1 assignment, dated `U.Work`, F.6 `performedUnderAssignment` occurrence and holder equality, and direct actor-side or Work-to-change relations; use A.15.1 `CC-A15.1-17` when several systems perform. |
| `influenceSourceRecovery` | An architecture or structure is said to shape a candidate. | Name its exact kind and direct influence relation; otherwise keep it as a candidate cue. |
| `architecturePairRecovery` | Two architectures are compared or linked. | Apply the direct relation pattern. With no kind/predicate, return `missing-governor`; with unresolved facts, keep the pair synthesis-local and name the missing grounding; with a false predicate, assert no occurrence; with a satisfied predicate, name the exact obtaining occurrence and pair. |
| `inverseConwayRetargeting` | The desired transformed architecture is sound, but the current source-side arrangement cannot sustain it. | Change selected influence-source structures and record migration cost, new burden, and stop condition. |
| `transformedArchitectureRetargeting` | The source-side arrangement is fixed or too expensive to change in the current window. | Change the transformed architecture candidate and record the lost desired property or exception. |
| `jointCorrespondenceSynthesis` | Neither side alone can carry the architecture characteristic. | Change both sides and record preserved structure, lost structure, and coordination burden. |
| `boundedCorrespondenceMismatch` | A mismatch is tolerable for now. | State exception cost, bounded-use limit, source-return condition, and reopen trigger. |

**Stop condition.** A first-pass frame may stop when it names the changed referent, separately typed source and transformed architectures, one selected structure on each side, either governed affected-characteristic refs or visibly provisional heads with their exact return, the applicable candidate-form heads, and the next subject pattern. Every acting, performance, or influence fact that is asserted must already have its direct basis. Before a candidate enters comparison or reliance, complete its source-side change, transformed-side change, expected gain, known loss, evolution window, pattern for the next question, source-return condition, and stop. An exact pair row additionally requires its direct relation predicate to be satisfied and its obtaining occurrence to be identified. A provisional pressure stays in `correspondenceClaims[]` with the exact reason visible: missing governor, unresolved grounding or information sufficiency, or a false predicate.

**Lowering condition.** Lower an exact row to synthesis-local correspondence material when its influence occurrence, either C.30 architecture-relation occurrence or participant pair, changed referent, evolution window, or receiving use is missing or stale. Retire a candidate when its source-side change, transformed-side change, bounded mismatch, or known loss no longer belongs to the declared evolution window. Use A.3.4 or E.18 when the actual transformation, changed referent, or flow relation is not recovered; to A.12, A.2.1, A.15.1, and F.6 when the issue is acting side, assignment, Work, or attribution; and to C.29 when the current claim is structural similarity or preservation.

