---
chunk_kind: "child"
pattern_id: "C.28"
pattern_title: "CausalUse-CAL: Causal-Use Questions, Identification, and Realizability"
section_id: "C.28:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28/C.28__002_use-this-when.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "C.28 — CausalUse-CAL: Causal-Use Questions, Identification, and Realizability"
  - "C.28:0 — Use This When"
line_start: 58387
line_end: 58466
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

### C.28:0 - Use This When

Use `C.28` when a result is offered as support for a causal effect, intervention, counterfactual comparison, causal fairness claim, causal policy, causal benchmark, or causal explanation. Common cues include:

- “method A improves the outcome”;
- “users who received X did better, so X works”;
- “this policy would have prevented the failure”;
- “the model shows what would have happened”;
- “this fairness metric proves the intervention is fair”; and
- “this benchmark shows that one causal method is better”.

The cue opens a question, not a verdict. Ask what claim is being supported and what use of the evidence depends on that support.

**Not this pattern when.** If the task only reports a measurement, temporal change or model output without causal reliance, continue with that direct task. Section :4.11 locates the relevant neighboring pattern when a return is needed.


**Simulation at entry.** “The simulator produced these traces” can finish as a model-output report. “These traces support what would happen under policy P” opens C.28: identify the model, assumptions, validation and the causal use they support.

#### C.28:0.1 - What Goes Wrong If Missed

- association becomes an intervention-effect claim;
- a changed metric becomes causal fairness;
- a simulated trace becomes realized counterfactual evidence;
- an estimated number is treated as proof that its estimand was identified;
- support for one population or environment is transported to another without an endpoint or assumption; or
- a support verdict is mistaken for permission to publish, deploy, or certify.

#### C.28:0.2 - What This Buys

The first result is a supported statement with its limits and the next useful step. Section :4.0 locates additional support components by the question each answers; open a specialist profile only when its result is needed.

#### C.28:0.3 - First-Minute Questions

1. What is the concrete claim, and what causal question must be answered to rely on it?
2. Is the requested statement about an observed association, an intervention, or a counterfactual?
3. What observations, experiments, model assumptions or derived results are available?
4. Which live threat could overturn the conclusion: for example, confounding, time order, missing comparison cases, interference, measurement error or transfer to another population?
5. What statement is supported under those conditions, and what further evidence or calculation would change it?

#### C.28:0.4 - First Output

**Ordinary first result.** Suppose the available comparison says that self-selected teams using method A completed more tasks than teams not using it, while task difficulty and prior team capability were not controlled. Report the observed association; the claim that A caused the improvement remains unsupported by that comparison. The next useful question is whether a design or existing evidence can distinguish the method's effect from those rival explanations.

This sentence-level result can finish the task. When the triage must be reused, its local form is:

```text
CausalUseTriageRecord:
  causalUseQuestionRef?: CausalUseQuestionRef
  causalUse: yes | no | unclear
  targetCausalityLadderRung?: CausalityLadderRung
  comparatorOrCounterfactualRef?
  availableSupportCues?
  liveThreats?
  supportedUse?
  unsupportedUse?
  nextCausalUseAction
```

`supportedUse` states the causal statement or evidential reliance supported under the named limits. `unsupportedUse` states the nearby stronger statement or reliance left unsupported by that evidence.

```text
nextCausalUseAction =
  stopNoCausalUse |
  reportAssociationOnly |
  keepNonCausalSimulationUse |
  downgradeCausalWording |
  requestIdentificationOrBound |
  requestEstimate |
  requestCounterfactualSamplingRealizabilityCheck |
  requestPerformedSamplingEvidence |
  requestTransportCheck |
  requestEvidenceDesign |
  sendFairnessUseToD5BiasAuditReport |
  sendParityUseToG9 |
  abstainDownstream
```

Triage may be the final result when it blocks the overclaim and names the narrower statement. Do not open a durable object merely because a causal word appears.


