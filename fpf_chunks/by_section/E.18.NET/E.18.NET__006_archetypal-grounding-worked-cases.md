---
chunk_kind: "child"
pattern_id: "E.18.NET"
pattern_title: "Network of Transformation-Flow Structures"
section_id: "E.18.NET:5"
section_title: "Archetypal Grounding — worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.NET/E.18.NET__006_archetypal-grounding-worked-cases.md"
commit_sha: "2ada413629b846ef308222d16489a82cb5b40a71"
heading_path:
  - "E.18.NET — Network of Transformation-Flow Structures"
  - "E.18.NET:5 — Archetypal Grounding — worked cases"
line_start: 83907
line_end: 83976
dependencies:
  - "A.12"
  - "A.15"
  - "A.22"
  - "A.22.CGUS"
  - "A.3.4"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.6.REL"
  - "C.2.1"
  - "C.29"
  - "C.30.TFS-REL"
  - "C.32.CONWAY"
  - "E.11.PUA"
  - "E.17"
  - "E.18"
  - "E.18.2"
  - "E.18.3"
  - "F.18"
  - "U.Transfer"
keywords:
---

### E.18.NET:5 - Archetypal Grounding — worked cases

#### E.18.NET:5.1 - Same surface vocabulary, different ontic answers

**Several valuations of one TFS.** A cooling-loop review compares nominal-load and emergency-load valuations of the same exact cooling-loop `TransformationFlowStructure`. Both valuations use the same structure positions and internal `U.Transfer` occurrences. The load value, path slice, and local tags differ; the TFS identity does not. E.18.NET is not used.

**Internal coffee subflow.** A coffee-brewing TFS exposes a preparation portion containing grinding, dosing, and wetting positions plus their parent-internal `U.Transfer` occurrences. Its entry and exit remain positions of the brewing TFS. The practitioner uses E.18's `SubflowRef`; no second TFS or network is created.

**Independent network.** A roastery-production TFS and a café-brewing TFS have separate governed objects, Work occurrences, valuation boundaries, and architecture change cadence. The direct supply owner has an admitted relation kind, supplies the predicate and applicability, and the current delivery-and-acceptance facts satisfy that predicate for a dispatch position in the first and an accepted-stock position in the second. For ordinary first use, fill the selected network directly:

```text
selectedNetworkRef: RoasteryCafeSupplyNetwork@CoffeeService
directMemberRefs[]:
  - RoasteryProductionTFS@Dispatch
  - CafeBrewingTFS@AcceptedStock
selectedCrossFlowRelationOccurrenceRefs[]:
  - SupplyOccurrence@Lot24Dispatch-to-CafeAcceptance
selectedNetworkConstraintRefs[]:
  - SupplyEndpointConstraint@Dispatch-to-AcceptedStock
  - SelectedExposureConstraint@RoasteryDispatch-and-CafeAcceptedStock
  - AcyclicDirectMemberConstraint@RoasteryCafe
networkUseFrame:
  questionOrAction: decide which accepted stock can enter the coffee-service brewing flow
  forbiddenOverread: shared coffee does not make both members one TFS or make supply a generic edge
returnCondition: either member, the supply occurrence, an endpoint or exposure, acyclicity, or the coffee-service question changes
```

This filled basis is enough for the immediate selection; it is not a `TransformationFlowStructureNetworkRecord@Context`. Create that separate descriptive record only when the result must survive the current work. With no direct supply kind or predicate, the same diagram remains a proposed description with `missing-governor`. With an applicable governor but undecided facts, it remains proposed with the missing grounding or information-sufficiency boundary. With a false predicate, no supply occurrence fills the network. With a satisfied predicate but a missing endpoint binding, it remains proposed with that binding named.

#### E.18.NET:5.2 - Recursive build-the-builder

A project distinguishes five independently identified flow structures:

1. a compiler-source-change TFS;
2. a bootstrap-compiler build TFS;
3. an application-build TFS using the admitted compiler artifact through a directly governed project relation;
4. a release-assurance TFS that evaluates the built application through its own direct relation; and
5. a deployment-and-operation TFS whose exact software-use relation is governed separately.

It then selects four nested networks. `CompilerBuildNetwork` has members 1 and 2. `ApplicationCompilerUseNetwork` has that independently identified network and member 3. `ReleaseAssuranceNetwork` has `ApplicationCompilerUseNetwork` and member 4. `DeliveryOperationNetwork` has `ReleaseAssuranceNetwork` and member 5. Every selection has at least two direct members and its own exact obtaining cross-member relation occurrence and endpoint bindings.

The bootstrap compiler result is exposed from the outer delivery network through this exact finite path:

```text
ExposedFlowPositionRef:
  networkStructureRef: DeliveryOperationNetwork
  memberPath[]:
    - ReleaseAssuranceNetwork
    - ApplicationCompilerUseNetwork
    - CompilerBuildNetwork
    - BootstrapCompilerBuildTFS
  leafFlowPositionRef:
    transformationFlowStructureRef: BootstrapCompilerBuildTFS
    localFlowPositionId: ExecutableCompilerResult
```

Each path entry is a direct member of the preceding network, the final entry is the TFS named by `leafFlowPositionRef`, and no network repeats. This is one four-entry member path, not four numbered network kinds. “Builds”, “uses”, “evaluates”, and “delivers” remain ordinary cues until every selected cross-member link resolves to its exact direct relation kind, participants, obtaining occurrence, and endpoint bindings.

#### E.18.NET:5.3 - N-ary relation and feedback cycle

A manufacturing release relation has three participants under one direct domain pattern: one product-definition position in a development TFS, one equipment-readiness position in a production-system-change TFS, and one release-condition position in an assurance TFS. Its network row keeps the three participants and their order. It is not replaced by three unlabeled arrows.

Later, an exact use-observation relation connects an operating TFS position back to a development TFS position. The relation occurrences form a feedback cycle, while the selected direct-member nesting remains acyclic. The feedback does not make the operating TFS a member of itself and does not turn observation into development Work.

#### E.18.NET:5.4 - Architecture and demonstrative reading

For one containing product-development holon, a current `ArchitectureOf@Context` claim may select the network among its structures. If the selected members belong to separately named holons and no containing bearer is grounded, record the use as inter-holon and name the participating architecture claims. Do not invent one system that contains them merely to fill the architecture field.

A teaching mantra may show a finite admitted dependency slice through the network. The slice uses only the network locator family, cites admitted positions and exact relation-reference epistemes, and keeps omissions and return visible. It does not prescribe project work order and does not make the displayed path the whole network.

