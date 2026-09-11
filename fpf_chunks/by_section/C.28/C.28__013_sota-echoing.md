---
chunk_kind: "child"
pattern_id: "C.28"
pattern_title: "CausalUse-CAL: Causal-Use Questions, Identification, and Realizability"
section_id: "C.28:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28/C.28__013_sota-echoing.md"
commit_sha: "cda9087f48e0bce2c5f9d5f4389e7e025c7678f5"
heading_path:
  - "C.28 — CausalUse-CAL: Causal-Use Questions, Identification, and Realizability"
  - "C.28:11 — SoTA-Echoing"
line_start: 58062
line_end: 58077
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

### C.28:11 - SoTA-Echoing

**Which question does the available model answer?** In :4.4, the same observed alarm distribution gives `P(H=1 | S=0)=0.1`, while replacing the alarm mechanism gives `P(H=1 | do(S=0))=0.5` under the stipulated no-feedback model. Reusing the observational answer is cheaper but answers the wrong question when the user proposes to set the output. Mechanism replacement, as explained in [Pearl, Glymour and Jewell's corrected primer, p.55](https://bayes.cs.ucla.edu/PRIMER/mueller-edits-questions-pearl-etal-2016-primer-errata-pages-august2019.pdf), supplies the operation used in the second derivation.

This comparison selects :0.3's question distinction and :4.4's requirement for an identifying expression or derivation. The added cost is stating the causal mechanism and assumptions needed for the requested intervention, instead of relying on the joint distribution alone. If the requested statement is observational, its existing answer suffices. If the alarm initiates cooling, the later-load question requires the changed mechanism and time order; reopen the earlier intervention result.

**What supports a counterfactual-fairness conclusion?** The analysis by [Ma, Melnychuk, Frauen and Feuerriegel, 2026](https://proceedings.mlr.press/v323/ma26a.html) identifies two failures in counterfactual-fairness baselines: missing counterfactual-identifiability assumptions and inconsistent counterfactual estimation. Their analysis uses identification up to a measure-preserving indeterminacy and a compatible consistency condition. More of the same data does not generally supply either missing condition.

For a receiving fairness audit, an improved metric or a large dataset therefore leaves a different question from the counterfactual guarantee. Section :4.6 selects a separate identification result and, when the conclusion uses an estimate, its Method's consistency result before D.5 consumes the support. The additional work is justified by that stronger question; an associative disparity report can finish at its own rung. The source supplies this failure analysis and a method-specific remedy, so the consumed guarantee retains its assumptions and scope. Reopen the support when those assumptions, the estimator or the fairness question changes.

**How much interface is useful?** A domain analyst's ordinary causal report can already state a question, assumptions, result and limitations. For the self-selected-team comparison in :0.4, that short report is sufficient: C.28's thin path returns the association and the live confounding question. Requiring the complete specialist profiles would add target, model and result declarations unused by that conclusion.

When several receiving uses need the same conclusion, the alternative is repeatedly extracting its question and limits from a larger report. Sections :4.0–:4.2 instead provide references to the independently used results and one common support conclusion. This costs explicit identification of those results and their conditions. It can avoid copying an identification derivation, estimate or sampling construction into each receiver. Use that structure when the receiving work needs it; reuse an existing result directly when it already supplies the required information.

These are bounded selections for the illustrated questions. They preserve cheap prose, expose a mathematical difference when it changes the answer, and require stronger support for a stronger fairness claim. Reopen the selected form if it hides a live causal distinction or requires information that the receiving use does not consume.

