---
chunk_kind: "child"
pattern_id: "A.3.4.P"
pattern_title: "Transformation Ontic Precision Restoration"
section_id: "A.3.4.P:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.4.P/A.3.4.P__005_solution.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "A.3.4.P — Transformation Ontic Precision Restoration"
  - "A.3.4.P:4 — Solution"
line_start: 7485
line_end: 7559
dependencies:
  - "A.10"
  - "A.15"
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
  - "B.3"
  - "C.2.1"
  - "C.2.P.DR"
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "E.18"
  - "E.18.2"
  - "E.20"
  - "E.24"
  - "E.8"
  - "F.18"
  - "F.19"
keywords:
---

### A.3.4.P:4 - Solution

Restore the change situation in this order.

1. **Name the working concern.** State what the text is trying to do: identify a change, describe a flow, choose a method, claim evidence, compare architectures, describe functioning, or use a publication.
2. **Test for `U.Transformation`.** If one bounded change is current, fill the `A.3.4` identity slots: transformed object, bounded context, initial condition, post-state or delta, transformation relation, boundary or admissibility condition, and temporal or ordering reference when relevant.
3. **Test for neighboring slots.** Decide whether the wording points to a transformer-side system or holon, method, method description, mechanism, work plan, dated work, functioning relation, transformation-flow structure, mathematical description, dynamics episteme, temporal aspect, evidence, source, publication, gate, decision, assurance, result, refresh, or reopen relation.
4. **Use the governing pattern for each filled value.** The slot may belong to the transformation ontic; the filler keeps its own kind and governing pattern.
5. **Rewrite only after kind recovery.** Keep ordinary wording when it is not FPF-governed, write quote-only source wording when no current use is admitted, or rewrite into the recovered FPF kind and relation named by value.
6. **Leave one reader move.** The repaired text must say what the reader may do now: use `A.3.4`, use `E.18`, use `C.29`, use a method, work, or mechanism pattern, keep a quote-only cue, or block the stronger claim.

#### A.3.4.P:4.1 - TransformationWordingRepair note

Use this note only when wording is doing FPF-governed work.

```text
TransformationWordingRepair:
  EncounteredWording:
  WorkingConcern:
  RecoveredEntityOfConcern:
  TransformationCoreDisposition:
  RecoveredSlotOrNeighboringValue:
  GoverningPattern:
  RetainedUse:
  BlockedOverread:
  RemainingReaderMove:
```

`TransformationCoreDisposition` is one of: bounded transformation recovered, not a transformation, not recovered, not current for this claim, quote-only source wording, or blocking missing value.

`TransformationWordingRepair` is a temporary wording-use restoration aid. Its retained output is the wording to keep or rewrite, the blocked overread, and the next governing-pattern application. Project records, evidence relations, gate decisions, work plans, and work occurrences are created only by the governing pattern selected in the note.

#### A.3.4.P:4.2 - Direct governing-pattern selection

| If recovery shows... | Use this governing pattern | Keep this boundary |
| --- | --- | --- |
| one bounded change under conditions | `A.3.4` | A source label does not identify the transformation until the identity slots are recoverable. |
| selected compound structure over transformations and adjacent loci | `E.18` | A flow, path, network, circuit, mesh, chain, loop, or pipeline is a structure form only when the selected structure is current. |
| mathematical expression over a selected structure or formal object | `E.18.2`, `C.29`, `A.6.0`, or the direct formal pattern | A graph, morphism, category, algebra, path, network expression, or circuit expression is not project-world work by notation. |
| semantic way of doing | `A.3.1` | Method is not dated work, mechanism, evidence, or transformation occurrence by label. |
| episteme describing a way of doing | `A.3.2` | Code, protocol, solver model, proof script, process model, or diagram may describe a method without being the method or the work. |
| law-governed operation algebra, laws, admissibility predicates, transport, audit, or mechanism-governing-definition assignment | `A.6.1` and `E.20` | Mechanism is not selected by a prestigious "algorithm", "process", or "mechanism" word. |
| planned or dated work | `A.15.2` or `A.15.1` | Plan and work occurrence are not method, method description, transformation-flow structure, or evidence by appearance. |
| function-like wording inside a change situation | `A.3.4.P` only to decide whether `U.Transformation`, `TransformationFlowStructure`, transformer-side filler, input boundary, output boundary, or `FunctioningRef?` is current; use `A.6.F` for detailed function-kind discrimination | A function word does not decide the transformation, bearer, mathematical function, software routine, module allocation, or architecture view by label. |
| state-space and transition-law episteme | `A.3.3` | Dynamics can model possible or claimed change; it is not the transformation itself. |
| time window, cadence, duration, latency, freshness, currentness, trajectory, inertia, or effort | `C.27.TA`; use `C.27` for temporal-claim adequacy | Temporal aspect is not the whole transformation and temporal-claim adequacy is not positive temporal subject matter. |
| evidence, provenance, source, publication, dashboard, view, gate, decision, assurance, result, or release claim | the direct governing evidence, source, publication, gate, decision, assurance, result, or release pattern | A visible record or path does not prove, permit, enact, or accept the change by itself. |

