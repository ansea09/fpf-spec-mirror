---
chunk_kind: "child"
pattern_id: "E.8.ECSPF"
pattern_title: "Evaluation CharacteristicSpace FPF Pattern Publication Form"
section_id: "E.8.ECSPF:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8.ECSPF/E.8.ECSPF__012_sota-echoing.md"
commit_sha: "205de763b710fe9f2baecbcdae132ec8fdbbe38c"
heading_path:
  - "E.8.ECSPF — Evaluation CharacteristicSpace FPF Pattern Publication Form"
  - "E.8.ECSPF:11 — SoTA-Echoing"
line_start: 59033
line_end: 59042
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
  - "F.19"
keywords:
---

### E.8.ECSPF:11 - SoTA-Echoing

**Source-use convention.** This section uses source rows only where they change the publication form: evaluated object and use before checklist, coordinate meanings and missingness, worked cases, non-scalar comparison, protected trade-offs, or action-guiding recognition text. Reporting frameworks and standards are reference-only use unless they solve the publication-form problem named by value.

| Claim | Current practice line | Use of source and representative sources | Adoption in E.8.ECSPF | Boundary |
|---|---|---|---|---|
| Evaluation rubrics are useful only when criteria, value meanings, and use context are explicit. | Current reporting practice makes evaluation cards, scenario descriptions, metric meanings, raw-result visibility, intended use, and performance-characteristic reporting explicit. | **Current-practice and reference use.** BenchmarkCards and EvalCards are current evaluation-card reporting sources; HELM, VHELM, and AHELM are current suite-reporting sources for scenarios, metrics, inference settings, prompts, raw outputs, and comparable reporting; model cards are retained lineage for intended-use and performance-characteristic reporting. | The publication form must publish evaluated object kind, use, coordinate meanings, missingness, and worked cases before checklist closure. | `E.8.ECSPF` is not a benchmark harness, model-card schema, automated evaluator, or reporting standard. |
| Multicriteria evaluation needs non-scalar comparison and trade-off visibility. | Current QD and multicriteria practice keeps dimensions, dominance, trade-offs, objective heads, and diversity or descriptor choices visible when one total score would hide important loss. | **Current-best source use for QD overview in this narrow use, plus retained lineage.** `A survey on Quality-Diversity optimization: Approaches, applications, and challenges`, *Swarm and Evolutionary Computation* 100:102240 (2026), supplies the current QD overview used here. MCDA and older QD practice are retained lineage for dimensions, dominance, and trade-offs. | The publication form keeps coordinate values, protected trade-offs, and status meanings distinct. | Scalarization belongs only to an neighboring pattern governing the claim or explicitly declared local method. |
| Pattern publication must remain action-guiding. | Pattern-language practice treats a pattern as reusable action guidance for recurring situations, not as a static rubric table. | **Lineage and current FPF reference use.** Pattern-language practice is retained as lineage and problem pressure; current FPF `E.8` supplies the governing publication-form rules for recognition text, first useful move, worked cases, and relations. | The publication form keeps recognition text and first evaluation use before coordinate tables. | `E.8.ECSPF` does not replace `E.8`; it specializes it for evaluation-characteristic-space patterns. |

