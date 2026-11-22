---
chunk_kind: "child"
pattern_id: "E.18.NET"
pattern_title: "Network of Transformation-Flow Structures"
section_id: "E.18.NET:5"
section_title: "Archetypal Grounding — worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.NET/E.18.NET__006_archetypal-grounding-worked-cases.md"
commit_sha: "a9845e2c1029313e518c91a459ff7fab39e2831e"
heading_path:
  - "E.18.NET — Network of Transformation-Flow Structures"
  - "E.18.NET:5 — Archetypal Grounding — worked cases"
line_start: 120489
line_end: 120602
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
keywords:
---

### E.18.NET:5 - Archetypal Grounding — worked cases

#### E.18.NET:5.1 - Same surface vocabulary, different ontic answers

**Several valuations of one TFS.** A cooling-loop review compares nominal-load and emergency-load valuations of the same cooling-loop `TransformationFlowStructure`. Both valuations retain the same A.22 selection O/R/C/F and use the E.18 connection/cut domain under their declared regimes. A counterfactual load value, path slice or local use tag may differ while those discriminators remain unchanged.

Replacing an actual run, applied selection constraint or selected occurrence first reopens the TFS identity. E.18.NET is not used.

**Internal coffee subflow.** A coffee-brewing TFS exposes a preparation portion containing grinding, dosing, and wetting positions plus their selected parent-internal relation occurrences with all participants retained. Its entry and exit remain positions of the brewing TFS. The practitioner uses E.18's `SubflowRef`; no second TFS or network is created.

**Independent network.** A roastery-production TFS and a café-brewing TFS concern different objects and have separate Work occurrences, valuation boundaries and architecture change cadence. The supply predicate and the dispatch and acceptance facts establish that lot 24 reached the café's accepted-stock position. For today's brewing decision the café also needs enough of this lot available and eligible at the time of use.

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
  admissibleUse: trace the accepted lot through the supply relation and check its present available quantity and release conditions for the intended batch
  stopOrReturnCondition: stop when the required quantity is eligible and available at brewing time, or when an established condition rules out this lot. Revisit any missing fact that can change the choice.
