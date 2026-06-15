---
chunk_kind: "child"
pattern_id: "C.2.P.DR"
pattern_title: "Declarative Representation Precision Restoration"
section_id: "C.2.P.DR:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.P.DR/C.2.P.DR__006_solution.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "C.2.P.DR — Declarative Representation Precision Restoration"
  - "C.2.P.DR:4 — Solution"
line_start: 38500
line_end: 38591
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.15.4"
  - "A.19.SPR"
  - "A.20"
  - "A.21"
  - "A.3.1"
  - "A.3.2"
  - "A.6.0"
  - "A.6.1"
  - "A.7"
  - "B.3"
  - "C.2.P"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.20"
  - "E.8"
  - "F.19"
keywords:
---

### C.2.P.DR:4 - Solution

Repair declarative-representation overread by recovering representation use, then naming the direct governing pattern for the current claim.

The repair order is:

1. **Name the encountered representation.** Quote or identify the graph, path, query, predicate, dashboard, table, publication face, evidence path, source-chain relation, carrier path, mathematical representation, method-description representation, or pattern relation.
2. **Name the representation kind.** State whether it is graph structure, flow valuation, evidence relation, provenance relation, state predicate, query, table, publication face, formal substrate, method description, source relation, carrier syntax, or another representation kind named by value.
3. **Name the represented EntityOfConcern or claim.** State what the representation is about: claim, effect, method, work occurrence, work plan, graph object, state, EntityOfConcern, publication, evidence relation, gate, source relation, or pattern relation.
4. **Recover source or publication relation when current.** If the representation is a face, source chain, generated explanation, copied text, dashboard, file path, or publication unit, use the publication pattern or source-use pattern governing that relation.
5. **Name the tempting imperative overread.** Say what the representation is being asked to do by resemblance: route, call, dispatch, invoke, run, flow, send, receive, authorize, release, prove, prescribe, execute, select, pass a gate, or record work.
6. **Select the governing pattern.** Use the direct pattern when the kind is already recovered; otherwise use this pattern only long enough to recover the representation use and blocked overread.
7. **State retained use.** Keep the weaker useful use: graph structure, evidence relation, source-finding, state predicate, publication face, method-description representation, formal-substrate input, method slot candidate, or pattern relation.
8. **State blocked overread.** Block only the stronger claim that is not recoverable.
9. **Stop or reopen.** Stop when the governing pattern can carry the next claim. Before stopping, ask what claim, evidence relation, gate relation, safety relation, method relation, work relation, or source relation would become less reviewable if the visible representation were accepted as the stronger claim. Reopen if a later source changes representation kind, represented EntityOfConcern, source currentness, governing pattern, or the intended use.

#### C.2.P.DR:4.1 - DeclarativeRepresentationRepair note

Use this compact note when the wording has FPF-governed use:

```text
DeclarativeRepresentationRepair:
  EncounteredRepresentation:
  RepresentationKind:
  RepresentedEntityOfConcernOrClaim:
  SourceOrPublicationRelation:
  TemptingImperativeOverread:
  RecoveredGoverningPattern:
  RetainedUse:
  BlockedOverread:
  StopOrReopenCondition:
```

The note records the local repair long enough to make the next governing pattern selectable. If the direct governing pattern already supplies a better record, use that record and keep only the repaired wording, retained use, blocked overread, and stop or reopen condition here.

#### C.2.P.DR:4.2 - Direct governing-pattern selection

