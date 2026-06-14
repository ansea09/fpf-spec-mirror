---
chunk_kind: "child"
pattern_id: "A.6.F"
pattern_title: "Function and Functional Precision Restoration (RPR-FUNCTION)"
section_id: "A.6.F:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.F/A.6.F__005_solution.md"
commit_sha: "7c617d5d0fa1abf94a21bac2dd909f68ed514249"
heading_path:
  - "A.6.F — Function and Functional Precision Restoration (RPR-FUNCTION)"
  - "A.6.F:4 — Solution"
line_start: 14573
line_end: 14801
dependencies:
  - "A.10"
  - "A.15"
  - "A.17"
  - "A.18"
  - "A.2"
  - "A.20"
  - "A.21"
  - "A.6.0"
  - "A.6.5"
  - "A.6.8"
  - "A.6.9"
  - "A.6.B"
  - "A.6.C"
  - "A.6.M"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.Q"
  - "C.2.P"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.10.ARCH"
  - "E.18"
  - "E.8"
  - "F.18"
  - "G.6"
  - "U.Function"
keywords:
  - "FunctionalStructure"
  - "capability/effect"
  - "function wording"
  - "function-use repair"
  - "functional architecture"
  - "mathematical function"
  - "module allocation"
  - "work/method boundary"
---

### A.6.F:4 - Solution

A.6.F is an A.6.P RPR specialization for function-like wording. It does not mint `U.Function`. It assigns the use under repair to an existing FPF kind, relation, claim record, view, or governing-pattern application and stops there unless another claim kind remains current.

#### A.6.F:4.1 - Trigger rule

A.6.F applies when a sentence uses function-like wording to carry one or more current FPF claim kinds:

- architecture or functional architecture;
- capability, effect, externally promised behavior, or user-visible functionality;
- method wording, work occurrence, or work result;
- role expectation or responsibility;
- mathematical function, mapping, relation, loss, objective, or value functional;
- quality, fitness, characteristic, score, or proxy wording;
- module allocation, interface, signature, port, API, protocol, flow, or mechanism relation;
- another FPF claim named by value, such as evidence, assurance, gate, decision, or release.

If none of those claim kinds is current, the wording may remain ordinary Plain prose.

#### A.6.F:4.2 - FunctionUseRepair

`FunctionUseRepair` is a pattern-local repair note. It carries no project-publication, evidence, decision, or `U.Function` authority. `FunctionalStructure` is an `ArchitectureStructureKindRef` value under C.30.ASV, not a kernel Function kind.

```text
FunctionUseRepair ::= {

  phrase,
  claimKindUnderRepair:
    requiredTransformation |
    requiredEffect |
    functionalElementLocus |
    transformerSideFiller |
    candidateBearer |
    inputCondition |
    outputCondition |
    functionalPort |
    holonCapability |
    methodPosition |
    methodDescription |
    mechanismRealization |
    workPlan |
    procedureWording |
    workOccurrence |
    workResult |
    roleExpectation |
    mathematicalFunction |
    mathematicalRelation |
    qualityExpression |
    characteristicExpression |
    moduleAllocation |
    interfaceRelation |
    signatureRelation |
    functionalArchitecture |
    evidenceClaim |
    assuranceClaim |
    gateClaim |
    decisionClaim |
    publicationClaim |
    otherDeclared,
  recoveredValueKindRefs?:
    U.Transformation |
    TransformationFlowStructure |
    U.Capability |
    U.Method |
    U.MethodDescription |
    U.Mechanism |
    U.WorkPlan |
    U.Work |
    MathematicalFunctionUnderC29 |
    otherDeclared,
  recoveredRelationRecordRefs?:
    FunctionalElement@Context |
    ModuleAllocationRelation |
    InterfaceSpecification |
    RoleExpectation |
    otherDeclared,
  recoveredSlotRefs?:
    TransformerRef? |
    CandidateBearerRef? |
    InputConditionRefs? |
    OutputConditionRefs? |
    FunctionalPortRefs? |
    FunctioningRef? |
    QBundleSlot |
    otherDeclared,
  recoveredViewRecordRefs?:
    FunctionalStructureView@Context |
    otherDeclared,
  recoveredFpFReferenceRefs?,

  sourceCueText?,
  directGoverningPatternApplicationRefs?,
  bearerRef?,
  candidateBearerRef?,
  functionalBehaviorRef?,
  blockedLocalOverreadRefs,
  admissibleUse,
  nonAdmissibleUse,
  nextAdmissibleMove,
  stopCondition
}
```
The repair is complete when a practitioner can say which FPF value kind named by value, relation record, slot reference, view record, or direct governing-pattern application the function-like wording uses. A source cue stays in `sourceCueText`; it is not a recovered value. If the text still hides a function, capability, work, method, role, module, evidence, gate, or mathematical-function collapse, the repair is incomplete.

