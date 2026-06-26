---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
section_id: "G.6:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__005_solution.md"
commit_sha: "f1d0f9319cf1f93129b7691a328a281022252c4e"
heading_path:
  - "G.6 — Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
  - "G.6:4 — Solution"
line_start: 89763
line_end: 89923
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.4"
  - "A.21"
  - "A.6.5"
  - "A.6.RSIR"
  - "B.3"
  - "C.2.1"
  - "C.28"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.2"
  - "E.17.EFP"
  - "E.18"
  - "E.18.2"
  - "E.24"
  - "E.5.2"
  - "F.10"
  - "F.15"
  - "F.17"
  - "F.9"
  - "G.10"
  - "G.11"
  - "G.4"
  - "G.5"
  - "G.8"
  - "G.9"
  - "G.Core"
keywords:
  - "CrossingBundle"
  - "EvidenceGraph"
  - "GateCrossing"
  - "PathId"
  - "PathSliceId"
  - "SCR/RSCR"
  - "TriggerAliasMap"
  - "UTS PathCard"
  - "lane tags (TA/VA/LA)"
  - "provenance"
  - "Γ-fold pinning"
---

### G.6:4 - Solution

Create a citable `EvidenceGraph` and `PathCitationRecord` set when a local evidence-use statement is too small for the reliance being claimed. Keep the graph declarative and typed: nodes and edges carry provenance relations; `PathId` and `PathSliceId` cite graph paths; a provenance ledger records replayable path entries.

#### G.6:4.1 - Boundary to Neighboring Patterns

`G.6` is a path-addressing pattern over evidence provenance. It consumes or cites the following values without redefining them:

| Current value or relation | Governing pattern |
| --- | --- |
| compact episteme evidence-use or status-use relation | `A.2.4` |
| evidence carrier, source-currentness, evidence-producing work relation, evidence relation, and evidence-provenance addressing basics | `A.10` |
| assurance, trust, safety, compliance, readiness, or release-confidence claim | `B.3` |
| causal-use support basis, identification profile, causal-use verdict, or realizability profile | `C.28` |
| status family, status cell, status-use statement, or cross-context status mapping | `F.10` |
| bridge, congruence level, loss, or context-transfer relation | `F.9` |
| transformation-flow structure, gate crossing, or work occurrence used as evidence source | `E.18`, `A.21`, or `A.15.1` as applicable |
| publication, view, explanation, source-use, or specification-use relation | `E.17`, `E.17.0`, `E.17.2`, `E.17.EFP`, or `E.10.D2` |

Do not add a local `EvidenceRole` value set. Source labels such as "proof role", "measurement role", "benchmark role", or "status role" are repair prompts. Recover the direct evidence-use, status-use, source-use, causal-use, assurance, work, or publication-use relation first.

#### G.6:4.2 - EvidenceGraph

An `EvidenceGraph` is a typed directed acyclic graph used for evidence-provenance citation. It is a graph because path identity, path slicing, and path-local refresh depend on graph structure. The graph is not a holarchy, not a transformation-flow structure, not a work plan, and not a method.

Minimal graph fields:

```text
EvidenceGraph:
  EvidenceGraphId:
  BoundedContext:
  ClaimFamilyOrUse:
  ReferencePlane:
  GraphNodeSet:
  GraphEdgeSet:
  TimePolicyOrWindow:
  SourceCurrentnessPolicy:
  BridgeOrTransferRefs:
  EditionOrPolicyRefs:
  GraphPathAddressingRule:
```

Minimal node kinds:

| Node kind | Value governed by | Use in G.6 |
| --- | --- | --- |
| `EvidenceUseRelationNode` | `A.2.4` or `A.10` | Names one episteme, carrier, source, proof, observation, or record being used as evidence for a claim or use. |
| `EvidenceCarrierNode` | `A.10` | References the concrete carrier or carrier class when material recoverability matters. |
| `SourcePublicationNode` | `E.17` and `A.10` | References a publication, source record, view, explanation, standard, model card, data card, or generated source relation. |
| `EvidenceProducingWorkNode` | `A.15.1` and `A.10` | References work occurrences, measurements, checks, tests, runs, audits, or observations that produced evidence. |
| `MethodDescriptionNode` | `A.3.2` and `A.10` | References the method description or formal substrate used to produce or interpret evidence. |
| `ExternalProducerRoleAssignmentNode` | `A.2.1` and `A.10` | References the work-facing role assignment of the producer, verifier, lab, issuer, or source-maintenance actor when externality decides the evidence relation. |
| `StatusUseRelationNode` | `A.2.4` and `F.10` | References a status-use statement when the path relies on validity, currentness, approval-looking status, or requirement status. |
| `CausalUseReferenceNode` | `C.28` | References causal-use support basis, identification, realizability, or verdict when the path is used for causal claims. |

Minimal edge kinds:

| Edge kind | Meaning |
| --- | --- |
| `verifiedBy` | Formal or proof-like evidence relation. |
| `validatedBy` | Empirical, observational, experimental, or run-time evidence relation. |
| `producedByWork` | Evidence was produced by a named work occurrence, measurement, check, run, or audit. |
| `usesMethodDescription` | Evidence production or interpretation used a named method description, formal substrate, or model description. |
| `derivedFrom` | One evidence node or source record is derived from another through a declared transformation, extraction, copy, representation shift, summary, or publication-use relation. |
| `happenedBefore` | A temporal ordering relation needed for the evidence claim. |
| `citesSource` | The path depends on a source publication, source record, status source, or source-currentness relation. |
| `crossesViaBridge` | The path crosses bounded context, reference plane, edition, or other bridge-relevant boundary through an explicit bridge or loss relation. |
| `hasStatusUse` | The path depends on a status-use statement rather than a display label. |
| `hasCausalUseRef` | The path depends on causal-use content governed by `C.28`. |

Extra graph annotations may exist for diagrams or tools, but conformance depends only on typed nodes, typed edges, path addresses, windows, constraints, and governing-pattern refs.

#### G.6:4.3 - PathId and PathSliceId

A `PathId` is a stable identifier for one claim-local graph path inside an `EvidenceGraph`. A `PathSliceId` is a stable identifier for the same path under a declared slice: time window, reference plane, bounded context, edition, bridge, policy, or selected evidence subset.

Here `path` means a path in the evidence-provenance graph. It is not an imperative route, work sequence, workflow, or transformation-flow path.

Use this compact record:

```text
PathCitationRecord:
  ClaimOrUseRef:
  EvidenceGraphRef:
  PathId:
  PathSliceId:
  BoundedContext:
  ReferencePlane:
  EvidenceUseRefs:
  PathNodeRefs:
  PathEdgeRefs:
  TimeWindowOrFreshnessPolicy:
  SourceCurrentnessRefs:
  BridgeOrLossRefs:
  EditionOrPolicyRefs:
  DownstreamCitationUse:
  NotCarried:
  ReopenTrigger:
```

`NotCarried` names the stronger claim not carried by this graph path: approval, permission, gate passage, release, performed work, assurance, causal identification, status assertion, compliance, benchmark superiority, or truth outside the declared claim and scope.

#### G.6:4.4 - Provenance Ledger

A `ProvenanceLedger` is a citable record over `PathCitationRecord` entries. It is not a work-progress log, review-comment log, or process-status log.

Minimal fields:

```text
ProvenanceLedger:
  LedgerId:
  EvidenceGraphRef:
  PathCitationRecords:
  SourceOrderPolicy:
  CurrentnessPolicy:
  PrivacyOrDisclosureBoundary:
  RefreshScopeRule:
```

Use a provenance ledger when several downstream records need the same path family: selector records, benchmark harnesses, assurance cases, release packages, maturity transitions, refresh records, or safety reviews. Do not create a ledger merely because one local evidence-use statement is easy to write in prose.

#### G.6:4.5 - Refresh and Source Return

Reopen the smallest affected path when one of these changes:

* evidence carrier identity, integrity, access, or hash;
* source publication, source order, supersession, or currentness window;
* work occurrence, measurement run, method description, proof check, or observation record;
* bridge, congruence level, loss statement, reference plane, or bounded context;
* causal-use profile, status-use statement, assurance-use requirement, or gate relation consumed downstream;
* edition, policy, threshold, verifier rule, relying-party context, or minimum disclosure boundary.

The reopen result is local to `PathId`, `PathSliceId`, or the smallest graph subpath that carries the changed relation. It does not rewrite the whole project and does not certify a new downstream decision by itself.

#### G.6:4.6 - Declarative Representation Discipline

`EvidenceGraph`, `PathId`, and `PathSliceId` are declarative representation values. They tell a reader what provenance relation is being cited. They do not tell a worker what to do next.

When a source phrase says "evidence path", "provenance route", "audit trail", "lineage flow", "data pipeline", or "workflow", recover the kind before copying the word:

| Source phrase is about | Governed by |
| --- | --- |
| graph path from claim to evidence and source refs | `G.6` and `A.10` |
| actual work that produced evidence | `A.15.1` |
| method or procedure for producing evidence | `A.3.1` and `A.3.2` |
| transformation-flow structure or graph | `E.18` and `E.18.2` |
| publication view, source form, explanation, or exported report | `E.17`, `E.17.0`, `E.17.2`, or `E.17.EFP` |
| assurance, gate, release, or permission use | `B.3`, `A.21`, or the direct governing boundary pattern |

#### G.6:4.7 - Extension Wiring Without Core Drift

Method-family, benchmark, selector, parity, or telemetry patterns may add required pins to a `PathCitationRecord`. They do not add new core node kinds unless the governing pattern explicitly changes G.6.

Examples:

* `G.5` may cite a `PathId` for selector explainability or admissibility.
* `G.9` may cite a `PathSliceId` for benchmark parity or replication lineage.
* `G.11` may consume reopen triggers and affected path slices for refresh.
* A causal-use pattern may add `C.28` refs to a path, but the causal-use relation remains governed by `C.28`.
* An assurance pattern may consume a path, but the assurance tuple remains governed by `B.3`.

