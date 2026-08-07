---
chunk_kind: "child"
pattern_id: "E.22"
pattern_title: "Improvement-Oriented Quality Evaluation Question Framing"
section_id: "E.22:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.22/E.22__012_sota-echoing.md"
commit_sha: "2729cfe5a3e4a86da8632aabcb859488c06a2d51"
heading_path:
  - "E.22 — Improvement-Oriented Quality Evaluation Question Framing"
  - "E.22:11 — SoTA-Echoing"
line_start: 87386
line_end: 87397
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

| Claim | Exact source and status | Inherited contribution and limit | Local adoption and disciplined case |
|---|---|---|---|
| A rubric-level evaluation needs its own reliability check rather than trust in one aggregate judge verdict. | Tianjun Pan et al., *RubricEval: A Rubric-Level Meta-Evaluation Benchmark for LLM Judges in Instruction Following*, arXiv:2603.25133 (2026), and Hongli Zhou et al., *Toward Robust LLM-Based Judges: Taxonomic Bias Evaluation and Debiasing Optimization*, arXiv:2603.08091 (2026), are current preprints for automated LLM judging. | Pan et al. show that fine-grained rubric judging can remain inaccurate and variable; Zhou et al. test a taxonomy of twelve bias types across generative and discriminative judges. These works concern LLM judges and instruction-following benchmarks; they do not validate an FPF evaluation or generalize their numeric results to physical, medical, or organizational evaluation. | `QualityEvaluationUseDeclaration` separates the governing evaluation pattern, semantic Method when declared, selected space and criterion, ClaimScope, quality-model descriptions, evidence basis, result form, and qualification window. The **Floor evaluation** and **Exceptional improvement** slices require the named evaluation's full result form rather than an unqualified judge verdict. |
| Actionable formative feedback distinguishes the desired condition, current performance, and a move that can close the gap. | D. Royce Sadler, *Formative assessment and the design of instructional systems*, *Instructional Science* 18, 119-144 (1989), DOI 10.1007/BF00117714; John Hattie and Helen Timperley, *The Power of Feedback*, *Review of Educational Research* 77(1), 81-112 (2007), DOI 10.3102/003465430298487. Both are retained historical education lineages. | Sadler supplies the comparison between a quality standard and current work plus action by the learner; Hattie and Timperley synthesize goal, current progress, and next-step feedback questions. Their classroom evidence does not establish FPF kinds, project authority, or the quality of a proposed repair. | The frame keeps floor or aim, current object version, expected result form, and proposal or checked no-proposal result distinct. The **Absorption** slice reports changed quality rather than merely counting accepted feedback. |
| Measurement questions should be derived from an explicit purpose rather than selected first and rationalized later. | Victor Basili, Gianluigi Caldiera, and H. Dieter Rombach, *The Goal Question Metric Approach*, in *Encyclopedia of Software Engineering* (1994), retained historical lineage; Victor Basili et al., *Linking Software Development and Business Strategy Through Measurement*, *Computer* 43(4), 57-65 (2010), DOI 10.1109/MC.2010.108, a later software-organization extension. | GQM contributes the purpose-to-question-to-measure direction; GQM+Strategies makes the link to higher-level goals and rationale explicit. Both are software-measurement methods and do not supply E.22's holonic ontology, evaluation values, or cross-domain quality model. | `QualityEvaluationPurposeSelection` is fixed before the evidence-basis and result-form descriptions. In the **Physical-system proposal**, the vibration purpose is declared before choosing the Q-Bundle, coordinate, measurement evidence, or proposal form. |
| Multi-coordinate improvement needs set-valued alternatives and explicit trade-offs rather than one scalar winner. | Xi Lin et al., *Quality-Diversity Optimization as Multi-Objective Optimization*, arXiv:2602.00478 (2026), current preprint; Haoxiang Qin et al., *A survey on Quality-Diversity optimization: Approaches, applications, and challenges*, *Swarm and Evolutionary Computation* 100:102240 (2026), DOI 10.1016/j.swevo.2025.102240, current survey. | Lin et al. reformulate QD as a large multi-objective problem and use set-based scalarization; Qin et al. survey high-performing collections over descriptor spaces. These algorithmic results do not assign FPF archive, front, publication, or selection authority. | `paretoTradeoffEvaluation`, `TradeoffProtectionSet@Context`, and `CandidateImprovementProposalPortfolio@Context` preserve alternatives and protected coordinates. The **Proposal portfolio** and **Physical-system proposal** slices stop before selection; archive, front, pool, and selected-set claims remain with their direct patterns. |
| Optimizing a measure can damage the intended value through several different mechanisms. | Charles Goodhart, *Problems of Monetary Management: The U.K. Experience* (1975), retained historical monetary-control lineage; Donald T. Campbell, *Assessing the Impact of Planned Social Change*, Occasional Paper 8 (1976), retained social-indicator lineage; David Manheim and Scott Garrabrant, *Categorizing Variants of Goodhart's Law*, arXiv:1803.04585 (2018), later taxonomy; Jongwoon Choi, Gary Hecht, and William Tayler, *Lost in Translation: The Effects of Incentive Compensation on Strategy Surrogation*, *The Accounting Review* 87(4), 1135-1164 (2012), peer-reviewed experimental evidence. | Goodhart concerns control that changes an observed regularity; Campbell concerns corruption pressure on social indicators; Manheim and Garrabrant distinguish several overoptimization mechanisms; Choi et al. show managers treating a measure as the strategic construct. None says that every metric is invalid or supplies the intended value automatically. | The **Goodharted improvement** repair separates floor repair from substantive improvement, protects other qualities, rejects discharge count and all-`5` posture as value, and returns proxy-to-value repair to `E.13`. |
| Automated-judge mitigation is model-dependent and can itself require a declared guarantee or evidence profile. | Sadman Kabir Soumik, *Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines*, arXiv:2604.23178 (2026), current preprint; Benjamin Feuer, Lucas Rosenblatt, and Oussama Elachqar, *Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation*, arXiv:2603.05485 (2026), current preprint. | Soumik compares nine mitigations and reports model-dependent effects across four bias types; Feuer et al. define average bias-boundedness for specified judge settings. These results are benchmark- and model-bound and do not make any LLM judge generally unbiased. | `ExpectedEvaluationEvidenceBasis@Context` and the qualification window state what reliability support is actually claimed. The **Exceptional improvement** slice rejects style or proof apparatus that pleases an evaluator without improving the governed content. |
| OEE and NQD can use proposal-shaped quality pressure without collapsing proposal, candidate retention, and selection. | Xi Lin et al., *Quality-Diversity Optimization as Multi-Objective Optimization*, arXiv:2602.00478 (2026), current preprint; Haoxiang Qin et al., *A survey on Quality-Diversity optimization: Approaches, applications, and challenges*, *Swarm and Evolutionary Computation* 100:102240 (2026), DOI 10.1016/j.swevo.2025.102240, current survey. | The shared comparison question is how to preserve several high-performing alternatives across declared coordinates or descriptors. The sources do not say that an evaluation proposal is already a generated candidate, archive insertion, front update, or selected result. | `CandidateImprovementProposalRow@Context` names the expected later evaluation effect before generation or selection. E.22:4.6 and the **Proposal portfolio** slice keep C.17-C.19 and G.5 authority outside E.22. |