#### A.6.F:4.3 - Repair assignments

When a function-like phrase is claim-bearing, recover the positive object under concern before lowering or rewriting the phrase. FPF treats `FunctionalElement@Context` as a view-local functional-structure record under C.30.ASV when stable identity, bearer, behavior, ports, capability, and allocation obligations are all current; otherwise A.6.F may stop at the smaller recovered value kind, relation record, slot reference, or source cue.

| Function wording use | First FPF kind or receiving locus | Boundary |
| --- | --- | --- |
| required functional behavior, transformation, or effect | `U.Transformation` for one bounded required change or required effect; `TransformationFlowStructure` for compound behavior; `FunctionalElement@Context.functionalBehaviorRef` when a functional element is current | Do not compare the element noun directly with `U.Transformation`. Compare the functional behavior or functioning with transformation, and keep the bearer or view-local locus separate. |
| functional element in a view | `FunctionalElement@Context` inside `FunctionalStructureView@Context` when selected view, bounded context, functional behavior, and bearer or candidate-bearer locus are current | Not `U.Function`, not a loose table row, and not the module by default. If no bearer or candidate allocation is current, keep a required transformation, effect, capability gap, or behavior slot rather than claiming a full functional element. |
| transformer-side filler and candidate bearer | `U.System` bearing `TransformerRole@Context` for a transformer-side filler; candidate system reference for an allocation candidate; coordinated with `A.3.4 TransformerRef?`, `A.7`, `A.15`, `A.15.1`, and `A.15.2` when role, work, responsibility, or enactment claims are current | A functional element may recover one of these loci, but it is not the whole transformer ontology. Old device cues and old transformer-bearer cues map here, not to a new durable transformer kind. |
| input condition, output condition, and functional ports | `A.3.4 InputConditionRefs?`, `OutputConditionRefs?`, and `FunctionalPortRefs?`; `U.Signature` discipline through `A.6.0` and `A.6.5` when accepted or produced states, media, flows, signals, information, work products, formal objects, or functional port signatures matter | A functional port is not automatically a module interface. Use A.6.M only when module-interface or substitution compatibility is the claim. |
| capability of a holon | `U.Capability` or the capability-governing pattern or project record named by the claim being made | Does not imply that a method, module, work occurrence, or successful transformation exists. |
| method or algorithm wording | `U.Method` when the source says the semantic way of doing under conditions; `U.MethodDescription` when it is an authored procedure, code, solver, recipe, protocol, or algorithm text | Does not imply execution or evidence. Algorithm wording is a source cue; recover the current kind rather than treating it as software-only. |
| mechanism wording | `U.Mechanism` through `A.6.1` and `E.20` when a law-governed realization or operation structure is the claim | Does not become method, work, capability, or functional element by label. |
| work plan, work occurrence, or work result | `U.WorkPlan`, `U.Work`, Work record, or P2W carry-through relation under `A.15`, `A.15.2`, `A.15.1`, and `E.18.1` according to the asserted claim | Does not imply reusable function ontology or completed functioning. |
| responsibility or role expectation | `VP.RoleEnactor` and the relevant role and enactor relation, with `U.RoleAssignment` when a role assignment claim is current | Does not imply the role-holder performed the work or that the bearer has the capability. |
| mathematical function or relation | C.29 mathematical-lens use with domain, codomain or relation domain, preserved and lost structure, lens-use admissibility value, and stop condition | Does not become architecture, evidence, causal proof, assurance, or decision claim by itself. |
| quality or fitness expression | `C.25`, `C.16`, `C.16.Q`, `A.17`, `A.18`, or an admitted characteristic or measurement governing pattern according to the claim being made | Does not let "functionality" carry a quality claim without bearer and governing pattern. |
| module allocation | `FunctionalStructureView@Context` plus declared correspondence, allocation, retargeting, or `A.6.M` module-relation repair when a module-interface claim is being made | Does not make function and module one FPF kind; allow one module to realize many functional elements, many modules to realize one functional element, abstract functional elements before allocation, and modules with no current functional behavior in a view. |
| interface relation, module-interface relation, or signature relation | module-interface boundary note governed by `A.6.M` and signature discipline governed by `A.6.5`, with `A.6.0`, A.6.B, A.6.C, or A.6.8 only when that signature claim is being made | Does not turn a functional link, port label, API name, or signature into implemented compatibility. |
| evidence, result, assurance, gate, decision, or publication claim | the direct evidence, result, assurance, gate, decision, publication, or source pattern named by value | Function wording can point to these claims, but it does not authorize or prove them by itself. |
| functional architecture | `ArchitectureOf@Context` with `structureKindRef = FunctionalStructure` and `FunctionalStructureView@Context` under C.30.ASV | Not a peer architecture ontology, selected transformation-flow structure, or mathematical graph description by itself. |

