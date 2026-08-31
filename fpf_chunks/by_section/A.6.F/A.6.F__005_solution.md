---
chunk_kind: "child"
pattern_id: "A.6.F"
pattern_title: "Function and Functional Precision Restoration (RPR-FUNCTION)"
section_id: "A.6.F:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.F/A.6.F__005_solution.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "A.6.F — Function and Functional Precision Restoration (RPR-FUNCTION)"
  - "A.6.F:4 — Solution"
line_start: 18409
line_end: 18671
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.17"
  - "A.18"
  - "A.2"
  - "A.20"
  - "A.21"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.0"
  - "A.6.5"
  - "A.6.9"
  - "A.6.B"
  - "A.6.C"
  - "A.6.M"
  - "A.6.P"
  - "A.6.REL"
  - "A.6.RSIR"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.Q"
  - "C.2.1"
  - "C.2.P"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.10.ARCH"
  - "E.18"
  - "E.24.PUB"
  - "E.8"
  - "F.18"
  - "G.6"
keywords:
  - "FunctionalStructure"
  - "actual transformation"
  - "capability"
  - "episteme/publication boundary"
  - "function wording"
  - "functional architecture"
  - "mathematical function"
  - "method-description membership"
  - "module allocation"
  - "required behavior or effect"
  - "work"
---

### A.6.F:4 - Solution

A.6.F is an A.6.P RPR specialization for function-like wording. It does not mint `U.Function`. It assigns the use under repair to an exact entity, value, claim, or claim-bearing episteme and its subject pattern, then stops unless another claim remains current. It does not package direct relations, declaration-local `SlotSpec`s, assertions, specifications, views, and representation elements as peer records.

#### A.6.F:4.1 - Trigger rule

A.6.F applies when function-like wording may carry one or more of these independently established readings. The list is a recognition and dispatch palette, not a `U.*` kind, claim kind, relation kind, or admission result:

The familiar estimate of roughly seven meanings is only a recall cue, not a fixed count. Several entries below unfold into different objects, claims, and relations, function wording often transfers metonymically among them, and one occurrence may carry more than one reading. Recover what the sentence actually says rather than assigning it to a numbered meaning.

- architecture or functional architecture;
- capability, effect, externally promised behavior, or user-visible functionality;
- method wording, work occurrence, or work result;
- a system-role kind or assignment, participation, actual functioning, or responsibility;
- mathematical function, mapping, relation, loss, objective, or value functional;
- quality, fitness, characteristic, score, or proxy wording;
- module allocation, interface, signature, port, API, protocol, flow, or mechanism relation;
- another independently established claim named by value, such as evidence, assurance, gate, decision, or release.

If none of those readings carries a current FPF claim, the wording may remain ordinary Plain prose.

#### A.6.F:4.2 - FunctionUseRepair

`FunctionUseRepair` is a pattern-local repair note. Its `functionLikeReadingUnderRepair` value only helps a reader recognize and dispatch a possible reading; neither that value nor the three scan groups below is a `U.*` kind, claim kind, relation kind, or admission result. The recovered result belongs in `exactGovernedObjectOrClaim` under its subject pattern. The note carries no project-publication, evidence, decision, or `U.Function` authority. `FunctionalStructure` is an `ArchitectureStructureKindRef` value under C.30.ASV, not a kernel Function kind.

