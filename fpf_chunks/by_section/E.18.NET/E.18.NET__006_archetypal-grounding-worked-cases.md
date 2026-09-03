---
chunk_kind: "child"
pattern_id: "E.18.NET"
pattern_title: "Network of Transformation-Flow Structures"
section_id: "E.18.NET:5"
section_title: "Archetypal Grounding — worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.NET/E.18.NET__006_archetypal-grounding-worked-cases.md"
commit_sha: "59c455329e49715c64dc1b16f22c1efba6a3cf6f"
heading_path:
  - "E.18.NET — Network of Transformation-Flow Structures"
  - "E.18.NET:5 — Archetypal Grounding — worked cases"
line_start: 87645
line_end: 87736
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
  - "E.11"
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

**Independent network.** A roastery-production TFS and a café-brewing TFS concern different objects and have separate Work occurrences, valuation boundaries, and architecture change cadence. The applicable supply pattern defines its predicate and applicability, and the current delivery-and-acceptance facts satisfy that predicate for a dispatch position in the first and an accepted-stock position in the second. For ordinary first use, fill the selected network directly:

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
  admissibleUse: use the selected supply relation to choose accepted coffee stock for the brewing flow
  stopOrReturnCondition: return to the supply claim when its delivery-and-acceptance basis no longer supports this stock choice
