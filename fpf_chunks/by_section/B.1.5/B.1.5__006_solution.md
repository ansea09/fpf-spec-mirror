---
chunk_kind: "child"
pattern_id: "B.1.5"
pattern_title: "Gamma_method - Order-Sensitive Method Composition and Work Enactment"
section_id: "B.1.5:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5/B.1.5__006_solution.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "B.1.5 — Gamma_method - Order-Sensitive Method Composition and Work Enactment"
  - "B.1.5:4 — Solution"
line_start: 34863
line_end: 35015
dependencies:
  - "A.1"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.3.1"
  - "A.3.2"
  - "A.6.0"
  - "A.6.1"
  - "B.1"
  - "B.1.4"
  - "B.1.6"
  - "B.2"
  - "B.3"
  - "B.3.5"
  - "C.13"
  - "C.29"
  - "E.10"
  - "E.20"
  - "G.5"
  - "U.Method"
  - "U.MethodDescription"
keywords:
  - "MIC"
  - "assurance hooks"
  - "capability continuity"
  - "method composition"
  - "method relation structure"
  - "method/work granularity"
  - "order-sensitive method"
  - "submethod"
  - "typed join"
  - "work enactment"
---

### B.1.5:4 - Solution

Admit one composite `U.Method` only when all composition coordinates are recovered.

```text
OrderSensitiveMethodComposition:
  WholeMethodRef: U.Method
  BoundedContextRef: U.BoundedContext
  PartMethodRefs: non-empty set of U.Method
  WholeFormingRelations:
    serial | parallel | guardedChoice | iteration | refinement | substitution | fallback | adapter | typedJoin
  WholeIdentity:
    preconditions
    effects or postconditions
    invariants
    accepted inputs and outputs
    failure and stop conditions
  MethodInterfaceExposure:
    exposed interactions
    forwarded interactions
    encapsulated interactions
  MHTOrWholeReidentification:
    whole-level commitment or B.2 relation when needed
  AssuranceHooks:
    typed joins, adapters, fragile branches, cutsets, evidence targets
  EnactmentBoundary:
    which U.Work may enact this method and which U.MethodDescription describes it
  LoweredDispositionIfNotComposite:
    MethodRelationStructure | U.MethodDescription | U.WorkPlan | U.Work | G.5 selector | lens | A.15.4 appearance-based reliance repair request
```

#### B.1.5:4.1 - Recover Parts Before Composition

Do not start from the word "step". Start from the object claim.

An apparent step can be:

- a `U.Method` submethod;
- a description constituent inside `U.MethodDescription`;
- a plan item inside `U.WorkPlan`;
- a dated `U.Work` occurrence or work part;
- an order relation, fallback relation, or selector relation inside `MethodRelationStructure@BoundedContext`;
- a mathematical or representation lens over a relation structure;
- mechanism or formal-substrate material;
- quoted wording that does not yet carry a method claim.

Only the first case can be a method part. Do not mint `U.StepSpec`, `U.StepMethod`, `U.MethodStep`, or `U.MethodAlgebra` for the others.

#### B.1.5:4.2 - Admit The Composite Method

When the apparent parts are recovered as `U.Method` values, compose them only after naming the whole-forming relations:

- **serial composition** when one submethod's accepted result is a precondition for the next;
- **parallel composition** when branches can proceed independently under a declared join condition;
- **guarded choice** when one branch is selected by a declared predicate;
- **iteration** when a submethod repeats until a stop condition is met;
- **refinement or substitution** when a submethod can stand in for another under declared bounds;
- **fallback or dispatch** when a selector chooses a method family member;
- **adapter** when a conversion method is needed to make a typed join admissible.

For order-sensitive composition, the method-composition claim also needs the order apparatus by reference: `OrderSpecRef`, any context hash or partial-order reproducibility condition inherited from `B.1.4`, and the typed join or adapter evidence that says one submethod's accepted outputs meet the next submethod's preconditions. This preserves the old capability-continuity obligation without treating "capability type" as the capability instance itself.

The result is one composite `U.Method` only when the whole has its own identity: preconditions, effects, invariants, accepted inputs and outputs, failure conditions, and work-facing acceptance relation. If those whole-level commitments cannot be named, lower the claim to `MethodRelationStructure@BoundedContext` or another neighboring object.

#### B.1.5:4.3 - Keep Order Out Of Structural Mereology

`SerialStepOf`, `ParallelFactorOf`, guarded choice, iteration, fallback, adapter, and typed join are method-composition or method-relation claims. They are not A.14 component parthood.

Use A.14, C.13, and B.3.5 when the claim is about structural parts of a holon. Use B.1.5 when the claim is about how ways of doing compose into a larger way of doing. The same project may need both, but they are different relation families.

When the current method-composition claim needs explicit order aggregation, context hash, partial-order soundness, or `Gamma_ctx` notation, use `B.1.4` for that ordered-relation apparatus. `B.1.4` can express the order discipline; B.1.5 still decides whether the recovered ordered methods are enough to admit one composite `U.Method`.

