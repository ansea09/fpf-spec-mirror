---
chunk_kind: "child"
pattern_id: "E.21"
pattern_title: "FPF Pattern-Quality Evaluation CharacteristicSpace"
section_id: "E.21:10"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.21/E.21__012_sota-echoing.md"
commit_sha: "322625be006f38158e4e7d600f662558f03df77a"
heading_path:
  - "E.21 — FPF Pattern-Quality Evaluation CharacteristicSpace"
  - "E.21:10 — SoTA-Echoing"
line_start: 87776
line_end: 87794
dependencies:
  - "A.17-A.19"
  - "A.19.ECS"
  - "A.6.1"
  - "A.6.P"
  - "C.16"
  - "C.2.P"
  - "C.25"
  - "E.10"
  - "E.11"
  - "E.19"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9.DA"
  - "F.18"
  - "F.19"
  - "I.2"
keywords:
---

### E.21:10 - SoTA-Echoing

**Current source decision, qualified through 2026-08-19.** E.21's design problem is not “find a recent quality checklist.” It is to detect semantic and use defects without losing practitioner value, while keeping evaluator effort, replayability, multi-quality trade-offs, and stop conditions visible. Three current primary branches answer different parts of that problem: scientific validation of patterns, lightweight defect detection in natural-language requirements, and standardized holistic multi-metric evaluation. For the bounded decisions in their rows, they are SoTA-bearing branches; their useful parts are combined below, while their domain-specific machinery is not imported.

No external source validates E.21's nineteen-coordinate set or demonstrates inter-evaluator agreement for it. The set and its noncompensatory result architecture therefore remain a qualified FPF-local synthesis. E.21 requires pinned evidence and adjacent-value rationales so another evaluator can replay and challenge the judgment; it does not call that unmeasured property reliability or universal validation.