```text
FunctionUseRepair ::= {

  phrase,
  functionLikeReadingUnderRepair: {
    directObjectOrValueReading?:
      holonCapability |
      methodDescription |
      mechanismRealization |
      workPlan |
      workOccurrence |
      workResult |
      mathematicalFunction,

    claimOrConditionReading?:
      requiredTransformation |
      requiredEffect |
      inputCondition |
      outputCondition |
      systemRoleKindOrAssignmentCue |
      participationOrFunctioningCue |
      responsibilityCue |
      qualityExpression |
      characteristicExpression |
      functionalArchitecture |
      evidenceClaim |
      assuranceClaim |
      gateClaim |
      decisionClaim |
      publicationClaim,

    relationParticipantOrLocusReading?:
      functionalElementLocus |
      transformerSideFiller |
      candidateBearer |
      functionalPort |
      methodPosition |
      mathematicalRelation |
      moduleAllocation |
      interfaceRelation |
      signatureRelation,

    otherDeclared?
  },
  exactGovernedObjectOrClaim: oneOrMoreOf {
    exactEntityOrValueRef?,
    exactClaimOrClaimContent?,
    exactClaimBearingEpistemeRef?
  },

  directRelationPredicateUse?: {
    admittedDirectRelationKindRef,
    relationKindToken?,
    semanticPredicate,
    actualParticipantRefs,
    directRelationPatternRef
  },

  relationalAssertionUse?: {
    relationalAssertionEpistemeRef,
    assertedClaimContent,
    assertedSemanticPredicate,
    polarityOrModality,
    actualParticipantRefs,
    directRelationPatternRef
  },

  obtainingRelationOccurrenceUse?: {
    individuatedRelationOccurrenceRef,
    obtainingSemanticPredicate,
    actualParticipantRefs,
    occurrenceIdentityRuleRef,
    directRelationPatternRef
  },

  reusableDeclarationUse?: {
    relationSignatureRef,
    declarationLocalSlotSpecRefs
  },

  selectedClaimBearingEpistemeUse?: {
    assertionSpecificationOrViewEpistemeRef,
    selectedClaimOrDesignation
  },

  representationUse?: {
    representationElementRefs,
    explicitC29Correspondence,
    representedObjectOrClaimRef
  },

  sourceCueText?,
  subjectPatternApplicationRefs?,
  blockedLocalOverreadRefs,
  admissibleUse,
  nonAdmissibleUse,
  nextAdmissibleUse,
  stopCondition
}
```
The repair is complete when a practitioner can name the exact object or claim, apply its subject pattern, and state the remaining action. At least one exact entity or value, claim or claim content, or claim-bearing episteme is required in `exactGovernedObjectOrClaim`. A source cue stays in `sourceCueText`; it is not a recovered value. When a direct relation is current, first name its admitted kind, semantic predicate, and actual participants in `directRelationPredicateUse`. Add `relationalAssertionUse` only when one exact `C.2.1` episteme affirms, denies, or otherwise modalizes that predicate. Add `obtainingRelationOccurrenceUse` only when the receiving use needs one separately individuated obtaining occurrence under the subject pattern's identity rule, applied through `A.6.REL`; a predicate or assertion never supplies occurrence identity. Add a reusable `RelationSignature` and declaration-local `SlotSpec`s only for reusable typed use; add another selected assertion, specification, or view episteme only when it is a separate claim-bearing object; add a C.29 representation element and explicit correspondence only when representation matters. If the text still hides a function, capability, work, method, system-role kind or assignment, participation, functioning, responsibility, module, evidence, gate, or mathematical-function collapse, the repair is incomplete.

#### A.6.F:4.3 - Repair assignments

When a function-like phrase is claim-bearing, recover the exact object or claim under concern before lowering or rewriting the phrase. C.30.ASV does not define a world-side or view-local `FunctionalElement` individual. Its `FunctionalStructureView` is the same `ArchitectureStructuralView` episteme about one selected functional `U.Structure`; a `FunctionalStructureViewUse` may cite exact `FunctionalElementClaim` epistemes and other values needed by the use. Required or desired effects, actual transformations, candidate bearers, capabilities, ports, allocations, and correspondences remain separately established claims or values. If a distinct functional-element individual is genuinely needed, first define its predicate and identity in a subject pattern; otherwise stop at the smaller exact requirement, behavior or effect claim, capability, participant, condition, port declaration, or other directly defined object. A field name or source cue is not a substitute for that object.

**Method-description guard.** A procedure, code file, solver model, recipe, protocol, or algorithm is only a clue. First identify the knowledge object and the exact method it is about. Then point to at least one claim that says how that method is done, such as its transformation or enactment concern, applicability, precondition, intended effect or preserved condition, bound, generic participant meaning, or internal method composition. Only then classify that already identified `U.Episteme` as `U.MethodDescription` under A.3.2. A title, author, citation, approval, file form, or runnable artifact alone is a near-miss. If no admitted `U.Method` is its exact `EntityOfConcern`, or no way-of-doing claim is present, do not use `U.MethodDescription`: keep the actual plan, work, result, formal substrate, mechanism declaration, representation, publication occurrence or form, or carrier with its subject pattern. A different code, text, diagram, or publication form does not decide membership. If claim content, exact method, or effective reference scheme changes, C.2.1 first identifies the resulting episteme; then apply A.3.2 to that individual.

