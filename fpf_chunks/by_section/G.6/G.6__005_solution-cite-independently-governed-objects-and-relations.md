---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
section_id: "G.6:4"
section_title: "Solution — cite independently governed objects and relations"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__005_solution-cite-independently-governed-objects-and-relations.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "G.6 — Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
  - "G.6:4 — Solution — cite independently governed objects and relations"
line_start: 128906
line_end: 129067
dependencies:
  - "A.10"
  - "A.10.1"
  - "A.13"
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
  - "E.24.PUB"
  - "F.10"
  - "F.6"
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

#### G.6:4.1 - Subject-pattern map

| Represented claim or object | Subject pattern before G.6 represents it |
| --- | --- |
| Reusable method, generic participants, parameters, effects, and conditions | `A.3.1` for the exact `U.Method`; `A.3.2` for its `U.MethodDescription` |
| Independently admitted dated Work and its exact actual performer refs; optional obtaining F.6 relation and assignment occurrence refs when the path expressly consumes attribution; enactment, resources, and direct participation or binding facts | `A.13` for each exact actual performer and `A.15.1` for independent Work admission; `F.6` and `A.2.1` only when the path represents precise assignment-bound attribution; the exact direct participation or resource relation; and `A.6.1` for operation-application bindings |
| Production or inception of an entity or episteme | one exact local A.15.PROD claim when its entry condition is met, or a direct subject predicate under its own pattern |
| Measurement result and its measurement-specific basis | `C.16` |
| Acceptance-clause application or other runtime evaluation result | `G.4` or the exact formal, conformance, diagnostic, causal, comparison, selection, gate, or decision governor |
| Work-resource aggregation result | `B.1.6` |
| Durable episteme that states a local result | `C.2.1`; it remains distinct from the domain result |
| Outcome, later action, acceptance, gate passage, permission, or decision | its exact work and domain governor, including `C.11` or `A.21` when applicable |
| Source publication, carrier, copy, extraction, or publication occurrence | `E.17` for a source-backed face and source return; `E.24.PUB` for an obtaining publication occurrence; the direct rule for each copy, extraction or source relation |
| Representation correspondence | `C.29` |
| Bridge, congruence, loss, or cross-context transfer | `F.9` |
| Transformation-flow structure distinct from performed work | `E.18` and `E.18.2` |
| First evidence/status use, provenance and bounded reliance, currentness, or assurance | `A.2.4`, `A.10`, `G.11`, or `B.3` respectively |

If the subject pattern or relation cannot be recovered, the path records an unresolved gap and cannot present that edge as obtaining.

Do not add a local `U.EvidenceRole` or turn proof, measurement, benchmark, source, or status labels into system-role kinds. For any claim that a producer, verifier, laboratory, issuer, or maintainer participates, recover the exact direct relation, the participants it declares, and the place each actual participant fills. Other nearby facts—for example, a local system-role kind, assignment, Work occurrence, responsibility, authority, or permission—are separate and may be cited only when they independently obtain; none establishes participation. Do not infer that a passive laboratory or produced entity performs Work merely because the path cites it.

**Work recovery and compact citation.** Before G.6 represents dated `U.Work`, its subject account must already recover each exact actual performer through A.13 and admit that Work independently under `A.15.1`. Include an assignment occurrence and obtaining F.6 relation only when the graph path or receiving use expressly consumes precise assignment-bound attribution; any present attribution must use the same obtaining A.13 assignment. If a required Work or performer ref is absent, record a Work gap. If an expressly consumed F.6 ref is absent or unresolved, retain the Work node and record an attribution gap rather than suppressing the Work. G.6 neither re-admits the Work nor retests assignment species, occurrence identity, holder, classification, predicate duration, or interval coverage. Merely listing an assignment beside Work establishes no relation between them.

#### G.6:4.2 - EvidenceGraph as a representation

An `EvidenceGraph` is a typed directed graph used for provenance citation and replay. It may project a dependency-closed slice of independently governed objects and relations.

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

A node record is a projection:

```text
RepresentedNodeRecord:
  GraphNodeId
  RepresentedObjectRef
  ObjectKindAsGoverned
  SubjectPatternLocator
  ContextEditionOrTimeQualification?
  RepresentationRef
```

Node records use the object kinds and subject patterns in §4.1. Every cited Work occurrence uses the independently established performer and A.15.1 Work refs specified there; add F.6 refs only when precise attribution is consumed. Co-listing creates no relation among the cited objects.

An asserted edge is also a projection:

```text
RepresentedRelationEdgeRecord:
  GraphEdgeId
  DirectRelationRef
  DirectRelationKindRef
  ActualParticipantRefs
  SubjectPatternLocator
  ObtainingClaimRef
  ContextEditionOrTimeQualification?
  RepresentationRef
```

