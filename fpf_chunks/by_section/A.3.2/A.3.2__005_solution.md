---
chunk_kind: "child"
pattern_id: "A.3.2"
pattern_title: "U.MethodDescription: Description Episteme for a Way of Doing"
section_id: "A.3.2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.2/A.3.2__005_solution.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "A.3.2 — U.MethodDescription: Description Episteme for a Way of Doing"
  - "A.3.2:4 — Solution"
line_start: 6303
line_end: 6399
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.3"
  - "A.3.1"
  - "B.3"
  - "C.2.P.DR"
  - "C.28"
  - "E.10"
  - "E.10.ARCH"
  - "F.18"
  - "U.BoundedContext"
  - "U.Method"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "SOP"
  - "U.Episteme"
  - "code"
  - "model"
  - "recipe"
  - "specification"
---

### A.3.2:4 - Solution

#### A.3.2:4.1 - Definition

`U.MethodDescription` is an `U.Episteme` that describes a `U.Method` in a representation such as text, code, diagram, model, rule set, proof script, protocol, or executable form.

A method description is not the method, not the work occurrence, not the work plan, not the performer, not the capability, not the mechanism, not the formal substrate, and not the evidence relation. A system in a transformer-like role may enact a method during `U.Work` while using a method description, but the description itself does not enact anything.

Working distinction:

| Claim being made | Governing pattern |
| --- | --- |
| context-defined semantic way of doing | `A.3.1 U.Method` |
| representation that describes that way of doing | `A.3.2 U.MethodDescription` |
| selected formal object, invariant, substrate, or mathematical declaration | `A.6.0`, `C.29`, or another direct mathematical pattern |
| law-governed operation structure, admissibility predicate set, transport, or realization relation | `A.6.1`, with `E.20` when mechanism meaning is introduced or revised |
| planned dated work, work preparation, schedule, or launch value | `A.15.2 U.WorkPlan` plus gate or authority patterns when a gate or authority claim is current |
| dated occurrence with witnesses, logs, measurements, and outputs | `A.15.1 U.Work` |
| evidence relation or provenance relation for a claim, effect, or use | `A.10`, `B.3`, `G.6`, or the direct evidence pattern or assurance pattern |

#### A.3.2:4.2 - Representation-agnostic stance

`U.MethodDescription` does not privilege imperative procedures or software code. A method description can be written as:

* an SOP, checklist, BPMN diagram, PLC ladder, shell script, or operational protocol;
* functional composition, typed pipeline, process model, state machine, or event rule set;
* SAT, SMT, MILP, theorem-prover, proof-assistant, or constraint-model file;
* statistical or ML training, evaluation, inference, or deployment description;
* lab protocol, clinical guideline, control recipe, or organizational rule set;
* a hybrid form that combines several representations.

These forms are `U.MethodDescription` only when the current claim is that they describe a method. A solver formulation may also expose a formal substrate. A program run may be `U.Work`. A mechanism card may declare laws and admissibility predicates. A proof may be evidence for a claim. A workflow diagram may describe a method or a work plan depending on the fields it actually states. Representation style alone does not decide the FPF kind.

#### A.3.2:4.3 - Method-description fields

A useful method description usually makes these fields recoverable in the current bounded context:

| Field | What to recover |
| --- | --- |
| Method described | the named `U.Method` and the bounded context where the name has meaning |
| Inputs and outputs | accepted inputs, produced outputs, resources, interfaces, ports, and relevant standards |
| Preconditions | states, guards, invariants, input conditions, and required environmental conditions |
| Effects | postconditions, guaranteed effects, produced result kinds, and failure semantics |
| Bounds | latency, precision, cost, safety envelope, reliability, uncertainty, or other local bounds |
| Role and capability requirements | role kinds and capability thresholds required for enactment, not named people |
| Parameters | values that may vary across work occurrences, defaults, ranges, and binding time |
| Acceptance criteria | how a work occurrence or result is judged against the method description |
| Variants and refinement | declared deltas, preserved interface, strengthened preconditions or effects, and identity criterion |
| Source and edition | publication, file, document, or source relation when reliance depends on a version |

Calendars, assignees, work authorization, gate passage, and dated execution witnesses are not part of the method-description claim. They may cite the method description, but they are governed elsewhere.

#### A.3.2:4.4 - Method-description acceptance and use boundaries

A method description may be accepted, regulated, preferred, deprecated, or forbidden in a bounded context. That is a separate publication, gate, authority, or policy claim. The acceptance label does not turn the description into work, evidence, a gate decision, or a mechanism.

When a method description is used to prepare or enact work, keep the chain explicit:

1. `U.MethodDescription` describes `U.Method`.
2. `U.WorkPlan` may cite that description when preparing dated work.
3. A system in a role assignment enacts the method during `U.Work`.
4. Work outputs, logs, traces, measurements, or publications may become evidence only through the governing evidence or assurance pattern.

#### A.3.2:4.5 - Method, mechanism, and formal-substrate boundary

Do not decide method, mechanism, or formal substrate by the surface word. When a source expression names changing, producing, selecting, deriving, controlling, or maintaining an `EntityOfConcern`, use `E.10.ARCH:3.1` to recover the project concern first and then assign separately governed typed FPF values.

For this host, keep the local question thin: is the current claim an episteme that describes a method? If the same source expression also raises method, mechanism, formal-substrate, work-plan, dated-work, evidence, source, gate, result, publication, or temporal claims, keep those values linked only by explicit relation positions and apply their own governing patterns.

The local position checks are:
* In **method-description position**, the claim is that a representation describes a method.
* In **method position**, the claim is the context-defined semantic way of doing.
* In **formal-substrate position**, the claim is the selected formal object, structure, invariant, or mathematical declaration used for reasoning.
* In **mechanism position**, the claim is the law-governed operation algebra, law set, admissibility predicates, applicability, transport, audit surface, or realization relation.
* In **work position**, the claim is a dated occurrence with witnesses and outputs.

Those links remain typed relation-position links to separately governed claims. Do not assign the same typed value as both `U.Method` and `U.Mechanism` unless a governing pattern explicitly admits such dual typing; a slot-position label names the relation position, not a new ontology.

Example: a MILP file can describe a scheduling method; the mathematical formulation can be a formal substrate; a selector mechanism can declare admissible selection operations over candidate methods; a scheduled solver run is work; the resulting production schedule can become evidence for a separate claim. Those claims may be linked, but one does not close the others.

#### A.3.2:4.6 - Constructor and process-theory note

In the constructor-theory and process-theory interpretation used by this campaign, both informational and physical procedures are understood through possible or impossible transformations. That motivates a broad method-description kind without making software code privileged:

* a program, proof script, or solver model may describe a method for information transformation;
* an SOP, lab protocol, or control recipe may describe a method for material, energetic, organizational, or mixed transformation;
* a method description can be used by a system in a transformer-like role during work;
* a mechanism may declare law-governed operation structure for transformations, but that mechanism claim is separate from the method-description claim.

This note is not a license to call every algorithm-looking expression a method description. It only explains why FPF can treat many representation forms uniformly after the current slot is recovered.

#### A.3.2:4.7 - Declarative representation boundary

Some method descriptions use declarative representations: constraint sets, graph patterns, state predicates, SQL-like queries, policy rules, e-graphs, monoidal diagrams, or process constraints. Do not translate such representations into an imperative route unless the method claim actually states an ordered action structure.

If the source turns a graph path, evidence path, query plan, predicate, checklist, publication face, or pattern relation into a route, dispatch, call sequence, receiver path, or work workflow by metaphor, apply `C.2.P.DR` before assigning the direct governing pattern.