| Function wording use | Recovered object or claim and subject pattern | Boundary |
| --- | --- | --- |
| required or desired functional behavior, transformation, or effect | Keep the requirement or other claim about the required or desired behavior or effect with its exact requirement, architecture, capability-gap, functional-view, method, or other claim-bearing pattern. Use `U.Transformation` only for one independently grounded actual bounded change under A.3.4. Use `TransformationFlowStructure` only for an independently selected structure over explicitly named loci, not for the required effect itself. | Requirement wording establishes neither an occurrence nor a filled `FunctionalElementClaim`. Stop at the claim pattern unless the changed referent, boundary, conditions, actual before/during/after facts, and continuity or reidentification rule are grounded. A functional view may cite the required claim, selected structure, bearer candidate, capability, and allocation without saying that the change occurred. |
| functional element in a view | Under C.30.ASV, use one `ArchitectureStructuralView` episteme whose `EntityOfConcern` is one selected functional `U.Structure`. When needed, add a `FunctionalStructureViewUse` that cites exact C.2.1 `FunctionalElementClaim` epistemes and only separately established behavior or effect, bearer, capability, port, allocation, or correspondence values. | This is a claim-and-view interface, not a `FunctionalElement` individual, loose table row, or module. If no bearer or candidate allocation is current, keep the requirement, required-behavior claim, required-effect claim, capability gap, functional-behavior slot, or candidate-allocation question with its subject pattern. |
| transformer-side filler and candidate bearer | For a design-only candidate, keep the candidate transformer-side system locus or candidate `U.System` reference without asserting an assignment or performed Work. If the local kind `TransformerSystemRole` is current, name that kind; add a separate judgment classifying a System under it only when that judgment obtains. If an assignment is independently current, recover its directly declared species and its obtaining occurrence with actual participant values, holder, applicability, and extent under A.2.1. If performed Work is independently current, point to its basis: A.13 first, independent A.15.1 Work admission second, and F.6 afterward only for precise assignment-bound attribution. Coordinate the selected locus with `A.3.4 TransformerRef?`, `A.7`, `A.15`, `A.15.1`, and `A.15.2` only for the claims that are actually current. | A `FunctionalElementClaim` may cite an independently established candidate-bearer locus, but that citation is not the whole transformer ontology. A kind, classification judgment, assignment species, assignment occurrence, and dated Work are independent facts; none manufactures another. |
| input condition, output condition, and functional ports | `A.3.4 InputConditionRefs?`, `OutputConditionRefs?`, and `FunctionalPortRefs?`; `U.Signature` discipline through `A.6.0` and `A.6.5` when accepted or produced states, media, flows, signals, information, work products, formal objects, or functional port signatures matter | A functional port is not automatically a module interface. Use A.6.M only when module-interface or substitution compatibility is the claim. |
| capability of a holon | the exact `U.Capability` value or capability claim under its subject pattern | Does not imply that a method, module, work occurrence, or successful transformation exists. |
| method or algorithm wording | `U.Method` only when the claim concerns a reusable semantic way of doing; `U.MethodDescription` only for an already identified `U.Episteme` that passes the A.3.2 guard above: one admitted `U.Method` is its exact `EntityOfConcern` and at least one claim says how that method is done | Procedure, code, solver, recipe, protocol, and algorithm forms are clues only; they establish neither membership, execution, nor evidence. |
| mechanism wording | `U.Mechanism` through `A.6.1` and `E.20` when a law-governed realization or operation structure is the claim | Does not become a method, Work occurrence, capability, selected functional structure, or functional-view claim by label. |
| work plan, work occurrence, or work result | Recover the exact `U.WorkPlan` under `A.15.2`, one exact dated `W : U.Work` under `A.15.1`, or the separately identified result entity or episteme together with the predicate that relates it to the current Work or application. Use `A.15.PROD` when production, entity inception, or production completion is current, and `A.6.RCD` only when the needed direct result relation has no current governor. | A plan, Work occurrence, and result are different objects. None implies reusable function ontology or completed functioning, and a result is not part of Work identity. |
| system-role or responsibility wording | `VP.AllocationResponsibility` is only a recognition cue. A positive responsibility claim names an admitted domain responsibility predicate, its actual participants, applicability, and occurrence identity; otherwise return the exact `A.6.RCD` missing governor. If an assignment claim is also current, recover its directly declared species and obtaining occurrence under A.2.1. If performed Work is current, point to its basis: A.13 first, independent A.15.1 Work admission second, and F.6 afterward only for precise assignment-bound attribution. | A system-role kind, classification judgment, assignment, function phrase, commitment, position, authority label, or Work attribution establishes no responsibility relation by form. Responsibility may obtain with or without a commitment, and each relation keeps its own predicate and identity. |
| participation or actual functioning | Name the direct domain predicate, actual participants, applicability, and occurrence identity for the claimed participation or functioning. If the corpus has no such predicate for the receiving use, return the exact `A.6.RCD` missing governor. | Assignment, capability, allocation, nearby Work, or a function label does not make participation or actual functioning obtain. |
| mathematical function or relation | C.29 mathematical-lens use with domain, codomain or relation domain, preserved and lost structure, lens-use admissibility value, and stop condition | Does not become architecture, evidence, causal proof, assurance, or decision claim by itself. |
| quality or fitness expression | `C.25`, `C.16`, `C.16.Q`, `A.17`, `A.18`, or an admitted characteristic or measurement subject pattern according to the claim being made | Does not let "functionality" carry a quality claim without bearer and subject pattern. |
| module allocation | Recover the exact allocation or correspondence claim or relation under its subject pattern. When a functional view cites it, use `FunctionalStructureViewUse` with its `ArchitectureStructuralView` and the exact claim or relation reference; use `A.6.M` when a module-interface claim is being made. | Does not make function and module one FPF kind. One selected functional structure may have allocation claims involving several modules, one module may occur in claims about several functional structures, and a module may have no current functional-view claim. |
| interface relation, module-interface relation, or signature relation | Use `A.6.RSIR` first when bare interface, API, port, protocol, or service-access wording could point to several direct EoCs; then use `A.6.M` for the module-interface boundary and `A.6.0` and `A.6.5` for signature discipline, with `A.6.B`, `A.6.C`, or `A.6.P:4.11a` only when that boundary, interface condition, API, protocol, service, promise, or duty claim is being made | Does not turn a functional link, port label, API name, or signature into implemented compatibility. |
| evidence, result, assurance, gate, decision, or publication claim | the direct evidence, result, assurance, gate, decision, publication, or source pattern named by value | Function wording can point to these claims, but it does not authorize or prove them by itself. |
| functional architecture | `ArchitectureOf@Context` whose `structureKindRefs` includes `FunctionalStructure`, one selected functional `U.Structure`, and the `ArchitectureStructuralView` episteme about that structure. Use `FunctionalStructureViewUse` only when citations to exact `FunctionalElementClaim` epistemes or other separately established values change action. | Not a peer architecture ontology, functional-element individual, selected transformation-flow structure, or mathematical graph description by itself. |

