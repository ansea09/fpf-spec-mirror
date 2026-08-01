---
chunk_kind: "child"
pattern_id: "C.28"
pattern_title: "CausalUse-CAL: Causal-Use Questions, Causality-Ladder Rungs, Identification and Realizability"
section_id: "C.28:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28/C.28__002_use-this-when.md"
commit_sha: "1eb56cd0cfd6dccad65143e03d28509373bd8dd5"
heading_path:
  - "C.28 — CausalUse-CAL: Causal-Use Questions, Causality-Ladder Rungs, Identification and Realizability"
  - "C.28:0 — Use This When"
line_start: 56946
line_end: 57059
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

### C.28:0 - Use This When

Use `C.28` when a claim is being used causally:

- "method A improves result";
- "users who received intervention X had better outcomes";
- "this practice is fair";
- "the agent chose optimally";
- "the model simulates what would have happened";
- "the system can collect counterfactual data";
- "this benchmark shows a causal method is better";
- "this policy should be deployed because it would have changed the outcome".

Use `C.28` especially when the claim must distinguish:

- observed association;
- intervention or action effect;
- counterfactual comparison;
- direct counterfactual-rung data collection;
- identified counterfactual estimate;
- simulation-only counterfactual output;
- causal policy class;
- causal fairness use;
- causality-ladder parity in method comparison.

**Not this pattern when.** If no causal use is claimed, keep the work in the neighboring pattern: `C.16` for measurement, `C.27` for temporal trend or rate-change adequacy, `B.3` for assurance result, `A.10` for evidence graph reference, `G.9` for ordinary parity, `C.11` for local choice, `C.19` for pool policy, `C.24` for call planning, or `C.26` for a surviving quantum-like modeling cue after ordinary causal explanations have been tried.

**Activation boundary.** `C.28` activates at `CausalUseActivation`: causal wording changes what the claim makes admissible for publication, choice, deployment, assurance, audit, benchmark, or support treatment. The trigger is admissible downstream use, not the presence of a causal-looking word. If the wording is only exploratory prose and no causal use governed by `C.28` is made, rewrite to association, trend, measurement, or simulation-only wording and stop.

Exploratory causal-looking prose is not a `CausalUseActivation` by itself. A note may say that a relation is plausible, worth probing, or suggested by traces and still remain in `C.16`, `C.27`, `A.10`, `C.11`, `C.19`, `C.24`, `G.5`, or `G.9` until the text makes a causal use governed by `C.28` admissible. The moment the text makes publication, choice, deployment, assurance, audit, benchmark, or support treatment depend on causal support, `C.28` governs the causal-use boundary.

#### C.28:0.1 - What Goes Wrong If Missed

A causal-looking phrase backed only by association, proxy, simulation-only, or rhetorical support gets promoted into a causal use that requires a named `C.28` support basis and verdict.

Correlation becomes intervention effect. Interventional proxy becomes counterfactual fairness. A simulation becomes realized counterfactual-rung evidence. A benchmark compares methods across different causality-ladder rungs and still publishes one scalar superiority claim. An agentic policy is called optimal without saying whether it is a natural behavior policy, an interventional policy, or a counterfactual policy.

The practical error is laundering: the reader sees causal language but cannot recover what rung, estimand, evidence basis, and supported use are actually admissible.

#### C.28:0.2 - What This Buys

`C.28` gives FPF one cheap first stop for causal use.

The first useful result is not a heavy record. It is one small causal-use triage that says whether causal use is present, which causality-ladder rung is being used, what comparator or counterfactual is in play, what causal support-basis triage value supports it, and what the next supported use is.

Durable cards and profiles appear only when the claim needs them. The pattern buys explicit causal discipline without turning every causal word into a paperwork exercise.

#### C.28:0.3 - First-Minute Questions

`C.28` in 60 seconds is the operational entry into `CausalUseTriageRecord`:

1. Detect whether the claim reaches `CausalUseActivation`: it changes what publication, choice, deployment, assurance, audit, benchmark, or support treatment is admissible.
2. Stop with `nextCausalUseAction.cheapStop` if the claim only reports association, trend, description, measurement, or simulation-only output.
3. If causal use is live, fill `targetCausalityLadderRung`, `comparatorOrCounterfactualRef`, and `causalSupportBasisTriageValue`.
4. Fill `supportedUse: CausalUseSupportStatement` and `unsupportedUse: CausalUseUnsupportedStatement` as one action pair.
5. Fill `nextCausalUseAction: CausalUseNextAction`: choose `cheapStop` or escalate only when the claim is decision-bearing, publication-bearing, assurance-bearing, fairness-bearing, benchmark-bearing, or reusable.

#### C.28:0.4 - First Output

The first output is a `CausalUseTriageRecord`:

```text
CausalUseTriageRecord:
  causalUse: yes | no | unclear
  targetCausalityLadderRung?: CausalityLadderRung
  comparatorOrCounterfactualRef?
  causalSupportBasisTriageValue: CausalSupportBasisTriageValue
  supportedUse?: CausalUseSupportStatement
  unsupportedUse?: CausalUseUnsupportedStatement
  nextCausalUseAction: CausalUseNextAction
```

```text
CausalUseNextAction:
  cheapStop:
    stopNoCausalUse |
    publishAssociationOnly |
    rewriteAsTrendOrAssociation |
    keepSimulationOnlyModelUse |
    downgradeCausalWording |
    abstainFromCausalUse |
    selectNeighborPattern
  escalateOnlyIfUseDependsOnCausalSupport:
    openLocalCausalUseQuestionCard |
    openDurableCausalUseQuestionCard |
    buildCausalIdentificationProfile |
    buildCounterfactualSamplingRealizabilityProfile |
    planCausalUseEvidenceDesign |
    openCausalFairnessUseAuditCard |
    openCausalMethodRungParityRecord
```

```text
CausalSupportBasisTriageValue =
  observationalAssociationSupportBasis |
  interventionalActionSupportBasis |
  realizedCounterfactualSampleSupportBasis |
  identifiedCounterfactualEstimateSupportBasis |
  simulationOnlyCounterfactualOutputBasis |
  missing
```

`cheapStop` values are terminal or downgrade actions. They close the local causal-use question for now by saying what narrower use remains admissible, which neighboring pattern governs the remaining non-causal question, or that causal use is declined. `escalateOnlyIfUseDependsOnCausalSupport` values are record-opening actions. They are admissible only when the supported-use and unsupported-use boundary cannot safely carry the reader's next action by itself.

If this first output cannot be written honestly, the causal-use claim is not ready.

`CausalUseSupportStatement` is one concrete causal-use action the current support makes admissible, such as publish association-only wording, use a bounded interventional estimate for a named decision, deploy only under a named policy constraint, run a fairness audit under a named causal estimand, or compare methods only inside one declared causality-ladder rung. It is not a confidence label, graph name, method name, or generic "evidence exists" phrase.

`CausalUseUnsupportedStatement` is the matching concrete causal-use action the current support does not make admissible, such as intervention-effect wording, realized counterfactual sample wording, causal fairness certification, causal policy optimality, cross-rung benchmark superiority, or release use or deployment use. The supported and unsupported statements travel as a pair so the reader can act without inferring the boundary from prose tone.

The triage record may be the final causal-use record. Triage lines are enough when they block the overclaim and tell the reader what narrower use remains admissible. Do not open a local card merely because the word "cause", "effect", or "counterfactual" appears.

The triage `causalSupportBasisTriageValue` field is the first-pass local field for `CausalEvidenceSupportBasis | missing`. If a claim escalates beyond triage, the value must be refined to `CausalEvidenceSupportBasis`; `missing` becomes `unsupportedUse`, `CausalUseSupportVerdict = unsupported`, or `abstain`.

