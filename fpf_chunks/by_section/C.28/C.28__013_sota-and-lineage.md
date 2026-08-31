---
chunk_kind: "child"
pattern_id: "C.28"
pattern_title: "CausalUse-CAL: Causal-Use Questions, Identification, and Realizability"
section_id: "C.28:11"
section_title: "SoTA and lineage"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28/C.28__013_sota-and-lineage.md"
commit_sha: "e400eab3757d60a8d05196046bed002dff1839e0"
heading_path:
  - "C.28 — CausalUse-CAL: Causal-Use Questions, Identification, and Realizability"
  - "C.28:11 — SoTA and lineage"
line_start: 56914
line_end: 56937
dependencies:
  - "A.10"
  - "A.15"
  - "A.2.4"
  - "A.3.2"
  - "A.6"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.19"
  - "C.24"
  - "C.26"
  - "C.27"
  - "D.5"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "CausalUseSupportResult"
  - "Pearl Causal Hierarchy"
  - "Structural Causal Model"
  - "association"
  - "causal diagram"
  - "causal estimand"
  - "causal fairness"
  - "causal support components"
  - "causal-RL evaluation"
  - "causal-use question"
  - "causality ladder"
  - "counterfactual"
  - "counterfactual sampling realizability"
  - "identification"
  - "intervention"
  - "off-policy causal evaluation"
  - "target trial"
---

### C.28:11 - SoTA and lineage

**Qualification window.** This comparison was reviewed through 2026-08-21. Reopen it when a current contribution is materially superseded, TARGET guidance changes, a specialist branch changes the minimum replay fields, or direct consumers need a different support-result contract.

| Status and live problem | Contribution used | Adopted, adapted, or rejected FPF move |
| --- | --- | --- |
| Lineage: seeing, doing, imagining, and identification | Pearl hierarchy and identification tradition, [On Pearl's Hierarchy and the Foundations of Causal Inference](https://causalai.net/r60.pdf) | Retain the three-rung distinction and no unsupported climb. This is history and foundation, not proof that one graphical school covers every domain. |
| Current counterfactual theory | Correa and Bareinboim, 2025, [Counterfactual Graphical Models](https://proceedings.mlr.press/v267/correa25a.html) | Name graph form and calculus when the derivation depends on them. Do not make the formalism part of ordinary triage or treat a graph label as a result. |
| Current reporting practice | TARGET Statement, BMJ 2025, [Reporting of observational studies explicitly emulating a target trial](https://www.bmj.com/content/390/bmj-2025-087179) | Retain causal question and estimand, assumptions, protocol-to-data mapping, estimate and precision, and sensitivity reporting. Reject the overread that complete reporting is identification or low risk of bias. |
| Current bounded transport research | NeurIPS 2025, [Causal Effect Estimation under Covariate Shift](https://proceedings.neurips.cc/paper_files/paper/2025/hash/795679e4056817ee71d37680939e980f-Abstract-Conference.html) | Keep identification and estimation under a named shift explicit. This does not replace the broader endpoint and assumption requirements for other transport problems. |
| Current sampling-realizability decision | Raghavan and Bareinboim, ICLR 2025, [Counterfactual Sampling Realizability](https://proceedings.iclr.cc/paper_files/paper/2025/hash/e59c4efcaed615db8911fecb84c1d51b-Abstract-Conference.html) | **Adopt:** make realizability a replayable prospective result with its decision Method and construction, bound, or obstruction. Reject the earlier C.28 collapse with WorkPlan, dated Work, or data. |
| Current Layer-3 identification and bounds | Raghavan and Bareinboim, 2026, [Causal Identification from Counterfactual Data: Completeness and Bounding Results](https://arxiv.org/abs/2602.23541) | **Adopt as composition, not collapse:** realized counterfactual data may feed a separate identification or bound result. Producing those data still needs dated Work and an evidence path to the result; realizability alone supplies neither data nor identification. |
| Lineage and current domain practice: potential outcomes | Rubin 1974 and later target-trial practice | Retain estimand, contrast, assignment/time zero, follow-up, outcome, and analysis plan. Use `PotentialOutcomeContrastRef`, not an unadmitted U-kind. |
| Conditional estimator family | Chernozhukov et al. 2018, [Double/debiased machine learning](https://academic.oup.com/ectj/article/21/1/C1/5056401) | Use orthogonal scores and cross-fitting only for a selected DML Method. Reject their use as universal estimation fields. |
| Current counterfactual-fairness limit | Ma et al., CLeaR 2026, [Consistent End-to-End Estimation for Counterfactual Fairness](https://proceedings.mlr.press/v323/ma26a.html) | **Adopt:** a supported counterfactual-fairness use exposes additional counterfactual-identifiability assumptions and estimation consistency. Infinite data does not repair either omission; D.5 receives a bounded or unsupported result when they are absent. |
| Lineage: causal representation | Schölkopf et al., [Toward Causal Representation Learning](https://is.mpg.de/en/publications/scholkopfetal21) | Retain intervention validity, invariance, abstraction fidelity, query preservation, and shift checks when learned causal variables are used. This broad source is lineage, not a claim that one representation is current-best for every domain. |
| Lineage: sequential causal policy | Maiti and Bareinboim, [Sequential Causal Games](https://causalai.net/r145.pdf), plus causal bandit and data-fusion work | Retain natural, interventional, counterfactual, and mixed policy distinctions and keep history, overlap, and transport visible. Do not infer policy optimality from replay reward. |
| 2026 domain-specific representation and policy alternatives | Mandyam et al., [CANDOR](https://proceedings.mlr.press/v333/mandyam26a.html), and Balashankar et al., [Domain Faithfulness through Counterfactually Robust Learning](https://proceedings.mlr.press/v323/balashankar26a.html) | **Reject as shared-interface additions:** imperfect counterfactual annotations, healthcare policy evaluation, subgroup rules, and representation/training choices materially affect their domain Methods, diagnostics, and supported use, but add no missing universal C.28 field. Keep them in method-specific detail and reopen only if a cross-domain result exposes a new minimum support distinction. |
| Lineage: fairness and accuracy | Plecko and Bareinboim, [Fairness-Accuracy Trade-Offs: A Causal Perspective](https://causalai.net/r107.pdf) | Retain the causal estimand and trade-off question, but do not use this lineage alone as current counterfactual-fairness support. The 2026 identification and consistency conditions above now bound D.5 consumption. |

**Why this combination is retained.** The 2025 realizability result answers whether samples can be produced; the 2026 completeness and bounding result answers what can be identified from realized Layer-3 data; the 2026 fairness result states extra conditions for one consequential downstream use. Keeping those results separate preserves their different questions while allowing explicit composition. The domain-specific 2026 lines improve selected Methods but do not dominate the small shared interface. This is the current non-dominated contract for a practitioner who needs a cheap causal stop plus replayable specialist results.

**Synthesis boundary.** No source above establishes the whole C.28 architecture. The orthogonal support components, common threat screen, small support-result interface, support/authority split, and cross-pattern consumer contract are a bounded FPF synthesis. Validate them through filled cases and consumer replay; reopen when they hide a real causal distinction, impose unused apparatus, or fail a practitioner.