**Required-versus-actual check.** “The cooling loop shall reduce outlet temperature by 8 °C within 60 seconds” remains a requirement or functional-view claim; by itself it identifies no `U.Transformation`. If a later run actually changes the loop state, identify that cooling occurrence separately under A.3.4 from the changed loop, exact boundary and conditions, actual before/during/after facts, and continuity or reidentification rule. Requirement-only material is the countercase and stop: it cannot admit an actual transformation, observed functioning, or evidence of success.

#### A.6.F:4.4 - Functional architecture boundary

Functional architecture is the `FunctionalStructure` case of `ArchitectureOf@Context`: the declared organization used to relate one selected functional structure to independently established claims about required behavior or effects, capabilities, functional dependencies, and constraints that a holon is to realize, before or alongside allocation to modules, local system-role kinds or assignments, work, evidence, control relations, selected transformation-flow structures, or mathematical descriptions of those structures. Under C.30.ASV, the view is an `ArchitectureStructuralView` episteme whose `EntityOfConcern` is that selected structure; it does not define a functional-element individual. A `FunctionalStructureViewUse` may cite exact `FunctionalElementClaim` epistemes and other separately established values needed by the use.

```text
Functional architecture shorthand:
  open the `ArchitectureOf@Context` form in the current C.30 edition;
  name the exact described holon and select one functional `U.Structure`;
  use the `ArchitectureStructuralView` episteme whose `EntityOfConcern` is that structure and whose exact viewpoint conformance obtains;
  add `FunctionalStructureViewUse` only when exact `FunctionalElementClaim` epistemes or other separately established values change action;
  require an independent A.3.4 basis for every actual-transformation reference;
  fill every other C.30 field required by this architecture use.
```
The view keeps requirement, required-behavior/effect, capability, dependency, and constraint claims with their subject patterns; their wording does not turn them into `U.StructureRef` values or actual transformations. An actual-transformation reference is admissible only after A.3.4 independently grounds the occurrence. A selected `TransformationFlowStructure`, path slice, crossing, flow valuation, or mathematical description may be related to functional structure through `C.30.TFS-REL`, `E.18`, or `E.18.2`, but it is neither the required effect nor the functional architecture itself unless the positive selected-structure co-reference check succeeds.