Before the edge enters a relied-on path, the exact direct relation must already be established under its governor. The participant refs in the edge must match that relation; adjacency, direction, shared identifiers, timestamps, source order, or visual layout cannot supply them. `RepresentationRef` points outward to the applicable C.29 correspondence when that correspondence is current.

G.6 defines no fallback core edge vocabulary. Legacy or display labels such as `verifiedBy`, `validatedBy`, `measuredBy`, `producedByWork`, `derivedFrom`, `usesMethodDescription`, `citesSource` or `evidences` are navigation prompts. Recover the exact direct relation and its governor before asserting an edge as obtaining.

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
  SubjectPatternLocators
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

`NotCarried` names the stronger claim or use at issue that the path does not establish. Recover the exact premise, reference, operation-argument, decision-use, or other direct relation for actual downstream use. If the use asserts dated `U.Work`, cite its independently admitted A.15.1 Work ref and A.13-qualified performer refs. Add attribution refs only when the use expressly consumes precise assignment-bound attribution. Path availability or citation alone does not establish that use.

#### G.6:4.4 - Provenance ledger

A `ProvenanceLedger` indexes `PathCitationRecord` entries for citation and replay. Its object and relation indexes let a user find paths that cite the same basis.

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

Use a ledger when several downstream consumers need the same path family; a single local source-to-use account can remain in A.10.

#### G.6:4.5 - Refresh and source return

When a cited object, direct relation, governor, source, bridge, representation correspondence, edition, policy, time window, currentness result or reliance boundary changes, start at its node or relation-edge projection. Identify the exact changed claim or condition and the receiving use it may alter. Use the represented-object and direct-relation indexes to locate other `PathId` or `PathSliceId` values that consume the same basis. The first located slice is an entry to this inquiry, not its completion boundary.

For each candidate path, recover the actual premise, evidence-use, operation-argument or other direct use under its governor. Follow that dependence while a receiving claim, action or required check can change. A shared calibration, causal assumption or source conclusion can affect several otherwise separate paths; include each affected use. Common storage, a citation or graph reachability alone establishes no such dependence. When a changed source requires discovery beyond an adequate existing index, use A.10.1 for its bounded search, direct-use test and coverage limits. An unsearched or unresolved branch is a limit on the conclusion, not an unaffected branch.

Retain independent results and their qualified paths. For an affected branch, return to the subject pattern to determine whether the available basis supports the same result, a narrower use, a changed result or a scoped gap. If a represented relation no longer obtains or its required support is unavailable, remove it from the relied-on path or mark that gap; retain the earlier account for its historical use where warranted. G.11 uses the resulting dependency scope to decide which refresh actions, if any, are needed. Updating a projection does not establish a replacement relation or perform that Work.

#### G.6:4.6 - Declarative representation discipline

`EvidenceGraph`, `PathId`, `PathSliceId` and `ProvenanceLedger` identify the governed accounts a reader can inspect. When a needed account is missing, return to its subject pattern.

| Current phrase or artifact | Required recovery before G.6 representation |
| --- | --- |
| method, protocol, algorithm, clause, or policy | exact reusable declaration; when the path cites dated Work, recover it separately under §4.1; when it cites actual operation bindings, recover them under A.6.1 |
| work trace, run, test, audit, measurement, or evaluation | independently admitted dated Work ref and A.13-qualified actual performer refs under §4.1; enacted Method, resources, exact direct participation facts, and A.6.1 binding facts remain separate; expose an assignment occurrence and obtaining F.6 relation only when the path expressly consumes precise assignment-bound attribution |
| produced carrier, model, report, or episteme | exact produced entity and either its subject-specific direct production relation, when the subject pattern declares one, or the one local A.15.PROD production-work or inception claim that the current use needs |
| reading, score, verdict, estimate, aggregate, diagnosis, or outcome | exact domain result and direct governor; distinct C.2.1 episteme when durably stated |
| publication, view, export, or graph rendering | exact source relation, E.17 source-backed face, E.24.PUB publication occurrence, and C.29 representation correspondence when each is current |
| evidence, provenance, currentness, reliance, or assurance | A.2.4/A.10, G.11, and B.3 under their separate entry conditions |
| later acceptance, gate, release, or decision | its local result and exact later-use relation under their direct rules; dated Work admitted under §4.1 when that occurrence is asserted |

#### G.6:4.7 - Extension wiring without core drift

Selector, benchmark, assurance, refresh or telemetry patterns may require additional pins in `PathCitationRecord` and cite `PathId` or `PathSliceId`. Each added record still names its represented object or direct relation and governor.

`G.5` may cite a path for selector explanation, `G.9` for benchmark replication, `G.11` for local refresh, and B.3 for an assurance input. Their selection, benchmark, currentness, and assurance results remain their own.

