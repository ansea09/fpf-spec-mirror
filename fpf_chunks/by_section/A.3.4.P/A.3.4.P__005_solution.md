---
chunk_kind: "child"
pattern_id: "A.3.4.P"
pattern_title: "Transformation Wording Repair: Recover Objects and Claims"
section_id: "A.3.4.P:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.4.P/A.3.4.P__005_solution.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "A.3.4.P — Transformation Wording Repair: Recover Objects and Claims"
  - "A.3.4.P:4 — Solution"
line_start: 13242
line_end: 13328
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
  - "F.19"
keywords:
  - "actual subject facts"
  - "and continuity rule"
  - "and other neighboring claims through exact governors"
  - "and routing flow structure"
  - "boundary"
  - "distinguishing performed-work or other direct actor-side claims from differently typed influence sources"
  - "evidence"
  - "method"
  - "publication"
  - "representation"
  - "transformation ontic precision restoration. Repairs change-situation wording by grounding any actual U.Transformation in its changed referent"
  - "work"
---

### A.3.4.P:4 - Solution

Restore the change situation in this order.

1. **Name the working concern.** State what the text is trying to do: identify a change, describe a flow, choose a method, claim evidence, compare architectures, describe functioning, or use a publication.
2. **Test an actual-change claim when one is made.** Under A.3.4, identify the continuing changed subject, temporal extent or formal ordering boundary, boundary conditions, actual characteristic and relation facts, and continuity or reidentification rule. A plan, prediction or assertion alone leaves occurrence unresolved; its content can support occurrence facts when its evidence or derivation use warrants them.
3. **Separate an acting-System claim from influence when either is asserted.** For dated Work, recover each precise performer’s A.13 core and independently admit the Work under A.15.1; add F.6 afterward only for precise attribution to that same assignment. Establish the Work-to-change relation required by the claim separately. A non-Work action needs the System and the participant, operation-application, functioning, causal or other actor-side relation defined by its subject pattern. An influence source keeps its own kind: for example, an organization, toolchain, selected structure or Method. Identify the architecture, Work, communication, constraint or other relation by which that source influences the subject; leave an unsupported claim unresolved.
4. **Recover the neighboring claims the passage needs.** A way of doing, performed Work, a flow structure and evidence for a result require different objects and relations. Use the selection table in 4.2 for those questions.
5. **Use the exact governing relation for each neighboring value.** A neighboring object keeps its own kind and governor; state its current relation to the transformation, changed referent, work, architecture candidate, or receiving use instead of placing it inside a transformation record.
6. **Rewrite after kind and relation recovery.** Keep ordinary domain wording when it conveys the recovered kind and relation unambiguously. Keep quoted source wording within its supported source use. Use F.19 to preserve the complete claim while removing unnecessary apparatus; an unresolved meaning leaves the dependent wording unresolved.
7. **Make the next use recoverable.** The reader should be able to use the identified object or claim under its subject pattern, retain the bounded source use, or recognize the missing basis that limits the claim.

#### A.3.4.P:4.1 - TransformationWordingRepair note

Use this optional note when the receiving use needs an inspectable repair. Fill only the fields needed by that use; an ordinary wording repair can finish in the revised passage.

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
  StopOrReturnCondition:
  BlockedOverread?:
  RemainingReaderUse:
```

`ActualTransformationDisposition` is one of: actual bounded transformation recovered, not a transformation, not recovered, not current for this claim, quote-only source wording, or blocking missing value.

`TransformationWordingRepair` holds wording-repair information. `RetainedUse` identifies the use of the encountered wording that remains; `RemainingReaderUse` names the next action with the recovered object or claim. Include `BlockedOverread?` only for a mistaken interpretation with an independent local ground, a plausible intended reader and an effect on truth, understanding or use under F.19:4. The actor and influence fields describe the claims actually being examined; they introduce no kinds or relations.

Use the actor and influence tests in 4.4 only for the claims represented in those fields.

If an episteme asserts possible, intended, planned, modelled, predicted, or actual change, identify that episteme separately through C.2.1 when the assertion is current. Empirical grounding remains optional and, when current, uses its own exact relation; neither the assertion nor its grounding relation substitutes for the actual transformation basis. Use the governing subject pattern's requirements when creating a project record, gate decision, work plan, or work occurrence.

#### A.3.4.P:4.2 - Subject pattern selection

| If recovery shows... | Use this subject pattern | Keep this boundary |
| --- | --- | --- |
| one actual bounded change under conditions | `A.3.4` | A source label identifies no transformation until the exact changed referent, temporal or formal boundary, boundary conditions, actual subject facts, and continuity or reidentification basis are recoverable. |
| selected structure over transformation loci and adjacent governed values | `E.18` | `TransformationFlowStructure` positions, relates, or locates those loci and values. Selection or common structure membership establishes neither an actual transformation occurrence nor transformation composition, parthood, or partlessness. |
| mathematical expression over a selected structure or formal object | `E.18.2`, `C.29`, `A.6.0`, or the direct formal pattern | Recover project-world work separately under `A.15.1` when the current use also claims it. |
| semantic way of doing | `A.3.1` | Recover the semantic way of doing under `A.3.1`; identify dated work, mechanism, evidence, or transformation claims separately when current. |
| episteme describing a way of doing | `A.3.2` | For example, code, a protocol, a solver model, a proof script, a process model, or a diagram may describe a method. |
| law-governed operation algebra, laws, admissibility predicates, transport, audit, or mechanism-governing-definition assignment | `A.6.1` and `E.20` | Recover the mechanism's defining content under `A.6.1` and `E.20`. |
| planned or dated work | `A.15.2` or `A.15.1` | Identify the plan or dated occurrence under its governing pattern; recover any Method, MethodDescription, transformation-flow structure, or evidence claim separately. |
| pattern-use recommendation, work-entry readiness, language-state move, architecture candidate use, or call-planning next action | The applicable subject pattern; use `E.10.MOVE` when the move-like meaning remains unresolved | Move-like wording is not transformation wording unless a bounded `U.Transformation` or selected `TransformationFlowStructure` is actually current. |
| function-like wording inside a change situation | `A.3.4.P` only to distinguish the actual transformation, selected `TransformationFlowStructure`, a System claimed to act under an exact actor-side relation, a differently typed influence source under its exact relation, boundary binding, or `FunctioningRef?`; use `A.6.F` for detailed function-kind discrimination | For an actual-transformation claim, recover its occurrence basis; for an actor claim, use the performed-Work or non-Work basis in 4.4. |
| state-space and transition-law episteme | `A.3.3` | Dynamics can model possible or claimed change; recover any claimed actual occurrence independently under `A.3.4`. |
| time window, cadence, duration, latency, freshness, currentness, trajectory, inertia, or effort | `C.27.TA`; use `C.27` for temporal-claim adequacy | `C.27.TA` supplies positive temporal subject matter; `C.27` governs temporal-claim adequacy. Recover transformation identity under `A.3.4` when that separate claim is current. |
| evidence, provenance, source, publication, dashboard, view, gate, decision, assurance, result, or release claim | the direct governing evidence, source, publication, gate, decision, assurance, result, or release pattern | A visible record or path does not establish evidence sufficiency, assurance, gate passage, deontic permission, work authorization, release authorization, performed work, or acceptance by itself. |

#### A.3.4.P:4.3 - Common source-label settlements

| Source label | First recovery question | Typical admissible outcomes |
| --- | --- | --- |
| `pipeline` or `dataflow` | Is the current object one transformation, a compound transformation-flow structure, a method description, a work plan, or a publication diagram? | `A.3.4`, `E.18`, `A.3.2`, `A.15.2`, `C.2.P.DR`, or quote-only source wording. |
| `flow` | Is flow the selected structure, a mathematical expression, an actual material, energy, signal, or information flow, or an ordinary source label? | `E.18`, `E.18.2`, `C.29`, direct subject pattern, or quote-only source wording. |
| `network` or `circuit` | Is it a structure form, topology label, mathematical-expression family, functional structure, architecture-selected structure, or subject-domain system? | `E.18`, `E.18.2`, `C.29`, `C.30.ASV`, `A.6.F`, or direct subject pattern. |
| `path` or `slice` | Is it graph path, `PathSlice`, evidence path, carrier path, mathematical path, source quote, or action-route metaphor? | `E.18`, `A.10`, `C.29`, `C.2.P.DR`, carrier wording, source wording, or an explicit stop when no exact current claim is recovered. |
| `workflow` or `process` | Is it method, method description, work plan, dated work, transformation-flow structure, mechanism, or source label? | `A.3.1`, `A.3.2`, `A.15.2`, `A.15.1`, `E.18`, `A.6.1` with `E.20`, or quote-only source wording. |
| `algorithm`, `program`, `solver`, or `proof` | Is it method, method description, formal substrate, mathematical lens, mechanism, work occurrence, evidence, or proof publication? | `A.3.1`, `A.3.2`, `A.6.0`, `C.29`, `A.6.1` with `E.20`, `A.15.1`, `A.10`, `C.2.1`, or the governing publication pattern. |
| `function`, `functional`, or `functioning` | Does the passage claim an actual change, flow structure, action, influence or boundary relation, or does the function-like kind itself remain unresolved? | Use the conditional tests in 4.4 for the claimed relations; use `A.6.F` for remaining function-kind discrimination. |

#### A.3.4.P:4.4 - Functional change-situation settlement

When change-situation wording includes `function`, `functional`, `functioning`, `transforms`, or `implements`, use this pattern only to recover the exact current claims:

- Is one actual bounded `U.Transformation` established by changed referent, temporal or formal boundary, boundary conditions, actual subject facts, and continuity or reidentification?
- Is a selected `TransformationFlowStructure` current without being treated as the acting system or the change occurrence?
- Is performed Work being attributed to a System? Recover each precise performer's A.13 core and independently admit the Work under A.15.1. Add F.6 only when precise assignment-bound attribution is current, then state separately the realization, causal, production, or other Work-to-change relation required by the claim. An assignment occurrence, Work record, common timestamp, or generic transformation-participant fact does not prove performance.
- Is a non-work functional or physical actor-side claim current? Recover the exact system and the participant, operation-application, functioning, causal, or other direct actor-side relation supplied by its governor. If no actor-side governor is recoverable, leave the actor claim unresolved.
- Is a distinct influence source claimed? Recover its kind and influence relation. An organization can be an admitted System, a selected structure remains a structure, and a Method or Method family is not made a holon by its label. Use the architecture, Work, communication, constraint or candidate-synthesis relation the claim needs. System membership and action require their own bases when those claims are made.
- Are exact participant, port, operation-application, relation-signature, or functioning relations current at the boundary? Keep them under their direct governors; a transformation input or output requires its own direct relation.

After recovering the claim, apply `A.6.F` if the function-like kind or relation remains unresolved. Otherwise use the governing subject pattern directly.

#### A.3.4.P:4.5 - Description, publication, and evidence boundary

A diagram or report, for example, may describe a transformation, state a claim about it, provide evidence for that claim, or help compare transformations. When an actual transformation is claimed, recover its subject-side occurrence basis separately. If the description, assertion, or publication is current, use the episteme, publication, source, or declarative-representation pattern; C.2.1 empirical grounding remains an optional separate relation when the use requires it. If the actual transformation is current, keep every description, assertion, publication, and evidence use as an exact neighboring claim.

