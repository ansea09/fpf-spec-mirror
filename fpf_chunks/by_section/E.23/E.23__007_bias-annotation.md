---
chunk_kind: "child"
pattern_id: "E.23"
pattern_title: "Quality Improvement Loop Method"
section_id: "E.23:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/E.23/E.23__007_bias-annotation.md"
commit_sha: "c7ac61bbaa8d3c10165b1a5a4a350956c87d77c9"
heading_path:
  - "E.23 — Quality Improvement Loop Method"
  - "E.23:6 — Bias-Annotation"
line_start: 87681
line_end: 87696
dependencies:
  - "A.19.ECS"
  - "A.22.CGUS"
  - "C.17-C.19"
  - "C.32.P2S"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.9.DA"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
---

### E.23:6 - Bias-Annotation

This pattern biases FPF toward adaptive improvement with explicit re-evaluation. The bias is useful because many real objects improve only through feedback and revision.

The bias is bounded. One direct evaluation can close without a loop. Repetition is justified only by a scale-qualified `ExpectedEvaluationResultChange@Context` and acceptable cost and risk.

**Scope: limited.** The pattern covers repeated improvement of one declared object version under one rerunnable evaluation. It is not a universal account of change, learning, capability development, cultural evolution, publication, release, or project authorization; use the subject pattern for those claims.

| Lens | Declared bias and check |
|---|---|
| **Gov** | Favors an explicit evaluation, protected trade-offs, and a local stop or switch condition. Keep evaluation evidence separate from the decision, gate, publication, or release that may later use it. |
| **Arch** | Favors one bounded object-under-improvement loop with named exits to specialized Methods and neighboring patterns. Do not let the loop absorb capability development, cultural evolution, DPF authoring, archive, selection, parity, or refresh architecture. |
| **Onto-Epist** | Favors keeping a proposal, selected continuation, performed Work, changed object or Transformation, later evaluation, evidence, and result episteme distinct. Completion or a better score alone establishes none of the neighboring claims. |
| **Prag** | Favors rerunnable evidence and non-dominated improvement under cost, risk, and protected qualities. For a cheap one-pass question, a direct evaluation is preferable to maintaining a loop. |
| **Did** | Favors an ordinary first move and unlike worked cases before formal loop records. Loop language can invite readers to mistake a visible cycle for enduring Work or context, so the grounding and anti-patterns show the distinctions in use. |

