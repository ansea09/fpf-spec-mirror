---
chunk_kind: "child"
pattern_id: "E.22"
pattern_title: "Improvement-Oriented Quality-Read Question Framing"
section_id: "E.22:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.22/E.22__012_sota-echoing.md"
commit_sha: "a0c90e3bbfcc0285893cc5bb9d4a88fcd224f00e"
heading_path:
  - "E.22 — Improvement-Oriented Quality-Read Question Framing"
  - "E.22:11 — SoTA-Echoing"
line_start: 68611
line_end: 68622
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

### E.22:11 - SoTA-Echoing

`E.22:11` uses `SoTA` in the E.8 sense: current best-known problem-solving practice for the local read-framing question. A row may mention older lineage only to name the inherited invariant that current practice still uses; lineage does not carry SoTA by itself. Current references are used only for the local read-framing problem named in the row.

| Claim | Current SoTA anchor and retained lineage | Local adoption | Non-use boundary |
|---|---|---|---|
| Quality reads need multidimensional, diagnostic, actionable movement rather than one overall judgement. | Current anchors: `LLM-Rubric: A Multidimensional, Calibrated Approach to Automated Evaluation of Natural Language Texts` (ACL 2024), `Human-aligned long-form evaluation (HALF-Eval): Framework for assessing AI-generated content and improvement` (2025), and `RubricEval: A Rubric-Level Meta-Evaluation Benchmark for LLM Judges in Instruction Following` (`arXiv:2603.25133`, 2026) treat rubric quality, multidimensional evaluation, calibration, meta-evaluation, and actionable feedback as live evaluation problems rather than as one score. | `QualityReviewFindingRow`, object-under-improvement evaluation effects, and `absorptionRead` make returned findings name expected quality movement, correction direction, closure test, and discharge evidence; absorption reports quality impact, not only applied or not-applied disposition. | This does not make `E.22` an automated evaluator, LLM judge, benchmark harness, or content-scoring method. |
| Feedback must connect desired condition, current condition, and next action. | Current anchors: `Can LLM feedback enhance review quality? A randomized study of 20K reviews at ICLR 2025` (`arXiv:2504.09737`, Review Feedback Agent) and `FeedEval: Pedagogically Aligned Evaluation of LLM-Generated Essay Feedback` (`arXiv:2601.04574`, ACL ARR 2026 January submission) retain specificity, actionability, validity, and improvement guidance as live quality dimensions. Retained lineage: Hattie and Timperley plus Sadler for the desired-condition, current-condition, and next-action invariant. | `QualityReadQuestionFrame` names purpose, floor or desired improvement aim, expected result form, and first repair or improvement result before the object-under-improvement evaluation reads values. | This does not turn FPF reviews into educational assessment or require a teaching cycle for every small edit. |
| Evaluation questions must be derived from the declared purpose; otherwise values answer the wrong question. | Current anchors: `LLM-Rubric` (ACL 2024), `RUBICON: Rubric-based Evaluation of Domain-Specific Human-AI Conversations` (2024), `HALF-Eval` (2025), and `RubricEval` (`arXiv:2603.25133`, 2026) make task-domain-specific criteria and rubric-level validity live evaluation concerns. Retained lineage: GQM and GQM+Strategies for deriving questions and measures from goals. | `QualityReadPurposeSelection` precedes coordinate reading; a reviewer cannot infer exceptional-improvement questions from a bare "review this" prompt, and a value result is inadmissible when the question belongs to a different object-under-improvement evaluation. | This does not import software-measurement programs, numeric measures, or a GQM document set into ordinary quality reads. |
| Multi-criteria improvement needs explicit trade-offs and non-dominated alternatives. | Current anchors: `The Architecture Tradeoff and Risk Analysis Framework (ATRAF): A Unified Approach for Evaluating Software Architectures, Reference Architectures, and Architectural Frameworks` (`arXiv:2505.00688`, 2025) and `Multi-criteria design methods in facade engineering: State-of-the-art and future trends` (2024) continue the quality-attribute trade-off line for systems and architecture evaluation. Retained lineage: MCDA, Pareto-front reasoning, and ATAM for explicit trade-off points. | `paretoTradeoffRead`, `TradeoffProtectionSet`, protected qualities, and non-dominated improvement wording keep quality improvement from collapsing into one score or one forced winner. | This does not require formal optimization, utility functions, quantitative MCDA, or an architecture-evaluation method for ordinary FPF review. |
| Proxy optimization can make the intended value worse even when visible values improve. | Current anchors: `Goodhart's Law in Reinforcement Learning` (ICLR 2024), current catastrophic-Goodhart reward-misspecification work (NeurIPS 2024), and `RubricEval` (`arXiv:2603.25133`, 2026) show that optimizing a proxy, reward, or weak rubric can degrade the intended value. Retained lineage: Manheim and Garrabrant's Goodhart taxonomy. | `paretoTradeoffRead`, protected qualities, `CC-E22-10`, and `CC-E22-15` require the read to ask what became worse before stopping, especially when visible coordinates, popularity, adoption, review count, or discharge count could be mistaken for quality. | This does not make `E.22` a predictive model of Goodhart mechanisms, adoption model, or AI safety evaluation. |
| OEE/NQD and improvement loops need proposal-shaped candidate changes before generation or candidate change. | Current QD anchor: `A survey on Quality-Diversity optimization: Approaches, applications, and challenges`, Swarm and Evolutionary Computation 100:102240 (2026). Retained lineage: OEE/QD archive and front practice, plus feedback-as-next-action review traditions. | `candidateImprovementProposalRead` can return one proposed candidate change or a bounded proposal portfolio. Each row names object-under-improvement evaluation pressure, expected movement, affected locus, protected trade-off, closure test, and neighbour exit before `E.23`, `C.18`, `C.19`, `G.5`, `G.9`, or `G.11` consumes it. | This does not make `E.22` a candidate generator, candidate-change policy, selected-set publisher, parity harness, or refresh orchestrator. |
