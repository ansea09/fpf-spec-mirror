---
chunk_kind: "child"
pattern_id: "B.1.5"
pattern_title: "Gamma_method - Order-Sensitive Method Composition and Work Enactment"
section_id: "B.1.5:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5/B.1.5__003_problem.md"
commit_sha: "43c46859c3926a371fa60cfb1c76aefa19f9eaf9"
heading_path:
  - "B.1.5 — Gamma_method - Order-Sensitive Method Composition and Work Enactment"
  - "B.1.5:2 — Problem"
line_start: 37488
line_end: 37501
dependencies:
  - "A.1"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.22"
  - "A.22.CGUS"
  - "A.3.1"
  - "A.3.2"
  - "A.6.0"
  - "A.6.1"
  - "A.6.RCD"
  - "A.6.REL"
  - "B.1"
  - "B.1.4"
  - "B.1.5"
  - "B.1.6"
  - "B.2"
  - "B.3"
  - "C.13"
  - "C.2.1"
  - "C.29"
  - "E.10"
  - "E.20"
  - "E.24"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.6"
  - "G.5"
  - "U.MethodDescription"
  - "U.PresentationCarrier"
  - "U.Signature"
  - "U.Structure"
  - "U.Work"
keywords:
  - "A.6.RCD claim disposition"
  - "assurance hooks"
  - "capability continuity"
  - "composite-Method boundary account"
  - "method composition"
  - "method relation structure"
  - "method/work granularity"
  - "methodPartOf"
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
4. **Typed joins disappear.** One submethod's intended result is assumed to satisfy the next submethod's precondition without an adapter method, governed correspondence or equivalence, and an explicit failure route.
5. **Interface exposure is hidden.** Callers rely on internal interactions that should be encapsulated, or fail to see interactions that the composite method must expose.
6. **Run-time leakage.** Resources, timestamps, telemetry, performed values, and results are baked into the method instead of remaining occurrence-side facts and separately governed resource, result, and evidence relations.
7. **False whole method.** A method-family registry, fallback table, selector rule, or A.22-selected relation organization is treated as one whole method although no construction or whole identity has been recovered.
8. **Sequence becomes level.** A source list, vertical diagram, curriculum, or first–then account is treated as a subject hierarchy or level structure without an independently established level relation.
9. **Simultaneous contributions become stages.** Methods that contribute during the same bounded Work situation are forced into one before-after chain because the source, presentation, or review visits them one at a time.

