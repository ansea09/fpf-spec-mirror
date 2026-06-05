---
chunk_kind: "child"
pattern_id: "A.6.F"
pattern_title: "Function and Functional Precision Restoration (RPR-FUNCTION)"
section_id: "A.6.F:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.F/A.6.F__005_solution.md"
commit_sha: "eaafd3a43b9173706e1f8388a3bc94c6445397e4"
heading_path:
  - "A.6.F — Function and Functional Precision Restoration (RPR-FUNCTION)"
  - "A.6.F:4 — Solution"
line_start: 13483
line_end: 13657
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
  - "C.30.TGA-FLOW-REL"
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

A.6.F is an A.6.P RPR specialization for function-like wording. It does not mint `U.Function`. It assigns the live use to an existing FPF kind, relation, claim record, view, or receiving-pattern application and stops there unless another claim kind remains live.

#### A.6.F:4.1 - Trigger rule

A.6.F applies when a sentence uses function-like wording to carry one or more live FPF claim kinds:

- architecture or functional architecture;
- capability, effect, externally promised behavior, or user-visible functionality;
- method wording, work occurrence, or work result;
- role expectation or responsibility;
- mathematical function, mapping, relation, loss, objective, or value functional;
- quality, fitness, characteristic, score, or proxy wording;
- module allocation, interface, signature, port, API, protocol, flow, or mechanism relation;
- another exact FPF claim, such as evidence, assurance, gate, decision, or release.

If none of those claim kinds is live, the wording may remain ordinary Plain prose.

#### A.6.F:4.2 - FunctionUseRepair

`FunctionUseRepair` is a pattern-local repair note, not a project publication, not evidence, not a decision, and not `U.Function`. `FunctionalStructure` is an `ArchitectureStructureKindRef` value under C.30.ASV, not a kernel Function kind.

```text
FunctionUseRepair ::= {
  phrase,
  liveUse:
    requiredTransformationOrEffect |
    holonCapability |
    methodOrProcedure |
    workOccurrenceOrResult |
    roleExpectation |
    mathematicalFunctionOrRelation |
    qualityOrCharacteristic |
    moduleAllocation |
    interfaceOrSignatureRelation |
    functionalArchitecture |
    evidenceAssuranceGateDecisionClaim |
    otherDeclared,
  recoveredFpFKind:
    FunctionalStructure |
    U.Capability |
    U.Method |
    U.MethodDescription |
    U.Work |
    MathematicalFunctionUnderC29 |
    QBundleSlot |
    ModuleAllocationRelation |
    InterfaceSpecification |
    RoleExpectation |
    EvidenceOrGateCue |
    otherDeclared,
  recoveredFpFReference?,
  falseFpFKindRefs,
  recordGoverningPatternRef,
  governingPatternApplicationRefs?,
  admissibleUse,
  nonAdmissibleUse,
  nextAdmissibleMove,
  stopCondition
}
```

The repair is complete when a practitioner can say which exact FPF kind, relation, claim record, view, or receiving-pattern application the function-like wording uses, which false FPF kinds or relations it does not use, and what the next admissible architecture or exact governing pattern application is. If the text still hides a function, capability, work, method, role, module, or mathematical-function collapse, the repair is incomplete.
#### A.6.F:4.3 - Repair assignments

| Function wording use | First FPF kind or receiving locus | Boundary |
| --- | --- | --- |
| required transformation or effect | `VP.Functional`, `FunctionalStructureView@Context`, or locally declared capability or effect record | Does not imply physical module, work occurrence, or evidence. |
| capability of a holon | `U.Capability` or the exact capability-governing pattern or project record named by the live claim | Does not imply that a method, module, or work occurrence exists. |
| method wording | `U.Method`, `MethodDescription`, `VP.Procedural`, or A.15 design or run boundary as triggered | Does not imply execution. |
| work occurrence or work result | `U.Work`, Work record, or P2W relation under the governing TGA work-result pattern | Does not imply reusable function ontology. |
| responsibility or role expectation | `VP.RoleEnactor` and the relevant role and enactor relation | Does not imply the role-holder performed the work. |
| mathematical function or relation | C.29 mathematical-lens use with domain, codomain or relation domain, preserved and lost structure, lens-use admissibility value, and stop condition | Does not become architecture, evidence, causal proof, assurance, or decision claim by itself. |
| quality or fitness expression | `C.25`, `C.16`, `C.16.Q`, `A.17`, `A.18`, or an admitted characteristic or measurement receiving pattern according to the live claim | Does not let "functionality" carry a quality claim without bearer and exact governing pattern. |
| module allocation | `FunctionalStructureView@Context` plus declared correspondence, allocation, retargeting, or `A.6.M` module-relation repair as live | Does not make function and module one FPF kind. |
| interface or signature relation | `InterfaceSignatureBoundaryNote`, A.6.0, A.6.5, A.6.B, A.6.C, A.6.8, or `A.6.M` module-relation repair when live | Does not turn a functional link, port label, API name, or signature into implemented compatibility. |
| functional architecture | `ArchitectureOf@Context` with `structureKindRef = FunctionalStructure` and `FunctionalStructureView@Context` under C.30.ASV | Not a peer architecture ontology and not a TGA graph by itself. |