#### A.6.F:4.4 - Functional architecture boundary

Functional architecture is the `FunctionalStructure` case of `ArchitectureOf@Context`: the declared organization of required transformations, capabilities, effects, functional dependencies, and constraints that a holon is to realize, before or alongside allocation to modules, roles, work, evidence, control relations, selected transformation-flow structures, or mathematical descriptions of those structures.

```text
FunctionalArchitecture@Context shorthand expands to:
  ArchitectureOf@Context(
    describedHolonRef,
    boundedContextRef,
    structureKindRefs includes FunctionalStructure,
    structureRefs includes `U.StructureRef` values for required transformations,
      effects, capabilities, dependencies, and constraints,
    admissibleUse,
    nonAdmissibleUse
  )
```

This shorthand is admissible only when the expanded C.30 or C.30.ASV interpretation is recoverable. A selected `TransformationFlowStructure`, path slice, crossing, flow valuation, or mathematical description may be related to functional structure through `C.30.TFS-REL`, `E.18`, or `E.18.2`, but it is not the functional architecture itself unless the positive selected-structure co-reference check succeeds.

#### A.6.F:4.5 - Function-flow-module alignment note

Use this note when functional wording touches flow or module allocation but does not yet require a full structural view or `A.6.M` module-relation repair.

```text
FunctionFlowModuleAlignmentNote:
required function or effect:
flow path or dependency:
proposed module allocation:
role, work, or evidence consequence:
known mismatch:
governingPatternApplicationRefs:
admissible use:
non-admissible use:
```

The note is a boundary and source-finding aid. Functional architecture, module relation, implemented-interface, evidence-sufficiency, and architecture-decision claims remain with their governing patterns.

#### A.6.F:4.6 - Common kind and relation separations

| Confusion | Repair |
| --- | --- |
| function = module | Keep `VP.Functional` and `VP.ModuleInterface` distinct; connect them through declared correspondence, allocation, retargeting, or `A.6.M` module-relation repair. |
| function = capability | Capability belongs to a holon; function-like wording describes required transformation, required effect, or architectural relation only when that FPF value kind, relation record, slot reference, view record, or governing pattern named by value is declared. |
| function = work | Work is a dated occurrence or result; function is design-side or description-side content unless a work-evidence claim is being made. |
| function = method | Method is a reusable way of doing; function-like wording names required transformation or effect only when a method or method-description claim is being made separately. |
| function = role | Role and enactor structure uses `VP.RoleEnactor` and role records; function-like responsibility wording needs role and enactor relation recovery. |
| mathematical function = holon purpose | Use C.29 for mathematical function or relation; recover domain, codomain or relation domain, preserved and lost structure, lens-use admissibility value, and stop condition. |
| functional diagram = evidence | Diagram is a view or publication; evidence claim uses `A.10` or `G.6`. |
| functionality = quality | Recover the quality bearer and governing pattern through `C.25`, `C.16`, or C.16.Q before using the wording as an adequacy claim. |

