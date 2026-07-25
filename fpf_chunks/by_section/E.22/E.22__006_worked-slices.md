---
chunk_kind: "child"
pattern_id: "E.22"
pattern_title: "Improvement-Oriented Quality Evaluation Question Framing"
section_id: "E.22:5"
section_title: "Worked slices"
source_path: "FPF-Spec.md"
output_path: "by_section/E.22/E.22__006_worked-slices.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "E.22 — Improvement-Oriented Quality Evaluation Question Framing"
  - "E.22:5 — Worked slices"
line_start: 84378
line_end: 84390
dependencies:
  - "A.19.ECS"
  - "C.17-C.19"
  - "C.25"
  - "E.10"
  - "E.19"
  - "E.2.DA"
  - "E.21"
  - "E.23"
  - "E.9.DA"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
---

### E.22:5 - Worked slices

**Floor evaluation.** A reviewer is asked whether one pattern is ready for ordinary use. The frame names `E.21`, purpose `floorEvaluation`, the declared floor, and the expected `E.21` result form. The result is a complete `E.21` coordinate table with `ShortRationale` and `EvaluationEvidenceBasis`, not a narrative "looks fine."

**Exceptional improvement.** A pattern already passes the floor. The frame asks for substantive non-dominated improvements for named coordinates while protecting usability and related-pattern fit. The result returns proposal rows for content improvements such as missing worked cases, source-currentness carry-through, mature-comparator discharge, deletion of displaced apparatus, or relation cleanup, plus checked no-candidate dispositions for coordinates where no non-dominated content move remains. It does not ask the evaluator to make every coordinate `5`.

**Absorption.** External review returns many suggestions. The frame asks for `absorptionEvaluation`. The result says which changes improved coordinates, which were already satisfied, which introduced trade-offs, and which belong outside the evaluation.

**Proposal portfolio.** A candidate improvement campaign needs alternatives before editing. The frame asks for `candidateImprovementProposalEvaluation`. The result returns bounded proposal rows; selection or generation stays with the pattern that governs that claim and is not decided by the evaluation frame.

**Physical-system proposal.** A vibration evaluation of `PumpAssembly@Prototype-3` finds excessive RMS vibration at one operating point. The proposal's `reviewLocationDescriptionRef` points to that evaluation row. Its `correctionTargetRef` points to `ImpellerBladeGeometryDescription@v3`, the exact design episteme that would change; the measurement row is not the correction target. The affected coordinate is the declared RMS-vibration coordinate. The coarse proposal effect is `raiseTowardExceptional`, `kindRestorationCheckDisposition=notTriggered`, and the trade-off set includes efficiency and manufacturability. If the proposal is selected for a repeated loop, E.23 adds a scale-qualified `ExpectedEvaluationResultChange@Context`. Manufacturing a new impeller remains dated work under A.15 rather than an E.22 result.