#### A.6.F:4.4 - Functional architecture boundary

Functional architecture is the `FunctionalStructure` case of `ArchitectureOf@Context`: the declared organization of required transformations, capabilities, effects, functional dependencies, and constraints that a holon is to realize, before or alongside allocation to modules, roles, work, evidence, control relations, or flow or transduction descriptions.

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

This shorthand is admissible only when the expanded C.30 or C.30.ASV interpretation is recoverable. A TGA graph, path slice, crossing, or flow valuation may be related to functional structure through `C.30.TGA-FLOW-REL`, but it is not the functional architecture itself.

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

The note is a boundary and source-finding aid. It is not the functional architecture, not a module relation, not an implemented interface, not evidence sufficiency, and not an architecture decision.

#### A.6.F:4.6 - Common kind and relation separations

| Confusion | Repair |
| --- | --- |
| function = module | Keep `VP.Functional` and `VP.ModuleInterface` distinct; connect them through declared correspondence, allocation, retargeting, or `A.6.M` module-relation repair. |
| function = capability | Capability belongs to a holon; function-like wording describes required transformation or effect or architectural relation only when that exact FPF kind or relation is declared. |
| function = work | Work is a dated occurrence or result; function is design-side or description-side content unless work evidence is explicitly live. |
| function = method | Method is a reusable way of doing; function-like wording names required transformation or effect only when method or method-description claim is not live. |
| function = role | Role and enactor structure uses `VP.RoleEnactor` and role records; function-like responsibility wording needs role and enactor relation recovery. |
| mathematical function = holon purpose | Use C.29 for mathematical function or relation; recover domain, codomain or relation domain, preserved and lost structure, lens-use admissibility value, and stop condition. |
| functional diagram = evidence | Diagram is a view or publication; evidence claim uses `A.10` or `G.6`. |
| functionality = quality | Recover the quality bearer and exact governing pattern through `C.25`, `C.16`, or C.16.Q before using the wording as an adequacy claim. |

#### A.6.F:4.7 - Composability and compositionality

Composability and quality compositionality are separate claims. If the text says parts can be assembled, keep that as a structure or use claim. If it says a quality of the whole follows from parts, assign the quality-composition claim to `C.25` and C.16-backed measurement or quality claim:

```text
Composability:
  "A and B can be assembled under interface X."
  recoveredFpFKind: ModuleAllocationRelation | InterfaceSpecification
Quality compositionality:
  "The assembled whole preserves safety, latency, or reliability."
  recoveredFpFKind: QBundleSlot | structuralCharacteristicQBundleInputSlot | structuralCharacteristicCausalHypothesisForQBundleSlot | structuralCharacteristicEvidencePathForQBundleSlot
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
liveUse: functionalArchitecture
recoveredFpFKind: FunctionalStructure
recoveredFpFReference: ArchitectureOf@Context with structureKindRef = FunctionalStructure
falseFpFKindRefs: user journey publication, work log, TGA graph, module diagram
nextAdmissibleMove: open C.30.ASV only if the selected functional structure changes action
stopCondition: ordinary phrase remains Plain if no architecture claim is live
```
**Functionality as quality.** A product note says, "new functionality improves adequacy." The repair separates added capability or effect from quality claim. Capability or effect wording may stay as recognition, but adequacy claim goes to `C.25`, `C.16`, C.16.Q, or an admitted characteristic or measurement receiving pattern when the claim is live. A.6.F stops after exact-kind or relation recovery when no quality claim remains.

**Mathematical function or loss.** A model note says, "the loss function explains the holon purpose." The repair keeps the mathematical function under C.29 lens discipline: domain, codomain or relation domain, preserved and lost structure, lens-use admissibility value, and stop condition. The loss may inform a reasoning move; it does not become holon purpose, evidence sufficiency, causal proof, assurance, or project decision by itself.