returnCondition: either member, the supply occurrence, an endpoint or exposure, acyclicity, or the coffee-service question changes
```

The dispatch and acceptance records suffice to trace what the café received. Suppose its current records show 4 kg of lot 24 still on hand and uncommitted, cleared for brewing at 10:00. The café can choose it for a 3 kg batch then. If 3 kg has since been reserved for another order, only 1 kg remains available for this batch. A recall can close the choice even with all 4 kg present. With only the acceptance receipt, report the completed delivery and recover the needed current condition. Create a `TransformationFlowStructureNetworkRecord@Context` only when the network description must survive the current work.

If the supply claim has no admitted relation kind or applicable predicate, carry the governing pattern's `missing-governor` result. If required facts are unavailable, carry `missing-information`; if a sufficient case basis fails the positive test, carry `factually unsupported`. Neither missing information nor a failed positive test asserts a negative. Only an applicable negative rule and satisfying case basis can supply a negative result.

When the supply occurrence obtains but an endpoint binding is missing, keep the positive occurrence and name the missing binding as a separate E.18.NET selection blocker. A missing member, applied constraint, or coffee-service use frame is also a separate selection blocker.

#### E.18.NET:5.2 - Project system-of-interest and recursive build-the-builder

For one project question, practitioners ask which independently identified flow structures must be considered together to connect production and later operation of the project system-of-interest, and which builder branches must also be visible. The actual project remains composite `U.Work`; the selected network is a non-agentive `U.Structure`.

Project designation and `U.System` identity remain separate from any local system-role kind, classification, assignment, selection Work, or result episteme. None follows from a project or network label.

For the compiler-and-application use, identify five TFS values by the questions they answer:

1. `CompilerEditionPreparationTFS`, whose loci bind compiler-edition preparation and the obtaining source-use occurrences needed by the build;
2. `BootstrapCompilerBuildTFS`, whose loci bind Work on pre-existing build substrates and the separately grounded production and identity-inception claims for one bootstrap compiler;
3. `ApplicationBuildTFS`, whose loci bind application-production Work and the use of that admitted compiler in the application build;
4. `ReleaseAssuranceTFS`, selected for release-assurance questions; and
5. `DeploymentOperationTFS`, selected for deployment and operation after the application system exists.

These names designate independently identified TFS values, not lifecycle kinds. They assert no transformation of a not-yet-existing compiler or application. Use E.18 for each TFS, A.15.1 for any current Work occurrence, A.3.4 for a change of a continuing referent, A.15.PROD for production or identity inception, and the applicable relation pattern for each cross-member occurrence used here.

The compiler-producing contribution of `BootstrapCompilerBuildTFS` and the application-producing contribution of `ApplicationBuildTFS` occupy different functional layers in this build-the-builder account. Their connection runs through the produced compiler and its participation in application-building Work.

The nested networks below instead group members for successively broader questions. Their four depths are not four functional layers or four levels of a modular structure.

Select the nested network values from those already established inputs:

| Selected network | Direct members | Exact selected cross-member occurrence and ordered endpoint binding | Network use frame |
|---|---|---|---|
| `CompilerRealizationNetwork` | `CompilerEditionPreparationTFS`; `BootstrapCompilerBuildTFS` | `CompilerEditionSourceUsedByBootstrapBuild-1`: `CompilerSourceEditionReady` -> `BootstrapCompilerBuildInput` | connect the admitted source edition to the bootstrap-compiler build question |
| `ApplicationCompilerUseNetwork` | `CompilerRealizationNetwork`; `ApplicationBuildTFS` | `BootstrapCompilerUsedByApplicationBuild-1`: exposed `ExecutableCompilerResult` -> `ApplicationCompilerUsePosition` | connect the admitted compiler to the application-build question |
| `ReleaseAssuranceNetwork` | `ApplicationCompilerUseNetwork`; `ReleaseAssuranceTFS` | `ApplicationBuildEvaluatedForRelease-1`: exposed `ApplicationBuildResult` -> `ReleaseEvaluationSubject` | connect the application result to the release-assurance question |
| `DeliveryOperationNetwork` | `ReleaseAssuranceNetwork`; `DeploymentOperationTFS` | `ReleasedApplicationUsedByDeployment-1`: exposed `ReleasedApplicationPosition` -> `DeploymentApplicationInput` | connect the released application to the deployment-and-operation question |

Each named occurrence is independently established under its project predicate before selection. Each network applies its endpoint-binding and boundary-exposure constraints plus the acyclic direct-member constraint, and each keeps the use frame in its row. The local names select or add nothing by themselves.

No claim about who selected these networks is required. If the case also needs `CompilerNetworkSelectionWork-5`, cite each precise performer's independently established A.13 core and the Work's independent A.15.1 admission. Add F.6 only if the case also needs attribution under the assignment in question; its assignment declaration and proof remain outside E.18.NET. Adding or removing the Work or attribution claim changes none of the four network identities above.

The result episteme may describe the selected structures and cite a separate selection or decision relation, but it is not a decision or accountability relation by form. Any accountability claim needs the predicate and participants of that accountability relation.

A compiler-production case can close on separately grounded identity inception, production completion or readiness, evidence, and decision while naming the application-build position as the downstream use outside that closed case. Project-level reasoning continues into the member where the compiler later participates.

The same joint-selection question recurs for a builder system: select the TFS in which that admitted builder performs the Work at issue together with the independently identified TFS or nested network concerning production and identity inception of the builder, or its later change after it exists.

Shared identity creates no edge; use obtaining production, inception, participation, application, use, or other relation occurrences and their endpoint bindings.

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

Each path entry is a direct member of the preceding network, the final entry is the TFS named by `leafFlowPositionRef`, and no network repeats. `FlowValuation`, path slices, and `DesignRunTag` remain leaf-local. “Builds”, “uses”, “evaluates”, and “delivers” are ordinary cues until each link resolves to an admitted relation kind, complete participant meanings and order, obtaining occurrence, and endpoint bindings.

Before these identities and relations are grounded, A.1.STM may show the dependency only as a Plain provisional long-mantra map and must name the missing member, the exact relation-claim result returned by its governing pattern, or the separate missing occurrence, endpoint, or position binding. It is not yet an E.18.NET selection.

Once the network is admitted, a separate A.22.CGUS demonstrative slice may traverse admitted positions and relation-reference epistemes; it remains a demonstration, not the project, network, case, or Work order.

#### E.18.NET:5.3 - N-ary relation and feedback cycle

A manufacturing release relation has three participants defined by one admitted domain relation pattern: one product-definition position in a TFS selected to answer the development question, one equipment-readiness position in a TFS selected to follow the changes that establish equipment readiness, and one release-condition position in a TFS selected for assurance. Keep the three participants in predicate order in one network row. Three unlabeled arrows would lose the ternary relation.

Later, an observation from use reaches a development position. If admitted cross-member relations also lead from that position to the operating position, these connections form a directed cycle. To establish operating feedback, trace the observation into a subsequent development decision that governs operation. For example, the engineer used the reported failure rate to retain the current setting under the applicable rule. A rate merely stored in a log establishes receipt or storage. The network can retain its directed cycle while the decision follows an independent schedule. Direct-member nesting remains acyclic.

#### E.18.NET:5.4 - Architecture and two demonstrative boundaries

For one containing holon, an independently obtaining C.30 `ArchitectureRelation` may have the exact network as its selected structure. A bounded C.30 claim Q about one named holon H and the independently selected network N may instead remain negative, unresolved or candidate/expected under C.30.TFS-REL's single-holon claim branch; retain Q's basis and next return.

If the selected members belong to separately named holons and no containing bearer is grounded, use the inter-holon branch and name the participating architecture claims. None of these architecture uses supplies a missing network discriminator.

A Plain A.1.STM long-mantra map may display proposed members and a missing cross-member link before network admission. It names the intended final result and the absent member, relation kind or predicate, predicate result, occurrence, or endpoint binding; it asserts neither an E.18.NET structure nor a CGUS.

After the network is admitted, a separate teaching mantra may show one finite admitted dependency slice. The slice uses the network locator family, cites admitted positions and exact relation-reference epistemes, and keeps omissions and return visible. It does not prescribe project Work order, make the path the whole network, or turn a leaf-local `DesignRunTag` into a project phase.

