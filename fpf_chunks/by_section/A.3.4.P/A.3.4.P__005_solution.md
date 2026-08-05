---
chunk_kind: "child"
pattern_id: "A.3.4.P"
pattern_title: "Transformation Ontic Precision Restoration"
section_id: "A.3.4.P:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.4.P/A.3.4.P__005_solution.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "A.3.4.P — Transformation Ontic Precision Restoration"
  - "A.3.4.P:4 — Solution"
line_start: 8915
line_end: 9000
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.3.1"
  - "A.3.2"
  - "A.3.3"
  - "A.3.4"
  - "A.6.0"
  - "A.6.1"
  - "A.6.5"
  - "A.6.F"
  - "A.6.M"
  - "C.2.1"
  - "C.2.P.DR"
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "C.30.ASV"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.MOVE"
  - "E.17"
  - "E.18"
  - "E.18.2"
  - "E.20"
  - "E.24"
  - "E.8"
keywords:
---

### A.3.4.P:4 - Solution

Restore the change situation in this order.

1. **Name the working concern.** State what the text is trying to do: identify a change, describe a flow, choose a method, claim evidence, compare architectures, describe functioning, or use a publication.
2. **Test for one actual `U.Transformation`.** Recover the exact changed referent; exact temporal extent or exact ordering boundary in a declared formal substrate; boundary conditions; actual characteristic-state and obtaining direct-relation facts before, during, and after that boundary; and the continuity or reidentification rule that makes this one occurrence at the resolution required by the current use. Possible, intended, planned, modelled, predicted, or merely asserted change remains claim content and identifies no actual transformation until this subject-side basis obtains.
3. **Separate an acting-system claim from influence.** For performed work, recover one exact dated Work occurrence admitted under `U.Work`, the exact covering `U.RoleAssignment`, and direct `performedBy(WorkOccurrenceSlot, RoleAssignmentSlot)`; then recover separately the realization, causal, production, or other exact work-to-change relation required by the current use. Role assignment alone and generic transformation participation prove no action. For a non-work functional or physical actor-side claim, recover the exact system and the participant, operation-application, functioning, causal, or other direct actor-side relation supplied by its governor; otherwise leave the actor claim unresolved. Each manufacturing organization, certification organization, design organization, toolchain, communication system, selected structure, method, method family, or other possible influence source first keeps its exact kind—a method or method family is not a holon by label—and receives only the exact architecture, work, communication, constraint, or candidate-synthesis relation current for the claim.
4. **Test neighboring claims.** Decide whether the wording points to a method, method description, mechanism, work plan, dated work, functioning relation, transformation-flow structure, mathematical description, dynamics episteme, temporal aspect, evidence, source, publication, gate, decision, assurance, result, refresh, reopen relation, or another direct subject claim.
5. **Use the exact governing relation for each neighboring value.** A neighboring object keeps its own kind and governor; state its current relation to the transformation, changed referent, work, architecture candidate, or receiving use instead of placing it inside a transformation record.
6. **Rewrite only after kind and relation recovery.** Keep ordinary wording when it is not FPF-governed, write quote-only source wording when no current use is admitted, or rewrite into the recovered FPF kind and exact relation named by value.
7. **Leave one reader use.** The repaired text must say what the reader may do now: use `A.3.4`, use `E.18`, use `C.29`, use a method, work, mechanism, architecture, or evidence pattern, keep a quote-only cue, or block the stronger claim.

#### A.3.4.P:4.1 - TransformationWordingRepair note

Use this note only when wording is doing FPF-governed work.

```text
TransformationWordingRepair:
  EncounteredWording:
  WorkingConcern:
  RecoveredEntityOfConcern:
  ActualTransformationDisposition:
  TransformationOccurrenceBasis:
  ActingSystemDisposition:
  ArchitectureInfluenceDisposition:
  NeighboringClaimAndExactRelation:
  GoverningPattern:
  RetainedUse:
  BlockedOverread:
  RemainingReaderUse:
```

`ActualTransformationDisposition` is one of: actual bounded transformation recovered, not a transformation, not recovered, not current for this claim, quote-only source wording, or blocking missing value.

`TransformationWordingRepair` is a temporary wording-use restoration aid. Its retained output is the wording to keep or rewrite, the blocked overread, and the next governing-pattern application. `ActingSystemDisposition` and `ArchitectureInfluenceDisposition` are temporary note fields, not FPF kinds or universal relations. An actual transformation occurrence is grounded only through its subject-side occurrence basis.

