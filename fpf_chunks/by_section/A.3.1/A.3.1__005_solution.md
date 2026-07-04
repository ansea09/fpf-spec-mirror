---
chunk_kind: "child"
pattern_id: "A.3.1"
pattern_title: "U.Method: Context-Defined Way of Doing"
section_id: "A.3.1:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.1/A.3.1__005_solution.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "A.3.1 — U.Method: Context-Defined Way of Doing"
  - "A.3.1:4 — Solution"
line_start: 6313
line_end: 6503
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.7"
  - "A.3"
  - "A.3.2"
  - "A.3.3"
  - "A.6.0"
  - "A.6.1"
  - "B.1.5"
  - "C.2.P.DR"
  - "C.20"
  - "C.29"
  - "C.36"
  - "C.36.P"
  - "E.18"
  - "E.18.1"
  - "E.20"
  - "G.5"
  - "U.BoundedContext"
  - "U.Capability"
  - "U.RoleAssignment"
keywords:
  - "method"
  - "method composition"
  - "method vs method description vs work"
  - "non-agentive holon"
  - "submethod"
  - "way of doing"
---

### A.3.1:4 - Solution

`U.Method` is the **context-defined semantic way of doing a kind of transformation or enactment**.

It is a non-agentive holon kind. Part methods can be selected, bounded, ordered, joined, adapted, and hidden or exposed through method interfaces to form a whole method with whole-level preconditions, effects, invariants, constraints, and assurance hooks. The whole method may then be used as a part method in a larger method.

It is not the text, code, diagram, model, plan, run, role, capability, or evidence relation that may be associated with that way of doing. A `U.Method` is:

* **context-defined**: its identity, admissible inputs, conditions, effects, and bounds are interpreted inside a `U.BoundedContext`;
* **semantic**: it is the way of doing that descriptions denote and work may enact;
* **transformation-facing**: it concerns a possible or intended transformation, enactment, or produced result, including physical, informational, organizational, mathematical, or hybrid transformations;
* **description-independent**: one method may be described by several `U.MethodDescription` epistemes;
* **run-independent**: one method may be enacted by many `U.Work` occurrences;
* **assignment-independent**: method admission conditions may name role kinds or capability-fit conditions, but named holders and dated assignments belong elsewhere.

The primary repair action is not to replace the word "method" or "practice" with one better word. In ordinary source speech, `practice` often works as a synonym for method-like wording, but it can also name enacted work, role arrangement, discipline, tradition, source label, or cultural-evolution material. Recover the current slot first:

| If the text is really about... | Govern it as... |
| --- | --- |
| semantic way of doing | `A.3.1 U.Method` |
| relation or composition among methods, method families, or local method expressions | `A.3.1` with `A.3.2`, `A.15`, `G.5`, or a direct method-composition pattern such as `B.1.5` when current; algebraic or graph notation is only `C.29` lens or method-description representation |
| description of that way of doing: SOP, program, proof script, solver model, protocol, diagram, process model, recipe text | `A.3.2 U.MethodDescription` |
| source phrase such as practice, technique, school, tradition, or local method label whose current object is unclear | recover the claim kind first through `E.10` and this table; use `A.1.1` when the phrase names a bounded context, and use `C.36.P` when the cultural-evolution, tradition, style, canon, recognition, selection, or mediation context is current |
| selected formal substrate or mathematical declaration | `A.6.0` and `C.29` when mathematical-lens use is current |
| mechanism declaration or realization relation | `A.6.1` and `E.20` |
| role assignment, role relation, responsibility allocation, or holder eligibility hidden under a practice or method phrase | `A.2`, `A.2.1`, `A.2.7`, and `A.15` as applicable |
| planned dated work or authorization to prepare work | `A.15.2 U.WorkPlan` plus the relevant gate, authority, or commitment pattern |
| dated work occurrence, run, trace-backed execution, result record | `A.15.1 U.Work` and evidence or source patterns when an evidence relation or source relation is current |
| field-level discipline, bounded context, community tradition, canon or memory episteme, recognition or selection regime, mediation system, variant set, or cultural-evolution intervention | `A.1.1`, `C.20`, `C.36`, `C.36.P`, `F.17`, `F.18`, `F.9`, `C.18`, `C.19`, `G.5`, or `G.11` according to the recovered claim |
| evidence or provenance relation for a claim | `A.10` |
| graph path, path slice, flow valuation, state predicate, query, table, dashboard, publication face, or pattern relation overread as a method or work sequence | `C.2.P.DR` first, then the direct governing pattern named by the recovery |

