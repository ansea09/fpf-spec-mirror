---
chunk_kind: "child"
pattern_id: "E.18.3"
pattern_title: "Constraint-Governed Transformation-Flow Unfolding Structure"
section_id: "E.18.3:8"
section_title: "Common Anti-Patterns and How to Avoid Them — Repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.3/E.18.3__010_common-anti-patterns-and-how-to-avoid-them-repairs.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "E.18.3 — Constraint-Governed Transformation-Flow Unfolding Structure"
  - "E.18.3:8 — Common Anti-Patterns and How to Avoid Them — Repairs"
line_start: 86949
line_end: 86963
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.PROD"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.22.CGUS"
  - "A.3.4"
  - "A.6.3.NAR"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.30.TFS-REL"
  - "C.32.CONWAY"
  - "C.32.P2S"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.18.3"
  - "E.18.NET"
  - "E.23"
  - "G.11"
  - "G.5"
keywords:
---

### E.18.3:8 - Common Anti-Patterns and How to Avoid Them — Repairs

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **P2W as launch permission** | A carry-through note or selected continuation is used to begin Work. | Apply the exact Method definition, A.15.2 plan test, A.15.5 readiness test, A.21 gate test or applicable permission rule required by the claim; none alone performs Work. |
| **Flow card as architecture decision** | A P2S flow card is treated as the decision or ADR. | Keep flow use in E.18.3 or C.32.P2S; use `C.32.PAD` and `C.32.ADR` for their exact distinct objects. |
| **Parallel specialization object** | Reciprocal refs, a context field or profile record create a generic CGUS plus another E.18.3 structure. | Keep one selected A.22 `U.Structure` and treat E.18.3 as an additional membership-and-use condition. |
| **Network graph as admitted slice** | Raw paths, edge labels, copied positions, or one global tag are inserted into a demonstration. | Select E.18.NET first, then reuse the same CGUS locus bindings and relation-reference epistemes through the complete A.22 network locator. |
| **One giant flow** | Independent development, production, use or evaluation flows are merged because a product or arrow connects them. | Preserve member identity and use exact cross-boundary occurrences in E.18.NET; keep valuations and internal subflow detail on one TFS. |
| **Wrapper connection relation** | `basisDependency`, `producedResult`, `comparisonPeer`, or a return arrow is treated as a universal E.18.3 relation. | State the exact question and use an exact supporting relation with its predicate definition and current facts; otherwise keep the values separate and stop. |
| **Guard label as relation occurrence** | A condition claim or a `GuardFail` emitted by `USM.CompareGuard` or `USM.LaunchGuard` is inserted into `relationReferenceEpistemeRefs[]` because its label contains guard. | Keep the claim with its test and current facts, or the E.18 event with its gate-assignment facts. Use a relation reference only for an independently defined exact obtaining relation occurrence. |
| **Evidence path as evidence** | A path through evidence-looking boxes or a broad evidence-use label is treated as sufficient evidence. | Use the applicable `A.10`, `B.3`, or `G.6` rule and cite the exact independently governed claim or relation that passes it; the label and path establish nothing by themselves. |
| **Intended realization as MethodDescription or Work** | A pattern ref, sequence, recommendation, imperative or filled block is said to describe a Method or perform the continuation. | Apply A.3.2 to an episteme about one admitted Method and A.15.1 to an exact dated occurrence; otherwise retain only the cue. |
| **Loop as improvement** | A retry or feedback loop is called quality improvement. | Use `E.23` only when object version, evaluation frame, repair, re-evaluation, stop, branch and return are current. |

