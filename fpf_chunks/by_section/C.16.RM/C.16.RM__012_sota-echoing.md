---
chunk_kind: "child"
pattern_id: "C.16.RM"
pattern_title: "Repair a Measurement Model or Arrangement"
section_id: "C.16.RM:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.RM/C.16.RM__012_sota-echoing.md"
commit_sha: "31f4cb0b7f8000e0115098b50b44f80c8c36a671"
heading_path:
  - "C.16.RM — Repair a Measurement Model or Arrangement"
  - "C.16.RM:11 — SoTA-Echoing"
line_start: 53686
line_end: 53695
dependencies:
  - "B.5.MPC.R"
  - "B.5.RR"
  - "C.11.DUA"
  - "C.16"
  - "C.16.IR"
  - "C.16.MR"
  - "C.28"
  - "C.29.2"
keywords:
---

### C.16.RM:11 - SoTA-Echoing

**Practice question and selected answer.** How should one change a measurement whose current model, calculation or arrangement fails the receiving question? Select a contribution-specific repair, compare what it would resolve, and stop at an adequate result. The serious alternatives are a known applicable correction, a more detailed model, or more observations under the unchanged procedure. A known sufficient correction remains the cheaper route. The selected comparison is useful when repetition preserves the defect or extra model detail adds an undetermined influence. In :5.1 the already available on/off contrast resolves the beam contribution; in :5.2 changing loading yields a sufficient bound without identifying every parameter. Changing equipment can cost more than calculation, so its value depends on availability and the wanted conclusion.

**Model and apparatus alternatives.** [Dounas-Frazer and Lewandowski (2018), §2 and §§4.1–4.3](https://arxiv.org/pdf/1805.10334) explains iterative comparison and revision of physical-system and measurement-system models and apparatus. Its optics cases distinguish controlling unwanted light, avoiding saturation and revising response models. **Adapt** these alternatives into :4.2–4.4's choice of repair location and conditions. The paper's educational investigations support these modeling moves in experimental physics; they do not establish universal transfer or the effectiveness of the present cross-case Method.

**Adequacy and computational comparison.** [JCGM GUM-6:2020, §12](https://www.bipm.org/documents/20126/2071204/JCGM_GUM_6_2020.pdf) distinguishes comparisons with reference situations, computational tests using generated data, fit over the intended range and the adequacy of a simpler model. **Adapt** those distinctions in :4.2 and :4.5: select a comparison for the contribution and claim being repaired. Section :4.3 applies C.11.DUA to its attainable value and cost. The numerical cases are constructed demonstrations; the source does not supply their instrument laws or performed observations.

The integrated repair sequence, target continuity and return through a useful conclusion are conceptual synthesis. Reopen the choice when a cheaper remedy settles the same question, a changed condition invalidates the correction, or a comparison reveals a consequential influence left outside the model.