#### A.3.1:4.1 - Thin first-use record

For ordinary first use, write only the fields needed to keep the method claim from collapsing into a description, plan, run, mechanism, or evidence relation:

```text
Method statement:
  MethodRef:
  BoundedContext:
  TransformationOrEnactmentKind:
  EntityOfConcern:
  Preconditions:
  IntendedEffectsOrPreservedConditions:
  CurrentMethodDescriptionRef:
  WorkRelation:
  ClaimBoundary:
```

`ClaimBoundary` names the nearest stronger claim that is not carried by this method statement, such as work authorization, performed work, evidence for success, mechanism declaration, or formal-substrate adequacy. It is a boundary field, not a place to repeat every neighboring pattern.

#### A.3.1:4.2 - Method and mechanism settlement

Do not decide the method and mechanism question by vocabulary. When a source expression or project concern appears to name changing, producing, selecting, deriving, controlling, or maintaining an `EntityOfConcern`, use `E.10.ARCH:3.1` to recover the project concern first and then assign separately governed typed FPF values.

For this host, keep the local question thin: does the current claim state a `U.Method`, the context-local way of doing a transformation or enactment? If the source label also raises mechanism, formal-substrate, work-plan, dated-work, role-assignment, cultural-evolution, discipline, evidence, source, gate, result, publication, or temporal claims, keep those values linked only by explicit relation positions and apply their own governing patterns.
* In **method position**, the current claim is the context-local way of doing a transformation or enactment.
* In **mechanism position**, the current claim is a law-governed declaration or revision of operations, laws, admissibility predicates, transport, audit relation set, and monotone realizations under `A.6.1` and `E.20`.

Do not assign the same typed value as both `U.Method` and `U.Mechanism` unless a governing pattern explicitly admits such dual typing. Slot-position labels do not create alternate ontology.

This gives the working distinction:

| Current question | Governing pattern | What must be recoverable |
| --- | --- | --- |
| What way of doing is intended or enacted? | `A.3.1 U.Method` | context, transformation or enactment kind, preconditions, effects, work-facing identity, description relation |
| What description states the way of doing? | `A.3.2 U.MethodDescription` | episteme, representation form, method described, parameters, acceptance criteria, edition relation or source relation when current |
| What law-governed operation structure is being declared, specialized, transported, or realized? | `A.6.1 U.Mechanism` | `SubjectBlock`, `OperationAlgebra`, `LawSet`, `AdmissibilityConditions`, `Applicability`, `Transport`, `Audit`, realization relation |
| Where should new or revised mechanism meaning be governed? | `E.20` | governing-definition assignment for mechanism meaning, suite, plan, wiring, token continuity, or local non-trigger stop |
| What happened this time? | `A.15.1 U.Work` | performer, method enacted, method-description source relation when current, time window, parameters, resources, outcome |

A method may cite a mechanism, be selected by a mechanism, be constrained by a mechanism, or be one value in a mechanism's slot. A mechanism may govern an operation algebra whose operations include applying, selecting, composing, or normalizing methods. Those links do not collapse the typed values or their governing claims. If both claims are current, write both: the `U.Method` statement for the way of doing, and the `U.Mechanism` statement for the law-governed declaration or realization relation.

Fail closed when neither position can be recovered. Do not repair `practice`, `algorithm`, `program`, `workflow`, `process`, `solver`, `proof`, `recipe`, or `control strategy` to `method` or `mechanism` merely because the replacement sounds more technical.

#### A.3.1:4.3 - Method, MethodDescription, WorkPlan, Work

Keep the four positions separate.

| Position | What it means | Common mistaken substitutes |
| --- | --- | --- |
| `U.Method` | how in principle, inside a bounded context | code, SOP, graph, solver model, proof script, workflow diagram |
| `U.MethodDescription` | an episteme that describes a method in a representation | method semantics, actual run, authority to work |
| `U.WorkPlan` | planned dated work or work preparation | timeless method, generic recipe, proof that work happened |
| `U.Work` | dated work occurrence | method, plan, result interpretation, evidence relation |

