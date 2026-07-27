---
chunk_kind: "child"
pattern_id: "C.28"
pattern_title: "CausalUse-CAL: Causal-Use Questions, Causality-Ladder Rungs, Identification and Realizability"
section_id: "C.28:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28/C.28__013_sota-echoing.md"
commit_sha: "66e732dfef7a4a93ff23eec43b3f759a6664652d"
heading_path:
  - "C.28 — CausalUse-CAL: Causal-Use Questions, Causality-Ladder Rungs, Identification and Realizability"
  - "C.28:11 — SoTA-Echoing"
line_start: 57423
line_end: 57441
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
  - "Pearl Causal Hierarchy"
  - "Structural Causal Model"
  - "association"
  - "causal diagram"
  - "causal estimand"
  - "causal evidence support basis"
  - "causal fairness"
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

### C.28:11 - SoTA-Echoing

| SoTA claim | Practice implication | Source anchors | FPF adoption |
| --- | --- | --- | --- |
| Causal reasoning separates seeing, doing, and imagining. | A claim must declare `CausalityLadderRung` before support is judged. | Pearl, SCM, and PCH: [On Pearl's Hierarchy and the Foundations of Causal Inference](https://causalai.net/r60.pdf). | Adopted as `observationalAssociationRung`, `interventionalActionRung`, `counterfactualComparisonRung`. |
| Lower-rung data generally underdetermines higher-rung questions. | No unsupported causality-ladder climb. | Pearl causal hierarchy and identification tradition: [On Pearl's Hierarchy and the Foundations of Causal Inference](https://causalai.net/r60.pdf). | Adopted as `CC-C28-3`. |
| Counterfactual sampling realizability is operational and partial. | Some counterfactual-rung distributions can be directly sampled; some cannot; some are bounded. | Raghavan and Bareinboim: [Counterfactual Sampling Realizability](https://openreview.net/forum?id=uuriavczkL), [technical report](https://causalai.net/r113.pdf). | Adopted as `CounterfactualSamplingRealizabilityProfile`. |
| Counterfactual randomization is `U.Work` over an SCM with action primitives. | Realized counterfactual-rung data collection needs `U.Work`, action primitives, graph constraints, and guards. | Forney, Bareinboim, Pearl: [Counterfactual Randomization](https://causalai.net/r39.pdf). | Adopted as `CC-C28-5` and evidence-design fields. |
| Counterfactual data can change what is identifiable or bounded. | Identification profiles must make realized counterfactual data, identification methods, and bound changes explicit rather than treating all data regimes as one scalar source. | Raghavan and Bareinboim: [Counterfactual Sampling Realizability](https://openreview.net/forum?id=uuriavczkL); Forney, Bareinboim, Pearl: [Counterfactual Randomization](https://causalai.net/r39.pdf). | Adopted as `availableDataRegimeSetRef`, `realizedCounterfactualDataRefs`, `counterfactualDataIdentificationMethodRef`, and `counterfactualDataBoundRef`. |
| Counterfactual graphical models require named graph forms and calculus. | Graph form, separation criterion, and calculus must be visible for counterfactual support. | Yang and Bareinboim: [A Hierarchy of Graphical Models for Counterfactual Inferences](https://causalai.net/r130.pdf); Correa and Bareinboim: [Counterfactual Graphical Models](https://proceedings.mlr.press/v267/correa25a.html). | Adopted as `CausalGraphRepresentationKind`, `GraphSeparationCriterionKind`, and `CausalInferenceCalculusKind`; `doCalculus` and `ctfCalculus` are controlled calculus values, not free-form hooks. |
| Potential outcomes and target-trial emulation operationalize intervention-effect claims. | Applied intervention claims need target population, eligibility, treatment strategies, assignment/time-zero, follow-up, outcome, contrast, estimand, and analysis plan. | Rubin: [Estimating Causal Effects of Treatments](https://www.ets.org/research/policy_research_reports/publications/article/1974/hrbx.html); Hernan/Wang/Leaf: [Target Trial Emulation](https://jamanetwork.com/journals/jama/fullarticle/2799678). | Adopted as `U.PotentialOutcomeContrast` and `TargetTrialProtocolRecord`. |
| Target-trial emulation from observational data needs mapping and reporting, not only protocol naming. | Eligibility, strategies, assignment and time-zero, follow-up, outcomes, residual confounding, and sensitivity analyses and additional analyses must be mapped from observational data to the target trial. | Hernan/Wang/Leaf: [Target Trial Emulation](https://jamanetwork.com/journals/jama/fullarticle/2799678). | Adopted as `TargetTrialEmulationMappingRecord`. |
| Causal ML estimation is not the same as identification or prediction. | Estimator, nuisance models, orthogonal score, cross-fitting, overlap/positivity, sensitivity, and uncertainty must be visible when estimation validity is claimed. | Chernozhukov et al.: [Double/debiased machine learning for treatment and structural parameters](https://academic.oup.com/ectj/article/21/1/C1/5056401). | Adopted as `CausalParameterEstimationProfile`. |
| Causal support may not transport across populations or domains without assumptions. | Source populations, target populations, source contexts, target contexts, selection diagrams, domain-shift assumptions, and transport formula or bridge must be named. | Pearl and Bareinboim: [Transportability of Causal and Statistical Relations](https://cir.nii.ac.jp/crid/1360298345422626304). | Adopted as `CausalTransportabilityProfile`. |
| AI causal work often cannot assume causal variables are already given. | Learned or selected causal variables need a representation record. | Scholkopf et al.: [Toward Causal Representation Learning](https://is.mpg.de/en/publications/scholkopfetal21). | Adopted as `CausalVariableRepresentationRecord`. |
| Causal representation support depends on intervention validity, invariance, abstraction fidelity, query preservation, and shift handling. | A learned representation must not silently become a causal variable for every query or domain. | Scholkopf et al.: [Toward Causal Representation Learning](https://is.mpg.de/en/publications/scholkopfetal21). | Adopted as causal representation validation hooks in `CausalVariableRepresentationRecord`. |
| Sequential causal games and causal RL make counterfactuality policy-relevant. | Natural behavior, interventional, and counterfactual policies, sequential horizons, adaptive policies, unit-history conditioning, and transportability must be distinguished. | Maiti and Bareinboim: [Sequential Causal Games](https://causalai.net/r145.pdf); Bareinboim/Forney/Pearl: [Bandits with Unobserved Confounders](https://papers.nips.cc/paper/5692-bandits-with-unobserved-confounders-a-causal-approach); Forney/Pearl/Bareinboim: [Counterfactual Data-Fusion for Online Reinforcement Learners](https://proceedings.mlr.press/v70/forney17a.html). | Adopted as `CausalActionPolicyClass` and `OffPolicyCausalEvaluationProfile` hooks. |
| Causal fairness is not only metric choice. | Fairness claims must declare causal rung, path or estimand where live, and supported fairness use. | Plecko and Bareinboim: [Fairness-Accuracy Trade-Offs: A Causal Perspective](https://causalai.net/r107.pdf). | Adopted through `D.5` relation and `CausalFairnessUseAuditCard`. |