returnCondition: either member, the supply occurrence, an endpoint or exposure, acyclicity, or the coffee-service question changes
```

This filled basis is enough for the immediate selection; it is not a `TransformationFlowStructureNetworkRecord@Context`. Create that separate descriptive record only when the result must survive the current work. If the supply claim has no admitted relation kind or applicable predicate, carry the governing pattern's `missing-governor` result. If required facts are unavailable, carry `missing-information`; if a sufficient case basis fails the positive test, carry `factually unsupported`. Neither result asserts a negative. Only an applicable negative rule and satisfying case basis can supply a negative result. When the supply occurrence obtains but an endpoint binding is missing, keep the positive occurrence and name the missing binding as a separate E.18.NET selection blocker. A missing member, applied constraint, or coffee-service use frame is also a separate selection blocker.

#### E.18.NET:5.2 - Project system-of-interest and recursive build-the-builder

For one project question, practitioners ask which independently identified flow structures must be considered together to connect production and later operation of the project system-of-interest, and which builder branches must also be visible. The actual project remains composite `U.Work`; the selected network is a non-agentive `U.Structure`. Project designation and `U.System` identity remain separate from any local system-role kind, classification, assignment, selection Work, or result episteme. None follows from a project or network label.

For the compiler-and-application use, identify five TFS values by the questions they answer:

1. `CompilerEditionPreparationTFS`, whose loci bind compiler-edition preparation and the obtaining source-use occurrences needed by the build;
2. `BootstrapCompilerBuildTFS`, whose loci bind Work on pre-existing build substrates and the separately grounded production and identity-inception claims for one bootstrap compiler;
3. `ApplicationBuildTFS`, whose loci bind application-production Work and the exact use of that admitted compiler;
4. `ReleaseAssuranceTFS`, selected for release-assurance questions; and
5. `DeploymentOperationTFS`, selected for deployment and operation after the application system exists.

These names designate independently identified TFS values, not lifecycle kinds. They assert no transformation of a not-yet-existing compiler or application. Use E.18 for each TFS, A.15.1 for any current Work occurrence, A.3.4 for a change of a continuing referent, A.15.PROD for production or identity inception, and the applicable relation pattern for each exact cross-member occurrence.

Select the nested network values from those already established inputs:

| Selected network | Direct members | Exact selected cross-member occurrence and ordered endpoint binding | Network use frame |
|---|---|---|---|
| `CompilerRealizationNetwork` | `CompilerEditionPreparationTFS`; `BootstrapCompilerBuildTFS` | `CompilerEditionSourceUsedByBootstrapBuild-1`: `CompilerSourceEditionReady` -> `BootstrapCompilerBuildInput` | connect the admitted source edition to the bootstrap-compiler build question |
| `ApplicationCompilerUseNetwork` | `CompilerRealizationNetwork`; `ApplicationBuildTFS` | `BootstrapCompilerUsedByApplicationBuild-1`: exposed `ExecutableCompilerResult` -> `ApplicationCompilerUsePosition` | connect the admitted compiler to the application-build question |
| `ReleaseAssuranceNetwork` | `ApplicationCompilerUseNetwork`; `ReleaseAssuranceTFS` | `ApplicationBuildEvaluatedForRelease-1`: exposed `ApplicationBuildResult` -> `ReleaseEvaluationSubject` | connect the application result to the release-assurance question |
| `DeliveryOperationNetwork` | `ReleaseAssuranceNetwork`; `DeploymentOperationTFS` | `ReleasedApplicationUsedByDeployment-1`: exposed `ReleasedApplicationPosition` -> `DeploymentApplicationInput` | connect the released application to the deployment-and-operation question |

Each named occurrence is independently established under its project predicate before selection. Each network applies its exact endpoint-binding and boundary-exposure constraints plus the acyclic direct-member constraint, and each keeps the use frame in its row. The local names select or add nothing by themselves.

No claim about who selected these networks is required. If the case also needs `CompilerNetworkSelectionWork-5`, cite each precise performer's independently established A.13 core and the Work's independent A.15.1 admission. Add F.6 only if the case also needs exact assignment-bound attribution; its assignment declaration and proof remain outside E.18.NET. Adding or removing the Work or attribution claim changes none of the four network identities above. The result episteme may describe the selected structures and cite a separate selection or decision relation, but it is not a decision or accountability relation by form. Any accountability claim needs its own exact predicate and participants.

A compiler-production case can close on separately grounded identity inception, production completion or readiness, evidence, and decision while naming the application-build position as the downstream use outside that closed case. Project-level reasoning continues into the member where the compiler later participates. The same joint-selection question recurs for a builder system: select the TFS in which that admitted builder performs exact Work together with the independently identified TFS or nested network concerning production and identity inception of the builder, or its later change after it exists. Shared identity creates no edge; use obtaining production, inception, participation, application, use, or other relation occurrences and their endpoint bindings.

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

Before these identities and relations are grounded, A.1.STM may show the dependency only as a Plain provisional long-mantra map and must name the missing member, the exact relation-claim result returned by its governing pattern, or the separate missing occurrence, endpoint, or position binding. It is not yet an E.18.NET selection. Once the network is admitted, a separate A.22.CGUS demonstrative slice may traverse admitted positions and relation-reference epistemes; it remains a demonstration, not the project, network, case, or Work order.

#### E.18.NET:5.3 - N-ary relation and feedback cycle

A manufacturing release relation has three participants defined by one admitted domain relation pattern: one product-definition position in a TFS selected to answer the development question, one equipment-readiness position in a TFS selected to follow the changes that establish equipment readiness, and one release-condition position in a TFS selected for assurance. Its network row keeps the three participants and their order. It is not replaced by three unlabeled arrows.

Later, an exact use-observation relation connects a position in a TFS selected for operation or use back to a position in a TFS selected to answer the development question. The relation occurrences form a feedback cycle, while the selected direct-member nesting remains acyclic. The feedback does not make the operation-or-use TFS a member of itself and does not turn observation into development Work.

#### E.18.NET:5.4 - Architecture and two demonstrative boundaries

For one containing holon, a current `ArchitectureOf@Context` claim may select the network among its structures. If the selected members belong to separately named holons and no containing bearer is grounded, record the use as inter-holon and name the participating architecture claims. Do not invent one system merely to fill the architecture field.

A Plain A.1.STM long-mantra map may display proposed members and a missing cross-member link before network admission. It names the intended final result and the absent member, relation kind or predicate, predicate result, occurrence, or endpoint binding; it asserts neither an E.18.NET structure nor a CGUS.

After the network is admitted, a separate teaching mantra may show one finite admitted dependency slice. The slice uses the network locator family, cites admitted positions and exact relation-reference epistemes, and keeps omissions and return visible. It does not prescribe project Work order, make the path the whole network, or turn a leaf-local `DesignRunTag` into a project phase.