#### A.6.F:4.5 - Function-flow-module alignment note

Use this note when functional wording touches flow or module allocation but does not yet require a full structural view or `A.6.M` module-relation repair.

```text
FunctionFlowModuleAlignmentNote:
required function or effect:
flow path or dependency:
proposed module allocation:
separateNeighborClaims:
known mismatch:
subjectPatternApplicationRefs:
admissible use:
non-admissible use:
```

The note records only the local function-flow-module alignment and boundary. Functional architecture, module relation, implemented-interface, evidence-sufficiency, and architecture-decision claims remain with their subject patterns.

#### A.6.F:4.6 - Common kind and relation separations

| Confusion | Repair |
| --- | --- |
| function = module | Keep `VP.Functional` and `VP.ModuleInterface` distinct; connect them through declared correspondence, allocation, retargeting, or `A.6.M` module-relation repair. |
| function = capability | Capability belongs to a holon. Keep a required or desired behavior/effect as claim content under its requirement, architecture, capability-gap, functional-view, method, or other subject pattern; neither that claim nor the capability establishes an actual transformation. |
| function = work | One `W : U.Work` is a dated world-side occurrence. Its result or output is a separately identified entity or episteme. Connect it only through the subject-specific direct result or production relation that actually obtains, or use one local `A.15.PROD` claim for the current production-work, inception, or completion question. Use `A.6.RCD` only when a needed relation has no current governor. Function wording remains design-side or description-side content unless an exact work-facing claim is current. |
| function = method | Method is a reusable way of doing. A method claim may state an intended effect, but that effect is neither the method nor an actual `U.Transformation`; apply A.3.4 only when the actual change occurrence is independently grounded. |
| function = system-role kind, assignment, participation, functioning, or responsibility | Recover only the branch the sentence asserts. A system-role kind is a local `...SystemRole` kind; an assignment is one occurrence and its declared `U.SystemRoleAssignment` species; performed Work uses F.6 separately; participation, functioning, and responsibility each need their domain predicate or an `A.6.RCD` missing governor. |
| mathematical function = holon purpose | Use C.29 for mathematical function or relation; recover domain, codomain or relation domain, preserved and lost structure, lens-use admissibility value, and stop condition. |
| functional diagram = evidence | Diagram is a view or publication; evidence claim uses `A.10` or `G.6`. |
| functionality = quality | Recover the quality bearer and subject pattern through `C.25`, `C.16`, or C.16.Q before using the wording as an adequacy claim. |

#### A.6.F:4.7 - Composability and compositionality

Composability and quality compositionality are separate claims. If the text says parts can be assembled, keep that as a structure or use claim. If it says a quality of the whole follows from parts, assign the quality-composition claim to `C.25` and C.16-backed measurement or quality claim:

