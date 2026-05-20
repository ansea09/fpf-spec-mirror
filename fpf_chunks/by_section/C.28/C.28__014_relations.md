---
chunk_kind: "child"
pattern_id: "C.28"
pattern_title: "CausalUse-CAL: Causal-Use Questions, Causality-Ladder Rungs, Identification and Realizability"
section_id: "C.28:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28/C.28__014_relations.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "C.28 — CausalUse-CAL: Causal-Use Questions, Causality-Ladder Rungs, Identification and Realizability"
  - "C.28:12 — Relations"
line_start: 47142
line_end: 47161
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

### C.28:12 - Relations


- `C.16` governs measurement and metrics. `C.28` activates only when a measurement is used causally.
- `C.27` governs temporal claim adequacy. `C.28` activates when temporal change is used as causal effect, intervention evidence, or counterfactual comparison.
- `A.10` governs evidence graph referring. `C.28` supplies causal evidence support basis and causal-use support refs for evidence paths.
- `A.2.4` governs evidence roles. `C.28` requires the evidence-role distinctions that keep `simulationOnlyCounterfactualOutputBasis`, `identifiedCounterfactualEstimateSupportBasis`, interventional evidence, and `realizedCounterfactualSampleSupportBasis` from being confused.
- `A.6` / `A.6.B` / `A.6.C` govern boundary, deontic, promise, commitment, utterance, contract-language, and L/A/D/E-classified claim language. `C.28` supplies only causal-use support when mixed boundary sentences claim causal effect or counterfactual support.
- `A.15` governs role, method, plan, and work alignment. `C.28` supplies the causal-use semantics for intervention assignment, target-trial emulation, counterfactual sampling work, and causal evidence collection.
- `B.3` governs trust and assurance. `C.28` supplies the causal-use verdict that `B.3` can degrade, bound, or abstain over.
- `C.11` governs decision theory. `C.28` supplies causal-use question and causal action-policy class when value, utility, regret, or optimality depends on causal rung.
- `C.19` governs explore/exploit pool policy. `C.28` supplies causal rung and policy/regime fields when exploration collects causal data or learns causal policy.
- `C.24` governs agentic tool use and call planning. `C.28` supplies `causalActionUseSpec` when calls select observation, intervention, counterfactual-rung evidence collection, or counterfactual policy conditioning.
- `D.5` governs bias audit and ethical assurance. `C.28` supplies causal fairness rung, estimand, support, and supported fairness use.
- `G.5` governs method dispatch and MethodFamily registry. `C.28` supplies causal method or policy class declarations when method dispatch compares causal methods.
- `G.9` governs parity and benchmarks. `C.28` supplies causal method rung parity.
- `G.11` governs refresh orchestration. `C.28` supplies causal-use support records whose realizability, identification, fairness, representation, off-policy, target-trial, and simulation-validation shifts can trigger refresh.
- `C.26` governs quantum-like modeling. `C.28` is a required causal exit before QL retention when the live question is intervention, causal effect, causal fairness, causal policy, counterfactual comparison, or counterfactual-rung-data realizability.


