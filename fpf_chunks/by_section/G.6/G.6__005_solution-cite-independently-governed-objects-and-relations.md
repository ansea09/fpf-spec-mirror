---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
section_id: "G.6:4"
section_title: "Solution — cite independently governed objects and relations"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__005_solution-cite-independently-governed-objects-and-relations.md"
commit_sha: "1eb56cd0cfd6dccad65143e03d28509373bd8dd5"
heading_path:
  - "G.6 — Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
  - "G.6:4 — Solution — cite independently governed objects and relations"
line_start: 99243
line_end: 99400
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.PROD"
  - "A.2.1"
  - "A.2.4"
  - "A.6.1"
  - "B.1.6"
  - "B.3"
  - "C.16"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "E.17"
  - "E.18"
  - "E.18.2"
  - "F.10"
  - "F.9"
  - "G.11"
  - "G.4"
  - "G.5"
  - "G.9"
keywords:
  - "EvidenceGraph"
  - "NotCarried"
  - "PathCitationRecord"
  - "PathId"
  - "PathSliceId"
  - "actual-use relation"
  - "direct governors"
  - "downstream work"
  - "exact direct relations"
  - "exact represented objects"
  - "local refresh"
  - "obtaining claims"
  - "provenance ledger"
  - "representation correspondence"
  - "source/currentness"
  - "unresolved gaps"
---

### G.6:4 - Solution — cite independently governed objects and relations

Create an `EvidenceGraph` only after the relied-on claim or bounded use and its supporting objects have been recovered. The graph is a declarative, addressable representation. Each node record cites one independently governed object; each asserted edge record cites one independently established direct relation. `PathId`, `PathSliceId`, and the provenance ledger add citation and refresh locality, not world-side facts.

#### G.6:4.1 - Direct-owner map

| Represented claim or object | Direct owner before G.6 represents it |
| --- | --- |
| Reusable method, generic participants, parameters, effects, and conditions | exact `U.Method`; `A.3.2` for its `U.MethodDescription` |
| Dated work, role assignment, enactment, resources, and actual participants or bindings | `A.15.1`, `A.2.1`, exact subject relations, and `A.6.1` when operation-application bindings are used |
| Production or inception of an entity or episteme | the exact production relation and `A.15.PROD` when its entry condition is met |
| Measurement result and its measurement-specific basis | `C.16` |
| Acceptance-clause application or other runtime evaluation result | `G.4` or the exact formal, conformance, diagnostic, causal, comparison, selection, gate, or decision governor |
| Work-resource aggregation result | `B.1.6` |
| Durable episteme that states a local result | `C.2.1`; it remains distinct from the domain result |
| Outcome, later action, acceptance, gate passage, permission, or decision | its exact work and domain governor, including `C.11` or `A.21` when applicable |
| Source publication, carrier, copy, extraction, or publication occurrence | `E.17` family and the exact source relation owner |
| Representation correspondence | `C.29` |
| Bridge, congruence, loss, or cross-context transfer | `F.9` |
| Transformation-flow structure distinct from performed work | `E.18` and `E.18.2` |
| First evidence/status use, provenance and bounded reliance, currentness, or assurance | `A.2.4`, `A.10`, `G.11`, or `B.3` respectively |

G.6 does not substitute for any row. If the direct owner or relation cannot be recovered, the path records an unresolved gap and cannot present that edge as obtaining.

Do not add a local `U.EvidenceRole` or turn proof, measurement, benchmark, source, or status labels into roles. A producer, verifier, laboratory, issuer, or maintainer participates only through an independently established work-facing role assignment and exact work relation.

#### G.6:4.2 - EvidenceGraph as a representation

An `EvidenceGraph` is a typed directed graph used for provenance citation and replay. It may project a dependency-closed slice of independently governed objects and relations. It is not a holarchy, work plan, method, transformation flow, result algebra, or proof that its contents obtain.

Minimal graph fields:

```text
EvidenceGraph:
  EvidenceGraphId
  ReliedOnClaimOrBoundedUseRef
  BoundedContext
  ReferencePlane
  RepresentedNodeRecords
  RepresentedRelationEdgeRecords
  TimeWindowOrPolicy
  SourceCurrentnessRefs
  BridgeOrLossRefs
  EditionOrPolicyRefs
  GraphPathAddressingRule
  C29RepresentationRefs
```

A node record is a projection, not a new universal object kind:

```text
RepresentedNodeRecord:
  GraphNodeId
  RepresentedObjectRef
  ObjectKindAsGoverned
  DirectGovernorRef
  ContextEditionOrTimeQualification?
  RepresentationRef
```

The node set may cite exact work occurrences, role assignments, actual bindings, produced entities, measurement or other subject results, evaluation or aggregation results, C.2.1 result epistemes, outcomes, source publications, carriers, currentness results, reliance dispositions, and later work. Co-listing creates no relation among them.

An asserted edge is also a projection:

```text
RepresentedRelationEdgeRecord:
  GraphEdgeId
  DirectRelationRef
  DirectRelationKindRef
  ActualParticipantRefs
  DirectGovernorRef
  ObtainingClaimRef
  ContextEditionOrTimeQualification?
  RepresentationRef
```

