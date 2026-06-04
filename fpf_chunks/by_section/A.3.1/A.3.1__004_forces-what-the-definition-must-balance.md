---
chunk_kind: "child"
pattern_id: "A.3.1"
pattern_title: "U.Method"
section_id: "A.3.1:3"
section_title: "Forces (what the definition must balance)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.1/A.3.1__004_forces-what-the-definition-must-balance.md"
commit_sha: "3d19010169827708d0bca36d0551af8323908640"
heading_path:
  - "A.3.1 — U.Method"
  - "A.3.1:3 — Forces (what the definition must balance)"
line_start: 5752
line_end: 5761
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.3"
  - "B.1"
  - "U.BoundedContext"
  - "U.Capability"
  - "U.Dynamics"
  - "U.PromiseContent"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.WorkPlan"
keywords:
  - "abstract process"
  - "how-to"
  - "procedure"
  - "recipe"
---

### A.3.1:3 - Forces (what the definition must balance)

| Force                                  | Tension we resolve                                                                                        |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Universality vs. specificity**       | One notion must cover welding, ETL, proofs, and schedulers, while letting each domain keep its idioms.    |
| **Representation vs. semantics**       | Many notations express the same “way of doing”; we need one semantic anchor across specs.                 |
| **Reusability vs. assignment**        | The *how* should be reusable regardless of *who* is assigned this time.                                  |
| **Compositionality vs. executability** | Methods compose (serial/parallel/choice/iteration), but execution may diverge due to conditions/failures. |
| **Determinism vs. search**             | Methods may be deterministic algorithms or constraint problems with admissible solution sets.             |

