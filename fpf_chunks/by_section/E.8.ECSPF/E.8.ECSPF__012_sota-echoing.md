---
chunk_kind: "child"
pattern_id: "E.8.ECSPF"
pattern_title: "Evaluation CharacteristicSpace FPF Pattern Publication Form"
section_id: "E.8.ECSPF:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8.ECSPF/E.8.ECSPF__012_sota-echoing.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "E.8.ECSPF — Evaluation CharacteristicSpace FPF Pattern Publication Form"
  - "E.8.ECSPF:11 — SoTA-Echoing"
line_start: 55215
line_end: 55221
dependencies:
  - "A.19.ECS"
  - "C.25"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9.DA"
  - "F.18"
keywords:
---

### E.8.ECSPF:11 - SoTA-Echoing

| Claim | Current practice line | Adoption in E.8.ECSPF | Boundary |
|---|---|---|---|
| Evaluation rubrics are useful only when criteria, value meanings, and use context are explicit. | Current reporting anchors: BenchmarkCards/EvalCards practice for evaluation-card structure, HELM/VHELM/AHELM-style suite reporting for scenario, metric, and raw-result transparency, and model-card lineage for intended-use and performance-characteristic reporting. | The publication form must publish evaluated object kind, use, coordinate meanings, missingness, and worked cases before checklist closure. | `E.8.ECSPF` is not a benchmark harness or automated evaluator. |
| Multicriteria evaluation needs non-scalar comparison and trade-off visibility. | Current QD overview: `A survey on Quality-Diversity optimization: Approaches, applications, and challenges`, Swarm and Evolutionary Computation 100:102240 (2026); retained design lineage: MCDA and quality-diversity practice for dimensions, dominance, and trade-offs when one total score would hide important loss. | The publication form keeps coordinate values, protected trade-offs, and status meanings distinct. | Scalarization belongs only to an exact neighbouring pattern or explicitly declared local method. |
| Pattern publication must remain action-guiding. | Pattern-language practice is retained as lineage/problem pressure for practical guidance in recurring situations; current FPF `E.8` supplies the governing publication-form rules. | The publication form keeps recognition text and first read before coordinate tables. | `E.8.ECSPF` does not replace `E.8`; it specializes it for evaluation-characteristic-space patterns. |
