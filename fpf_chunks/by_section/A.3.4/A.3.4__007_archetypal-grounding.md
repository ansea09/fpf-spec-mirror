---
chunk_kind: "child"
pattern_id: "A.3.4"
pattern_title: "U.Transformation: Bounded Change Under Conditions"
section_id: "A.3.4:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.4/A.3.4__007_archetypal-grounding.md"
commit_sha: "89fcd508edbf9a49dc956955a42884fbca43f88c"
heading_path:
  - "A.3.4 — U.Transformation: Bounded Change Under Conditions"
  - "A.3.4:5 — Archetypal Grounding"
line_start: 7684
line_end: 7747
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.3"
  - "A.3.1"
  - "A.3.2"
  - "A.3.3"
  - "A.6.0"
  - "A.6.1"
  - "A.6.5"
  - "A.6.F"
  - "A.7"
  - "B.3"
  - "C.2.1"
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "C.30.ASV"
  - "C.32.P2S"
  - "E.18"
  - "E.18.1"
  - "E.18.2"
  - "E.20"
  - "E.24"
keywords:
  - "bounded change"
  - "functioning"
  - "input/output conditions"
  - "transformation"
  - "transformation-flow structure"
  - "transformed entity"
  - "transformer"
---

### A.3.4:5 - Archetypal Grounding

#### A.3.4:5.1 - Physical System Change

A nuclear-plant team claims a revised operating method stabilizes a temperature profile after a thermal-power change.

`U.Transformation` names the bounded change: reactor subsystem under context, initial operating condition, post-change stability condition, transformation relation, admissibility and safety boundary, and time window. The operating method is `U.Method`; the operation algebra or control law may be `U.Mechanism`; the state-space model is `U.Dynamics`; the work trace is `U.Work`; the safety evidence and gate use remain with evidence and gate patterns.

#### A.3.4:5.2 - Biological Editing

A CRISPR project claims an editing protocol changes a DNA target while keeping off-target risk under a bound.

`U.Transformation` names the changed biological target, initial condition, post-state or delta, editing transformation relation, admissibility or boundary condition, and any temporal or ordering reference that changes the claim. The editing protocol fills `MethodDescriptionRef` or `MethodRef` when it is a selected way of doing; the biochemical mechanism fills `MechanismRef`; off-target measurements fill `EvidenceOrSourceRef`; the observed edited sequence or accepted lab output fills `ResultRef`. The protocol description is not the transformation; the biochemical mechanism is not the dated lab work; the off-target evidence is not permission to use the result.

#### A.3.4:5.3 - Specification Repair

A safety specification is revised so that an emergency-stop boundary no longer permits two incompatible readings.

`U.Transformation` can name the bounded change to the specification episteme: the affected episteme or section, the initial ambiguous condition, the clarified post-state condition, the transformation relation, and the review or acceptance condition. The edit work is `U.Work`; the repair method is `U.Method`; the revised specification remains an episteme or publication under its own governing pattern.

#### A.3.4:5.4 - Formal Construction

A mathematical proof constructs an object and shows that a morphism preserves a chosen invariant.

`U.Transformation` may govern the formal transformation when the formal object is the `EntityOfConcern`: initial formal object, constructed object or delta, morphism or construction relation, and admissibility or invariant condition. Formal substrate or mathematical lens fills `FormalOrMathLensRef` unless it is already the context-of-meaning for the formal object; the proof relation fills an evidence relation, a source relation, or a `C.2.1` claim-bearing episteme, not core transformation identity. It does not describe project-world work until a separate realization, method, work, or evidence relation is named.

#### A.3.4:5.5 - Architecture Move

An architecture team changes a selected structure so that an interlevel conflict is reduced while a key architecture characteristic stays within bounds.

`U.Transformation` names the structure change and delta condition. The architecture pattern governs the selected structure and characteristic; `C.29` may supply a mathematical lens for preserved and lost structure; `C.27.TA` may govern trajectory, cadence, recovery, inertia, or validity window; work planning and dated work stay with `A.15.2` and `A.15.1`.

#### A.3.4:5.6 - Functional Transformer In A Flow

Use this slice when the same sentence says that a system "performs a function", "transforms input to output", or "implements an algorithm". The first question is not whether a function word is present. The first question is which transformation, bearer, input/output boundary, method or algorithm, and flow position are current.

```text
Functional transformation slice:
  TransformationCore:
    transformedEntityOrStructure:
    boundedContext:
    initialCondition:
    postStateConditionOrDelta:
    transformationRelation:
    admissibilityOrBoundaryCondition:
  TransformerRef?: U.System bearing TransformerRole@Context, candidate system, or not recovered
  InputConditionOrPortRefs?: accepted input state, flow, material, energy, signal, information, work product, formal object, condition, or functional port signature
  OutputConditionOrPortRefs?: produced state, flow, material, energy, signal, information, work product, formal object, condition, or functional port signature
  FunctioningRef?: FunctionalElement@Context relation when this transformation is used as the element's functioning
  MethodRef? or MethodDescriptionRef?: algorithm, protocol, recipe, controller, or generalized method only when that claim is current
  MechanismRef?: law-governed realization or operation structure when current
  TransformationFlowStructureRef?: containing flow, path, path slice, composition, coupling, or constraint when current
```

Examples:

- A pump in a hydraulic network is a `U.System` filling `TransformerRef?` when it raises pressure or moves fluid under the current claim. Its required behavior grounds a `U.Transformation`; inlet/outlet hydraulic conditions or port signatures fill input/output slots; the pump curve may fill mechanism or dynamics slots; the network path fills `TransformationFlowStructureRef?`.
- A resistor in an electrical circuit is a system or component locus bearing transformer role when the claim is voltage-current relation, heat dissipation, or signal conditioning. Its terminals are not module interfaces by default; they are input/output or port-signature slots for the electrical transformation unless a module-interface claim is current.
- A warehouse in a logistics network performs receiving, storing, picking, or shipping transformations. The warehouse or candidate subsystem fills `TransformerRef?`; pallets, orders, inventory states, or documents fill input/output slots; a routing algorithm may be `U.Method` or `U.MethodDescription`; dated picking work remains `U.Work`.
- A refrigerator thermal cycle has compressor, condenser, expansion, and evaporator transformations inside one `TransformationFlowStructure`. The refrigerator or subsystem can fill `TransformerRef?`; heat-flow and refrigerant-state boundaries fill input/output slots; the thermodynamic mechanism and control method stay with their governing slots.
- A neural-network block transforms activations inside an architecture flow. The block can be a candidate system or module locus depending on the claim; tensor shape signatures may fill input/output slots; an attention algorithm may be method or method description; benchmarks, ablations, or pruning masks are evidence/result or architecture claims only when their governing patterns are current.

These cases permit the sentence "the system performs a functional transformation at this point in the flow" when the system/candidate system, `TransformerRole@Context`, bounded transformation, input/output boundary, and flow location are named or explicitly marked unknown/not-current. They also prevent the overread that a named algorithm, module, port, or evidence record by itself proves the transformation, functioning, compatibility, or result.

