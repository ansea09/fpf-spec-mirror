---
chunk_kind: "child"
pattern_id: "C.28"
pattern_title: "CausalUse-CAL: Causal-Use Questions, Identification, and Realizability"
section_id: "C.28:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28/C.28__002_use-this-when.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "C.28 — CausalUse-CAL: Causal-Use Questions, Identification, and Realizability"
  - "C.28:0 — Use This When"
line_start: 56213
line_end: 56293
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

**Not this pattern when.** If no causal statement or causal evidential reliance is current, stay with the direct pattern: `C.16` for measurement, `C.27` for temporal change, `A.10` for an evidence path, `C.11` for choice, `C.19` for live-pool policy, `C.24` for call planning, `D.5` for bias or fairness audit, or `G.9` for ordinary parity.

**Activation condition.** C.28 is needed when causal support changes the statement relied on by a downstream publication, choice, deployment, audit, assurance, policy evaluation, or benchmark. C.28 decides only the causal-support boundary. The downstream pattern still decides whether to publish, choose, deploy, certify, assure, or abstain.

**Simulation boundary at entry.** A report that only describes simulator output and makes no causal use exits to ordinary model or simulation handling. Simulator output offered as support for an effect, counterfactual, policy, fairness, benchmark, or evidence claim stays in C.28 and must name the model, assumptions, validation, supported causal use, and unsupported use.

#### C.28:0.1 - What Goes Wrong If Missed

- association becomes an intervention-effect claim;
- a changed metric becomes causal fairness;
- a simulated trace becomes realized counterfactual evidence;
- an estimated number is treated as proof that its estimand was identified;
- support for one population or environment is transported to another without an endpoint or assumption; or
- a support verdict is mistaken for permission to publish, deploy, or certify.

#### C.28:0.2 - What This Buys

The cheap result states the question, rung, available support components, the common validity threat that matters now, the causal statement supported, the statement not supported, and the next useful step. Heavy profiles appear only when identification, estimation, counterfactual-sampling realizability, actual sampling evidence, transport, target-trial emulation, causal policy evaluation, representation learning, or fairness work is actually current.

#### C.28:0.3 - First-Minute Questions

1. What exact causal-use question is being asked, and which claim-bearing episteme states it?
2. Is the intended statement observational, interventional, or counterfactual?
3. What is actually available: an evidence path and empirical data regime, an identification or bound result, an estimate, a prospective counterfactual-sampling realizability result, dated sampling Work plus resulting data, or a simulation result?
4. Which common validity problem could overturn the use: intervention definition or consistency, time order, confounding, overlap, interference, selection or missingness, measurement, or transport?
5. What causal statement or evidential reliance is supported now, and what stronger statement is not?
6. Does the downstream pattern have enough basis to make its own decision, or should it abstain, downgrade, or request more evidence?

#### C.28:0.4 - First Output

The first output may be only this triage:

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

`supportedUse` means the causal statement or evidential reliance supported under the named limits. It is not a permission or command. `unsupportedUse` states the nearby stronger causal statement or reliance that the evidence does not support.

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

**Adjacent simulation examples.** “The simulator produced these traces” with no causal reliance returns `keepNonCausalSimulationUse`. “The simulated traces support what would happen under policy P” remains inside C.28 and needs `simulationResultRef`, model assumptions, validation, supported use, and unsupported use.