For performed work, an acting-system claim needs one exact dated Work occurrence admitted under `U.Work`, the exact covering `U.RoleAssignment`, direct `performedBy(WorkOccurrenceSlot, RoleAssignmentSlot)`, and the separately governed realization, causal, production, or other work-to-change relation required by the use. For a non-work actor-side claim, use an exact participant, operation-application, functioning, causal, or other direct relation supplied by its governor. If no such relation is recoverable, keep the actor claim unresolved. Every influence source retains its exact kind and only its current architecture, work, communication, constraint, or candidate-synthesis relation; influence establishes no acting fact by itself.

If an episteme asserts possible, intended, planned, modelled, predicted, or actual change, identify that episteme separately through C.2.1 when the assertion is current. Empirical grounding remains optional and, when current, uses its own exact relation; neither the assertion nor its grounding relation substitutes for the actual transformation basis. Project records, gate decisions, work plans, and work occurrences are created only by their direct governing patterns.

#### A.3.4.P:4.2 - Direct governing-pattern selection

| If recovery shows... | Use this governing pattern | Keep this boundary |
| --- | --- | --- |
| one actual bounded change under conditions | `A.3.4` | A source label identifies no transformation until the exact changed referent, temporal or formal boundary, boundary conditions, actual subject facts, and continuity or reidentification basis are recoverable. |
| selected structure over transformation loci and adjacent governed values | `E.18` | `TransformationFlowStructure` positions, relates, or locates those loci and values. Selection or common structure membership establishes neither an actual transformation occurrence nor transformation composition, parthood, or partlessness. |
| mathematical expression over a selected structure or formal object | `E.18.2`, `C.29`, `A.6.0`, or the direct formal pattern | A graph, morphism, category, algebra, path, network expression, or circuit expression is not project-world work by notation. |
| semantic way of doing | `A.3.1` | Method is not dated work, mechanism, evidence, or transformation occurrence by label. |
| episteme describing a way of doing | `A.3.2` | Code, protocol, solver model, proof script, process model, or diagram may describe a method without being the method or the work. |
| law-governed operation algebra, laws, admissibility predicates, transport, audit, or mechanism-governing-definition assignment | `A.6.1` and `E.20` | Mechanism is not selected by a prestigious "algorithm", "process", or "mechanism" word. |
| planned or dated work | `A.15.2` or `A.15.1` | Plan and work occurrence are not method, method description, transformation-flow structure, or evidence by appearance. |
| pattern-use recommendation, work-entry readiness, language-state move, architecture candidate use, or call-planning next action | `E.10.MOVE` first, then `E.11.PUR`, `A.15.5`, `A.16`, `C.30`, `C.24`, or the direct governing pattern | Move-like wording is not transformation wording unless a bounded `U.Transformation` or selected `TransformationFlowStructure` is actually current. |
| function-like wording inside a change situation | `A.3.4.P` only to distinguish the actual transformation, selected `TransformationFlowStructure`, a system claimed to act under an exact actor-side governor, a differently typed influence source under its exact relation, boundary binding, or `FunctioningRef?`; use `A.6.F` for detailed function-kind discrimination | A function word, role assignment, generic participant fact, module allocation, architecture locus, toolchain, or organization establishes neither the actual transformation nor action by label. |
| state-space and transition-law episteme | `A.3.3` | Dynamics can model possible or claimed change; it is not the transformation itself. |
| time window, cadence, duration, latency, freshness, currentness, trajectory, inertia, or effort | `C.27.TA`; use `C.27` for temporal-claim adequacy | Temporal aspect is not the whole transformation and temporal-claim adequacy is not positive temporal subject matter. |
| evidence, provenance, source, publication, dashboard, view, gate, decision, assurance, result, or release claim | the direct governing evidence, source, publication, gate, decision, assurance, result, or release pattern | A visible record or path does not establish evidence sufficiency, assurance, gate passage, deontic permission, work authorization, release authorization, performed work, or acceptance by itself. |

#### A.3.4.P:4.3 - Common source-label settlements

