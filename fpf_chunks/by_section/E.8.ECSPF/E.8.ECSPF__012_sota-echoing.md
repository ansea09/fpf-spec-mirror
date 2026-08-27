---
chunk_kind: "child"
pattern_id: "E.8.ECSPF"
pattern_title: "FPF Pattern Publication Form for Evaluation Guidance"
section_id: "E.8.ECSPF:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8.ECSPF/E.8.ECSPF__012_sota-echoing.md"
commit_sha: "322625be006f38158e4e7d600f662558f03df77a"
heading_path:
  - "E.8.ECSPF — FPF Pattern Publication Form for Evaluation Guidance"
  - "E.8.ECSPF:11 — SoTA-Echoing"
line_start: 72305
line_end: 72319
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

**Source-use convention and qualification.** The current-source decisions below are qualified through 2026-08-15 for the identified editions and this publication-form question. Each source is used only for the content named in its row. Reopen the smallest affected row when a new edition, successor, or materially better competitor changes that adopted content, its scope, or its currentness; a bibliographic change alone does not reopen the pattern.

| Source and stable identity | Adopted content | Change made here | Boundary | Reopen condition |
|---|---|---|---|---|
| [*BenchmarkCards: Large Language Model and Risk Reporting* (arXiv:2410.12974)](https://arxiv.org/abs/2410.12974) | Structured documentation of benchmark properties, including targeted risks and evaluation methodology, to support informed benchmark selection. | When published evaluation guidance relies on a benchmark, its source basis identifies the benchmark properties that affect coordinate or evidence selection. | BenchmarkCards documents benchmark properties. It does not define the whole evaluation process or prescribe how to measure and interpret a result. | Reopen this use if a successor changes which benchmark properties are needed for informed selection. |
| [*Evaluation Cards: An Interpretive Layer for AI Evaluation Reporting* (arXiv:2606.09809)](https://arxiv.org/abs/2606.09809) | Composition of benchmark metadata, evaluation-run data, and model metadata into one interpretable reporting layer, with reader-sensitive interpretation. | The publication form keeps benchmark description, run evidence, evaluated-object metadata, and the evaluation result distinguishable when those values are required. | This is the 2026 *Evaluation Cards* paper. A separate 2025 proposal called *EvalCards* is not a source here unless its content is deliberately selected and identified. | Reopen if the reporting layers or their interpretive use materially change. |
| [*Holistic Evaluation of Language Models* (HELM, arXiv:2211.09110)](https://arxiv.org/abs/2211.09110) | Standardized scenario-and-metric comparison, multi-metric visibility, stated coverage and missingness, and inspectable prompts and completions. | The pattern publishes the declared scenario or use, metric or coordinate meanings, missingness, and evidence needed for comparison instead of a bare aggregate. | HELM is a language-model evaluation suite, not a general FPF publication method. | Reopen if HELM's comparison discipline is superseded for the adopted scenario, metric, or evidence use. |
| [*VHELM: A Holistic Evaluation of Vision Language Models* (arXiv:2410.07112)](https://arxiv.org/abs/2410.07112) | The HELM comparison discipline extended to vision-language models, with modality-relevant aspects and standardized prompting, inference, metrics, and released generations. | A claimed cross-modality evaluation must publish the modality-specific use, procedure, and evidence that actually affect its coordinates. | Only the vision-language extension is adopted; VHELM does not justify claims about every evaluated object or modality. | Reopen if a successor changes the adopted vision-language procedure or exposes a missing modality boundary. |
| [*AHELM: A Holistic Evaluation of Audio-Language Models* (arXiv:2508.21376)](https://arxiv.org/abs/2508.21376) | The HELM comparison discipline extended to audio-language models across audio-relevant aspects, with standardized prompts, inference parameters, metrics, and released outputs. | An audio-language evaluation must publish the audio-specific use, procedure, and evidence that change its coordinates. | AHELM is an audio-language source, not an agent-evaluation source and not evidence for unrelated modalities. | Reopen if a successor changes the adopted audio-language procedure or exposes a missing audio boundary. |
| [*A survey on Quality-Diversity optimization: Approaches, applications, and challenges* (2026, DOI 10.1016/j.swevo.2025.102240)](https://doi.org/10.1016/j.swevo.2025.102240) | Current overview, for this narrow question, of QD feature or descriptor spaces, local quality and objective heads, diversity, containers, comparison or dominance, and evaluation metrics. | The publication form keeps dimensions, comparison rules, and protected trade-offs visible when an aggregate would hide loss. | QD is optimization over a declared feature space, not a universal evaluation architecture. A bounded scalarization remains separately declared with its use, loss, and non-use boundary. | Reopen if a newer synthesis changes the QD comparison used here or if this pattern claims more than the narrow non-scalar lesson. |

Model-card literature and classic pattern-language literature remain historical lineage for intended-use reporting and action-guiding publication. The retained publication lesson is concrete: put recognition and the first evaluation use before coordinate tables. This lineage is not presented as current-best evidence for the question. Current FPF `E.8` supplies the internal authoring rule and is not an external SoTA source.

