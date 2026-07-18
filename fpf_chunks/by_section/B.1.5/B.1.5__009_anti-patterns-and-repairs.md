---
chunk_kind: "child"
pattern_id: "B.1.5"
pattern_title: "Gamma_method - Order-Sensitive Method Composition and Work Enactment"
section_id: "B.1.5:7"
section_title: "Anti-Patterns And Repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5/B.1.5__009_anti-patterns-and-repairs.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "B.1.5 — Gamma_method - Order-Sensitive Method Composition and Work Enactment"
  - "B.1.5:7 — Anti-Patterns And Repairs"
line_start: 33866
line_end: 33886
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

### B.1.5:7 - Anti-Patterns And Repairs

| Anti-pattern | Repair |
| --- | --- |
| "The workflow diagram is the composite method." | First govern the diagram as `U.MethodDescription`; admit a composite `U.Method` only after recovered submethods and whole-forming relations are named. |
| "Step A is part of the method because it is a box." | Recover whether the box denotes a `U.Method`, description node, plan item, work occurrence, relation edge, or lens expression. |
| "Parallel branches can join because the picture rejoins." | State the typed join, adapter, or equivalence relation; otherwise the composite method is not admitted. |
| "The selector table is the method." | Use `G.5` or `MethodRelationStructure@BoundedContext` unless one whole method with whole-level commitments is recovered. |
| "The run proved the method structure." | Record the run as `U.Work` and evidence separately; use it as evidence only through the governing evidence or assurance relation. |
| "The phase is a method step." | Use phase or temporal relation discipline for carrier phases and use B.2 only when the phase boundary changes whole identity, supervision, closure, or context. |
| "The join improves throughput, so the method has emergence." | First name critical path, cutsets, typed joins, and CL-sensitive mappings for assurance; open B.2 only when the whole-level reidentification claim remains. |
| "The MIC is a nice diagram." | Treat MIC as reliance-bearing method-interface description only when callers, planners, auditors, or substitutions depend on exposed, forwarded, or encapsulated interactions. |

#### B.1.5:7.1 - Consequences And Rationale

B.1.5 buys deterministic method composition without confusing method, method description, work occurrence, resource ledger, and assurance argument. The practitioner sees what is being composed by order and typed joins, what is spent by performed work, and what is later assessed by assurance.

The cost is explicitness: submethods, order apparatus, typed joins, adapters, interface exposure, and assurance hooks must be named before the composite method can be relied on. That cost prevents hidden brittleness at joins and accidental external dependencies at method boundaries.

The rationale is the old strict distinction in updated ontology. Order is semantic but not structural parthood. A method can be a non-agentive holon, but a step label, graph node, phase, source section, or work part is not a method part until the `U.Method` object is recovered. `Gamma_method` composes ways of doing; `Gamma_work` accounts resources; B.3 evaluates assurance; B.2 handles whole reidentification when the composed method participates as a new whole.