The same solver model, repository, protocol, diagram, or run packet may participate in several claims, but each claim has its own slot. A solver model can be a `U.MethodDescription`; its mathematical formulation can also expose a formal substrate for `C.29`; a solver run can be `U.Work`; a run result can be evidence for a separate claim. Those claims are not interchangeable.

#### A.3.1:4.4 - Method statement fields

A useful `U.Method` statement can usually recover these fields in ordinary project language:

| Field | What to name |
| --- | --- |
| Method name | the context-local way of doing |
| Bounded context | the project, discipline, organization, regulatory setting, theory, or operational context that interprets the method |
| Transformation or enactment kind | what changes, is produced, decided, derived, controlled, selected, or maintained |
| EntityOfConcern under transformation | the material object, information object, organization, episteme, holon, or state whose transformation matters |
| Preconditions | what must already hold for the method to be applicable |
| Effects or postconditions | what successful enactment is meant to produce or preserve |
| Interface or signature | inputs, outputs, ports, resources, constraints, or role-kind admission conditions needed to state the method without naming this run |
| Capability requirements | thresholds or envelopes to be checked against a holder's capability, not baked into the method identity |
| Failure and stop conditions | when the method is blocked, when a description must be revised, or when work must not start |
| Description relation | which `U.MethodDescription` epistemes currently describe it |
| Work relation | what kind of `U.Work` may enact it and how runs cite the description used |

This is not a data schema. It is the minimum recognition field set needed before method-like wording can guide work, evidence, assurance, gates, or planning.

#### A.3.1:4.5 - Representation and programming-paradigm discipline

A `U.Method` does not require an imperative step structure.

Imperative procedures, functional compositions, logical rule sets, constraint models, object-centric event models, effect-handler programs, process diagrams, SQL queries, equality-saturation graphs, proof scripts, and optimization models may all help describe, represent, or analyze a way of doing. Their representation style does not by itself decide whether the current claim position is a method, a method description, a formal substrate, a mechanism, a work plan, work, evidence, or a declarative representation under `C.2.P.DR`.

Use this discipline:

* If the text states the semantic way of doing, use `A.3.1`.
* If the text states the representation that describes that way, use `A.3.2`.
* If the text states a formal object or mathematical representation used to reason, use `A.6.0`, `C.29`, or the direct mathematical pattern.
* If the text states a law-governed operation structure, admissibility predicate set, transport clause, or realization relation, use `A.6.1` or `E.20`.
* If the text states planned work, use `A.15.2`.
* If the text states dated performed work, use `A.15.1`.
* If the text states an evidence relation or provenance relation, use `A.10`.
* If the text turns a graph, path, query, table, dashboard, predicate, publication face, or pattern relation into a route, call sequence, dispatch, or work procedure by metaphor, use `C.2.P.DR` before choosing the direct governing pattern.

This is why "algorithm" and "practice" are not repaired to "method" automatically. An algorithm-looking expression may indicate a method description, formal substrate, mechanism, control strategy, work plan, work occurrence, evidence relation, or quoted source wording. A practice-looking expression may indicate a method, method family, method relation structure, method description, work plan, dated work, role assignment, bounded context, discipline position, cultural-evolution case, canon or memory episteme, recognition or selection regime, mediation system, evidence relation, or quoted source wording. The repair must recover the slot.

#### A.3.1:4.6 - Constructor and process-theory settlement

FPF interprets method claims through transformation first, not software notation first.

In the constructor-theory and process-theory source line adopted here, claims about computation, information, dynamics, and procedure are kept close to possible or impossible transformations and their compositional realization. That gives FPF the following settlement:

* a system in a transformer-like role can enact a method;
* the method is the context-local way of doing the transformation;
* a method description is an episteme that describes that way;
* a formal substrate or mathematical lens may make the method analyzable, but does not become the method by itself;
* a mechanism may declare law-governed operation structure, admissibility predicates, transport, and realization relations for a method-facing transformation, but that mechanism claim is not the same claim as selecting, describing, planning, or enacting a method;
* a work plan prepares or schedules dated work;
* dated work is the occurrence that happened.

This settlement covers welding, milling, reagent mixing, clinical triage, proof construction, optimization, scheduling, training, inference, and software execution without making "code" the privileged form of method.