#### A.3.4.P:4.3 - Common source-label settlements

| Source label | First recovery question | Typical admissible outcomes |
| --- | --- | --- |
| `pipeline` or `dataflow` | Is the current object one transformation, a compound transformation-flow structure, a method description, a work plan, or a publication diagram? | `A.3.4`, `E.18`, `A.3.2`, `A.15.2`, `C.2.P.DR`, or quote-only source wording. |
| `flow` | Is flow the selected structure, a mathematical expression, an actual material, energy, signal, or information flow, or an ordinary source label? | `E.18`, `E.18.2`, `C.29`, direct subject pattern, or quote-only source wording. |
| `network` or `circuit` | Is it a structure form, topology label, mathematical-expression family, functional structure, architecture-selected structure, or subject-domain system? | `E.18`, `E.18.2`, `C.29`, `C.30.ASV`, `A.6.F`, or direct subject pattern. |
| `path` or `slice` | Is it graph path, `PathSlice`, evidence path, carrier path, mathematical path, source quote, or action-route metaphor? | `E.18`, `A.10`, `C.29`, `C.2.P.DR`, carrier wording, source wording, or blocked overread. |
| `workflow` or `process` | Is it method, method description, work plan, dated work, transformation-flow structure, mechanism, or source label? | `A.3.1`, `A.3.2`, `A.15.2`, `A.15.1`, `E.18`, `A.6.1` with `E.20`, or quote-only source wording. |
| `algorithm`, `program`, `solver`, or `proof` | Is it method, method description, formal substrate, mathematical lens, mechanism, work occurrence, evidence, or proof publication? | `A.3.1`, `A.3.2`, `A.6.0`, `C.29`, `A.6.1` with `E.20`, `A.15.1`, `A.10`, `C.2.1`, or the governing publication pattern. |
| `function`, `functional`, or `functioning` | Is the change-situation question about `U.Transformation`, `TransformationFlowStructure`, transformer-side filler, input boundary, output boundary, or `FunctioningRef?`; or is the word asking for function-kind discrimination? | Use `A.3.4` or `E.18` for the transformation-side recovery; use `A.6.F` for function-kind discrimination; use the direct governing pattern when another kind is already recovered. |

#### A.3.4.P:4.4 - Functional transformer settlement

When change-situation wording includes `function`, `functional`, or `functioning`, use this pattern only for the transformation-side recovery:

- Is one bounded `U.Transformation` current?
- Is a `TransformationFlowStructure` current?
- Is the current value a transformer-side filler such as a system, holon, module, bearer, allocation locus, interface, port, or signature-side value?
- Is the current value an input boundary, output boundary, or `FunctioningRef?` for transformation behavior under conditions?

After that recovery, apply `A.6.F` when the question is which function-like kind or relation is being claimed. `A.3.4.P` does not decide mathematical function, software routine, capability, quality, role, work, method, module allocation, evidence use, assurance use, gate use, or decision use except by selecting the governing pattern that owns the recovered value.

#### A.3.4.P:4.5 - Description, publication, and evidence boundary

A diagram, model, dashboard, report, source span, proof, graph, or publication may describe, evidence, or help compare a transformation. It is not the transformation. If the current object is the description or publication, use the episteme, publication, source, or declarative-representation pattern. If the current object is the transformation, keep the description or publication as a neighboring value and state the evidence use, description use, or comparison use separately.

