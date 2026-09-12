---
chunk_kind: "child"
pattern_id: "C.28"
pattern_title: "CausalUse-CAL: Causal-Use Questions, Identification, and Realizability"
section_id: "C.28:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28/C.28__009_conformance-checklist.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "C.28 — CausalUse-CAL: Causal-Use Questions, Identification, and Realizability"
  - "C.28:7 — Conformance Checklist"
line_start: 59040
line_end: 59060
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

### C.28:7 - Conformance Checklist

1. The concrete claim and exact causal-use question remain identifiable from entry to the supported statement and its limits.
2. Every reference required by the current use resolves to the exact question, target or result defined at :4.0; a sentence-level triage can finish without such references.
3. Data regime, identification, estimate, sampling realizability, performed sampling evidence, simulation, and transport remain distinct and may be combined.
4. A downstream decision uses the causal-support result within its stated limits and checks its remaining conditions under the receiving pattern, as required by :4.9.
5. An identified result cites an expression or derivation; a bounded result cites a bound; a nonidentified result cites an obstruction or witness.
6. A causal estimate cites an identification or explicit design-based result. Method-family details appear only when that Method is selected.
7. The common threat screen routes every live ordinary threat or lowers the result; it is not a mandatory dossier.
8. Non-causal simulator reporting and simulation-supported causal use take different routes at first entry.
9. A sampling-realizability result cites its decision Method, any derivation used, and the sampling construction or obstruction required by its status; `unclear` names the unresolved question. Counterfactual-quantity bounds remain in the separate identification result. A prospective result claims no Work or data.
10. Performed counterfactual-sampling support cites independently admitted dated Work and resulting data or evidence; it cites exact assignment-bound attribution only when the receiving support claim uses it. A WorkPlan or `realizable` label cannot satisfy this branch.
11. Before execution, evidence design cites a MethodDescription or WorkPlan only when used. When it cites performed Work, it identifies each precise performer under A.13 and the dated occurrence independently under A.15.1. Performed counterfactual sampling used as evidence also cites the resulting data through A.10. F.6 is required only when that account uses exact assignment-bound attribution.
12. Transport identifies every changed population/domain/environment/data-generating-regime endpoint separately from semantic schemes.
13. A counterfactual-fairness escalation exposes its additional identification assumptions and, when an estimate is used, estimation consistency before D.5 consumes it.
14. `CausalActionPolicyClass` identifies the specified rule or available family through :4.10's mechanism and information conditions; reductions, combinations and unresolved classifications stay explicit. Consumers use the same meaning and omit an unused field.
15. Every specialist field changes support, a downstream decision basis, evidence work, or a reopen condition.
16. A target-trial mapping result identifies the observational source and every protocol-to-data mapping, gap, residual-confounding assessment, and sensitivity mapping needed for its bounded use.
17. Every retained specialist result that can independently change support can enter `CausalSupportComponentRefs`; when it shapes further evidence, the evidence-design record can cite the same result without copying it.
18. The whole pattern remains understandable to a practitioner without requiring the formal graph vocabulary on the ordinary path.

