---
chunk_kind: "child"
pattern_id: "E.18.NET"
pattern_title: "Network of Transformation-Flow Structures"
section_id: "E.18.NET:5"
section_title: "Archetypal Grounding — worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.NET/E.18.NET__006_archetypal-grounding-worked-cases.md"
commit_sha: "308edacfa2bdb2c60d07e4e10c0deb1f260a6a31"
heading_path:
  - "E.18.NET — Network of Transformation-Flow Structures"
  - "E.18.NET:5 — Archetypal Grounding — worked cases"
line_start: 83999
line_end: 84078
dependencies:
  - "A.1.STM"
  - "A.12"
  - "A.15"
  - "A.15.6"
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

#### E.18.NET:5.2 - Project system-of-interest and recursive build-the-builder

For one project question, practitioners ask which independently identified flow structures must be considered together to connect production and later operation of the project system-of-interest, and which builder branches must also be visible. The actual project remains composite `U.Work`; the selected network is a non-agentive `U.Structure`. Project designation, U.System identity, a role interpretation, and any assignment remain separate.

For a compiler-and-application use, practitioners independently identify five TFS values by the questions they answer:

1. a TFS whose loci bind the compiler-edition preparation and directly governed source-use facts needed by the build;
2. a TFS whose loci bind Work and changes of pre-existing build substrates plus production and identity-inception claims for one bootstrap compiler;
3. a TFS whose loci bind application-production Work and the exact use of that admitted compiler;
4. a TFS selected for release-assurance questions; and
5. a TFS selected for deployment and operation after the application system exists.

These descriptions are not TFS kinds or lifecycle phases. No transformation of a not-yet-existing compiler or application is asserted. Each TFS, Work occurrence, change of a continuing referent, production claim, identity-inception claim, completion claim, role assignment, and later operation/use fact keeps its direct owner.

In this worked use, `CompilerArchitectureTeam-1 : U.System` performs dated `CompilerNetworkSelectionWork-5 : U.Work` under obtaining `CompilerNetworkSelectionAssignment-5`; the separately identified result episteme records the accountable selection decision. During that Work the team selects nested networks only after exact cross-member relations obtain and every endpoint is bound. `CompilerRealizationNetwork` selects members 1 and 2 through the exact source/use, production, or other admitted occurrences needed by that use. `ApplicationCompilerUseNetwork` selects that network and member 3 through the exact compiler-input or operation-application occurrence supplied by its direct owner. `ReleaseAssuranceNetwork` adds member 4 through its exact evaluation or assurance occurrence. `DeliveryOperationNetwork` adds member 5 through its exact deployment, participation, application, or use occurrence. The names are local designators; every selection still needs direct members, obtaining relation occurrences, applied constraints, and its own `networkUseFrame`. The project Work, network, result episteme, team, assignment, and selection Work remain different objects.

A compiler-production case can close on separately grounded identity inception, production completion or readiness, evidence, and decision while naming the application-build position as the downstream use outside that closed case. Project-level reasoning continues into the member where the compiler later participates. The same joint-selection question recurs for a builder system: select the TFS in which that admitted builder performs exact Work together with the independently identified TFS or nested network concerning production and identity inception of the builder, or its later change after it exists. Shared identity creates no edge; use exact production, inception, participation, application, use, or other directly governed occurrences and endpoint bindings.

The bootstrap compiler result is exposed from the outer network through one finite member path:

```text
ExposedFlowPositionRef:
  networkStructureRef: DeliveryOperationNetwork
  memberPath[]:
    - ReleaseAssuranceNetwork
    - ApplicationCompilerUseNetwork
    - CompilerRealizationNetwork
    - BootstrapCompilerBuildTFS
  leafFlowPositionRef:
    transformationFlowStructureRef: BootstrapCompilerBuildTFS
    localFlowPositionId: ExecutableCompilerResult
```

Each path entry is a direct member of the preceding network, the final entry is the TFS named by `leafFlowPositionRef`, and no network repeats. `FlowValuation`, path slices, and `DesignRunTag` remain leaf-local. “Builds”, “uses”, “evaluates”, and “delivers” are ordinary cues until each link resolves to an admitted relation kind, complete participant signature, obtaining occurrence, and endpoint bindings.

Before these identities and relations are grounded, A.1.STM may show the dependency only as a Plain provisional long-mantra map and must name the missing member, governor, false or unresolved predicate, occurrence, or binding. It is not yet an E.18.NET selection. Once the network is admitted, a separate A.22.CGUS demonstrative slice may traverse admitted positions and relation-reference epistemes; it remains a demonstration, not the project, network, case, or Work order.

#### E.18.NET:5.3 - N-ary relation and feedback cycle

A manufacturing release relation has three participants under one direct domain pattern: one product-definition position in a TFS selected to answer the development question, one equipment-readiness position in a TFS selected to follow the changes that establish equipment readiness, and one release-condition position in a TFS selected for assurance. Its network row keeps the three participants and their order. It is not replaced by three unlabeled arrows.

Later, an exact use-observation relation connects a position in a TFS selected for operation or use back to a position in a TFS selected to answer the development question. The relation occurrences form a feedback cycle, while the selected direct-member nesting remains acyclic. The feedback does not make the operation-or-use TFS a member of itself and does not turn observation into development Work.

#### E.18.NET:5.4 - Architecture and two demonstrative boundaries

For one containing holon, a current `ArchitectureOf@Context` claim may select the network among its structures. If the selected members belong to separately named holons and no containing bearer is grounded, record the use as inter-holon and name the participating architecture claims. Do not invent one system merely to fill the architecture field.

A Plain A.1.STM long-mantra map may display proposed members and a missing cross-member link before network admission. It names the intended final result and the absent member, governor, predicate result, occurrence, or endpoint binding; it asserts neither an E.18.NET structure nor a CGUS.

After the network is admitted, a separate teaching mantra may show one finite admitted dependency slice. The slice uses the network locator family, cites admitted positions and exact relation-reference epistemes, and keeps omissions and return visible. It does not prescribe project Work order, make the path the whole network, or turn a leaf-local `DesignRunTag` into a project phase.

