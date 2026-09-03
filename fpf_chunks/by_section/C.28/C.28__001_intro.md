---
chunk_kind: "child"
pattern_id: "C.28"
pattern_title: "CausalUse-CAL: Causal-Use Questions, Identification, and Realizability"
section_id: "C.28:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28/C.28__001_intro.md"
commit_sha: "59c455329e49715c64dc1b16f22c1efba6a3cf6f"
heading_path:
  - "C.28 — CausalUse-CAL: Causal-Use Questions, Identification, and Realizability"
  - "C.28:intro — Intro"
line_start: 56495
line_end: 56508
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

## C.28 - CausalUse-CAL: Causal-Use Questions, Identification, and Realizability

> **Type:** Calculus (C)
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain-name.** Causal-use calculus.

**Intent.** Help a practitioner decide what a causal-looking claim is supported to say, under which limits, and which narrower statement remains when the support is insufficient.

**Primary EntityOfConcern.** One exact causal-use question. The claim, estimand or contrast, evidence paths, identification result, estimate, sampling-realizability result, performed sampling and resulting data, simulation result, support result, and downstream decision remain separately identified.

**Not a physical ontology.** This pattern does not define causation in the world or replace domain science. It supplies a practical interface for using causal evidence and models without promoting association, simulation, or a graph label into a stronger causal claim.

