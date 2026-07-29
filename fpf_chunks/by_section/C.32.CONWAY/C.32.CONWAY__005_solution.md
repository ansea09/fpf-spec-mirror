---
chunk_kind: "child"
pattern_id: "C.32.CONWAY"
pattern_title: "Architecture-Influence and Transformed-Architecture Correspondence"
section_id: "C.32.CONWAY:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.CONWAY/C.32.CONWAY__005_solution.md"
commit_sha: "2ada413629b846ef308222d16489a82cb5b40a71"
heading_path:
  - "C.32.CONWAY — Architecture-Influence and Transformed-Architecture Correspondence"
  - "C.32.CONWAY:4 — Solution"
line_start: 65190
line_end: 65269
dependencies:
  - "A.10"
  - "A.12"
  - "A.15.1"
  - "A.19.CPM"
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
  - "G.5"
keywords:
---

### C.32.CONWAY:4 - Solution

Build the local synthesis frame first. Admit a relation kind only through its relation-kind admission owner and direct settlement. Use that owner's predicate and applicability to test the current pair. If current facts or constituting history satisfy the predicate affirmatively, one world-side occurrence obtains and the row may cite its exact identity. If the predicate is false, no exact pair row is asserted. If the current facts do not decide it, keep the correspondence synthesis-local and name the missing grounding or information-sufficiency boundary. Use `missing-governor` only when no direct relation kind and predicate govern the intended pair and use.

#### C.32.CONWAY:4.1 - Keep acting, influence, and correspondence facts separate

1. **Name the domain action and changed referent.** Identify `changedReferentRef` independently. Add `exactChangingRelationRef` only under its direct governor; architecture influence does not identify the change.
2. **Add acting and performance facts only when claimed.** Every actor or performer is one exact `U.System`. A claimed role requires an obtaining `U.RoleAssignment`. Claimed performance requires one exact dated `U.Work`, `performedUnderAssignment(W, RA)`, and `S = RA.HolderSystemSlot`, plus the exact actor-side or work-to-change relation needed by the claim. Use A.15.1 multiple-performer forms when several systems perform.
3. **Name every influence source by kind.** Architecture, selected structure, Work, communication, constraint, and candidate-synthesis results retain their kinds and direct influence relations. Influence alone supplies no system identity, role, Work, performer status, changed-referent identity, or transformation participation.
4. **Select one architecture pair.** Name one exact influence-source `ArchitectureOf@Context` and one exact transformed-holon `ArchitectureOf@Context`. Their described holons may differ from every acting system. Record equality only when independent actor and architecture-bearer facts establish it.
5. **Map only structures and characteristics that change the candidate.** Name the source-side selected structure, transformed-side selected structure, expected gain, known loss, evolution window, receiving pattern, and source-return condition. For each affected characteristic, reference only the few current `C.32.ACS` criteria rows and any declared `C.25` Q-Bundle slots that make this trade-off real.
6. **Prepare four candidate forms.** Change the influence-source side, change the transformed architecture, change both, or keep a bounded mismatch with an explicit cost and reopen trigger.
7. **Use C.29 only for structural-similarity claims.** A correspondence row does not establish homomorphism, equivalence, or architecture adequacy.
8. **Stop at the next governed claim.** Send comparison, selection, publication, choice, decision, evidence, assurance, gate, Work, or organization-governance claims to their direct patterns.

#### C.32.CONWAY:4.2 - Exact reusable architecture-pair row

```text
ArchitectureInfluenceTransformedArchitectureCorrespondenceRow@Context <: U.Episteme:
  entityOfConcernRef: exactArchitectureInfluenceOrCorrespondenceRelationOccurrenceRef
  entityOfConcernKindRef: exactArchitectureInfluenceOrCorrespondenceRelationKindRef
  governingPatternRef: direct owner of that exact relation kind and occurrence
  influenceSourceArchitectureRef: one exact ArchitectureOf@Context
  influenceSourceHolonRef: describedHolonRef of influenceSourceArchitectureRef
  transformedArchitectureRef: one exact ArchitectureOf@Context
  transformedHolonRef: describedHolonRef of transformedArchitectureRef
  influenceSourceSelectedStructureRef: U.StructureRef
  transformedSelectedStructureRef: U.StructureRef
  changedReferentRef: exact independently identified referent of the current change
  exactChangingRelationRef?: U.RelationRef, separately governed
  performerRows[]?:
    actingSystemRef: U.SystemRef
    roleAssignmentRef?: U.RoleAssignmentRef, required when a role is claimed
    workOccurrenceRef?: U.WorkRef, required when performance is claimed
    performedUnderAssignmentRelationRef?: U.RelationRef, required with workOccurrenceRef
    actorSideOrWorkToChangeRelationRefs[]: U.RelationRef
  additionalInfluenceSourceRows[]?:
    influenceSourceRef
    influenceSourceKindRef
    exactInfluenceRelationRef: U.RelationRef
    influenceGoverningPatternRef
  affectedArchitectureCharacteristicRefs[]: current C.32.ACS criteria-row refs; exact C.25 Q-Bundle slot refs when composite
  evolutionWindowRef
  correspondenceUse
  expectedArchitectureGain
  knownArchitectureLoss
  receivingPatternRef
  sourceReturnCondition
  networkCrossFlowRelationRowRef?: E.18.NET NetworkCrossFlowRelationRowRef
```

