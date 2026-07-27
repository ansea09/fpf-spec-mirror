---
chunk_kind: "child"
pattern_id: "A.3.4.P"
pattern_title: "Transformation Ontic Precision Restoration"
section_id: "A.3.4.P:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.4.P/A.3.4.P__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "1f413fcd23f4ea26956a45d67dde57bb233f6ad9"
heading_path:
  - "A.3.4.P — Transformation Ontic Precision Restoration"
  - "A.3.4.P:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 8529
line_end: 8541
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

### A.3.4.P:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Cue word as ontology | "Pipeline", "process", "network", or "circuit" is treated as the FPF kind. | Recover the current object: `U.Transformation`, `TransformationFlowStructure`, mathematical description, method, work, publication, or direct subject pattern. |
| Replacement by smoother umbrella | "Process" is replaced with "flow" or "operation" without recovered kind. | Run the replacement through the same recovery. If the kind is still hidden, keep the row open. |
| Network head inflation | Frequent network or circuit wording becomes a peer durable head. | Use network or circuit as structure form, topology label, mathematical-expression family, domain label, or subject-domain system only when recovered by value. |
| Selected structure as transformation composition | Common membership in one flow, path, network, circuit, or pipeline is treated as a composite transformation, transformation-part relation, or proof of indivisibility. | Use `E.18` only to position, relate, or locate transformation loci and adjacent governed values. Ground every actual `U.Transformation` independently under `A.3.4`; common structure membership establishes neither composition, parthood, nor partlessness. |
| Workflow as performed work | A workflow diagram or process model is treated as dated work. | Use `A.3.2`, `E.18`, or `C.2.P.DR` for the description or structure; use `A.15.1` only for dated work. |
| Function as proof of behavior | A module, port, participant, role assignment, or "transformer" label is treated as proof of actual change or action. | Recover the actual transformation basis; for performed work, one exact Work occurrence admitted under `U.Work`, its covering `U.RoleAssignment`, direct `performedBy`, and the required separate work-to-change relation; otherwise the exact participant, operation-application, functioning, causal, or other direct actor-side relation. |
| Architecture influence as action | A manufacturing or certification organization, design organization, method or method family, toolchain, communication system, selected structure, or other value is called the actor because it constrained or enabled a candidate. | Recover the value's exact kind first, then only its exact architecture, work, communication, constraint, or candidate-synthesis relation. A method or method family is not a holon by label, the temporary influence-disposition field is no new relation, and influence alone proves no role, work, actor status, or transformation participation. |
| Publication as change | A diagram, proof, dashboard, or source span is treated as the changed object or change occurrence. | Use description, publication, evidence, or source-use pattern for the carrier and keep the transformation under `A.3.4`. |

