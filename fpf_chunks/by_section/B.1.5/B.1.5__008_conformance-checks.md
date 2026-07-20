---
chunk_kind: "child"
pattern_id: "B.1.5"
pattern_title: "Gamma_method - Order-Sensitive Method Composition and Work Enactment"
section_id: "B.1.5:6"
section_title: "Conformance Checks"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5/B.1.5__008_conformance-checks.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "B.1.5 — Gamma_method - Order-Sensitive Method Composition and Work Enactment"
  - "B.1.5:6 — Conformance Checks"
line_start: 35042
line_end: 35060
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

### B.1.5:6 - Conformance Checks

| Check | Requirement |
| --- | --- |
| `CC-B1.5-1` | Every claimed method part is recovered as a `U.Method` value before method-holon composition is admitted. |
| `CC-B1.5-2` | Step wording, description nodes, plan items, work occurrences, file modules, graph edges, and source wording are not method parts by position or wording. |
| `CC-B1.5-3` | Serial, parallel, guarded, iterative, fallback, adapter, and typed-join relations are method-composition or method-relation claims, not structural component parthood. |
| `CC-B1.5-4` | The composite method states whole-level preconditions, effects, invariants, accepted inputs and outputs, failure conditions, and work-facing acceptance relation. |
| `CC-B1.5-5` | Interface exposure distinguishes exposed, forwarded, and encapsulated interactions when outside reliance depends on the method boundary. |
| `CC-B1.5-6` | `U.MethodDescription`, `U.WorkPlan`, `U.Work`, mechanism, formal substrate, mathematical lens, evidence, and publication-use claims remain with their direct patterns. |
| `CC-B1.5-7` | If whole-method identity is not recovered, the claim is lowered to `MethodRelationStructure@BoundedContext` or another neighboring object without demoting `U.Method` as a holon kind. |
| `CC-B1.5-8` | When the composite method needs whole reidentification or emergence-family explanation, use `B.2` in addition to B.1.5. |
| `CC-B1.5-9` | A work part is not evidence of a submethod unless the method-side candidate is recovered as `U.Method`; temporal slices, episodes, event-log segments, telemetry intervals, engine strokes, detector components, and work-plan items stay with their direct patterns until that recovery is made. |
| `CC-B1.5-10` | Order-sensitive composition that relies on order semantics names the `B.1.4` order apparatus, including `OrderSpecRef`, context hash, partial-order soundness, or equivalent order evidence when current. |
| `CC-B1.5-11` | Typed joins show capability-continuity evidence as input/output, pre/post, adapter, bridge, or equivalence claims without turning those signatures into `U.Capability` instances. |
| `CC-B1.5-12` | Reliance-bearing composite boundaries publish MIC or equivalent exposure lines and performed work honours only the exposed or forwarded interactions unless the method is revised. |
| `CC-B1.5-13` | Resource costs, yields, dissipation, telemetry, and resource ledgers are handed to `U.Work`, `B.1.6`, and evidence patterns; B.1.5 may point to them but does not aggregate them. |
| `CC-B1.5-14` | Assurance hooks name cutsets, fragile joins, adapter points, CL-sensitive mappings, and envelope or scope refs for B.3; apparent super-additivity is returned to B.2-family whole reidentification instead of being averaged into the method. |

