---
chunk_kind: "child"
pattern_id: "C.28"
pattern_title: "CausalUse-CAL: Causal-Use Questions, Causality-Ladder Rungs, Identification and Realizability"
section_id: "C.28:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28/C.28__008_bias-annotation.md"
commit_sha: "9a9a42e4d154021ca3f7415e0009a4214832f65f"
heading_path:
  - "C.28 — CausalUse-CAL: Causal-Use Questions, Causality-Ladder Rungs, Identification and Realizability"
  - "C.28:6 — Bias-Annotation"
line_start: 57769
line_end: 57782
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

### C.28:6 - Bias-Annotation

`C.28` is mainly a causal-discipline and anti-overclaim pattern for decision-bearing causal use. One part of that work is catching language laundering, but the larger job is to keep causal reasoning, evidence design, realizability, policy evaluation, fairness use, and benchmark parity from silently borrowing a `C.28` support basis, support verdict, or admissible-use value they do not actually have.

Common biases:

- **Causal prestige bias.** A result sounds more important when phrased causally, so under-supported evidence gets overused.
- **Simulation laundering.** A simulated counterfactual is treated as observed or realized counterfactual-rung evidence.
- **Metric proxy bias.** A fairness or performance proxy is treated as a causal result without rung and estimand.
- **Benchmark scalarization bias.** A method comparison collapses different causal rungs, estimands, or transport assumptions into one score.
- **Graph sufficiency bias.** A named graph is treated as enough without assumptions, data regime, calculus, and admissible use.

The repair is not to ban causal language. The repair is to recover the live causal question, choose the least-committing admissible causal use supported by the available evidence, and then either downgrade, bound, design a causal-evidence plan with the required `C.28` support basis, open identification or realizability work, or abstain.