#### A.3.1:4.7 - Semantic identity and variants

Two `U.MethodDescription` epistemes may describe the same `U.Method` in a bounded context when, for the recognized inputs and conditions of that context, they preserve the same method identity:

* compatible preconditions;
* compatible effects or postconditions;
* compatible non-functional bounds;
* accepted nondeterminism or search behavior;
* the same work-facing acceptance relation.

Different internal control flow, search strategy, proof notation, programming paradigm, diagram notation, or textual format does not by itself make a different method. Conversely, the same name, diagram family, repository, supplier label, or workflow label does not by itself prove identity.

When variants differ only by parameter ranges, equipment envelope, or local representation, keep one method with declared variation when the context accepts that identity. When variants change effects, bounds, accepted inputs, safety envelope, or work-facing acceptance criteria, declare a refinement, substitution, or distinct method.

#### A.3.1:4.8 - Method relation structure, composition, and work enactment

Methods may compose into larger method holons. Work occurrences may compose into larger work histories. These are related but different claims.

When the current question is one semantic way of doing, the governed object is `U.Method`. When submethods are assembled into a whole method, the governed object is still `U.Method`, now under method-holon composition. When the current question is only a relation among methods, method families, local method expressions, method-description links, or work-facing method-use relations, the governed object is `MethodRelationStructure@BoundedContext`: a context-local structure over method-side values.

A method relation structure may include:

- serial composition;
- parallel composition;
- guarded choice;
- iteration;
- refinement;
- substitution;
- decomposition;
- parameterization;
- method-family membership, selection, fallback, or dispatch relation;
- a relation from method role-admission condition to accepted role assignment when work admission depends on it.

Those relations are design-side or definition-side claims about ways of doing. They are not dated work merely because an implementation, graph, process model, or workflow-looking diagram can be executed or followed.

Method-holon composition is not A.14 structural component mereology. `SerialStepOf`, `ParallelFactorOf`, guarded choice, iteration, typed joins, adapters, and method-interface exposure are arrangement or constraint relations over recovered `U.Method` submethods. Method-description nodes may describe those relations, but they are not method parts unless the governed object is recovered as a `U.Method`. Use `B.1.5` when order-sensitive method composition is current, and use `B.2` when the composite method requires whole reidentification.

Work composition is occurrence-side: dated work may interleave, split, merge, retry, fail, recover, or be recorded in traces differently from the method description or method relation structure. Method decomposition and work decomposition are coupled because work enacts method, but they are not isomorphic. A temporal work part may enact the same whole method during a slice. An episode may record continuity under one method or mode while spanning several operational parts, repeating a fragment, or being split by evidence policy. A work part corresponds to a submethod only when the candidate factor is recovered as a `U.Method` with method-level preconditions, effects, interface or boundary, and whole-method relation under `B.1.5`.

**Quick distinction for readers.** If the source names a step, stroke, graph node, detector component, event-log segment, telemetry interval, work-plan item, or document section, ask two questions before using method-part wording:

1. Does this candidate name a reusable way of doing with method-level preconditions, effects, interface, and whole-method relation? If yes, recover a `U.Method` submethod.
2. Does this candidate instead name what happened, when it happened, which resources burned, which component behaved, or which evidence slice was recorded? If yes, use `U.Work`, `TemporalPartOf_work`, `EpisodeOf_work`, `OperationalPartOf_work`, evidence, mechanism, system-component behavior, or method-description constituent under the direct pattern.

Algebraic, graph, categorical, process-calculus, effect-calculus, matrix, embedding, distributed, or neural notation may describe or analyze a selected `MethodRelationStructure@BoundedContext`. That notation is a mathematical or representation lens under `C.29` or a `U.MethodDescription` representation when the description itself is current. Do not name it `U.MethodAlgebra` or treat the lens as the method, method family, work plan, performed work, mechanism, role relation structure, or selector registry.

Do not infer method composition from document modules, graph layout, table order, method-family registry rows, or source-file structure alone. A two-module description is not automatically a two-step method. A path in a graph is not automatically an execution sequence. A pipeline-looking diagram is not automatically dated work. A method-family registry may select among or compose families, but the registry entry is not the method relation structure unless the governing selector or method pattern states that relation by value.

