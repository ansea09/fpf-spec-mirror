---
chunk_kind: "child"
pattern_id: "A.3.4"
pattern_title: "U.Transformation: Bounded Change Under Conditions"
section_id: "A.3.4:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.4/A.3.4__009_conformance-checklist.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "A.3.4 — U.Transformation: Bounded Change Under Conditions"
  - "A.3.4:7 — Conformance Checklist"
line_start: 7670
line_end: 7686
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.3"
  - "A.3.1"
  - "A.3.2"
  - "A.3.3"
  - "A.6.0"
  - "A.6.1"
  - "A.6.5"
  - "A.6.F"
  - "A.7"
  - "B.3"
  - "C.2.1"
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "C.30.ASV"
  - "C.32.P2S"
  - "E.18"
  - "E.18.1"
  - "E.18.2"
  - "E.20"
  - "E.24"
keywords:
  - "bounded change"
  - "functioning"
  - "input/output conditions"
  - "transformation"
  - "transformation-flow structure"
  - "transformed entity"
  - "transformer"
---

### A.3.4:7 - Conformance Checklist

| Check | Conformance statement |
| --- | --- |
| `CC-A34-1` | The `TransformationCore` identifies the transformed object, bounded context, initial condition, post-state condition or delta, transformation relation, and boundary condition. |
| `CC-A34-2` | Participation and check slots are considered and each receives an open-world disposition: filled, unknown or not recovered, not asserted, not current for this claim, or used to lower or block a claim that depends on the missing value. |
| `CC-A34-3` | The transformed object is typed through its governing pattern, with A.1 used for entity, holon, or system source discipline where relevant. |
| `CC-A34-4` | Method, method description, mechanism, work plan, work occurrence, dynamics episteme, temporal aspect, temporal-claim adequacy, evidence, result, source, gate, decision, assurance, publication, and refresh or reopen values keep their own governing patterns while filling participation and check slots in the transformation ontic. |
| `CC-A34-5` | A `C.2.1` episteme may carry claims about the transformation, one transformation slot, one slot filler, or a relation among those values, but descriptions and publications of a transformation are not treated as the transformation itself. |
| `CC-A34-6` | Time, rate, rhythm, cadence, effort, inertia, freshness, validity-window, or ordering wording uses `C.27.TA` for positive temporal aspects and `C.27` for temporal-claim adequacy. |
| `CC-A34-7` | Formal or mathematical structure uses `A.6.0`, `A.6.1`, `C.29`, or the direct mathematical pattern before it is used as a transformation law, formal relation, or evidence relation. |
| `CC-A34-8` | Evidence, assurance, gate, result acceptance, and decision authority are not inferred from `TransformationCore` or from a `C.2.1` episteme about the transformation. |
| `CC-A34-9` | The identity-plus-participation slot relation follows `A.6.5` SlotKind/ValueKind/RefKind discipline; dependent patterns may cite `U.Transformation`, filled identity slots, or specific participation and check slots without copying the full slot relation or turning their own values into identity slots. |
| `CC-A34-10` | Functional-transformation uses recover `TransformerRef?`, `InputConditionOrPortRefs?`, `OutputConditionOrPortRefs?`, `FunctioningRef?`, and `TransformationFlowStructureRef?` when those claims are current; none is silently left to A.6.F, C.30.ASV, or E.18 as an outside reference. |
| `CC-A34-11` | A system/candidate system may be said to perform a functional transformation at a flow point only when the system or candidate system, `TransformerRole@Context`, bounded transformation, input/output or port boundary, and flow location are named or explicitly marked unknown/not-current. |
| `CC-A34-12` | Algorithm wording is recovered as `U.Method`, `U.MethodDescription`, formal substrate, mechanism, work, or evidence according to the current claim; it is not treated as software-only and not used as proof that transformation occurred. |