```text
Composability:
  exactGovernedObjectOrClaim: the A.6.M `ModuleInterfaceClaim` content for "A and B can be assembled under interface X"
  selectedClaimBearingEpistemeUse: the exact C.2.1 episteme carrying that claim content
  directRelationPredicateUse?: only an exact domain predicate independently admitted for a direct module-allocation or module-interface relation, with its actual participants
  relationalAssertionUse?: the exact C.2.1 episteme that affirms, denies, or modalizes that admitted predicate, only when such a predicate is current
  obtainingRelationOccurrenceUse?: only when that admitted relation has a same-versus-new-occurrence rule and the receiving use must distinguish one obtaining occurrence through A.6.REL
  reusableDeclarationUse?: one compatible RelationSignature and its declaration-local SlotSpecs, only when repeated typed use needs them
  subjectPatternApplicationRefs: A.6.M for `ModuleInterfaceClaim`; C.2.1 for its claim-bearing episteme; A.6.RCD when a reusable direct relation is needed but absent; A.6.REL only after the direct relation is admitted and one obtaining occurrence must be distinguished; A.6.0 and A.6.5 only for the reusable declaration
Quality compositionality:
  exactGovernedObjectOrClaim: the affected Q-Bundle and the exact structural-characteristic, causal-hypothesis, or evidence-relation claim that this use relies on
  directRelationPredicateUse?: the exact predicate defined or tested through C.16, C.16.Q, or A.10 and its actual participants, only when that relation is current
  relationalAssertionUse?: the exact C.2.1 episteme and its affirmative, negative, or modal quality or evidence claim when that assertion is current
  subjectPatternApplicationRefs: C.25; C.16 or C.16.Q; A.10 only when evidence provenance is the claim being made
Non-admissible:
  successful assembly is not quality propagation
```
Compositional formalisms may express explicit composition structures and view or model relations. They do not make safety, latency, reliability, or another quality propagate automatically.

A.6.F defines no separate quality-composition record. Use the claim form supplied by the applicable subject pattern. A composite family uses the exact C.25 Q-Bundle, including its bearer, scope, measures, qualification window, mechanisms or status, and evidence. A single characteristic or measurement follows C.16, with C.16.Q used only when quality wording still needs repair; name its bearer, scope, measure, and claim identity. Keep a causal inference with its causal pattern, and use A.10 only when evidence provenance is the claim being made. If those values cannot be named, keep the quality-composition claim unresolved rather than filling an A.6.F-only schema.

#### A.6.F:4.8 - Worked slices

**Function-like module claim; no direct relation.** A release note says, “The brake-control functional package is in the vehicle-control system.” The head noun is `package`; do not turn the modifier `functional` into `U.Function`. For this use, recover this concrete result:

- `exactGovernedObjectOrClaim`: A.6.M `ModuleInterfaceClaim` content naming `BrakeControllerPackage`, `VehicleControlSystem`, `Release-2026Q2`, `VP.ModuleInterface`, `BrakeControlBoundary`, and an `interfaceSpecificationRef` that resolves `BrakeControlInterfaceSpec-v5`; its direct-relation disposition is `noDirectRelationClaimed`;
- `selectedClaimBearingEpistemeUse`: `BrakeArchitectureNote_v3 : U.Episteme` under C.2.1 carries that content and has `BrakeControllerPackage` as its exact `EntityOfConcern`;
- `directRelationPredicateUse`, `relationalAssertionUse`, and `obtainingRelationOccurrenceUse`: `not used`, because no domain rule has admitted a direct module relation predicate or an obtaining occurrence for this case;
- remaining action: apply A.6.M to the declared interface and admissibility conditions; do not infer a function allocation, direct relation, or implemented compatibility from the source phrase.

