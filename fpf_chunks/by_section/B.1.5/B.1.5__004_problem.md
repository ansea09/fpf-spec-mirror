---
chunk_kind: "child"
pattern_id: "B.1.5"
pattern_title: "Gamma_method - Order-Sensitive Method Composition and Work Enactment"
section_id: "B.1.5:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5/B.1.5__004_problem.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "B.1.5 — Gamma_method - Order-Sensitive Method Composition and Work Enactment"
  - "B.1.5:2 — Problem"
line_start: 35785
line_end: 35796
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

### B.1.5:2 - Problem

Without B.1.5:

1. **Source-wording composition.** "Step", "stage", "activity", "task", "procedure", "workflow", "pipeline", or "algorithm" wording is accepted as method composition without recovering the actual objects.
2. **Description-as-method.** A workflow diagram, BPMN model, code repository, proof script, table, checklist, or graph path is treated as the composite method itself.
3. **Order as mereology.** `SerialStepOf`, `ParallelFactorOf`, guarded choice, or fallback relation is placed in a structural part-whole chain.
4. **Typed joins disappear.** One submethod's output is assumed to satisfy the next submethod's precondition without an adapter, bridge, conversion, or declared equivalence.
5. **Interface exposure is hidden.** Callers rely on internal interactions that should be encapsulated, or fail to see interactions that the composite method must expose.
6. **Run-time leakage.** Resources, timestamps, telemetry, performed values, and outcomes are baked into the method instead of being recorded on `U.Work`.
7. **False whole method.** A method-family registry, fallback table, selector rule, or local relation structure is treated as one whole method although no whole-method identity has been recovered.

