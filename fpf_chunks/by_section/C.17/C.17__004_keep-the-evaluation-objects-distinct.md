---
chunk_kind: "child"
pattern_id: "C.17"
pattern_title: "Characterising Generative Novelty and Value"
section_id: "C.17:2"
section_title: "Keep the evaluation objects distinct"
source_path: "FPF-Spec.md"
output_path: "by_section/C.17/C.17__004_keep-the-evaluation-objects-distinct.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "C.17 — Characterising Generative Novelty and Value"
  - "C.17:2 — Keep the evaluation objects distinct"
line_start: 48548
line_end: 48582
dependencies:
  - "A.0"
  - "A.1.1"
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.15.2"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.ECS"
  - "A.3.1"
  - "A.3.2"
  - "A.6.1"
  - "B.1.6"
  - "B.3"
  - "B.4"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "F.18"
  - "F.6"
  - "F.9"
  - "G.11"
  - "G.5"
  - "U.Mechanism"
keywords:
  - "ConstraintFit"
  - "Novelty"
  - "Use-Value"
  - "bounded quantitative result"
  - "evidence"
  - "incomparability"
  - "named comparison basis"
  - "qualitative-first evaluation"
  - "uncertainty"
---

### C.17:2 - Keep the evaluation objects distinct

| What the reader needs | C.17 treatment |
| --- | --- |
| Evaluation space | `CreativityCharacteristicSpace` is a local designator for one A.19 `U.CharacteristicSpace`. Its slots bind selected Characteristics to Scales and value sets. |
| Evaluation specification | One `C.2.1` episteme specializes `A.19.ECS` for the selected bearer kind and use. It states applicability, coordinate meanings, evidence and missingness rules, calibration, result shape, protected trade-offs, stop, and reopen conditions. |
| Comparison basis | A finite corpus or reference set, with inclusion rule, source editions, coverage boundary, and comparison window. Use a separate source-selection episteme when the selection must persist. |
| Similarity or measurement procedure | One `U.Method`, with a separate MethodDescription when needed. Identify the model, encoder, distance definition, invariances, calibration, and limits used by that Method. |
| Generative expectation | One model episteme and its separately recoverable training basis: members or selection rule, source editions, training window, preprocessing, and evidence. |
| Evaluated bearer | The design, episteme, System, dated Work, finite set, or change under its already established kind. *Creative outcome* may remain ordinary prose; it is not another kind. When a change or Work episode has no single result episteme, identify that actual bearer and cite the result-and-evidence bundle used by the claim instead of wrapping the bundle in a new outcome kind. |
| Coordinate result | One claim about the bearer, characteristic, scale value, scope, use, window, method or probe, basis, rationale, uncertainty, and evidence. |
| Aggregate result | One `CreativityEvaluationResult` episteme whose EntityOfConcern is the bearer and whose claims state only the bounded coordinate and comparison conclusion. |
| Optional profile | `CreativityProfile` is a local, non-arithmetic payload containing selected coordinate-claim references, their declared arrangement, and any current frontier or incomparability annotation. |
| Representation and publication | A table, chart, dashboard, or publication form represents or publishes the payload or result. It is not the payload or result. |
| Optional record | A separate `CreativityEvaluationRecord` episteme may package references to the configuration, results, profile, evidence, rendering, and actual Work for a named receiver. |
| Assessment occurrence | Dated Work exists only when an overall assessment actually occurred and its System, assignment, Method enactment, Work extent, and evidence are recoverable. Any claimed application of a Mechanism operation is a separate conditional fact under A.6.1. |

Changing a space slot, corpus membership or inclusion rule, model claims or training basis, objective, criterion, constraint, Scale meaning, scope, or window reopens only the coordinate claims that depend on that change and any aggregate conclusion that uses them.

#### C.17:2.1 - Retired predecessor heads

The following names no longer introduce root kinds:

| Retired head | Use instead |
| --- | --- |
| `U.CreativitySpace` | the selected A.19 CharacteristicSpace, locally called `CreativityCharacteristicSpace` when a short name helps |
| `U.CreativityProfile` | the optional local `CreativityProfile` payload, with any representation, publication form, or record identified separately |
| `U.ReferenceBase` | the finite corpus or reference set and, when needed, its source-selection episteme |
| `U.SimilarityKernel` | the Method used plus its model, encoder, distance definition, calibration, and limits |
| `U.GenerativePrior` | the model episteme and its separate training basis |
| `U.CreativeOutcome` | the bearer under its existing kind |
| `U.CreativeEvaluation` | the separately recoverable configuration, coordinate claims, aggregate result, optional payload and record, and any actual assessment Work |

Earlier results remain historical epistemes under their original editions. Relate an earlier and later result as editions only when both results and the continuity claim are recoverable; do not retype an old result merely because the current ontology is clearer.