Before the edge enters a relied-on path, the exact direct relation must already be established under its governor. The participant refs in the edge must match that relation; adjacency, direction, shared identifiers, timestamps, source order, or visual layout cannot supply them. `RepresentationRef` points outward to the applicable C.29 correspondence when that correspondence is current.

G.6 defines no fallback core edge vocabulary. Legacy or display labels such as `verifiedBy`, `validatedBy`, `measuredBy`, `producedByWork`, `derivedFrom`, `usesMethodDescription`, `citesSource`, or `evidences` are navigation prompts only. Replace each with the exact formal, measurement, work, production, publication, representation, provenance, temporal, status-use, premise, reference, argument, or other direct relation before asserting the edge as obtaining.

#### G.6:4.3 - PathId and PathSliceId

A `PathId` identifies one claim-local path inside an `EvidenceGraph`. A `PathSliceId` identifies the same path under a declared time window, reference plane, bounded context, edition, bridge, policy, or selected object/relation subset.

Use this compact record:

```text
PathCitationRecord:
  ReliedOnClaimOrBoundedUseRef
  EvidenceGraphRef
  PathId
  PathSliceId
  BoundedContext
  ReferencePlane
  RepresentedObjectRefs
  RepresentedDirectRelationRefs
  DirectGovernorRefs
  SourcePublicationAndCarrierRefs
  C29RepresentationRefs
  TimeWindowOrFreshnessPolicy
  SourceCurrentnessRefs
  BridgeOrLossRefs
  EditionOrPolicyRefs
  DownstreamWorkRef?
  ExactDownstreamUseRelationRef?
  A10RelianceDispositionRef?
  NotCarried
  UnresolvedRelationGaps
  ReopenTrigger
```

`NotCarried` names every stronger use that the path does not establish: work occurrence, participation, production, claim truth, assurance, approval, permission, gate passage, release, causal identification, benchmark superiority, acceptance, or decision. Actual downstream use requires dated work and one exact premise, reference, operation-argument, decision-use, or other direct relation; path availability or citation is not actual use.

#### G.6:4.4 - Provenance ledger

A `ProvenanceLedger` is a citable replay index over `PathCitationRecord` entries. It is not a work-progress log, result registry, review-comment log, process-status log, or ontic source.

```text
ProvenanceLedger:
  LedgerId
  EvidenceGraphRef
  PathCitationRecords
  RepresentedObjectIndex
  RepresentedDirectRelationIndex
  SourceOrderPolicy
  CurrentnessPolicy
  PrivacyOrDisclosureBoundary
  RefreshScopeRule
```

The ledger may cite work, participants, produced entities, domain results, result epistemes, outcomes, sources, transformations, representation correspondences, provenance, and later uses. A row establishes none of them. Use a ledger when several downstream consumers need the same path family; do not create one merely because a local A.10 account is easy to write.

#### G.6:4.5 - Refresh and source return

Reopen the smallest affected `PathId`, `PathSliceId`, node projection, or relation-edge projection when any cited object, direct relation, governor, source, bridge, representation correspondence, edition, policy, time window, currentness result, or reliance boundary changes.

If the direct relation no longer obtains or its proof becomes unavailable, remove it from the relied-on path or mark the exact unresolved gap. Do not preserve the edge from graph history, infer a replacement relation, rerun unrelated paths, or certify a new downstream result through refresh alone.

#### G.6:4.6 - Declarative representation discipline

`EvidenceGraph`, `PathId`, `PathSliceId`, and `ProvenanceLedger` tell a reader which already governed account is being cited. They do not tell a worker what to do and they do not reconstruct missing world-side facts.

| Current phrase or artifact | Required recovery before G.6 representation |
| --- | --- |
| method, protocol, algorithm, clause, or policy | exact reusable declaration; dated work and actual bindings only when independently established |
| work trace, run, test, audit, measurement, or evaluation | dated work, role assignment, method enactment, resources, and actual direct/A.6.1 bindings |
| produced carrier, model, report, or episteme | exact produced entity and production/inception relation |
| reading, score, verdict, estimate, aggregate, diagnosis, or outcome | exact domain result and direct governor; distinct C.2.1 episteme when durably stated |
| publication, view, export, or graph rendering | exact source/publication relation and C.29 representation correspondence when current |
| evidence, provenance, currentness, reliance, or assurance | A.2.4/A.10, G.11, and B.3 under their separate entry conditions |
| later acceptance, gate, release, or decision | separate dated work, local result, and exact later-use relation |

#### G.6:4.7 - Extension wiring without core drift

Selector, benchmark, assurance, refresh, or telemetry patterns may require additional pins in `PathCitationRecord`. They may cite `PathId` or `PathSliceId`, but they do not mint a universal edge, result, evidence, or criterion-participant relation. Any added graph record still names the exact represented object or direct relation and its governor.

`G.5` may cite a path for selector explanation, `G.9` for benchmark replication, `G.11` for local refresh, and B.3 for an assurance input. Their selection, benchmark, currentness, and assurance results remain their own.