| If recovery shows... | Use this governing pattern | Keep this boundary |
| --- | --- | --- |
| graph object, graph path, `PathSlice`, crossing, flow valuation, transformation-flow structure relation, or graph expression over that structure | `E.18`, `E.18.2`, or `E.18.1` when P2W carry-through is current | Graph structure or path structure is not work route, method narrative, evidence result, or pattern dispatch by layout. |
| evidence relation or provenance relation for a claim, effect, or reliance use | `A.10` | Evidence path is not approval, permission, gate passage, release, safety, work occurrence, or assurance by itself. |
| state, status value, readiness, validity, or predicate-like value whose bearer and value frame is hidden | `A.19.SPR` or the direct status-value or state-value pattern | A predicate or state-like value is not a workflow, gate, or proof unless the governing pattern says so. |
| publication face, source expression, generated explanation, dashboard face, publication unit, or source-chain relation | `E.17`, `E.17.EFP`, `C.2.P`, `A.15.4`, or source-use pattern named by value | Publication and source visibility do not create work, evidence, authority, release, or gate passage. |
| mathematical representation, formal object, formal substrate, invariant, or mathematical-lens output | `A.6.0`, `C.29`, or direct mathematical pattern | Mathematical representation is not method, mechanism, proof of project result, or work execution until that claim is separately recovered. |
| context-local semantic way of doing | `A.3.1 U.Method` | A method claim is not closed by code, diagram, proof script, plan, run, or mechanism declaration; use `E.10.ARCH:3.1` only to recover the project concern and then recover each linked typed value under its own governing pattern. |
| episteme describing a method: code, SOP, proof script, solver model, process model, protocol, recipe, or diagram | `A.3.2 U.MethodDescription` | Description is not the method itself and not dated work. |
| law-governed operation algebra, laws, admissibility predicates, transport, audit, realization, or governing-definition assignment | `A.6.1` and `E.20` | Mechanism meaning is not selected by saying "algorithm" or "method"; it needs mechanism fields. |
| planned work, intended window, role requirements, resource budget, or acceptance criterion | `A.15.2 U.WorkPlan` | Plan is not method, method description, evidence, gate passage, or performed work. |
| dated work occurrence, run trace, concrete parameter binding, result, resource use, or performed-work record | `A.15.1 U.Work` | Work occurrence is not a diagram, plan, method description, source cue, or evidence path by appearance. |
| FPF pattern application, pattern relation, neighboring-pattern relation, or placement cue | `E.8`, `F.19`, `E.10.ARCH`, or the direct pattern relation named by value | Pattern relations are declarative references or applications, not exits, receivers, routes, calls, owners, homes, or dispatches. |
| quoted source wording or ordinary navigation | quote-only or ordinary prose | Do not repair ordinary words into FPF terms when no FPF-governed claim is being made. |

#### C.2.P.DR:4.3 - Legitimate path and route settlement

`path` is not banned.

`A.10 evidence path for <claim, effect, or use>` is legitimate when the evidence relation or provenance relation for the named claim, effect, or reliance use is current. `E.18` graph path and `PathSlice` are legitimate when the graph object, path, slice, crossing, or flow valuation is current. Carrier file paths, URLs, mathematical paths, and quoted source paths are legitimate when their notation or source role is current.

The defect is not the word. The defect is hidden ontology: the sentence treats a representation as if something literally ran, flowed, executed, authorized, released, proved, selected, or prescribed action without the governing kind named by value.

#### C.2.P.DR:4.4 - Method, algorithm, mechanism, and work-slot settlement

Do not repair `algorithm`, `program`, `solver`, `proof`, `recipe`, `method`, `workflow`, `process`, `procedure`, `access path`, `query plan`, or `control strategy` by choosing one fashionable replacement.

Recover the current slot or use-position:

| Current claim | Governing pattern |
| --- | --- |
| context-local semantic way of doing, transformation kind, or enactment kind | `A.3.1 U.Method` |
| episteme describing that way | `A.3.2 U.MethodDescription` |
| formal substrate, signature, postulates, laws, or mathematical declaration | `A.6.0`; use `C.29` when mathematical-lens use is current |
| operation algebra, admissibility predicates, transport, audit, realization, or mechanism-governing-definition assignment | `A.6.1` and `E.20` |
| planned work | `A.15.2 U.WorkPlan` |
| dated performed work | `A.15.1 U.Work` |
| evidence relation or provenance relation for a claim | `A.10` |
| wording quoted from source with no FPF-governed use | quote-only source wording |

When the source label hides method, mechanism, formal-substrate, work, evidence, gate, result, or temporal assignments, use `E.10.ARCH:3.1` to recover the project concern and the current relation position. For this host, recover only the representation overread and the direct governing pattern for the current claim; linked typed values remain under their own governing patterns rather than becoming one representation-repair claim.

#### C.2.P.DR:4.5 - Programming-paradigm and process-model settlement

Imperative, functional, logical, constraint, object-centric event, effect-handler, pipeline, orchestration, Declare-style, SQL-like, e-graph, hypergraph, or process-mining wording is a cue to recover representation kind and FPF slot. It is not a decision procedure by itself.

Current practice makes the old contrast between imperative and declarative labels too weak as a final ontology:

- constructor and process-theory lines keep computation, information, dynamics, and procedure close to possible or impossible transformations and compositional realization;
- scoped effects and handlers separate operation syntax, semantic handling, scopes, resources, equations, type information, and effect information;
- Declare-style process models and object-centric event logs distinguish constraints, events, objects, relations, ingestion, transformation, storage, and analysis;
- e-graph and monoidal-rewriting work shows that computation or process representation may be equivalence or composition structure rather than instruction order.

Use those lines as guardrails: recover the FPF kind and slot instead of replacing one programming-paradigm label with another.

