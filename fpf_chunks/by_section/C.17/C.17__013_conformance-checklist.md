---
chunk_kind: "child"
pattern_id: "C.17"
pattern_title: "Characterising Generative Novelty and Value"
section_id: "C.17:11"
section_title: "Conformance checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.17/C.17__013_conformance-checklist.md"
commit_sha: "322625be006f38158e4e7d600f662558f03df77a"
heading_path:
  - "C.17 — Characterising Generative Novelty and Value"
  - "C.17:11 — Conformance checklist"
line_start: 48628
line_end: 48647
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
  - "C.11.CRC"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "E.10.LRN"
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

### C.17:11 - Conformance checklist

| ID | Requirement |
| --- | --- |
| `CC-C17-1` | The result identifies the bearer, comparison basis, objective or must-criterion, supported difference or coordinate, consequence, evidence, and limit needed by its use. |
| `CC-C17-2` | A qualitative result stops before scores, reusable objects, or Work detail when none is needed. |
| `CC-C17-3` | Every selected characteristic has a declared Characteristic, Scale, polarity, admissible operations, missingness rule, and evidence route under one selected A.19 space and A.19.ECS specification. |
| `CC-C17-4` | Novelty identifies the finite corpus and inclusion rule, source editions, comparison window, Method, distance definition, coordinate construction and resulting Scale, calibration, uncertainty, scope, evidence, and use. The `1 - max similarity` construction requires calibrated `[0,1]` similarity results or a declared lawful normalization to that range. When representations or observations are compared instead of the bearers, the result identifies both, the describing, projection, measurement, or other support relation, a compatible corpus basis or stated mapping, and relevant loss. When the value is load-bearing, the evidence includes an appropriate robustness diagnostic such as nearest-neighbour inspection, corpus/Method sensitivity, or an invariance ablation; the input inventory alone is not robustness evidence. |
| `CC-C17-5` | Surprise identifies one model episteme and its separate training basis, modeled sample unit, encoding, size treatment, and discrete probability or continuous measure. A cross-bearer comparison uses a justified common extent, declared per-unit or code-length normalization, or another calibrated rule; otherwise the raw result stays basis-local. Use-Value identifies its objective or criterion; an improvement or gain also identifies its baseline and comparison or counterfactual Method. ConstraintFit identifies the must-constraints and their sources. AttributionIntegrity identifies the applicable duty set, the source or rule used to determine applicability, Scale, missingness rule, and evidence for each duty it evaluates. An empty applicable-duty set produces no numeric ratio; omit the characteristic or return explicit `not applicable`, distinct from an unresolved applicable duty. |
| `CC-C17-6` | Each coordinate is either a complete C.16 measurement result or a C.2.1 non-measurement ascription under an explicit rule. A displayed number alone fails. |
| `CC-C17-7` | Aggregate result, optional profile payload, representation or publication form, optional record, and any dated assessment Work remain distinct. |
| `CC-C17-8` | Novelty is paired with Use-Value or ConstraintFit for approval-facing use; must-constraint failure remains an eligibility failure unless an independently valid exception applies. |
| `CC-C17-9` | Dominance names the characteristic subset, Scale compatibility, polarity, eligibility conditions, and comparison rule. Frontiers are computed from that rule; scalarization is explicit and primitive coordinates remain available. |
| `CC-C17-10` | Every used retained-set or applied reading identifies its bearer or set, local rule and Scale, and evidence. `Diversity_P`, Illumination, retained-set readings, and Work readings do not silently become selection rules or characteristics of a different bearer. |
| `CC-C17-11` | Uncertainty, evidence, time window, model or corpus drift, and any cross-source or cross-scale loss are visible at the claim that depends on them. |
| `CC-C17-12` | Dated overall-assessment Work is asserted only with its actual System, assignment, Method enactment, Work extent, and evidence. Do not infer an A.6.1 operation application from those facts. When an exact application or binding is separately claimed, satisfy the current A.6.1 application account and cite that application. Coordinate-measurement Work remains separate. |
| `CC-C17-13` | Use C.17 to report characteristics and comparison results, C.18 for generation plus Archive and Front maintenance, C.19 for pool policy, G.5 for selector-facing declarations, and C.11 for choices. |
| `CC-C17-14` | The seven retired predecessor heads are not used to create new kinds or actors. |
| `CC-C17-15` | A cold reader can tell what to inspect first, when to stop, and what additional evidence is required for the stronger branch. |