**Interrupted assignment; occurrence identity needed.** A maintenance log says, “Robot-7 resumed its inspection function after a documented period with no inspection assignment.” Treat `function` as a cue. Recover `InspectorSystemRole` and one declared direct species `CellInspectorAssignment <: U.SystemRoleAssignment`; then test its direct predicate for `Robot-7 : U.System` and the species-specific cell and interval participants. Keep `Robot7AssignmentLog_42` as the separate C.2.1 episteme that states the interval facts. A.2.1 says that the demonstrated non-assignment period ends the first assignment occurrence and the later resumption begins another. When the maintenance history must distinguish them, apply A.6.REL with that identity rule to keep `InspectorAssignment_PreGap` and `InspectorAssignment_PostGap` distinct. A taxonomy or scheme is not an assignment participant, and neither assignment implies inspection Work.

**Neighbor claims that need their own relation.**

- `TestArticle-7 participates passively in TestWork-9 during TestInterval-9` is not established by `TestArticleSystemRole` or `TestArticleAssignment-7`. Until a direct passive-test-participation predicate supplies participant order and identity, return `A.6.RCD missing-governor[direct passive-test-participation relation]`; the tester's Work and F.6 attribution remain usable.
- `Motor-M1 drives PumpAssembly-A during PumpRun-17` needs a direct motor-drive-functioning predicate. Assignment, torque capability, and pumping Work remain separate; without that predicate return `A.6.RCD missing-governor[direct motor-drive-functioning relation]`.
- `Hammer-3 supports PaperStack-9 during Interval-P` needs a direct artifact-support predicate. Do not replace that exact claim with an interchangeable list of use, load, support, or function kinds; without the predicate return `A.6.RCD missing-governor[direct artifact-support relation]`.

**Functional architecture phrase.** A team says, "the functional architecture is the user journey." A.6.F does not let the phrase create a separate architecture kind. The repair is:

```text
FunctionUseRepair:
phrase: "functional architecture"
functionLikeReadingUnderRepair: functionalArchitecture
exactGovernedObjectOrClaim: the `ArchitectureOf@Context` claim record and its one selected functional `U.Structure`
selectedClaimBearingEpistemeUse: the exact `ArchitectureStructuralView` episteme whose `EntityOfConcern` is that structure, plus any exact C.2.1 `FunctionalElementClaim` epistemes cited by the use
subjectPatternApplicationRefs: C.30; C.30.ASV
blockedLocalOverreadRefs: functional-element individual, user journey publication, work log, selected transformation-flow structure, mathematical graph description, module diagram
nextAdmissibleUse: when the view changes action, use `FunctionalStructureViewUse` to cite the view, exact claim epistemes, and only separately established bearer, capability, port, allocation, or correspondence values
stopCondition: ordinary phrasing remains Plain when no architecture claim is made; requirement-only material remains a claim; an actual transformation appears only on an independent A.3.4 basis
```
**Functionality as quality.** A product note says, "new functionality improves adequacy." The repair separates the exact added-capability or required-effect claim from the quality claim. Capability or effect wording may stay as recognition, but the adequacy claim goes to `C.25`, `C.16`, C.16.Q, or the admitted characteristic or measurement pattern that states its bearer and criterion. A.6.F stops once those exact claims and subject patterns are clear; it adds no reusable declaration, view, or representation apparatus unless the receiving use actually needs it.

**Mathematical function or loss.** A model note says, "the loss function explains the holon purpose." The repair keeps the mathematical function under C.29 lens discipline: domain, codomain or relation domain, preserved and lost structure, lens-use admissibility value, and stop condition. The loss may inform a reasoning move; it does not become holon purpose, evidence sufficiency, causal proof, assurance, or project decision by itself.

**Pump-station functional dependency.** A maintenance note says, "the backup pump function is degraded." A.6.F first separates the required effect, the exact `U.Capability` value or capability claim, the physical module allocation, the performed maintenance work, the evidence relation, and the quality claim. The functional wording may open a `FunctionalStructure` view under C.30.ASV or go to the capability pattern; it does not by itself prove the pump was tested, authorize operation, or make the backup module compatible with the main line.

**Product-platform allocation.** A hardware team says, "thermal management functionality moved to the chassis." The repair separates required heat-removal effect, module allocation, interface constraints, signature constraints, architecture structural view, and any evidence or gate claim. A.6.F keeps the function-like wording useful for architecture work while sending module-interface and evidence claims to their subject patterns.