The row is a `U.Episteme` about one already obtaining relation. It neither creates that occurrence nor mints a universal Conway relation. The occurrence keeps its identity under its direct relation owner and A.6.REL; this row only describes it for the current correspondence use. `entityOfConcernRef`, its kind, its governor, both architectures, their selected structures, and the changed referent are required. If the practitioner has only a useful local compound correspondence claim, keep it in the frame for candidate synthesis. Assert the row only after the admitted relation kind's direct predicate is applicable and current facts satisfy it affirmatively. If the predicate is false, assert no row; if facts are unresolved, keep the frame and name that boundary; if the kind/predicate is absent, return `missing-governor`. None of these branches permits inferring a relation from two architectures.

#### C.32.CONWAY:4.3 - Qualified network reading

The same exact pair row may appear in `architectureCorrespondenceRowRefs[]` of several `TransformationFlowStructureNetworkRecord@Context` values while its pair, relation occurrence, evolution window, correspondence use, and claim scope remain current. Each citation contributes only one qualified architecture reading. The row's optional singular `networkCrossFlowRelationRowRef`, when present, qualifies only the exact current record edition named by that locator; it does not qualify the row's citations from other records. No citation makes the pair row the network, adds a member, or satisfies the network's exact cross-flow-relation discriminator.

Set `networkCrossFlowRelationRowRef` only when the row's exact relation participants are independently grounded in member-flow positions and its `transformationFlowStructureNetworkRecordRef` names the same exact current record whose `architectureCorrespondenceRowRefs[]` citation this mapping is intended to qualify. Resolve that record first, then require exactly one `crossFlowRelationRow` to match the occurrence and complete ordered endpoint-binding identity. That row must preserve the same kind, governor, participant order, endpoints, and bindings as this correspondence row. Zero or several matches, a different record, or a stale record edition leaves the locator unresolved. Do not reuse one locator to qualify another record's citation. A record citation alone infers none of those facts. Actor, role, Work, changing relation, influence relation, and network cross-flow relation remain separately governed even when one case cites all of them.

#### C.32.CONWAY:4.4 - Candidate moves and repair rows

Plain text begins with the domain action—builds, assembles, repairs, configures, treats, teaches, compiles, or evaluates. It then names the acting system and Work only when those facts are current. In a separate sentence it says which architecture or other source influences which candidate through which exact relation. `Creator`, `creation`, `producer`, `transformer architecture`, and `uses` remain ordinary cues, not universal technical labels.

Choose only pressures that change the candidate or protect against a concrete loss. Every `affectedArchitectureCharacteristicRefs[]` value in an exact pair row or comparison-ready candidate must resolve to a current `C.32.ACS` criteria row; when the pressure is one slot of a composite quality family, also resolve the declared `C.25` Q-Bundle and that exact slot. If those governed objects do not yet exist, put plain heads such as independent change, substitutability, evidence reuse, latency, coupling or cohesion, coordination load, and source-return cost only in the local frame's `provisionalArchitectureCharacteristicHeads[]`; never place them in `affectedArchitectureCharacteristicRefs[]`. These heads are discovery cues, not a universal catalogue and not criteria refs. Return to `C.32.ACS` or `C.25` before making a stronger comparison, selection, or decision claim.

| Correspondence repair row | Use | Minimum repair against overread |
|---|---|---|
| `changedReferentRecovery` | The story names a team, line, tool, method, or organization but not what changes. | Identify the changed referent and direct changing relation before making actor or architecture claims. |
| `performerRecovery` | A source is said to build, design, repair, or operate. | Name the exact system, role assignment when claimed, dated Work when performance is claimed, `performedUnderAssignment`, and direct actor-side or work-to-change relations. |
| `influenceSourceRecovery` | An architecture or structure is said to shape a candidate. | Name its exact kind and direct influence relation; otherwise keep it as a candidate cue. |
| `architecturePairRecovery` | Two architectures are compared or linked. | Apply the direct relation owner. With no kind/predicate, return `missing-governor`; with unresolved facts, keep the pair synthesis-local and name the missing grounding; with a false predicate, assert no occurrence; with a satisfied predicate, name the exact obtaining occurrence and pair. |
| `inverseConwayRetargeting` | The desired transformed architecture is sound, but the current source-side arrangement cannot sustain it. | Change selected influence-source structures and record migration cost, new burden, and stop condition. |
| `transformedArchitectureRetargeting` | The source-side arrangement is fixed or too expensive to change in the current window. | Change the transformed architecture candidate and record the lost desired property or exception. |
| `jointCorrespondenceSynthesis` | Neither side alone can carry the architecture characteristic. | Change both sides and record preserved structure, lost structure, and coordination burden. |
| `boundedCorrespondenceMismatch` | A mismatch is tolerable for now. | State exception cost, bounded-use limit, source-return condition, and reopen trigger. |

**Stop condition.** A first-pass frame may stop when it names the changed referent, separately typed source and transformed architectures, one selected structure on each side, either governed affected-characteristic refs or visibly provisional heads with their exact return, the applicable candidate-form heads, and the next governing pattern. Every acting, performance, or influence fact that is asserted must already have its direct basis. Before a candidate enters comparison or reliance, complete its source-side change, transformed-side change, expected gain, known loss, evolution window, receiving pattern, source-return condition, and stop. An exact pair row additionally requires its direct relation predicate to be satisfied and its obtaining occurrence to be identified. A provisional pressure stays in `correspondenceClaims[]` with the exact reason visible: missing governor, unresolved grounding or information sufficiency, or a false predicate.

**Lowering condition.** Lower an exact row to synthesis-local correspondence material when its relation occurrence, architecture pair, selected structures, changed referent, evolution window, or receiving use is missing or stale. Retire a candidate when its source-side change, transformed-side change, bounded mismatch, or known loss no longer belongs to the declared evolution window. Return to A.3.4 or E.18 when the changed referent or flow relation is not recovered, to A.12 and A.15.1 when the issue is actor or Work attribution, and to C.29 when the current claim is structural similarity or preservation.