| Practice question | Exact source and source-use status | Adopted, adapted, or rejected effect in E.21 | Limit and reopen condition |
|---|---|---|---|
| What evidence can support a pattern-validation claim rather than a favorable review? | Riehle, Harutyunyan, and Barcomb, [*Pattern Discovery and Validation Using Scientific Research Methods*](https://doi.org/10.1007/978-3-662-70810-1_6) (final publication 2025), is a current primary SoTA-bearing source for the bounded pattern-validation branch. | **Adapt.** E.21 evaluates one edition for one use; stronger validity claims need separately declared expert checks, observed applications or case studies, or stronger fit-for-purpose research. Actual-use absence caps only values that claim such evidence. Reject the rule of three and reject calling one E.21 result universal validation. | The handbook method is costly and its reported studies are exploratory; it does not validate E.21. Reopen when a stronger current pattern-validation method changes the evidence needed for the value or validation boundary. |
| How can a multi-quality evaluation remain comparable and expose missing coverage and trade-offs? | Bommasani et al., [*Holistic Evaluation of Language Models*](https://doi.org/10.1111/nyas.15007) (2023), is a current primary SoTA-bearing source for the bounded standardized scenario-and-metric comparison branch, including explicit coverage gaps, multi-metric visibility, and released raw evidence. | **Adapt.** E.21 fixes use, reader, probes, and evidence conditions before comparing editions; names missing or underrepresented evidence; keeps every required coordinate visible; and retains replayable evidence refs. Reject the LM taxonomy, benchmark leaderboard, arithmetic aggregation, and any claim that standardized conditions alone establish evaluator agreement. | HELM evaluates language models, not pattern texts. Reopen if current evaluation research supplies a lower-cost comparison that preserves the same coverage, missingness, trade-off, and replay properties. |
| What can cheap defect detection contribute without replacing semantic review? | Veizaga, Shin, and Briand, [*Automated Smell Detection and Recommendation in Natural Language Requirements*](https://doi.org/10.1109/TSE.2024.3361033) (IEEE TSE 2024), is a current primary SoTA-bearing source for the bounded automated requirements-defect branch, tested on 2,725 requirements from 13 financial systems. | **Adapt.** A bounded smell, lexical, or checklist screen may seed suspect loci in `EvaluationEvidenceBasis` and reduce search cost. Reject treating that screen as a coordinate value, semantic-completeness proof, practitioner-use test, or substitute for the complete evaluation. | The reported detector is tied to natural-language requirements, Rimay patterns, and one industrial domain; it does not evaluate FPF pattern quality. Reopen if a current cross-domain method demonstrates broader semantic and use-defect coverage with declared limits. |
| What prevents an evaluation value from replacing the value it is meant to indicate? | Karwowski et al., [*Goodhart's Law in Reinforcement Learning*](https://proceedings.iclr.cc/paper_files/paper/2024/hash/6ad68a54eaa8f9bf6ac698b02ec05048-Abstract-Conference.html) (ICLR 2024), is a current primary source for one proxy-optimization branch. | **Adapt.** `ProxyForValueSubstitutionResistance`, protected qualities, and the stop rule ask what became worse. Reject all-`5`, discharge-count, or proof-apparatus targeting and do not generalize the paper's reinforcement-learning mechanism to every evaluation. | Reopen if later proxy-risk work changes the protected-value or early-stop rule used here, or a material proxy failure escapes the current probes. |
| How should measurement questions stay tied to the use that needs the answer? | [ISO/IEC/IEEE 15939:2017](https://www.iso.org/standard/71197.html), confirmed current in 2022, is a current standard reference rather than a primary SoTA source; GQM and GQM+Strategies remain software-measurement lineage. | **Adapt as a bounded reference.** Scope, reader, intended use, qualification window, and evidence need are fixed before values. Reject a convenient coordinate set selected first and rationalized after the result. | Reopen on a revised edition or a stronger cross-domain measurement practice that changes the purpose-to-question-to-evidence order used here. |
| Should optimizer-based multi-objective machinery define pattern-quality comparison? | Lin et al., [*Quality-Diversity Optimization as Multi-Objective Optimization*](https://arxiv.org/abs/2602.00478) (2026 preprint), is a current research comparator for set-based multi-objective optimization, not a SoTA-bearing pattern-evaluation source; MCDA, Pareto comparison, and ATAM remain lineage or domain-specific comparators. | **Reject the transfer.** Retain only the warning that scalarization can hide dimensions. E.21 uses an ordinal same-bearer bundle and declared dominance comparisons; it imports no QD archive, optimizer, scalarization, MCDA method, or software-architecture method. | Remove this comparator if it no longer changes the anti-scalarization boundary; reopen if E.21 later claims an optimizer or numeric aggregation. |
| Why must an evaluation result remain distinct from management and authority decisions? | NIST [AI Risk Management Framework 1.0](https://doi.org/10.6028/NIST.AI.100-1) (2023) is a current domain reference, not pattern-evaluation SoTA; NIST is revising it. | **Adapt only the separation.** E.21 supplies a pattern-quality result. Admission, assurance, safety, compliance, release, and authority decisions remain separate. Reject AI RMF vocabulary and domain evidence as proof of an FPF result. | Reopen when the revised NIST framework is published or a broader current source changes this non-overread boundary. |
| What makes feedback actionable rather than merely evaluative? | Sadler, [*Formative assessment and the design of instructional systems*](https://doi.org/10.1007/BF00117714) (1989), and Hattie and Timperley, [*The Power of Feedback*](https://doi.org/10.3102/003465430298487) (2007), remain education lineage, not current cross-domain SoTA. | **Retain as lineage.** Keep desired condition, current result, and possible next improvement distinct: `ShortRationale` states the present value, while finding or proposal rows carry later action. Reject praise or a score without an action-changing diagnosis. | Retain only while this distinction changes the E.21 result/proposal boundary; reopen from current feedback research when that action structure changes. |

The resulting practice decision is deliberately asymmetric: cheap screening may narrow where to look; the complete use-scoped evaluation constitutes the E.21 result; actual-use research is needed for stronger pattern-validation claims. That combination addresses detection cost, use-value preservation, trade-off visibility, and replayability without claiming that the FPF-local coordinate architecture has already been externally validated.