#### A.6.F:4.7 - Composability and compositionality

Composability and quality compositionality are separate claims. If the text says parts can be assembled, keep that as a structure or use claim. If it says a quality of the whole follows from parts, assign the quality-composition claim to `C.25` and C.16-backed measurement or quality claim:

```text
Composability:
  "A and B can be assembled under interface X."
  recoveredRelationRecordRefs: ModuleAllocationRelation; InterfaceSpecification
  directGoverningPatternApplicationRefs: A.6.M when a module-interface claim remains; A.6.5 when a signature claim remains
Quality compositionality:
  "The assembled whole preserves safety, latency, or reliability."
  recoveredSlotRefs: QBundleSlot; structuralCharacteristicQBundleInputSlot; structuralCharacteristicCausalHypothesisForQBundleSlot; structuralCharacteristicEvidenceRelationForQBundleSlot
  directGoverningPatternApplicationRefs: C.25; C.16 or C.16.Q; A.10 only when the evidence-provenance path is the claim being made
Non-admissible:
  successful assembly is not quality propagation
```
Compositional formalisms may express explicit composition structures and view or model relations. They do not make safety, latency, reliability, or another quality propagate automatically.

```text
CompositionalityClaim@Quality ::= {
  affectedQBundleRef,
  partStructureRefs,
  wholeStructureRef,
  compositionRelation,
  lensUseAdmissibilityValue,
  nonAdmissibleUse
}
```

#### A.6.F:4.8 - Worked slices

**Functional architecture phrase.** A team says, "the functional architecture is the user journey." A.6.F does not let the phrase create a separate architecture kind. The repair is:

```text
FunctionUseRepair:
phrase: "functional architecture"
claimKindUnderRepair: functionalArchitecture
recoveredSlotRefs: ArchitectureOf@Context.structureKindRef = FunctionalStructure
recoveredViewRecordRefs: FunctionalStructureView@Context when selected functional structure changes action
recoveredFpFReferenceRefs: ArchitectureOf@Context with structureKindRef = FunctionalStructure
directGoverningPatternApplicationRefs: C.30; C.30.ASV
blockedLocalOverreadRefs: user journey publication, work log, selected transformation-flow structure, mathematical graph description, module diagram
nextAdmissibleMove: open C.30.ASV only if the selected functional structure changes action
stopCondition: ordinary phrase remains Plain if no architecture claim is being made
```
**Functionality as quality.** A product note says, "new functionality improves adequacy." The repair separates added capability or effect from quality claim. Capability or effect wording may stay as recognition, but adequacy claim goes to `C.25`, `C.16`, C.16.Q, or an admitted characteristic or measurement governing pattern when the claim is being made. A.6.F stops after value-kind, relation-record, slot-reference, view-record, or governing-pattern recovery when no quality claim remains.

**Mathematical function or loss.** A model note says, "the loss function explains the holon purpose." The repair keeps the mathematical function under C.29 lens discipline: domain, codomain or relation domain, preserved and lost structure, lens-use admissibility value, and stop condition. The loss may inform a reasoning move; it does not become holon purpose, evidence sufficiency, causal proof, assurance, or project decision by itself.

**Pump-station functional dependency.** A maintenance note says, "the backup pump function is degraded." A.6.F first separates the required effect, the holon capability, the physical module allocation, the performed maintenance work, the evidence relation, and the quality claim. The functional wording may open a `FunctionalStructure` view under C.30.ASV or a capability record; it does not by itself prove the pump was tested, authorize operation, or make the backup module compatible with the main line.

**Product-platform allocation.** A hardware team says, "thermal management functionality moved to the chassis." The repair separates required heat-removal effect, module allocation, interface constraints, signature constraints, architecture structural view, and any evidence or gate claim. A.6.F keeps the function-like wording useful for architecture work while sending module-interface and evidence claims to their governing patterns.