When the current claim is temporal phasing of the same carrier or method-description edition history, use the pattern that governs the phase or temporal claim rather than B.1.5. A phase boundary becomes a B.2-family question only when the boundary also introduces whole reidentification, closure, supervision, or context rebase. Order, phase, structural parthood, and MHT are different claims even when one source diagram uses one line for all of them.

#### B.1.5:4.4 - Expose The Composite Method Interface

A composite method needs an interface exposure decision:

- **exposed:** a caller may rely on the interaction as part of the whole method;
- **forwarded:** a caller may address an internal submethod interaction through a declared namespace or adapter;
- **encapsulated:** the interaction is internal and cannot be relied on from outside the whole method.

The interface exposure decision is part of the composite method identity when outside work, assurance, planning, or substitution relies on it. It is not a publication layout decision.

#### B.1.5:4.4.1 - Method Interface Card (MIC)

When an interface exposure decision is reliance-bearing, publish it as a compact Method Interface Card (MIC). The MIC is a method-description or assurance-facing card about the composite method; it is not a new U-kind and not the method itself.

```text
MethodInterfaceCard:
  methodRef: U.Method
  methodDescriptionRef?: U.MethodDescription
  orderSpecRef?: B.1.4 order apparatus
  externalInteractions:
    - interactionName
      exposureMode: exposed | forwarded | encapsulated
      acceptedInputOrCallSignature
      preconditions
      postconditionsOrEffects
      qualityEnvelopeRefs?
  invariants
  adapterOrTypedJoinRefs?
  assuranceHookRefs?
  rationale
```

Use a MIC when callers, planners, auditors, or substituting methods may rely on the composite boundary. For lightweight internal use, a few exposure lines may be enough; do not create a separate card by ritual.

#### B.1.5:4.5 - Keep Method Admission And Work Occurrence Separate

B.1.5 admits and grounds a composite `U.Method`. It may require a `U.MethodDescription` to describe the composition. It does not by itself create performed work.

A performed enactment is `U.Work` under `A.15.1`. The work record cites:

- the enacted `U.Method`;
- the method-description reference when current;
- the performer through `U.RoleAssignment`;
- the time window, parameter bindings, affected referent, resource ledger, outcome, and evidence relations.

Resource aggregation, elapsed time, telemetry, retries, and work outcomes belong to `U.Work`, `Gamma_work`, and evidence patterns. They do not become parts of the method.

The composition link is not one-to-one. A work occurrence may enact the whole method without exposing every submethod as a separate work part. A temporal work slice often enacts the same whole method during a selected interval. An episode may span several method factors, repeat one factor, or be split by evidence policy without changing the method identity. A work part enacts a submethod only when that submethod has already been recovered as `U.Method`; otherwise the current object is a work part, method-description node, evidence segment, mechanism material, system-component behavior, or `A.15.4` appearance-based reliance repair request.

**Reader check.** Before saying that a work part enacts a submethod, name both sides:

- the occurrence-side object: parent `U.Work`, part relation, interval or boundary event, performer, resources or evidence role;
- the method-side object: recovered `U.Method` submethod, whole-forming relation, preconditions, effects, interface, and whole-method identity.

If either side is missing, lower only that side. Do not repair a missing submethod by inventing a work part, and do not repair a missing work part by inventing a submethod.

#### B.1.5:4.5.1 - Planning And Performed-Work Obligations

B.1.5 has two common use positions, but they are positions in use, not two U-kinds:

- **Planning or description-side use.** Recover the submethods, order apparatus, typed joins or adapters, method interface exposure, invariants, and whole-level commitments. The output is a composite `U.Method` claim and, when a representation is needed, a `U.MethodDescription` or MIC that describes that method.
- **Performed-work use.** A `U.Work` occurrence may cite the composite `U.Method` and the method-description reference it used. The work record checks role assignment, capability-fit or admission conditions when current, preconditions, postconditions, order conformance, MIC-honouring interactions, resource ledger handoff, and evidence relations. These checks annotate or support the performed work; they do not become parts of the method.
- **Assurance use.** Identify cutset submethods, fragile typed joins, adapter points, mapping congruence or CL-sensitive edges, and the envelope or scope in which the composite method is expected to hold. B.3 and related assurance patterns evaluate those hooks; B.1.5 only makes them visible.

Useful invariants remain: a single recovered submethod composed alone does not create a surprising new method; order is deterministic only under the declared order apparatus; composite quality or throughput is constrained by critical path and weakest-link considerations unless a B.2-family whole reidentification claim is separately admitted; strengthening a submethod, adapter, or typed join should not make the composite method worse unless a stated side condition changes.

#### B.1.5:4.6 - Use MethodRelationStructure Below Whole-Method Threshold

Use `MethodRelationStructure@BoundedContext` when method-side relations are current but one whole method is not admitted. Typical cases:

- a fallback registry selects among alternatives;
- a workflow diagram relates method descriptions but does not recover method parts;
- a method family has refinement, substitution, or dispatch relations;
- a graph or algebra analyzes method relations as a lens;
- a cross-context source uses the same method names without a bridge for method identity;
- a work plan orders tasks but does not define one reusable method.

This lower object is not a failure. It is the right governed object when relation structure is useful but method holon composition is not current.