| Source label | First recovery question | Typical admissible outcomes |
| --- | --- | --- |
| `pipeline` or `dataflow` | Is the current object one transformation, a compound transformation-flow structure, a method description, a work plan, or a publication diagram? | `A.3.4`, `E.18`, `A.3.2`, `A.15.2`, `C.2.P.DR`, or quote-only source wording. |
| `flow` | Is flow the selected structure, a mathematical expression, an actual material, energy, signal, or information flow, or an ordinary source label? | `E.18`, `E.18.2`, `C.29`, direct subject pattern, or quote-only source wording. |
| `network` or `circuit` | Is it a structure form, topology label, mathematical-expression family, functional structure, architecture-selected structure, or subject-domain system? | `E.18`, `E.18.2`, `C.29`, `C.30.ASV`, `A.6.F`, or direct subject pattern. |
| `path` or `slice` | Is it graph path, `PathSlice`, evidence path, carrier path, mathematical path, source quote, or action-route metaphor? | `E.18`, `A.10`, `C.29`, `C.2.P.DR`, carrier wording, source wording, or blocked overread. |
| `workflow` or `process` | Is it method, method description, work plan, dated work, transformation-flow structure, mechanism, or source label? | `A.3.1`, `A.3.2`, `A.15.2`, `A.15.1`, `E.18`, `A.6.1` with `E.20`, or quote-only source wording. |
| `algorithm`, `program`, `solver`, or `proof` | Is it method, method description, formal substrate, mathematical lens, mechanism, work occurrence, evidence, or proof publication? | `A.3.1`, `A.3.2`, `A.6.0`, `C.29`, `A.6.1` with `E.20`, `A.15.1`, `A.10`, `C.2.1`, or the governing publication pattern. |
| `function`, `functional`, or `functioning` | Is the current claim about an actual `U.Transformation`, selected `TransformationFlowStructure`, a performed-work or non-work actor under an exact direct governor, a separately typed influence source, boundary binding, or `FunctioningRef?`; or is the word asking for function-kind discrimination? | Use `A.3.4` or `E.18` for transformation-side recovery; use one exact Work occurrence admitted under `U.Work` plus `performedBy` and a separate work-to-change relation for performed work, or another exact participant, operation-application, functioning, causal, or direct actor-side relation; keep every influence source under its own kind and exact relation; use `A.6.F` for function-kind discrimination. |

#### A.3.4.P:4.4 - Functional change-situation settlement

When change-situation wording includes `function`, `functional`, `functioning`, `transforms`, or `implements`, use this pattern only to recover the exact current claims:

- Is one actual bounded `U.Transformation` established by changed referent, temporal or formal boundary, boundary conditions, actual subject facts, and continuity or reidentification?
- Is a selected `TransformationFlowStructure` current without being treated as the acting system or the change occurrence?
- Is performed work being attributed to a system? Recover the exact dated Work occurrence admitted under `U.Work`, exact covering `U.RoleAssignment`, and direct `performedBy(WorkOccurrenceSlot, RoleAssignmentSlot)`. Then state separately the realization, causal, production, or other exact work-to-change relation required by the claim. A role assignment, work record, common timestamp, or generic transformation-participant fact does not prove performance.
- Is a non-work functional or physical actor-side claim current? Recover the exact system and the participant, operation-application, functioning, causal, or other direct actor-side relation supplied by its governor. A changed referent, resource, port-bound object, module, or other participant is not an actor merely because it participates. If no actor-side governor is recoverable, leave the actor claim unresolved.
- Is a distinct influence source current? First recover its exact kind. A manufacturing, certification, or design organization may be a system under its direct governor; a toolchain or communication system needs its own admitted kind; a selected structure remains a structure; and a method or method family is not a holon by label. State only the exact architecture, work, communication, constraint, or candidate-synthesis relation current for that value. Influence alone establishes no role, work, actor status, or transformation participation.
- Are exact participant, port, operation-application, relation-signature, or functioning relations current at the boundary? Use their direct governors; do not turn them into generic transformation inputs or outputs.

Do not introduce a `TransformerHolon` kind, a generic transformer role, or a universal architecture-influence relation to bridge these claims. After recovery, apply `A.6.F` when the question is which function-like kind or relation is being claimed. `A.3.4.P` selects the direct governor; it does not infer mathematical function, software routine, capability, quality, work, method, architecture allocation, evidence, assurance, gate, or decision from functional wording.

#### A.3.4.P:4.5 - Description, publication, and evidence boundary

A diagram, model, dashboard, report, source span, proof, graph, or publication may describe, assert, evidence, or help compare a transformation. It is not the transformation and does not supply its subject-side occurrence basis. If the description, assertion, or publication is current, use the episteme, publication, source, or declarative-representation pattern; C.2.1 empirical grounding remains an optional separate relation when the use requires it. If the actual transformation is current, keep every description, assertion, publication, and evidence use as an exact neighboring claim.

